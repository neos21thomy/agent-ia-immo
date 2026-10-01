"""Génère les 10 films de conversion (reels/film-XX-*.html) à partir d'un gabarit commun.

Chaque film = un bloc CSS propre + un script qui utilise K (kit.js) et P (premium.js).
Usage : python3 outils/films.py   (réécrit les 10 fichiers ; durées dans DUR)
"""
import pathlib

SHELL = """<!doctype html>
<html lang="fr">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1080, height=1920" />
    <title>LIMO — {title}</title>
    <script src="assets/lib/gsap.min.js"></script>
    <link rel="stylesheet" href="assets/kit/kit.css" />
    <link rel="stylesheet" href="assets/kit/premium.css" />
    <style>
      @font-face {{
        font-family: "Anton";
        src: url("assets/fonts/anton-latin-400-normal.woff2") format("woff2");
        font-weight: 400;
        font-style: normal;
      }}
      @font-face {{
        font-family: "Source Serif 4";
        src: url("assets/fonts/source-serif-4-latin-400-normal.woff2") format("woff2");
        font-weight: 400;
        font-style: normal;
      }}
      @font-face {{
        font-family: "Source Serif 4";
        src: url("assets/fonts/source-serif-4-latin-600-normal.woff2") format("woff2");
        font-weight: 600;
        font-style: normal;
      }}
      @font-face {{
        font-family: "Caveat";
        src: url("assets/fonts/caveat-latin-700-normal.woff2") format("woff2");
        font-weight: 700;
        font-style: normal;
      }}
{css}
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="{dur}" data-width="1080" data-height="1920">
      <section id="s-main" class="clip" data-start="0" data-duration="{dur}" data-track-index="0"></section>
      <audio id="sfx" src="assets/audio/{name}.wav" data-start="0" data-duration="{dur}" data-track-index="10" data-volume="1"></audio>
    </div>
    <script src="assets/kit/kit.js"></script>
    <script src="assets/kit/premium.js"></script>
    <script>
      (function () {{
        const tl = gsap.timeline({{ paused: true }});
        K.init(tl);
        const root = document.getElementById("s-main");
        const D = {dur};
        P.init(tl, root, D);
{body}
        window.__timelines["main"] = tl;
      }})();
    </script>
  </body>
</html>
"""

FILMS = {}

# ---------------------------------------------------------------- 1 · le mandat perdu
FILMS["film-01-mandat-perdu"] = ("Film 1 · Le mandat perdu", """
      #rw { top: 760px; font-family: "JetBrains Mono", monospace; font-weight: 700; font-size: 150px; color: #fff; }
      #rwi { left: 390px; top: 560px; width: 300px; height: 150px; }
      #rwi svg { width: 300px; height: 150px; }
""", """
        const k1 = P.text("ctr p-kick", "MARDI · 9 H 12", { top: "330px" }, 0.1);
        const n1 = P.notif({ title: "SMS · M. ALBERT", time: "9:12", icon: "msg", c: "red", text: "Finalement, on a signé avec une autre agence. Vous ne nous avez jamais rappelés…" }, { left: "90px", top: "470px" }, 0.45);
        tl.fromTo(n1, { x: 0 }, { x: 10, duration: 0.05, ease: "none", yoyo: true, repeat: 7, immediateRender: false }, 1.0);
        P.flash(1.7);
        K.sfx(1.7, "buzz", 0.22);
        const t1 = P.title(["LE MANDAT", "<span class='red'>QUE T’AS OUBLIÉ</span>", "DE RAPPELER."], { top: "860px", fontSize: "94px" }, 1.9, { slam: 0.4 });
        P.out([k1, n1, t1], 4.3);
        // on rembobine
        const rwi = P.ab("", `<svg viewBox="0 0 200 100"><path d="M100 10 L30 50 L100 90Z M180 10 L110 50 L180 90Z" fill="#00C6FC"/></svg>`, {});
        rwi.id = "rwi";
        const rt = P.title(["ON REMBOBINE."], { top: "380px", fontSize: "100px" }, 4.6, { slam: 0.3 });
        const rw = P.ab("ctr", "MAR 09:12", {});
        rw.id = "rw";
        tl.set([rwi, rw], { opacity: 0 }, 0);
        tl.fromTo([rwi, rw], { opacity: 0 }, { opacity: 1, duration: 0.2 }, 4.6);
        tl.fromTo(rwi, { x: 0 }, { x: -24, duration: 0.12, ease: "sine.inOut", yoyo: true, repeat: 11 }, 4.7);
        const P0 = { m: 24 * 60 + 9 * 60 + 12 };
        tl.to(P0, { m: 8 * 60, duration: 1.4, ease: "power2.inOut", onUpdate: () => {
          const m = Math.round(P0.m); const d = m >= 24 * 60 ? "MAR" : "LUN"; const r = m % (24 * 60);
          rw.textContent = `${d} ${String(Math.floor(r / 60)).padStart(2, "0")}:${String(r % 60).padStart(2, "0")}`;
        } }, 4.8);
        for (let i = 0; i < 12; i++) K.sfx(4.8 + i * 0.11, "tick", 0.12, 0, { f: 3200 - i * 120 });
        K.sfx(4.7, "whoosh", 0.24, 0, { d: 1.4, f0: 6000, f1: 300, pk: 0.8 });
        P.out([rt, rwi, rw], 6.5);
        // avec LIMO
        const k2 = P.text("ctr p-kick", "LUNDI · 8 H 00 · AVEC LIMO", { top: "250px" }, 6.7);
        const { ph, halo } = P.phone({ left: "213px", top: "520px" }, 6.8);
        const n2 = P.notif({ title: "RAPPEL", text: "M. Albert attend ton rappel aujourd’hui." }, { left: "90px", top: "640px" }, 7.7);
        K.tapAt(n2, 800, 80, 8.8);
        const n3 = P.notif({ title: "APPEL PASSÉ", icon: "phone", c: "cy", time: "8:05", text: "RDV d’estimation calé : jeudi, 10 h." }, { left: "90px", top: "830px" }, 9.2);
        const n4 = P.notif({ title: "MANDAT", icon: "file", c: "ok", time: "Jeudi", text: "Mandat exclusif signé : famille Albert.", snd: "success", g: 0.3 }, { left: "90px", top: "1020px" }, 10.4);
        K.sfx(10.6, "fanfare", 0.22);
        K.burst(K.sparkles(root, 540, 1100, 18, 480, 160, 3), 10.55);
        P.out([k2, ph, halo, n2, n3, n4], 12.3, { y: 60 });
        const t3 = P.title(["UN RAPPEL OUBLIÉ", "= <span class='red'>UN MANDAT PERDU.</span>"], { top: "620px", fontSize: "76px" }, 12.6, { slam: 0.35 });
        const s3 = P.text("ctr p-serif", "LIMO ne t’en laisse passer aucun.", { top: "860px", fontSize: "54px" }, 13.6);
        P.out([t3, s3], 15.2);
        window.__TE = 15.9;
        P.outro(15.4, "dm");
""")

# ---------------------------------------------------------------- 2 · dimanche 18 h
FILMS["film-02-dimanche-18h"] = ("Film 2 · Dimanche 18 h", """
      .task { left: 160px; width: 760px; height: 104px; border-radius: 24px; background: #1c1830; border: 2px solid #2d2748;
        display: flex; align-items: center; gap: 20px; padding: 0 28px; font-family: Montserrat, sans-serif; font-weight: 600; font-size: 32px; color: #fff;
        box-shadow: 0 14px 30px rgba(0,0,0,.4); }
      .task .dt { flex: none; width: 18px; height: 18px; border-radius: 50%; background: var(--red); }
      .task .ck { margin-left: auto; width: 46px; height: 46px; border-radius: 50%; background: var(--ok); display: flex; align-items: center; justify-content: center; color: #06281c; }
      .task .ck svg.i { width: 28px; height: 28px; stroke-width: 3; }
""", """
        const t1 = P.title(["DIMANCHE,", "<em>18 H.</em>"], { top: "190px", fontSize: "140px" }, 0.1, { slam: 0.4 });
        const s1 = P.text("ctr p-serif", "Toi, sans LIMO :", { top: "560px", fontSize: "52px" }, 1.0);
        const T = ["12 relances à trier", "Compromis Roche à saisir", "3 annonces à rédiger", "Les posts de la semaine", "2 avis Google sans réponse", "L’anniversaire de Mme Roy ?"];
        const cards = T.map((x, i) => {
          const c = P.ab("task", `<i class="dt"></i>${x}<span class="ck">${K.icon("check")}</span>`, { top: 680 + i * 122 + "px" });
          tl.set(c, { opacity: 0 }, 0);
          tl.set(K.$(".ck", c), { scale: 0 }, 0);
          const t = 1.4 + i * 0.32;
          tl.fromTo(c, { opacity: 0, y: -260, rotation: (i % 2 ? 1 : -1) * 6 }, { opacity: 1, y: 0, rotation: (i % 2 ? 1 : -1) * 1.5, duration: 0.4, ease: "bounce.out" }, t);
          K.sfx(t + 0.25, "drop", 0.18, (i % 2 ? 0.3 : -0.3));
          return c;
        });
        const bad = P.pill("red", "alert", "6 tâches en retard pour lundi", { top: "1440px" }, 3.5);
        P.out([s1, bad], 4.8);
        const s2 = P.text("ctr p-serif", "Avec LIMO :", { top: "560px", fontSize: "52px" }, 5.0);
        cards.forEach((c, i) => {
          const t = 5.4 + i * 0.28;
          tl.to(K.$(".ck", c), { scale: 1, duration: 0.25, ease: "back.out(2.5)" }, t);
          tl.to(K.$(".dt", c), { backgroundColor: "#2bd99a", duration: 0.2 }, t);
          K.sfx(t, "tick", 0.2, 0, { f: 1800 + i * 150 });
          tl.to(c, { x: 1100, opacity: 0, rotation: 4, duration: 0.4, ease: "power2.in" }, t + 0.35);
        });
        const good = P.pill("ok", "check", "0 tâche en retard", { top: "1000px" }, 7.6);
        P.out([t1, s2, good], 8.7);
        const t3 = P.title(["DIMANCHE 18 H :", "<em>TOUT EST PRÊT.</em>"], { top: "250px", fontSize: "96px" }, 9.0, { slam: 0.35 });
        const ph = P.photo({ left: "60px", top: "560px", width: "960px", height: "578px" }, 9.2);
        const s3 = P.text("ctr p-serif", "Ton brief de lundi est déjà écrit.<br>Toi, tu profites.", { top: "1200px", fontSize: "50px", lineHeight: "1.35" }, 10.2);
        P.out([t3, ph, s3], 12.4);
        window.__TE = 13.1;
        P.outro(12.6, "essai");
""")

# ---------------------------------------------------------------- 3 · le calcul
FILMS["film-03-le-calcul"] = ("Film 3 · Le calcul", """
      .row { left: 90px; width: 900px; height: 118px; display: flex; align-items: center; justify-content: space-between;
        border-bottom: 2px solid rgba(255,255,255,.1); font-family: Montserrat, sans-serif; }
      .row b { font-weight: 600; font-size: 38px; color: #fff; }
      .row span { font-family: "JetBrains Mono", monospace; font-weight: 700; font-size: 36px; color: var(--vio-l); }
      #tot { top: 1130px; font-family: Montserrat, sans-serif; font-weight: 800; font-size: 170px; }
""", """
        const k = P.text("ctr p-kick", "LE CALCUL QUI FAIT MAL", { top: "250px" }, 0.1);
        const t1 = P.title(["COMBIEN D’HEURES", "TU PERDS", "<em>CHAQUE SEMAINE ?</em>"], { top: "560px", fontSize: "84px" }, 0.3, { slam: 0.35 });
        P.out(t1, 2.5);
        const R = [["Saisir 2 compromis", "2 × 30 min"], ["Rédiger 4 annonces", "4 × 45 min"], ["Trier tes relances", "5 × 15 min"], ["Posts réseaux", "3 × 20 min"], ["Répondre aux avis", "3 × 10 min"]];
        const rows = R.map((r, i) => {
          const e = P.ab("row", `<b>${r[0]}</b><span>${r[1]}</span>`, { top: 360 + i * 130 + "px" });
          tl.set(e, { opacity: 0 }, 0);
          K.fin(e, 2.8 + i * 0.45, { y: 24 });
          K.sfx(2.8 + i * 0.45, "pop", 0.14, 0, { f: 500 + i * 70 });
          return e;
        });
        const lab = P.text("ctr p-kick", "PAR SEMAINE", { top: "1070px" }, 5.2);
        const tot = P.ab("ctr", `<em style="font-style:normal;background:linear-gradient(90deg,#a893ff,#7b5cff 55%,#00c6fc);-webkit-background-clip:text;background-clip:text;color:transparent">0 h 00</em>`, {});
        tot.id = "tot";
        tl.set(tot, { opacity: 0 }, 0);
        tl.set(tot, { opacity: 1 }, 5.3);
        const em = K.$("em", tot);
        K.count(em, 405, 5.3, 1.3, (v) => `${Math.floor(v / 60)} h ${String(Math.round(v % 60)).padStart(2, "0")}`);
        K.sfx(6.6, "slam", 0.35);
        const note = P.text("ctr p-sm", "Exemple indicatif, à ajuster à ton activité", { top: "1680px", fontSize: "24px", color: "#8f8ba8" }, 5.3);
        P.out([...rows, lab, tot], 7.9);
        const y1 = P.title(["SUR UN AN :", "<em>≈ 310 HEURES.</em>"], { top: "520px", fontSize: "104px" }, 8.2, { slam: 0.35 });
        const y2 = P.text("ctr p-serif", "Presque <b>8 semaines</b> de travail<br>passées à faire de l’administratif.", { top: "860px", fontSize: "50px", lineHeight: "1.35" }, 9.1);
        P.out([y1, y2, k, note], 11.2);
        const q = P.title(["ET SI LIMO", "<em>S’EN OCCUPAIT ?</em>"], { top: "700px", fontSize: "96px" }, 11.4, { slam: 0.4 });
        P.out(q, 13.3);
        window.__TE = 14.0;
        P.outro(13.5, "demo");
""")

# ---------------------------------------------------------------- 4 · fais le test
FILMS["film-04-fais-le-test"] = ("Film 4 · Fais le test", """
      .it { left: 90px; width: 900px; height: 150px; border-radius: 28px; background: #16132a; border: 2px solid #2a2445;
        display: flex; align-items: center; gap: 26px; padding: 0 30px; font-family: Montserrat, sans-serif; font-weight: 600; font-size: 34px; line-height: 1.25; color: #fff; }
      .it .bx { flex: none; width: 64px; height: 64px; border-radius: 18px; border: 4px solid #4a4370; position: relative; }
      .it .bx i { position: absolute; inset: -4px; border-radius: 18px; background: var(--vio); display: flex; align-items: center; justify-content: center; color: #fff; }
      .it .bx svg.i { width: 40px; height: 40px; stroke-width: 3.2; }
      #score { right: 90px; top: 150px; height: 80px; padding: 0 28px; border-radius: 40px; background: #fff; display: flex; align-items: center;
        font-family: Montserrat, sans-serif; font-weight: 800; font-size: 40px; color: var(--vio); }
      #robo { left: 390px; top: 1020px; width: 300px; height: 375px; object-fit: contain; }
""", """
        const t1 = P.title(["AGENT IMMO :", "<em>FAIS LE TEST.</em>"], { top: "250px", fontSize: "100px" }, 0.1, { slam: 0.4 });
        const sc = P.ab("", [0, 1, 2, 3, 4, 5].map((n) => `<span class="sn" style="position:absolute;left:0;right:0;text-align:center">${n}/5</span>`).join("") + `<span style="visibility:hidden">5/5</span>`, {});
        sc.id = "score";
        tl.set(sc, { opacity: 0 }, 0);
        K.pop(sc, 1.0);
        const sn = K.$$(".sn", sc);
        sn.slice(1).forEach((x) => tl.set(x, { opacity: 0 }, 0));
        const S = ["T’as déjà oublié de rappeler un vendeur.", "Tu écris tes annonces le soir.", "Tu recopies tes compromis à la main.", "Tu ne sais plus qui relancer.", "Un avis Google attend ta réponse."];
        const its = S.map((s, i) => {
          const e = P.ab("it", `<span class="bx"><i>${K.icon("check")}</i></span>${s}`, { top: 560 + i * 176 + "px" });
          tl.set(e, { opacity: 0 }, 0);
          tl.set(K.$(".bx i", e), { scale: 0 }, 0);
          const t = 1.4 + i * 1.0;
          K.fin(e, t, { y: 30 });
          K.sfx(t, "whoosh", 0.1, 0.2, { d: 0.3, f0: 600, f1: 3000, pk: 0.5 });
          tl.to(K.$(".bx i", e), { scale: 1, duration: 0.28, ease: "back.out(2.6)" }, t + 0.55);
          K.sfx(t + 0.55, "tick", 0.26, 0, { f: 1600 + i * 200 });
          tl.set(sn[i], { opacity: 0 }, t + 0.6);
          tl.set(sn[i + 1], { opacity: 1 }, t + 0.6);
          tl.fromTo(sc, { scale: 1.25 }, { scale: 1, duration: 0.3, ease: "back.out(2)", immediateRender: false }, t + 0.6);
          return e;
        });
        P.out([t1, ...its], 6.9);
        const t2 = P.title(["5 SUR 5 ?", "<em>IL TE FAUT</em>", "<em>UN BRAS DROIT.</em>"], { top: "420px", fontSize: "96px" }, 7.2, { slam: 0.4 });
        const robo = K.h("img", "ab", null, root);
        robo.id = "robo";
        robo.src = "assets/img/limo-robot.png";
        robo.alt = "Robot LIMO";
        tl.set(robo, { opacity: 0 }, 0);
        tl.fromTo(robo, { opacity: 0, y: 80, scale: 0.6 }, { opacity: 1, y: 0, scale: 1, duration: 0.55, ease: "back.out(1.7)" }, 8.1);
        K.sfx(8.15, "thump", 0.4);
        K.sfx(8.2, "bloop-up", 0.22, 0, { f0: 260, f1: 780, d: 0.16 });
        const s2 = P.text("ctr p-sm", "Et commente ton score !", { top: "1450px" }, 8.9);
        P.out([t2, robo, s2, sc], 10.6);
        window.__TE = 11.3;
        P.outro(10.8, "comment");
""")

# ---------------------------------------------------------------- 5 · ton téléphone bosse
FILMS["film-05-ton-telephone-bosse"] = ("Film 5 · Ton téléphone bosse", "", """
        const t1 = P.title(["PENDANT QUE", "TU FAIS TES VISITES…"], { top: "180px", fontSize: "76px" }, 0.1, { slam: 0.35 });
        const { ph, halo } = P.phone({ left: "213px", top: "560px" }, 0.8);
        const N = [
          ["BRIEF", "8:00", "sparkles", "", "Brief prêt : 5 actions aujourd’hui."],
          ["ANNIVERSAIRE", "9:30", "cake", "cy", "Mme Roy : SMS d’anniversaire prêt."],
          ["NOUVELLE PISTE", "11:00", "pin", "ok", "DPE F à 300 m : vendeur potentiel."],
          ["COMPROMIS", "14:00", "file", "cy", "Compromis Roche lu : fiche remplie."],
          ["AVIS GOOGLE", "16:30", "star", "", "Marie L., 5 étoiles : réponse prête."],
          ["RAPPEL", "18:00", "bell", "red", "M. Albert attend ton rappel."],
        ];
        const els = [];
        N.forEach((n, i) => {
          const t = 2.0 + i * 1.05;
          els.forEach((e, j) => {
            const depth = i - j;
            tl.to(e, { y: 180 * depth, scale: 1 - 0.03 * depth, opacity: depth >= 4 ? 0 : 1, duration: 0.4, ease: "power3.out" }, t);
          });
          const e = P.notif({ title: n[0], time: n[1], icon: n[2], c: n[3], text: n[4], pan: i % 2 ? 0.3 : -0.3 }, { left: "90px", top: "470px", transformOrigin: "50% 0" }, t);
          els.push(e);
        });
        P.out([t1, ph, halo, ...els], 8.7, { y: 60 });
        const t2 = P.title(["…LIMO FAIT", "<em>TOUT LE RESTE.</em>"], { top: "700px", fontSize: "110px" }, 9.0, { slam: 0.4 });
        P.out(t2, 11.0);
        window.__TE = 11.7;
        P.outro(11.2, "essai");
""")

# ---------------------------------------------------------------- 6 · tout-en-un
FILMS["film-06-tout-en-un"] = ("Film 6 · Tout-en-un", """
      .tile { width: 290px; height: 190px; border-radius: 28px; background: #16132a; border: 2px solid #2a2445;
        display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 14px;
        font-family: Montserrat, sans-serif; font-weight: 700; font-size: 25px; color: #fff; text-align: center; line-height: 1.15; }
      .tile .ic { width: 74px; height: 74px; border-radius: 22px; background: rgba(123,92,255,.2); color: var(--vio-l); display: flex; align-items: center; justify-content: center; }
      .tile .ic svg.i { width: 40px; height: 40px; }
      #hs { left: 290px; top: 700px; width: 500px; height: 441px; }
      #hs img { width: 500px; height: 441px; }
""", """
        const t1 = P.title(["11 OUTILS.", "<em>1 SEUL ASSISTANT.</em>"], { top: "200px", fontSize: "96px" }, 0.1, { slam: 0.4 });
        const TL = [["zap", "Brief du jour"], ["mic", "Dictée vocale"], ["file", "Lecture de compromis"], ["calc", "Estimation DVF"], ["pen", "Annonces"], ["image", "Posts réseaux"], ["camera", "Photos « VENDU »"], ["msg", "SMS clients"], ["star", "Avis Google"], ["radar", "Pistes DPE"], ["scale", "Questions juridiques"]];
        const tiles = TL.map((x, i) => {
          const col = i % 3, row = Math.floor(i / 3);
          const left = row === 3 ? 245 + col * 310 : 85 + col * 310;
          const e = P.ab("tile", `<span class="ic">${K.icon(x[0])}</span>${x[1]}`, { left: left + "px", top: 560 + row * 210 + "px" });
          tl.set(e, { opacity: 0 }, 0);
          const t = 1.1 + i * 0.13;
          tl.fromTo(e, { opacity: 0, scale: 0.5, y: 40 }, { opacity: 1, scale: 1, y: 0, duration: 0.4, ease: "back.out(1.8)" }, t);
          K.sfx(t, "pop", 0.1, (col - 1) * 0.4, { f: 480 + i * 40 });
          return { e, cx: left + 145, cy: 560 + row * 210 + 95 };
        });
        const s1 = P.text("ctr p-serif", "Fini de jongler entre six applis.", { top: "1450px", fontSize: "48px" }, 3.0);
        P.out([t1, s1], 4.6);
        tiles.forEach((o, i) => {
          tl.to(o.e, { x: 540 - o.cx, y: 920 - o.cy, scale: 0.15, opacity: 0, rotation: (i % 2 ? 1 : -1) * 40, duration: 0.55, ease: "power3.in" }, 4.7 + i * 0.04);
        });
        K.sfx(4.7, "whoosh", 0.24, 0, { d: 0.8, f0: 3000, f1: 300, pk: 0.8 });
        const hs = P.ab("", `<img src="assets/img/limo-house.png" alt="Logo LIMO" />`, {});
        hs.id = "hs";
        tl.set(hs, { opacity: 0 }, 0);
        tl.fromTo(hs, { opacity: 0, scale: 0.3 }, { opacity: 1, scale: 1, duration: 0.6, ease: "back.out(1.6)" }, 5.3);
        K.sfx(5.35, "thump", 0.5);
        K.burst(K.sparkles(root, 540, 920, 18, 340, 300, 5), 5.35);
        const t2 = P.title(["TOUT DANS", "<em>UN SEUL OUTIL.</em>"], { top: "1230px", fontSize: "96px" }, 5.8, { slam: 0.3 });
        P.out([hs, t2], 8.2);
        window.__TE = 8.9;
        P.outro(8.4, "demo");
""")

# ---------------------------------------------------------------- 7 · mythes vs réalité
FILMS["film-07-mythes-realite"] = ("Film 7 · Mythes et réalité", """
      .strike { left: 120px; width: 840px; height: 8px; border-radius: 4px; background: var(--red); transform-origin: 0 50%; }
""", """
        const k = P.text("ctr p-kick", "IDÉES REÇUES", { top: "250px" }, 0.1);
        const t1 = P.title(["L’IA POUR LES", "<em>AGENTS IMMO ?</em>"], { top: "620px", fontSize: "104px" }, 0.3, { slam: 0.4 });
        P.out(t1, 2.2);
        const M = [
          ["« C’est trop compliqué. »", "Tu parles.<br><em>LIMO écrit.</em>"],
          ["« C’est hors de prix. »", "Dès<br><em>49 € par mois.</em>"],
          ["« L’IA va remplacer les agents. »", "Elle remplace la paperasse.<br><em>Pas toi.</em>"],
        ];
        M.forEach((m, i) => {
          const t = 2.5 + i * 3.1;
          const mp = P.pill("red", "x", "MYTHE", { top: "620px" }, t, { snd: false });
          const my = P.text("ctr p-serif", m[0], { top: "740px", fontSize: "60px", lineHeight: "1.25" }, t + 0.1);
          const st = P.ab("strike", null, { top: "780px" });
          tl.set(st, { scaleX: 0 }, 0);
          tl.to(st, { scaleX: 1, duration: 0.3, ease: "power3.out" }, t + 0.9);
          tl.to(my, { opacity: 0.45, duration: 0.3 }, t + 0.95);
          K.sfx(t + 0.9, "buzz", 0.16);
          const rp = P.pill("ok", "check", "RÉALITÉ", { top: "1000px" }, t + 1.4);
          const re = P.text("ctr p-mid", m[1], { top: "1120px", fontSize: "74px" }, t + 1.5);
          P.out([mp, my, st, rp, re], t + 2.8);
        });
        P.out(k, 11.6);
        window.__TE = 12.4;
        P.outro(11.9, "dm");
""")

# ---------------------------------------------------------------- 8 · manifeste
FILMS["film-08-manifeste"] = ("Film 8 · Manifeste", "", """
        const a = P.text("ctr p-serif", "Tu n’es pas devenu agent immo", { top: "800px", fontSize: "62px" }, 0.2, { d: 0.9 });
        const b = P.title(["pour remplir des cases."], { top: "920px", fontSize: "70px" }, 1.3, { cls: "ctr p-mid", slam: 0.25 });
        P.out([a, b], 3.4);
        const c = P.text("ctr p-serif", "Tu l’es devenu pour les gens.", { top: "660px", fontSize: "62px" }, 3.7, { d: 0.8 });
        const d = P.text("ctr p-serif", "Les visites. Les familles.", { top: "840px", fontSize: "62px" }, 4.7, { d: 0.8 });
        const e = P.title(["<em>Les clés qu’on remet.</em>"], { top: "1040px", fontSize: "84px" }, 5.7, { cls: "ctr p-mid", slam: 0.3 });
        K.sfx(5.7, "sparkle", 0.18);
        P.out([c, d, e], 7.9);
        const t = P.title(["LA PAPERASSE ?", "<em>LAISSE-LA À LIMO.</em>"], { top: "250px", fontSize: "90px" }, 8.2, { slam: 0.4 });
        const ph = P.photo({ left: "60px", top: "560px", width: "960px", height: "578px" }, 8.4);
        const s = P.text("ctr p-serif", "Toi, retourne sur le terrain.", { top: "1200px", fontSize: "54px" }, 9.6);
        P.out([t, ph, s], 11.6);
        window.__TE = 12.3;
        P.outro(11.8, "essai");
""")

# ---------------------------------------------------------------- 9 · le prix d'un café
FILMS["film-09-prix-cafe"] = ("Film 9 · Le prix d’un café", """
      #cup { left: 120px; top: 760px; width: 360px; height: 360px; }
      #cup svg { width: 360px; height: 360px; }
      .eq { left: 520px; width: 480px; font-family: Montserrat, sans-serif; font-weight: 700; font-size: 52px; color: #fff; }
      .eq.big { font-weight: 800; font-size: 76px; }
""", """
        const t1 = P.title(["LIMO COÛTE", "MOINS CHER QUE", "<em>TON CAFÉ.</em>"], { top: "240px", fontSize: "100px" }, 0.1, { slam: 0.4 });
        const cup = P.ab("", `<svg viewBox="0 0 200 200"><path class="st" d="M70 60 C60 45 80 35 70 20" stroke="#c9c6e6" stroke-width="5" fill="none" stroke-linecap="round"/><path class="st" d="M100 60 C90 45 110 35 100 20" stroke="#c9c6e6" stroke-width="5" fill="none" stroke-linecap="round"/><path class="st" d="M130 60 C120 45 140 35 130 20" stroke="#c9c6e6" stroke-width="5" fill="none" stroke-linecap="round"/><path d="M40 75 H160 L148 170 Q146 182 132 182 H68 Q54 182 52 170Z" fill="#f5f4fa"/><path d="M160 95 Q192 95 190 122 Q188 150 154 150" stroke="#f5f4fa" stroke-width="12" fill="none"/><rect x="40" y="75" width="120" height="16" fill="#6b4f3a"/></svg>`, {});
        cup.id = "cup";
        tl.set(cup, { opacity: 0 }, 0);
        tl.fromTo(cup, { opacity: 0, scale: 0.6, rotation: -10 }, { opacity: 1, scale: 1, rotation: 0, duration: 0.6, ease: "back.out(1.7)" }, 1.4);
        tl.fromTo(K.$$(".st", cup), { y: 0, opacity: 0.2 }, { y: -8, opacity: 1, duration: 0.6, ease: "sine.inOut", yoyo: true, repeat: 5, stagger: 0.15 }, 1.6);
        K.sfx(1.4, "pop", 0.2, -0.3, { f: 420 });
        const e1 = P.text("eq", "49 € / mois", { top: "800px" }, 2.0);
        const e2 = P.text("eq", "÷ 30 jours", { top: "890px", color: "#a893ff" }, 2.6);
        const e3 = P.ab("eq big", `= <span>0,00</span> €<br><small style="font-size:34px;color:#c9c6e6">par jour</small>`, { top: "990px" });
        tl.set(e3, { opacity: 0 }, 0);
        K.fin(e3, 3.2, { y: 20 });
        K.count(K.$("span", e3), 1.63, 3.3, 1.0, (v) => v.toFixed(2).replace(".", ","));
        K.sfx(4.35, "slam", 0.3);
        P.out([t1, cup, e1, e2, e3], 5.6);
        const k2 = P.text("ctr p-kick", "ET EN FACE ?", { top: "520px" }, 5.9);
        const f1 = P.text("ctr p-mid", "Une vente à 200 000 €", { top: "680px", fontSize: "64px" }, 6.2);
        const f2 = P.text("ctr p-mid", "× 5 % d’honoraires", { top: "800px", fontSize: "64px", color: "#a893ff" }, 6.8);
        const f3 = P.ab("ctr p-big", `= <em>0 €</em>`, { top: "930px", fontSize: "130px" });
        tl.set(f3, { opacity: 0 }, 0);
        K.fin(f3, 7.4, { y: 20 });
        K.count(K.$("em", f3), 10000, 7.5, 1.0, (v) => String(Math.round(v / 100) * 100).replace(/\\B(?=(\\d{3})+(?!\\d))/g, " ") + " €");
        K.sfx(8.55, "slam", 0.35);
        const note = P.text("ctr p-sm", "Exemple indicatif", { top: "1170px", fontSize: "26px", color: "#8f8ba8" }, 7.5);
        P.out([k2, f1, f2, f3, note], 9.6);
        const t2 = P.title(["UN MANDAT DE PLUS", "<em>ET LIMO EST PAYÉ</em>", "<em>POUR DES ANNÉES.</em>"], { top: "620px", fontSize: "82px" }, 9.9, { slam: 0.4 });
        P.out(t2, 12.2);
        window.__TE = 12.9;
        P.outro(12.4, "essai");
""")

# ---------------------------------------------------------------- 10 · de la visite au mandat
FILMS["film-10-visite-au-mandat"] = ("Film 10 · De la visite au mandat", """
      #track { left: 0; top: 0; width: 1080px; height: 1920px; }
      .rail { left: 150px; width: 6px; top: 640px; height: 1260px; border-radius: 3px; background: rgba(255,255,255,.12); }
      .fill { left: 150px; width: 6px; top: 640px; height: 1260px; border-radius: 3px; background: linear-gradient(180deg, #7b5cff, #00c6fc); transform-origin: 50% 0; }
      .node { left: 129px; width: 48px; height: 48px; border-radius: 50%; background: #1a1628; border: 4px solid #3a3358; }
      .step { left: 210px; width: 790px; height: 150px; border-radius: 28px; background: #16132a; border: 2px solid #2a2445;
        display: flex; align-items: center; gap: 24px; padding: 0 28px; font-family: Montserrat, sans-serif; }
      .step .ic { flex: none; width: 80px; height: 80px; border-radius: 22px; background: rgba(123,92,255,.2); color: var(--vio-l); display: flex; align-items: center; justify-content: center; }
      .step .ic svg.i { width: 42px; height: 42px; }
      .step b { display: block; font-weight: 700; font-size: 36px; color: #fff; }
      .step span { display: block; margin-top: 6px; font-weight: 500; font-size: 26px; color: #b4b0cf; }
      .step.win { background: linear-gradient(90deg, rgba(43,217,154,.25), rgba(43,217,154,.08)); border-color: rgba(43,217,154,.6); }
      .step.win .ic { background: var(--ok); color: #06281c; }
""", """
        const t1 = P.title(["DE LA VISITE", "<em>AU MANDAT.</em>"], { top: "180px", fontSize: "110px" }, 0.1, { slam: 0.4 });
        const k = P.text("ctr p-kick", "SANS RIEN RESSAISIR", { top: "470px" }, 0.8);
        const track = P.ab("", null, {});
        track.id = "track";
        const rail = P.ab("rail", null, {}, track);
        const fill = P.ab("fill", null, {}, track);
        tl.set(fill, { scaleY: 0 }, 0);
        tl.set([rail], { opacity: 0 }, 0);
        tl.to(rail, { opacity: 1, duration: 0.3 }, 1.2);
        const ST = [
          ["mic", "Tu dictes ta visite", "« Maison 120 m², ils vendent en mars. »"],
          ["users", "La fiche vendeur se remplit", "Famille Martin · relance J+7"],
          ["calc", "L’estimation tombe", "312 000 € · 14 ventes DVF"],
          ["pen", "L’annonce s’écrit", "Mentions légales incluses"],
          ["image", "Les posts sont prêts", "LinkedIn publié · Instagram prêt"],
          ["bell", "La relance est programmée", "Jeudi 10 h : rappeler M. Martin"],
          ["trophy", "Mandat signé.", "Et tu n’as rien recopié."],
        ];
        const GAP = 178;
        ST.forEach((s, i) => {
          const y = 640 + i * GAP;
          const t = 1.5 + i * 1.2;
          const nd = P.ab("node", null, { top: y + 51 + "px" }, track);
          const st = P.ab("step" + (i === ST.length - 1 ? " win" : ""), `<span class="ic">${K.icon(s[0])}</span><div><b>${s[1]}</b><span>${s[2]}</span></div>`, { top: y + "px" }, track);
          tl.set([nd, st], { opacity: 0 }, 0);
          tl.fromTo(nd, { opacity: 0, scale: 0.4 }, { opacity: 1, scale: 1, duration: 0.3, ease: "back.out(2.5)" }, t);
          tl.fromTo(nd, { backgroundColor: "#1a1628" }, { backgroundColor: i === ST.length - 1 ? "#2bd99a" : "#00C6FC", duration: 0.2, immediateRender: false }, t + 0.1);
          tl.to(fill, { scaleY: (i * GAP + 75) / 1260, duration: 0.5, ease: "power2.out" }, t);
          tl.fromTo(st, { opacity: 0, x: 220 }, { opacity: 1, x: 0, duration: 0.45, ease: "power3.out" }, t + 0.05);
          K.sfx(t + 0.05, "whoosh", 0.12, 0.3, { d: 0.3, f0: 500, f1: 3500, pk: 0.5 });
          K.sfx(t + 0.3, i === ST.length - 1 ? "fanfare" : "tick", i === ST.length - 1 ? 0.25 : 0.2, 0, { f: 1500 + i * 180 });
          if (i >= 4) tl.to(track, { y: -(i - 3) * GAP, duration: 0.6, ease: "power2.inOut" }, t - 0.1);
        });
        tl.to([t1, k], { opacity: 0, y: -60, duration: 0.4, ease: "power2.in" }, 6.2);
        K.burst(K.sparkles(root, 600, 1170, 18, 460, 120, 6), 1.5 + 6 * 1.2 + 0.3);
        P.out([track], 10.8, { y: -60 });
        window.__TE = 11.5;
        P.outro(11.0, "demo");
""")

DUR = {
    "film-01-mandat-perdu": 19.0,
    "film-02-dimanche-18h": 16.2,
    "film-03-le-calcul": 17.1,
    "film-04-fais-le-test": 14.4,
    "film-05-ton-telephone-bosse": 14.8,
    "film-06-tout-en-un": 12.0,
    "film-07-mythes-realite": 15.5,
    "film-08-manifeste": 15.4,
    "film-09-prix-cafe": 16.0,
    "film-10-visite-au-mandat": 14.6,
}

if __name__ == "__main__":
    for name, (title, css, body) in FILMS.items():
        html = SHELL.format(title=title, css=css.strip("\n"), body=body.strip("\n"), dur=DUR[name], name=name)
        pathlib.Path(f"reels/{name}.html").write_text(html, encoding="utf-8")
        print("reels/" + name + ".html")
