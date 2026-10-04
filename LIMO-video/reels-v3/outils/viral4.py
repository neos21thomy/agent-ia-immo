"""Film V4 « Ta journée avec LIMO » : une journée de conseiller, heure par heure (7:30 → 21:00), racontée par
la mascotte d'une voix douce (voix française Siwis générée en local par `hyperframes tts`, fichiers dans
sources/voix/tts/). Direction « premium calme » (kit motion-design-skills) : pas de rebond, fondus enchaînés,
une seule animation « héros » par plan, une horloge qui défile en fil rouge, un seul moment fort (18:30).
Données affichées = exemples fictifs.

Usage : python3 outils/viral4.py   (réécrit reels/viral-04-ta-journee-avec-limo.html et complète outils/voix.json)
"""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from cine import COMMON, FACES  # noqa: E402
from lifestyle import V  # noqa: E402
from premium2 import SHELL  # noqa: E402
from premium3 import CSS  # noqa: E402
from premium4 import SH4  # noqa: E402

NAME = "viral-04-ta-journee-avec-limo"
# (début, fin) des scènes ; voix : (fichier, départ, texte affiché)
SC = [(0, 4.3), (4.3, 8.6), (8.6, 13.6), (13.6, 18.6), (18.6, 24.3), (24.3, 28.6), (28.6, 32.9)]
T_OUT = 32.9
DUR = 38.2
VO = [
    ("tts/v4-01.wav", 0.7, 2.30, "Bonjour Julien. Ta journée est prête."),
    ("tts/v4-02.wav", 4.9, 2.92, "En route ? Je t’ai résumé ton rendez-vous de 10 h."),
    ("tts/v4-03.wav", 9.0, 4.29, "Pendant ton estimation, je prends les notes. Le compte rendu est déjà prêt."),
    ("tts/v4-04.wav", 14.1, 3.84, "Visite terminée. Deux acquéreurs correspondants ont été prévenus."),
    ("tts/v4-05.wav", 19.1, 4.27, "J’ai relancé tes 6 contacts du jour. Mme Martin te voit vendredi."),
    ("tts/v4-06.wav", 25.4, 1.69, None),
    ("tts/v4-07.wav", 29.3, 2.01, None),
    ("tts/v4-08.wav", 33.6, 2.50, None),
]
PRE = (V("v1", "agent-voiture-grade", 4.0, 4.9, 1) + V("v2", "vendeuse-canape-grade", 8.3, 5.0, 2)
       + V("v3", "villa-recul-lent-grade", 13.3, 5.6, 3) + V("v4", "femme-vent-grade", 24.0, 4.9, 4))
EXTRA_CSS = """
      .vo { display: inline-block; max-width: 900px; padding: 16px 28px; border-radius: 26px; background: rgba(10,10,30,.42); backdrop-filter: blur(14px); -webkit-backdrop-filter: blur(14px); color: #fff; font-family: Inter, sans-serif; font-weight: 600; font-size: 40px; line-height: 1.3; text-shadow: 0 2px 10px rgba(0,0,0,.35); }
      .hd2 { font-family: Inter, sans-serif; font-size: 25px; letter-spacing: .08em; color: rgba(255,255,255,.78); }
      .big { display: block; margin-top: 8px; font-family: Montserrat, sans-serif; font-weight: 800; font-size: 54px; line-height: 1.12; }
      .ln { display: flex; align-items: center; gap: 18px; margin-top: 20px; font-family: Inter, sans-serif; font-size: 36px; line-height: 1.3; }
      .ln svg { flex: none; width: 40px; height: 40px; color: #2cc4b5; }
"""
BODY = SH4 + r"""
        const TOP = document.getElementById("root");
        tl.set([C.barT, C.barB], { opacity: 0 }, 0);
        const EZ = "power2.inOut", EO = "power2.out";
        const WARM = (tint) => `<img src="assets/img/bien-mas-lavande.jpg" alt="" style="position:absolute;left:-120px;top:-120px;width:1320px;height:2160px;object-fit:cover;filter:blur(36px) brightness(.55) saturate(1.2)" /><div style="position:absolute;inset:0;background:${tint}"></div>`;
        // scène en fondu enchaîné (0,6 s), légère dérive de caméra
        const scene = (t0, t1, html = "", css = {}) => {
          const l = FX.ab(TOP, Object.assign({ left: "0", top: "0", width: "1080px", height: "1920px", overflow: "hidden" }, css), html);
          tl.set(l, { opacity: 0 }, 0);
          tl.to(l, { opacity: 1, duration: 0.6, ease: EZ }, Math.max(0, t0 - 0.3));
          tl.to(l, { opacity: 0, duration: 0.6, ease: EZ }, t1 - 0.3);
          return l;
        };
        const drift = (id, t0, t1) => tl.fromTo(document.getElementById(id), { scale: 1.06 }, { scale: 1.0, duration: t1 - t0 + 0.6, ease: "none" }, t0 - 0.3);
        const shadeIn = (l) => FX.ab(l, { inset: "0", background: "linear-gradient(180deg, rgba(5,6,15,.6) 0%, rgba(5,6,15,.1) 34%, rgba(5,6,15,.15) 58%, rgba(5,6,15,.7) 100%)" });
        // carte héros : entre en douceur, puis ses lignes une à une (60 ms de décalage, sans rebond)
        const hero = (p, t, head, big, lines, top = 430) => {
          const g = FX.glass(p, { left: "70px", width: "940px", top: top + "px", padding: "30px 36px 34px", boxSizing: "border-box" },
            `<span class="hd2">${head}</span><b class="big">${big}</b>` + lines.map((l) => `<div class="ln">${K.icon(l[0])}<span>${l[1]}</span></div>`).join(""));
          tl.set(g, { opacity: 0 }, 0);
          tl.fromTo(g, { opacity: 0, y: 24 }, { opacity: 1, y: 0, duration: 0.6, ease: EO, immediateRender: false }, t);
          K.$$(".ln", g).forEach((r, i) => { tl.set(r, { opacity: 0 }, 0); tl.fromTo(r, { opacity: 0, y: 14 }, { opacity: 1, y: 0, duration: 0.5, ease: EO, immediateRender: false }, t + 0.7 + i * 0.55); K.sfx(t + 0.7 + i * 0.55, "sparkle", 0.05); });
          FX.sheen(g, t + 0.5, 1.4);
          return g;
        };
        // sous-titre de la voix (doux, en bas)
        const vo = (t, d, txt) => {
          const e = FX.ab(TOP, { left: "60px", right: "60px", top: "1150px", textAlign: "center", zIndex: 34 }, `<span class="vo">${txt}</span>`);
          tl.set(e, { opacity: 0 }, 0);
          tl.fromTo(e, { opacity: 0, y: 10 }, { opacity: 1, y: 0, duration: 0.4, ease: EO, immediateRender: false }, t - 0.1);
          tl.to(e, { opacity: 0, duration: 0.4, ease: EZ }, t + d + 0.3);
        };

        // ── fil rouge : horloge qui défile + barre de la journée
        const TIMES = ["7:30", "9:15", "11:00", "14:30", "17:00", "18:30", "21:00"];
        const HOURS = [7.5, 9.25, 11, 14.5, 17, 18.5, 21];
        const hud = FX.ab(TOP, { left: "0", right: "0", top: "150px", textAlign: "center", zIndex: 35 },
          `<div style="display:inline-block;position:relative;height:96px;width:290px;border-radius:999px;overflow:hidden;background:rgba(255,255,255,.16);border:1.5px solid rgba(255,255,255,.38);backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);box-shadow:0 14px 40px rgba(0,0,0,.25)"><div class="strip" style="position:absolute;left:0;right:0;top:0">${TIMES.map((t) => `<div style="height:96px;line-height:96px;font-family:Inter,sans-serif;font-weight:700;font-size:60px;color:#fff;letter-spacing:-.01em">${t}</div>`).join("")}</div></div>
<div style="margin:18px auto 0;width:520px;height:8px;border-radius:8px;background:rgba(255,255,255,.22);overflow:hidden"><div class="fill" style="height:100%;width:100%;border-radius:8px;background:linear-gradient(90deg,#f3a35b,#2cc4b5);transform-origin:0 50%"></div></div>`);
        const strip = K.$(".strip", hud), fill = K.$(".fill", hud);
        tl.set(hud, { opacity: 0 }, 0); tl.to(hud, { opacity: 1, duration: 0.6, ease: EO }, 0.2);
        tl.set(strip, { y: 0 }, 0); tl.set(fill, { scaleX: (HOURS[0] - 7) / 14 }, 0);
        SC.forEach(([t0], i) => {
          if (!i) return;
          tl.to(strip, { y: -96 * i, duration: 0.7, ease: EZ }, t0 - 0.35);
          tl.to(fill, { scaleX: (HOURS[i] - 7) / 14, duration: 0.9, ease: EZ }, t0 - 0.35);
          K.sfx(t0 - 0.3, "tick", 0.12, 0, { f: 1500 });
        });
        tl.to(hud, { opacity: 0, duration: 0.5, ease: EZ }, SC[5][0] - 0.4);
        tl.to(hud, { opacity: 1, duration: 0.6, ease: EZ }, SC[6][0] - 0.1);
        tl.to(hud, { opacity: 0, duration: 0.4, ease: EZ }, T_OUT - 0.4);

        // ── 7:30 · le matin
        const s1 = scene(...SC[0], WARM("linear-gradient(180deg,rgba(243,163,91,.4) 0%,rgba(107,79,224,.3) 60%,rgba(10,8,30,.65) 100%)"));
        C.leak(0.1, 3.4);
        hero(s1, 1.0, "LIMO · TA JOURNÉE", "Mardi 6 octobre", [["clock", "3 rendez-vous · le premier à 10:00"], ["bell", "2 relances prioritaires"], ["users", "1 nouveau prospect : Mme Leroy"]]);
        // ── 9:15 · en voiture
        const s2 = scene(...SC[1]); shadeIn(s2); drift("v1", ...SC[1]);
        hero(s2, 5.0, "LIMO · AVANT TON RENDEZ-VOUS", "M. et Mme T. · 10:00", [["home", "Vendent pour se rapprocher de leurs petits-enfants"], ["wrench", "Travaux évoqués : toiture, 15&nbsp;000&nbsp;€"], ["msg", "Dernier échange : 28 septembre"]]);
        // ── 11:00 · l'estimation (dictée → compte rendu)
        const s3 = scene(...SC[2]); shadeIn(s3); drift("v2", ...SC[2]);
        const wv = FX.glass(s3, { left: "70px", width: "940px", top: "430px", padding: "28px 36px", boxSizing: "border-box" },
          `<span class="hd2">LIMO · PRISE DE NOTES</span><div class="bars" style="display:flex;align-items:center;gap:9px;height:120px;margin-top:14px">${Array.from({ length: 40 }, () => `<i style="display:block;flex:1;height:100%;border-radius:6px;background:#2cc4b5;transform-origin:50% 50%"></i>`).join("")}</div><div class="cr" style="display:flex;align-items:center;gap:18px;margin-top:18px"><span style="width:62px;height:62px;border-radius:50%;background:#2cc4b5;display:flex;align-items:center;justify-content:center">${K.icon("check")}</span><span><b style="display:block;font-family:Montserrat,sans-serif;font-weight:800;font-size:44px">Compte rendu prêt</b><span style="font-family:Inter,sans-serif;font-size:31px;opacity:.88">envoyé aux vendeurs · 11:42</span></span></div>`);
        K.$$("svg.i", wv).forEach((s) => (s.style.cssText = "width:36px;height:36px;color:#fff"));
        tl.set(wv, { opacity: 0 }, 0); tl.fromTo(wv, { opacity: 0, y: 24 }, { opacity: 1, y: 0, duration: 0.6, ease: EO, immediateRender: false }, 9.0);
        K.$$(".bars i", wv).forEach((b, i) => {
          tl.set(b, { scaleY: 0.12 }, 0);
          for (let k = 0; k < 6; k++) tl.to(b, { scaleY: 0.18 + 0.8 * Math.abs(Math.sin(i * 0.55 + k * 1.3)) * (0.5 + 0.5 * Math.abs(Math.cos(i * 0.21 + k))), duration: 0.42, ease: "sine.inOut" }, 9.3 + k * 0.42);
          tl.to(b, { scaleY: 0.12, duration: 0.4, ease: EZ }, 11.9);
        });
        const cr = K.$(".cr", wv); tl.set(cr, { opacity: 0 }, 0); tl.fromTo(cr, { opacity: 0, y: 12 }, { opacity: 1, y: 0, duration: 0.5, ease: EO, immediateRender: false }, 12.2); K.sfx(12.2, "success", 0.1);
        // ── 14:30 · après la visite
        const s4 = scene(...SC[3]); shadeIn(s4); drift("v3", ...SC[3]);
        hero(s4, 14.2, "LIMO · VISITE TERMINÉE", "Villa contemporaine · 4 ch.", [["send", "Compte rendu envoyé au propriétaire"], ["users", "2 acquéreurs correspondants prévenus"], ["clock", "Contre-visite proposée samedi 11:00"]]);
        // ── 17:00 · les relances
        const s5 = scene(...SC[4], WARM("linear-gradient(180deg,rgba(243,140,91,.45) 0%,rgba(107,79,224,.35) 60%,rgba(10,8,30,.7) 100%)"));
        const rl = hero(s5, 19.2, "LIMO · RELANCES DU JOUR", `<span class="ct">0</span> / 6 envoyées`, [["check", "Mme Martin : rendez-vous vendredi 10:00"], ["check", "M. Bernard : offre bien reçue"], ["check", "4 autres : réponses en attente, je suis"]]);
        K.count(K.$(".ct", rl), 6, 19.9, 1.6, (v) => String(Math.round(v)), {});

        // ── 18:30 · le moment fort : plus d'interface, juste la vie
        const s6 = scene(...SC[5]); drift("v4", ...SC[5]);
        FX.ab(s6, { inset: "0", background: "linear-gradient(180deg, rgba(5,6,15,.35) 0%, rgba(5,6,15,0) 40%, rgba(5,6,15,0) 70%, rgba(5,6,15,.45) 100%)" });
        C.leak(24.4, 3.6);
        FX.rise(s6, "Et toi…", { top: "330px", fontSize: "88px", fontWeight: "700", textShadow: "0 6px 30px rgba(0,0,0,.4)" }, 25.2, { snd: false, st: 0.04 });
        FX.rise(s6, "tu rentres [plus] [tôt.]", { top: "440px", fontSize: "94px", textShadow: "0 8px 36px rgba(0,0,0,.45)" }, 26.0, { snd: false, st: 0.04, accent: "#ffe2b8" });
        // ── 21:00 · la nuit
        const s7 = scene(...SC[6], `<div style="position:absolute;inset:0;background:radial-gradient(ellipse at 50% 35%,#2a2160 0%,#0d0f2a 60%,#05060f 100%)"></div><div style="position:absolute;left:640px;top:330px;width:240px;height:240px;border-radius:50%;background:radial-gradient(circle at 40% 40%,#fff7e0 0%,#f3e3b0 45%,rgba(243,227,176,0) 72%);opacity:.85"></div>`);
        const sp = K.sparkles(s7, 540, 760, 22, 500, 420, 5);
        sp.forEach((o, i) => { const e = o.el; tl.set(e, { x: o.dx, y: o.dy, scale: 0.6 }, 0); tl.fromTo(e, { opacity: 0.15 }, { opacity: 0.9, duration: 1.1 + (i % 4) * 0.3, ease: "sine.inOut", yoyo: true, repeat: 2, immediateRender: false }, 28.6 + (i % 5) * 0.2); });
        const nt = FX.ab(s7, { left: "60px", right: "60px", top: "1120px", textAlign: "center", fontFamily: "Montserrat, sans-serif", fontWeight: "800", fontSize: "84px", color: "#fff", lineHeight: "1.1" }, `Dors bien. 🌙<div style="margin-top:16px;font-family:Inter,sans-serif;font-weight:500;font-size:40px;color:rgba(255,255,255,.85)">Je veille sur tes dossiers.</div>`);
        tl.set(nt, { opacity: 0 }, 0); tl.fromTo(nt, { opacity: 0, y: 16 }, { opacity: 1, y: 0, duration: 0.8, ease: EO, immediateRender: false }, 29.3);

        // sous-titres de la voix
        VO.forEach(([, t, d, txt]) => { if (txt) vo(t, d, txt); });

        // ── la mascotte : petite, douce, elle « parle » (antenne qui s'allume)
        const M = N.mascot({ left: "390px", top: "760px", width: "300px" }, { expr: "happy" });
        TOP.appendChild(M.el); M.el.style.zIndex = "30";
        const ant = K.$(".ant", M.el);
        const speak = (t, d) => { const n = Math.max(1, Math.round(d / 0.36)); tl.fromTo(ant, { opacity: 0.2 }, { opacity: 1, duration: 0.18, ease: "sine.inOut", yoyo: true, repeat: n * 2 - 1, immediateRender: false }, t); tl.set(ant, { opacity: 0 }, t + n * 0.36 + 0.05); };
        VO.forEach(([, t, d]) => { if (t < T_OUT) speak(t, d); });
        tl.set(M.el, { opacity: 0 }, 0);
        tl.set(M.el, { x: 340, y: 480, scale: 0.55 }, 0);
        tl.to(M.el, { opacity: 1, duration: 0.6, ease: EO }, 0.4);
        M.float(0.5, 23.4, 8);
        [2.6, 6.8, 11.0, 16.2, 21.6].forEach((t) => M.blink(t));
        M.expr("wink", 3.4, false); M.expr("happy", 4.3, false);
        M.expr("heart", 22.9, false);
        tl.to(M.el, { opacity: 0, duration: 0.5, ease: EZ }, SC[5][0] - 0.4);
        // la nuit : au centre, elle s'endort doucement
        tl.set(M.el, { x: 0, y: -40, scale: 0.95 }, SC[6][0] - 0.2);
        tl.to(M.el, { opacity: 1, duration: 0.7, ease: EO }, SC[6][0]);
        M.expr("happy", SC[6][0], false); M.blink(30.0); M.expr("sleep", 31.4, false);
        M.float(28.6, 4.0, 10);
        tl.to(M.el, { opacity: 0, duration: 0.4, ease: EZ }, T_OUT - 0.4);
        outro(T_OUT);
""".replace("T_OUT", str(T_OUT)).replace("SC = null", "")

if __name__ == "__main__":
    body = "        const SC = " + json.dumps(SC) + ";\n        const VO = " + json.dumps([[v[0], v[1], v[2], v[3]] for v in VO], ensure_ascii=False) + ";\n" + BODY
    html = SHELL.format(title="Ta journée avec LIMO", faces=FACES, css=(CSS + EXTRA_CSS).strip("\n"), body=(COMMON + body).strip("\n"), dur=DUR, name=NAME)
    html = html.replace('      <section id="s-main"', PRE + '      <section id="s-main"', 1)
    (HERE.parent / "reels" / f"{NAME}.html").write_text(html, encoding="utf-8")
    vj = HERE / "voix.json"
    data = json.loads(vj.read_text(encoding="utf-8"))
    data[NAME] = [[v[0], v[1]] for v in VO]
    vj.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    print("reels/" + NAME + ".html")
