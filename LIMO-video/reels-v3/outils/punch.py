"""Films « punch » sur les voix émotion (sources/voix/emotion/) : pas de sous-titres continus, seulement les
mots-clés en très grand au moment où ils sont dits ; coupes franches ; noir et blanc pendant la galère,
la couleur revient quand Limo arrive. E1 Ce qu'on ne voit pas · E2 23 heures · E3 Le mandat d'à côté ·
E4 Seul, mais pas tout seul · E6 Lettre à un conseiller. Données affichées = exemples fictifs.

Usage : python3 outils/punch.py   (réécrit reels/punch-*.html et complète outils/voix.json)
"""
import json
import pathlib

from cine import COMMON, FACES
from premium2 import SHELL
from premium3 import CSS
from premium4 import SH4

O = 0.3
GRAY = "grayscale(1) contrast(1.15) brightness(.8)"
TEAL, PINK, LILA = "#2cc4b5", "#ff8f8f", "#d9ceff"
DARK = ["#2a2c40", "#1a1c2a", "#3a3d55"]
NIGHT = ["#1d2a7a", "#2b1f5e", "#0f2a4a"]
TEALC = ["#2cc4b5", "#6b4fe0", "#1d6f8a"]

PW = r"""
        // mot-choc plein écran : surgit en grand, tient, disparaît net
        const PW = (t, txt, o = {}) => {
          const inner = o.box ? `<span style="display:inline-block;padding:14px 30px;background:${o.box};color:${o.bc || "#fff"};border-radius:18px;${o.border ? "border:8px solid " + o.border + ";" : ""}transform:rotate(${o.rot ?? -3}deg)">${txt}</span>` : txt;
          const e = FX.ab(root, { left: "40px", right: "40px", top: (o.top ?? 760) + "px", textAlign: "center", zIndex: 30, fontFamily: "Montserrat, sans-serif", fontWeight: "800", fontSize: (o.fs ?? 128) + "px", lineHeight: "1.02", letterSpacing: "-0.02em", color: o.c || "#fff", textShadow: o.box ? "none" : "0 10px 40px rgba(0,0,0,.6)" }, inner + (o.strike ? `<i class="st" style="position:absolute;left:12%;right:12%;top:50%;height:12px;margin-top:-6px;background:#ff5b5b;border-radius:6px;transform-origin:0 50%"></i>` : ""));
          tl.set(e, { opacity: 0 }, 0);
          tl.fromTo(e, { opacity: 0, scale: o.from ?? 1.7, filter: "blur(12px)" }, { opacity: 1, scale: 1, filter: "blur(0px)", duration: 0.22, ease: "power4.out", immediateRender: false }, t);
          tl.to(e, { opacity: 0, scale: 0.94, duration: 0.1, ease: "power2.in" }, o.end);
          K.sfx(t, o.snd || "thump", o.g ?? 0.2);
          if (o.shake) { tl.to(e, { x: 14, duration: 0.04, yoyo: true, repeat: 7, ease: "none" }, t + 0.18); tl.set(e, { x: 0 }, t + 0.5); K.sfx(t, "slam", 0.3); }
          if (o.strike) { const s = K.$(".st", e); tl.set(s, { scaleX: 0 }, 0); tl.to(s, { scaleX: 1, duration: 0.3, ease: "power2.out" }, t + 0.7); K.sfx(t + 0.7, "swipe", 0.2); }
          return e;
        };
        const photo = (t0, t1, src, o = {}) => {
          const l = FX.layer(t0, t1);
          const p = FX.ab(l, { left: "-60px", top: "-100px", width: "1200px", height: "2120px" }, `<img src="assets/img/${src}.jpg" alt="" style="width:100%;height:100%;object-fit:cover;object-position:${o.pos || "50% 50%"};filter:${o.gray ? "GRAY" : "none"}" />`);
          tl.fromTo(p, { scale: o.z0 ?? 1.25 }, { scale: o.z1 ?? 1.05, duration: t1 - t0, ease: "power1.out" }, t0);
          FX.ab(l, { inset: "0", background: "rgba(5,6,15,.38)" });
          return l;
        };
        const vshot = (id, t0, t1) => {
          const v = document.getElementById(id);
          const l = FX.layer(t0, t1);
          FX.ab(l, { inset: "0", background: "rgba(5,6,15,.36)" });
          tl.fromTo(v, { scale: 1.2 }, { scale: 1.04, duration: 0.45, ease: "power3.out" }, t0);
          tl.to(v, { scale: 1.1, duration: Math.max(0.1, t1 - t0 - 0.45), ease: "none" }, t0 + 0.45);
          return l;
        };
        const cut = (t, flash) => { if (flash) C.flash(t, "#ffffff", 0.75); K.sfx(t, "whoosh", 0.1, 0, { d: 0.25, f0: 300, f1: 2400, pk: 0.4 }); };
""".replace('"GRAY"', '"' + GRAY + '"')


def build(shots, punches, extra, outro_t):
    """shots : ("v", src, t0, t1, ms, gray) | ("p", img, t0, t1, gray, pos) | ("a", t0, t1, colors)"""
    pre, js, n = "", [], 0
    for i, s in enumerate(shots):
        kind = s[0]
        t0 = s[2] if kind in "vp" else s[1]
        if i:
            js.append(f"cut({t0}, {str(kind == 'v' and not s[5] or kind == 'p' and not s[4]).lower()});")
        if kind == "v":
            _, src, t0, t1, ms, gray = s
            n += 1
            pre += (f'      <video id="w{n}" class="clip" src="assets/video/{src}.mp4" data-start="{t0}" data-duration="{round(t1 - t0, 2)}"'
                    + (f' data-media-start="{ms}"' if ms else "") + f' data-track-index="{n}" muted playsinline style="position:absolute;left:0;top:0;width:1080px;height:1920px;object-fit:cover;filter:{GRAY if gray else "none"}"></video>\n')
            js.append(f'vshot("w{n}", {t0}, {t1});')
        elif kind == "p":
            _, img, t0, t1, gray, pos = s
            js.append(f'photo({t0}, {t1}, "{img}", {{ gray: {str(gray).lower()}, pos: "{pos}" }});')
        else:
            _, t0, t1, colors = s
            js.append(f'lay({t0}, {t1}, null, {{ colors: {json.dumps(colors)}, a: 0.5 }});')
    ps = sorted(punches, key=lambda p: p[0])
    for i, (t, txt, o) in enumerate(ps):
        o = dict(o)
        if "end" not in o:
            nxt = next((q[0] for q in ps[i + 1:] if q[2].get("top", 760) == o.get("top", 760)), outro_t)
            o["end"] = round(min(t + o.pop("hold", 1.4), nxt - 0.06, outro_t - 0.1), 2)
        o.pop("keep", None)
        js.append(f'PW({t}, {json.dumps(txt.replace("|", "<br>"), ensure_ascii=False)}, {json.dumps(o, ensure_ascii=False)});')
    js.append("const TOP = document.getElementById(\"root\");")
    js.append(extra.strip().replace("(root,", "(TOP,"))
    js.append(f"outro({outro_t});")
    return pre, PW + "\n".join("        " + l for l in "\n".join(js).split("\n")) + "\n"


VOICE, FILMS = {}, {}

# ---------------------------------------------------------------- E1 · Ce qu'on ne voit pas (Emilie)
VOICE["punch-01-ce-quon-ne-voit-pas"] = [["emotion/Emilie-10h50m58.mp3", O]]
FILMS["punch-01-ce-quon-ne-voit-pas"] = ("LIMO, ce qu'on ne voit pas", 35.8, 30.75, [
    ("v", "villa-recul-lent-grade", 0, 3.3, 0, True),
    ("v", "vendeuse-canape-grade", 3.3, 7.7, 0.3, True),
    ("v", "agent-voiture-grade", 7.7, 12.7, 0, True),
    ("v", "femme-vent-grade", 12.7, 16.3, 1.0, True),
    ("p", "bien-pierre-balcon", 16.3, 20.5, True, "50% 40%"),
    ("a", 20.5, 21.4, DARK),
    ("v", "villa-recul-lent-grade", 21.4, 26.0, 4.5, False),
    ("a", 26.0, 30.75, TEALC),
], [
    (0.55, "Ils pensent…", {"fs": 96, "c": LILA}), (1.5, "qu’on fait|visiter.", {"fs": 130}),
    (3.9, "Le téléphone", {}), (4.9, "à côté de|l’assiette", {"fs": 110}), (6.0, "le dimanche.", {"c": PINK, "hold": 1.6}),
    (8.4, "Les estimations", {"fs": 104}), (9.2, "du soir.", {"c": PINK}),
    (10.0, "Le compromis", {"fs": 112}), (11.0, "qui tombe.", {"c": PINK, "shake": True, "fs": 150, "hold": 2.0}),
    (13.2, "Des mois", {}), (13.8, "sans vente.", {"c": PINK, "fs": 150}), (15.0, "Le bon choix ?", {"fs": 110, "hold": 1.3}),
    (17.3, "Les projets", {}), (18.0, "des autres…", {}), (18.9, "…avant|les nôtres.", {"c": LILA, "hold": 1.5}),
    (20.6, "Et pourtant.", {"fs": 120, "hold": 0.85}),
    (22.4, "Les clés.", {"box": TEAL, "fs": 150, "snd": "slam", "hold": 1.5}), (24.1, "Pourquoi on fait|ce métier.", {"fs": 104, "hold": 1.8}),
    (27.9, "Tout le reste.", {"top": 900, "fs": 110}), (29.3, "Ce qui compte.", {"top": 900, "c": TEAL, "fs": 120, "hold": 1.4}),
], """
tl.to(logoCard(root, 26.0, 470), { opacity: 0, duration: 0.2 }, 30.5);
""")

# ---------------------------------------------------------------- E2 · 23 heures (Emilie)
VOICE["punch-02-23-heures"] = [["emotion/Emilie-10h52m01.mp3", O]]
FILMS["punch-02-23-heures"] = ("LIMO, 23 heures", 39.3, 34.3, [
    ("a", 0, 4.4, NIGHT),
    ("v", "villa-recul-lent-grade", 4.4, 8.3, 6.0, True),
    ("a", 8.3, 15.0, ["#2b1f5e", "#1a1c2a", "#3a2a6a"]),
    ("v", "femme-vent-grade", 15.0, 19.7, 6.0, True),
    ("v", "agent-voiture-grade", 19.7, 22.3, 0, False),
    ("a", 22.3, 25.95, NIGHT),
    ("a", 25.95, 30.0, TEALC),
    ("v", "villa-recul-lent-grade", 30.0, 34.3, 1.0, False),
], [
    (0.3, "23 h.", {"fs": 320, "snd": "slam", "hold": 1.6}), (2.05, "Les enfants|dorment.", {"fs": 120, "c": LILA, "hold": 2.2}),
    (4.5, "Toi ?", {"fs": 200}), (5.3, "encore devant|l’écran.", {"fs": 112, "hold": 2.8}),
    (8.5, "Un compte rendu", {"top": 620, "fs": 88, "end": 14.6, "box": "rgba(255,255,255,.14)"}),
    (10.74, "3 relances", {"top": 800, "fs": 88, "end": 14.6, "box": "rgba(255,255,255,.14)"}),
    (12.78, "une annonce", {"top": 980, "fs": 88, "end": 14.6, "box": "rgba(255,255,255,.14)"}),
    (15.3, "Une petite voix…", {"fs": 100, "c": LILA, "hold": 2.2}), (17.7, "« J’ai oublié|quelqu’un. »", {"fs": 110, "c": PINK, "shake": True, "hold": 1.9}),
    (20.6, "La liberté.", {"fs": 150, "c": TEAL, "hold": 1.5}), (22.4, "Pas minuit,|seul avec|tes dossiers.", {"fs": 104, "c": PINK, "hold": 3.2}),
    (26.6, "prend le relais.", {"top": 900, "fs": 100, "hold": 0.85}),
    (27.5, "Relances", {"top": 820, "fs": 90, "end": 29.9, "box": "rgba(44,196,181,.35)"}),
    (28.2, "Mails", {"top": 990, "fs": 90, "end": 29.9, "box": "rgba(44,196,181,.35)"}),
    (28.8, "Comptes rendus", {"top": 1160, "fs": 90, "end": 29.9, "box": "rgba(44,196,181,.35)"}),
    (30.0, "Ce soir,", {"fs": 120, "hold": 1.0}), (31.0, "ferme l’ordi.", {"fs": 140, "c": TEAL, "snd": "slam", "hold": 1.6}),
    (32.7, "Limo s’en|souvient.", {"fs": 130, "hold": 1.6}),
], """
tl.to(logoCard(root, 26.1, 470), { opacity: 0, duration: 0.2 }, 29.8);
""")

# ---------------------------------------------------------------- E3 · Le mandat d'à côté (Yariq)
VOICE["punch-03-le-mandat-da-cote"] = [["emotion/Yariq-10h52m37.mp3", O]]
FILMS["punch-03-le-mandat-da-cote"] = ("LIMO, le mandat d'à côté", 40.0, 35.0, [
    ("a", 0, 2.9, DARK),
    ("p", "bien-pierre-balcon", 2.9, 6.6, True, "50% 35%"),
    ("v", "vendeuse-canape-grade", 6.6, 11.6, 0, True),
    ("p", "bien-pierre-balcon", 11.6, 16.8, True, "30% 85%"),
    ("v", "agent-voiture-grade", 16.8, 21.8, 0, True),
    ("a", 21.8, 22.9, DARK),
    ("a", 22.9, 29.2, TEALC),
    ("v", "femme-vent-grade", 29.2, 35.0, 6.0, False),
], [
    (0.35, "Tu connais|ce sentiment.", {"fs": 120, "hold": 2.4}),
    (3.1, "Une maison.", {"fs": 130}), (4.9, "Ton estimation.", {"fs": 112, "c": LILA}),
    (7.7, "Une heure", {"fs": 130}), (8.6, "à l’écouter.", {"fs": 130, "hold": 3.0}),
    (12.1, "Et sur|le portail…", {"fs": 120, "hold": 2.2}),
    (14.9, "Une autre|agence.", {"box": "rgba(10,5,10,.4)", "bc": "#ff5b5b", "border": "#ff5b5b", "rot": -7, "fs": 120, "shake": True, "hold": 1.9}),
    (17.0, "Pas moins bon.", {"fs": 120}), (18.9, "Tu as juste|rappelé…", {"fs": 120}),
    (20.55, "trop tard.", {"fs": 200, "c": PINK, "shake": True, "hold": 2.2}),
    (23.0, "Plus jamais.", {"fs": 140, "c": TEAL, "snd": "slam", "hold": 1.4}),
    (24.6, "Qui rappeler.", {"top": 300, "fs": 110, "hold": 1.4}), (26.1, "Et quand.", {"top": 300, "fs": 120, "c": TEAL, "hold": 0.9}),
    (30.4, "Pas le meilleur…", {"fs": 120, "hold": 2.0}), (32.5, "celui qui est là", {"fs": 110, "hold": 1.2}),
    (33.7, "au bon|moment.", {"fs": 150, "c": TEAL, "snd": "slam", "hold": 1.3}),
], """
const cc = card(root, "phone", "Rappeler Mme Martin", "Estimation lundi · aujourd’hui 9 h", { top: "560px" }, 24.7, { check: true });
const mm = msgCard(root, "LIMO · MESSAGE PRÊT", "« Bonjour Madame Martin, avez-vous pu réfléchir à notre estimation ? »", "Envoyer", { top: "740px" }, 27.0);
tapSend(mm, 28.5);
tl.to([cc, mm], { opacity: 0, duration: 0.2 }, 29.0);
""")

# ---------------------------------------------------------------- E4 · Seul, mais pas tout seul (Emilie)
VOICE["punch-04-pas-tout-seul"] = [["emotion/Emilie-10h53m35.mp3", O]]
FILMS["punch-04-pas-tout-seul"] = ("LIMO, pas tout seul", 38.6, 33.6, [
    ("v", "agent-voiture-grade", 0, 4.5, 0, False),
    ("v", "villa-recul-lent-grade", 4.5, 11.6, 2.0, True),
    ("a", 11.6, 16.1, DARK),
    ("p", "bien-lac", 16.1, 17.55, True, "50% 50%"),
    ("p", "bien-chalet", 17.55, 18.55, True, "50% 50%"),
    ("p", "bien-mas-lavande", 18.55, 19.55, True, "50% 50%"),
    ("p", "bien-terrasse-mer", 19.55, 20.4, True, "50% 50%"),
    ("p", "villa-photo", 20.4, 21.85, True, "50% 50%"),
    ("v", "vendeuse-canape-grade", 21.85, 23.35, 2.0, True),
    ("a", 23.35, 30.3, TEALC),
    ("v", "femme-vent-grade", 30.3, 33.6, 9.0, False),
], [
    (0.6, "Indépendant,", {"fs": 120}), (2.3, "libre.", {"fs": 220, "c": TEAL, "snd": "slam", "hold": 2.0}),
    (4.7, "Parfois…", {"fs": 120}), (5.9, "seul.", {"fs": 240, "c": PINK, "hold": 1.3}),
    (7.5, "Pas de collègue.", {"fs": 110}), (9.6, "Pas d’assistante.", {"fs": 110}),
    (11.8, "Personne", {"fs": 130, "hold": 0.9}), (12.8, "« T’as relancé|Mme Martin ? »", {"fs": 100, "c": LILA, "hold": 2.5}),
    (16.2, "Tu fais tout.", {"fs": 130, "hold": 1.3}),
    (17.6, "Le terrain", {"fs": 130}), (18.6, "L’admin", {"fs": 130}), (19.6, "Les réseaux", {"fs": 130}), (20.4, "La compta", {"fs": 130}),
    (21.9, "Et tu tiens.", {"fs": 130, "c": PINK, "hold": 1.4}),
    (24.4, "Le collègue|que tu n’as pas.", {"top": 900, "fs": 100, "hold": 1.3}),
    (26.6, "Mandats", {"top": 850, "fs": 90, "end": 28.6, "box": "rgba(44,196,181,.35)"}),
    (27.3, "Clients", {"top": 1010, "fs": 90, "end": 28.6, "box": "rgba(44,196,181,.35)"}),
    (27.9, "Acquéreurs", {"top": 1170, "fs": 90, "end": 28.6, "box": "rgba(44,196,181,.35)"}),
    (28.8, "Il n’oublie|rien.", {"top": 880, "fs": 130, "c": TEAL, "snd": "slam", "hold": 1.4}),
    (30.35, "Tu restes libre.", {"fs": 120, "hold": 1.2}), (31.6, "Juste plus|tout seul.", {"fs": 140, "c": TEAL, "snd": "slam", "hold": 1.9}),
], """
tl.to(logoCard(root, 23.4, 470), { opacity: 0, duration: 0.2 }, 30.1);
""")

# ---------------------------------------------------------------- E6 · Lettre à un conseiller (Yariq)
VOICE["punch-05-lettre-a-un-conseiller"] = [["emotion/Yariq-10h54m31.mp3", O]]
FILMS["punch-05-lettre-a-un-conseiller"] = ("LIMO, lettre à un conseiller", 41.9, 36.9, [
    ("a", 0, 2.5, DARK),
    ("v", "agent-voiture-grade", 2.5, 7.2, 0, False),
    ("v", "vendeuse-canape-grade", 7.2, 9.95, 1.0, False),
    ("a", 9.95, 14.85, DARK),
    ("p", "bien-pierre-balcon", 14.85, 17.55, True, "50% 50%"),
    ("v", "femme-vent-grade", 17.55, 24.6, 3.0, False),
    ("a", 24.6, 27.25, DARK),
    ("a", 27.25, 33.15, TEALC),
    ("v", "villa-recul-lent-grade", 33.15, 36.9, 2.0, False),
], [
    (0.35, "À toi,", {"fs": 130, "hold": 0.55}), (0.9, "conseiller|immo.", {"fs": 150, "c": TEAL, "snd": "slam", "hold": 1.6}),
    (3.0, "Au téléphone|en vacances.", {"fs": 110}), (5.6, "Le samedi.", {"fs": 140, "c": LILA}),
    (7.3, "Les vendeurs|inquiets.", {"fs": 110}), (8.6, "Les acheteurs|qui doutent.", {"fs": 110}),
    (10.5, "Des mois|sans vente.", {"fs": 130, "c": PINK}), (12.5, "Et tu as|continué.", {"fs": 140, "c": TEAL, "snd": "slam", "hold": 2.2}),
    (15.6, "« Une commission »", {"fs": 84, "strike": True, "hold": 1.9}),
    (17.6, "Tu portes|des vies.", {"fs": 140, "c": TEAL, "snd": "slam", "hold": 2.0}),
    (19.75, "Un divorce.", {"fs": 120}), (20.7, "Une succession.", {"fs": 110}), (21.8, "Un premier enfant.", {"fs": 100}), (23.0, "Une retraite.", {"fs": 120, "hold": 1.5}),
    (24.7, "Tu mérites|mieux.", {"fs": 150, "hold": 2.4}),
    (27.8, "Un bras droit.", {"top": 900, "fs": 120, "c": TEAL, "hold": 1.1}),
    (29.0, "Qui retient tout.", {"top": 900, "fs": 100, "hold": 1.5}), (30.6, "N’oublie personne.", {"top": 900, "fs": 96, "hold": 1.15}),
    (31.8, "Te rend du temps.", {"top": 900, "fs": 100, "c": TEAL, "hold": 1.3}),
    (33.2, "Par des agents|immo.", {"fs": 130, "hold": 2.4}), (35.7, "Pour toi.", {"fs": 220, "c": TEAL, "snd": "slam", "hold": 1.2}),
], """
tl.to(logoCard(root, 27.3, 470), { opacity: 0, duration: 0.2 }, 32.95);
""")

if __name__ == "__main__":
    for name, (title, dur, outro_t, shots, punches, extra) in FILMS.items():
        pre, body = build(shots, punches, extra, outro_t)
        html = SHELL.format(title=title, faces=FACES, css=CSS.strip("\n"), body=(COMMON + SH4 + body).strip("\n"), dur=dur, name=name)
        html = html.replace('      <section id="s-main"', pre + '      <section id="s-main"', 1)
        pathlib.Path(f"reels/{name}.html").write_text(html, encoding="utf-8")
        print("reels/" + name + ".html")
    vj = pathlib.Path("outils/voix.json")
    data = json.loads(vj.read_text()) if vj.exists() else {}
    data.update(VOICE)
    vj.write_text(json.dumps(data, indent=1), encoding="utf-8")
