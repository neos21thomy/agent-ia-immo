"""Film V5 « LIMO veille sur ton secteur » : ancré en Corrèze (photos de villages fournies par Thomy : pont et église,
ruelle en pierre, village au bord de la rivière, halle). Avant : le conseiller débordé au bureau. Avec LIMO : la mascotte,
d'une voix douce (Siwis, `hyperframes tts`), fait le tour du secteur et dit ce qu'elle a déjà fait sur chaque dossier ;
un compteur de tâches faites monte en fil rouge. Moment fort : « Et toi… tu profites. » Même direction « premium calme »
que la V4 (helpers repris de viral4.py). Données affichées = exemples fictifs.

Usage : python3 outils/viral5.py   (réécrit reels/viral-05-limo-veille-sur-ton-secteur.html et complète outils/voix.json)
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
from viral4 import BODY as BODY4, EXTRA_CSS  # noqa: E402

NAME = "viral-05-limo-veille-sur-ton-secteur"
SC = [(0, 4.0), (4.0, 8.8), (8.8, 13.3), (13.3, 18.3), (18.3, 22.8), (22.8, 27.8), (27.8, 32.6)]
T_OUT = 32.6
DUR = 37.9
VO = [
    ("tts/v5-01.wav", 0.6, 1.54, "Avant, tu courais après tout."),
    ("tts/v5-02.wav", 4.6, 2.07, "Maintenant, je veille sur ton secteur."),
    ("tts/v5-03.wav", 9.3, 2.35, "La maison de bourg ? L’annonce est prête."),
    ("tts/v5-04.wav", 13.8, 3.31, "Au bord de la rivière, 3 acquéreurs ont été relancés."),
    ("tts/v5-05.wav", 18.8, 2.41, "Ton estimation de 14 h est prête."),
    ("tts/v5-06.wav", 23.3, 2.82, "Pour le compromis, tous les diagnostics sont arrivés."),
    ("tts/v5-07.wav", 28.7, 1.47, None),
    ("tts/v4-08.wav", 33.3, 2.50, None),
]
PRE = (V("v1", "agent-deborde", 0, 4.0, 1) + V("v2", "maison-contemporaine", 22.5, 5.0, 2)
       + V("v3", "piscine-liberte", 27.5, 2.7, 3) + V("v3b", "piscine-liberte", 30.2, 2.4, 4, 4.65).replace(' data-track-index="4"', ' data-playback-rate="0.75" data-track-index="4"'))
HELPERS = BODY4.split("        // ── fil rouge")[0]
BODY = HELPERS + r"""
        // photo de village en panoramique lent (image 1920 px de haut, on glisse de x0 à x1)
        const pano = (src, x0, x1, t0, t1) => {
          const l = scene(t0, t1, `<img src="assets/img/${src}.jpg" alt="" style="position:absolute;left:0;top:0;height:1920px" />`);
          tl.fromTo(K.$("img", l), { x: -x0, scale: 1.04 }, { x: -x1, scale: 1.0, duration: t1 - t0 + 0.6, ease: "none" }, t0 - 0.3);
          shadeIn(l);
          return l;
        };

        // ── fil rouge : compteur de tâches faites
        const DONE = [0, 3, 7, 12, 16, 21];
        const hud = FX.ab(TOP, { left: "0", right: "0", top: "150px", textAlign: "center", zIndex: 35 },
          `<div style="display:inline-flex;align-items:center;gap:16px;padding:16px 30px;border-radius:999px;background:rgba(255,255,255,.16);border:1.5px solid rgba(255,255,255,.38);backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px);box-shadow:0 14px 40px rgba(0,0,0,.25);font-family:Inter,sans-serif;font-size:38px;color:#fff"><span style="width:46px;height:46px;border-radius:50%;background:#2cc4b5;display:flex;align-items:center;justify-content:center">${K.icon("check")}</span><b class="n" style="font-weight:800;font-size:46px">0</b><span>tâches faites pour toi</span></div>`);
        K.$$("svg.i", hud).forEach((s) => (s.style.cssText = "width:28px;height:28px;color:#fff"));
        tl.set(hud, { opacity: 0 }, 0); tl.to(hud, { opacity: 1, duration: 0.6, ease: EO }, SC[1][0] + 0.2);
        for (let i = 1; i < 6; i++) { K.count(K.$(".n", hud), DONE[i], SC[i][0] + 1.6, 0.8, (v) => String(Math.round(v)), {}); K.sfx(SC[i][0] + 2.3, "success", 0.07); }
        tl.to(hud, { opacity: 0, duration: 0.5, ease: EZ }, SC[6][0] - 0.4);

        // ── avant : au bureau, débordé (désaturé, sans interface)
        const s0 = scene(...SC[0]); drift("v1", ...SC[0]);
        FX.ab(s0, { inset: "0", background: "linear-gradient(180deg, rgba(5,6,15,.55) 0%, rgba(5,6,15,.1) 40%, rgba(5,6,15,.55) 100%)" });
        // ── avec LIMO : le tour du secteur
        const s1 = pano("correze-pont", 1300, 1650, ...SC[1]); C.leak(4.0, 3.0);
        hero(s1, 4.9, "LIMO · TON SECTEUR", "12 mandats suivis", [["users", "38 acquéreurs actifs, chacun avec ses critères"], ["bell", "Aucune relance oubliée"], ["pin", "Tout ton secteur, en un coup d’œil"]]);
        const s2 = pano("correze-ruelle", 1050, 1450, ...SC[2]);
        hero(s2, 9.2, "LIMO · ANNONCE PRÊTE", "Maison de bourg en pierre", [["home", "4 pièces · 110&nbsp;m² · cour intérieure"], ["image", "Photos classées, texte rédigé"], ["check", "Prête à publier"]]);
        const s3 = pano("correze-riviere", 1000, 1350, ...SC[3]);
        hero(s3, 13.7, "LIMO · RELANCES", "Maison au bord de la rivière", [["send", "3 acquéreurs correspondants relancés"], ["clock", "1 visite calée samedi 10:00"], ["msg", "Message personnalisé pour chacun"]]);
        const s4 = pano("correze-halle", 650, 950, ...SC[4]);
        hero(s4, 18.7, "LIMO · ESTIMATION DE 14:00", "Maison de ville, près de la halle", [["calc", "4 ventes comparables du secteur"], ["file", "Rapport prêt à présenter"], ["note", "Tes notes de la 1re visite, résumées"]]);
        const s5 = scene(...SC[5]); shadeIn(s5); drift("v2", ...SC[5]);
        hero(s5, 23.2, "LIMO · COMPROMIS", "Maison contemporaine", [["shield", "Diagnostics : 6 / 6 reçus"], ["scale", "Notaire prévenu"], ["clock", "Signature mardi 15:00"]]);
        // ── le moment fort : plus d'interface, juste la vie
        const s6 = scene(...SC[6]); drift("v3", ...SC[6]); tl.fromTo(document.getElementById("v3b"), { scale: 1.04 }, { scale: 1.0, duration: 2.4, ease: "none" }, 30.2);
        FX.ab(s6, { inset: "0", background: "linear-gradient(180deg, rgba(5,6,15,.4) 0%, rgba(5,6,15,0) 38%, rgba(5,6,15,0) 70%, rgba(5,6,15,.35) 100%)" });
        C.leak(27.9, 3.6);
        FX.rise(s6, "Et toi…", { top: "300px", fontSize: "88px", fontWeight: "700", textShadow: "0 6px 30px rgba(0,0,0,.4)" }, 28.4, { snd: false, st: 0.04 });
        FX.rise(s6, "tu [profites.]", { top: "410px", fontSize: "120px", textShadow: "0 8px 36px rgba(0,0,0,.45)" }, 29.1, { snd: false, st: 0.04, accent: "#ffe2b8" });

        VO.forEach(([, t, d, txt]) => { if (txt) vo(t, d, txt); });

        // ── la mascotte : arrive après le « avant », douce, l'antenne s'allume quand elle parle
        const M = N.mascot({ left: "390px", top: "760px", width: "300px" }, { expr: "happy" });
        TOP.appendChild(M.el); M.el.style.zIndex = "30";
        const ant = K.$(".ant", M.el);
        const speak = (t, d) => { const n = Math.max(1, Math.round(d / 0.36)); tl.fromTo(ant, { opacity: 0.2 }, { opacity: 1, duration: 0.18, ease: "sine.inOut", yoyo: true, repeat: n * 2 - 1, immediateRender: false }, t); tl.set(ant, { opacity: 0 }, t + n * 0.36 + 0.05); };
        VO.forEach(([, t, d], i) => { if (i > 0 && t < T_OUT) speak(t, d); });
        tl.set(M.el, { opacity: 0, x: 340, y: 480, scale: 0.55 }, 0);
        tl.to(M.el, { opacity: 1, duration: 0.7, ease: EO }, SC[1][0]);
        M.float(4.2, 23.0, 8);
        [6.6, 11.6, 16.4, 21.2, 25.8].forEach((t) => M.blink(t));
        M.expr("wink", 12.2, false); M.expr("happy", 13.3, false); M.expr("heart", 26.2, false);
        tl.to(M.el, { opacity: 0, duration: 0.5, ease: EZ }, SC[6][0] - 0.4);
        outro(T_OUT);
""".replace("T_OUT", str(T_OUT))

if __name__ == "__main__":
    body = "        const SC = " + json.dumps(SC) + ";\n        const VO = " + json.dumps([list(v) for v in VO], ensure_ascii=False) + ";\n" + BODY
    html = SHELL.format(title="LIMO veille sur ton secteur", faces=FACES, css=(CSS + EXTRA_CSS).strip("\n"), body=(COMMON + body).strip("\n"), dur=DUR, name=NAME)
    html = html.replace('      <section id="s-main"', PRE + '      <section id="s-main"', 1)
    (HERE.parent / "reels" / f"{NAME}.html").write_text(html, encoding="utf-8")
    vj = HERE / "voix.json"
    data = json.loads(vj.read_text(encoding="utf-8"))
    data[NAME] = [[v[0], v[1]] for v in VO]
    vj.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    print("reels/" + NAME + ".html")
