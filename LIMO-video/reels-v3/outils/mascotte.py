"""Série « Mascotte » : 10 Reels où la mascotte officielle LIMO parle aux agents immo.

Mascotte : assets/img/mascotte-corps.png (visière vide) + yeux animés en SVG (N.mascot, kit naturel).
Données fictives. Usage : python3 outils/mascotte.py   (réécrit reels/mascotte-*.html)
"""
import pathlib

from hooks import FACES, SHELL

# Fin commune : la mascotte rétrécit en bas à droite et salue pendant la carte de fin.
END = """
        const endM = (M, left, top, W, t) => {
          const H = (W * 904) / 747;
          const s = 260 / W;
          M.move(t, { x: 890 - (left + W / 2), y: 1610 - (top + H / 2), scale: s, rotation: -8 }, 0.7);
          M.expr("happy", t + 0.1, false);
          M.wave(t + 0.9);
          M.blink(t + 2.4);
        };
"""

FILMS = {}

# ---------------------------------------------------------------- 1 · présentation
FILMS["mascotte-01-salut-agent-immo"] = ("Salut l’agent immo, moi c’est LIMO", 15.2, "", """
        const hk = N.hook(["TON NOUVEL", "<span class='hl'>ASSISTANT</span>", "EST ARRIVÉ<span class='v'>.</span>"], { top: "220px", fontSize: "108px" });
        const M = N.mascot({ left: "260px", top: "800px", width: "560px" });
        M.float(0, 11);
        M.wave(0.3);
        M.blink(1.9);
        const b0 = N.say("Salut l’agent immo !<br><span class='v'>Moi, c’est LIMO.</span>", { left: "190px", top: "600px", width: "700px" }, 0.9);
        N.out([hk], 2.7, { y: -40 });
        N.out(b0, 2.7, { y: -10, d: 0.2 });
        const L = [["J’écris tes annonces.", "open", "Mentions légales incluses"], ["Je relance tes vendeurs.", "wink", "Au bon moment, avec le bon message"], ["Je réponds à tes avis Google.", "happy", "En 1 minute"], ["Je prépare ta journée.", "open", "Chaque matin à 7 h 30"]];
        const bs = L.map((l, i) => {
          const t = 3.0 + i * 1.5;
          const b = N.say(`${l[0]}<small>${l[2]}</small>`, { left: "140px", top: "430px", width: "800px" }, t);
          M.expr(l[1], t, false);
          if (i === 3) M.glow(t, 1.2);
          M.hop(t + 0.1, 50);
          if (i < 3) N.out(b, t + 1.35, { y: -10, d: 0.15 });
          return b;
        });
        N.out(bs[3], 9.0, { y: -10, d: 0.15 });
        const b5 = N.say("Et je ne prends <span class='v'>jamais</span><br>de vacances.", { left: "190px", top: "480px", width: "700px" }, 9.2, { cls: "" });
        M.expr("wink", 9.3);
        M.hop(9.4);
        N.out(b5, 11.2, { y: -10, d: 0.2 });
        window.__TE = 11.4;
        N.outro(11.4, "dm");
        endM(M, 260, 800, 560, 11.3);
""")

# ---------------------------------------------------------------- 2 · entretien d'embauche
FILMS["mascotte-02-entretien-embauche"] = ("Entretien d’embauche", 16.2, """
      .stamp { font-family: "Montserrat Hook", Montserrat, sans-serif; font-weight: 800; font-size: 110px; color: #15877d; border: 12px solid #15877d; border-radius: 26px; padding: 6px 40px; }
""", """
        const chip = N.chip(`${K.icon("users")}ENTRETIEN D’EMBAUCHE`, { top: "200px" });
        const hk = N.hook(["POSTE :", "<span class='hl'>ASSISTANT</span>", "D’AGENT IMMO<span class='v'>.</span>"], { top: "300px", fontSize: "100px" });
        const M = N.mascot({ left: "330px", top: "1060px", width: "420px" }, { expr: "open" });
        M.float(0, 12, 10);
        M.expr("think", 1.3, false);
        N.out([chip, hk], 2.6, { y: -40 });
        const QA = [["Vos horaires ?", "24 h / 24. 7 j / 7.", "happy"], ["Et vos congés ?", "Des congés… c’est quoi ?", "wow"], ["Votre salaire ?", "Dès 49 € par mois.", "euro"], ["Vous commencez quand ?", "Tout de suite.<br>14 jours offerts.", "heart"]];
        QA.forEach((q, i) => {
          const t = 2.8 + i * 1.9;
          const Q = N.say(q[0], { left: "90px", top: "320px", width: "620px" }, t, { tail: "down", tx: "90px", n: 0, g: 0 });
          K.sfx(t, "pop", 0.14);
          M.expr("think", t, false);
          const A = N.say(q[1], { left: "300px", top: "760px", width: "690px" }, t + 0.7, { cls: "vio", tail: "down", tx: "240px" });
          M.expr(q[2], t + 0.7, false);
          M.hop(t + 0.75, 40);
          N.out([Q, A], t + 1.75, { y: -10, d: 0.15 });
        });
        const st = N.ab("ctr", `<span class="stamp">EMBAUCHÉ</span>`, { top: "480px" });
        N.hide(st);
        tl.fromTo(st, { opacity: 0, scale: 2.2, rotation: -14 }, { opacity: 1, scale: 1, rotation: -8, duration: 0.3, ease: "power4.in" }, 10.5);
        K.sfx(10.78, "stamp", 0.4);
        M.expr("happy", 10.8);
        M.hop(10.9, 110);
        N.out(st, 12.2, { y: -20 });
        window.__TE = 12.4;
        N.outro(12.4, "essai");
        endM(M, 330, 1060, 420, 12.3);
""")

# ---------------------------------------------------------------- 3 · 3 h du matin
FILMS["mascotte-03-3h-du-matin"] = ("3 h du matin", 15.4, "", """
        const night = N.ab("", null, { left: "0", top: "0", width: "1080px", height: "1920px", background: "linear-gradient(180deg, #10122b 0%, #23265c 100%)" });
        const hk = N.hook(["3 H DU MATIN<span class='v'>.</span>", "TOI, TU DORS<span class='v'>.</span>", "<span class='hl'>LUI, NON.</span>"], { top: "300px", fontSize: "100px", color: "#ffffff" });
        const M = N.mascot({ left: "300px", top: "1020px", width: "480px" }, { expr: "open" });
        M.float(0, 7, 10);
        M.glow(0.4, 1.4);
        N.out(hk, 2.5, { y: -40 });
        const L = [["ANNONCE", "3:02", "Maison à Allassac : annonce rédigée, mentions légales incluses."], ["RELANCES", "3:15", "12 relances vendeurs préparées pour demain."], ["AVIS GOOGLE", "4:40", "2 réponses prêtes à publier."], ["BRIEF DU MATIN", "6:00", "Ta journée est prête. On commence par M. Albert."]];
        const ns = L.map((l, i) => {
          const t = 2.8 + i * 0.95;
          M.blink(t + 0.4);
          return N.notif({ title: l[0], time: l[1], text: l[2], g: 0.2 }, { left: "90px", top: 170 + i * 200 + "px" }, t);
        });
        M.glow(3.8, 1.2);
        N.out(ns, 7.2, { y: -30 });
        tl.to(night, { opacity: 0, duration: 0.9, ease: "power2.inOut" }, 7.3);
        K.sfx(7.3, "riser", 0.12, 0, { d: 0.8 });
        M.expr("happy", 7.8);
        M.wave(7.9);
        const b = N.say("Bonjour ! Ta journée<br>est <span class='v'>déjà prête</span>.", { left: "190px", top: "760px", width: "700px" }, 8.0);
        K.sfx(8.0, "success", 0.2);
        N.out(b, 10.0, { y: -10, d: 0.2 });
        const c = N.cap("Il bosse la nuit.<br>Toi, tu signes le jour.", { top: "560px" }, 10.2, { dark: true });
        N.out(c, 11.6, { y: -20 });
        window.__TE = 11.8;
        N.outro(11.8, "essai");
        endM(M, 300, 1020, 480, 11.7);
""")

# ---------------------------------------------------------------- 4 · il réagit
FILMS["mascotte-04-il-reagit"] = ("LIMO réagit à tes habitudes", 15.4, "", """
        const chip = N.chip(`${K.icon("alert")}ÇA PIQUE UN PEU`, { top: "200px" });
        const hk = N.hook(["LIMO RÉAGIT", "À TES", "<span class='hl'>HABITUDES.</span>"], { top: "300px", fontSize: "116px" });
        const M = N.mascot({ left: "280px", top: "920px", width: "520px" });
        M.float(0, 11, 10);
        M.blink(1.4);
        N.out([chip, hk], 2.4, { y: -40 });
        const R = [["Tu rappelles ton vendeur<br>« la semaine prochaine ».", "wow", "shake"], ["Tu recopies le compromis<br>à la main.", "dizzy", "tilt"], ["5 avis Google<br>sans réponse.", "sad", ""], ["Tu bosses encore<br>le dimanche soir.", "angry", "shake"]];
        R.forEach((r, i) => {
          const t = 2.6 + i * 1.8;
          const c = N.cap(r[0], { top: "360px" }, t);
          M.expr(r[1], t + 0.55);
          if (r[2] === "shake") M.shake(t + 0.6, 0.4);
          if (r[2] === "tilt") { M.tilt(t + 0.6, 14); M.tilt(t + 1.5, 0, 0.2); }
          if (r[1] === "sad") K.sfx(t + 0.55, "bloop-down", 0.2);
          N.out(c, t + 1.65, { y: -10, d: 0.15 });
        });
        const b = N.say("Stop. <span class='v'>Laisse-moi faire.</span>", { left: "190px", top: "680px", width: "700px" }, 9.9, { cls: "" });
        M.expr("happy", 9.9, false);
        M.glow(10.0, 1.0);
        M.hop(10.1, 90);
        N.out(b, 11.4, { y: -10, d: 0.2 });
        window.__TE = 11.6;
        N.outro(11.6, "comment");
        endM(M, 280, 920, 520, 11.5);
""")

# ---------------------------------------------------------------- 5 · vrai ou faux
FILMS["mascotte-05-vrai-ou-faux"] = ("Vrai ou faux, spécial agents immo", 17.6, """
      .vf { display: flex; gap: 30px; justify-content: center; }
      .vf span { width: 300px; height: 110px; border-radius: 55px; background: #fff; box-shadow: 0 10px 30px rgba(27,31,75,.12); display: flex; align-items: center; justify-content: center;
        font-family: "Montserrat Hook", Montserrat, sans-serif; font-weight: 800; font-size: 44px; color: var(--navy); }
      .qc { padding: 40px 46px; font-size: 44px; line-height: 1.3; font-weight: 600; text-align: center; }
      .ex { padding: 30px 40px; font-size: 32px; line-height: 1.38; }
""", """
        const hk = N.hook(["VRAI", "OU <span class='hl'>FAUX ?</span>"], { top: "300px", fontSize: "140px" });
        const s1 = N.text("ctr n-body", "<b>Spécial agents immo. 2 questions.</b>", { top: "680px", fontSize: "44px" }, 0.8);
        const M = N.mascot({ left: "320px", top: "1120px", width: "440px" }, { expr: "think" });
        M.float(0, 14, 10);
        N.out([hk, s1], 2.3, { y: -40 });
        const Q = [
          ["Un DPE réalisé en 2019 est encore valable pour vendre.", 1, "Les DPE faits entre 2018 et mi-2021 ne sont <b>plus valables depuis le 1er janvier 2025</b>."],
          ["Si l’acquéreur paie les honoraires, le prix affiché doit les inclure.", 0, "Prix <b>honoraires inclus</b>, avec le taux d’honoraires TTC affiché à côté."],
        ];
        Q.forEach((q, i) => {
          const t = 2.5 + i * 5.2;
          const lab = N.chip(`QUESTION ${i + 1} / 2`, { top: "230px" }, t);
          const card = N.ab("n-card qc", q[0], { left: "90px", top: "330px", width: "900px" });
          N.hide(card);
          K.fin(card, t, { y: 30, d: 0.4 });
          const vf = N.ab("ctr vf", `<span>VRAI</span><span>FAUX</span>`, { top: "640px" });
          N.hide(vf);
          tl.set(vf, { opacity: 1 }, t + 0.4);
          K.pop(K.$$("span", vf), t + 0.4, { st: 0.1 });
          M.expr("think", t, false);
          [0, 1, 2].forEach((k) => { K.sfx(t + 1.0 + k * 0.5, "beep", 0.12, 0, { f: 880 }); M.blink(t + 1.0 + k * 0.5); });
          const good = K.$$("span", vf)[q[1]], bad = K.$$("span", vf)[1 - q[1]];
          tl.to(good, { backgroundColor: "#2cc4b5", color: "#ffffff", scale: 1.06, duration: 0.3 }, t + 2.5);
          tl.to(bad, { opacity: 0.45, duration: 0.3 }, t + 2.5);
          K.sfx(t + 2.5, "success", 0.26);
          M.expr("happy", t + 2.5, false);
          M.hop(t + 2.55, 70);
          const ex = N.ab("n-card ex", `<div style="display:flex;align-items:center;gap:14px;margin-bottom:10px"><img src="assets/img/limo-house-ad.png" alt="" style="width:48px;height:48px;object-fit:contain" /><b style="font-size:26px;color:#6b4fe0">LIMO t’explique</b></div>${q[2]}`, { left: "90px", top: "800px", width: "900px" });
          N.hide(ex);
          K.fin(ex, t + 2.9, { y: 20, d: 0.35 });
          K.sfx(t + 2.9, "chirp", 0.12);
          N.out([lab, card, vf, ex], t + 4.9, { y: -20, d: 0.25 });
        });
        const c = N.cap("T’as eu 2 / 2 ?<br>Dis-le en commentaire.", { top: "600px" }, 12.9, { dark: true });
        M.expr("wink", 12.9);
        N.out(c, 13.8, { y: -20 });
        window.__TE = 14.0;
        N.outro(14.0, "comment");
        endM(M, 320, 1120, 440, 13.9);
""")

# ---------------------------------------------------------------- 6 · pendant ton café
FILMS["mascotte-06-pendant-ton-cafe"] = ("Pendant ton café", 14.6, """
      #chrono { top: 250px; font-family: "Montserrat Hook", Montserrat, sans-serif; font-weight: 800; font-size: 96px; color: var(--vio); }
      #chrono span { position: absolute; left: 0; right: 0; }
""", """
        const hk = N.hook(["PENDANT", "TON CAFÉ<span class='v'>,</span>", "<span class='hl'>J’AI FAIT ÇA.</span>"], { top: "260px", fontSize: "100px" });
        const M = N.mascot({ left: "300px", top: "980px", width: "480px" }, { expr: "wink" });
        M.float(0, 10, 10);
        M.blink(1.6);
        N.out(hk, 2.4, { y: -40 });
        const ch = N.ab("ctr", Array.from({ length: 6 }, (_, k) => `<span>${k}:00</span>`).join(""), {});
        ch.id = "chrono";
        N.hide(ch);
        tl.set(ch, { opacity: 1 }, 2.6);
        const cs = K.$$("span", ch);
        cs.forEach((s, k) => { tl.set(s, { opacity: 0 }, 0); tl.set(s, { opacity: 1 }, 2.6 + k * 0.95); if (k < 5) tl.set(s, { opacity: 0 }, 2.6 + (k + 1) * 0.95); });
        const L = ["Brief du jour prêt", "Annonce Brive rédigée", "3 relances préparées", "Avis Google : réponse prête", "Avis de valeur Vignols", "Post LinkedIn publié"];
        const card = N.ab("n-card", L.map((l) => `<div class="n-row"><span style="color:#1c1c1e">${l}</span><i class="ok" style="margin-left:auto">${K.icon("check")}</i></div>`).join(""), { left: "110px", top: "400px", width: "860px" });
        N.hide(card);
        K.fin(card, 2.6, { y: 30, d: 0.4 });
        M.expr("open", 2.6, false);
        M.move(2.6, { y: 120, scale: 0.8 }, 0.5);
        M.glow(3.0, 4.6);
        K.$$(".n-row", card).forEach((r, i) => {
          const t = 3.1 + i * 0.8;
          tl.set(r, { opacity: 0.25 }, 0);
          tl.to(r, { opacity: 1, duration: 0.2 }, t);
          tl.fromTo(K.$(".ok", r), { scale: 0 }, { scale: 1, duration: 0.25, ease: "back.out(2.4)" }, t);
          K.sfx(t, "success", 0.12);
          if (i % 2) M.blink(t + 0.2);
        });
        N.out([card, ch], 8.3, { y: -30 });
        M.move(8.3, { y: 0, scale: 1 }, 0.5);
        const b = N.say("Il te reste<br>du café ?", { left: "240px", top: "700px", width: "600px" }, 8.7);
        M.expr("wink", 8.7, false);
        M.hop(8.8, 80);
        N.out(b, 10.6, { y: -10, d: 0.2 });
        window.__TE = 10.8;
        N.outro(10.8, "demo");
        endM(M, 300, 980, 480, 10.7);
""")

# ---------------------------------------------------------------- 7 · ne me dis pas
FILMS["mascotte-07-ne-me-dis-pas"] = ("Ne me dis pas que tu fais encore ça", 15.2, """
      .old { left: 140px; width: 800px; height: 300px; display: flex; align-items: center; justify-content: center; text-align: center; padding: 0 50px; font-size: 44px; line-height: 1.25; font-weight: 700; }
""", """
        const hk = N.hook(["NE ME DIS PAS", "QUE TU FAIS", "<span class='hl'>ENCORE ÇA…</span>"], { top: "260px", fontSize: "100px" });
        const M = N.mascot({ left: "300px", top: "980px", width: "480px" }, { expr: "sad" });
        M.float(0, 11, 10);
        N.out(hk, 2.5, { y: -40 });
        const O = [["Des post-it collés<br>partout sur l’écran.", "#ffe98a", "#5a4a00", "Rappels automatiques"], ["« contacts_2019_V3_final.xlsx »", "#e3f4e6", "#1d5a2c", "Fiches contacts à jour"], ["Le carnet de visites<br>griffonné.", "#f3ece2", "#5a4630", "Compte rendu de visite prêt"]];
        O.forEach((o, i) => {
          const t = 2.7 + i * 2.2;
          const c = N.ab("n-card old", o[0], { top: "380px", background: o[1], color: o[2], transform: `rotate(${i % 2 ? 2 : -2}deg)` });
          N.hide(c);
          tl.fromTo(c, { opacity: 0, y: -200, rotation: -8 }, { opacity: 1, y: 0, rotation: i % 2 ? 2 : -2, duration: 0.45, ease: "bounce.out" }, t);
          K.sfx(t + 0.2, "drop", 0.25);
          M.expr(i === 1 ? "dizzy" : "wow", t + 0.3);
          M.shake(t + 0.35, 0.3);
          M.expr("angry", t + 1.0, false);
          M.glow(t + 1.0, 0.6);
          K.sfx(t + 1.1, "scan", 0.16, 0, { d: 0.4 });
          tl.to(c, { scale: 0, rotation: 30, opacity: 0, duration: 0.3, ease: "back.in(2)" }, t + 1.2);
          const n = N.chip(`${K.icon("check")}${o[3]}`, { top: "500px" }, t + 1.5);
          n.querySelector("span").style.cssText = "height:88px;font-size:40px;padding:0 36px";
          M.expr("happy", t + 1.5, false);
          N.out(n, t + 2.1, { y: -10, d: 0.15 });
        });
        const b = N.say("Voilà. Bienvenue<br>au <span class='v'>XXIe siècle</span>.", { left: "190px", top: "700px", width: "700px" }, 9.5);
        M.expr("wink", 9.5, false);
        M.hop(9.6, 80);
        N.out(b, 11.2, { y: -10, d: 0.2 });
        window.__TE = 11.4;
        N.outro(11.4, "dm");
        endM(M, 300, 980, 480, 11.3);
""")

# ---------------------------------------------------------------- 8 · le duel
FILMS["mascotte-08-duel"] = ("Agent seul VS agent + LIMO", 15.4, """
      .col { width: 440px; top: 360px; }
      .col h4 { margin: 0 0 18px; font-family: "Montserrat Hook", Montserrat, sans-serif; font-weight: 800; font-size: 40px; text-align: center; }
      .tk { height: 130px; margin-bottom: 18px; padding: 20px 24px; }
      .tk b { display: flex; justify-content: space-between; font-size: 30px; font-weight: 700; color: #1c1c1e; }
      .tk b em { font-style: normal; }
      .tk .br { margin-top: 18px; height: 18px; border-radius: 9px; background: #efeff4; overflow: hidden; }
      .tk .br i { display: block; height: 100%; width: 100%; border-radius: 9px; transform-origin: 0 50%; }
      .tot { font-family: "Montserrat Hook", Montserrat, sans-serif; font-weight: 800; font-size: 64px; text-align: center; }
""", """
        const hk = N.hook(["AGENT SEUL", "<span class='v'>VS</span>", "<span class='hl'>AGENT + LIMO</span>"], { top: "320px", fontSize: "106px" });
        const M = N.mascot({ left: "350px", top: "1180px", width: "380px" }, { expr: "angry" });
        M.float(0, 12, 8);
        M.blink(1.5);
        N.out(hk, 2.3, { y: -40 });
        const T = [["Annonce", "45 min", "2 min"], ["Relances", "1 h", "5 min"], ["Compte rendu", "30 min", "1 min"], ["Avis Google", "20 min", "1 min"]];
        const col = (x, title, color, idx) => N.ab("col", `<h4 style="color:${color}">${title}</h4>` + T.map((r) => `<div class="n-card tk"><b>${r[0]}<em style="color:${color}">${r[idx]}</em></b><div class="br"><i style="background:${color}"></i></div></div>`).join(""), { left: x + "px" });
        const A = col(80, "SEUL", "#6e6e78", 1), B = col(560, "+ LIMO", "#6b4fe0", 2);
        [A, B].forEach((c) => { N.hide(c); K.fin(c, 2.5, { y: 30, d: 0.4 }); });
        K.sfx(2.6, "go", 0.2);
        M.expr("open", 2.6, false);
        K.$$(".br i", A).forEach((b, i) => tl.fromTo(b, { scaleX: 0 }, { scaleX: 1, duration: 5.5, ease: "none" }, 2.9 + i * 0.1));
        K.$$(".br i", B).forEach((b, i) => { tl.fromTo(b, { scaleX: 0 }, { scaleX: 1, duration: 0.5, ease: "power2.out" }, 2.9 + i * 0.6); K.sfx(3.4 + i * 0.6, "success", 0.12); });
        M.hop(5.4, 70);
        M.expr("heart", 5.4);
        const tA = N.ab("tot", `<span>0</span>`, { left: "80px", top: "1060px", width: "440px", color: "#6e6e78" });
        const tB = N.ab("tot", `<span>0</span>`, { left: "560px", top: "1060px", width: "440px", color: "#6b4fe0" });
        [tA, tB].forEach((x) => { N.hide(x); tl.set(x, { opacity: 1 }, 5.8); });
        K.count(K.$("span", tA), 155, 5.8, 1.2, (v) => { const m = Math.round(v); return Math.floor(m / 60) + " h " + String(m % 60).padStart(2, "0"); }, { ticks: 8 });
        K.count(K.$("span", tB), 9, 5.8, 1.2, (v) => Math.round(v) + " min", { ticks: 0 });
        K.sfx(7.1, "thump", 0.3);
        const fx = N.text("ctr n-body", "Temps indicatifs", { top: "1150px", fontSize: "24px" }, 6.0);
        N.out([A, B, tA, tB, fx], 9.2, { y: -30 });
        const c = N.cap("Tu choisis quelle équipe ?", { top: "700px" }, 9.5, { dark: true });
        M.expr("wink", 9.5);
        N.out(c, 11.4, { y: -20 });
        window.__TE = 11.6;
        N.outro(11.6, "essai");
        endM(M, 350, 1180, 380, 11.5);
""")

# ---------------------------------------------------------------- 9 · POV : un agent m'installe
FILMS["mascotte-09-pov-installation"] = ("POV : un agent immo m’installe", 14.8, """
      .big { font-family: "Montserrat Hook", Montserrat, sans-serif; font-weight: 800; font-size: 150px; color: var(--navy); line-height: 1; }
""", """
        const hk = N.hook(["POV :", "UN AGENT IMMO", "<span class='hl'>M’INSTALLE.</span>"], { top: "260px", fontSize: "100px" });
        const M = N.mascot({ left: "300px", top: "980px", width: "480px" });
        M.float(0, 11, 10);
        M.wave(0.4);
        N.out(hk, 2.4, { y: -40 });
        const b1 = N.say("Montre-moi<br>tes contacts.", { left: "240px", top: "680px", width: "600px" }, 2.6);
        M.expr("open", 2.6, false);
        N.out(b1, 3.8, { y: -10, d: 0.15 });
        const big = N.ab("ctr big", `<span>0</span><div class="n-body" style="font-size:40px;margin-top:10px"><b>contacts</b> dont 37 à relancer</div>`, { top: "330px" });
        N.hide(big);
        tl.set(big, { opacity: 1 }, 3.9);
        K.count(K.$("span", big), 842, 3.9, 1.0, (v) => String(Math.round(v)), { ticks: 12 });
        M.expr("wow", 4.9);
        M.shake(4.9, 0.3);
        const b2 = N.say("Ok. Je m’occupe<br>des <span class='v'>37 relances</span>.", { left: "240px", top: "680px", width: "600px" }, 5.5);
        M.expr("angry", 5.5, false);
        M.glow(5.6, 1.0);
        N.out([big, b2], 7.0, { y: -10, d: 0.2 });
        const b3 = N.say("Et tes annonces…<br>on va les <span class='v'>réécrire</span>.", { left: "240px", top: "680px", width: "600px" }, 7.2);
        M.expr("dizzy", 7.3, false);
        M.tilt(7.4, -12);
        M.tilt(8.4, 0, 0.2);
        N.out(b3, 8.6, { y: -10, d: 0.15 });
        const b4 = N.say("Terminé. Tu fais quoi<br>de ton <span class='v'>après-midi</span> ?", { left: "190px", top: "680px", width: "700px" }, 8.8);
        M.expr("wink", 8.8, false);
        M.hop(8.9, 90);
        N.out(b4, 10.8, { y: -10, d: 0.2 });
        window.__TE = 11.0;
        N.outro(11.0, "dm");
        endM(M, 300, 980, 480, 10.9);
""")

# ---------------------------------------------------------------- 10 · mieux que ton stagiaire
FILMS["mascotte-10-mieux-que-ton-stagiaire"] = ("3 trucs que je fais mieux que ton stagiaire", 15.4, """
      .num { font-family: "Montserrat Hook", Montserrat, sans-serif; font-weight: 800; font-size: 200px; color: var(--vio); line-height: 1; }
""", """
        const hk = N.hook(["3 TRUCS QUE JE", "FAIS MIEUX QUE", "<span class='hl'>TON STAGIAIRE.</span>"], { top: "280px", fontSize: "92px" });
        const M = N.mascot({ left: "300px", top: "980px", width: "480px" }, { expr: "wink" });
        M.float(0, 12, 10);
        M.blink(1.7);
        N.out(hk, 2.4, { y: -40 });
        const R = [["3", "Je ne dors jamais.", "sleep", "open"], ["2", "Je n’oublie aucune relance.", "think", "happy"], ["1", "Je ne demande pas<br>d’augmentation.", "euro", "wink"]];
        R.forEach((r, i) => {
          const t = 2.6 + i * 2.2;
          const n = N.ab("ctr num", r[0], { top: "250px" });
          N.hide(n);
          tl.fromTo(n, { opacity: 0, scale: 1.6 }, { opacity: 1, scale: 1, duration: 0.3, ease: "back.out(2)" }, t);
          K.sfx(t, "slam", 0.22);
          const c = N.ab("ctr n-head", r[1], { top: "500px", fontSize: "62px" });
          N.hide(c);
          K.fin(c, t + 0.2, { y: 20, d: 0.35 });
          M.expr(r[2], t + 0.2);
          M.expr(r[3], t + 1.2, false);
          M.hop(t + 1.2, 50);
          N.out([n, c], t + 2.0, { y: -20, d: 0.2 });
        });
        const b = N.say("Mais garde-le :<br>il fait très bien le café.", { left: "190px", top: "680px", width: "700px" }, 9.4);
        M.expr("wink", 9.4, false);
        M.hop(9.5, 90);
        N.out(b, 11.4, { y: -10, d: 0.2 });
        window.__TE = 11.6;
        N.outro(11.6, "demo");
        endM(M, 300, 980, 480, 11.5);
""")

if __name__ == "__main__":
    for name, (title, dur, css, body) in FILMS.items():
        html = SHELL.format(title=title, faces=FACES, css=css.strip("\n"), body=(END + body).strip("\n"), dur=dur, name=name)
        pathlib.Path(f"reels/{name}.html").write_text(html, encoding="utf-8")
        print("reels/" + name + ".html")
