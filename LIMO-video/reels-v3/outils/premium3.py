"""Films premium sur les voix ElevenLabs v4 (sources/voix/v4/) : kit assets/kit/fx.js (karaoké mot à mot,
titres lettre par lettre, whip pan, verre dépoli, aurore) + plans étalonnés (assets/video/*-grade.mp4).
P2 Les 3 erreurs (Marie) · P3 Dimanche soir (Lucie) · P4 Le calcul (Paul) · P5 Une journée avec Limo (Lucie).
Temps des phrases : transcription locale de chaque voix (Whisper small) ; données affichées = exemples fictifs.

Usage : python3 outils/premium3.py   (réécrit reels/prem-0[2-5]-*.html et complète outils/voix.json)
"""
import json
import pathlib

from cine import COMMON, FACES, GLASS
from lifestyle import V
from premium2 import SHELL

O = 0.3  # décalage de la voix dans chaque film
VOICE = {
    "prem-02-trois-erreurs": [["v4/Marie_-07h34-cut.mp3", O]],
    "prem-03-dimanche-soir": [["v4/Lucie_-07h35.mp3", O]],
    "prem-04-le-calcul": [["v4/Paul_K_-07h36-cut.mp3", O]],
    "prem-05-une-journee": [["v4/Lucie_-07h40.mp3", O]],
}
PRE, FILMS = {}, {}

CSS = GLASS + """
      .note { position: absolute; padding: 22px 26px 26px; width: 330px; background: #ffe98a; color: #3b3000; font-family: Caveat, cursive; font-weight: 700; font-size: 46px; line-height: 1.05; box-shadow: 0 18px 40px rgba(0,0,0,.45); }
      .note::before { content: ""; position: absolute; left: 50%; top: -14px; width: 90px; height: 28px; margin-left: -45px; background: rgba(255,255,255,.55); transform: rotate(-3deg); }
"""

# outils communs à tous les films premium
SH = r"""
        tl.set([K.$(".n-bg", root), ...K.$$(".n-arc", root)], { opacity: 0 }, 0);
        C.bars(0.5, true, 1.0);
        const LIGHT = "linear-gradient(180deg, #f5f3fe 0%, #ece7fb 100%)";
        const O = 0.3;
        const shade = (p) => FX.ab(p, { inset: "0", background: "linear-gradient(180deg, rgba(5,6,15,.62) 0%, rgba(5,6,15,.05) 36%, rgba(5,6,15,.08) 62%, rgba(5,6,15,.72) 100%)" });
        const num = (p, txt, t, css = {}) => {
          const e = FX.ab(p, Object.assign({ left: "56px", top: "110px", fontFamily: "Montserrat, sans-serif", fontWeight: "800", fontSize: "200px", lineHeight: "1", color: "rgba(255,255,255,.1)", WebkitTextStroke: "3px rgba(255,255,255,.5)" }, css), txt);
          tl.set(e, { opacity: 0 }, 0);
          tl.fromTo(e, { opacity: 0, x: -90 }, { opacity: 1, x: 0, duration: 0.8, ease: "expo.out" }, t);
          return e;
        };
        const chip = (p, html, css, t, o = {}) => {
          const g = FX.glass(p, Object.assign({ padding: "18px 28px", borderRadius: "28px", fontFamily: "Montserrat, sans-serif", fontWeight: "700", fontSize: "34px", whiteSpace: "nowrap", display: "flex", alignItems: "center", gap: "16px" }, css), html);
          K.$$("svg.i", g).forEach((s) => (s.style.cssText = "width:38px;height:38px;color:#fff;flex:none"));
          tl.set(g, { opacity: 0 }, 0);
          tl.fromTo(g, { opacity: 0, scale: 0.7, y: 30 }, { opacity: 1, scale: 1, y: 0, duration: 0.45, ease: "back.out(1.7)" }, t);
          if (o.snd !== false) K.sfx(t, o.snd || "pop", o.g ?? 0.14, 0, { f: 900 });
          return g;
        };
        const card = (p, ic, big, small, css, t, o = {}) => {
          const g = FX.glass(p, Object.assign({ left: "90px", width: "900px", display: "flex", alignItems: "center", gap: "22px" }, css),
            `<span style="flex:none;width:80px;height:80px;border-radius:22px;background:${o.bg || "rgba(44,196,181,.38)"};display:flex;align-items:center;justify-content:center">${K.icon(ic)}</span><span style="min-width:0"><b style="display:block;font-family:Montserrat,sans-serif;font-weight:800;font-size:38px;line-height:1.12">${big}</b><span style="font-size:27px;color:rgba(255,255,255,.88)">${small}</span></span>${o.check ? `<span class="ok" style="margin-left:auto;flex:none;width:58px;height:58px;border-radius:50%;background:#2cc4b5;display:flex;align-items:center;justify-content:center">${K.icon("check")}</span>` : ""}`);
          K.$$("svg.i", g).forEach((s) => (s.style.cssText = "width:42px;height:42px;color:#fff"));
          tl.set(g, { opacity: 0 }, 0);
          tl.fromTo(g, { opacity: 0, y: 70, scale: 0.94, filter: "blur(8px)" }, { opacity: 1, y: 0, scale: 1, filter: "blur(0px)", duration: 0.6, ease: "expo.out" }, t);
          FX.sheen(g, t + 0.3);
          K.sfx(t, o.snd || "pop", o.g ?? 0.16, 0, { f: 900 });
          if (o.check) {
            const ok = K.$(".ok", g);
            tl.set(ok, { scale: 0 }, 0);
            tl.to(ok, { scale: 1, duration: 0.35, ease: "back.out(2.4)" }, t + 0.45);
            K.sfx(t + 0.45, "success", 0.2);
          }
          return g;
        };
        const tag = (p, txt, t, sub = "") => {
          const g = FX.glass(p, { left: "0", right: "0", margin: "0 auto", width: "430px", top: "110px", padding: "16px 26px", borderRadius: "999px", display: "flex", alignItems: "center", justifyContent: "center", gap: "16px", fontFamily: "Montserrat, sans-serif", fontWeight: "800", fontSize: "54px" },
            `${K.icon("clock")}<span>${txt}</span>${sub ? `<small style="font-size:26px;font-weight:600;opacity:.75">${sub}</small>` : ""}`);
          K.$$("svg.i", g).forEach((s) => (s.style.cssText = "width:46px;height:46px;color:#2cc4b5"));
          tl.set(g, { opacity: 0 }, 0);
          tl.fromTo(g, { opacity: 0, y: -40 }, { opacity: 1, y: 0, duration: 0.5, ease: "expo.out" }, t);
          K.sfx(t, "tick", 0.2, 0, { f: 1800 });
          return g;
        };
        const kar = (segs) => FX.karaoke(segs.map((s) => [s[0] + O, s[1] + O, s[2]]), { keys: ["limo", "mandats", "tard", "tête", "pleine", "terrain", "trois", "dimanches", "secret", "calcul", "deux", "temps", "clients", "estimation"] });
        const phoneIn = (p, css, html, t, o = {}) => {
          const ph = A.phone(css, { time: o.time || "8:00" });
          p.appendChild(ph.wrap);
          const pg = A.page(ph, html);
          A.enter(ph, t, { flatAt: 0.7 });
          return { ph, pg };
        };
        const outro = (t) => {
          FX.layer(t - 0.25, null, { background: LIGHT }, "", true);
          C.flash(t - 0.25, "#ffffff", 0.95);
          C.leak(t - 0.2, 2.4);
          window.__TE = t;
          N.outro(t, "essai");
          const m = N.mascot({ left: "440px", top: "1500px", width: "190px" });
          m.enter(t + 1.4);
          m.wave(t + 2.1);
        };
"""

# ---------------------------------------------------------------- P2 · Les 3 erreurs (Marie, 36,5 s)
PRE["prem-02-trois-erreurs"] = V("v1", "vendeuse-canape-grade", 6.65, 5.0, 1)
FILMS["prem-02-trois-erreurs"] = ("LIMO, les 3 erreurs", 39.6, SH + r"""
        // A · accroche
        const sA = FX.layer(0, 6.9);
        FX.aurora(sA, 0, 7);
        num(sA, "3", 1.6, { left: "0", right: "0", textAlign: "center", top: "520px", fontSize: "700px", WebkitTextStroke: "4px rgba(255,255,255,.18)" });
        FX.rise(sA, "CONSEILLER IMMO…", { top: "300px", fontSize: "62px" }, 0.25, { color: "#d9ceff" });
        FX.rise(sA, "3 [erreurs]|qui te font perdre|des [mandats].", { top: "720px", fontSize: "100px" }, 1.85, { accent: "#ff8f8f" });
        C.leak(0.3, 2.4);
        // B · erreur 1 (plan de la vendeuse, puis le panneau d'une autre agence)
        const v1 = document.getElementById("v1");
        const sB = FX.layer(6.65, 11.75);
        shade(sB);
        FX.whip(sA, [v1, sB], 6.5);
        tl.fromTo(v1, { scale: 1.0 }, { scale: 1.08, duration: 5, ease: "none" }, 6.65);
        num(sB, "01", 6.9);
        const b1 = FX.rise(sB, "Super [estimation]…", { top: "430px", fontSize: "84px", textShadow: "0 6px 30px rgba(0,0,0,.45)" }, 7.95, { snd: false });
        FX.fall(b1, 10.6);
        FX.rise(sB, "…et tu rappelles|[trop] [tard].", { top: "430px", fontSize: "92px", textShadow: "0 6px 30px rgba(0,0,0,.45)" }, 10.85, { accent: "#ff8f8f" });
        card(sB, "phone", "Rappeler Mme Roy", "Estimation lundi · aucun rappel depuis 12 jours", { top: "1080px" }, 11.0, { bg: "rgba(217,58,63,.55)", snd: "buzz" });
        const sB2 = FX.layer(11.75, 15.0);
        const ph1 = FX.ab(sB2, { left: "-60px", top: "-100px", width: "1200px", height: "2120px" }, `<img src="assets/img/bien-pierre-balcon.jpg" alt="" style="width:100%;height:100%;object-fit:cover" />`);
        tl.fromTo(ph1, { scale: 1.12 }, { scale: 1.0, duration: 3.4, ease: "power1.out" }, 11.75);
        shade(sB2);
        num(sB2, "01", 11.75);
        FX.rise(sB2, "Le vendeur, lui,|n’a pas [attendu].", { top: "430px", fontSize: "88px", textShadow: "0 6px 30px rgba(0,0,0,.45)" }, 12.45, { accent: "#ff8f8f", snd: false });
        const stamp = FX.ab(sB2, { left: "150px", top: "1000px", padding: "18px 34px", border: "8px solid #ff5b5b", borderRadius: "18px", color: "#ff5b5b", fontFamily: "Montserrat, sans-serif", fontWeight: "800", fontSize: "56px", textAlign: "center", lineHeight: "1.1", background: "rgba(10,5,10,.35)" }, "SIGNÉ AVEC UNE<br>AUTRE AGENCE");
        tl.set(stamp, { opacity: 0 }, 0);
        tl.fromTo(stamp, { opacity: 0, scale: 2.2, rotation: -14 }, { opacity: 1, scale: 1, rotation: -7, duration: 0.28, ease: "power4.in" }, 13.4);
        K.sfx(13.68, "slam", 0.35);
        // C · erreur 2 : la tête pleine
        const sC = FX.layer(14.85, 20.95);
        FX.aurora(sC, 14.8, 21, { colors: ["#6b4fe0", "#d93a7a", "#3a2a9a"] });
        FX.whip(sB2, sC, 14.7);
        num(sC, "02", 14.95);
        FX.rise(sC, "Tes relances sont|dans ta [tête].", { top: "390px", fontSize: "88px" }, 16.25, { snd: false });
        const T = [["Rappeler M. Vidal", 120, 640, -4], ["Famille Durand ?", 560, 700, 3], ["Compromis Roche", 90, 820, 2], ["Mme Roy !!", 600, 880, -3], ["Diags manquants", 160, 1000, -2], ["Visite 10 h 30", 590, 1060, 4], ["Notaire : pièces ?", 110, 1180, 3], ["Acquéreurs mas", 560, 1240, -4], ["Avis Google", 330, 940, -1]];
        const cs = T.map((c, i) => {
          const g = chip(sC, c[0], { left: c[1] + "px", top: c[2] + "px", fontSize: "30px" }, 16.7 + i * 0.2, { g: 0.1 });
          tl.set(g, { rotation: c[3] }, 16.7 + i * 0.2 + 0.45);
          return g;
        });
        // « déjà pleine » : tout tremble puis explose dans le flou
        tl.to(cs, { x: "+=10", duration: 0.05, yoyo: true, repeat: 9, ease: "none" }, 19.0);
        tl.to(cs, { scale: 1.3, opacity: 0, filter: "blur(16px)", duration: 0.45, ease: "power2.in", stagger: 0.02 }, 20.25);
        K.sfx(19.0, "buzz", 0.22);
        // D · erreur 3 : les soirées
        const sD = FX.layer(20.95, 26.4);
        FX.aurora(sD, 20.9, 26.5, { colors: ["#1d3a8a", "#6b4fe0", "#0f6d7a"] });
        FX.whip(sC, sD, 20.8);
        num(sD, "03", 21.05);
        const clk = FX.glass(sD, { left: "0", right: "0", margin: "0 auto", width: "620px", top: "640px", padding: "30px 0", textAlign: "center", fontFamily: "Montserrat, sans-serif", fontWeight: "800", fontSize: "170px", lineHeight: "1", borderRadius: "44px" }, `<span class="hh">19:30</span><small style="display:block;font-size:30px;font-weight:600;margin-top:12px;opacity:.75">lundi soir</small>`);
        tl.set(clk, { opacity: 0 }, 0);
        tl.fromTo(clk, { opacity: 0, scale: 0.85 }, { opacity: 1, scale: 1, duration: 0.5, ease: "expo.out" }, 21.2);
        K.count(K.$(".hh", clk), 22 * 60 + 47, 21.6, 2.6, (v) => { const m = Math.round(v); return String(Math.floor(m / 60)).padStart(2, "0") + ":" + String(m % 60).padStart(2, "0"); }, { from: 19 * 60 + 30, ticks: 12 });
        FX.rise(sD, "Tes soirées sur|l’[administratif].", { top: "360px", fontSize: "84px" }, 22.25, { snd: false });
        [["file", "Compte rendu de visite", 1000, 23.2], ["pen", "Annonce à rédiger", 1110, 23.7], ["mail", "12 relances à écrire", 1220, 24.2]].forEach((d) => chip(sD, `${K.icon(d[0])}${d[1]}`, { left: "0", right: "0", margin: "0 auto", width: "fit-content", top: d[2] + "px" }, d[3]));
        // E · la solution
        const sE = FX.layer(26.1, 31.9);
        FX.aurora(sE, 26.1, 32, { colors: ["#2cc4b5", "#6b4fe0", "#1d6f8a"] });
        tl.set(sE, { clipPath: "circle(0px at 540px 960px)" }, 0);
        C.iris(sE, 26.1, 0.8);
        FX.rise(sE, "Limo [corrige]|[les] [trois].", { top: "200px", fontSize: "100px" }, 26.25, { snd: false });
        card(sE, "phone", "01 · Rappel au bon moment", "Il te dit qui rappeler, et quand", { top: "500px" }, 26.9, { check: true });
        card(sE, "refresh", "02 · Relances suivies", "Plus rien dans ta tête", { top: "660px" }, 27.5, { check: true });
        card(sE, "zap", "03 · Admin préparé", "Tes soirées te reviennent", { top: "820px" }, 28.1, { check: true });
        const msg = FX.glass(sE, { left: "90px", width: "900px", top: "1000px", padding: "24px 28px" },
          `<span style="display:block;font-size:24px;letter-spacing:.06em;color:rgba(255,255,255,.75)">LIMO · MESSAGE PRÊT POUR MME ROY</span><span style="display:block;margin-top:10px;font-size:31px;line-height:1.35">« Bonjour Madame Roy, suite à notre estimation de lundi, avez-vous pu y réfléchir ? »</span><span class="snd" style="display:inline-block;margin-top:16px;padding:12px 28px;border-radius:999px;background:#6b4fe0;font-family:Montserrat,sans-serif;font-weight:800;font-size:28px">Envoyer</span>`);
        tl.set(msg, { opacity: 0 }, 0);
        tl.fromTo(msg, { opacity: 0, y: 60 }, { opacity: 1, y: 0, duration: 0.55, ease: "expo.out" }, 29.85);
        tl.to(K.$(".snd", msg), { scale: 0.9, duration: 0.08, yoyo: true, repeat: 1 }, 31.0);
        K.sfx(31.0, "send", 0.3);
        outro(31.9);
        kar([
          [0.0, 1.2, "Conseiller immo…"], [1.56, 4.05, "voici trois erreurs qui te font perdre des mandats."], [4.51, 5.95, "Sans que tu t’en rendes compte."],
          [6.34, 7.26, "Erreur numéro un :"], [7.69, 9.51, "tu fais une super estimation…"], [10.56, 11.68, "et tu rappelles trop tard."], [12.14, 14.3, "Le vendeur, lui, n’a pas attendu."],
          [14.58, 15.53, "Erreur numéro deux :"], [16.01, 17.57, "tes relances sont dans ta tête."], [17.88, 20.1, "Et ta tête… elle est déjà pleine."],
          [20.5, 21.55, "Erreur numéro trois :"], [21.95, 25.37, "tu passes tes soirées sur l’administratif, au lieu d’être sur le terrain."],
          [25.81, 27.13, "Limo corrige les trois."], [27.51, 29.3, "Il te dit qui relancer, quand,"], [29.58, 30.92, "et prépare le message pour toi."],
        ]);
""")

# ---------------------------------------------------------------- P3 · Dimanche soir (Lucie, 18,4 s)
PRE["prem-03-dimanche-soir"] = V("v1", "villa-recul-lent-grade", 7.25, 3.9, 1, 1.0) + V("v2", "femme-vent-grade", 15.05, 2.4, 2, 3.0)
FILMS["prem-03-dimanche-soir"] = ("LIMO, dimanche soir", 23.4, SH + r"""
        // A · dimanche 22 h, les post-it
        const sA = FX.layer(0, 7.4);
        FX.aurora(sA, 0, 7.5, { colors: ["#1d2a7a", "#4b2a9a", "#0f3d6a"], a: 0.5 });
        FX.rise(sA, "DIMANCHE", { top: "250px", fontSize: "60px", letterSpacing: ".18em" }, 0.2, { color: "#d9ceff" });
        const clk = FX.glass(sA, { left: "0", right: "0", margin: "0 auto", width: "600px", top: "360px", padding: "26px 0", textAlign: "center", fontFamily: "Montserrat, sans-serif", fontWeight: "800", fontSize: "180px", lineHeight: "1", borderRadius: "44px" }, "22:00");
        tl.set(clk, { opacity: 0 }, 0);
        tl.fromTo(clk, { opacity: 0, scale: 0.8, filter: "blur(10px)" }, { opacity: 1, scale: 1, filter: "blur(0px)", duration: 0.7, ease: "expo.out" }, 0.5);
        K.sfx(0.5, "tick", 0.25, 0, { f: 1500 });
        const NOTES = [["Rappeler Mme Martin ??", 70, 700, -6], ["Relancer qui déjà ?", 640, 680, 5], ["Durand → mardi ?", 110, 960, 4], ["Notaire !!!", 680, 950, -4], ["Visite Vignols ?", 380, 1150, -2]];
        NOTES.forEach((n, i) => {
          const e = FX.ab(sA, { left: n[1] + "px", top: n[2] + "px" }, `<div class="note">${n[0]}</div>`);
          tl.set(e, { opacity: 0 }, 0);
          tl.fromTo(e, { opacity: 0, scale: 1.5, rotation: n[3] * 3 }, { opacity: 1, scale: 1, rotation: n[3], duration: 0.35, ease: "power3.out" }, 3.6 + i * 0.55);
          K.sfx(3.6 + i * 0.55 + 0.2, "thump", 0.12);
        });
        // B · le collègue devant un film (plan du salon, feu de cheminée)
        const v1 = document.getElementById("v1");
        const sB = FX.layer(7.25, 11.3);
        shade(sB);
        FX.whip(sA, [v1, sB], 7.1);
        tl.fromTo(v1, { scale: 1.05 }, { scale: 1.12, duration: 4, ease: "none" }, 7.25);
        const b1 = FX.rise(sB, "Ton collègue ?", { top: "330px", fontSize: "96px", textShadow: "0 6px 30px rgba(0,0,0,.5)" }, 7.35, { snd: false });
        FX.fall(b1, 8.25);
        const b2 = FX.rise(sB, "Il regarde|un [film].", { top: "330px", fontSize: "110px", textShadow: "0 6px 30px rgba(0,0,0,.5)" }, 8.4, { snd: false });
        FX.fall(b2, 9.8);
        FX.rise(sB, "Son [secret] ?", { top: "380px", fontSize: "116px", textShadow: "0 6px 30px rgba(0,0,0,.5)" }, 9.95, { snd: false });
        // C · Limo prépare sa semaine
        const sC = FX.layer(11.3, 15.2);
        FX.aurora(sC, 11.2, 15.3, { colors: ["#2cc4b5", "#6b4fe0", "#1d6f8a"] });
        FX.whip(sB, sC, 11.0);
        FX.rise(sC, "Limo prépare|sa [semaine].", { top: "170px", fontSize: "90px" }, 11.2, { snd: false });
        const P = phoneIn(sC, { left: "290px", top: "430px", width: "500px" }, A.HD + `<div class="a-hello"><span>Bonjour Julien,</span><br>Ta semaine est prête.</div>` +
          A.row("phone", "r", "Mme Martin", "Rappel prioritaire", "lun.", `<span class="a-tag t">Priorité</span>`) + A.row("refresh", "v", "12 relances", "Messages prêts", "lun.") +
          A.row("home", "t", "4 visites", "Confirmées", "mar.") + A.row("file", "v", "3 dossiers", "Pièces complètes", "mer."), 11.15, { time: "22:01" });
        K.$$(".a-row", P.pg).forEach((r, i) => { tl.set(r, { opacity: 0 }, 0); tl.fromTo(r, { opacity: 0, x: 60 }, { opacity: 1, x: 0, duration: 0.4, ease: "expo.out" }, 11.9 + i * 0.6); K.sfx(11.9 + i * 0.6, "pop", 0.12, 0, { f: 1000 }); });
        // D · reprends tes dimanches
        const v2 = document.getElementById("v2");
        const sD = FX.layer(15.05, 17.5);
        shade(sD);
        FX.whip(sC, [v2, sD], 14.9);
        FX.rise(sD, "Reprends tes|[dimanches].", { top: "380px", fontSize: "110px", textShadow: "0 6px 30px rgba(0,0,0,.5)" }, 15.2, { snd: false });
        outro(17.4);
        kar([
          [0.0, 2.12, "Dimanche, vingt-deux heures…"], [3.25, 6.53, "Toi, tu ressors tes notes pour savoir qui tu devais rappeler cette semaine."],
          [6.99, 7.69, "Ton collègue, lui ?"], [8.06, 9.5, "Il regarde un film."], [9.6, 10.54, "Son secret ?"],
          [10.86, 14.4, "Limo prépare sa semaine : les relances, les rendez-vous, les dossiers."], [14.8, 16.47, "Toi aussi, reprends tes dimanches."],
        ]);
""")

# ---------------------------------------------------------------- P4 · Le calcul (Paul, 24,2 s)
PRE["prem-04-le-calcul"] = V("v1", "agent-voiture-grade", 14.85, 5.0, 1)
FILMS["prem-04-le-calcul"] = ("LIMO, le calcul", 27.6, SH + r"""
        // A · le calcul
        const sA = FX.layer(0, 7.2);
        FX.aurora(sA, 0, 7.3);
        const a1 = FX.rise(sA, "Fais le [calcul].", { top: "260px", fontSize: "100px" }, 0.2);
        const box = FX.glass(sA, { left: "0", right: "0", margin: "0 auto", width: "820px", top: "560px", padding: "40px 0 34px", textAlign: "center", borderRadius: "48px" },
          `<b class="big" style="display:block;font-family:Montserrat,sans-serif;font-weight:800;font-size:200px;line-height:1">1 h</b><span class="lab" style="display:block;margin-top:14px;font-family:Montserrat,sans-serif;font-weight:700;font-size:44px;color:#2cc4b5">par jour</span>`);
        tl.set(box, { opacity: 0 }, 0);
        tl.fromTo(box, { opacity: 0, scale: 0.85 }, { opacity: 1, scale: 1, duration: 0.55, ease: "expo.out" }, 1.45);
        K.sfx(1.45, "pop", 0.2);
        K.count(K.$(".big", box), 220, 4.0, 1.4, (v) => Math.round(v) + " h", { from: 1, ticks: 14 });
        tl.set(K.$(".lab", box), { textContent: "par an" }, 4.0);
        const note = FX.ab(sA, { left: "0", right: "0", top: "980px", textAlign: "center", fontFamily: "Inter, sans-serif", fontSize: "30px", color: "rgba(255,255,255,.7)" }, "1 h × 220 jours travaillés");
        tl.set(note, { opacity: 0 }, 0);
        tl.to(note, { opacity: 1, duration: 0.4 }, 4.6);
        tl.to(box, { scale: 1.08, duration: 0.15, yoyo: true, repeat: 1, ease: "power2.out" }, 6.0);
        K.sfx(6.0, "slam", 0.28);
        // B · des dizaines de rendez-vous
        const sB = FX.layer(7.2, 10.3);
        FX.aurora(sB, 7.1, 10.4, { colors: ["#6b4fe0", "#2cc4b5", "#3a2a9a"] });
        FX.whip(sA, sB, 7.05);
        FX.rise(sB, "= des dizaines de|[RDV] [vendeurs].", { top: "230px", fontSize: "84px" }, 7.3, { snd: false });
        for (let i = 0; i < 30; i++) {
          const c = FX.glass(sB, { left: 95 + (i % 5) * 182 + "px", top: 560 + Math.floor(i / 5) * 118 + "px", width: "160px", height: "100px", padding: "0", borderRadius: "20px", display: "flex", alignItems: "center", justifyContent: "center" },
            `<span style="font-family:Montserrat,sans-serif;font-weight:800;font-size:26px;color:#fff">RDV</span>`);
          tl.set(c, { opacity: 0 }, 0);
          tl.fromTo(c, { opacity: 0, scale: 0.4, background: "rgba(107,79,224,.0)" }, { opacity: 1, scale: 1, background: "rgba(107,79,224,.55)", duration: 0.3, ease: "back.out(2)" }, 7.6 + i * 0.065);
        }
        K.sfx(7.6, "riser", 0.12, 0, { d: 1.9 });
        // C · Limo s'occupe du reste
        const sC = FX.layer(10.3, 15.0);
        FX.aurora(sC, 10.2, 15.1, { colors: ["#2cc4b5", "#6b4fe0", "#1d6f8a"] });
        FX.whip(sB, sC, 10.1);
        FX.rise(sC, "Limo s’occupe|du [reste].", { top: "200px", fontSize: "100px" }, 10.3, { snd: false });
        card(sC, "refresh", "Les relances", "Messages prêts à envoyer", { top: "540px" }, 11.0, { check: true });
        card(sC, "note", "Les comptes rendus", "Dictés, rédigés, classés", { top: "700px" }, 11.75, { check: true });
        card(sC, "pen", "Les annonces", "Rédigées en 2 minutes", { top: "860px" }, 12.85, { check: true });
        card(sC, "file", "Le suivi des dossiers", "Jusqu’au notaire", { top: "1020px" }, 13.75, { check: true });
        // D · sur le terrain
        const v1 = document.getElementById("v1");
        const sD = FX.layer(14.85, 19.85);
        shade(sD);
        FX.whip(sC, [v1, sD], 14.7);
        tl.fromTo(v1, { scale: 1.0 }, { scale: 1.08, duration: 5, ease: "none" }, 14.85);
        const d1 = FX.rise(sD, "Toi, tu récupères|ton [temps]…", { top: "300px", fontSize: "92px", textShadow: "0 6px 30px rgba(0,0,0,.5)" }, 14.95, { snd: false });
        FX.fall(d1, 16.5);
        FX.rise(sD, "…et tu le passes|sur le [terrain].", { top: "300px", fontSize: "92px", textShadow: "0 6px 30px rgba(0,0,0,.5)" }, 16.65, { snd: false });
        outro(19.75);
        const price = FX.ab(root, { left: "0", right: "0", top: "1400px", textAlign: "center", zIndex: 30 }, `<span style="display:inline-block;padding:14px 30px;border-radius:999px;background:#1b1f4b;color:#fff;font-family:Montserrat,sans-serif;font-weight:800;font-size:36px">Dès 49 €/mois</span>`);
        tl.set(price, { opacity: 0 }, 0);
        tl.fromTo(price, { opacity: 0, scale: 0.7 }, { opacity: 1, scale: 1, duration: 0.4, ease: "back.out(2)" }, 20.0);
        kar([
          [0.0, 0.85, "Fais le calcul."], [1.24, 2.98, "Une heure d’administratif par jour…"], [3.66, 5.37, "c’est plus de deux cents heures par an."],
          [5.69, 6.74, "Deux cents heures."], [7.09, 9.7, "C’est des dizaines de rendez-vous vendeurs que tu ne fais pas."],
          [9.91, 14.25, "Limo s’occupe des relances, des comptes rendus, des annonces et du suivi des dossiers."],
          [14.6, 16.06, "Toi, tu récupères ton temps…"], [16.36, 18.81, "et tu le passes là où ça rapporte : sur le terrain."],
        ]);
""")

# ---------------------------------------------------------------- P5 · Une journée avec Limo (Lucie, 30,6 s)
PRE["prem-05-une-journee"] = (V("v1", "agent-voiture-grade", 7.95, 5.0, 1) + V("v2", "vendeuse-canape-grade", 24.0, 2.8, 2, 1.5))
FILMS["prem-05-une-journee"] = ("LIMO, une journée", 34.3, SH + r"""
        // A · 8 h : les priorités du jour
        const sA = FX.layer(0, 8.1);
        FX.aurora(sA, 0, 8.2, { colors: ["#f3a35b", "#6b4fe0", "#2cc4b5"], a: 0.45 });
        tag(sA, "08:00", 0.25);
        const P = phoneIn(sA, { left: "280px", top: "300px", width: "520px" }, A.HD + `<div class="a-hello"><span>Bonjour Julien,</span><br>Voici tes priorités du jour.</div>` +
          A.row("phone", "r", "Rappeler Mme Martin", "Estimation lundi", "09:00", `<span class="a-tag t">Priorité</span>`) + A.row("refresh", "v", "Relancer 12 contacts", "Messages prêts", "09:30") + A.row("home", "t", "2 visites", "Vignols · Allassac", "11:00"), 1.1);
        K.$$(".a-row", P.pg).forEach((r, i) => { const t = [4.1, 5.2, 6.6][i]; tl.fromTo(r, { boxShadow: "0 0 0 0 rgba(107,79,224,0)" }, { boxShadow: "0 0 0 6px rgba(107,79,224,.55)", duration: 0.3, yoyo: true, repeat: 1 }, t); });
        // B · 10 h : dictée dans la voiture → fiche
        const v1 = document.getElementById("v1");
        const sB = FX.layer(7.95, 14.4);
        const bB = FX.aurora(sB, 7.9, 14.5, { colors: ["#2cc4b5", "#6b4fe0", "#1d6f8a"] });
        tl.set(bB, { opacity: 0 }, 0);
        tl.to(bB, { opacity: 1, duration: 0.4 }, 12.75);
        shade(sB);
        FX.whip(sA, [v1, sB], 7.8);
        tl.fromTo(v1, { scale: 1.0 }, { scale: 1.08, duration: 5, ease: "none" }, 7.95);
        tag(sB, "10:00", 8.0);
        const mic = FX.glass(sB, { left: "90px", width: "900px", top: "1020px", display: "flex", alignItems: "center", gap: "24px" },
          `<span style="flex:none;width:84px;height:84px;border-radius:50%;background:#d93a3f;display:flex;align-items:center;justify-content:center">${K.icon("mic")}</span><span style="flex:1"><b style="display:block;font-family:Montserrat,sans-serif;font-weight:800;font-size:34px">Dictée en cours…</b><span class="wv" style="display:flex;gap:6px;align-items:center;height:44px;margin-top:8px">${Array.from({ length: 26 }, () => `<i style="display:block;width:8px;height:12px;border-radius:4px;background:#2cc4b5"></i>`).join("")}</span></span>`);
        K.$$("svg.i", mic).forEach((s) => (s.style.cssText = "width:44px;height:44px;color:#fff"));
        tl.set(mic, { opacity: 0 }, 0);
        tl.fromTo(mic, { opacity: 0, y: 60 }, { opacity: 1, y: 0, duration: 0.5, ease: "expo.out" }, 10.2);
        K.$$(".wv i", mic).forEach((b, i) => { for (let k = 0; k < 9; k++) tl.to(b, { height: 10 + ((i * 7 + k * 13) % 34), duration: 0.18, ease: "sine.inOut" }, 10.4 + k * 0.2); });
        tl.to(mic, { opacity: 0, y: -30, duration: 0.3 }, 12.25);
        card(sB, "note", "Fiche créée", "Estimation Mme Roy · compte rendu classé", { top: "1020px" }, 12.35, { check: true });
        // C · 14 h : nouveau mandat → annonce
        const sC = FX.layer(14.4, 19.35);
        const pc = FX.ab(sC, { left: "-60px", top: "-100px", width: "1200px", height: "2120px" }, `<img src="assets/img/bien-chalet.jpg" alt="" style="width:100%;height:100%;object-fit:cover" />`);
        tl.fromTo(pc, { scale: 1.15 }, { scale: 1.02, duration: 5, ease: "power1.out" }, 14.4);
        shade(sC);
        FX.whip(sB, sC, 14.2);
        tag(sC, "14:00", 14.45);
        card(sC, "pin", "Nouveau mandat", "Chalet · 4 chambres · exemple", { top: "560px" }, 15.2, { snd: "notif" });
        const ann = FX.glass(sC, { left: "90px", width: "900px", top: "760px", padding: "28px 30px" },
          `<span style="display:block;font-size:24px;letter-spacing:.06em;color:rgba(255,255,255,.75)">LIMO · ANNONCE</span><b style="display:block;margin-top:8px;font-family:Montserrat,sans-serif;font-weight:800;font-size:40px;line-height:1.15">Chalet de charme, vue dégagée sur les sommets</b><span class="ty" style="display:block;margin-top:12px;font-size:28px;line-height:1.4;color:rgba(255,255,255,.9);min-height:120px"></span><span class="pub" style="display:inline-flex;align-items:center;gap:10px;margin-top:10px;padding:12px 26px;border-radius:999px;background:#2cc4b5;font-family:Montserrat,sans-serif;font-weight:800;font-size:28px">Prête à publier ✓</span>`);
        tl.set(ann, { opacity: 0 }, 0);
        tl.fromTo(ann, { opacity: 0, y: 60 }, { opacity: 1, y: 0, duration: 0.55, ease: "expo.out" }, 16.2);
        K.type(K.$(".ty", ann), "Au calme, à deux pas des pistes : 4 chambres, poêle à bois, grande terrasse plein sud…", 16.5, 1.9, 0.03);
        const pub = K.$(".pub", ann);
        tl.set(pub, { opacity: 0 }, 0);
        tl.fromTo(pub, { opacity: 0, scale: 0.6 }, { opacity: 1, scale: 1, duration: 0.35, ease: "back.out(2.2)" }, 18.5);
        K.sfx(18.5, "success", 0.24);
        // D · 18 h : tout est relancé
        const sD = FX.layer(19.35, 24.15);
        FX.aurora(sD, 19.3, 24.2, { colors: ["#f36b5b", "#6b4fe0", "#1d3a8a"], a: 0.45 });
        FX.whip(sC, sD, 19.15);
        tag(sD, "18:00", 19.4);
        card(sD, "shield", "Diagnostiqueur relancé", "DPE et amiante demandés", { top: "560px" }, 20.4, { check: true, snd: "notif" });
        card(sD, "file", "Notaire : pièces reçues", "Dossier complet", { top: "730px" }, 21.9, { check: true, snd: "notif" });
        // E · et toi ? avec tes clients
        const v2 = document.getElementById("v2");
        const sE = FX.layer(24.0, 26.75);
        shade(sE);
        FX.whip(sD, [v2, sE], 23.85);
        const e1 = FX.rise(sE, "Et toi ?", { top: "360px", fontSize: "120px", textShadow: "0 6px 30px rgba(0,0,0,.5)" }, 24.0, { snd: false });
        FX.fall(e1, 24.65);
        FX.rise(sE, "Ta journée,|avec tes [clients].", { top: "360px", fontSize: "96px", textShadow: "0 6px 30px rgba(0,0,0,.5)" }, 24.75, { snd: false });
        outro(26.7);
        kar([
          [0.0, 0.69, "Huit heures."], [1.0, 3.46, "Tu ouvres Limo : tes priorités du jour sont prêtes."], [3.77, 7.19, "Mme Martin à rappeler, douze contacts à relancer, deux visites."],
          [7.62, 8.21, "Dix heures."], [8.52, 9.61, "Tu sors d’une estimation."], [9.98, 11.77, "Tu dictes ton compte rendu dans la voiture…"], [12.03, 13.75, "et Limo rédige la fiche."],
          [13.99, 14.62, "Quatorze heures."], [14.93, 15.55, "Un nouveau mandat ?"], [15.96, 18.7, "L’annonce est rédigée en deux minutes, prête à publier."],
          [18.91, 19.64, "Dix-huit heures."], [19.94, 23.11, "Le diagnostiqueur a été relancé, le notaire a reçu les pièces."],
          [23.71, 24.15, "Et toi ?"], [24.44, 26.02, "Tu as passé ta journée avec tes clients."],
        ]);
""")

if __name__ == "__main__":
    for name, (title, dur, body) in FILMS.items():
        html = SHELL.format(title=title, faces=FACES, css=CSS.strip("\n"), body=(COMMON + body).strip("\n"), dur=dur, name=name)
        html = html.replace('      <section id="s-main"', PRE[name] + '      <section id="s-main"', 1)
        pathlib.Path(f"reels/{name}.html").write_text(html, encoding="utf-8")
        print("reels/" + name + ".html")
    vj = pathlib.Path("outils/voix.json")
    data = json.loads(vj.read_text()) if vj.exists() else {}
    data.update(VOICE)
    vj.write_text(json.dumps(data, indent=1), encoding="utf-8")
