#!/usr/bin/env python3
"""Effets sonores du Reel LIMO, synthétisés et calés sur les repères de index.html.

Usage (depuis projet-hyperframes/) :
    python3 outils/sfx.py        ->  assets/audio/sfx.wav

- Aucun échantillon externe : chaque son est fabriqué ici (libre de droits).
- Déterministe : graine fixe, même fichier à chaque exécution.
- Les instants viennent du bloc JSON <script id="cues"> de index.html,
  le même que celui qui pilote les animations : si on décale une scène,
  on relance ce script et le son suit.
Dépendances : numpy, scipy.
"""
import json
import os
import re
import wave

import numpy as np
from scipy.signal import butter, fftconvolve, sosfilt

SR = 48000
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
html = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()
C = json.loads(re.search(r'<script type="application/json" id="cues">(.*?)</script>', html, re.S).group(1))
DUR = C["duration"]
N = int((DUR + 1.5) * SR)
out = np.zeros((2, N))
rng = np.random.default_rng(7)


# ---------------------------------------------------------------- outils
def t_axis(d):
    return np.arange(int(d * SR)) / SR


def place(sig, at, gain=1.0, pan=0.0):
    """Pose un son mono à l'instant `at` (s), panoramique -1 (gauche) … 1 (droite)."""
    i = int(round(at * SR))
    left, right = np.cos((pan + 1) * np.pi / 4), np.sin((pan + 1) * np.pi / 4)
    st = np.vstack([sig * left, sig * right]) * np.sqrt(2)
    n = min(st.shape[1], N - i)
    if n > 0 and i >= 0:
        out[:, i : i + n] += gain * st[:, :n]


def env_exp(t, tau, att=0.002):
    return np.exp(-t / tau) * np.clip(t / att, 0, 1)


def bp(x, lo, hi):
    return sosfilt(butter(2, [lo / (SR / 2), hi / (SR / 2)], btype="band", output="sos"), x)


def hp(x, f):
    return sosfilt(butter(2, f / (SR / 2), btype="high", output="sos"), x)


def lp(x, f):
    return sosfilt(butter(2, f / (SR / 2), btype="low", output="sos"), x)


def noise(d):
    return rng.standard_normal(int(d * SR))


def sweep(d, f0, f1):
    t = t_axis(d)
    return np.sin(2 * np.pi * np.cumsum(f0 * (f1 / f0) ** (t / d)) / SR)


# ---------------------------------------------------------------- sons
def tick(f=2600):
    d = 0.05
    t = t_axis(d)
    click = hp(noise(d), 2500) * env_exp(t, 0.0012, 0.0002)
    tone = np.sin(2 * np.pi * f * t) * env_exp(t, 0.010, 0.0005)
    return 0.6 * click + 0.5 * tone


def whoosh(d=0.45, f0=300, f1=3200, peak=0.6):
    """Bruit filtré par une bande qui glisse de f0 à f1, enveloppe en cloche."""
    n = int(d * SR)
    x = noise(d)
    y = np.zeros(n)
    blocks = 48
    edges = np.linspace(0, n, blocks + 1).astype(int)
    for b in range(blocks):
        a, z = edges[b], edges[b + 1]
        fc = f0 * (f1 / f0) ** ((b + 0.5) / blocks)
        lo, hi = fc / 1.8, min(fc * 1.8, SR / 2 * 0.95)
        y[a:z] = bp(x[max(0, a - 2048) : z], lo, hi)[-(z - a) :]
    u = t_axis(d) / d
    e = np.where(u < peak, (u / peak) ** 2, ((1 - u) / (1 - peak)) ** 1.6)
    y = y * e
    return y / (np.max(np.abs(y)) + 1e-9)


def pop(f0=520, d=0.16):
    t = t_axis(d)
    f = f0 * (0.55 + 0.45 * np.exp(-t / 0.03))
    s = np.sin(2 * np.pi * np.cumsum(f) / SR) * env_exp(t, 0.045, 0.002)
    return s + hp(noise(d), 3000) * env_exp(t, 0.0015, 0.0002) * 0.25


def bloop(f0=320, f1=900, d=0.12):
    return sweep(d, f0, f1) * env_exp(t_axis(d), 0.05, 0.004)


def tap():
    d = 0.06
    t = t_axis(d)
    return 0.8 * hp(noise(d), 3500) * env_exp(t, 0.002, 0.0002) + 0.45 * np.sin(2 * np.pi * 1700 * t) * env_exp(t, 0.012, 0.0005)


def bell(f, d=1.2, tau=0.45, bright=1.0):
    t = t_axis(d)
    parts = [(1, 1.0, tau), (2.0, 0.32 * bright, tau * 0.6), (3.01, 0.16 * bright, tau * 0.45), (4.2, 0.07 * bright, tau * 0.3)]
    s = sum(a * np.sin(2 * np.pi * f * k * t) * np.exp(-t / tt) for k, a, tt in parts)
    return s * np.clip(t / 0.003, 0, 1)


def chime(notes, gap=0.085, tau=0.4):
    y = np.zeros(int((gap * len(notes) + 1.3) * SR))
    for i, f in enumerate(notes):
        b = bell(f, 1.2, tau)
        a = int(i * gap * SR)
        y[a : a + len(b)] += b
    return y


def thump(d=0.6, f0=95, f1=38):
    t = t_axis(d)
    f = f1 + (f0 - f1) * np.exp(-t / 0.06)
    s = np.sin(2 * np.pi * np.cumsum(f) / SR) * env_exp(t, 0.22, 0.003)
    s = s + lp(noise(d), 180) * env_exp(t, 0.05, 0.001) * 0.8
    return np.tanh(1.6 * s) / np.tanh(1.6)


def riser(d=1.0):
    u = t_axis(d) / d
    return (0.8 * whoosh(d, 350, 6000, peak=0.97) + sweep(d, 180, 720) * u**2 * 0.35) * (0.2 + 0.8 * u**1.5)


def sparkle(d=0.7, n=9, seed=1):
    r = np.random.default_rng(seed)
    y = np.zeros(int(d * SR))
    t = t_axis(0.35)
    for _ in range(n):
        f = r.uniform(3200, 7200)
        at = int(r.uniform(0, d - 0.36) * SR)
        y[at : at + len(t)] += np.sin(2 * np.pi * f * t) * np.exp(-t / r.uniform(0.04, 0.12)) * r.uniform(0.4, 1.0)
    return y + hp(noise(d), 6000) * np.exp(-t_axis(d) / 0.25) * 0.12


def pad(d=2.8, root=174.61):
    """Accord doux (fa majeur 7) qui gonfle puis s'efface : le moment « envie »."""
    t = t_axis(d)
    u = t / d
    y = np.zeros(len(t))
    for j, f in enumerate([root, root * 5 / 4, root * 3 / 2, root * 15 / 8, root * 2]):
        for det in (-0.0025, 0.0025):
            y += sum((1 / k) * np.sin(2 * np.pi * f * (1 + det) * k * t + j) for k in (1, 2, 3))
    y = lp(y, 1600) * np.minimum(np.clip(u / 0.3, 0, 1), np.clip((1 - u) / 0.35, 0, 1))
    return y / np.max(np.abs(y))


def voice_texture(d=0.85):
    """Souffle modulé très discret pendant l'écoute du micro."""
    t = t_axis(d)
    mod = 0.5 + 0.5 * np.sin(2 * np.pi * 5.2 * t) * np.sin(2 * np.pi * 1.3 * t)
    v = bp(noise(d), 300, 2200) * mod * np.minimum(1, t / 0.1) * np.minimum(1, (d - t) / 0.15)
    return v / np.max(np.abs(v))


# ---------------------------------------------------------------- partition
H, B, Ch, Es, De, L, En = (C[k] for k in ("hook", "brief", "chat", "est", "det", "life", "end"))

# 1 · Accroche : un tic à chaque graduation franchie par l'aiguille (ease power1.inOut)
def quad_inout_inv(p):
    return np.sqrt(p / 2) if p < 0.5 else 1 - np.sqrt(2 * (1 - p)) / 2


for k in range(1, 13):
    at = H["ring"] + H["ringDur"] * quad_inout_inv(k / 12)
    place(tick(2600 if k % 2 else 2000), at, 0.22 + (0.1 if k % 3 == 0 else 0), np.sin(k / 12 * 2 * np.pi) * 0.5)
place(whoosh(0.3, 500, 4000, 0.8), H["time"] - 0.12, 0.25)
place(thump(0.5, 110, 45), H["time"] + 0.02, 0.55)
place(whoosh(0.35, 700, 5000, 0.7), H["l1"] - 0.08, 0.16, -0.3)
place(whoosh(0.35, 800, 6000, 0.7), H["l2"] - 0.08, 0.16, 0.3)
place(whoosh(0.45, 2500, 500, 0.35), H["exit"], 0.25)

# 2 · Brief : téléphone, notification, tap, cartes, coche
place(whoosh(0.7, 180, 1500, 0.6), B["rise"] - 0.05, 0.3)
place(chime([880.0, 1318.5], gap=0.11, tau=0.5), B["notif"] + 0.08, 0.32)
place(tap(), B["tap"], 0.45)
place(whoosh(0.3, 600, 3500, 0.5), B["open"], 0.2)
for i in range(5):
    place(pop(420 + i * 60, 0.12), B["cards"] + 0.05 + i * 0.09, 0.12, -0.4 + i * 0.2)
place(tap(), B["check"] - 0.06, 0.4)
place(chime([1046.5, 1568.0], gap=0.07, tau=0.35), B["check"] + 0.02, 0.28)
place(tick(1800), B["count"] + 0.05, 0.18)

# 3 · Chat : micro, écoute, bulle, mots, réponse, coches
place(whoosh(0.35, 800, 3000, 0.5), Ch["swap"], 0.22)
place(bloop(300, 900, 0.12), Ch["pill"], 0.35)
place(voice_texture(0.85), Ch["pill"] + 0.08, 0.06)
place(bloop(900, 400, 0.1), Ch["expand"] - 0.02, 0.22)
place(whoosh(0.4, 400, 2500, 0.5), Ch["expand"], 0.14)
for i in range(12):
    place(tick(3000 + (i % 3) * 300), Ch["words"] + i * 0.035, 0.06, -0.3 + (i % 5) * 0.15)
for i in range(3):
    place(pop(700 + i * 90, 0.08), Ch["typing"] + 0.05 + i * 0.07, 0.08)
place(pop(600, 0.18), Ch["answer"], 0.22)
place(whoosh(0.35, 300, 1800, 0.5), Ch["receipt"], 0.14)
for i, f in enumerate([1046.5, 1318.5, 1568.0]):
    place(bell(f, 1.0, 0.3), Ch["checks"] + 0.1 + i * 0.13, 0.2, -0.3 + i * 0.3)

# 4 · Estimation : un tic par palier du compteur (ease power3.out = 1-(1-t)^4)
place(whoosh(0.35, 800, 3000, 0.5), Es["swap"], 0.22)
for k in range(1, 23):
    v = k / 22
    place(tick(1200 + 1400 * v), Es["count"] + Es["countDur"] * (1 - (1 - v) ** 0.25), 0.12 + 0.06 * v)
place(chime([1568.0, 2093.0], gap=0.06, tau=0.3), Es["count"] + Es["countDur"] - 0.05, 0.18)
place(whoosh(0.4, 500, 4000, 0.4), Es["fill"], 0.14, 0.3)
place(pop(760, 0.14), Es["marker"] + 0.35, 0.18)
t_ring = t_axis(Es["ringDur"])
place(sweep(Es["ringDur"], 520, 1040) * np.minimum(1, t_ring / 0.1) * np.exp(-t_ring / 0.6), Es["ring"], 0.07)
for i in range(3):
    place(pop(560 + i * 110, 0.13), Es["chips"] + i * 0.09, 0.14, -0.4 + i * 0.4)

# 5 · Détecteur : carte qui se dessine, sonar sur les DPE, piste
place(whoosh(0.35, 800, 3000, 0.5), De["swap"], 0.22)
place(whoosh(0.9, 250, 2400, 0.55), De["map"] - 0.05, 0.16)
for i, f in enumerate([1318.5, 1174.7, 1568.0]):
    b = bell(f, 1.0, 0.22, bright=0.4)
    place(b, De["pins"] + i * 0.16, 0.2, [-0.5, 0.1, 0.5][i])
    place(b, De["pins"] + i * 0.16 + 0.14, 0.07, [-0.5, 0.1, 0.5][i])
place(pop(680, 0.15), De["badge"], 0.2, -0.4)
place(whoosh(0.45, 300, 2200, 0.5), De["lead"], 0.18)
place(tap(), De["press"] - 0.05, 0.4)
place(bloop(700, 1100, 0.08), De["press"] + 0.02, 0.12)

# 5b · Quotidien : la photo qui donne envie
place(whoosh(0.5, 2400, 400, 0.4), L["phoneOut"], 0.22)
place(whoosh(0.8, 300, 5000, 0.55), L["photo"] - 0.05, 0.2)
place(sparkle(0.8, 8, 3), L["photo"] + 0.25, 0.1)
place(pad(2.9), L["photo"], 0.1)
for i in range(3):
    place(pop(620 + i * 120, 0.15), L["chips"] + i * 0.14, 0.16, -0.4 + i * 0.4)
place(whoosh(0.4, 2500, 500, 0.35), L["exit"], 0.2)

# 6 · Fin : montée, logo, impact du robot, étincelles, offre
place(riser(En["toBelly"] + 0.2 - En["house"]), En["house"] - 0.05, 0.22)
for i in range(18):
    place(tick(3200 + (i * 397) % 2400), En["house"] + 0.35 + i * 0.028, 0.05, ((i * 7) % 11 - 5) / 7)
place(whoosh(0.4, 3000, 600, 0.4), En["toBelly"], 0.16)
place(thump(0.7, 120, 40), En["robot"] + 0.08, 0.6)
place(bloop(260, 780, 0.16), En["robot"] + 0.12, 0.3)
place(sparkle(0.8, 10, 5), En["robot"] + 0.12, 0.2)
place(whoosh(0.4, 600, 3500, 0.5), En["word"] - 0.05, 0.12)
place(pop(500, 0.2), En["cta"], 0.25)
place(chime([1318.5, 1760.0, 2637.0], gap=0.06, tau=0.45), En["cta"] + 0.08, 0.2)
place(sparkle(0.9, 12, 9), En["sparkle"], 0.22)
place(whoosh(0.8, 3000, 9000, 0.5), En["sheen"], 0.06)

# ---------------------------------------------------------------- mixage
t_ir = t_axis(1.1)
ir = []
for pre in (0.012, 0.017):
    x = rng.standard_normal(len(t_ir)) * np.exp(-t_ir / 0.28)
    x[: int(pre * SR)] = 0
    x = lp(x, 5000)
    ir.append(x / np.sqrt(np.sum(x**2)))
wet = np.vstack([fftconvolve(out[0], ir[0])[:N], fftconvolve(out[1], ir[1])[:N]])
mix = out + 0.22 * wet
mix = np.vstack([hp(mix[0], 30), hp(mix[1], 30)])
mix = mix / np.max(np.abs(mix)) * 0.9
mix = np.tanh(1.2 * mix) / np.tanh(1.2)
mix = mix / np.max(np.abs(mix)) * 10 ** (-3.0 / 20)
n_end = int(DUR * SR)
fade = int(0.25 * SR)
mix = mix[:, :n_end]
mix[:, -fade:] *= np.linspace(1, 0, fade)

os.makedirs(os.path.join(ROOT, "assets", "audio"), exist_ok=True)
with wave.open(os.path.join(ROOT, "assets", "audio", "sfx.wav"), "wb") as w:
    w.setnchannels(2)
    w.setsampwidth(2)
    w.setframerate(SR)
    w.writeframes((mix.T * 32767).astype("<i2").tobytes())
print(f"assets/audio/sfx.wav : {DUR} s, {SR} Hz, stéréo")
