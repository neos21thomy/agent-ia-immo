/* LIMO — application recréée en HTML (thème clair) + téléphone 3D. S'appuie sur K (kit.js) et N (naturel.js). */
(function () {
  "use strict";
  const A = (window.A = {});
  let tl, root;
  const STATUS = `<svg viewBox="0 0 112 24" fill="#111"><rect x="0" y="15" width="5" height="7" rx="1.5"/><rect x="8" y="11" width="5" height="11" rx="1.5"/><rect x="16" y="7" width="5" height="15" rx="1.5"/><rect x="24" y="3" width="5" height="19" rx="1.5"/><path d="M40 10.5a14 14 0 0 1 20 0M44 14.5a8 8 0 0 1 12 0M48.5 18.5a2 2 0 0 1 3 0" fill="none" stroke="#111" stroke-width="2.6" stroke-linecap="round"/><rect x="70" y="4" width="36" height="17" rx="5" fill="none" stroke="#111" stroke-opacity=".4" stroke-width="2"/><rect x="73" y="7" width="27" height="11" rx="2.5"/></svg>`;
  A.init = (timeline, r) => { tl = timeline; root = r; return A; };
  // élément posé volontairement par-dessus l'écran du téléphone (bannière, carte flottante)
  A.over = (el) => { [el, ...K.$$("*", el)].forEach((e) => { e.setAttribute("data-layout-allow-overlap", ""); e.setAttribute("data-layout-allow-occlusion", ""); }); return el; };
  A.HD = `<div class="a-hd"><img src="assets/img/limo-logo-ad.png" alt="LIMO" /><span class="bell"><svg class="i"><use href="#i-bell"/></svg><i></i></span></div>`;
  A.row = (icon, c, title, sub, right = "", extra = "") =>
    `<div class="a-card a-row"><span class="a-ic ${c}">${K.icon(icon)}</span><span class="tx"><b>${title}</b><small>${sub}</small></span>${right ? `<span class="tm">${right}</span>` : ""}${extra}</div>`;
  const TABS = [["home", "Accueil"], ["users", "Contacts"], ["+", ""], ["pin", "Mandats"], ["note", "Plus"]];
  // Téléphone : css = { left, top, width } (hauteur = largeur × 2,05)
  A.phone = (css, o = {}) => {
    const W = parseFloat(css.width), H = Math.round(W * 2.05);
    const wrap = N.ab("a-wrap", null, Object.assign({ height: H + "px" }, css));
    wrap.setAttribute("data-layout-allow-overflow", "");
    wrap.setAttribute("data-layout-allow-occlusion", "");
    wrap.innerHTML = `<div class="a-dev"><div class="a-scr"><div class="a-st"><span>${o.time || "9:41"}</span>${STATUS}</div><div class="a-isl"></div><div class="a-view"></div>
<div class="a-tab">${TABS.map((t, i) => t[0] === "+" ? `<div class="plus">${K.icon("plus")}</div>` : `<div class="${i === (o.tab ?? 0) ? "on" : ""}">${K.icon(t[0])}<span>${t[1]}</span></div>`).join("")}</div><div class="a-shine"></div></div></div>`;
    K.$$("*", wrap).forEach((e) => e.setAttribute("data-layout-allow-occlusion", ""));
    const ph = { wrap, scr: K.$(".a-scr", wrap), view: K.$(".a-view", wrap), W, H, pages: [] };
    tl.set(K.$(".a-shine", wrap), { xPercent: -120 }, 0);
    return ph;
  };
  A.page = (ph, html, o = {}) => {
    const p = K.h("div", "a-pg", html, ph.view);
    p.setAttribute("data-layout-allow-overflow", "");
    K.$$("*", p).forEach((e) => e.setAttribute("data-layout-allow-occlusion", ""));
    tl.set(p, { opacity: ph.pages.length ? 0 : 1, xPercent: 0 }, 0);
    ph.pages.push(p);
    return p;
  };
  // Passage d'un écran à l'autre (glissement iOS)
  A.go = (ph, from, to, t, o = {}) => {
    tl.fromTo(to, { opacity: 1, xPercent: o.back ? -30 : 100 }, { opacity: 1, xPercent: 0, duration: 0.45, ease: "power3.inOut" }, t);
    tl.to(from, { xPercent: o.back ? 100 : -30, opacity: 0, duration: 0.45, ease: "power3.inOut" }, t);
    K.sfx(t, "swipe", 0.12);
  };
  A.tap = (ph, x, y, t) => {
    const d = K.h("span", "a-tap", null, ph.scr);
    d.style.left = x + "px";
    d.style.top = y + "px";
    tl.set(d, { opacity: 0 }, 0);
    tl.fromTo(d, { scale: 0.4, opacity: 0 }, { scale: 0.7, opacity: 1, duration: 0.08, ease: "none" }, t);
    tl.to(d, { scale: 1.8, opacity: 0, duration: 0.45, ease: "power2.out" }, t + 0.08);
    K.sfx(t, "tap", 0.35);
  };
  A.shine = (ph, t) => {
    tl.fromTo(K.$(".a-shine", ph.wrap), { xPercent: -120 }, { xPercent: 120, duration: 1.1, ease: "power2.inOut" }, t);
  };
  // Entrée en 3D, puis le téléphone se met de face
  A.enter = (ph, t, o = {}) => {
    N.hide(ph.wrap);
    tl.fromTo(ph.wrap, { opacity: 0, y: 700, rotationY: o.ry ?? -32, rotationX: 14, rotationZ: 6, transformPerspective: 2400 },
      { opacity: 1, y: 0, rotationY: o.ry2 ?? -14, rotationX: 5, rotationZ: 0, transformPerspective: 2400, duration: 1.0, ease: "power4.out" }, t);
    K.sfx(t, "whoosh", 0.22, 0, { d: 0.7, f0: 180, f1: 1600, pk: 0.6 });
    A.shine(ph, t + 0.6);
    if (o.flat !== false) tl.to(ph.wrap, { rotationY: 0, rotationX: 0, duration: 1.2, ease: "power2.inOut" }, t + (o.flatAt ?? 1.1));
  };
  A.leave = (ph, t) => {
    tl.to(ph.wrap, { y: -260, rotationY: 18, opacity: 0, duration: 0.55, ease: "power3.in", transformPerspective: 2400 }, t);
  };
  A.float = (html, css, t, o = {}) => {
    const e = A.over(N.ab("a-float", html, css));
    N.hide(e);
    tl.fromTo(e, { opacity: 0, scale: 0.6, y: 40 }, { opacity: 1, scale: 1, y: 0, duration: 0.5, ease: "back.out(1.8)" }, t);
    tl.to(e, { y: -14, duration: 1.4, ease: "sine.inOut", yoyo: true, repeat: 1 }, t + 0.5);
    K.sfx(t, o.snd || "pop", o.g ?? 0.18, 0, { f: 900 });
    return e;
  };
  // Écrans types de l'application (HTML), réutilisables
  A.S = {
    home: () => A.HD + `<div class="a-hello"><span>Bonjour,</span><br>Voici les actions prioritaires du jour.</div>
<div class="a-card a-prio"><span class="n">5</span><span><b>Actions prioritaires</b><small>à traiter aujourd’hui</small></span></div>
<div class="a-h2">Actions du jour</div>` + A.row("refresh", "v", "Relancer 32 contacts", "Relances programmées", "09:30") + A.row("home", "t", "Suivre 2 visites", "Visites à suivre", "11:00") + A.row("shield", "g", "Envoyer 1 proposition", "Mandat en préparation", "14:00") + A.row("star", "t", "Nouveau mandat détecté", "Opportunité à saisir", "15:30") + A.row("gift", "v", "Anniversaire client", "Message à personnaliser", "17:00"),
    relances: () => `<div class="a-back">${K.icon("chev")}Relances du jour</div><div style="display:flex;gap:10px;margin:4px 0 16px"><span class="a-tag">${K.icon("refresh")}32 contacts</span><span class="a-tag t">${K.icon("check")}Messages prêts</span></div>` +
      A.row("users", "v", "M. Vidal", "Estimation · il y a 47 j", "", `<span class="a-tag t">Prêt</span>`) + A.row("users", "v", "Famille Martin", "Vendre au printemps", "", `<span class="a-tag t">Prêt</span>`) + A.row("users", "v", "Mme Roy", "Succession en cours", "", `<span class="a-tag t">Prêt</span>`) + A.row("users", "v", "M. Albert", "Mutation en juin", "", `<span class="a-tag t">Prêt</span>`) +
      `<div class="a-btn" style="margin-top:12px">${K.icon("check")}32 relances envoyées</div>`,
    annonce: () => `<div class="a-back">${K.icon("chev")}Annonce</div><div class="a-ph" style="height:200px;margin-bottom:14px">${K.houseArt(480, 200, "as")}</div>
<div class="a-card" style="padding:20px 22px"><div style="font-family:'Source Serif 4',serif;font-size:30px;font-weight:600;line-height:1.2">Maison familiale au calme avec grand terrain</div><div style="margin-top:10px;font-size:20px;line-height:1.45;color:#3a3a3c">À Vignols, 120 m² lumineux, 4 chambres, séjour traversant sur 1 500 m² de terrain.</div></div>
<div style="display:flex;gap:10px;margin-top:14px"><span class="a-tag t">${K.icon("check")}Mentions légales</span><span class="a-tag">${K.icon("check")}Prête à publier</span></div>`,
    detect: () => {
      const roads = `<svg viewBox="0 0 480 380" width="100%" height="100%" style="position:absolute;inset:0"><rect width="480" height="380" fill="#eef0f7"/><path d="M0 110 C120 90 220 150 320 120 S440 60 480 70" stroke="#fff" stroke-width="22" fill="none"/><path d="M90 0 C120 120 80 240 150 380" stroke="#fff" stroke-width="16" fill="none"/><path d="M350 0 C320 130 380 250 330 380" stroke="#fff" stroke-width="16" fill="none"/><path d="M0 290 C150 260 300 310 480 260" stroke="#fff" stroke-width="14" fill="none"/></svg>`;
      const P = [[70, 60, 0], [170, 180, 1], [260, 70, 0], [380, 190, 1], [120, 310, 0], [290, 270, 1], [440, 300, 0]];
      return `<div class="a-back">${K.icon("chev")}Détecteur</div><div class="a-map">${roads}${P.map((q) => `<span class="a-pin${q[2] ? " hot" : ""}" style="left:${q[0]}px;top:${q[1]}px">${q[2] ? '<i class="rg"></i>' : ""}</span>`).join("")}</div><div class="a-h2">3 vendeurs probables</div>` +
        A.row("home", "v", "Maison · Allassac", "Signaux de vente repérés", "", `<span class="a-tag t">Fort</span>`) + A.row("home", "v", "Longère · Voutezac", "Signaux de vente repérés", "", `<span class="a-tag t">Fort</span>`);
    },
    avis: () => `<div class="a-back">${K.icon("chev")}Avis Google</div><div class="a-card" style="display:flex;align-items:center;gap:20px;padding:22px 24px;margin-bottom:16px"><b style="font-size:58px;font-weight:700">4,8</b><span><span class="a-stars">${K.icon("star").repeat(5)}</span><small style="display:block;margin-top:6px;font-size:20px;color:#6e6e80">37 avis · tous répondus</small></span></div>` +
      A.row("users", "o", "Marie L. · 5 étoiles", "Réponse publiée", "", `<span class="a-tag t">${K.icon("check")}</span>`) + A.row("users", "g", "Paul D. · 3 étoiles", "Réponse publiée", "", `<span class="a-tag t">${K.icon("check")}</span>`) + A.row("users", "t", "Julie R. · 5 étoiles", "Réponse publiée", "", `<span class="a-tag t">${K.icon("check")}</span>`),
    dictee: () => `<div class="a-back">${K.icon("chev")}Compte rendu de visite</div><div class="a-card a-msg" style="display:flex;align-items:center;gap:14px;background:#6b4fe0;color:#fff">${K.icon("mic")}<span>Note vocale · 0:38</span></div>
<div class="a-h2">Fiche mise à jour</div>` + A.row("users", "v", "Famille Durand", "Acheteurs · Vignols") + A.row("home", "t", "Coup de cœur jardin", "Hésitent sur la cuisine") + A.row("clock", "o", "Rappel jeudi 18 h", "Envoyer 2 biens similaires"),
  };
  A.gain = (icon, c, big, small) => `<span class="a-ic ${c}">${K.icon(icon)}</span><span><b>${big}</b><small>${small}</small></span>`;
})();
