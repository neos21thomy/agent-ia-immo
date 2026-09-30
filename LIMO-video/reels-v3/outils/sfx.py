#!/usr/bin/env python3
"""Moteur d'effets sonores des Reels LIMO.

Usage :  python3 outils/sfx.py .sfx/reel-1-pov.json assets/audio/reel-1-pov.wav

Le JSON (produit par outils/extract-sfx.mjs) contient la durée de la vidéo et la liste
des sons déclarés par les animations (K.sfx(t, type, gain, pan, extra) dans kit.js).
Chaque son est synthétisé ici : aucun échantillon externe, libre de droits, déterministe.
Dépendances : numpy, scipy.
"""
import json
import sys
import wave

import numpy as np
from scipy.signal import butter, fftconvolve, sosfilt

SR = 48000
rng = np.random.default_rng(7)


def t_axis(d):
    return np.arange(max(1, int(d * SR))) / SR


def env_exp(t, tau, att=0.002):
    return np.exp(-t / tau) * np.clip(t / att, 0, 1)


def bp(x, lo, hi):
    return sosfilt(butter(2, [lo / (SR / 2), hi / (SR / 2)], btype="band", output="sos"), x)


def hp(x, f):
    return sosfilt(butter(2, f / (SR / 2), btype="high", output="sos"), x)


def lp(x, f):
    return sosfilt(butter(2, f / (SR / 2), btype="low", output="sos"), x)


def noise(d):
    return rng.standard_normal(max(1, int(d * SR)))


def sweep(d, f0, f1):
    t = t_axis(d)
    return np.sin(2 * np.pi * np.cumsum(f0 * (f1 / f0) ** (t / d)) / SR)


def norm(x):
    return x / (np.max(np.abs(x)) + 1e-9)


# ------------------------------------------------------------------ sons élémentaires
def tick(f=2600):
    t = t_axis(0.05)
    return 0.6 * hp(noise(0.05), 2500) * env_exp(t, 0.0012, 0.0002) + 0.5 * np.sin(2 * np.pi * f * t) * env_exp(t, 0.010, 0.0005)


def type_click(f=2800):
    t = t_axis(0.03)
    return 0.7 * hp(noise(0.03), 3000) * env_exp(t, 0.0015, 0.0002) + 0.25 * np.sin(2 * np.pi * f * t) * env_exp(t, 0.005, 0.0005)


def whoosh(d=0.45, f0=300, f1=3200, peak=0.6):
    n = int(d * SR)
    x = noise(d)
    y = np.zeros(n)
    edges = np.linspace(0, n, 49).astype(int)
    for b in range(48):
        a, z = edges[b], edges[b + 1]
        fc = f0 * (f1 / f0) ** ((b + 0.5) / 48)
        y[a:z] = bp(x[max(0, a - 2048) : z], fc / 1.8, min(fc * 1.8, SR / 2 * 0.95))[-(z - a) :]
    u = t_axis(d) / d
    return norm(y * np.where(u < peak, (u / peak) ** 2, ((1 - u) / (1 - peak)) ** 1.6))


def pop(f0=520, d=0.16):
    t = t_axis(d)
    f = f0 * (0.55 + 0.45 * np.exp(-t / 0.03))
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * env_exp(t, 0.045, 0.002) + hp(noise(d), 3000) * env_exp(t, 0.0015, 0.0002) * 0.25


def bloop(f0=320, f1=900, d=0.12):
    return sweep(d, f0, f1) * env_exp(t_axis(d), 0.05, 0.004)


def tap():
    t = t_axis(0.06)
    return 0.8 * hp(noise(0.06), 3500) * env_exp(t, 0.002, 0.0002) + 0.45 * np.sin(2 * np.pi * 1700 * t) * env_exp(t, 0.012, 0.0005)


def bell(f, d=1.2, tau=0.45, bright=1.0):
    t = t_axis(d)
    parts = [(1, 1.0, tau), (2.0, 0.32 * bright, tau * 0.6), (3.01, 0.16 * bright, tau * 0.45), (4.2, 0.07 * bright, tau * 0.3)]
    return sum(a * np.sin(2 * np.pi * f * k * t) * np.exp(-t / tt) for k, a, tt in parts) * np.clip(t / 0.003, 0, 1)


def chime(notes, gap=0.085, tau=0.4, bright=1.0):
    y = np.zeros(int((gap * len(notes) + 1.3) * SR))
    for i, f in enumerate(notes):
        b = bell(f, 1.2, tau, bright)
        a = int(i * gap * SR)
        y[a : a + len(b)] += b
    return y


def thump(d=0.6, f0=95, f1=38):
    t = t_axis(d)
    f = f1 + (f0 - f1) * np.exp(-t / 0.06)
    s = np.sin(2 * np.pi * np.cumsum(f) / SR) * env_exp(t, 0.22, 0.003) + lp(noise(d), 180) * env_exp(t, 0.05, 0.001) * 0.8
    return np.tanh(1.6 * s) / np.tanh(1.6)


def riser(d=1.0):
    u = t_axis(d) / d
    return (0.8 * whoosh(d, 350, 6000, 0.97) + sweep(d, 180, 720) * u**2 * 0.35) * (0.2 + 0.8 * u**1.5)


def sparkle(d=0.8, n=10, seed=1):
    r = np.random.default_rng(seed)
    y = np.zeros(int(d * SR))
    t = t_axis(0.35)
    for _ in range(n):
        at = int(r.uniform(0, d - 0.36) * SR)
        y[at : at + len(t)] += np.sin(2 * np.pi * r.uniform(3200, 7200) * t) * np.exp(-t / r.uniform(0.04, 0.12)) * r.uniform(0.4, 1.0)
    return y + hp(noise(d), 6000) * np.exp(-t_axis(d) / 0.25) * 0.12


def pad(d=2.8, root=174.61):
    t = t_axis(d)
    u = t / d
    y = np.zeros(len(t))
    for j, f in enumerate([root, root * 5 / 4, root * 3 / 2, root * 15 / 8, root * 2]):
        for det in (-0.0025, 0.0025):
            y += sum((1 / k) * np.sin(2 * np.pi * f * (1 + det) * k * t + j) for k in (1, 2, 3))
    return norm(lp(y, 1600) * np.minimum(np.clip(u / 0.3, 0, 1), np.clip((1 - u) / 0.35, 0, 1)))


def voice(d=0.8):
    t = t_axis(d)
    mod = 0.5 + 0.5 * np.sin(2 * np.pi * 5.2 * t) * np.sin(2 * np.pi * 1.3 * t)
    return norm(bp(noise(d), 300, 2200) * mod * np.minimum(1, t / 0.1) * np.minimum(1, (d - t) / 0.15))


def scan(d=0.6):
    t = t_axis(d)
    trem = 0.6 + 0.4 * np.sin(2 * np.pi * 18 * t)
    s = sweep(d, 600, 2400) * trem * 0.5 + bp(noise(d), 2000, 7000) * 0.3
    return s * np.minimum(1, t / 0.05) * np.minimum(1, (d - t) / 0.12)


def shutter():
    y = np.zeros(int(0.12 * SR))
    for at, g in ((0.0, 1.0), (0.045, 0.7)):
        c = bp(noise(0.03), 1500, 9000) * env_exp(t_axis(0.03), 0.004, 0.0003) * g
        a = int(at * SR)
        y[a : a + len(c)] += c
    return y


def stamp():
    t = t_axis(0.35)
    return 0.9 * thump(0.35, 140, 55) + 0.6 * bp(noise(0.35), 300, 3000) * env_exp(t, 0.03, 0.001)


def send():
    y = 0.6 * whoosh(0.25, 600, 3500, 0.35)
    p = pop(900, 0.12)
    y[: len(p)] += 0.5 * p
    return y


def receive():
    y = np.zeros(int(0.6 * SR))
    p = pop(760, 0.14)
    y[: len(p)] += p
    b = bell(1568, 0.5, 0.15, 0.5) * 0.35
    a = int(0.04 * SR)
    y[a : a + len(b)] += b[: len(y) - a]
    return y


def sonar(f=1318.5):
    b = bell(f, 1.0, 0.22, 0.4)
    y = np.zeros(len(b) + int(0.14 * SR))
    y[: len(b)] += b
    y[int(0.14 * SR) :] += 0.35 * b
    return y


def beep(f=880, d=0.16):
    t = t_axis(d)
    s = np.sin(2 * np.pi * f * t) + 0.25 * np.sin(2 * np.pi * 3 * f * t)
    return s * np.minimum(1, t / 0.004) * np.minimum(1, (d - t) / 0.03)


def buzz(d=0.28):
    t = t_axis(d)
    f = 118 * (1 + 0.03 * np.sin(2 * np.pi * 22 * t))
    s = np.tanh(3 * np.sin(2 * np.pi * np.cumsum(f) / SR))
    return lp(s, 1800) * np.minimum(1, t / 0.01) * np.minimum(1, (d - t) / 0.05)


def slam():
    y = np.zeros(int(0.7 * SR))
    th = thump(0.6, 130, 42)
    y[: len(th)] += th
    t = t_axis(0.12)
    y[: len(t)] += 0.5 * bp(noise(0.12), 800, 8000) * env_exp(t, 0.02, 0.0005)
    return y


def clack():
    y = np.zeros(int(0.12 * SR))
    for at, f in ((0.0, 2400), (0.055, 1700)):
        c = tick(f)
        a = int(at * SR)
        y[a : a + len(c)] += c
    return y


def go():
    y = np.zeros(int(0.9 * SR))
    b = beep(1760, 0.35)
    y[: len(b)] += b
    w = 0.5 * whoosh(0.5, 400, 6000, 0.3)
    y[: len(w)] += w
    return y


SOUNDS = {
    "tick": lambda e: tick(e.get("f", 2600)),
    "tock": lambda e: tick(1900),
    "type": lambda e: type_click(e.get("f", 2800)),
    "pop": lambda e: pop(e.get("f", 520), e.get("d", 0.16)),
    "tap": lambda e: tap(),
    "bloop-up": lambda e: bloop(e.get("f0", 320), e.get("f1", 900), e.get("d", 0.12)),
    "bloop-down": lambda e: bloop(900, 400, 0.1),
    "whoosh": lambda e: whoosh(e.get("d", 0.45), e.get("f0", 300), e.get("f1", 3200), e.get("pk", 0.6)),
    "swipe": lambda e: whoosh(0.3, 800, 3000, 0.5),
    "success": lambda e: chime([1046.5, 1568.0], 0.07, 0.35),
    "notif": lambda e: chime([880.0, 1318.5], 0.11, 0.5),
    "cta": lambda e: chime([1318.5, 1760.0, 2637.0], 0.06, 0.45),
    "split": lambda e: chime([1568.0, 2093.0], 0.05, 0.3),
    "fanfare": lambda e: chime([1046.5, 1318.5, 1568.0, 2093.0], 0.09, 0.6),
    "thump": lambda e: thump(0.7, 120, 40),
    "drop": lambda e: thump(0.35, 150, 60),
    "riser": lambda e: riser(e.get("d", 1.0)),
    "sparkle": lambda e: sparkle(0.8, 10, int(e["t"] * 10) % 97 + 1),
    "pad": lambda e: pad(e.get("d", 2.8)),
    "voice": lambda e: voice(e.get("d", 0.8)),
    "scan": lambda e: scan(e.get("d", 0.6)),
    "shutter": lambda e: shutter(),
    "stamp": lambda e: stamp(),
    "send": lambda e: send(),
    "receive": lambda e: receive(),
    "sonar": lambda e: sonar(e.get("f", 1318.5)),
    "beep": lambda e: beep(e.get("f", 880), e.get("d", 0.16)),
    "go": lambda e: go(),
    "buzz": lambda e: buzz(e.get("d", 0.28)),
    "slam": lambda e: slam(),
    "clack": lambda e: clack(),
}


def render(events, dur):
    n = int((dur + 1.5) * SR)
    out = np.zeros((2, n))
    unknown = set()
    for e in sorted(events, key=lambda e: e["t"]):
        fn = SOUNDS.get(e["k"])
        if fn is None:
            unknown.add(e["k"])
            continue
        sig = fn(e) * e.get("g", 1.0)
        pan = max(-1.0, min(1.0, e.get("p", 0.0)))
        left, right = np.cos((pan + 1) * np.pi / 4), np.sin((pan + 1) * np.pi / 4)
        i = int(round(e["t"] * SR))
        m = min(len(sig), n - i)
        if m > 0 and i >= 0:
            out[0, i : i + m] += sig[:m] * left * np.sqrt(2)
            out[1, i : i + m] += sig[:m] * right * np.sqrt(2)
    if unknown:
        print("Sons inconnus ignorés :", ", ".join(sorted(unknown)))
    # réverbération légère (réponse impulsionnelle synthétique stéréo)
    t_ir = t_axis(1.1)
    irs = []
    for pre in (0.012, 0.017):
        x = rng.standard_normal(len(t_ir)) * np.exp(-t_ir / 0.28)
        x[: int(pre * SR)] = 0
        x = lp(x, 5000)
        irs.append(x / np.sqrt(np.sum(x**2)))
    wet = np.vstack([fftconvolve(out[0], irs[0])[:n], fftconvolve(out[1], irs[1])[:n]])
    mix = out + 0.2 * wet
    mix = np.vstack([hp(mix[0], 30), hp(mix[1], 30)])
    mix = mix / (np.max(np.abs(mix)) + 1e-9) * 0.9
    mix = np.tanh(1.2 * mix) / np.tanh(1.2)
    mix = mix / (np.max(np.abs(mix)) + 1e-9) * 10 ** (-3.0 / 20)
    end = int(dur * SR)
    fade = int(0.25 * SR)
    mix = mix[:, :end]
    mix[:, -fade:] *= np.linspace(1, 0, fade)
    return mix


def main():
    src, dst = sys.argv[1], sys.argv[2]
    data = json.load(open(src, encoding="utf-8"))
    mix = render(data["events"], float(data["duration"]))
    with wave.open(dst, "wb") as w:
        w.setnchannels(2)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes((mix.T * 32767).astype("<i2").tobytes())
    print(f"{dst} : {len(data['events'])} sons, {data['duration']} s")


if __name__ == "__main__":
    main()
