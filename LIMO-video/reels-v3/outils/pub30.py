"""Pubs 30 s : « Agent immobilier, … » → problème vécu → l'application LIMO en action → gains (temps, argent)
→ « Contacte-nous et découvre LIMO ». Application recréée en HTML (assets/kit/app.*). Données fictives.

Usage : python3 outils/pub30.py   (réécrit reels/pub30-*.html)
"""
import pathlib

from hooks import FACES, SHELL as _SHELL

SHELL = _SHELL.replace('<link rel="stylesheet" href="assets/kit/naturel.css" />', '<link rel="stylesheet" href="assets/kit/naturel.css" />\n    <link rel="stylesheet" href="assets/kit/app.css" />')
SHELL = SHELL.replace('<script src="assets/kit/naturel.js"></script>', '<script src="assets/kit/naturel.js"></script>\n    <script src="assets/kit/app.js"></script>')
SHELL = SHELL.replace("N.init(tl, root, D);", "N.init(tl, root, D);\n        A.init(tl, root);")

# Bloc commun : gains (3 cartes) puis fin « Contacte-nous » avec la mascotte
COMMON = r"""
        const glow = (x, y, s, t) => { const g = N.ab("n-glow", null, { left: x + "px", top: y + "px", width: s + "px", height: s + "px" }); g.setAttribute("data-layout-allow-overflow", ""); N.hide(g); tl.fromTo(g, { opacity: 0, scale: 0.6 }, { opacity: 1, scale: 1, duration: 1.2, ease: "power2.out" }, t); return g; };
        const gains = (t, G, note) => {
          const h = N.head(["CE QUE ÇA", "TE RAPPORTE<span class='v'>.</span>"], { top: "170px", fontSize: "86px" }, t);
          const els = G.map((g, i) => {
            const c = N.ab("g-card", `<div class="k">${g.k}</div><div class="v ${g.c || ""}"><span>${g.v0 || ""}</span></div><div class="d">${g.d}</div>`, { left: "90px", top: 480 + i * 330 + "px", width: "900px" });
            N.hide(c);
            const tt = t + 0.5 + i * 0.7;
            tl.fromTo(c, { opacity: 0, x: i % 2 ? 120 : -120 }, { opacity: 1, x: 0, duration: 0.55, ease: "power3.out" }, tt);
            K.sfx(tt, "whoosh", 0.12, 0, { d: 0.35, f0: 600, f1: 3000, pk: 0.6 });
            if (g.n != null) K.count(K.$(".v span", c), g.n, tt + 0.2, 1.0, g.f, { ticks: 10 }); else K.$(".v span", c).innerHTML = g.v;
            if (g.n != null) K.sfx(tt + 1.2, "success", 0.18);
            return c;
          });
          const nt = N.text("ctr g-note", note || "Exemples indicatifs", { top: "1490px" }, t + 2.4);
          return [h, ...els, nt];
        };
        const fin = (t, M) => {
          N.outro(t, "contact");
          const m = N.mascot({ left: "440px", top: "1240px", width: "200px" });
          m.enter(t + 1.6);
          m.wave(t + 2.3);
          m.blink(t + 3.2);
        };
"""

FILMS = {}

# ---------------------------------------------------------------- 1 · mandats perdus (relances)
FILMS["pub30-01-mandats-perdus"] = ("Agent immobilier, tu perds des mandats sans le savoir", 30.0, "", r"""
        glow(-300, 300, 1100, 0);
        const hk = N.hook(["<span class='kk'>AGENT IMMOBILIER,</span>", "TU PERDS", "DES MANDATS", "<span class='hl'>SANS LE SAVOIR.</span>"], { top: "470px", fontSize: "100px" });
        const s1 = N.text("ctr n-body", "Pas à cause du prix.<br><b>À cause d’un oubli.</b>", { top: "1060px", fontSize: "48px" }, 0.9);
        N.out([hk, s1], 2.7, { y: -40 });
        // ---- le problème
        const cap = N.cap("Ta liste « à rappeler »…", { top: "150px" }, 2.9);
        const ip = N.iphone({ left: "110px", top: "400px", width: "860px", height: "1480px" }, "18:40");
        N.hide(ip.el);
        tl.fromTo(ip.el, { opacity: 0, y: 300 }, { opacity: 1, y: 0, duration: 0.6, ease: "power3.out" }, 2.9);
        const notes = K.h("div", "n-notes", `<h3>À rappeler</h3><div class="dt">Notes · mis à jour en février</div>`, ip.screen);
        notes.setAttribute("data-layout-allow-occlusion", "");
        K.$$("*", notes).forEach((e) => e.setAttribute("data-layout-allow-occlusion", ""));
        [["M. Vidal · estimation", "il y a 47 j"], ["Famille Martin · vendre au printemps", "il y a 62 j"], ["Mme Roy · succession", "il y a 30 j"], ["M. Albert · mutation", "il y a 21 j"]].forEach((l, i) => {
          const r = K.h("div", "n-li", `<span class="c"></span><span class="t" style="font-size:34px">${l[0]}</span><span class="tag" style="background:#ffe8e8;color:#c0282d">${l[1]}</span>`, notes);
          N.hide(r);
          r.setAttribute("data-layout-allow-occlusion", "");
          K.fin(r, 3.3 + i * 0.3, { y: 14, d: 0.3 });
          K.sfx(3.3 + i * 0.3, "tick", 0.14, 0, { f: 1500 + i * 120 });
        });
        const bad = A.over(N.notif({ title: "MESSAGES", time: "18:42", text: "Mme Martin : « Finalement, nous avons signé avec une autre agence. »", snd: "buzz", g: 0.2 }, { left: "90px", top: "520px" }, 5.0));
        bad.setAttribute("data-layout-allow-overlap", "");
        tl.fromTo(ip.el, { x: 0 }, { x: 10, duration: 0.05, ease: "none", yoyo: true, repeat: 5, immediateRender: false }, 5.1);
        N.out(cap, 5.8, { y: -10, d: 0.2 });
        const c2 = N.cap("4 vendeurs oubliés.<br>1 mandat perdu.", { top: "150px" }, 6.0, { dark: true });
        K.sfx(6.0, "thump", 0.3);
        N.out([c2, ip.el, bad], 7.6, { y: 60, d: 0.4 });
        // ---- LIMO en action
        const h = N.head(["AVEC LIMO, PLUS PERSONNE", "N’EST OUBLIÉ<span class='v'>.</span>"], { top: "150px", fontSize: "62px" }, 7.9, { bar: false });
        glow(140, 520, 800, 7.9);
        const ph = A.phone({ left: "260px", top: "470px", width: "560px" }, { time: "9:30" });
        const p1 = A.page(ph, A.HD + `<div class="a-hello"><span>Bonjour,</span><br>Voici les actions prioritaires du jour.</div>
<div class="a-card a-prio"><span class="n">5</span><span><b>Actions prioritaires</b><small>à traiter aujourd’hui</small></span></div>
<div class="a-h2">Actions du jour</div>` + A.row("refresh", "v", "Relancer 32 contacts", "Relances programmées", "09:30") + A.row("home", "t", "Suivre 2 visites", "Visites à suivre", "11:00") + A.row("shield", "g", "Envoyer 1 proposition", "Mandat en préparation", "14:00") + A.row("star", "t", "Nouveau mandat détecté", "Opportunité à saisir", "15:30"));
        const p2 = A.page(ph, `<div class="a-back">${K.icon("chev")}Relances du jour</div>
<div style="display:flex;gap:10px;margin:4px 0 18px"><span class="a-tag">${K.icon("refresh")}32 contacts</span><span class="a-tag t">${K.icon("check")}Messages prêts</span></div>` +
          A.row("users", "v", "M. Vidal", "Estimation · il y a 47 j", "", `<span class="a-tag t">Prêt</span>`) + A.row("users", "v", "Famille Martin", "Vendre au printemps", "", `<span class="a-tag t">Prêt</span>`) + A.row("users", "v", "Mme Roy", "Succession en cours", "", `<span class="a-tag t">Prêt</span>`) +
          `<div class="a-card a-msg"><span class="ty"></span></div><div class="a-btn" style="margin-top:18px"><span class="bt">${K.icon("send")}Envoyer les 32 relances</span></div>`);
        A.enter(ph, 8.1);
        K.$$(".a-row", p1).forEach((r, i) => K.fin(r, 9.0 + i * 0.12, { y: 18, d: 0.35 }));
        A.tap(ph, 270, 640, 10.6);
        A.go(ph, p1, p2, 10.8);
        K.type(K.$(".ty", p2), "Bonjour M. Vidal, vous m’aviez parlé de vendre au printemps : on fait le point cette semaine ?", 11.5, 1.6, 0.04);
        A.tap(ph, 264, 1030, 13.5);
        const btn = K.$(".a-btn", p2);
        tl.to(btn, { backgroundColor: "#2cc4b5", duration: 0.25 }, 13.6);
        tl.set(K.$(".bt", btn), { innerHTML: `${K.icon("check")}32 relances envoyées` }, 13.6);
        K.sfx(13.6, "success", 0.26);
        const f1 = A.float(A.gain("timer", "v", "− 2 h 30", "de relances / semaine"), { left: "30px", top: "760px" }, 14.2);
        const f2 = A.float(A.gain("check", "t", "0 oubli", "chaque vendeur suivi"), { left: "590px", top: "1420px" }, 14.8);
        const n1 = A.over(N.notif({ title: "RENDEZ-VOUS", time: "10:12", text: "Famille Martin : estimation jeudi à 10 h." }, { left: "90px", top: "600px" }, 16.0));
        const n2 = A.over(N.notif({ title: "MANDAT", time: "jeudi", text: "Mandat exclusif signé : famille Martin.", snd: "success", g: 0.3 }, { left: "90px", top: "600px" }, 17.4));
        tl.to(n1, { opacity: 0, y: -40, duration: 0.25 }, 17.3);
        N.out([h, f1, f2, n2], 19.2, { y: -30 });
        A.leave(ph, 19.2);
        // ---- gains
        const g = gains(19.9, [
          { k: "TEMPS GAGNÉ", n: 150, f: (v) => { const m = Math.round(v); return Math.floor(m / 60) + " h " + String(m % 60).padStart(2, "0"); }, d: "par semaine : tes relances sont <b>déjà écrites</b>." },
          { k: "ARGENT", c: "t", n: 7500, f: (v) => "+ " + K.eur(v), d: "<b>1 seul mandat récupéré</b> = les honoraires d’une vente." },
          { k: "PRIX DE LIMO", v: "dès 49 €<small style='font-size:.4em'>/mois</small>", d: "Rentabilisé dès <b>le premier mandat</b>." },
        ]);
        N.out(g, 25.6, { y: -30 });
        window.__TE = 26.0;
        fin(26.0);
""")

# Fonctions de temps partagées
MIN = r"(v) => { const m = Math.round(v); return m >= 60 ? Math.floor(m / 60) + ' h ' + String(m % 60).padStart(2, '0') : m + ' min'; }"
PRIX = r"""{ k: "PRIX DE LIMO", v: "dès 49 €<small style='font-size:.4em'>/mois</small>", d: "Rentabilisé dès <b>le premier mandat</b>." }"""

# ---------------------------------------------------------------- 2 · le vendeur a appelé 3 agences (rapidité)
FILMS["pub30-02-trois-agences"] = ("Agent immobilier, ton vendeur a appelé 3 agences", 30.0, "", r"""
        glow(-300, 300, 1100, 0);
        const hk = N.hook(["<span class='kk'>AGENT IMMOBILIER,</span>", "TON VENDEUR A", "APPELÉ 3 AGENCES", "<span class='hl'>HIER SOIR.</span>"], { top: "470px", fontSize: "84px" });
        const s1 = N.text("ctr n-body", "Il signera avec<br><b>la première qui répond.</b>", { top: "980px", fontSize: "48px" }, 0.9);
        N.out([hk, s1], 2.7, { y: -40 });
        const cap = N.cap("19 h 12. Tu es en visite.", { top: "150px" }, 2.9);
        const ip = N.iphone({ left: "110px", top: "400px", width: "860px", height: "1480px" }, "19:58");
        N.hide(ip.el);
        tl.fromTo(ip.el, { opacity: 0, y: 300 }, { opacity: 1, y: 0, duration: 0.6, ease: "power3.out" }, 2.9);
        const notes = K.h("div", "n-notes", `<h3>Récents</h3><div class="dt">Téléphone</div>`, ip.screen);
        notes.style.background = "#fff";
        [["Mme Garnier", "Appel manqué · 19:12"], ["Mme Garnier", "Appel manqué · 19:14"], ["Messagerie", "Nouveau message (0:42)"]].forEach((l, i) => {
          const r = K.h("div", "n-li", `<span class="c" style="border-color:#ff3b30"></span><span class="t" style="font-size:34px;color:#d93a3f">${l[0]}<br><small style="font-size:24px;color:#6e6e73">${l[1]}</small></span>`, notes);
          N.hide(r);
          K.fin(r, 3.3 + i * 0.35, { y: 14, d: 0.3 });
          K.sfx(3.3 + i * 0.35, "buzz", 0.1);
        });
        K.$$("*", notes).forEach((e) => e.setAttribute("data-layout-allow-occlusion", ""));
        N.out(cap, 5.4, { y: -10, d: 0.2 });
        const c2 = N.cap("Le lendemain,<br>elle a déjà choisi une agence.", { top: "150px" }, 5.6, { dark: true });
        K.sfx(5.6, "thump", 0.3);
        N.out([c2, ip.el], 7.6, { y: 60, d: 0.4 });
        const h = N.head(["LIMO RÉPOND PENDANT", "QUE TU TRAVAILLES<span class='v'>.</span>"], { top: "150px", fontSize: "62px" }, 7.9, { bar: false });
        glow(140, 520, 800, 7.9);
        const ph = A.phone({ left: "260px", top: "470px", width: "560px" }, { time: "19:16", tab: 1 });
        const p1 = A.page(ph, `<div class="a-back">${K.icon("chev")}Mme Garnier</div>
<div style="display:flex;gap:10px;margin:4px 0 16px"><span class="a-tag">${K.icon("sparkles")}Nouveau vendeur</span><span class="a-tag t">${K.icon("check")}Fiche créée</span></div>` +
          A.row("home", "v", "Maison 120 m² · Brive", "Bien à estimer") + A.row("calc", "t", "Souhaite une estimation", "Projet : vendre cet été") +
          `<div class="a-h2">SMS prêt à envoyer</div><div class="a-card a-msg"><span class="ty"></span></div><div class="a-btn" style="margin-top:16px"><span class="bt">${K.icon("send")}Valider et envoyer</span></div>`);
        const p2 = A.page(ph, `<div class="a-back">${K.icon("chev")}Agenda</div><div class="a-h2">Jeudi</div>` +
          A.row("calc", "v", "Estimation · Mme Garnier", "Maison 120 m² · Brive", "10:00", `<span class="a-tag t">Confirmé</span>`) + A.row("home", "t", "Visite · Vignols", "Famille Durand", "14:30") + A.row("users", "g", "Point mandat · M. Albert", "Appel", "17:00"));
        A.enter(ph, 8.1);
        K.type(K.$(".ty", p1), "Bonjour Madame Garnier, merci pour votre appel ! Je peux passer estimer votre maison jeudi à 10 h. Cela vous convient ?", 9.6, 1.9, 0.04);
        A.tap(ph, 264, 1010, 11.9);
        const btn = K.$(".a-btn", p1);
        tl.to(btn, { backgroundColor: "#2cc4b5", duration: 0.25 }, 12.0);
        tl.set(K.$(".bt", btn), { innerHTML: `${K.icon("check")}SMS envoyé à 19 h 16` }, 12.0);
        K.sfx(12.0, "send", 0.24);
        const f1 = A.float(A.gain("timer", "v", "4 min", "pour répondre"), { left: "30px", top: "760px" }, 12.6);
        const n1 = A.over(N.notif({ title: "MESSAGES", time: "19:21", text: "Mme Garnier : « Jeudi 10 h, parfait ! Merci pour votre réactivité. »", snd: "receive", g: 0.28 }, { left: "90px", top: "600px" }, 13.8));
        tl.to(n1, { opacity: 0, y: -40, duration: 0.25 }, 15.6);
        A.go(ph, p1, p2, 15.7);
        K.$$(".a-row", p2).forEach((r, i) => K.fin(r, 16.1 + i * 0.15, { y: 16, d: 0.3 }));
        const f2 = A.float(A.gain("trophy", "t", "1re agence", "à répondre"), { left: "590px", top: "1420px" }, 16.8);
        N.out([h, f1, f2], 19.2, { y: -30 });
        A.leave(ph, 19.2);
        const g = gains(19.9, [
          { k: "TEMPS DE RÉPONSE", n: 4, f: (v) => Math.round(v) + " min", d: "au lieu du <b>lendemain</b> : tu réponds le premier." },
          { k: "ARGENT", c: "t", n: 6000, f: (v) => "+ " + K.eur(v), d: "<b>1 estimation décrochée</b> = un mandat potentiel." },
          """ + PRIX + r""",
        ]);
        N.out(g, 25.6, { y: -30 });
        window.__TE = 26.0;
        fin(26.0);
""")

# ---------------------------------------------------------------- 3 · les soirées sur les annonces
FILMS["pub30-03-annonces"] = ("Agent immobilier, combien de soirées sur tes annonces ?", 30.0, """
      .cur { display: inline-block; width: 4px; height: 44px; background: #f5b700; vertical-align: -8px; margin-left: 2px; }
""", r"""
        glow(-300, 300, 1100, 0);
        const hk = N.hook(["<span class='kk'>AGENT IMMOBILIER,</span>", "COMBIEN DE", "SOIRÉES SUR", "<span class='hl'>TES ANNONCES ?</span>"], { top: "470px", fontSize: "90px" });
        const s1 = N.text("ctr n-body", "45 minutes par annonce.<br><b>Fois 8 annonces par mois.</b>", { top: "980px", fontSize: "48px" }, 0.9);
        N.out([hk, s1], 2.7, { y: -40 });
        const cap = N.cap("22 h 47. Page blanche.", { top: "150px" }, 2.9);
        const ip = N.iphone({ left: "110px", top: "400px", width: "860px", height: "1480px" }, "22:47");
        N.hide(ip.el);
        tl.fromTo(ip.el, { opacity: 0, y: 300 }, { opacity: 1, y: 0, duration: 0.6, ease: "power3.out" }, 2.9);
        const nt = K.h("div", "n-notes", `<h3>Annonce Vignols</h3><div class="dt">22:47</div><div style="font-size:40px;line-height:1.4"><span class="t"></span><span class="cur"></span></div>`, ip.screen);
        const tt = K.$(".t", nt);
        tl.fromTo(K.$(".cur", nt), { opacity: 1 }, { opacity: 0, duration: 0.3, repeat: 9, yoyo: true, ease: "steps(1)" }, 3.2);
        let t0 = 3.4;
        ["Charmante maison idéalement située…", "Belle maison familiale avec ter…"].forEach((d) => {
          const P1 = { n: 0 }, P2 = { n: d.length };
          tl.to(P1, { n: d.length, duration: 0.7, ease: "none", onUpdate: () => { tt.textContent = d.slice(0, Math.round(P1.n)); } }, t0);
          for (let x = 0; x < 6; x++) K.sfx(t0 + x * 0.11, "type", 0.05, 0, { f: 2800 + x * 60 });
          tl.to(P2, { n: 0, duration: 0.35, ease: "none", onUpdate: () => { tt.textContent = d.slice(0, Math.round(P2.n)); } }, t0 + 0.9);
          t0 += 1.35;
        });
        N.out(cap, 5.8, { y: -10, d: 0.2 });
        const c2 = N.cap("6 heures par mois.<br>Le soir.", { top: "150px" }, 6.0, { dark: true });
        K.sfx(6.0, "thump", 0.3);
        N.out([c2, ip.el], 7.6, { y: 60, d: 0.4 });
        const h = N.head(["LIMO L’ÉCRIT", "EN 2 MINUTES<span class='v'>.</span>"], { top: "150px", fontSize: "70px" }, 7.9, { bar: false });
        glow(140, 520, 800, 7.9);
        const ph = A.phone({ left: "260px", top: "470px", width: "560px" }, { time: "10:05", tab: 3 });
        const pics = [0, 1, 2].map((i) => `<div class="a-ph" style="flex:1;height:150px">${K.houseArt(160, 150, "pa" + i)}</div>`).join("");
        const p1 = A.page(ph, `<div class="a-back">${K.icon("chev")}Nouvelle annonce</div><div style="display:flex;gap:10px;margin-bottom:16px">${pics}</div>` +
          A.row("home", "v", "Maison · Vignols", "120 m² · 4 chambres") + A.row("pin", "t", "Terrain 1 500 m²", "Au calme, sans vis-à-vis") + A.row("euro", "o", "245 000 €", "Honoraires inclus · DPE D") +
          `<div class="a-btn" style="margin-top:14px">${K.icon("sparkles")}Générer l’annonce</div>`);
        const p2 = A.page(ph, `<div class="a-back">${K.icon("chev")}Annonce</div><div class="a-gen"><i></i><i></i><i></i>LIMO rédige…</div>
<div class="a-card" style="padding:22px 24px;margin-top:12px"><div class="ti" style="font-family:'Source Serif 4',serif;font-size:32px;font-weight:600;line-height:1.2;min-height:76px"></div><div class="bo" style="margin-top:10px;font-size:21px;line-height:1.45;color:#3a3a3c;min-height:150px"></div>
<div class="lg" style="margin-top:12px;padding-top:12px;border-top:1px solid #efeff4;font-size:17px;line-height:1.4;color:#6e6e80">245 000 € honoraires inclus, dont 5 % TTC à la charge de l’acquéreur (233 333 € hors honoraires) · DPE D · GES B</div></div>
<div class="cs" style="display:flex;gap:10px;margin-top:14px"><span class="a-tag t">${K.icon("check")}Mentions légales</span><span class="a-tag">${K.icon("check")}Prête à publier</span></div>`);
        A.enter(ph, 8.1);
        K.$$(".a-row", p1).forEach((r, i) => K.fin(r, 9.0 + i * 0.15, { y: 16, d: 0.3 }));
        A.tap(ph, 264, 890, 10.4);
        A.go(ph, p1, p2, 10.6);
        K.$$(".a-gen i", p2).forEach((d, i) => tl.fromTo(d, { opacity: 0.25 }, { opacity: 1, duration: 0.2, yoyo: true, repeat: 3 }, 10.9 + i * 0.1));
        K.type(K.$(".ti", p2), "Maison familiale au calme avec grand terrain", 11.4, 0.8, 0.05);
        K.type(K.$(".bo", p2), "À Vignols, 120 m² lumineux, 4 chambres, séjour traversant ouvert sur un terrain de 1 500 m² sans vis-à-vis. À 15 min de Brive.", 12.2, 1.6, 0.04);
        N.hide(K.$(".lg", p2));
        K.fin(K.$(".lg", p2), 13.9, { y: 8 });
        N.hide(K.$(".cs", p2));
        tl.set(K.$(".cs", p2), { opacity: 1 }, 14.3);
        K.pop(K.$$(".cs .a-tag", p2), 14.3, { st: 0.12 });
        K.sfx(14.3, "success", 0.24);
        const f1 = A.float(A.gain("timer", "v", "2 min", "au lieu de 45"), { left: "30px", top: "760px" }, 14.8);
        const f2 = A.float(A.gain("shield", "t", "Conforme", "mentions légales"), { left: "590px", top: "1420px" }, 15.4);
        const n1 = A.over(N.notif({ title: "LINKEDIN", time: "10:08", text: "Post « Nouveauté à Vignols » publié.", snd: "success", g: 0.24 }, { left: "90px", top: "600px" }, 16.8));
        N.out([h, f1, f2, n1], 19.2, { y: -30 });
        A.leave(ph, 19.2);
        const g = gains(19.9, [
          { k: "TEMPS GAGNÉ", n: 344, f: """ + MIN + r""", d: "par mois (8 annonces × 43 min) : <b>tes soirées te reviennent</b>." },
          { k: "TON TEMPS VAUT", c: "t", n: 860, f: (v) => "≈ " + Math.round(v / 10) * 10 + " €", d: "5 h 44 × 150 €/h, le taux horaire indicatif d’un agent." },
          """ + PRIX + r""",
        ]);
        N.out(g, 25.6, { y: -30 });
        window.__TE = 26.0;
        fin(26.0);
""")

# ---------------------------------------------------------------- 4 · qui va vendre dans ton secteur (détecteur)
FILMS["pub30-04-qui-va-vendre"] = ("Agent immobilier, tu sais qui va vendre dans ton secteur ?", 30.0, "", r"""
        glow(-300, 300, 1100, 0);
        const hk = N.hook(["<span class='kk'>AGENT IMMOBILIER,</span>", "TU SAIS QUI", "VA VENDRE DANS", "<span class='hl'>TON SECTEUR ?</span>"], { top: "470px", fontSize: "88px" });
        const s1 = N.text("ctr n-body", "Pendant que tu boîtes<br><b>au hasard…</b>", { top: "980px", fontSize: "48px" }, 0.9);
        N.out([hk, s1], 2.7, { y: -40 });
        const cap = N.cap("Le boîtage du samedi.", { top: "150px" }, 2.9);
        const L = [["image", "o", "500 flyers distribués"], ["timer", "v", "4 heures de marche"], ["phone", "r", "2 appels… dont 1 locataire"]];
        const cards = L.map((l, i) => {
          const c = N.ab("n-card", `<div style="display:flex;align-items:center;gap:24px;padding:30px 36px"><span class="a-ic ${l[1]}" style="width:84px;height:84px;border-radius:24px">${K.icon(l[0])}</span><b style="font-size:44px;font-weight:700">${l[2]}</b></div>`, { left: "90px", top: 480 + i * 210 + "px", width: "900px", fontFamily: "Inter, sans-serif", color: "#1b1f4b" });
          N.hide(c);
          K.fin(c, 3.2 + i * 0.5, { y: 30, d: 0.4 });
          K.sfx(3.2 + i * 0.5, "pop", 0.16, 0, { f: 600 + i * 100 });
          return c;
        });
        tl.to(cards[2], { x: 10, duration: 0.05, ease: "none", yoyo: true, repeat: 5 }, 4.4);
        K.sfx(4.4, "buzz", 0.14);
        N.out(cap, 5.4, { y: -10, d: 0.2 });
        const c2 = N.cap("500 boîtes.<br>0 mandat.", { top: "150px" }, 5.6, { dark: true });
        K.sfx(5.6, "thump", 0.3);
        N.out([c2, ...cards], 7.6, { y: 60, d: 0.4 });
        const h = N.head(["LIMO TE DIT", "QUI APPELER<span class='v'>.</span>"], { top: "150px", fontSize: "70px" }, 7.9, { bar: false });
        glow(140, 520, 800, 7.9);
        const ph = A.phone({ left: "260px", top: "470px", width: "560px" }, { time: "9:12", tab: 3 });
        const roads = `<svg viewBox="0 0 480 380" width="100%" height="100%" style="position:absolute;inset:0"><rect width="480" height="380" fill="#eef0f7"/><path d="M0 110 C120 90 220 150 320 120 S440 60 480 70" stroke="#fff" stroke-width="22" fill="none"/><path d="M90 0 C120 120 80 240 150 380" stroke="#fff" stroke-width="16" fill="none"/><path d="M350 0 C320 130 380 250 330 380" stroke="#fff" stroke-width="16" fill="none"/><path d="M0 290 C150 260 300 310 480 260" stroke="#fff" stroke-width="14" fill="none"/><circle cx="410" cy="330" r="40" fill="#dff3ee"/><circle cx="40" cy="200" r="30" fill="#dff3ee"/></svg>`;
        const P = [[70, 60, 0], [170, 180, 1], [260, 70, 0], [380, 190, 1], [120, 310, 0], [290, 270, 1], [440, 300, 0]];
        const p1 = A.page(ph, `<div class="a-back">${K.icon("chev")}Détecteur</div><div class="a-map">${roads}${P.map((q) => `<span class="a-pin${q[2] ? " hot" : ""}" style="left:${q[0]}px;top:${q[1]}px">${q[2] ? '<i class="rg"></i>' : ""}</span>`).join("")}</div><div class="a-h2">3 vendeurs probables</div>` +
          A.row("home", "v", "Maison · Allassac", "Signaux de vente repérés", "", `<span class="a-tag t">Fort</span>`) + A.row("home", "v", "Longère · Voutezac", "Signaux de vente repérés", "", `<span class="a-tag t">Fort</span>`) + A.row("home", "g", "Appartement · Brive", "À surveiller", "", `<span class="a-tag o">Moyen</span>`));
        const p2 = A.page(ph, `<div class="a-back">${K.icon("chev")}Maison · Allassac</div><div class="a-ph" style="height:220px;margin-bottom:16px">${K.houseArt(480, 220, "pd")}</div>` +
          A.row("radar", "v", "Signal de vente fort", "Repéré cette semaine") + A.row("pin", "t", "Ton secteur", "Tu y as déjà vendu 3 biens") + A.row("clock", "o", "Meilleur moment", "Appeler avant vendredi") +
          `<div style="display:flex;gap:12px;margin-top:14px"><div class="a-btn" style="flex:1">${K.icon("phone")}Appeler</div><div class="a-btn l" style="flex:1">${K.icon("msg")}Message</div></div>`);
        A.enter(ph, 8.1);
        K.$$(".a-pin", p1).forEach((q, i) => { tl.fromTo(q, { scale: 0 }, { scale: 1, duration: 0.25, ease: "back.out(2.5)" }, 9.1 + i * 0.1); });
        K.$$(".a-pin.hot .rg", p1).forEach((q, i) => tl.fromTo(q, { scale: 1, opacity: 0.9 }, { scale: 2.6, opacity: 0, duration: 0.9, ease: "power2.out", repeat: 2 }, 9.9 + i * 0.3));
        K.sfx(9.9, "sonar", 0.16);
        K.$$(".a-row", p1).forEach((r, i) => K.fin(r, 10.2 + i * 0.15, { y: 16, d: 0.3 }));
        A.tap(ph, 264, 640, 11.6);
        A.go(ph, p1, p2, 11.8);
        K.$$(".a-row", p2).forEach((r, i) => K.fin(r, 12.3 + i * 0.2, { y: 16, d: 0.3 }));
        const f1 = A.float(A.gain("phone", "v", "5 appels", "ciblés, pas 500 flyers"), { left: "30px", top: "760px" }, 13.4);
        A.tap(ph, 140, 1010, 14.6);
        K.sfx(14.8, "beep", 0.12, 0, { f: 440, d: 0.3 });
        const n1 = A.over(N.notif({ title: "AGENDA", time: "9:20", text: "Estimation maison Allassac : samedi à 11 h.", snd: "success", g: 0.28 }, { left: "90px", top: "600px" }, 15.6));
        const f2 = A.float(A.gain("calc", "t", "+ 1 RDV", "avant les autres agences"), { left: "590px", top: "1420px" }, 16.4);
        N.out([h, f1, f2, n1], 19.2, { y: -30 });
        A.leave(ph, 19.2);
        const g = gains(19.9, [
          { k: "TEMPS GAGNÉ", n: 240, f: """ + MIN + r""", d: "de boîtage au hasard <b>chaque semaine</b>." },
          { k: "ARGENT", c: "t", n: 7500, f: (v) => "+ " + K.eur(v), d: "<b>1 mandat trouvé avant les autres</b> = les honoraires d’une vente." },
          """ + PRIX + r""",
        ]);
        N.out(g, 25.6, { y: -30 });
        window.__TE = 26.0;
        fin(26.0);
""")

# ---------------------------------------------------------------- 5 · ton CRM dort (brief du matin)
FILMS["pub30-05-crm-dort"] = ("Agent immobilier, ton CRM dort. Pas toi.", 30.0, """
      #big { top: 560px; font-family: "Montserrat Hook", Montserrat, sans-serif; font-weight: 800; font-size: 220px; color: var(--navy); line-height: 1; }
      #big small { font-size: 70px; color: var(--mut); }
""", r"""
        glow(-300, 300, 1100, 0);
        const hk = N.hook(["<span class='kk'>AGENT IMMOBILIER,</span>", "TON CRM DORT<span class='v'>.</span>", "<span class='hl'>PAS TOI.</span>"], { top: "520px", fontSize: "100px" });
        const s1 = N.text("ctr n-body", "Il stocke tes contacts.<br><b>Il ne te dit jamais quoi faire.</b>", { top: "940px", fontSize: "48px" }, 0.9);
        N.out([hk, s1], 2.7, { y: -40 });
        const cap = N.cap("842 contacts dans ton CRM.", { top: "150px" }, 2.9);
        const big = N.ab("ctr", `<span>0</span><small> rappelés</small>`, {});
        big.id = "big";
        N.hide(big);
        tl.set(big, { opacity: 1 }, 3.4);
        K.count(K.$("span", big), 12, 3.4, 1.0, (v) => String(Math.round(v)), { ticks: 8 });
        const bar = N.ab("a-bar", `<i></i>`, { left: "140px", top: "880px", width: "800px", height: "26px", borderRadius: "13px" });
        N.hide(bar);
        tl.set(bar, { opacity: 1 }, 3.4);
        tl.fromTo(K.$("i", bar), { scaleX: 0 }, { scaleX: 0.014, duration: 1.0, ease: "power3.out" }, 3.4);
        const s2 = N.text("ctr n-body", "ce mois-ci, sur 842.", { top: "950px", fontSize: "44px" }, 4.4);
        N.out(cap, 5.4, { y: -10, d: 0.2 });
        const c2 = N.cap("Les 830 autres attendent.<br>Et signent ailleurs.", { top: "150px" }, 5.6, { dark: true });
        K.sfx(5.6, "thump", 0.3);
        N.out([c2, big, bar, s2], 7.6, { y: 60, d: 0.4 });
        const h = N.head(["CHAQUE MATIN, LIMO", "TE DIT QUOI FAIRE<span class='v'>.</span>"], { top: "150px", fontSize: "62px" }, 7.9, { bar: false });
        glow(140, 520, 800, 7.9);
        const ph = A.phone({ left: "260px", top: "470px", width: "560px" }, { time: "8:00" });
        const ok = `<span class="ok">${K.icon("check")}</span>`;
        const p1 = A.page(ph, A.HD + `<div class="a-hello"><span>Bonjour,</span><br>Voici les actions prioritaires du jour.</div>
<div class="a-card a-prio"><span class="n">${[5, 4, 3, 2, 1, 0].map((n) => `<em style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font-style:normal">${n}</em>`).join("")}</span><span><b>Actions prioritaires</b><small>à traiter aujourd’hui</small></span></div>
<div class="a-h2">Actions du jour</div>` + A.row("refresh", "v", "Relancer 32 contacts", "Relances programmées", "09:30", ok) + A.row("home", "t", "Suivre 2 visites", "Visites à suivre", "11:00", ok) + A.row("shield", "g", "Envoyer 1 proposition", "Mandat en préparation", "14:00", ok) + A.row("star", "t", "Nouveau mandat détecté", "Opportunité à saisir", "15:30", ok) + A.row("gift", "v", "Anniversaire client", "Message à personnaliser", "17:00", ok));
        K.$(".a-prio .n", p1).style.position = "relative";
        A.enter(ph, 8.1);
        K.$$(".a-row", p1).forEach((r, i) => { K.fin(r, 9.0 + i * 0.12, { y: 16, d: 0.3 }); tl.set(K.$(".ok", r), { scale: 0 }, 0); });
        const nums = K.$$(".a-prio .n em", p1);
        nums.forEach((e, k) => tl.set(e, { opacity: k === 0 ? 1 : 0 }, 0));
        K.$$(".a-row", p1).forEach((r, i) => {
          const t = 10.8 + i * 0.9;
          A.tap(ph, 264, 590 + i * 92, t);
          tl.to(K.$(".ok", r), { scale: 1, duration: 0.25, ease: "back.out(2.4)" }, t + 0.1);
          tl.to(r, { opacity: 0.55, duration: 0.25 }, t + 0.3);
          tl.set(nums[i], { opacity: 0 }, t + 0.1);
          tl.set(nums[i + 1], { opacity: 1 }, t + 0.1);
          K.sfx(t + 0.1, "success", 0.14);
        });
        tl.to(K.$$(".a-pg > *", p1), { y: -130, duration: 0.5, ease: "power2.inOut" }, 13.7);
        const f1 = A.float(A.gain("timer", "v", "45 min", "gagnées chaque matin"), { left: "30px", top: "760px" }, 12.6);
        const n1 = A.over(N.notif({ title: "ANNIVERSAIRE", time: "17:00", text: "SMS prêt pour Mme Roy. Tu veux l’envoyer ?" }, { left: "90px", top: "600px" }, 15.2));
        const f2 = A.float(A.gain("check", "t", "5 / 5", "actions faites"), { left: "590px", top: "1420px" }, 15.6);
        N.out([h, f1, f2, n1], 19.2, { y: -30 });
        A.leave(ph, 19.2);
        const g = gains(19.9, [
          { k: "TEMPS GAGNÉ", n: 225, f: """ + MIN + r""", d: "par semaine : fini les 45 min par jour <b>à chercher quoi faire</b>." },
          { k: "ARGENT", c: "t", n: 7500, f: (v) => "+ " + K.eur(v), d: "si ce suivi te fait signer <b>1 mandat de plus par trimestre</b>." },
          """ + PRIX + r""",
        ]);
        N.out(g, 25.6, { y: -30 });
        window.__TE = 26.0;
        fin(26.0);
""")

# ---------------------------------------------------------------- 6 · avis Google
FILMS["pub30-06-avis-google"] = ("Agent immobilier, tes avis Google te coûtent des clients", 30.0, "", r"""
        glow(-300, 300, 1100, 0);
        const hk = N.hook(["<span class='kk'>AGENT IMMOBILIER,</span>", "TES AVIS GOOGLE", "TE COÛTENT", "<span class='hl'>DES CLIENTS.</span>"], { top: "470px", fontSize: "88px" });
        const s1 = N.text("ctr n-body", "Un vendeur lit tes avis<br><b>avant de t’appeler.</b>", { top: "980px", fontSize: "48px" }, 0.9);
        N.out([hk, s1], 2.7, { y: -40 });
        const cap = N.cap("Ce qu’il voit en ce moment :", { top: "150px" }, 2.9);
        const R = [["ML", "#b86e00", "Marie L.", 5, "Maison vendue en 3 semaines, merci !", "il y a 12 jours"], ["PD", "#5f6477", "Paul D.", 3, "Bon suivi, mais j’ai attendu le compte rendu de visite.", "il y a 3 semaines"]];
        const rv = R.map((r, i) => {
          const c = N.ab("n-card", `<div style="padding:30px 36px"><div style="display:flex;align-items:center;gap:20px"><div style="width:76px;height:76px;border-radius:50%;background:${r[1]};color:#fff;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:30px">${r[0]}</div><div><b style="font-size:34px">${r[2]}</b><div style="display:flex;align-items:center;gap:12px;margin-top:4px"><span class="n-stars">${K.icon("star").repeat(r[3])}</span><span style="font-size:24px;color:#6e6e73">${r[5]}</span></div></div></div><div style="margin-top:18px;font-size:34px;line-height:1.35">« ${r[4]} »</div><div class="nr" style="margin-top:16px;font-size:26px;color:#c0392b;font-weight:600">Aucune réponse du propriétaire</div></div>`, { left: "90px", top: 440 + i * 470 + "px", width: "900px" });
          N.hide(c);
          K.fin(c, 3.2 + i * 0.6, { y: 40, d: 0.45 });
          return c;
        });
        K.$$(".nr", rv[0].parentNode).forEach((n, i) => { tl.fromTo(n, { opacity: 1 }, { opacity: 0.3, duration: 0.25, yoyo: true, repeat: 3 }, 4.6 + i * 0.2); });
        K.sfx(4.6, "buzz", 0.12);
        N.out(cap, 5.4, { y: -10, d: 0.2 });
        const c2 = N.cap("Sans réponse,<br>tu as l’air absent.", { top: "150px" }, 5.6, { dark: true });
        K.sfx(5.6, "thump", 0.3);
        N.out([c2, ...rv], 7.6, { y: 60, d: 0.4 });
        const h = N.head(["LIMO RÉPOND À TES", "AVIS EN 1 MINUTE<span class='v'>.</span>"], { top: "150px", fontSize: "62px" }, 7.9, { bar: false });
        glow(140, 520, 800, 7.9);
        const ph = A.phone({ left: "260px", top: "470px", width: "560px" }, { time: "12:30", tab: 4 });
        const st = (n) => `<span class="a-stars">${K.icon("star").repeat(n)}</span>`;
        const p1 = A.page(ph, `<div class="a-back">${K.icon("chev")}Avis Google</div>
<div class="a-card" style="display:flex;align-items:center;gap:20px;padding:22px 24px;margin-bottom:16px"><b style="font-size:58px;font-weight:700">4,8</b><span>${st(5)}<small style="display:block;margin-top:6px;font-size:20px;color:#6e6e80">37 avis · 3 sans réponse</small></span></div>` +
          A.row("users", "o", "Marie L. · 5 étoiles", "Maison vendue en 3 semaines…", "", `<span class="a-tag">Prête</span>`) + A.row("users", "g", "Paul D. · 3 étoiles", "Bon suivi, mais j’ai attendu…", "", `<span class="a-tag">Prête</span>`) + A.row("users", "t", "Julie R. · 5 étoiles", "Très professionnel !", "", `<span class="a-tag">Prête</span>`) +
          `<div class="a-btn" style="margin-top:14px"><span class="bt">${K.icon("send")}Publier les 3 réponses</span></div>`);
        const p2 = A.page(ph, `<div class="a-back">${K.icon("chev")}Paul D.</div><div class="a-card a-msg">${st(3)}<div style="margin-top:8px">« Bon suivi, mais j’ai attendu le compte rendu de visite. »</div></div>
<div class="a-h2">Réponse proposée par LIMO</div><div class="a-card a-msg" style="min-height:250px"><span class="ty"></span></div>
<div class="a-btn" style="margin-top:16px"><span class="bt">${K.icon("send")}Publier la réponse</span></div>`);
        A.enter(ph, 8.1);
        K.$$(".a-row", p1).forEach((r, i) => K.fin(r, 9.0 + i * 0.15, { y: 16, d: 0.3 }));
        A.tap(ph, 264, 520, 10.4);
        A.go(ph, p1, p2, 10.6);
        K.type(K.$(".ty", p2), "Merci Paul pour votre retour et votre confiance ! Vous avez raison : le compte rendu aurait dû vous parvenir plus vite. C’est corrigé, et je reste disponible pour la suite de votre projet.", 11.2, 2.2, 0.04);
        A.tap(ph, 264, 900, 13.7);
        const b2 = K.$(".a-btn", p2);
        tl.to(b2, { backgroundColor: "#2cc4b5", duration: 0.25 }, 13.8);
        tl.set(K.$(".bt", b2), { innerHTML: `${K.icon("check")}Réponse publiée` }, 13.8);
        K.sfx(13.8, "success", 0.26);
        const f1 = A.float(A.gain("timer", "v", "1 min", "par réponse"), { left: "30px", top: "760px" }, 14.3);
        A.go(ph, p2, p1, 15.0, { back: true });
        A.tap(ph, 264, 900, 15.9);
        const b1 = K.$(".a-btn", p1);
        tl.to(b1, { backgroundColor: "#2cc4b5", duration: 0.25 }, 16.0);
        tl.set(K.$(".bt", b1), { innerHTML: `${K.icon("check")}3 réponses publiées` }, 16.0);
        K.sfx(16.0, "success", 0.24);
        const f2 = A.float(A.gain("star", "t", "100 %", "d’avis répondus"), { left: "590px", top: "1420px" }, 16.5);
        N.out([h, f1, f2], 19.2, { y: -30 });
        A.leave(ph, 19.2);
        const g = gains(19.9, [
          { k: "TEMPS GAGNÉ", n: 90, f: """ + MIN + r""", d: "par mois : des réponses <b>soignées, en 1 clic</b>." },
          { k: "CONFIANCE", c: "t", v: "4,8 ★", d: "Des avis tous répondus : <b>le vendeur t’appelle, toi</b>." },
          """ + PRIX + r""",
        ]);
        N.out(g, 25.6, { y: -30 });
        window.__TE = 26.0;
        fin(26.0);
""")

if __name__ == "__main__":
    for name, (title, dur, css, body) in FILMS.items():
        html = SHELL.format(title=title, faces=FACES, css=css.strip("\n"), body=(COMMON + body).strip("\n"), dur=dur, name=name)
        pathlib.Path(f"reels/{name}.html").write_text(html, encoding="utf-8")
        print("reels/" + name + ".html")
