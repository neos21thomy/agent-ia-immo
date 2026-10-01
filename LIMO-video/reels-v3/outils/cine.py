"""Films « haut budget » de 30 s pour vendre LIMO : traitement cinéma (caméra, grain, fuites de lumière,
iris, bandes cinéma), application recréée en 3D, mascotte. Données fictives, gains = exemples indicatifs.

Usage : python3 outils/cine.py   (réécrit reels/cine-*.html)
"""
import pathlib

from pub30 import COMMON, FACES, SHELL as _SHELL

SHELL = _SHELL.replace('<script src="assets/kit/app.js"></script>', '<script src="assets/kit/app.js"></script>\n    <script src="assets/kit/cine.js"></script>')
SHELL = SHELL.replace("A.init(tl, root);", "A.init(tl, root);\n        C.init(tl, root, D);")

FILMS = {}

# ---------------------------------------------------------------- 1 · le manifeste
FILMS["cine-01-manifeste"] = ("LIMO, le manifeste", 30.0, """
      .doc { width: 300px; height: 380px; border-radius: 18px; background: #fff; box-shadow: 0 20px 50px rgba(0,0,0,.35); padding: 28px; font-family: Inter, sans-serif; color: #1b1f4b; }
      .doc b { display: block; font-size: 26px; margin: 14px 0 18px; }
      .doc i { display: block; height: 12px; border-radius: 6px; background: #dcdce6; margin-bottom: 14px; }
      .pit { width: 260px; height: 230px; padding: 26px; background: #ffe98a; box-shadow: 0 16px 30px rgba(0,0,0,.3); font-family: Caveat, cursive; font-weight: 700; font-size: 44px; line-height: 1.1; color: #4a3d00; }
      .clk { font-family: "Montserrat Hook", Montserrat, sans-serif; font-weight: 800; font-size: 300px; color: transparent; -webkit-text-stroke: 4px rgba(185,166,255,.55); text-align: center; }
      .big3 { font-family: "Montserrat Hook", Montserrat, sans-serif; font-weight: 800; font-size: 104px; text-align: center; color: #1b1f4b; }
      .big3 .v { color: #6b4fe0; }
""", r"""
        const dark = C.bg({ background: "radial-gradient(ellipse at 50% 40%, #23275e 0%, #0d0f2a 70%)" });
        C.cam(0, { scale: 1.07 }, 11.4, "none");
        // ---- acte 1 : ce que le métier n'est pas
        const t1 = C.title("Ton métier,", { top: "700px", fontSize: "104px" }, 0.02, { color: "#ffffff", st: 0.12 });
        const t2 = C.title("c’est [les] [gens.]", { top: "830px", fontSize: "104px" }, 0.8, { color: "#ffffff", accent: "#b9a6ff" });
        C.leak(0.3, 2.6, { max: 0.5 });
        C.out([t1, t2], 2.5);
        const t3 = C.title("Pas les papiers.", { top: "820px", fontSize: "96px" }, 2.9, { color: "#ffffff" });
        ["Compromis.pdf", "Mandat.pdf", "DPE.pdf", "Bon de visite", "Offre d’achat", "Diagnostics", "Avenant.pdf", "Relevé.xls"].forEach((n, i) => {
          const d = C.ab({ left: 390 + ((i * 137) % 300) - 150 + "px", top: 760 + ((i * 89) % 260) - 130 + "px" }, `<div class="doc">${K.icon("file")}<b>${n}</b><i style="width:90%"></i><i style="width:70%"></i><i style="width:84%"></i><i style="width:60%"></i></div>`);
          K.$("svg", d).style.cssText = "width:44px;height:44px;color:#6b4fe0";
          const t = 3.1 + i * 0.28, ang = (i * 47) % 360, dx = Math.cos(ang) * 900, dy = Math.sin(ang) * 1300;
          tl.set(d, { opacity: 0 }, 0);
          tl.fromTo(d, { opacity: 0, scale: 0.15, x: 0, y: 0, rotation: (i % 2 ? -1 : 1) * 10, filter: "blur(6px)" }, { opacity: 1, scale: 0.5, filter: "blur(0px)", duration: 0.3, ease: "power2.out" }, t);
          tl.to(d, { scale: 3.2, x: dx, y: dy, rotation: (i % 2 ? 1 : -1) * 40, opacity: 0, filter: "blur(10px)", duration: 1.1, ease: "power2.in" }, t + 0.3);
          K.sfx(t + 0.3, "swipe", 0.08, (i % 2 ? 0.4 : -0.4));
        });
        C.out(t3, 5.6);
        const t4 = C.title("Pas les relances oubliées.", { top: "780px", fontSize: "92px" }, 5.9, { color: "#ffffff" });
        ["Rappeler M. Vidal !!", "Mme Roy ??", "Famille Martin → mars", "Relancer Albert", "Estimation Brive", "Avis Google"].forEach((n, i) => {
          const p = C.ab({ left: 80 + (i % 3) * 320 + "px", top: (i < 3 ? 380 : 1180) + "px" }, `<div class="pit">${n}</div>`);
          const t = 6.2 + i * 0.15;
          tl.set(p, { opacity: 0 }, 0);
          tl.fromTo(p, { opacity: 0, y: -200, rotation: (i % 2 ? 8 : -8) }, { opacity: 1, y: 0, rotation: (i % 2 ? 4 : -5), duration: 0.45, ease: "bounce.out" }, t);
          tl.to(p, { y: 1400, rotation: (i % 2 ? 40 : -40), duration: 0.9, ease: "power2.in" }, 7.9 + i * 0.08);
          tl.set(p, { opacity: 0 }, 9.0);
          K.sfx(t + 0.15, "drop", 0.12);
        });
        C.out(t4, 8.4);
        const clk = C.ab({ left: "0", right: "0", top: "640px" }, `<div class="clk">22:47</div>`);
        tl.set(clk, { opacity: 0 }, 0);
        tl.fromTo(clk, { opacity: 0, scale: 1.2 }, { opacity: 1, scale: 1, duration: 1.0, ease: "power2.out" }, 8.6);
        const t5 = C.title("Pas les soirées sur les annonces.", { top: "780px", fontSize: "88px" }, 8.8, { color: "#ffffff" });
        [0, 1, 2].forEach((k) => K.sfx(8.9 + k * 0.5, k % 2 ? "tock" : "tick", 0.16));
        C.out([t5, clk], 11.0);
        // ---- révélation
        C.camSet(11.5, { scale: 1 });
        const light = C.bg({ background: "linear-gradient(180deg, #f5f3fe 0%, #ece7fb 100%)" });
        tl.set(light, { clipPath: "circle(0px at 540px 960px)" }, 0);
        C.iris(light, 11.5, 0.9);
        C.bars(11.6, true, 1.0);
        C.leak(11.6, 2.8);
        const t6 = C.title("Alors on a créé", { top: "640px", fontSize: "64px" }, 12.0, { color: "#5d6285" });
        const logo = C.ab({ left: "190px", top: "760px", width: "700px", height: "265px" }, `<img src="assets/img/limo-logo-ad.png" alt="LIMO" style="width:100%;height:100%" />`);
        tl.set(logo, { opacity: 0 }, 0);
        tl.fromTo(logo, { opacity: 0, scale: 1.35, filter: "blur(20px)" }, { opacity: 1, scale: 1, filter: "blur(0px)", duration: 1.0, ease: "power3.out" }, 12.6);
        K.sfx(12.7, "thump", 0.42);
        C.sweep(logo, 13.4, 1.0);
        const t7 = C.title("Le bras droit du conseiller immo.", { top: "1080px", fontSize: "48px" }, 13.6, { color: "#1b1f4b", snd: false });
        C.out([t6, t7], 14.8, 0.4);
        tl.to(logo, { y: -620, scale: 0.5, duration: 0.8, ease: "power3.inOut" }, 14.8);
        // ---- montage produit
        glow(140, 520, 800, 15.0);
        const ph = A.phone({ left: "260px", top: "540px", width: "560px" }, { time: "9:41" });
        const pages = ["home", "relances", "annonce", "detect", "avis"].map((k) => A.page(ph, A.S[k]()));
        A.enter(ph, 15.0, { flatAt: 1.0 });
        C.cam(15.6, { scale: 1.06, rotation: -1 }, 7.0, "sine.inOut");
        const W = [["IL RELANCE<span class='v'>.</span>", "refresh", "v", "32 relances", "prêtes en 1 clic", 30, 760], ["IL RÉDIGE<span class='v'>.</span>", "pen", "t", "2 min", "par annonce", 590, 1420], ["IL DÉTECTE<span class='v'>.</span>", "radar", "v", "3 vendeurs", "probables cette semaine", 30, 760], ["IL RÉPOND<span class='v'>.</span>", "star", "t", "100 %", "d’avis répondus", 590, 1420]];
        W.forEach((w, i) => {
          const t = 16.6 + i * 1.6;
          A.go(ph, pages[i], pages[i + 1], t);
          const big = C.ab({ left: "0", right: "0", top: "330px" }, `<div class="big3">${w[0]}</div>`);
          tl.set(big, { opacity: 0 }, 0);
          tl.fromTo(big, { opacity: 0, y: 40, filter: "blur(12px)" }, { opacity: 1, y: 0, filter: "blur(0px)", duration: 0.4, ease: "power3.out" }, t + 0.05);
          tl.to(big, { opacity: 0, y: -30, duration: 0.25, ease: "power2.in" }, t + 1.35);
          K.sfx(t + 0.05, "slam", 0.16);
          const f = A.float(A.gain(w[1], w[2], w[3], w[4]), { left: w[5] + "px", top: w[6] + "px" }, t + 0.3);
          tl.to(f, { opacity: 0, scale: 0.8, duration: 0.25 }, t + 1.4);
        });
        tl.to(logo, { opacity: 0, duration: 0.3 }, 22.6);
        A.leave(ph, 22.8);
        C.cam(22.8, { scale: 1, rotation: 0 }, 0.6, "power2.inOut");
        // ---- la mascotte
        C.leak(23.0, 2.4);
        const M = N.mascot({ left: "280px", top: "760px", width: "520px" });
        M.enter(23.2);
        M.glow(23.6, 1.2);
        M.wave(23.9);
        const b = N.say("Moi, c’est LIMO.<br><span class='v'>On bosse ensemble ?</span>", { left: "190px", top: "520px", width: "700px" }, 24.0);
        M.expr("wink", 24.8);
        N.out(b, 25.6, { y: -10, d: 0.2 });
        window.__TE = 26.0;
        N.outro(26.0, "contact");
        M.move(25.9, { x: 540 - 540, y: 1370 - (760 + 314), scale: 200 / 520 }, 0.7);
        M.expr("happy", 26.0, false);
        M.wave(27.2);
""")

# ---------------------------------------------------------------- 2 · une journée avec LIMO
FILMS["cine-02-une-journee"] = ("Une journée avec LIMO", 30.0, """
      .hr { font-family: "Montserrat Hook", Montserrat, sans-serif; font-weight: 800; font-size: 120px; text-align: center; color: #1b1f4b; }
      .hr span { position: absolute; left: 0; right: 0; }
      .orb { width: 170px; height: 170px; border-radius: 50%; }
""", r"""
        const sky = [
          C.bg({ background: "linear-gradient(180deg, #ffd9c4 0%, #f2e6ff 60%, #ece7fb 100%)" }),
          C.bg({ background: "linear-gradient(180deg, #cfe6ff 0%, #f1efff 70%)" }),
          C.bg({ background: "linear-gradient(180deg, #ffb28a 0%, #c69bff 55%, #8f6bff 100%)" }),
          C.bg({ background: "linear-gradient(180deg, #0f1230 0%, #23275e 100%)" }),
        ];
        sky.forEach((s, i) => tl.set(s, { opacity: i ? 0 : 1 }, 0));
        tl.to(sky[1], { opacity: 1, duration: 2.0, ease: "sine.inOut" }, 5.0);
        tl.to(sky[2], { opacity: 1, duration: 2.0, ease: "sine.inOut" }, 14.0);
        tl.to(sky[3], { opacity: 1, duration: 1.6, ease: "sine.inOut" }, 19.6);
        tl.to(sky, { opacity: 0, duration: 0.6 }, 25.6);
        const sun = C.ab({ left: "60px", top: "520px" }, `<div class="orb" style="background:radial-gradient(circle,#fff6d8 0%,#ffd27a 55%,rgba(255,210,122,0) 72%)"></div>`);
        tl.fromTo(sun, { x: 0, y: 0 }, { x: 420, y: -330, duration: 9, ease: "sine.out" }, 0);
        tl.to(sun, { x: 860, y: 40, duration: 11, ease: "sine.in" }, 9);
        tl.to(sun, { opacity: 0, duration: 0.8 }, 19.6);
        const moon = C.ab({ left: "760px", top: "230px" }, `<div class="orb" style="width:120px;height:120px;background:radial-gradient(circle at 35% 35%,#ffffff 0%,#dcdcf5 60%,rgba(220,220,245,0) 72%)"></div>`);
        tl.set(moon, { opacity: 0 }, 0);
        tl.to(moon, { opacity: 1, duration: 1.2 }, 20.2);
        tl.to(moon, { opacity: 0, duration: 0.5 }, 25.6);
        C.cam(0, { scale: 1.04 }, 25, "none");
        // ---- ouverture
        const t1 = C.title("Une journée", { top: "640px", fontSize: "110px" }, 0.02, { st: 0.12 });
        const t2 = C.title("d’agent immobilier", { top: "780px", fontSize: "76px" }, 0.5, { color: "#3a3f6b" });
        const t3 = C.title("[avec] [LIMO.]", { top: "890px", fontSize: "110px" }, 1.0);
        C.leak(0.2, 2.6, { max: 0.55 });
        C.out([t1, t2, t3], 2.3);
        C.bars(2.2, true, 1.0);
        // ---- l'horloge et le téléphone
        const HRS = ["7:30", "9:30", "11:00", "14:00", "16:00", "18:00", "19:00"];
        const hr = C.ab({ left: "0", right: "0", top: "190px", height: "140px" }, `<div class="hr">${HRS.map((h) => `<span>${h}</span>`).join("")}</div>`);
        const hs = K.$$(".hr span", hr);
        tl.set(hr, { opacity: 0 }, 0);
        tl.set(hr, { opacity: 1 }, 2.5);
        const ph = A.phone({ left: "260px", top: "560px", width: "560px" }, { time: "7:30" });
        const pages = ["home", "relances", "annonce", "dictee", "detect", "avis"].map((k) => A.page(ph, A.S[k]()));
        A.enter(ph, 2.5, { flatAt: 0.9 });
        const B = [["Ton brief est prêt", "avant ton café."], ["32 relances préparées.", "Tu valides, c’est envoyé."], ["L’annonce de Vignols", "s’écrit toute seule."], ["Tu dictes ta visite.", "La fiche se remplit."], ["3 vendeurs probables", "dans ton secteur."], ["Tes avis Google", "ont tous une réponse."]];
        let prevCap = null;
        hs.forEach((s, i) => {
          const t = 2.5 + i * 3.0;
          tl.set(s, { opacity: 0 }, 0);
          tl.fromTo(s, { opacity: 0, y: 40, filter: "blur(10px)" }, { opacity: 1, y: 0, filter: "blur(0px)", duration: 0.4, ease: "power3.out" }, t);
          if (i < hs.length - 1) tl.to(s, { opacity: 0, y: -40, duration: 0.3, ease: "power2.in" }, t + 2.7);
          K.sfx(t, "tick", 0.2, 0, { f: 1800 });
          if (i < 6) {
            if (i > 0) A.go(ph, pages[i - 1], pages[i], t);
            const cap = C.ab({ left: "60px", right: "60px", top: "360px", textAlign: "center", fontFamily: "Montserrat, sans-serif", fontWeight: "700", fontSize: "44px", lineHeight: "1.2", color: i >= 4 ? "#ffffff" : "#1b1f4b" }, `${B[i][0]}<br><span style="color:${i >= 4 ? "#ffe2b8" : "#6b4fe0"}">${B[i][1]}</span>`);
            tl.set(cap, { opacity: 0 }, 0);
            tl.fromTo(cap, { opacity: 0, y: 20 }, { opacity: 1, y: 0, duration: 0.4, ease: "power3.out" }, t + 0.2);
            tl.to(cap, { opacity: 0, duration: 0.25 }, t + 2.75);
          }
        });
        tl.to(hs[6], { color: "#ffffff", duration: 0.3 }, 20.5);
        A.leave(ph, 20.4);
        // ---- le soir
        const n1 = C.title("Tu rentres.", { top: "640px", fontSize: "110px" }, 21.0, { color: "#ffffff" });
        const n2 = C.title("[Tout] [est] [fait.]", { top: "780px", fontSize: "110px" }, 21.6, { color: "#ffffff", accent: "#b9a6ff" });
        const M = N.mascot({ left: "370px", top: "1000px", width: "340px" }, { expr: "sleep" });
        M.enter(22.0);
        M.expr("wink", 23.4);
        const gc = C.ab({ left: "190px", right: "190px", top: "1460px", padding: "22px 30px", borderRadius: "30px", background: "rgba(255,255,255,.95)", textAlign: "center", fontFamily: "Inter, sans-serif", color: "#1b1f4b" }, `<div style="font-size:24px;font-weight:700;letter-spacing:.06em;color:#5d6285">TEMPS GAGNÉ AUJOURD’HUI</div><div style="font-family:Montserrat,sans-serif;font-weight:800;font-size:64px;color:#6b4fe0"><span>0</span></div><div style="font-size:20px;color:#6e6e80">exemple indicatif</div>`);
        tl.set(gc, { opacity: 0 }, 0);
        K.pop(gc, 23.6, { s: 0.7 });
        K.count(K.$("span", gc), 130, 23.8, 1.0, (v) => { const m = Math.round(v); return Math.floor(m / 60) + " h " + String(m % 60).padStart(2, "0"); }, { ticks: 10 });
        C.out([n1, n2, gc, hr], 25.5, 0.4);
        window.__TE = 26.0;
        N.outro(26.0, "contact");
        M.move(25.9, { x: 0, y: 1370 - (1000 + 205), scale: 200 / 340 }, 0.7);
        M.expr("happy", 26.0, false);
        M.wave(27.2);
""")

# ---------------------------------------------------------------- 3 · le calcul
FILMS["cine-03-le-calcul"] = ("Le calcul", 30.0, """
      .bar { position: absolute; left: 90px; width: 900px; height: 118px; font-family: Inter, sans-serif; }
      .bar .lb { display: flex; justify-content: space-between; font-size: 32px; font-weight: 600; }
      .bar .tr { margin-top: 12px; height: 34px; border-radius: 17px; background: rgba(255,255,255,.1); overflow: hidden; }
      .bar .tr i { display: block; height: 100%; border-radius: 17px; transform-origin: 0 50%; }
      .bar .hv span { position: absolute; right: 0; }
      .tot { font-family: "Montserrat Hook", Montserrat, sans-serif; font-weight: 800; text-align: center; }
""", r"""
        const dark = C.bg({ background: "radial-gradient(ellipse at 50% 35%, #262a66 0%, #0d0f2a 75%)" });
        C.cam(0, { scale: 1.05 }, 15, "none");
        const t1 = C.title("Combien te coûte", { top: "660px", fontSize: "96px" }, 0.02, { color: "#ffffff", st: 0.1 });
        const t2 = C.title("[l’administratif] ?", { top: "790px", fontSize: "96px" }, 0.7, { color: "#ffffff", accent: "#ff8f8f" });
        const t0 = C.title("Agent immobilier,", { top: "560px", fontSize: "50px" }, 0.02, { color: "#b9a6ff", snd: false });
        C.leak(0.3, 2.4, { max: 0.45, c1: "rgba(255,120,120,.6)" });
        C.out([t0, t1, t2], 2.5);
        const head = C.title("Ta semaine type", { top: "250px", fontSize: "66px" }, 2.7, { color: "#ffffff" });
        const T = [["Relances", 150, 25], ["Annonces", 90, 6], ["Comptes rendus", 90, 10], ["Suivi et tri", 120, 20], ["Avis et messages", 30, 5]];
        const fmt = (m) => (m >= 60 ? Math.floor(m / 60) + " h" + (m % 60 ? " " + String(m % 60).padStart(2, "0") : "") : m + " min");
        const bars = T.map((b, i) => {
          const el = C.ab({ left: "90px", top: 440 + i * 160 + "px", width: "900px", height: "118px", fontFamily: "Inter, sans-serif", color: "#ffffff" },
            `<div style="display:flex;justify-content:space-between;font-size:34px;font-weight:600"><span>${b[0]}</span><span style="position:relative;width:200px;text-align:right"><em class="a" style="font-style:normal;position:absolute;right:0">${fmt(b[1])}</em><em class="b" style="font-style:normal;position:absolute;right:0;color:#2cc4b5">${fmt(b[2])}</em></span></div>
<div style="margin-top:14px;height:34px;border-radius:17px;background:rgba(255,255,255,.1);overflow:hidden"><i style="display:block;height:100%;width:100%;border-radius:17px;transform-origin:0 50%;background:linear-gradient(90deg,#ff6b6b,#ff9f6b)"></i></div>`);
          tl.set(el, { opacity: 0 }, 0);
          const t = 3.0 + i * 0.45;
          K.fin(el, t, { y: 20, d: 0.35 });
          tl.set(K.$("em.b", el), { opacity: 0 }, 0);
          tl.fromTo(K.$("i", el), { scaleX: 0 }, { scaleX: b[1] / 150, duration: 0.7, ease: "power3.out" }, t + 0.1);
          K.sfx(t + 0.1, "whoosh", 0.08, 0, { d: 0.4, f0: 400, f1: 2000, pk: 0.6 });
          return el;
        });
        const tot = C.ab({ left: "0", right: "0", top: "1290px" }, `<div class="tot" style="font-size:150px;color:#ff8f8f"><span>0 h</span></div><div style="text-align:center;font-family:Inter,sans-serif;font-size:36px;color:#c9c9e8">par semaine (exemple)</div>`);
        tl.set(tot, { opacity: 0 }, 0);
        tl.set(tot, { opacity: 1 }, 5.6);
        K.count(K.$("span", tot), 8, 5.6, 0.9, (v) => Math.round(v) + " h", { ticks: 8 });
        K.sfx(6.6, "thump", 0.36);
        C.out([head, ...bars, tot], 8.0);
        // ---- à l'année
        const y1 = C.title("× 46 semaines", { top: "560px", fontSize: "86px" }, 8.4, { color: "#c9c9e8" });
        const y2 = C.ab({ left: "0", right: "0", top: "720px" }, `<div class="tot" style="font-size:230px;color:#ffffff"><span>0 h</span></div>`);
        tl.set(y2, { opacity: 0 }, 0);
        tl.set(y2, { opacity: 1 }, 9.0);
        K.count(K.$("span", y2), 368, 9.0, 1.2, (v) => Math.round(v) + " h", { ticks: 12 });
        const y3 = C.title("= [46] [jours] de travail par an.", { top: "1040px", fontSize: "62px" }, 10.6, { color: "#ffffff", accent: "#ff8f8f" });
        K.sfx(10.6, "thump", 0.32);
        C.out([y1, y2, y3], 12.6);
        // ---- avec LIMO
        C.camSet(13.0, { scale: 1 });
        const light = C.bg({ background: "linear-gradient(180deg, #f5f3fe 0%, #ece7fb 100%)" });
        tl.set(light, { clipPath: "circle(0px at 540px 960px)" }, 0);
        C.iris(light, 13.0, 0.9);
        C.bars(13.1, true, 1.0);
        C.leak(13.1, 2.6);
        const logo = C.ab({ left: "340px", top: "220px", width: "400px", height: "151px" }, `<img src="assets/img/limo-logo-ad.png" alt="LIMO" style="width:100%;height:100%" />`);
        tl.set(logo, { opacity: 0 }, 0);
        tl.fromTo(logo, { opacity: 0, scale: 1.3, filter: "blur(16px)" }, { opacity: 1, scale: 1, filter: "blur(0px)", duration: 0.8, ease: "power3.out" }, 13.5);
        K.sfx(13.6, "thump", 0.36);
        C.sweep(logo, 14.1, 0.9);
        const bars2 = T.map((b, i) => {
          const el = C.ab({ left: "90px", top: 470 + i * 150 + "px", width: "900px", height: "118px", fontFamily: "Inter, sans-serif", color: "#1b1f4b" },
            `<div style="display:flex;justify-content:space-between;font-size:34px;font-weight:600"><span>${b[0]}</span><span style="position:relative;width:200px;text-align:right"><em class="a" style="font-style:normal;position:absolute;right:0;color:#c0282d;text-decoration:line-through">${fmt(b[1])}</em><em class="b" style="font-style:normal;position:absolute;right:0;color:#0d6b62">${fmt(b[2])}</em></span></div>
<div style="margin-top:14px;height:34px;border-radius:17px;background:#e7e1fa;overflow:hidden"><i style="display:block;height:100%;width:100%;border-radius:17px;transform-origin:0 50%;background:linear-gradient(90deg,#ff6b6b,#ff9f6b)"></i><u style="position:absolute"></u></div>`);
          tl.set(el, { opacity: 0 }, 0);
          const t = 14.4 + i * 0.12;
          K.fin(el, t, { y: 20, d: 0.3 });
          const bar = K.$("i", el);
          tl.set(bar, { scaleX: b[1] / 150 }, 0);
          tl.set(K.$("em.b", el), { opacity: 0 }, 0);
          const tt = 15.4 + i * 0.35;
          tl.to(bar, { scaleX: Math.max(0.04, b[2] / 150), background: "linear-gradient(90deg,#6b4fe0,#2cc4b5)", duration: 0.6, ease: "power3.inOut" }, tt);
          tl.to(K.$("em.a", el), { opacity: 0, duration: 0.2 }, tt + 0.25);
          tl.to(K.$("em.b", el), { opacity: 1, duration: 0.2 }, tt + 0.3);
          K.sfx(tt, "success", 0.12);
          return el;
        });
        const tot2 = C.ab({ left: "0", right: "0", top: "1250px" }, `<div class="tot" style="font-size:120px;color:#6b4fe0">1 h 06</div><div style="text-align:center;font-family:Inter,sans-serif;font-size:34px;color:#3a3f6b">par semaine avec LIMO (exemple)</div>`);
        tl.set(tot2, { opacity: 0 }, 0);
        K.pop(tot2, 17.6, { s: 0.6 });
        K.sfx(17.6, "fanfare", 0.2);
        C.out([logo, ...bars2, tot2], 19.6, 0.4);
        const g = gains(20.0, [
          { k: "TEMPS RÉCUPÉRÉ", n: 317, f: (v) => Math.round(v) + " h / an", d: "(8 h − 1 h 06) × 46 semaines : <b>40 jours rendus</b>." },
          { k: "ARGENT", c: "t", n: 15000, f: (v) => "+ " + K.eur(v), d: "si ce temps te fait signer <b>2 mandats de plus par an</b>." },
          { k: "COÛT DE LIMO", v: "588 €<small style='font-size:.4em'>/an</small>", d: "soit <b>49 € par mois</b>, sans engagement." },
        ]);
        N.out(g, 25.6, { y: -30 });
        window.__TE = 26.0;
        fin(26.0);
""")

# ---------------------------------------------------------------- 4 · prestige (plans Higgsfield de la villa)
PRE = {}
PRE["cine-04-prestige"] = """      <video id="v1" class="clip" src="assets/video/villa-A.mp4" data-start="0" data-duration="5" data-track-index="1" muted playsinline style="position:absolute;left:0;top:0;width:1080px;height:1920px;object-fit:cover"></video>
      <video id="v2" class="clip" src="assets/video/villa-recul-lent.mp4" data-start="5" data-duration="9.9" data-track-index="2" muted playsinline style="position:absolute;left:0;top:0;width:1080px;height:1920px;object-fit:cover"></video>
"""
FILMS["cine-04-prestige"] = ("LIMO, prestige", 30.0, """
      #s-main { background: transparent; }
      .glass { border-radius: 40px; background: rgba(14, 16, 40, 0.42); backdrop-filter: blur(22px) saturate(1.3); -webkit-backdrop-filter: blur(22px) saturate(1.3);
        border: 1.5px solid rgba(255,255,255,.28); box-shadow: 0 30px 80px rgba(0,0,0,.35); color: #fff; font-family: Inter, sans-serif; }
      .gchip { display: inline-flex; align-items: center; gap: 10px; height: 52px; padding: 0 22px; border-radius: 26px; background: rgba(255,255,255,.16); border: 1px solid rgba(255,255,255,.3); color: #fff; font-family: Montserrat, sans-serif; font-weight: 700; font-size: 24px; white-space: nowrap; }
      .gchip svg.i { width: 26px; height: 26px; stroke-width: 2.6; }
      .shade { text-shadow: 0 4px 30px rgba(0,0,0,.55); }
""", r"""
        // le fond lavande du kit reste caché pendant les plans réels
        tl.set([K.$(".n-bg", root), ...K.$$(".n-arc", root)], { opacity: 0 }, 0);
        const sh = C.ab({ left: "0", top: "0", width: "1080px", height: "1920px", background: "linear-gradient(180deg, rgba(5,6,15,.55) 0%, rgba(5,6,15,0) 30%, rgba(5,6,15,0) 52%, rgba(5,6,15,.7) 100%)" });
        C.bars(4.6, true, 1.2);
        const t0 = C.title("Agent immobilier,", { top: "330px", fontSize: "54px" }, 0.02, { color: "#d9ceff", snd: false });
        const t1 = C.title("tu vends des [biens] [d’exception].", { top: "410px", fontSize: "84px" }, 0.25, { color: "#ffffff", accent: "#d9ceff" });
        [t0, t1].forEach((e) => e.classList.add("shade"));
        C.out([t0, t1], 2.6);
        const t2 = C.title("Tes [annonces] doivent l’être [aussi].", { top: "1380px", fontSize: "80px" }, 2.9, { color: "#ffffff", accent: "#d9ceff" });
        t2.classList.add("shade");
        C.out(t2, 4.8);
        // ---- LIMO rédige l'annonce de cette villa, par-dessus le plan
        const chip = C.ab({ left: "0", right: "0", top: "280px", textAlign: "center" }, `<span class="gchip">${K.icon("sparkles")}LIMO rédige l’annonce</span>`);
        tl.set(chip, { opacity: 0 }, 0);
        K.pop(chip, 5.2, { s: 0.7 });
        K.sfx(5.2, "chirp", 0.12);
        const card = C.ab({ left: "70px", top: "1000px", width: "940px", padding: "40px 44px" }, `<div class="ti" style="font-family:'Source Serif 4',serif;font-weight:600;font-size:52px;line-height:1.15;min-height:120px"></div>
<div class="bo" style="margin-top:16px;font-size:31px;line-height:1.45;color:rgba(255,255,255,.88);min-height:180px"></div>
<div class="lg" style="margin-top:18px;padding-top:16px;border-top:1px solid rgba(255,255,255,.25);font-size:22px;line-height:1.4;color:rgba(255,255,255,.72)">Prix honoraires inclus · part des honoraires à la charge de l’acquéreur indiquée · DPE et GES affichés</div>
<div class="cs" style="display:flex;gap:12px;margin-top:20px;flex-wrap:wrap"><span class="gchip">${K.icon("check")}Mentions légales</span><span class="gchip">${K.icon("check")}Prête à publier</span></div>`);
        card.classList.add("glass");
        tl.set(card, { opacity: 0 }, 0);
        tl.fromTo(card, { opacity: 0, y: 80 }, { opacity: 1, y: 0, duration: 0.7, ease: "power3.out" }, 5.5);
        K.sfx(5.5, "whoosh", 0.16, 0, { d: 0.5, f0: 300, f1: 2000, pk: 0.6 });
        K.type(K.$(".ti", card), "Villa d’architecte entre béton et forêt", 6.2, 1.1, 0.05);
        K.type(K.$(".bo", card), "Volumes généreux, baies vitrées toute hauteur et cheminée suspendue face à la canopée. Une adresse rare, au calme absolu.", 7.4, 2.6, 0.04);
        tl.set(K.$(".lg", card), { opacity: 0 }, 0);
        K.fin(K.$(".lg", card), 10.2, { y: 8 });
        tl.set(K.$(".cs", card), { opacity: 0 }, 0);
        tl.set(K.$(".cs", card), { opacity: 1 }, 10.7);
        K.pop(K.$$(".cs .gchip", card), 10.7, { st: 0.12 });
        K.sfx(10.7, "success", 0.24);
        const tm = C.ab({ left: "0", right: "0", top: "370px", textAlign: "center" }, `<span class="gchip" style="background:rgba(44,196,181,.35);border-color:rgba(44,196,181,.7)">${K.icon("timer")}Rédigée en 2 minutes</span>`);
        tl.set(tm, { opacity: 0 }, 0);
        K.pop(tm, 11.2, { s: 0.7 });
        C.out([chip, tm, card], 12.6, 0.5);
        const t3 = C.title("Toi, tu fais [visiter].", { top: "1460px", fontSize: "84px" }, 12.9, { color: "#ffffff", accent: "#d9ceff" });
        t3.classList.add("shade");
        C.out([t3, sh], 14.4, 0.4);
        // ---- l'application
        C.flash(14.7, "#ffffff", 0.95);
        const light = C.bg({ background: "linear-gradient(180deg, #f5f3fe 0%, #ece7fb 100%)" });
        tl.set(light, { clipPath: "circle(0px at 540px 960px)" }, 0);
        C.iris(light, 14.7, 0.8);
        C.leak(14.8, 2.6);
        const h = N.head(["TON BRAS DROIT", "S’OCCUPE DU RESTE<span class='v'>.</span>"], { top: "150px", fontSize: "70px" }, 15.3, { bar: false });
        glow(140, 520, 800, 15.3);
        const ph = A.phone({ left: "260px", top: "470px", width: "560px" }, { time: "10:05", tab: 3 });
        const p1 = A.page(ph, `<div class="a-back">${K.icon("chev")}Annonce</div><div class="a-ph" style="height:230px;margin-bottom:14px"><img src="assets/img/villa-photo.jpg" alt="Villa" style="width:100%;height:100%;object-fit:cover" /></div>
<div class="a-card" style="padding:20px 22px"><div style="font-family:'Source Serif 4',serif;font-size:30px;font-weight:600;line-height:1.2">Villa d’architecte entre béton et forêt</div><div style="margin-top:10px;font-size:20px;line-height:1.45;color:#3a3a3c">Volumes généreux, baies vitrées toute hauteur et cheminée suspendue face à la canopée.</div></div>
<div style="display:flex;gap:10px;margin-top:14px"><span class="a-tag t">${K.icon("check")}Mentions légales</span><span class="a-tag">${K.icon("check")}Prête à publier</span></div>
<div class="a-btn" style="margin-top:16px"><span class="bt">${K.icon("send")}Publier partout</span></div>`);
        const p2 = A.page(ph, A.S.relances());
        A.enter(ph, 15.4, { flatAt: 0.9 });
        A.tap(ph, 264, 900, 17.4);
        const btn = K.$(".a-btn", p1);
        tl.to(btn, { backgroundColor: "#2cc4b5", duration: 0.25 }, 17.5);
        tl.set(K.$(".bt", btn), { innerHTML: `${K.icon("check")}Publiée` }, 17.5);
        K.sfx(17.5, "success", 0.24);
        const n1 = A.over(N.notif({ title: "LINKEDIN", time: "10:07", text: "Post « Villa d’architecte » publié." }, { left: "90px", top: "600px" }, 18.0));
        tl.to(n1, { opacity: 0, y: -40, duration: 0.25 }, 19.3);
        A.go(ph, p1, p2, 19.4);
        const f1 = A.float(A.gain("users", "v", "12 acquéreurs", "relancés pour cette villa"), { left: "30px", top: "760px" }, 19.9);
        N.out([h, f1], 21.4, { y: -30 });
        A.leave(ph, 21.4);
        // ---- la mascotte
        const M = N.mascot({ left: "280px", top: "760px", width: "520px" });
        M.enter(21.9);
        M.glow(22.3, 1.2);
        M.wave(22.6);
        const b = N.say("Moi, c’est LIMO.<br><span class='v'>Ton bras droit.</span>", { left: "190px", top: "520px", width: "700px" }, 22.8);
        M.expr("wink", 24.0);
        N.out(b, 25.6, { y: -10, d: 0.2 });
        window.__TE = 26.0;
        N.outro(26.0, "contact");
        M.move(25.9, { x: 0, y: 1370 - (760 + 314), scale: 200 / 520 }, 0.7);
        M.expr("happy", 26.0, false);
        M.wave(27.2);
""")

if __name__ == "__main__":
    for name, (title, dur, css, body) in FILMS.items():
        html = SHELL.format(title=title, faces=FACES, css=css.strip("\n"), body=(COMMON + body).strip("\n"), dur=dur, name=name)
        if name in PRE:
            html = html.replace('      <section id="s-main"', PRE[name] + '      <section id="s-main"', 1)
        pathlib.Path(f"reels/{name}.html").write_text(html, encoding="utf-8")
        print("reels/" + name + ".html")
