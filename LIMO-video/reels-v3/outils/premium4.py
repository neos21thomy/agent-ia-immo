"""Films longs « l'assistant complet » sur les voix ElevenLabs v4 (sources/voix/longs/) :
L2 Imagine (Lucie) · L3 Un CRM qui travaille (Yariq) · L4 Une semaine avec ton bras droit (Camille) ·
L5 Tu peux tout lui dire (Yariq) · L6 Par des agents immobiliers, pour des agents immobiliers (Yariq).
Kit assets/kit/fx.js + outils communs de premium3 ; écrans animés par fonction (anniversaire, boîte mail,
frais kilométriques, publication, commandes vocales…). Données affichées = exemples fictifs.

Usage : python3 outils/premium4.py   (réécrit reels/long-*.html et complète outils/voix.json)
"""
import json
import pathlib

from cine import COMMON, FACES
from lifestyle import V
from premium2 import SHELL
from premium3 import CSS, SH

O = 0.3
VOICE = {
    "long-02-imagine": [["longs/Lucie-17h06.mp3", O]],
    "long-03-crm-qui-travaille": [["longs/Yariq-17h09.mp3", O]],
    "long-04-une-semaine": [["longs/Camille-17h11.mp3", O]],
    "long-05-tout-lui-dire": [["longs/Yariq-17h13b.mp3", O]],
    "long-06-par-des-agents": [["longs/Yariq-17h13c.mp3", O]],
}
PRE, FILMS = {}, {}

# écrans « fonctions » réutilisables
SH4 = SH + r"""
        const KEYS = ["limo", "tout", "jamais", "rien", "anniversaire", "anniversaires", "mails", "kilométriques", "relance", "relances", "oubli", "travaille", "métier", "collègue", "agit", "terrain", "clients", "vocal"];
        const kar2 = (segs) => FX.karaoke(segs.map((s) => [s[0] + O, s[1] + O, s[2]]), { keys: KEYS });
        const lay = (t0, t1, prev, o = {}) => {
          const l = FX.layer(t0, t1);
          if (o.colors !== false) FX.aurora(l, t0 - 0.1, t1 + 0.1, o.colors ? { colors: o.colors, a: o.a } : {});
          if (prev) FX.whip(prev, l, t0 - 0.15);
          return l;
        };
        const foot = (id, t0, t1, prev) => {
          const v = document.getElementById(id);
          const l = FX.layer(t0, t1);
          shade(l);
          if (prev) FX.whip(prev, [v, l], t0 - 0.15);
          tl.fromTo(v, { scale: 1.0 }, { scale: 1.08, duration: t1 - t0, ease: "none" }, t0);
          return l;
        };
        const web = (p, items, t) => {
          const c = FX.glass(p, { left: "390px", top: "760px", width: "300px", height: "300px", borderRadius: "50%", padding: "0", display: "flex", alignItems: "center", justifyContent: "center" }, `<img src="assets/img/limo-house-ad.png" alt="" style="width:130px;height:130px;background:#fff;border-radius:34px;padding:16px" />`);
          tl.set(c, { opacity: 0 }, 0);
          tl.fromTo(c, { opacity: 0, scale: 0.6 }, { opacity: 1, scale: 1, duration: 0.6, ease: "back.out(1.6)" }, t);
          const P = [[80, 470], [600, 520], [50, 1150], [610, 1120], [30, 830], [720, 840]];
          const els = [c];
          items.forEach((it, i) => {
            const g = chip(p, `${K.icon(it[0])}${it[1]}`, { left: P[i % 6][0] + "px", top: P[i % 6][1] + "px" }, it[2]);
            tl.to(g, { y: "-=16", duration: 1.5, ease: "sine.inOut", yoyo: true, repeat: 1 }, it[2] + 0.5);
            els.push(g);
          });
          return els;
        };
        const msgCard = (p, label, txt, btn, css, t) => {
          const m = FX.glass(p, Object.assign({ left: "90px", width: "900px", padding: "24px 28px" }, css),
            `<span style="display:block;font-size:24px;letter-spacing:.06em;color:rgba(255,255,255,.75)">${label}</span><span style="display:block;margin-top:10px;font-size:31px;line-height:1.35">${txt}</span>${btn ? `<span class="snd" style="display:inline-block;margin-top:16px;padding:12px 28px;border-radius:999px;background:#6b4fe0;font-family:Montserrat,sans-serif;font-weight:800;font-size:28px">${btn}</span>` : ""}`);
          tl.set(m, { opacity: 0 }, 0);
          tl.fromTo(m, { opacity: 0, y: 50 }, { opacity: 1, y: 0, duration: 0.5, ease: "expo.out" }, t);
          FX.sheen(m, t + 0.3);
          return m;
        };
        const tapSend = (m, t) => { tl.to(K.$(".snd", m), { scale: 0.88, duration: 0.08, yoyo: true, repeat: 1 }, t); tl.set(K.$(".snd", m), { textContent: "Envoyé ✓", background: "#2cc4b5" }, t + 0.18); K.sfx(t, "send", 0.3); };
        const bday = (p, name, t, top = 520) => [
          card(p, "cake", `Anniversaire · ${name}`, "Aujourd’hui · client fidèle", { top: top + "px" }, t, { bg: "rgba(255,143,143,.5)", snd: "notif" }),
          msgCard(p, "LIMO · MESSAGE PRÊT", `« Joyeux anniversaire ${name} ! Je vous souhaite une très belle journée. »`, "Envoyer", { top: top + 170 + "px" }, t + 0.8),
        ];
        const inbox = (p, t, top = 480) => {
          const R = [["Newsletter d’un portail", 0], ["Mme Roy · question sur le compromis", 1], ["Offre partenaire", 0], ["Me Faure · pièces du dossier", 1], ["Publicité logiciel", 0]];
          const box = FX.glass(p, { left: "90px", width: "900px", top: top + "px", padding: "22px 26px" },
            `<span style="display:block;font-size:24px;letter-spacing:.06em;color:rgba(255,255,255,.75);margin-bottom:8px">BOÎTE MAIL · TRIÉE PAR LIMO</span>` +
            R.map((r) => `<div class="mr ${r[1] ? "imp" : "pro"}" style="display:flex;align-items:center;gap:16px;padding:13px 0;border-top:1px solid rgba(255,255,255,.15);font-size:28px">${K.icon("mail")}<span style="flex:1;white-space:nowrap;overflow:hidden">${r[0]}</span><span class="tg" style="flex:none;padding:6px 16px;border-radius:999px;font-size:21px;font-weight:700;background:${r[1] ? "#2cc4b5" : "rgba(255,255,255,.18)"}">${r[1] ? "Réponse prête" : "Archivé"}</span></div>`).join(""));
          K.$$("svg.i", box).forEach((s) => (s.style.cssText = "width:30px;height:30px;color:#fff;flex:none"));
          tl.set(box, { opacity: 0 }, 0);
          tl.fromTo(box, { opacity: 0, y: 60 }, { opacity: 1, y: 0, duration: 0.5, ease: "expo.out" }, t);
          K.$$(".tg", box).forEach((g) => { tl.set(g, { opacity: 0 }, 0); tl.to(g, { opacity: 1, duration: 0.2 }, t + 0.8); });
          K.$$(".mr.pro", box).forEach((r, i) => { tl.to(r, { opacity: 0.35, x: 30, duration: 0.35, ease: "power2.in" }, t + 1.0 + i * 0.25); K.sfx(t + 1.0 + i * 0.25, "swipe", 0.1); });
          return box;
        };
        const km = (p, t, top = 600) => {
          const g = FX.glass(p, { left: "0", right: "0", margin: "0 auto", width: "780px", height: "380px", boxSizing: "border-box", top: top + "px", padding: "28px 0 0", textAlign: "center", borderRadius: "44px" },
            `<span style="display:inline-flex;align-items:center;gap:14px;font-family:Montserrat,sans-serif;font-weight:700;font-size:32px;color:#2cc4b5">${K.icon("car")}Frais kilométriques · octobre</span><b class="kv" style="display:block;width:100%;text-align:center;margin-top:10px;font-family:Montserrat,sans-serif;font-weight:800;font-size:110px;line-height:1.05;white-space:nowrap">0 km</b><span class="ok" style="position:absolute;left:0;right:0;bottom:30px;margin:0 auto;width:fit-content;padding:10px 26px;border-radius:999px;background:#2cc4b5;font-family:Montserrat,sans-serif;font-weight:800;font-size:28px">Calculé automatiquement</span>`);
          K.$$("svg.i", g).forEach((s) => (s.style.cssText = "width:40px;height:40px;color:#2cc4b5"));
          tl.set(g, { opacity: 0 }, 0);
          tl.fromTo(g, { opacity: 0, scale: 0.85 }, { opacity: 1, scale: 1, duration: 0.5, ease: "expo.out" }, t);
          K.count(K.$(".kv", g), 1248, t + 0.3, 1.5, (v) => { const n = Math.round(v); return (n >= 1000 ? Math.floor(n / 1000) + " " + String(n % 1000).padStart(3, "0") : n) + " km"; }, { ticks: 12 });
          const ok = K.$(".ok", g);
          tl.set(ok, { opacity: 0 }, 0);
          tl.fromTo(ok, { opacity: 0, scale: 0.6 }, { opacity: 1, scale: 1, duration: 0.35, ease: "back.out(2.2)" }, t + 1.9);
          K.sfx(t + 1.9, "success", 0.22);
          return g;
        };
        const post = (p, t, top = 420) => {
          const g = FX.glass(p, { left: "215px", width: "650px", top: top + "px", padding: "20px" },
            `<div style="display:flex;align-items:center;gap:14px;margin-bottom:14px"><img src="assets/img/limo-house-ad.png" alt="" style="width:56px;height:56px;border-radius:50%;background:#fff;padding:6px" /><b style="font-size:28px">ton.agence.immo</b></div><div style="height:430px;border-radius:18px;overflow:hidden"><img src="assets/img/bien-terrasse-mer.jpg" alt="" style="width:100%;height:100%;object-fit:cover" /></div><div style="margin-top:14px;font-size:27px;line-height:1.35">Nouveau mandat : villa vue mer, 4 chambres. Visites dès samedi.</div><span class="pr" style="display:inline-block;margin-top:12px;padding:10px 24px;border-radius:999px;background:#2cc4b5;font-family:Montserrat,sans-serif;font-weight:800;font-size:26px">Publication prête</span>`);
          tl.set(g, { opacity: 0 }, 0);
          tl.fromTo(g, { opacity: 0, y: 60, scale: 0.94 }, { opacity: 1, y: 0, scale: 1, duration: 0.55, ease: "expo.out" }, t);
          const pr = K.$(".pr", g);
          tl.set(pr, { opacity: 0 }, 0);
          tl.fromTo(pr, { opacity: 0, scale: 0.6 }, { opacity: 1, scale: 1, duration: 0.35, ease: "back.out(2.2)" }, t + 1.0);
          K.sfx(t + 1.0, "success", 0.2);
          return g;
        };
        const ask = (p, q, r, t, tr, top = 520) => {
          const qb = FX.ab(p, { right: "90px", width: "760px", top: top + "px", padding: "22px 28px", borderRadius: "34px 34px 8px 34px", background: "#6b4fe0", color: "#fff", fontFamily: "Inter, sans-serif", fontSize: "34px", lineHeight: "1.32", boxShadow: "0 20px 50px rgba(0,0,0,.3)" }, `<span style="display:inline-flex;align-items:center;gap:10px;font-size:22px;opacity:.85;margin-bottom:6px">${K.icon("mic")}Message vocal</span><br>${q}`);
          K.$$("svg.i", qb).forEach((s) => (s.style.cssText = "width:26px;height:26px;color:#fff"));
          tl.set(qb, { opacity: 0 }, 0);
          tl.fromTo(qb, { opacity: 0, y: 30, scale: 0.94 }, { opacity: 1, y: 0, scale: 1, duration: 0.35, ease: "back.out(1.8)" }, t);
          K.sfx(t, "send", 0.24);
          const rb = FX.glass(p, { left: "90px", width: "760px", top: top + 200 + "px", padding: "22px 28px", borderRadius: "34px 34px 34px 8px", fontSize: "33px", lineHeight: "1.32" }, `<span style="display:inline-flex;align-items:center;gap:10px;font-size:22px;color:#2cc4b5;font-weight:700;margin-bottom:6px">${K.icon("check")}Limo</span><br>${r}`);
          K.$$("svg.i", rb).forEach((s) => (s.style.cssText = "width:26px;height:26px;color:#2cc4b5"));
          tl.set(rb, { opacity: 0 }, 0);
          tl.fromTo(rb, { opacity: 0, y: 30, scale: 0.94 }, { opacity: 1, y: 0, scale: 1, duration: 0.35, ease: "back.out(1.8)" }, tr);
          K.sfx(tr, "receive", 0.24);
          return [qb, rb];
        };
        const logoCard = (p, t, top = 760) => {
          const g = FX.ab(p, { left: "240px", top: top + "px", width: "600px", padding: "40px 0", borderRadius: "44px", background: "#ffffff", boxShadow: "0 30px 80px rgba(0,0,0,.45)", textAlign: "center" }, `<img src="assets/img/limo-logo-ad.png" alt="LIMO" style="width:440px" />`);
          tl.set(g, { opacity: 0 }, 0);
          tl.fromTo(g, { opacity: 0, scale: 1.3, filter: "blur(14px)" }, { opacity: 1, scale: 1, filter: "blur(0px)", duration: 0.7, ease: "power3.out" }, t);
          K.sfx(t + 0.1, "thump", 0.4);
          C.sweep(g, t + 0.7, 0.9);
          return g;
        };
"""

# ---------------------------------------------------------------- L2 · Imagine (Lucie, 45,3 s)
PRE["long-02-imagine"] = V("v1", "vendeuse-canape-grade", 13.6, 5.0, 1) + V("v2", "agent-voiture-grade", 24.4, 4.4, 2)
FILMS["long-02-imagine"] = ("LIMO, imagine", 46.5, SH4 + r"""
        const sA = lay(0, 3.1);
        FX.rise(sA, "Imagine un assistant|qui n’oublie|[jamais] [rien].", { top: "560px", fontSize: "100px" }, 0.3);
        C.leak(0.3, 2.4);
        const sB = lay(3.1, 9.2, sA, { colors: ["#2cc4b5", "#6b4fe0", "#1d6f8a"] });
        FX.rise(sB, "Tous tes biens|par [cœur].", { top: "170px", fontSize: "90px" }, 3.3, { snd: false });
        web(sB, [["home", "Chaque mandat", 6.4], ["users", "Chaque vendeur", 7.1], ["target", "Chaque acquéreur", 7.9], ["msg", "Chaque demande", 8.7]], 4.2);
        const sC = lay(9.2, 13.75, sB, { colors: ["#f3a35b", "#6b4fe0", "#2cc4b5"], a: 0.45 });
        FX.rise(sC, "Chaque [matin].", { top: "160px", fontSize: "90px" }, 9.3, { snd: false });
        const P = phoneIn(sC, { left: "300px", top: "330px", width: "480px" }, A.HD + `<div class="a-hello"><span>Bonjour Julien,</span><br>Voici qui rappeler.</div>` +
          A.row("phone", "r", "Mme Martin", "Estimation lundi", "09:00", `<span class="a-tag t">Priorité</span>`) + A.row("phone", "v", "M. Vidal", "Visite samedi", "09:30") + A.row("refresh", "t", "12 relances", "Messages prêts", "10:00"), 9.3);
        tl.to(P.ph.wrap, { opacity: 0.3, duration: 0.3 }, 11.8);
        msgCard(sC, "LIMO · MESSAGE PRÊT POUR MME MARTIN", "« Bonjour Madame Martin, suite à notre estimation de lundi, avez-vous pu y réfléchir ? »", "Envoyer", { top: "1010px" }, 12.0);
        const sD = foot("v1", 13.75, 18.75, sC);
        FX.rise(sD, "Son [anniversaire]…", { top: "230px", fontSize: "86px", textShadow: "0 6px 30px rgba(0,0,0,.5)" }, 13.9, { snd: false });
        const bd = bday(sD, "Mme Martin", 14.5, 560);
        tapSend(bd[1], 17.8);
        const sE = lay(18.75, 24.55, sD, { colors: ["#6b4fe0", "#2cc4b5", "#3a2a9a"] });
        FX.rise(sE, "Mails, annonces,|[réseaux] [sociaux].", { top: "150px", fontSize: "80px" }, 19.2, { snd: false });
        const ib = inbox(sE, 19.4, 400);
        tl.to(ib, { opacity: 0, y: -40, duration: 0.3 }, 21.9);
        post(sE, 22.1, 400);
        const sF = foot("v2", 24.55, 28.95, sE);
        FX.rise(sF, "Pendant ton [rendez-vous]…", { top: "230px", fontSize: "76px", textShadow: "0 6px 30px rgba(0,0,0,.5)" }, 24.7, { snd: false });
        km(sF, 25.4, 620);
        const sG = lay(28.95, 34.95, sF, { colors: ["#2cc4b5", "#6b4fe0", "#1d6f8a"] });
        FX.rise(sG, "Tu peux [tout]|lui dire.", { top: "160px", fontSize: "90px" }, 29.1, { snd: false });
        ask(sG, "« Limo, rappelle-moi de relancer M. Vidal jeudi. »", "C’est noté : relance jeudi à 9 h.", 30.0, 31.0, 470);
        ask(sG, "« Limo, qui cherche un T3 à Brive ? »", "3 acquéreurs correspondent.", 32.2, 33.3, 900);
        const sH = lay(34.95, 38.75, sG, { colors: ["#3a2a9a", "#6b4fe0", "#0f3d6a"] });
        const h1 = FX.rise(sH, "Cet assistant|[existe].", { top: "520px", fontSize: "110px" }, 35.0);
        FX.fall(h1, 36.8);
        FX.rise(sH, "Il s’appelle", { top: "560px", fontSize: "70px" }, 36.95, { snd: false, color: "#d9ceff" });
        logoCard(sH, 37.05, 700);
        outro(38.7);
        kar2([
          [0, 2.43, "Imagine un assistant qui n’oublie jamais rien."],
          [2.78, 8.66, "Un assistant qui connaît tous tes biens par cœur. Chaque mandat, chaque vendeur, chaque acquéreur, chaque demande."],
          [8.88, 11.33, "Un assistant qui te dit chaque matin qui rappeler…"], [11.78, 13.05, "et qui prépare le message pour toi."],
          [13.34, 18.54, "Un assistant qui pense à l’anniversaire de Mme Martin… alors que toi, tu l’avais complètement oublié."],
          [18.94, 23.93, "Un assistant qui trie tes mails, qui écrit tes annonces, qui prépare tes publications pour les réseaux sociaux."],
          [24.26, 28.34, "Un assistant qui calcule tes frais kilométriques, pendant que toi, tu es en rendez-vous."],
          [28.77, 30.88, "Un assistant à qui tu peux tout dire."], [31.33, 34.04, "En vocal, depuis ta voiture, entre deux visites."],
          [34.7, 36.36, "Cet assistant… il existe."], [36.7, 37.86, "Il s’appelle Limo."],
        ]);
""")

# ---------------------------------------------------------------- L3 · Un CRM qui travaille (Yariq, 55,4 s)
PRE["long-03-crm-qui-travaille"] = ""
FILMS["long-03-crm-qui-travaille"] = ("LIMO, un CRM qui travaille", 56.4, SH4 + r"""
        const sA = lay(0, 11.2, null, { colors: ["#3a3d55", "#2a2c40", "#1a1c2a"], a: 0.6 });
        FX.rise(sA, "Ton [CRM],|il fait quoi ?", { top: "220px", fontSize: "100px" }, 0.3, { accent: "#ff8f8f" });
        const old = FX.ab(sA, { left: "90px", width: "900px", top: "560px", padding: "20px 26px", borderRadius: "24px", background: "rgba(255,255,255,.07)", border: "1px solid rgba(255,255,255,.15)", fontFamily: "Inter, sans-serif", color: "rgba(255,255,255,.75)" },
          `<div style="display:flex;font-size:22px;letter-spacing:.06em;padding-bottom:10px;opacity:.7"><span style="flex:1">NOM</span><span style="width:260px">TÉLÉPHONE</span><span style="width:200px">DERNIÈRE ACTION</span></div>` +
          [["Dupont", "06 12 •• •• ••", "il y a 8 mois"], ["Martin", "06 45 •• •• ••", "il y a 1 an"], ["Durand", "07 81 •• •• ••", "jamais"], ["Roy", "06 03 •• •• ••", "il y a 5 mois"], ["Vidal", "06 77 •• •• ••", "il y a 2 ans"], ["Faure", "07 22 •• •• ••", "jamais"]]
            .map((r) => `<div class="or" style="display:flex;font-size:30px;padding:14px 0;border-top:1px solid rgba(255,255,255,.1)"><span style="flex:1">${r[0]}</span><span style="width:260px">${r[1]}</span><span style="width:200px;color:#ff8f8f">${r[2]}</span></div>`).join(""));
        K.$$(".or", old).forEach((r, i) => { tl.set(r, { opacity: 0 }, 0); tl.to(r, { opacity: 1, duration: 0.2 }, 3.8 + i * 0.25); K.sfx(3.8 + i * 0.25, "tick", 0.08, 0, { f: 900 }); });
        tl.set(old, { opacity: 0 }, 0); tl.to(old, { opacity: 1, duration: 0.3 }, 3.6);
        tl.to(old, { filter: "grayscale(1) blur(2px)", opacity: 0.45, duration: 1.2 }, 7.6);
        FX.rise(sA, "Il [attend].", { top: "1180px", fontSize: "90px" }, 9.1, { accent: "#ff8f8f", snd: false });
        const sB = lay(11.2, 22.55, sA, { colors: ["#2cc4b5", "#6b4fe0", "#1d6f8a"] });
        FX.rise(sB, "Limo, un CRM|qui [travaille].", { top: "170px", fontSize: "96px" }, 11.3);
        web(sB, [["home", "Mandats", 15.6], ["users", "Vendeurs", 16.4], ["target", "Acquéreurs", 17.2], ["search", "Critères", 18.3], ["msg", "Demandes", 19.3], ["cake", "Dates importantes", 20.4]], 14.6);
        const sC = lay(22.55, 31.55, sB, { colors: ["#6b4fe0", "#2cc4b5", "#3a2a9a"] });
        FX.rise(sC, "Et il [agit].", { top: "170px", fontSize: "110px" }, 22.6);
        card(sC, "refresh", "Relances au bon moment", "Il te dit qui, et quand", { top: "430px" }, 23.6, { check: true });
        card(sC, "send", "Messages préparés", "Tu relis, tu envoies", { top: "590px" }, 25.6, { check: true });
        card(sC, "cake", "Anniversaires souhaités", "Tes clients s’en souviennent", { top: "750px" }, 27.2, { check: true, bg: "rgba(255,143,143,.5)" });
        card(sC, "msg", "Aucune demande sans réponse", "Chaque message suivi", { top: "910px" }, 28.8, { check: true });
        const sD = FX.layer(31.55, 38.95);
        const ph = FX.ab(sD, { left: "-60px", top: "-100px", width: "1200px", height: "2120px" }, `<img src="assets/img/bien-pierre-balcon.jpg" alt="" style="width:100%;height:100%;object-fit:cover" />`);
        tl.fromTo(ph, { scale: 1.12 }, { scale: 1.0, duration: 7.4, ease: "power1.out" }, 31.55);
        shade(sD);
        FX.whip(sC, sD, 31.4);
        card(sD, "users", "Nouvel acquéreur", "Maison 3 chambres · Brive · exemple", { top: "430px" }, 31.9, { snd: "notif" });
        chip(sD, `${K.icon("bell")}Limo s’en souvient`, { left: "0", right: "0", margin: "0 auto", width: "fit-content", top: "620px" }, 34.5);
        card(sD, "target", "Bien correspondant trouvé !", "Maison 3 ch. · Brive · à proposer", { top: "760px" }, 36.2, { check: true, snd: "success" });
        const sE = lay(38.95, 45.4, sD, { colors: ["#2cc4b5", "#6b4fe0", "#1d6f8a"] });
        card(sE, "mail", "Mails inutiles triés", "Les importants, réponse prête", { top: "330px" }, 39.2, { check: true });
        card(sE, "camera", "Réseaux sociaux", "Publications préparées", { top: "490px" }, 41.2, { check: true });
        km(sE, 42.9, 680);
        const sF = lay(45.4, 51.8, sE, { colors: ["#3a2a9a", "#6b4fe0", "#0f3d6a"] });
        const f1 = FX.rise(sF, "Plus un logiciel|que tu [remplis].", { top: "560px", fontSize: "96px" }, 46.55, { accent: "#ff8f8f" });
        FX.fall(f1, 48.6);
        FX.rise(sF, "Un assistant|qui [travaille]|[pour] [toi].", { top: "520px", fontSize: "104px" }, 48.8, { snd: false });
        outro(51.7);
        kar2([
          [0, 2.65, "Ton CRM, aujourd’hui… il fait quoi ?"], [3.38, 7.44, "Il stocke. Des noms, des numéros, des fiches que tu ne rouvres jamais."], [8.76, 10.16, "Il attend que tu fasses tout."],
          [10.91, 14.05, "Limo, c’est l’inverse. C’est un CRM qui travaille."],
          [14.3, 21.81, "Il retient tout : tes mandats, tes vendeurs, tes acquéreurs, leurs critères, leurs demandes, leurs dates importantes. Et surtout…"],
          [22.31, 22.79, "il agit."], [23.32, 25.07, "Il te rappelle les relances au bon moment."], [25.28, 28.11, "Il prépare les messages. Il souhaite les anniversaires."], [28.32, 30.47, "Il ne laisse aucune demande sans réponse."],
          [31.3, 33.62, "Un nouvel acquéreur cherche une maison avec trois chambres à Brive ?"], [34.23, 35.11, "Limo s’en souvient."], [35.62, 38.24, "Et le jour où le bon bien arrive… il te le dit."],
          [38.87, 40.43, "Les mails inutiles, il les trie."], [40.87, 42.35, "Les réseaux sociaux, il t’aide."], [42.6, 44.74, "Les frais kilométriques, il les calcule."],
          [46.29, 47.97, "Ce n’est plus un logiciel que tu remplis."], [48.51, 50.53, "C’est un assistant qui travaille pour toi."],
        ]);
""")

# ---------------------------------------------------------------- L4 · Une semaine avec ton bras droit (Camille, 58,3 s)
PRE["long-04-une-semaine"] = (V("v1", "agent-voiture-grade", 7.75, 5.0, 1) + V("v2", "villa-recul-lent-grade", 26.75, 9.6, 2)
                              + V("v3", "vendeuse-canape-grade", 45.6, 5.0, 3))
FILMS["long-04-une-semaine"] = ("LIMO, une semaine", 59.2, SH4 + r"""
        const sA = lay(0, 7.9, null, { colors: ["#f3a35b", "#6b4fe0", "#2cc4b5"], a: 0.45 });
        tag(sA, "LUNDI", 0.3);
        const P = phoneIn(sA, { left: "290px", top: "300px", width: "500px" }, A.HD + `<div class="a-hello"><span>Bonjour Julien,</span><br>Ta semaine est prête.</div>` +
          A.row("refresh", "r", "Vendeurs à relancer", "4 messages prêts", "lun.") + A.row("home", "t", "Visites", "3 confirmées", "mar.") + A.row("file", "v", "Compromis en cours", "2 dossiers", "jeu."), 1.4);
        K.$$(".a-row", P.pg).forEach((r, i) => tl.fromTo(r, { boxShadow: "0 0 0 0 rgba(107,79,224,0)" }, { boxShadow: "0 0 0 6px rgba(107,79,224,.55)", duration: 0.3, yoyo: true, repeat: 1 }, [4.0, 5.2, 6.3][i]));
        const sB = foot("v1", 7.75, 18.05, sA);
        const bB = FX.aurora(sB, 7.7, 18.2, { colors: ["#2cc4b5", "#6b4fe0", "#1d6f8a"] });
        tl.set(bB, { opacity: 0 }, 0); tl.to(bB, { opacity: 1, duration: 0.4 }, 12.6);
        tag(sB, "MARDI", 7.95);
        const mic = card(sB, "mic", "Dictée en cours…", "« Maison 120 m², vendeur motivé, rappeler dans 5 jours »", { top: "980px" }, 10.4, { bg: "rgba(217,58,63,.55)", snd: "tap" });
        tl.to(mic, { opacity: 0, y: -30, duration: 0.3 }, 12.3);
        card(sB, "note", "Fiche créée", "Estimation · compte rendu classé", { top: "980px" }, 12.45, { check: true });
        card(sB, "refresh", "Relance programmée", "Vendeur relancé dans 5 jours · automatique", { top: "1150px" }, 13.85, { check: true });
        const sC = lay(18.05, 26.95, sB, { colors: ["#1d2a7a", "#4b2a9a", "#0f3d6a"], a: 0.5 });
        tag(sC, "MERCREDI", 18.2);
        card(sC, "msg", "Nouveau message · 22:04", "Acquéreur : « Le T3 est toujours dispo ? »", { top: "520px" }, 19.3, { snd: "notif" });
        card(sC, "bell", "Demande notée", "Ressortie demain à 8:00", { top: "690px" }, 23.0, { check: true });
        const sD = foot("v2", 26.95, 36.55, sC);
        tag(sD, "JEUDI", 27.1);
        const bd = bday(sD, "M. Durand", 28.3, 470);
        tapSend(bd[1], 34.3);
        const sE = lay(36.55, 45.75, sD, { colors: ["#6b4fe0", "#2cc4b5", "#3a2a9a"] });
        tag(sE, "VENDREDI", 36.8);
        inbox(sE, 38.0, 280);
        card(sE, "camera", "Publications de la semaine", "Prêtes à poster", { top: "780px" }, 39.6, { check: true });
        km(sE, 41.85, 920);
        const sF = foot("v3", 45.6, 50.95, sE);
        const f1 = FX.rise(sF, "Et toi ?", { top: "380px", fontSize: "120px", textShadow: "0 6px 30px rgba(0,0,0,.5)" }, 46.2, { snd: false });
        FX.fall(f1, 47.4);
        FX.rise(sF, "Sur le terrain,|avec tes [clients].", { top: "380px", fontSize: "96px", textShadow: "0 6px 30px rgba(0,0,0,.5)" }, 47.85, { snd: false });
        outro(51.0);
        kar2([
          [0, 0.8, "Lundi matin."], [1.21, 3.29, "Tu ouvres Limo : ta semaine est prête."], [3.6, 6.89, "Les vendeurs à relancer, les visites, les compromis en cours."],
          [7.6, 8.06, "Mardi."], [8.56, 9.7, "Tu sors d’une estimation."], [10.14, 11.87, "Tu dictes trois phrases dans la voiture…"], [12.19, 13.1, "et la fiche est faite."], [13.51, 16.79, "Le vendeur sera relancé dans cinq jours. Automatiquement."],
          [17.84, 18.44, "Mercredi."], [18.94, 20.74, "Un acquéreur t’écrit à vingt-deux heures."], [21.1, 22.3, "Pas de panique :"], [22.7, 25.95, "Limo a noté sa demande, et te la ressort le lendemain matin."],
          [26.87, 27.36, "Jeudi."], [27.91, 31.13, "C’est l’anniversaire de M. Durand, qui t’a confié sa maison l’an dernier."], [31.69, 33.52, "Limo t’a préparé un petit message."], [33.95, 35.51, "Tu cliques. C’est envoyé."],
          [36.56, 37.14, "Vendredi."], [37.7, 38.91, "Ta boîte mail est triée."], [39.32, 41.13, "Tes publications de la semaine sont prêtes."], [41.54, 44.63, "Et tes frais kilométriques… déjà calculés."],
          [45.91, 46.86, "Et toi, pendant ce temps ?"], [47.53, 49.89, "Tu étais sur le terrain. Avec tes clients."],
        ]);
""")

# ---------------------------------------------------------------- L5 · Tu peux tout lui dire (Yariq, 41,7 s)
PRE["long-05-tout-lui-dire"] = ""
FILMS["long-05-tout-lui-dire"] = ("LIMO, tu peux tout lui dire", 42.6, SH4 + r"""
        const sA = lay(0, 4.2);
        FX.rise(sA, "Tu peux [tout]|lui dire.", { top: "620px", fontSize: "116px" }, 0.3);
        C.leak(0.3, 2.4);
        const sB = lay(4.2, 21.8, sA, { colors: ["#2cc4b5", "#6b4fe0", "#1d6f8a"] });
        const hd = FX.glass(sB, { left: "0", right: "0", margin: "0 auto", width: "520px", top: "250px", padding: "16px 26px", borderRadius: "999px", display: "flex", alignItems: "center", justifyContent: "center", gap: "14px", fontFamily: "Montserrat, sans-serif", fontWeight: "800", fontSize: "38px" }, `${K.icon("mic")}Demander à Limo`);
        K.$$("svg.i", hd).forEach((s) => (s.style.cssText = "width:40px;height:40px;color:#2cc4b5"));
        const Q = [
          ["« Limo, rappelle-moi de relancer Mme Roy jeudi. »", "C’est noté : relance jeudi à 9 h.", 4.25, 7.2, 8.15],
          ["« Limo, qui cherche un appartement avec terrasse ? »", "3 acquéreurs correspondent : Durand, Vidal, Faure.", 8.3, 11.1, 13.55],
          ["« Limo, prépare un mail pour le notaire du dossier Martin. »", "C’est rédigé. Tu veux le relire ?", 13.7, 16.5, 17.7],
          ["« Limo, combien j’ai fait de kilomètres ce mois-ci ? »", "1 248 km en octobre. Frais calculés.", 17.85, 20.1, 21.6],
        ];
        Q.forEach((q) => { const e = ask(sB, q[0], q[1], q[2], q[3], 520); tl.to(e, { opacity: 0, y: -40, duration: 0.25 }, q[4]); });
        const sC = lay(21.8, 27.75, sB, { colors: ["#6b4fe0", "#2cc4b5", "#3a2a9a"] });
        FX.rise(sC, "Il retient [tout].", { top: "170px", fontSize: "100px" }, 21.75, { snd: false });
        web(sC, [["home", "Mandats", 23.1], ["users", "Vendeurs", 24.0], ["target", "Acquéreurs", 24.8], ["refresh", "Chaque relance", 25.9], ["msg", "Chaque demande", 26.8]], 22.3);
        const sD = lay(27.75, 31.75, sC, { colors: ["#2cc4b5", "#6b4fe0", "#1d6f8a"] });
        card(sD, "cake", "Anniversaires", "Message prêt pour chaque client", { top: "470px" }, 27.7, { check: true, bg: "rgba(255,143,143,.5)" });
        card(sD, "mail", "Mails triés", "Les importants en premier", { top: "630px" }, 28.95, { check: true });
        card(sD, "camera", "Réseaux sociaux", "Publications prêtes", { top: "790px" }, 30.1, { check: true });
        const sE = lay(31.75, 35.55, sD, { colors: ["#3a2a9a", "#6b4fe0", "#0f3d6a"] });
        FX.rise(sE, "Tu [parles].", { top: "480px", fontSize: "116px" }, 31.8);
        FX.rise(sE, "Il [agit].", { top: "620px", fontSize: "116px" }, 32.75, { snd: false });
        FX.rise(sE, "Rien ne tombe|dans l’[oubli].", { top: "800px", fontSize: "84px" }, 33.6, { snd: false, color: "#d9ceff" });
        outro(35.5);
        kar2([
          [0, 3.43, "Et si tu pouvais tout dire à ton assistant… comme à un collègue ?"],
          [3.92, 6.21, "« Limo, rappelle-moi de relancer Mme Roy jeudi. »"], [6.91, 7.5, "C’est noté."],
          [7.97, 10.37, "« Limo, qui cherche un appartement avec terrasse en ce moment ? »"], [10.78, 12.97, "Il te sort les trois acquéreurs qui correspondent."],
          [13.41, 15.74, "« Limo, prépare un mail pour le notaire du dossier Martin. »"], [16.2, 17.21, "C’est rédigé."],
          [17.56, 19.41, "« Limo, combien j’ai fait de kilomètres ce mois-ci ? »"], [19.82, 21.08, "Il a déjà fait le calcul."],
          [21.41, 22.24, "Il retient tout."], [22.69, 27.02, "Tes mandats, tes clients, vendeurs comme acquéreurs, chaque relance, chaque demande."],
          [27.33, 31.08, "Il pense aux anniversaires. Il trie tes mails. Il t’aide sur les réseaux sociaux."], [31.5, 34.61, "Tu parles. Il agit. Et rien ne tombe dans l’oubli."],
        ]);
""")

# ---------------------------------------------------------------- L6 · Par des agents immobiliers (Yariq, 46,8 s)
PRE["long-06-par-des-agents"] = V("v1", "agent-voiture-grade", 4.45, 4.0, 1) + V("v2", "femme-vent-grade", 31.1, 3.8, 2, 4.0)
FILMS["long-06-par-des-agents"] = ("LIMO, par des agents immobiliers", 47.7, SH4 + r"""
        const sA = lay(0, 4.45, null, { colors: ["#3a2a9a", "#6b4fe0", "#0f3d6a"] });
        FX.rise(sA, "Pas inventé par des gens|qui n’ont jamais fait|une [visite].", { top: "600px", fontSize: "76px" }, 0.3);
        const sB = foot("v1", 4.45, 8.45, sA);
        FX.rise(sB, "Par des agents immo,|pour des [agents] [immo].", { top: "300px", fontSize: "70px", textShadow: "0 6px 30px rgba(0,0,0,.5)" }, 4.6, { snd: false });
        const sC = lay(8.45, 15.7, sB, { colors: ["#3a3d55", "#5a2a4a", "#1a1c2a"], a: 0.55 });
        FX.rise(sC, "On a [connu] ça.", { top: "240px", fontSize: "96px" }, 8.5, { accent: "#ff8f8f", snd: false });
        [["alert", "Relances oubliées", 600, 8.9], ["x", "Mandats perdus, rappelés trop tard", 740, 10.6], ["clock", "Dimanches soirs sur l’admin", 880, 13.4]].forEach((c) => {
          const g = chip(sC, `${K.icon(c[0])}${c[1]}`, { left: "0", right: "0", margin: "0 auto", width: "fit-content", top: c[2] + "px", background: "rgba(217,58,63,.35)" }, c[3], { snd: "buzz", g: 0.12 });
        });
        const sD = lay(15.7, 18.75, sC, { colors: ["#2cc4b5", "#6b4fe0", "#1d6f8a"] });
        FX.rise(sD, "Alors on a construit|l’assistant qu’on aurait|[voulu] [avoir].", { top: "640px", fontSize: "84px" }, 15.85);
        const sE = lay(18.75, 25.6, sD, { colors: ["#2cc4b5", "#6b4fe0", "#1d6f8a"] });
        FX.rise(sE, "Il retient [tout].", { top: "170px", fontSize: "100px" }, 18.8, { snd: false });
        web(sE, [["home", "Mandats", 20.6], ["users", "Vendeurs", 21.4], ["target", "Acquéreurs", 22.2], ["msg", "Demandes", 23.0], ["refresh", "Aucune relance oubliée", 24.0]], 19.3);
        const sF = lay(25.6, 31.25, sE, { colors: ["#6b4fe0", "#2cc4b5", "#3a2a9a"] });
        card(sF, "cake", "Anniversaires", "Souhaités pour toi", { top: "400px" }, 25.6, { check: true, bg: "rgba(255,143,143,.5)" });
        card(sF, "mail", "Mails inutiles", "Triés, archivés", { top: "560px" }, 26.95, { check: true });
        card(sF, "camera", "Réseaux sociaux", "Publications prêtes", { top: "720px" }, 28.0, { check: true });
        card(sF, "car", "Frais kilométriques", "Calculés automatiquement", { top: "880px" }, 29.3, { check: true });
        const sG = foot("v2", 31.25, 35.05, sF);
        const g1 = FX.rise(sG, "Il parle ton|[langage].", { top: "330px", fontSize: "100px", textShadow: "0 6px 30px rgba(0,0,0,.5)" }, 31.35, { snd: false });
        FX.fall(g1, 33.2);
        FX.rise(sG, "Il vient de|ton [métier].", { top: "330px", fontSize: "100px", textShadow: "0 6px 30px rgba(0,0,0,.5)" }, 33.35, { snd: false });
        const sH = lay(35.05, 40.1, sG, { colors: ["#3a2a9a", "#6b4fe0", "#0f3d6a"] });
        const h1 = FX.rise(sH, "Pas un logiciel|[de] [plus].", { top: "560px", fontSize: "104px" }, 35.2, { accent: "#ff8f8f" });
        FX.fall(h1, 37.2);
        FX.rise(sH, "Un [collègue]|qui comprend|ce que tu vis.", { top: "520px", fontSize: "100px" }, 37.45, { snd: false });
        outro(40.1);
        kar2([
          [0, 3.8, "Limo n’a pas été inventé par des gens qui n’ont jamais fait une visite."], [4.15, 7.56, "Il a été créé par des agents immobiliers, pour des agents immobiliers."],
          [7.97, 15.09, "Par des conseillers qui ont connu les relances oubliées, les mandats perdus parce qu’on a rappelé trop tard, les dimanches soirs passés sur l’administratif."],
          [15.52, 18.04, "Alors on a construit l’assistant qu’on aurait voulu avoir."], [18.47, 19.8, "Un assistant qui retient tout :"],
          [20.16, 24.98, "tes mandats, tes vendeurs, tes acquéreurs, leurs demandes. Qui n’oublie aucune relance."],
          [25.23, 30.57, "Qui souhaite les anniversaires, trie les mails inutiles, t’aide sur les réseaux sociaux, calcule tes frais kilométriques."],
          [30.96, 34.26, "Un assistant qui parle ton langage. Parce qu’il vient de ton métier."],
          [34.88, 39.01, "Limo, c’est pas un logiciel de plus. C’est un collègue qui comprend ce que tu vis."],
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
