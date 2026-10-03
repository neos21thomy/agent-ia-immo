"""Musiques originales synthétisées pour les Reels LIMO (aucun échantillon externe, libres de droits).

Chaque Reel a un préréglage (style, tempo, instant où le groove démarre). La musique :
- joue une intro filtrée pendant l'accroche, puis le groove complet à partir de `full` ;
- s'arrête sur une frappe (impact + accord tenu) à l'arrivée de la carte de fin (endCardAt) ;
- est mixée sous les bruitages, puis le tout passe dans un limiteur doux.

Usage : python3 outils/music.py <reel> .sfx/<reel>.json assets/audio/<reel>.wav renders/<reel>-musique.wav
        (le 3e argument est la piste de bruitages déjà synthétisée par sfx.py)
"""
import json
import sys
import wave

import numpy as np
from scipy.signal import butter, fftconvolve, sosfilt

SR = 48000
RNG = np.random.default_rng(7)

# style, tempo, début du groove (s) ; « drop » = instant où la batterie entre (série : après la frise)
PRESETS = {
    "reel-1-pov": ("house", 122, 2.3),
    "reel-2-speedrun": ("speed", 140, 2.39),
    "reel-3-avant-apres": ("trap", 140, 2.45),
    "reel-4-conversation": ("lofi", 88, 1.55),
    "reel-5-top11": ("pop", 124, 2.35),
    "short-1-pov": ("house", 122, 2.3),
    "short-2-speedrun": ("speed", 140, 2.39),
    "short-3-sans-vs-avec": ("trap", 140, 2.45),
    "short-4-conversation": ("lofi", 88, 1.55),
    "short-5-top3": ("pop", 124, 2.35),
    "serie-n1-declic": ("epic", 100, 2.45, 13.05),
    "premium-hero": ("epic", 100, 2.9, 6.4),
    "premium-15s": ("epic", 100, 2.4, 2.4),
    "film-01-mandat-perdu": ("epic", 100, 2.0, 6.7),
    "film-02-dimanche-18h": ("lofi", 88, 1.4),
    "film-03-le-calcul": ("speed", 140, 2.8),
    "film-04-fais-le-test": ("pop", 124, 1.4),
    "film-05-ton-telephone-bosse": ("house", 122, 2.0),
    "film-06-tout-en-un": ("epic", 100, 1.1, 5.3),
    "film-07-mythes-realite": ("trap", 140, 2.5),
    "film-08-manifeste": ("epic", 100, 3.5, 8.2),
    "film-09-prix-cafe": ("pop", 124, 1.4),
    "film-10-visite-au-mandat": ("house", 122, 1.5),
    "nat-01-rappelez-moi-en-mars": ("lofi", 88, 0.8),
    "nat-02-dimanche-soir": ("lofi", 88, 0.8),
    "nat-03-842-contacts": ("pop", 124, 0.8),
    "nat-04-compromis-12-pages": ("pop", 124, 0.8),
    "nat-05-note-vocale": ("lofi", 88, 0.8),
    "nat-06-avis-sans-reponse": ("house", 122, 0.8),
    "nat-07-annonce-22h": ("lofi", 88, 0.8),
    "nat-08-quiz-dpe": ("pop", 124, 0.8),
    "nat-09-anniversaire": ("lofi", 88, 0.8),
    "nat-10-ton-collegue": ("house", 122, 0.8),
    "hook-01-ia-remplace": ("trap", 140, 0.3),
    "hook-02-trois-agences": ("house", 122, 0.3),
    "hook-03-dix-secondes": ("speed", 140, 0.3),
    "hook-04-red-flags": ("trap", 140, 0.3),
    "hook-05-ton-concurrent": ("epic", 100, 0.3, 3.3),
    "hook-06-elle-vaut-combien": ("pop", 124, 0.3),
    "hook-07-qui-va-vendre": ("house", 122, 0.3),
    "hook-08-avant-8h": ("lofi", 88, 0.3),
    "hook-09-ne-like-pas": ("pop", 124, 0.3),
    "hook-10-le-test": ("house", 122, 0.3),
    "mascotte-01-salut-agent-immo": ("pop", 124, 0.3),
    "mascotte-02-entretien-embauche": ("house", 122, 0.3),
    "mascotte-03-3h-du-matin": ("lofi", 88, 0.3),
    "mascotte-04-il-reagit": ("trap", 140, 0.3),
    "mascotte-05-vrai-ou-faux": ("pop", 124, 0.3),
    "mascotte-06-pendant-ton-cafe": ("lofi", 88, 0.3),
    "mascotte-07-ne-me-dis-pas": ("house", 122, 0.3),
    "mascotte-08-duel": ("speed", 140, 0.3),
    "mascotte-09-pov-installation": ("pop", 124, 0.3),
    "mascotte-10-mieux-que-ton-stagiaire": ("house", 122, 0.3),
    "pub-01-trois-agences": ("house", 122, 0.3),
    "pub-02-ton-concurrent": ("epic", 100, 0.3, 3.3),
    "pub-03-qui-va-vendre": ("house", 122, 0.3),
    "pub-04-entretien-embauche": ("house", 122, 0.3),
    "pub-05-mieux-que-ton-stagiaire": ("house", 122, 0.3),
    "pub-06-rappelez-moi-en-mars": ("lofi", 88, 0.8),
    "pub30-01-mandats-perdus": ("house", 122, 0.3),
    "pub30-02-trois-agences": ("pop", 124, 0.3),
    "pub30-03-annonces": ("lofi", 88, 0.3),
    "pub30-04-qui-va-vendre": ("house", 122, 0.3),
    "pub30-05-crm-dort": ("pop", 124, 0.3),
    "pub30-06-avis-google": ("house", 122, 0.3),
    "cine-01-manifeste": ("epic", 100, 0.3, 11.5),
    "cine-02-une-journee": ("pop", 124, 0.3),
    "cine-03-le-calcul": ("epic", 100, 0.3, 13.0),
    "cine-04-prestige": ("epic", 100, 0.3, 14.7),
    "cine-05-chalet": ("epic", 100, 0.3, 14.7),
    "cine-06-bord-de-mer": ("house", 122, 0.3),
    "cine-07-trois-biens": ("epic", 100, 0.3, 14.7),
    "agents-01-les-12-agents": ("house", 122, 0.3),
    "life-01-pendant-ce-temps": ("lofi", 88, 0.3),
    "life-02-pov-collegue": ("pop", 124, 0.3),
    "life-03-biens-exception": ("epic", 100, 0.3, 17.0),
    "voix-01-julien": ("lofi", 84, 0.3),
    "voix-02-regarde-ca": ("pop", 120, 0.3),
    "voix-03-surcharge": ("house", 122, 0.3),
    "sign-01-derriere-chaque-signature": ("epic", 100, 0.3, 17.2),
    "prem-01-regarde-ca": ("pop", 120, 0.3),
    "prem-02-trois-erreurs": ("epic", 100, 0.3, 26.1),
    "prem-03-dimanche-soir": ("lofi", 84, 0.3),
    "prem-04-le-calcul": ("house", 122, 0.3),
    "prem-05-une-journee": ("pop", 118, 0.3),
    "long-02-imagine": ("pop", 118, 0.3),
    "punch-01-ce-quon-ne-voit-pas": ("epic", 100, 0.3, 21.4),
    "punch-02-23-heures": ("epic", 100, 0.3, 25.95),
    "punch-03-le-mandat-da-cote": ("epic", 100, 0.3, 22.9),
    "punch-04-pas-tout-seul": ("epic", 100, 0.3, 23.35),
    "punch-05-lettre-a-un-conseiller": ("epic", 100, 0.3, 27.25),
    "long-03-crm-qui-travaille": ("house", 122, 0.3, 11.2),
    "long-04-une-semaine": ("lofi", 88, 0.3),
    "long-05-tout-lui-dire": ("pop", 120, 0.3),
    "long-06-par-des-agents": ("epic", 100, 0.3, 15.8),
    "viral-01-il-te-lache-plus": ("pop", 122, 0.3, 23.8),
    "viral-02-limo-tappelle": ("pop", 122, 0.3, 17.0),
}

# progressions (MIDI) : accords (3-4 notes) et fondamentale de basse
PROG = {
    "minor": ([[57, 60, 64, 67], [53, 57, 60, 64], [48, 55, 60, 64], [55, 59, 62, 67]], [45, 41, 48, 43]),  # Am F C G
    "dark": ([[57, 60, 64], [53, 57, 60], [52, 55, 59], [52, 56, 59]], [45, 41, 40, 40]),  # Am F Em E
    "lofi": ([[50, 53, 57, 60], [55, 59, 62, 65], [48, 52, 55, 59], [45, 48, 52, 55]], [38, 43, 48, 45]),  # Dm9 G13 Cmaj7 Am7
    "bright": ([[48, 52, 55, 59], [55, 59, 62], [57, 60, 64], [53, 57, 60, 64]], [36, 43, 45, 41]),  # Cmaj7 G Am Fmaj7
}


def mtof(m):
    return 440.0 * 2 ** ((m - 69) / 12)


def tax(d):
    return np.arange(int(d * SR)) / SR


def lp(x, f, order=2):
    return sosfilt(butter(order, min(f, SR / 2 - 100), "low", fs=SR, output="sos"), x)


def hp(x, f, order=2):
    return sosfilt(butter(order, f, "high", fs=SR, output="sos"), x)


def bp(x, lo, hi):
    return sosfilt(butter(2, [lo, hi], "band", fs=SR, output="sos"), x)


def saw(f, d, hmax=9000):
    t = tax(d)
    out = np.zeros_like(t)
    for k in range(1, max(2, int(hmax / f)) + 1):
        out += np.sin(2 * np.pi * f * k * t) / k
    return out * 0.55


def square(f, d, hmax=7000):
    t = tax(d)
    out = np.zeros_like(t)
    for k in range(1, max(2, int(hmax / f)) + 1, 2):
        out += np.sin(2 * np.pi * f * k * t) / k
    return out * 0.7


def adsr(n, a=0.005, dcy=0.1, s=0.6, r=0.05):
    e = np.full(n, float(s))
    na, nd, nr = int(a * SR), int(dcy * SR), int(r * SR)
    na = min(na, n)
    e[:na] = np.linspace(0, 1, na, endpoint=False)
    nd = min(nd, n - na)
    e[na:na + nd] = np.linspace(1, s, nd, endpoint=False)
    if nr and n > nr:
        e[-nr:] *= np.linspace(1, 0, nr)
    return e


# ------------------------------------------------------------------ batterie
def kick(d=0.45, f0=150, f1=45, punch=1.0):
    t = tax(d)
    f = f1 + (f0 - f1) * np.exp(-t / 0.03)
    ph = 2 * np.pi * np.cumsum(f) / SR
    x = np.sin(ph) * np.exp(-t / 0.16)
    x[: int(0.004 * SR)] += RNG.standard_normal(int(0.004 * SR)) * 0.3 * punch
    return np.tanh(1.6 * x)


def k808(f, d=0.9):
    t = tax(d)
    fr = f * (1 + 1.2 * np.exp(-t / 0.02))
    x = np.sin(2 * np.pi * np.cumsum(fr) / SR) * np.exp(-t / 0.45)
    return np.tanh(2.2 * x) * 0.9


def clap(d=0.22):
    t = tax(d)
    n = RNG.standard_normal(len(t))
    env = np.zeros_like(t)
    for o in (0.0, 0.011, 0.022):
        m = t >= o
        env[m] += np.exp(-(t[m] - o) / (0.012 if o < 0.02 else 0.07))
    return bp(n * env, 900, 5000) * 1.4


def snare(d=0.25):
    t = tax(d)
    body = np.sin(2 * np.pi * 185 * t) * np.exp(-t / 0.05)
    nz = hp(RNG.standard_normal(len(t)), 1500) * np.exp(-t / 0.08)
    return 0.5 * body + 0.9 * nz


def hat(d=0.05, open_=False):
    dd = 0.28 if open_ else d
    t = tax(dd)
    x = hp(RNG.standard_normal(len(t)), 7500, 4) * np.exp(-t / (0.09 if open_ else 0.018))
    return x * 0.9


def crash(d=2.2):
    t = tax(d)
    x = hp(RNG.standard_normal(len(t)), 3500) * np.exp(-t / 0.7)
    return x * 0.6


def riser(d=1.2):
    t = tax(d)
    n = RNG.standard_normal(len(t))
    x = np.zeros_like(t)
    seg = 8
    for i in range(seg):
        a, b = int(i * len(t) / seg), int((i + 1) * len(t) / seg)
        x[a:b] = bp(n[a:b], 400 + 900 * i, 1200 + 1600 * i)
    return x * (t / d) ** 2 * 0.8


# ------------------------------------------------------------------ mélodique
def pad_chord(notes, d, cut=2200, bright=1.0):
    out = np.zeros(int(d * SR))
    for m in notes:
        for det in (-0.12, 0.0, 0.12):
            out += saw(mtof(m + det), d, 6000 * bright)
    out = lp(out, cut) / (len(notes) * 3)
    return out * adsr(len(out), a=0.25, dcy=0.3, s=0.85, r=0.3)


def pluck(m, d=0.35, cut=3000, sq=False):
    x = (square if sq else saw)(mtof(m), d)
    t = tax(d)
    return lp(x, cut) * np.exp(-t / (d / 3.5)) * adsr(len(t), a=0.002, dcy=0.01, s=1, r=0.02)


def epiano(m, d=0.9):
    t = tax(d)
    f = mtof(m)
    x = np.sin(2 * np.pi * f * t) + 0.35 * np.sin(2 * np.pi * 2 * f * t) * np.exp(-t / 0.25) + 0.12 * np.sin(2 * np.pi * 3 * f * t) * np.exp(-t / 0.1)
    return x * np.exp(-t / 0.7) * adsr(len(t), a=0.004, dcy=0.05, s=1, r=0.08) * 0.5


def bass_note(m, d, kind):
    t = tax(d)
    if kind == "sub":
        x = np.sin(2 * np.pi * mtof(m) * t)
    else:
        x = lp(saw(mtof(m), d, 2500), 520 if kind == "saw" else 900)
    return np.tanh(1.4 * x) * adsr(len(t), a=0.004, dcy=0.08, s=0.8, r=0.03)


# ------------------------------------------------------------------ outils de mix
def put(buf, x, t, g=1.0):
    i = int(round(t * SR))
    if i >= len(buf) or i + len(x) <= 0:
        return
    if i < 0:
        x = x[-i:]
        i = 0
    n = min(len(x), len(buf) - i)
    buf[i:i + n] += g * x[:n]


def reverb(x, secs=1.8, wet=0.28):
    t = tax(secs)
    irs = [lp(RNG.standard_normal(len(t)), 6000) * np.exp(-t / (secs / 5)) for _ in range(2)]
    irs = [ir / np.sqrt(np.sum(ir ** 2)) for ir in irs]
    return np.stack([x + wet * fftconvolve(x, ir)[: len(x)] for ir in irs])


def delay(x, dt, fb=0.35, n=4):
    out = x.copy()
    for k in range(1, n + 1):
        i = int(dt * k * SR)
        if i < len(x):
            out[i:] += (fb ** k) * x[: len(x) - i]
    return out


# ------------------------------------------------------------------ composition
def compose(style, bpm, full, dur, te, drop=None):
    n = int(dur * SR)
    beat = 60 / bpm
    bar = 4 * beat
    drums = np.zeros(n)
    bass = np.zeros(n)
    harm = np.zeros(n)
    lead = np.zeros(n)
    fx = np.zeros(n)
    prog = {"house": "minor", "pop": "bright", "speed": "minor", "trap": "dark", "lofi": "lofi", "epic": "minor"}[style]
    chords, roots = PROG[prog]
    drop = drop if drop is not None else full
    kicks = []

    # la grille démarre sur « full » ; l'intro (avant) n'a que la nappe
    first_bar = -int(np.ceil(full / bar))
    nb = int(np.ceil((te - full) / bar)) + 1
    for b in range(first_bar, nb):
        t0 = full + b * bar
        if t0 >= te:
            break
        ci = b % 4
        ch, root = chords[ci], roots[ci]
        seg = min(bar, te - t0)
        harm_g = 0.55 if b < 0 else 0.42
        put(harm, pad_chord(ch, seg + 0.3, cut=1400 if style == "lofi" else 2400), t0, harm_g)
        if b < 0:
            continue
        grooving = t0 >= drop - 1e-6
        for s in range(16):  # doubles-croches
            ts = t0 + s * beat / 4
            if ts >= te:
                break
            swing = (beat / 4) * 0.18 if style == "lofi" and s % 2 else 0
            ts += swing
            q, pos = divmod(s, 4)
            if style in ("house", "pop", "speed") and grooving:
                if pos == 0:
                    put(drums, kick(), ts, 0.9)
                    kicks.append(ts)
                if pos == 2:
                    put(drums, hat(open_=style != "speed"), ts, 0.35)
                elif style == "speed" or pos != 0:
                    put(drums, hat(), ts, 0.18 if pos else 0.12)
                if pos == 0 and q in (1, 3):
                    put(drums, clap(), ts, 0.55)
            elif style == "trap" and grooving:
                if s in (0, 7, 10):
                    put(drums, k808(mtof(root - 12 if root > 40 else root)), ts, 0.75)
                    kicks.append(ts)
                if s == 8:
                    put(drums, clap(), ts, 0.6)
                    put(drums, snare(), ts, 0.35)
                put(drums, hat(), ts, 0.16 if s % 2 else 0.24)
                if b % 2 and s >= 12:
                    put(drums, hat(), ts + beat / 8, 0.14)
            elif style == "lofi" and grooving:
                if s in (0, 10):
                    put(drums, kick(0.4, 110, 48, 0.4), ts, 0.7)
                    kicks.append(ts)
                if s in (4, 12):
                    put(drums, lp(snare(), 3500), ts, 0.45)
                if s % 2 == 0:
                    put(drums, lp(hat(), 9000), ts, 0.13)
            elif style == "epic":
                if grooving:
                    if pos == 0:
                        put(drums, kick(0.6, 120, 40), ts, 0.95)
                        kicks.append(ts)
                    if s in (4, 12):
                        put(drums, clap(), ts, 0.5)
                    put(drums, hat(), ts, 0.14)
                elif s % 2 == 0:  # tic-tac de la frise
                    put(drums, hat(), ts, 0.16 if pos == 0 else 0.09)
                    if pos == 0 and q == 0:
                        put(drums, kick(0.3, 90, 50, 0.2), ts, 0.35)

            # basse
            if style in ("house", "pop") and grooving and pos == 2:
                put(bass, bass_note(root, beat / 2, "saw"), ts, 0.6)
            if style == "speed" and grooving and s % 2 == 0:
                put(bass, bass_note(root + (12 if s % 8 == 6 else 0), beat / 2.2, "saw"), ts, 0.5)
            if style == "lofi" and grooving and s in (0, 8, 14):
                put(bass, bass_note(root, beat * (1.8 if s < 14 else 0.4), "sub"), ts, 0.55)
            if style == "epic" and grooving and pos == 0:
                put(bass, bass_note(root, beat * 0.95, "saw"), ts, 0.55)

            # mélodie / arpèges
            arp = ch + [ch[0] + 12]
            if style in ("house", "pop") and grooving and s % 2 == 0:
                m = arp[(s // 2) % len(arp)] + 12
                put(lead, pluck(m, 0.3, 2600 if style == "house" else 3800), ts, 0.16)
            if style == "speed" and grooving:
                m = arp[s % len(arp)] + 12
                put(lead, pluck(m, 0.14, 4200, sq=True), ts, 0.1)
            if style == "trap" and grooving and s in (0, 3, 6, 8, 11, 14):
                put(lead, pluck(arp[[0, 2, 1, 3, 2, 1][[0, 3, 6, 8, 11, 14].index(s)]] + 12, 0.45, 2200), ts, 0.13)
            if style == "lofi" and s in (0, 6, 11) and grooving:
                for k, m in enumerate(ch):
                    put(lead, epiano(m + 12, 1.1), ts + k * 0.012, 0.22)
            if style == "epic" and s % 2 == 0:
                m = arp[(s // 2) % len(arp)] + 12
                put(lead, pluck(m, 0.32, 2400), ts, 0.12 if grooving else 0.08)

    # montée avant le groove et avant la carte de fin ; impact final
    put(fx, riser(min(1.2, full - 0.1)), full - min(1.2, full - 0.1), 0.35)
    if style == "epic":
        put(fx, riser(1.6), drop - 1.6, 0.4)
        put(fx, crash(), drop, 0.45)
    put(fx, riser(0.9), te - 0.9, 0.3)
    put(drums, kick(0.9, 140, 35), te, 1.0)
    kicks.append(te)
    put(fx, crash(2.5), te, 0.5)
    ci = int(np.floor((te - full) / bar)) % 4
    tail = max(0.5, dur - te)
    put(harm, pad_chord(chords[0], tail, cut=1800), te, 0.5)
    put(lead, pluck(chords[0][0] + 24, 1.2, 3000), te, 0.12)

    # sidechain : la nappe et la basse respirent sur la grosse caisse
    sc = np.ones(n)
    tt = np.arange(n) / SR
    for k in kicks:
        i = int(k * SR)
        j = min(n, i + int(0.3 * SR))
        sc[i:j] = np.minimum(sc[i:j], 1 - 0.55 * np.exp(-(tt[i:j] - k) / 0.09))
    harm *= sc
    bass *= sc

    lead = delay(lead, beat * 0.75, 0.3)
    wet = reverb(harm + 0.6 * lead + 0.15 * drums, 2.0, 0.22)
    mono = drums + bass
    mix = np.stack([mono, mono]) + wet + np.stack([fx, fx]) * 0.9
    if style == "lofi":
        crack = (RNG.random(n) > 0.9993) * RNG.standard_normal(n) * 0.25 + lp(RNG.standard_normal(n), 3000) * 0.004
        mix += np.stack([crack, crack])

    # intro filtrée : on ouvre le filtre jusqu'au début du groove
    ramp = np.clip(tt / max(full, 0.1), 0, 1) ** 1.5
    dull = np.stack([lp(ch, 700) for ch in mix])
    mix = dull * (1 - ramp) + mix * ramp
    # fondu final
    fade = np.clip((dur - tt) / 0.6, 0, 1)
    return mix * fade


def load_wav(path):
    with wave.open(path) as w:
        x = np.frombuffer(w.readframes(w.getnframes()), "<i2").astype(np.float32) / 32767
        return x.reshape(-1, w.getnchannels()).T


def main():
    name, sfx_json, sfx_wav, out = sys.argv[1:5]
    data = json.load(open(sfx_json, encoding="utf-8"))
    dur, te = float(data["duration"]), float(data["endCardAt"])
    p = PRESETS[name]
    style, bpm, full = p[:3]
    drop = p[3] if len(p) > 3 else None
    music = compose(style, bpm, full, dur, te, drop)
    rms = np.sqrt(np.mean(music ** 2))
    music *= 10 ** (-21 / 20) / rms  # musique à -21 dBFS RMS, sous les bruitages
    sfx = load_wav(sfx_wav)
    n = min(sfx.shape[1], music.shape[1])
    mix = sfx[:, :n] * 0.95 + music[:, :n]
    mix = np.tanh(mix * 1.1) / np.tanh(1.1)  # limiteur doux
    mix *= 10 ** (-1 / 20) / np.max(np.abs(mix))
    with wave.open(out, "wb") as w:
        w.setnchannels(2)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes((mix.T * 32767).astype("<i2").tobytes())
    print(f"{out} : {style} {bpm} bpm, groove à {full:.2f} s, fin à {te:.2f} s")


if __name__ == "__main__":
    main()
