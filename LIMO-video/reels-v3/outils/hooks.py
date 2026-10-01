"""Série « hooks » : 10 Reels LIMO dont l'accroche est lisible dès la première image.

Charte « naturelle » (voir outils/naturel.py). Données fictives.
Usage : python3 outils/hooks.py   (réécrit reels/hook-*.html)
"""
import pathlib

from naturel import FACES as _FACES, SHELL

# Montserrat 800 embarquée localement : l'accroche doit être dans la bonne police dès l'image 1
FACES = _FACES + """      @font-face { font-family: "Montserrat Hook"; src: url("assets/fonts/montserrat-latin-800-normal.woff2") format("woff2"); font-weight: 800; font-style: normal; }\n"""

FILMS = {}

# ---------------------------------------------------------------- 1 · l'IA va remplacer les agents
FILMS["hook-01-ia-remplace"] = ("L’IA va remplacer les agents immo", 14.6, "", """
        const chip = N.chip(`${K.icon("alert")}AGENTS IMMO`, { top: "300px" });
        const hk = N.hook(["L’IA VA", "REMPLACER", "<span class='st'>LES AGENTS<i></i></span>", "<span class='st'>IMMO<i></i></span>"], { top: "400px", fontSize: "116px" }, { st: 1.0 });
        const h2 = N.head(["SEULEMENT CEUX", "QUI NE L’UTILISENT PAS<span class='v'>.</span>"], { top: "1000px", fontSize: "70px" }, 1.6);
        K.sfx(1.6, "thump", 0.3);
        N.out([chip, hk, h2], 4.0, { y: -40 });
        const cap = N.cap("L’utiliser, c’est simple :", { top: "150px" }, 4.3);
        const ph = N.phoneLimo({ left: "213px", top: "560px" }, 4.4);
        const n1 = N.notif({ title: "ANNONCE", text: "Maison à Allassac : annonce rédigée, mentions légales incluses." }, { left: "90px", top: "640px" }, 5.2);
        const n2 = N.notif({ title: "RELANCE", text: "M. Vidal : SMS de relance prêt, tu n’as qu’à valider.", g: 0.2 }, { left: "90px", top: "860px" }, 6.1);
        const n3 = N.notif({ title: "ESTIMATION", text: "Appartement Brive centre : avis de valeur prêt à envoyer.", snd: "success", g: 0.28 }, { left: "90px", top: "1080px" }, 7.0);
        N.out([cap, ph, n1, n2, n3], 8.9, { y: -30 });
        const c2 = N.cap("L’IA ne te remplace pas.<br>Elle bosse pour toi.", { top: "760px" }, 9.2, { dark: true });
        N.out(c2, 10.8, { y: -20 });
        window.__TE = 11.0;
        N.outro(11.0, "comment");
""")

# ---------------------------------------------------------------- 2 · 3 agences
FILMS["hook-02-trois-agences"] = ("Ton vendeur a appelé 3 agences", 15.2, """
      .ag { left: 90px; width: 900px; height: 170px; display: flex; align-items: center; gap: 28px; padding: 0 40px; }
      .ag .av { flex: none; width: 88px; height: 88px; border-radius: 24px; display: flex; align-items: center; justify-content: center; color: #fff; font-family: Montserrat, sans-serif; font-weight: 800; font-size: 36px; }
      .ag b { display: block; font-size: 38px; font-weight: 700; color: #1c1c1e; }
      .ag small { display: block; margin-top: 6px; font-size: 30px; font-weight: 600; }
      .ag .tm { margin-left: auto; font-family: Montserrat, sans-serif; font-weight: 800; font-size: 40px; }
""", """
        const chip = N.chip(`${K.icon("phone")}19 h 12 · UNE DEMANDE D’ESTIMATION`, { top: "300px" });
        const hk = N.hook(["TON VENDEUR", "A APPELÉ", "<span class='hl'>3 AGENCES.</span>"], { top: "440px", fontSize: "106px" });
        const s1 = N.text("ctr n-body", "<b>Devine laquelle il a choisie.</b>", { top: "860px", fontSize: "54px" }, 1.1);
        N.out([chip, hk, s1], 2.9, { y: -40 });
        const cap = N.cap("Même demande. Même soir.", { top: "150px" }, 3.1);
        const A = [["A", "#5f6477", "Agence du centre", "Rappelle 2 jours après", "J+2", "#c0282d"], ["B", "#5f6477", "Agence de la gare", "Rappelle le lendemain", "+14 h", "#9a5400"], ["L", "#6b4fe0", "Toi + LIMO", "Réponse prête, envoyée", "4 min", "#15877d"]];
        const rows = A.map((a, i) => {
          const r = N.ab("n-card ag", `<div class="av" style="background:${a[1]}">${a[0]}</div><div><b>${a[2]}</b><small style="color:${a[5]}">${a[3]}</small></div><span class="tm" style="color:${a[5]}">${a[4]}</span>`, { top: 440 + i * 210 + "px" });
          N.hide(r);
          K.fin(r, 3.4 + i * 0.45, { y: 30, d: 0.4 });
          K.sfx(3.4 + i * 0.45, "pop", 0.14, 0, { f: 600 + i * 120 });
          return r;
        });
        tl.to([rows[0], rows[1]], { opacity: 0.8, scale: 0.97, duration: 0.35 }, 5.3);
        tl.to(rows[2], { scale: 1.04, boxShadow: "0 24px 60px rgba(107,79,224,.35)", duration: 0.35, ease: "back.out(2)" }, 5.3);
        K.sfx(5.3, "success", 0.26);
        const ok = N.chip(`${K.icon("check")}Rendez-vous d’estimation calé`, { top: "1130px" }, 5.7);
        N.out(cap, 5.9, { y: -10, d: 0.2 });
        const c2 = N.cap("La première qui répond.<br>C’est tout.", { top: "150px" }, 6.1, { dark: true });
        K.sfx(6.1, "thump", 0.28);
        N.out([c2, ...rows, ok], 8.0, { y: 40 });
        const h = N.head(["LIMO PRÉPARE", "TA RÉPONSE<span class='v'>.</span>"], { top: "190px", fontSize: "92px" }, 8.3);
        const ph = N.phoneLimo({ left: "213px", top: "580px" }, 8.6);
        const n1 = N.notif({ title: "NOUVEAU VENDEUR", time: "19:12", text: "Mme Garnier veut faire estimer sa maison. Réponse prête : tu valides, c’est envoyé." }, { left: "90px", top: "700px" }, 9.4);
        N.out([h, ph, n1], 11.4, { y: -30 });
        window.__TE = 11.6;
        N.outro(11.6, "essai");
""")

# ---------------------------------------------------------------- 3 · donne-moi 10 secondes
FILMS["hook-03-dix-secondes"] = ("Donne-moi 10 secondes", 14.0, """
      #ring { left: 390px; top: 300px; width: 300px; height: 300px; }
      #ring svg { width: 300px; height: 300px; transform: rotate(-90deg); }
      #ring .n { position: absolute; inset: 0; display: flex; align-items: center; justify-content: center; font-family: Montserrat, sans-serif; font-weight: 800; font-size: 128px; color: var(--navy); }
      #ring .n span { position: absolute; }
""", """
        const hk = N.hook(["AGENT IMMO ?", "DONNE-MOI", "<span class='hl'>10 SECONDES.</span>"], { top: "480px", fontSize: "98px" });
        const s1 = N.text("ctr n-body", "Je te montre ta matinée <b>déjà faite</b>.", { top: "880px", fontSize: "46px" }, 0.9);
        N.out([hk, s1], 2.0, { y: -40 });
        const ring = N.ab("", `<svg viewBox="0 0 100 100"><circle cx="50" cy="50" r="44" fill="#fff" stroke="#e7e1fa" stroke-width="8"/><circle class="p" cx="50" cy="50" r="44" fill="none" stroke="#6b4fe0" stroke-width="8" stroke-linecap="round" pathLength="1" stroke-dasharray="1" stroke-dashoffset="0"/></svg><div class="n">${Array.from({ length: 11 }, (_, k) => `<span>${10 - k}</span>`).join("")}</div>`, {});
        ring.id = "ring";
        N.hide(ring);
        K.pop(ring, 2.2, { s: 0.7 });
        const T0 = 2.4, STEP = 0.6;
        tl.fromTo(K.$(".p", ring), { strokeDashoffset: 0 }, { strokeDashoffset: 1, duration: STEP * 10, ease: "none" }, T0);
        K.$$(".n span", ring).forEach((s, k) => {
          tl.set(s, { opacity: 0 }, 0);
          tl.set(s, { opacity: 1 }, k === 0 ? 2.2 : T0 + k * STEP);
          if (k < 10) tl.set(s, { opacity: 0 }, T0 + (k + 1) * STEP);
          if (k > 0) K.sfx(T0 + k * STEP, "tick", 0.16, 0, { f: 1500 + k * 90 });
        });
        const L = ["Brief du jour prêt", "3 relances préparées", "Annonce Brive rédigée", "Avis Google : réponse prête", "Avis de valeur Vignols", "Post LinkedIn publié"];
        const card = N.ab("n-card", L.map((l) => `<div class="n-row"><span style="color:#1c1c1e">${l}</span><i class="ok" style="margin-left:auto">${K.icon("check")}</i></div>`).join(""), { left: "110px", top: "680px", width: "860px" });
        N.hide(card);
        K.fin(card, 2.4, { y: 40, d: 0.4 });
        K.$$(".n-row", card).forEach((r, i) => {
          const t = 2.9 + i * 0.85;
          tl.set(r, { opacity: 0.25 }, 0);
          tl.to(r, { opacity: 1, duration: 0.2 }, t);
          tl.fromTo(K.$(".ok", r), { scale: 0 }, { scale: 1, duration: 0.25, ease: "back.out(2.4)" }, t);
          K.sfx(t, "success", 0.12);
        });
        const c1 = N.cap("0 seconde de ton temps.", { top: "1420px" }, 8.6, { dark: true });
        K.sfx(8.6, "thump", 0.3);
        N.out([ring, card, c1], 10.0, { y: -30 });
        window.__TE = 10.4;
        N.outro(10.4, "demo");
""")

# ---------------------------------------------------------------- 4 · 3 red flags
FILMS["hook-04-red-flags"] = ("3 red flags qui font fuir tes vendeurs", 15.4, """
      .rf { left: 90px; width: 900px; height: 280px; }
      .rf .fc { position: absolute; inset: 0; display: flex; align-items: center; gap: 30px; padding: 0 40px; }
      .rf .nb { font-family: Montserrat, sans-serif; font-weight: 800; font-size: 28px; color: #6e6e73; }
      .rf .tx { font-size: 40px; line-height: 1.25; font-weight: 600; color: #1c1c1e; }
      .rf .g .tx { font-size: 36px; }
      .rf .g .tx b { color: var(--vio); }
""", """
        const chip = N.chip(`${K.icon("alert")}LE N°2, TOUT LE MONDE LE FAIT`, { top: "320px" });
        const hk = N.hook(["3 RED FLAGS", "QUI FONT FUIR", "<span class='hl'>TES VENDEURS.</span>"], { top: "460px", fontSize: "90px" });
        N.out([chip, hk], 2.2, { y: -40 });
        const cap = N.cap("Sois honnête.", { top: "150px" }, 2.4);
        const F = [["Tu rappelles le lendemain.", "LIMO te prépare la réponse <b>en 1 minute</b>."], ["Ton annonce ressemble à toutes les autres.", "LIMO rédige une annonce <b>unique</b>, mentions légales incluses."], ["Tu oublies de relancer.", "LIMO te dit <b>qui relancer, et quand</b>."]];
        const cards = F.map((f, i) => {
          const c = N.ab("n-card rf", `<div class="fc r"><span class="n-flag" style="background:#e5484d">${K.icon("alert")}</span><div><div class="nb">RED FLAG N°${i + 1}</div><div class="tx">${f[0]}</div></div></div><div class="fc g"><span class="n-flag" style="background:#2cc4b5">${K.icon("check")}</span><div><div class="nb" style="color:#15877d">AVEC LIMO</div><div class="tx">${f[1]}</div></div></div>`, { top: 420 + i * 320 + "px" });
          N.hide(c);
          const t = 2.7 + i * 2.2;
          K.fin(c, t, { y: 40, d: 0.4 });
          K.sfx(t, "buzz", 0.12);
          const g = K.$(".g", c), r = K.$(".r", c);
          tl.set(g, { opacity: 0 }, 0);
          tl.to(r, { opacity: 0, y: -20, duration: 0.25, ease: "power2.in" }, t + 1.3);
          tl.fromTo(g, { opacity: 0, y: 20 }, { opacity: 1, y: 0, duration: 0.3, ease: "power3.out" }, t + 1.5);
          K.sfx(t + 1.5, "success", 0.2);
          return c;
        });
        N.out(cap, 9.3, { y: -10, d: 0.2 });
        const c2 = N.cap("T’en as combien ?<br>Dis-le en commentaire.", { top: "150px" }, 9.5, { dark: true });
        N.out([c2, ...cards], 11.6, { y: 40 });
        window.__TE = 11.8;
        N.outro(11.8, "comment");
""")

# ---------------------------------------------------------------- 5 · ton concurrent
FILMS["hook-05-ton-concurrent"] = ("Ton concurrent utilise déjà ça", 14.6, "", """
        const ph = N.ab("n-phone", `<img src="assets/img/phone-limo.png" alt="L’application LIMO sur téléphone" />`, { left: "213px", top: "1050px" });
        ph.setAttribute("data-layout-allow-overflow", "");
        tl.fromTo(ph, { filter: "blur(26px)", y: 0, rotation: 4 }, { filter: "blur(26px)", y: -30, rotation: 2, duration: 3.2, ease: "sine.inOut" }, 0);
        const hk = N.hook(["TON CONCURRENT", "UTILISE DÉJÀ", "<span class='hl'>ÇA.</span>"], { top: "340px", fontSize: "88px" });
        const hand = N.ab("ctr n-hand", "(et il ne te le dira pas)", { top: "680px", fontSize: "72px", transform: "rotate(-3deg)" });
        hand.setAttribute("data-layout-allow-overlap", "");
        N.hide(hand);
        tl.fromTo(hand, { opacity: 0, scale: 0.8 }, { opacity: 1, scale: 1, duration: 0.35, ease: "back.out(2)" }, 1.0);
        K.sfx(1.0, "pop", 0.16);
        const c1 = N.cap("Tu veux voir ?", { top: "150px" }, 2.3, { dark: true });
        N.out([hk, hand, c1], 3.2, { y: -40 });
        tl.to(ph, { y: -490, rotation: -2, filter: "blur(0px)", duration: 0.8, ease: "power3.inOut" }, 3.3);
        K.sfx(3.3, "whoosh", 0.2, 0, { d: 0.6, f0: 200, f1: 1800, pk: 0.6 });
        K.sfx(3.9, "shutter", 0.2);
        const h = N.head(["SON BRAS DROIT", "S’APPELLE LIMO<span class='v'>.</span>"], { top: "170px", fontSize: "80px" }, 3.9, { bar: false });
        const n1 = N.notif({ title: "BRIEF DU MATIN", time: "8:00", text: "5 actions aujourd’hui. On commence par M. Albert." }, { left: "90px", top: "660px" }, 4.8);
        const n2 = N.notif({ title: "DÉTECTEUR", text: "Maison à Voutezac : signaux de vente repérés.", g: 0.2 }, { left: "90px", top: "880px" }, 5.8);
        const n3 = N.notif({ title: "RELANCE", text: "Famille Martin : c’est le moment d’appeler.", snd: "success", g: 0.26 }, { left: "90px", top: "1100px" }, 6.8);
        N.out([h, ph, n1, n2, n3], 8.9, { y: -30 });
        const c2 = N.cap("Maintenant, tu sais.", { top: "800px" }, 9.2, { dark: true });
        K.sfx(9.2, "thump", 0.3);
        N.out(c2, 10.6, { y: -20 });
        window.__TE = 10.8;
        N.outro(10.8, "dm");
""")

# ---------------------------------------------------------------- 6 · « elle vaut combien ? »
FILMS["hook-06-elle-vaut-combien"] = ("Elle vaut combien, ma maison ?", 15.2, """
      .est { font-family: Montserrat, sans-serif; font-weight: 800; font-size: 50px; color: var(--navy); white-space: nowrap; }
""", """
        const hk = N.hook(["« ELLE VAUT", "COMBIEN,", "<span class='hl'>MA MAISON ? »</span>"], { top: "440px", fontSize: "92px" });
        const s1 = N.text("ctr n-body", "Ton vendeur. En pleine visite.<br><b>Il attend ta réponse. Là.</b>", { top: "820px", fontSize: "46px" }, 0.9);
        N.out([hk, s1], 2.8, { y: -40 });
        const cap = N.cap("Tu sors ton téléphone…", { top: "150px" }, 3.0);
        const ip = N.iphone({ left: "110px", top: "400px", width: "860px", height: "1480px" }, "15:24");
        N.hide(ip.el);
        tl.fromTo(ip.el, { opacity: 0, y: 300 }, { opacity: 1, y: 0, duration: 0.6, ease: "power3.out" }, 3.0);
        K.h("div", "n-mhead", `<div class="av" style="background:#fff;padding:6px"><img src="assets/img/limo-house-ad.png" alt="" style="width:100%;height:100%;object-fit:contain" /></div><b>LIMO</b>`, ip.screen);
        const th = K.h("div", "n-thread", null, ip.screen);
        K.h("div", "n-day", "Aujourd’hui · 15:24", th);
        const b1 = K.h("div", "n-bub out", "Maison 120 m², Vignols, terrain 1 500 m², 4 ch., DPE D. Estimation ?", th);
        N.hide(b1);
        K.fin(b1, 3.6, { y: 20, d: 0.35 });
        K.sfx(3.6, "send", 0.22);
        const dots = K.h("div", "n-dots", "<i></i><i></i><i></i>", th);
        N.hide(dots);
        tl.set(dots, { opacity: 1 }, 4.1);
        K.$$("i", dots).forEach((d, i) => tl.fromTo(d, { y: 0 }, { y: -8, duration: 0.14, yoyo: true, repeat: 3, ease: "sine.inOut" }, 4.15 + i * 0.07));
        tl.set(dots, { display: "none" }, 4.8);
        const b2 = K.h("div", "n-bub in", `<div style="font-size:30px;font-weight:600;color:#6e6e73">Fourchette estimée</div><div class="est"><span class="a">0 €</span> – <span class="b">0 €</span></div><div style="margin-top:10px;font-size:32px">Appuyée sur 3 ventes comparables du secteur. Avis de valeur prêt à envoyer.</div>`, th);
        b2.style.maxWidth = "92%";
        N.hide(b2);
        K.fin(b2, 4.8, { y: 20, d: 0.35 });
        K.sfx(4.8, "receive", 0.28);
        K.count(K.$(".a", b2), 212000, 5.0, 1.1, K.eur, { ticks: 10 });
        K.count(K.$(".b", b2), 228000, 5.0, 1.1, K.eur, { ticks: 0 });
        N.out(cap, 5.4, { y: -10, d: 0.2 });
        const c2 = N.cap("…et tu réponds en 30 secondes.", { top: "150px" }, 5.6, { dark: true });
        K.sfx(6.2, "success", 0.24);
        const fx = N.text("ctr n-body", "Exemple fictif", { top: "1830px", fontSize: "22px" }, 5.0);
        N.out([c2, ip.el, fx], 8.4, { y: 60, d: 0.4 });
        const h = N.head(["TU ASSURES", "DEVANT TON VENDEUR<span class='v'>.</span>"], { top: "620px", fontSize: "82px" }, 8.8);
        const s2 = N.text("ctr n-body", "Estimation argumentée, <b>avis de valeur prêt à envoyer</b>.", { top: "960px", fontSize: "38px" }, 9.5);
        N.out([h, s2], 11.4);
        window.__TE = 11.6;
        N.outro(11.6, "demo");
""")

# ---------------------------------------------------------------- 7 · qui va vendre dans ta rue
FILMS["hook-07-qui-va-vendre"] = ("Qui va vendre dans ta rue ?", 15.6, """
      .pin { position: absolute; width: 34px; height: 34px; margin: -17px 0 0 -17px; border-radius: 50%; background: #b9b3d6; border: 5px solid #fff; box-shadow: 0 4px 10px rgba(27,31,75,.25); }
      .pin.hot { background: var(--vio); }
      .pin .rg { position: absolute; inset: -5px; border-radius: 50%; border: 4px solid var(--vio); }
      .pl { position: absolute; transform: translate(-50%, -100%); margin-top: -30px; white-space: nowrap; padding: 8px 18px; border-radius: 16px; background: var(--navy); color: #fff; font-family: Inter, sans-serif; font-weight: 700; font-size: 24px; }
""", """
        const chip = N.chip(`${K.icon("pin")}BRIVE · ALLASSAC · VOUTEZAC`, { top: "300px" });
        const hk = N.hook(["ET SI TU SAVAIS", "QUI VA VENDRE", "<span class='hl'>DANS TA RUE ?</span>"], { top: "440px", fontSize: "82px" });
        N.out([chip, hk], 2.6, { y: -40 });
        const cap = N.cap("LIMO repère les signaux<br>de vente dans ton secteur.", { top: "150px" }, 2.8);
        const roads = `<svg viewBox="0 0 900 700" width="900" height="700" style="position:absolute;left:0;top:0"><rect width="900" height="700" fill="#f4f2fc"/><path d="M0 200 C200 180 380 260 560 220 S820 120 900 140" stroke="#fff" stroke-width="34" fill="none"/><path d="M160 0 C200 200 140 420 260 700" stroke="#fff" stroke-width="26" fill="none"/><path d="M640 0 C600 220 700 460 620 700" stroke="#fff" stroke-width="26" fill="none"/><path d="M0 520 C260 480 520 560 900 470" stroke="#fff" stroke-width="22" fill="none"/><path d="M380 700 C420 560 360 420 460 330" stroke="#fff" stroke-width="16" fill="none"/><path d="M0 200 C200 180 380 260 560 220 S820 120 900 140" stroke="#e4def8" stroke-width="3" fill="none" stroke-dasharray="14 12"/><circle cx="760" cy="600" r="70" fill="#dff3ee"/><circle cx="90" cy="360" r="50" fill="#dff3ee"/></svg>`;
        const P = [[120, 120, 0], [300, 300, 1, "Maison · Allassac"], [480, 140, 0], [700, 330, 1, "Longère · Voutezac"], [220, 560, 0], [540, 470, 1, "Appart. · Brive"], [820, 560, 0], [400, 620, 0]];
        const map = N.ab("n-card", roads + P.map((p) => `<span class="pin${p[2] ? " hot" : ""}" style="left:${p[0]}px;top:${p[1]}px">${p[2] ? '<i class="rg"></i>' : ""}</span>${p[3] ? `<span class="pl" style="left:${p[0]}px;top:${p[1]}px">${p[3]}</span>` : ""}`).join(""), { left: "90px", top: "440px", width: "900px", height: "700px", overflow: "hidden" });
        N.hide(map);
        K.fin(map, 3.0, { y: 40, d: 0.5 });
        const pins = K.$$(".pin", map);
        pins.forEach((p, i) => { tl.fromTo(p, { scale: 0 }, { scale: 1, duration: 0.25, ease: "back.out(2.5)" }, 3.5 + i * 0.12); K.sfx(3.5 + i * 0.12, "pop", 0.08, 0, { f: 500 + i * 60 }); });
        K.$$(".pin.hot", map).forEach((p, i) => {
          const t = 4.8 + i * 0.5;
          tl.fromTo(K.$(".rg", p), { scale: 1, opacity: 0.9 }, { scale: 2.8, opacity: 0, duration: 0.9, ease: "power2.out", repeat: 3 }, t);
          K.sfx(t, "sonar", 0.14);
        });
        K.$$(".pl", map).forEach((l, i) => { tl.fromTo(l, { opacity: 0, y: 10 }, { opacity: 1, y: 0, duration: 0.3 }, 5.0 + i * 0.5); });
        const n1 = N.notif({ title: "DÉTECTEUR", text: "3 vendeurs potentiels repérés cette semaine dans ton secteur.", snd: "success", g: 0.26 }, { left: "90px", top: "1200px" }, 6.8);
        const fx = N.text("ctr n-body", "Exemple fictif", { top: "1830px", fontSize: "22px" }, 3.0);
        N.out(cap, 8.6, { y: -10, d: 0.2 });
        const c2 = N.cap("Tu appelles<br>avant les autres.", { top: "150px" }, 8.8, { dark: true });
        K.sfx(8.8, "thump", 0.3);
        N.out([c2, map, n1, fx], 11.6, { y: 40 });
        window.__TE = 12.0;
        N.outro(12.0, "dm");
""")

# ---------------------------------------------------------------- 8 · avant 8 h
FILMS["hook-08-avant-8h"] = ("Ce que font les meilleurs avant 8 h", 14.8, "", """
        const hk = N.hook(["CE QUE FONT", "LES AGENTS", "QUI SIGNENT", "LE PLUS", "<span class='hl'>AVANT 8 H.</span>"], { top: "420px", fontSize: "104px" });
        N.out(hk, 2.6, { y: -40 });
        const cap = N.cap("7 h 58. Le brief est déjà prêt.", { top: "150px" }, 2.8);
        const ip = N.iphone({ left: "110px", top: "400px", width: "860px", height: "1480px" }, "7:58");
        N.hide(ip.el);
        tl.fromTo(ip.el, { opacity: 0, y: 300 }, { opacity: 1, y: 0, duration: 0.6, ease: "power3.out" }, 2.8);
        const notes = K.h("div", "n-notes", `<h3>Brief du jour</h3><div class="dt">Préparé par LIMO · 7:30</div>`, ip.screen);
        const L = [["Appeler M. Albert", "9:00"], ["Visite à Vignols", "10:30"], ["Relancer famille Martin", "Priorité"], ["Publier l’annonce Allassac", "Prête"], ["Répondre à 2 avis Google", "Prêt"]];
        L.forEach((l, i) => {
          const r = K.h("div", "n-li", `<span class="c"></span><span class="t">${l[0]}</span><span class="tag">${l[1]}</span>`, notes);
          N.hide(r);
          K.fin(r, 3.4 + i * 0.35, { y: 16, d: 0.3 });
          K.sfx(3.4 + i * 0.35, "tick", 0.16, 0, { f: 1600 + i * 150 });
        });
        N.out(cap, 5.8, { y: -10, d: 0.2 });
        const c2 = N.cap("Pas plus d’heures.<br>Juste savoir quoi faire.", { top: "150px" }, 6.0, { dark: true });
        K.sfx(6.0, "thump", 0.28);
        N.out([c2, ip.el], 8.4, { y: 60, d: 0.4 });
        const h = N.head(["TON BRIEF", "DU MATIN<span class='v'>.</span>"], { top: "560px", fontSize: "100px" }, 8.7);
        const s = N.text("ctr n-body", "Chaque jour, LIMO te dit <b>qui appeler,<br>quoi relancer, quoi publier</b>.", { top: "900px", fontSize: "38px" }, 9.4);
        N.out([h, s], 11.0);
        window.__TE = 11.2;
        N.outro(11.2, "essai");
""")

# ---------------------------------------------------------------- 9 · ne like pas
FILMS["hook-09-ne-like-pas"] = ("Ne like pas cette vidéo", 14.8, """
      .cur { display: inline-block; width: 4px; height: 44px; background: #f5b700; vertical-align: -8px; margin-left: 2px; }
      #heart { left: 390px; top: 620px; width: 300px; height: 300px; }
""", """
        const hk = N.hook(["NE LIKE PAS", "CETTE VIDÉO<span class='v'>…</span>"], { top: "520px", fontSize: "100px" }, { g: 0.3 });
        const s1 = N.text("ctr n-body", "<b>…si tu aimes écrire tes annonces<br>à 23 h.</b>", { top: "820px", fontSize: "54px" }, 0.8);
        N.out([hk, s1], 2.6, { y: -40 });
        const cap = N.cap("23 h 04. Page blanche.", { top: "150px" }, 2.8);
        const ip = N.iphone({ left: "110px", top: "400px", width: "860px", height: "1480px" }, "23:04");
        N.hide(ip.el);
        tl.fromTo(ip.el, { opacity: 0, y: 300 }, { opacity: 1, y: 0, duration: 0.6, ease: "power3.out" }, 2.8);
        const nt = K.h("div", "n-notes", `<h3>Annonce Allassac</h3><div class="dt">23:04</div><div style="font-size:40px;line-height:1.4"><span class="t"></span><span class="cur"></span></div>`, ip.screen);
        tl.fromTo(K.$(".cur", nt), { opacity: 1 }, { opacity: 0, duration: 0.3, repeat: 5, yoyo: true, ease: "steps(1)" }, 3.2);
        N.out([cap, ip.el], 4.9, { y: 60, d: 0.4 });
        const c2 = N.cap("Avec LIMO : tu décris, il rédige.", { top: "150px" }, 5.1, { dark: true });
        const an = N.ab("n-card", `<div style="padding:40px 44px"><div style="font-family:'Source Serif 4',serif;font-size:46px;font-weight:600;line-height:1.2;color:#1b1f4b" class="ti"></div><div class="bo" style="margin-top:18px;font-size:32px;line-height:1.4;color:#3a3a3c;min-height:140px"></div><div class="lg" style="margin-top:20px;padding-top:18px;border-top:1px solid #efeff4;font-size:24px;line-height:1.4;color:#6e6e73">Prix honoraires inclus · Honoraires à la charge du vendeur · DPE et GES affichés</div><div class="cs" style="display:flex;gap:14px;margin-top:22px"><span class="n-chip">${K.icon("check")}Mentions légales</span><span class="n-chip">${K.icon("check")}Prête à publier</span></div></div>`, { left: "90px", top: "440px", width: "900px" });
        N.hide(an);
        tl.fromTo(an, { opacity: 0, y: 60 }, { opacity: 1, y: 0, duration: 0.5, ease: "power3.out" }, 5.3);
        K.type(K.$(".ti", an), "Maison de bourg avec jardin, au calme", 5.7, 0.6, 0.05);
        K.type(K.$(".bo", an), "À Allassac, 105 m², 3 chambres, cuisine ouverte sur jardin clos de 600 m². Commerces à pied.", 6.3, 1.2, 0.04);
        N.hide(K.$(".lg", an));
        K.fin(K.$(".lg", an), 7.6, { y: 8 });
        N.hide(K.$(".cs", an));
        tl.set(K.$(".cs", an), { opacity: 1 }, 7.9);
        K.pop(K.$$(".cs .n-chip", an), 7.9, { st: 0.12 });
        K.sfx(7.9, "success", 0.22);
        N.out([c2, an], 9.4, { y: 40 });
        const c3 = N.cap("Bon… là, tu peux liker.", { top: "1000px" }, 9.7);
        const hr = N.ab("", `<svg viewBox="0 0 24 24" width="300" height="300"><path d="M12 21s-7.5-4.6-9.6-9.2C.9 8.5 2.9 4.5 6.6 4.5c2.2 0 3.7 1.3 4.4 2.5.7-1.2 2.2-2.5 4.4-2.5 3.7 0 5.7 4 4.2 7.3C19.5 16.4 12 21 12 21z" fill="#e5484d"/></svg>`, {});
        hr.id = "heart";
        N.hide(hr);
        K.pop(hr, 9.6, { s: 0.3, d: 0.5, e: "back.out(3)" });
        K.sfx(9.6, "pop", 0.24, 0, { f: 900 });
        tl.to(hr, { scale: 1.12, duration: 0.2, yoyo: true, repeat: 1, ease: "sine.inOut" }, 10.2);
        N.out([c3, hr], 10.9, { y: -20 });
        window.__TE = 11.2;
        N.outro(11.2, "comment");
""")

# ---------------------------------------------------------------- 10 · le test
FILMS["hook-10-le-test"] = ("Test : t’as besoin d’un assistant ?", 15.0, """
      .q { left: 90px; width: 900px; height: 150px; display: flex; align-items: center; gap: 28px; padding: 0 36px; font-size: 36px; line-height: 1.25; font-weight: 600; }
      .q .bx { flex: none; width: 60px; height: 60px; border-radius: 16px; border: 4px solid #c7c7cc; position: relative; }
      .q .bx i { position: absolute; inset: -4px; border-radius: 16px; background: var(--vio); color: #fff; display: flex; align-items: center; justify-content: center; }
      .q .bx svg.i { width: 36px; height: 36px; stroke-width: 3.4; }
      #sc { right: 90px; top: 300px; font-family: Montserrat, sans-serif; font-weight: 800; font-size: 44px; color: var(--vio); }
      #sc span { position: absolute; right: 0; white-space: nowrap; }
""", """
        const hk = N.hook(["TEST<span class='v'> :</span>", "T’AS BESOIN", "D’UN", "<span class='hl'>ASSISTANT ?</span>"], { top: "400px", fontSize: "104px" });
        const s1 = N.text("ctr n-body", "<b>Compte tes « oui ».</b>", { top: "900px", fontSize: "54px" }, 0.9);
        N.out([hk, s1], 2.5, { y: -40 });
        const cap = N.cap("Sois honnête.", { top: "150px" }, 2.6);
        const Q = ["Tu rappelles tes vendeurs « quand t’as le temps ».", "Tes annonces se ressemblent toutes.", "Tu bosses le dimanche soir.", "Tu as des avis Google sans réponse.", "Tu oublies les anniversaires clients."];
        const sc = N.ab("", Array.from({ length: 6 }, (_, k) => `<span>${k} / 5</span>`).join(""), {});
        sc.id = "sc";
        N.hide(sc);
        tl.set(sc, { opacity: 1 }, 2.8);
        const ss = K.$$("span", sc);
        const qs = Q.map((q, i) => {
          const e = N.ab("n-card q", `<span class="bx"><i>${K.icon("check")}</i></span><span>${q}</span>`, { top: 420 + i * 180 + "px" });
          N.hide(e);
          const t = 2.9 + i * 0.95;
          K.fin(e, t, { y: 24, d: 0.3 });
          tl.set(K.$(".bx i", e), { scale: 0 }, 0);
          tl.to(K.$(".bx i", e), { scale: 1, duration: 0.22, ease: "back.out(2.6)" }, t + 0.5);
          K.sfx(t + 0.5, "tick", 0.24, 0, { f: 1500 + i * 180 });
          return e;
        });
        ss.forEach((s, k) => {
          tl.set(s, { opacity: 0 }, 0);
          tl.set(s, { opacity: 1 }, k === 0 ? 2.8 : 2.9 + (k - 1) * 0.95 + 0.5);
          if (k < 5) tl.set(s, { opacity: 0 }, 2.9 + k * 0.95 + 0.5);
        });
        N.out(cap, 8.2, { y: -10, d: 0.2 });
        const c2 = N.cap("3 « oui » ou plus ?<br>LIMO est fait pour toi.", { top: "150px" }, 8.4, { dark: true });
        K.sfx(8.4, "thump", 0.3);
        N.out([c2, sc, ...qs], 11.0, { y: 40 });
        window.__TE = 11.2;
        N.outro(11.2, "dm");
""")

if __name__ == "__main__":
    for name, (title, dur, css, body) in FILMS.items():
        html = SHELL.format(title=title, faces=FACES, css=css.strip("\n"), body=body.strip("\n"), dur=dur, name=name)
        pathlib.Path(f"reels/{name}.html").write_text(html, encoding="utf-8")
        print("reels/" + name + ".html")
