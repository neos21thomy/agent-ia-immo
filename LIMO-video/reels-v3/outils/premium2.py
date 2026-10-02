"""Pack premium (kit assets/kit/fx.js) : P1 « Regarde ça » refait avec sous-titres karaoké mot à mot,
titres lettre par lettre, transitions whip pan, plongée dans l'écran, cartes en verre, fond aurore et
plans étalonnés cinéma (assets/video/*-grade.mp4). Même voix que voix-02 (Lucie), mêmes décalages.

Usage : python3 outils/premium2.py   (réécrit reels/prem-*.html et complète outils/voix.json)
"""
import json
import pathlib

from cine import COMMON, FACES, GLASS, SHELL as _SHELL
from lifestyle import V

SHELL = _SHELL.replace('<script src="assets/kit/cine.js"></script>', '<script src="assets/kit/cine.js"></script>\n    <script src="assets/kit/fx.js"></script>')
SHELL = SHELL.replace("C.init(tl, root, D);", "C.init(tl, root, D);\n        FX.init(tl);")

VOICE = {"prem-01-regarde-ca": [["Lucie-15_52_09.mp3", 0.2], ["Lucie-16_18_01.mp3", 15.9]]}
PRE, FILMS = {}, {}

PRE["prem-01-regarde-ca"] = V("v1", "agent-voiture-grade", 0, 3.3, 1) + V("v2", "villa-recul-lent-grade", 23.0, 3.2, 2, 1.0)
FILMS["prem-01-regarde-ca"] = ("LIMO, regarde ça (premium)", 29.8, GLASS, r"""
        tl.set([K.$(".n-bg", root), ...K.$$(".n-arc", root)], { opacity: 0 }, 0);
        const LIGHT = "linear-gradient(180deg, #f5f3fe 0%, #ece7fb 100%)";
        const v1 = document.getElementById("v1");
        // ── S1 · plan étalonné + accroche lettre par lettre
        const s1 = FX.layer(0, 3.2, { background: "linear-gradient(180deg, rgba(5,6,15,.55) 0%, rgba(5,6,15,0) 34%, rgba(5,6,15,0) 62%, rgba(5,6,15,.5) 100%)" });
        tl.fromTo(v1, { scale: 1.0 }, { scale: 1.08, duration: 3.2, ease: "none" }, 0);
        const h1 = FX.rise(s1, "CONSEILLER IMMO,", { top: "300px", fontSize: "70px", textShadow: "0 6px 30px rgba(0,0,0,.45)" }, 0.15, { color: "#d9ceff" });
        const h2 = FX.rise(s1, "[REGARDE] [ÇA.]", { top: "385px", fontSize: "132px", textShadow: "0 8px 40px rgba(0,0,0,.5)" }, 0.45, { accent: "#ffffff", snd: false });
        C.leak(0.2, 2.4);
        // ── S2 · aurore + téléphone : la question
        const s2 = FX.layer(2.7, 9.75);
        FX.aurora(s2, 2.7, 9.8);
        FX.whip([v1, s1], s2, 2.6);
        C.bars(2.6, true, 0.6);
        const q1 = FX.rise(s2, "Tu lui [demandes]…", { top: "200px", fontSize: "76px" }, 3.2, { snd: false });
        FX.fall(q1, 6.9);
        const q2 = FX.rise(s2, "…il te [répond].", { top: "200px", fontSize: "76px" }, 7.2, { snd: false });
        const ph = A.phone({ left: "280px", top: "320px", width: "520px" }, { time: "18:12" });
        s2.appendChild(ph.wrap);
        const chat = A.page(ph, `<div class="a-back">${K.icon("chev")}Demander à LIMO</div><div style="display:flex;flex-direction:column;gap:14px;margin-top:10px">
<div class="q" style="align-self:flex-end;max-width:86%;padding:16px 20px;border-radius:24px 24px 6px 24px;background:#6b4fe0;color:#fff;font-size:23px;line-height:1.35"><span class="ty"></span></div>
<div class="r a-card" style="padding:16px;border-radius:24px 24px 24px 6px">
<div class="a-ph" style="height:170px;margin-bottom:12px"><img src="assets/img/bien-mas-lavande.jpg" alt="" style="width:100%;height:100%;object-fit:cover;object-position:50% 40%" /></div>
<b style="font-size:24px">Mas en pierre · 165 m²</b><div style="margin-top:6px;font-size:19px;color:#55586c;line-height:1.45">Terrain 2 400 m² · 5 chambres · DPE C<br>Propriétaires : M. et Mme T. · mandat exclusif<br>Diagnostics : 4 / 6 reçus · notaire : Me Faure</div></div></div>`);
        A.enter(ph, 3.0, { flatAt: 0.7 });
        K.type(K.$(".ty", chat), "Peux-tu me rappeler les infos du bien de M. et Mme T. ?", 3.4, 3.2, 0.04);
        const r = K.$(".r", chat);
        tl.set(r, { opacity: 0 }, 0);
        tl.fromTo(r, { opacity: 0, y: 30, scale: 0.95 }, { opacity: 1, y: 0, scale: 1, duration: 0.45, ease: "back.out(1.6)" }, 7.15);
        K.sfx(7.15, "success", 0.26);
        tl.to(ph.wrap, { y: -30, duration: 2.2, ease: "sine.inOut" }, 7.0);
        // ── plongée dans la fiche du bien → S3
        FX.dive(ph.wrap, 260, 450, 9.0, 0.75, 5);
        tl.to(q2, { opacity: 0, duration: 0.3 }, 9.0);
        const s3 = FX.layer(9.75, 15.95);
        const photo = FX.ab(s3, { left: "-60px", top: "-80px", width: "1200px", height: "2080px" }, `<img src="assets/img/bien-mas-lavande.jpg" alt="" style="width:100%;height:100%;object-fit:cover" />`);
        tl.fromTo(photo, { scale: 1.18 }, { scale: 1.02, duration: 6.4, ease: "power1.out" }, 9.75);
        FX.ab(s3, { inset: "0", background: "linear-gradient(180deg, rgba(8,8,26,.6) 0%, rgba(8,8,26,.15) 30%, rgba(8,8,26,.25) 60%, rgba(8,8,26,.75) 100%)" });
        const t3 = FX.rise(s3, "Ton bien. [Tout] [est] [là].", { top: "190px", fontSize: "80px", textShadow: "0 6px 30px rgba(0,0,0,.4)" }, 10.0, { snd: false });
        const CARDS = [
          ["file", "12 documents", "classés sur ce bien", 70, 470, 10.3, -60],
          ["users", "Propriétaires", "M. et Mme T. · tout l’historique", 380, 700, 11.0, -110],
          ["calc", "Estimation", "485 000 – 510 000 € · ventes du secteur", 70, 930, 11.7, -80],
          ["shield", "Diagnostics", "4 sur 6 reçus · 2 relancés", 380, 1160, 12.4, -140],
        ];
        CARDS.forEach((c) => {
          const g = FX.glass(s3, { left: c[3] + "px", top: c[4] + "px", width: "630px", display: "flex", alignItems: "center", gap: "22px" },
            `<span style="flex:none;width:78px;height:78px;border-radius:22px;background:rgba(44,196,181,.35);display:flex;align-items:center;justify-content:center">${K.icon(c[0])}</span><span><b style="display:block;font-family:Montserrat,sans-serif;font-weight:800;font-size:38px;line-height:1.1">${c[1]}</b><span style="font-size:25px;color:rgba(255,255,255,.88)">${c[2]}</span></span>`);
          K.$$("svg.i", g).forEach((s) => (s.style.cssText = "width:40px;height:40px;color:#fff"));
          tl.set(g, { opacity: 0 }, 0);
          tl.fromTo(g, { opacity: 0, y: 80, scale: 0.92, filter: "blur(8px)" }, { opacity: 1, y: 0, scale: 1, filter: "blur(0px)", duration: 0.6, ease: "expo.out" }, c[5]);
          tl.to(g, { y: c[6], duration: 15.6 - c[5], ease: "none" }, c[5] + 0.6);
          FX.sheen(g, c[5] + 0.35);
          K.sfx(c[5], "pop", 0.16, 0, { f: 900 });
        });
        // ── S4 · pendant ce temps (aurore turquoise + notifications verre)
        const s4 = FX.layer(15.95, 26.2);
        const au = FX.aurora(s4, 15.9, 26.2, { colors: ["#2cc4b5", "#6b4fe0", "#1d6f8a"] });
        FX.whip(s3, s4, 15.6);
        const t4 = FX.rise(s4, "Et pendant ce [temps]…", { top: "220px", fontSize: "80px" }, 16.0, { snd: false });
        const NT = [
          ["refresh", "RELANCE ACQUÉREURS", "8 acquéreurs relancés pour le mas en pierre.", 16.95, 460],
          ["shield", "DIAGNOSTIQUEUR", "DPE et amiante manquants : demande envoyée.", 19.95, 690],
          ["file", "DOSSIER NOTAIRE", "Dossier complété : 2 pièces ajoutées.", 22.85, 920],
        ];
        const ns = NT.map((n) => {
          const g = FX.glass(s4, { left: "70px", top: n[4] + "px", width: "880px", display: "flex", alignItems: "center", gap: "22px", padding: "24px 28px" },
            `<img src="assets/img/limo-house-ad.png" alt="" style="flex:none;width:72px;height:72px;border-radius:18px;background:#fff;padding:8px" /><span><span style="display:block;font-size:22px;letter-spacing:.06em;color:rgba(255,255,255,.75)">LIMO · ${n[1]}</span><b style="display:block;font-size:32px;line-height:1.25;margin-top:4px">${n[2]}</b></span>`);
          tl.set(g, { opacity: 0 }, 0);
          tl.fromTo(g, { opacity: 0, y: -90, scale: 0.94 }, { opacity: 1, y: 0, scale: 1, duration: 0.55, ease: "back.out(1.5)" }, n[3]);
          FX.sheen(g, n[3] + 0.3);
          K.sfx(n[3], "notif", 0.24);
          return g;
        });
        // fin de S4 : le plan de la villa apparaît derrière, « toi, tu vends »
        FX.fall(t4, 22.6);
        tl.to(au, { opacity: 0, duration: 0.6 }, 23.1);
        tl.to(ns, { opacity: 0, y: -40, filter: "blur(10px)", duration: 0.45, stagger: 0.08, ease: "power2.in" }, 23.6);
        FX.ab(s4, { inset: "0", background: "linear-gradient(180deg, rgba(5,6,15,.35) 0%, rgba(5,6,15,0) 40%, rgba(5,6,15,.55) 100%)" });
        const t5 = FX.rise(s4, "Toi, tu [vends].", { top: "640px", fontSize: "130px", textShadow: "0 8px 40px rgba(0,0,0,.45)" }, 24.75, { accent: "#2cc4b5" });
        FX.fall(t5, 25.6);
        // ── S5 · signature LIMO
        FX.layer(25.95, null, { background: LIGHT }, "", true);
        C.flash(25.95, "#ffffff", 0.95);
        C.leak(26.0, 2.4);
        window.__TE = 26.2;
        N.outro(26.2, "pub");
        const m = N.mascot({ left: "440px", top: "1240px", width: "200px" });
        m.enter(27.6);
        m.wave(28.3);
        // ── sous-titres karaoké (temps des phrases issus de la transcription de la voix)
        const a = 0.2, b = 15.9;
        const KEYS = ["limo", "regarde", "relancer", "paperasse", "vends", "cœur", "partout"];
        FX.karaoke([
          [a + 0.0, a + 2.34, "Si t’es conseiller immobilier, regarde ça."],
          [a + 2.86, a + 6.79, "Peux-tu me rappeler les infos du bien de Madame et Monsieur T. ?"],
          [a + 6.88, a + 8.82, "Et hop, tout ressort."],
          [a + 9.27, a + 12.6, "Plus besoin d’aller chercher les informations partout."],
          [a + 12.78, a + 15.39, "LIMO connaît tes biens et tes clients par cœur."],
        ], { keys: KEYS });
        FX.karaoke([
          [b + 0.1, b + 0.95, "Et en plus,"],
          [b + 1.04, b + 3.77, "LIMO s’occupe de relancer tes futurs acquéreurs…"],
          [b + 4.08, b + 5.13, "…le diagnostiqueur…"],
          [b + 5.41, b + 6.72, "…s’il te manque des diags."],
          [b + 6.94, b + 9.8, "Il s’occupe de la paperasse pendant que toi, tu vends."],
        ], { keys: KEYS });
""")

if __name__ == "__main__":
    for name, (title, dur, css, body) in FILMS.items():
        html = SHELL.format(title=title, faces=FACES, css=css.strip("\n"), body=(COMMON + body).strip("\n"), dur=dur, name=name)
        html = html.replace('      <section id="s-main"', PRE[name] + '      <section id="s-main"', 1)
        pathlib.Path(f"reels/{name}.html").write_text(html, encoding="utf-8")
        print("reels/" + name + ".html")
    vj = pathlib.Path("outils/voix.json")
    data = json.loads(vj.read_text()) if vj.exists() else {}
    data.update(VOICE)
    vj.write_text(json.dumps(data, indent=1), encoding="utf-8")
