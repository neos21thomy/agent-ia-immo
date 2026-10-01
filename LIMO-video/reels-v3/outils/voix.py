"""Films en voix off (voix ElevenLabs fournies, sources/voix/) : V1 l'histoire de Julien (Marie),
V2 Regarde ça (Lucie), V3 Surchargé ? (Paul). Les temps des phrases viennent d'une transcription locale
(Whisper small, sherpa-onnx) de chaque fichier ; la voix est mixée au rendu (outils : voir README).

Usage : python3 outils/voix.py   (réécrit reels/voix-*.html et outils/voix.json)
"""
import json
import pathlib

from cine import COMMON, FACES, GLASS, SHELL
from lifestyle import TOOLS, V

# fichier de voix et décalage (s) de chaque film, lus par le script de rendu
VOICE = {
    "voix-01-julien": [["Marie-15_24_09.mp3", 0.3]],
    "voix-02-regarde-ca": [["Lucie-15_52_09.mp3", 0.2], ["Lucie-16_18_01.mp3", 15.9]],
    "voix-03-surcharge": [["Paul-14_59_59.mp3", 0.2]],
}

# couches plein écran avec fenêtre d'affichage, sous-titres synchronisés à la voix
VTOOLS = r"""
        const layer = (bg, t0, t1, fade = 0.25) => {
          const l = C.ab({ left: "-200px", top: "-200px", width: "1480px", height: "2320px", background: bg });
          tl.set(l, { opacity: 0 }, 0);
          tl.to(l, { opacity: 1, duration: fade }, t0);
          if (t1) tl.to(l, { opacity: 0, duration: fade }, t1);
          return l;
        };
        const DARK = "radial-gradient(ellipse at 50% 35%, #23264f 0%, #0c0d22 75%)", LIGHT = "linear-gradient(180deg, #f5f3fe 0%, #ece7fb 100%)";
        const sub = (txt, t0, t1, o = {}) => {
          const s = C.ab({ left: "70px", right: "70px", top: (o.top || 1330) + "px", textAlign: "center" }, `<span style="display:inline-block;padding:14px 26px;border-radius:22px;background:${o.light ? "rgba(255,255,255,.92)" : "rgba(8,9,24,.62)"};color:${o.light ? "#1b1f4b" : "#fff"};font-family:Montserrat,sans-serif;font-weight:700;font-size:${o.fs || 46}px;line-height:1.25;box-shadow:0 10px 30px rgba(0,0,0,.25)">${txt}</span>`);
          A.over(s);
          tl.set(s, { opacity: 0 }, 0);
          tl.fromTo(s, { opacity: 0, y: 14 }, { opacity: 1, y: 0, duration: 0.18, ease: "power2.out" }, t0);
          tl.to(s, { opacity: 0, duration: 0.15 }, t1);
          return s;
        };
        const front = (els) => [].concat(els).forEach((e) => root.appendChild(e));
"""

PRE = {}
FILMS = {}

# ---------------------------------------------------------------- V1 · l'histoire de Julien (Marie, 57 s)
O = 0.3  # décalage de la voix
PRE["voix-01-julien"] = (V("v1", "agent-voiture", 0, 3.7, 1) + V("v2", "vendeuse-canape", 3.7, 4.3, 2)
                         + V("v3", "vendeuse-canape", 46.3, 4.2, 3, 0.8))
FILMS["voix-01-julien"] = ("LIMO, l'histoire de Julien", 59.4, GLASS, TOOLS + VTOOLS + r"""
        const o = 0.3;
        // 1 · Julien
        shade(0, 8.0);
        const lt = C.ab({ left: "70px", top: "1180px", padding: "18px 26px", borderRadius: "22px" }, `<b style="display:block;font-family:Montserrat,sans-serif;font-weight:800;font-size:44px">Julien</b><span style="font-size:28px;opacity:.85">conseiller immobilier</span>`);
        lt.classList.add("glass");
        tl.set(lt, { opacity: 0 }, 0);
        tl.fromTo(lt, { opacity: 0, x: -60 }, { opacity: 1, x: 0, duration: 0.45, ease: "power3.out" }, 0.4);
        tl.to(lt, { opacity: 0, duration: 0.25 }, 3.5);
        sub("Ça, c’est Julien, conseiller immobilier.", 0 + o, 3.1 + o);
        // 2 · chez Mme Martin
        const lt2 = C.ab({ left: "70px", top: "1180px", padding: "18px 26px", borderRadius: "22px" }, `<b style="display:block;font-family:Montserrat,sans-serif;font-weight:800;font-size:44px">Mme Martin</b><span style="font-size:28px;opacity:.85">vendeuse · estimation ce soir</span>`);
        lt2.classList.add("glass");
        tl.set(lt2, { opacity: 0 }, 0);
        tl.fromTo(lt2, { opacity: 0, x: -60 }, { opacity: 1, x: 0, duration: 0.45, ease: "power3.out" }, 4.0);
        tl.to(lt2, { opacity: 0, duration: 0.25 }, 7.6);
        sub("Ce soir-là, son estimation avec Mme Martin s’est très bien passée.", 3.65 + o, 7.4 + o);
        // 3 · la note
        layer(DARK, 7.9, 13.1);
        const ip = N.iphone({ left: "160px", top: "300px", width: "760px", height: "1300px" }, "19:48");
        N.hide(ip.el);
        tl.fromTo(ip.el, { opacity: 0, y: 200 }, { opacity: 1, y: 0, duration: 0.5, ease: "power3.out" }, 8.0);
        const nt = K.h("div", "n-notes", `<h3>À faire</h3><div class="dt">Lundi 19:48</div><div style="font-size:46px;line-height:1.4"><span class="t"></span></div>`, ip.screen);
        K.$$("*", nt).forEach((e) => e.setAttribute("data-layout-allow-occlusion", ""));
        K.type(K.$(".t", nt), "Rappeler Mme Martin", 10.6 + o, 1.2, 0.06);
        tl.to(ip.el, { opacity: 0, y: 100, duration: 0.35 }, 12.8);
        sub("Avant de repartir, il se note simplement…", 7.9 + o, 10.5 + o);
        sub("« Rappeler Mme Martin. »", 10.6 + o, 12.4 + o);
        // 4 · la semaine l'engloutit
        layer(DARK, 13.0, 21.3);
        const W = [["APPEL MANQUÉ", "M. Vidal · 2 appels"], ["DOSSIER", "Compromis Roche : 3 pièces manquantes"], ["RELANCE", "Famille Durand attend ta réponse"], ["AGENDA", "Visite Vignols · 10:30"], ["MAIL", "Notaire : documents à envoyer"], ["APPEL MANQUÉ", "Mme Roy"], ["AGENDA", "Estimation Allassac · 14:00"], ["RELANCE", "M. Albert · mutation"]];
        const ws = W.map((w, i) => {
          const n = A.over(N.notif({ title: w[0], time: "", text: w[1], snd: "notif", g: 0.12 }, { left: (60 + (i % 3) * 20) + "px", top: 260 + i * 150 + "px", width: "900px" }, 13.5 + o + i * 0.55));
          return n;
        });
        tl.to(ws, { opacity: 0, filter: "blur(10px)", y: 40, duration: 0.5, stagger: 0.03 }, 19.5);
        sub("Mais la semaine reprend.", 13.26 + o, 14.4 + o);
        sub("Les appels, les dossiers, les relances, les rendez-vous…", 14.7 + o, 18.4 + o);
        sub("Et Julien oublie.", 19.27 + o, 21.0 + o);
        // 5 · le panneau
        photo("bien-pierre-balcon", 21.3, 26.6, [1.0, 1.1], [0, -30]);
        shade(21.3, 26.6);
        const sign = C.ab({ left: "520px", top: "860px", width: "460px", padding: "26px 30px", borderRadius: "14px", background: "#d93a3f", color: "#fff", textAlign: "center", fontFamily: "'Montserrat Hook', Montserrat, sans-serif", fontWeight: "800", boxShadow: "0 30px 60px rgba(0,0,0,.45)" }, `<div style="font-size:66px;line-height:1">À VENDRE</div><div style="margin-top:10px;font-family:Inter,sans-serif;font-weight:700;font-size:28px">Une autre agence</div>`);
        tl.set(sign, { opacity: 0 }, 0);
        tl.fromTo(sign, { opacity: 0, scale: 1.6, rotation: -8 }, { opacity: 1, scale: 1, rotation: -3, duration: 0.3, ease: "power4.in" }, 24.7 + o);
        K.sfx(24.95 + o, "stamp", 0.42);
        tl.to(sign, { opacity: 0, duration: 0.3 }, 26.4);
        sub("Quelques jours plus tard, il repasse devant chez elle…", 21.47 + o, 24.4 + o);
        sub("…et voit le panneau.", 24.7 + o, 26.3);
        // 6 · perdu après
        layer(DARK, 26.6, 35.0);
        const line = C.ab({ left: "120px", top: "760px", width: "840px", height: "8px", borderRadius: "4px", background: "rgba(255,255,255,.2)" });
        tl.set(line, { opacity: 0 }, 0); tl.set(line, { opacity: 1 }, 27.0);
        const P = [["Estimation", "lundi", "#2cc4b5", 0], ["Relance", "oubliée", "#d93a3f", 0.5], ["Panneau", "J + 12", "#d93a3f", 1]];
        const dots = [line];
        P.forEach((p, i) => {
          const d = C.ab({ left: 120 + p[3] * 840 - 40 + "px", top: "724px", width: "80px", textAlign: "center" }, `<div style="width:80px;height:80px;border-radius:50%;background:${p[2]};border:6px solid #0c0d22;box-shadow:0 0 0 4px ${p[2]}"></div><div style="margin-top:22px;font-family:Montserrat,sans-serif;font-weight:800;font-size:34px;color:#fff;white-space:nowrap;transform:translateX(-30%)">${p[0]}</div><div style="font-family:Inter,sans-serif;font-size:26px;color:rgba(255,255,255,.7);white-space:nowrap;transform:translateX(-30%)">${p[1]}</div>`);
          tl.set(d, { opacity: 0 }, 0);
          dots.push(d);
          K.pop(d, 27.2 + i * 1.6, { s: 0.4 });
          K.sfx(27.2 + i * 1.6, i ? "buzz" : "success", 0.16);
        });
        const big = C.title("Perdu [après].", { top: "330px", fontSize: "110px" }, 30.16 + o, { color: "#ffffff", accent: "#ff8f8f" });
        sub("Le mandat n’a pas été perdu pendant l’estimation.", 26.71 + o, 29.9 + o);
        sub("Il a été perdu après…", 30.16 + o, 32.1 + o);
        sub("…à cause d’une relance oubliée.", 32.37 + o, 34.6 + o);
        C.out(big, 34.4, 0.3);
        tl.to(dots, { opacity: 0, duration: 0.3 }, 34.4);
        // 7 · LIMO
        const L1 = layer(LIGHT, 34.9, 46.0, 0.01);
        C.iris(L1, 34.9, 0.8);
        C.leak(35.0, 2.4);
        const logo = C.ab({ left: "190px", top: "560px", width: "700px", height: "265px" }, `<img src="assets/img/limo-logo-ad.png" alt="LIMO" style="width:100%;height:100%" />`);
        tl.set(logo, { opacity: 0 }, 0);
        tl.fromTo(logo, { opacity: 0, scale: 1.3, filter: "blur(16px)" }, { opacity: 1, scale: 1, filter: "blur(0px)", duration: 0.8, ease: "power3.out" }, 35.9 + o);
        K.sfx(36.0 + o, "thump", 0.4);
        C.sweep(logo, 36.8 + o, 0.9);
        const tag = C.title("Le bras droit du [conseiller] [immo].", { top: "880px", fontSize: "52px" }, 37.74 + o, { snd: false });
        sub("Depuis, nous lui avons installé LIMO…", 35.14 + o, 37.5 + o, { light: true });
        sub("…le bras droit du conseiller immobilier.", 37.74 + o, 40.2 + o, { light: true });
        tl.to([logo, tag], { opacity: 0, y: -30, duration: 0.35 }, 40.4);
        const ph = A.phone({ left: "260px", top: "300px", width: "560px" }, { time: "8:00" });
        const pg = A.page(ph, A.HD + `<div class="a-hello"><span>Bonjour Julien,</span><br>Voici tes priorités du jour.</div>` +
          A.row("phone", "r", "Rappeler Mme Martin", "Estimation lundi · elle attend ton appel", "09:00", `<span class="a-tag t">Priorité</span>`) + A.row("refresh", "v", "Relancer 12 contacts", "Messages prêts", "09:30") + A.row("home", "t", "Suivre 2 visites", "Visites à suivre", "11:00"));
        A.enter(ph, 40.6, { flatAt: 0.8 });
        tl.fromTo(K.$(".a-row", pg), { boxShadow: "0 0 0 0 rgba(107,79,224,0)" }, { boxShadow: "0 0 0 6px rgba(107,79,224,.45)", duration: 0.4, yoyo: true, repeat: 3 }, 43.0);
        K.sfx(44.1 + o, "notif", 0.2);
        sub("Aujourd’hui, Julien ne compte plus seulement sur sa mémoire.", 40.62 + o, 43.9 + o, { light: true });
        sub("LIMO garde le fil.", 44.14 + o, 46.0, { light: true });
        A.leave(ph, 45.8);
        // 8 · Mme Martin relancée
        shade(46.2, 50.5);
        const s1 = sms("Bonjour Madame Martin, je reviens vers vous suite à l’estimation : avez-vous pu y réfléchir ?", "out", 320, 46.6, 50.3);
        const s2 = sms("Oui ! On aimerait signer avec vous 🙂".replace(" 🙂", ""), "in", 620, 48.3, 50.3);
        sub("Et Mme Martin, cette fois…", 46.28 + o, 48.1 + o);
        sub("…elle a bien été relancée.", 48.35 + o, 50.2);
        // 9 · signature
        layer(LIGHT, 50.4, null, 0.2);
        const e1 = C.title("Même les meilleurs", { top: "560px", fontSize: "68px" }, 50.55 + o);
        const e1b = C.title("conseillers", { top: "650px", fontSize: "68px" }, 51.0 + o, { snd: false });
        const e2 = C.title("oublient parfois.", { top: "740px", fontSize: "68px" }, 51.6 + o, { snd: false });
        const e3 = C.title("LIMO, [jamais].", { top: "900px", fontSize: "120px" }, 53.21 + o);
        K.sfx(54.17 + o, "slam", 0.3);
        C.out([e1, e1b, e2, e3], 55.2, 0.3);
        window.__TE = 55.5;
        N.outro(55.5, "demo");
        const m = N.mascot({ left: "440px", top: "1240px", width: "200px" });
        m.enter(57.0);
        m.wave(57.7);
""")

# ---------------------------------------------------------------- V2 · Regarde ça (Lucie, 15 s + 10 s)
FILMS["voix-02-regarde-ca"] = ("LIMO, regarde ça", 29.8, GLASS, TOOLS + VTOOLS + r"""
        const a = 0.2, b = 15.9;
        layer(LIGHT, 0, null, 0.01);
        const hk = N.hook(["<span class='kk'>CONSEILLER IMMO,</span>", "<span class='hl'>REGARDE ÇA.</span>"], { top: "300px", fontSize: "110px" });
        N.out(hk, 2.6, { y: -40 });
        sub("Si t’es conseiller immobilier, regarde ça.", 0 + a, 2.4 + a, { light: true });
        const ph = A.phone({ left: "260px", top: "380px", width: "560px" }, { time: "18:12" });
        const chat = A.page(ph, `<div class="a-back">${K.icon("chev")}Demander à LIMO</div><div style="display:flex;flex-direction:column;gap:14px;margin-top:10px">
<div class="q" style="align-self:flex-end;max-width:86%;padding:16px 20px;border-radius:24px 24px 6px 24px;background:#6b4fe0;color:#fff;font-size:23px;line-height:1.35"><span class="ty"></span></div>
<div class="r a-card" style="padding:16px;border-radius:24px 24px 24px 6px">
<div class="a-ph" style="height:170px;margin-bottom:12px"><img src="assets/img/bien-mas-lavande.jpg" alt="" style="width:100%;height:100%;object-fit:cover;object-position:50% 40%" /></div>
<b style="font-size:24px">Mas en pierre · 165 m²</b><div style="margin-top:6px;font-size:19px;color:#55586c;line-height:1.45">Terrain 2 400 m² · 5 chambres · DPE C<br>Propriétaires : M. et Mme T. · mandat exclusif<br>Diagnostics : 4 / 6 reçus · notaire : Me Faure</div></div></div>`);
        A.enter(ph, 2.4, { flatAt: 0.7 });
        K.type(K.$(".ty", chat), "Peux-tu me rappeler les infos du bien de M. et Mme T. ?", 2.9 + a, 3.4, 0.04);
        const r = K.$(".r", chat);
        tl.set(r, { opacity: 0 }, 0);
        tl.fromTo(r, { opacity: 0, y: 30, scale: 0.95 }, { opacity: 1, y: 0, scale: 1, duration: 0.45, ease: "back.out(1.6)" }, 7.0 + a);
        K.sfx(7.0 + a, "success", 0.26);
        sub("« Peux-tu me rappeler les informations du bien de M. et Mme T. ? »", 2.86 + a, 6.8 + a, { light: true, fs: 40 });
        sub("Et hop, tout ressort.", 6.99 + a, 8.9 + a, { light: true });
        const F = [["file", "v", "12 documents", "classés sur ce bien", 20, 260, 9.6], ["users", "t", "Propriétaires", "historique des échanges", 560, 1460, 10.6], ["calc", "v", "Estimation", "et ventes du secteur", 20, 1560, 11.6], ["shield", "t", "Diagnostics", "4 sur 6 reçus", 560, 300, 12.6]];
        const fs = F.map((f) => A.float(A.gain(f[0], f[1], f[2], f[3]), { left: f[4] + "px", top: f[5] + "px" }, f[6] + a));
        sub("Plus besoin d’aller chercher les informations partout.", 9.28 + a, 12.4 + a, { light: true });
        sub("LIMO connaît tes biens et tes clients par cœur.", 12.5 + a, 15.6 + a, { light: true });
        tl.to(fs, { opacity: 0, duration: 0.3 }, 15.6);
        // relances acquéreurs, diagnostiqueur, paperasse
        const n1 = A.over(N.notif({ title: "RELANCE ACQUÉREURS", time: "", text: "8 acquéreurs relancés pour le mas en pierre." }, { left: "90px", top: "600px" }, b + 0.8));
        const n2 = A.over(N.notif({ title: "DIAGNOSTIQUEUR", time: "", text: "DPE et amiante manquants : demande envoyée.", g: 0.2 }, { left: "90px", top: "800px" }, b + 4.1));
        const n3 = A.over(N.notif({ title: "DOSSIER", time: "", text: "Dossier notaire complété : 2 pièces ajoutées.", snd: "success", g: 0.26 }, { left: "90px", top: "1000px" }, b + 6.9));
        sub("Et en plus, LIMO relance tes futurs acquéreurs…", b + 0, b + 3.9, { light: true });
        sub("…le diagnostiqueur, s’il te manque des diags…", b + 4.08, b + 6.7, { light: true });
        sub("Il s’occupe de la paperasse pendant que toi, tu vends.", b + 6.94, b + 9.9, { light: true });
        N.out([n1, n2, n3], 25.6, { y: -30 });
        A.leave(ph, 25.6);
        window.__TE = 26.0;
        N.outro(26.0, "pub");
        const m = N.mascot({ left: "440px", top: "1240px", width: "200px" });
        m.enter(27.6);
        m.wave(28.3);
""")

# ---------------------------------------------------------------- V3 · Surchargé ? (Paul, 6 s)
FILMS["voix-03-surcharge"] = ("LIMO, surchargé ?", 10.4, GLASS, TOOLS + VTOOLS + r"""
        const a = 0.2;
        layer(DARK, 0, 3.4, 0.01);
        const hk = N.hook(["<span class='kk' style='color:#b9a6ff'>CONSEILLER IMMO,</span>", "<span class='hl'>SURCHARGÉ ?</span>"], { top: "330px", fontSize: "116px", color: "#ffffff" });
        const W = [["APPEL MANQUÉ", "M. Vidal"], ["DOSSIER", "3 pièces manquantes"], ["RELANCE", "Famille Durand"], ["AGENDA", "Visite 10:30"], ["MAIL", "Notaire"], ["ANNONCE", "à rédiger"], ["AVIS GOOGLE", "sans réponse"], ["ESTIMATION", "à envoyer"]];
        const ws = W.map((w, i) => A.over(N.notif({ title: w[0], time: "", text: w[1], snd: "notif", g: 0.1 }, { left: (40 + (i % 3) * 30) + "px", top: 700 + i * 110 + "px", width: "900px" }, 0.3 + i * 0.28)));
        tl.to(ws, { x: (i) => (i % 2 ? 1200 : -1200), rotation: (i) => (i % 2 ? 12 : -12), opacity: 0, duration: 0.5, ease: "power3.in", stagger: 0.03 }, 3.2);
        K.sfx(3.2, "whoosh", 0.3, 0, { d: 0.6, f0: 300, f1: 4000, pk: 0.5 });
        N.out(hk, 3.2, { y: -40 });
        sub("Si tu es conseiller immobilier et que tu es surchargé…", 0 + a, 2.95 + a);
        sub("…apprends à déléguer.", 3.15 + a, 4.4 + a, { light: true });
        layer(LIGHT, 3.4, null, 0.2);
        const logo = C.ab({ left: "190px", top: "560px", width: "700px", height: "265px" }, `<img src="assets/img/limo-logo-ad.png" alt="LIMO" style="width:100%;height:100%" />`);
        tl.set(logo, { opacity: 0 }, 0);
        tl.fromTo(logo, { opacity: 0, scale: 1.3, filter: "blur(16px)" }, { opacity: 1, scale: 1, filter: "blur(0px)", duration: 0.6, ease: "power3.out" }, 4.6 + a);
        K.sfx(4.7 + a, "thump", 0.4);
        const M = N.mascot({ left: "340px", top: "900px", width: "400px" });
        M.enter(4.9 + a);
        M.wave(5.3 + a);
        sub("LIMO est fait pour ça.", 4.65 + a, 6.4 + a, { light: true });
        tl.to(logo, { opacity: 0, duration: 0.3 }, 6.5);
        window.__TE = 6.7;
        N.outro(6.7, "pub");
        M.move(6.6, { x: 0, y: 1370 - (900 + 242), scale: 200 / 400 }, 0.6);
""")

if __name__ == "__main__":
    pathlib.Path("outils/voix.json").write_text(json.dumps(VOICE, indent=1), encoding="utf-8")
    for name, (title, dur, css, body) in FILMS.items():
        html = SHELL.format(title=title, faces=FACES, css=css.strip("\n"), body=(COMMON + body).strip("\n"), dur=dur, name=name)
        if name in PRE:
            html = html.replace('      <section id="s-main"', PRE[name] + '      <section id="s-main"', 1)
        pathlib.Path(f"reels/{name}.html").write_text(html, encoding="utf-8")
        print("reels/" + name + ".html")
