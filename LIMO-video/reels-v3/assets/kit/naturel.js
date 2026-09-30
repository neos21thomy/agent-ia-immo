/* LIMO — aides pour la charte « naturelle » (s'appuie sur K, kit.js). */
(function () {
  "use strict";
  const N = (window.N = {});
  let tl, root;
  const STATUS = `<svg viewBox="0 0 112 24" fill="#000"><rect x="0" y="15" width="5" height="7" rx="1.5"/><rect x="8" y="11" width="5" height="11" rx="1.5"/><rect x="16" y="7" width="5" height="15" rx="1.5"/><rect x="24" y="3" width="5" height="19" rx="1.5"/><path d="M40 10.5a14 14 0 0 1 20 0M44 14.5a8 8 0 0 1 12 0M48.5 18.5a2 2 0 0 1 3 0" fill="none" stroke="#000" stroke-width="2.6" stroke-linecap="round"/><rect x="70" y="4" width="36" height="17" rx="5" fill="none" stroke="#000" stroke-opacity=".4" stroke-width="2"/><rect x="73" y="7" width="27" height="11" rx="2.5"/></svg>`;
  N.init = (timeline, r, dur) => {
    tl = timeline;
    root = r;
    K.h("div", "n-bg", null, root);
    const arcs = [
      [620, -300, 900],
      [-420, 1180, 1000],
    ].map(([x, y, s]) => {
      const a = K.h("div", "n-arc", null, root);
      Object.assign(a.style, { left: x + "px", top: y + "px", width: s + "px", height: s + "px" });
      a.setAttribute("data-layout-allow-overflow", "");
      return a;
    });
    tl.fromTo(arcs, { rotation: 0, scale: 1 }, { rotation: 12, scale: 1.06, duration: dur, ease: "none" }, 0);
    return N;
  };
  N.ab = (cls, html, css, parent) => {
    const e = K.h("div", "ab " + (cls || ""), html == null ? null : html, parent || root);
    if (css) Object.assign(e.style, css);
    return e;
  };
  N.hide = (el) => tl.set(el, { opacity: 0 }, 0);
  // Titre façon pub LIMO (capitales marine, point violet, trait turquoise)
  N.head = (lines, css, t, o = {}) => {
    const el = N.ab("ctr n-head", lines.map((l) => `<span class="nmask" data-layout-allow-overflow><span data-layout-allow-occlusion data-layout-allow-overlap>${l}</span></span>`).join("") + (o.bar === false ? "" : `<div class="n-bar" style="margin:${o.left ? "34px 0 0" : "34px auto 0"}"></div>`), css);
    N.hide(el);
    tl.set(el, { opacity: 1 }, t - 0.02);
    const s = K.$$(".nmask > span", el);
    tl.fromTo(s, { yPercent: 105 }, { yPercent: 0, duration: 0.7, ease: "power4.out", stagger: 0.09 }, t);
    const bar = K.$(".n-bar", el);
    if (bar) tl.fromTo(bar, { scaleX: 0 }, { scaleX: 1, duration: 0.5, ease: "power3.out" }, t + 0.35 + s.length * 0.09);
    K.sfx(t, "whoosh", 0.08, 0, { d: 0.35, f0: 500, f1: 3000, pk: 0.5 });
    return el;
  };
  N.text = (cls, html, css, t, o = {}) => {
    const el = N.ab(cls, html, css);
    N.hide(el);
    K.fin(el, t, { y: o.y ?? 16, d: o.d ?? 0.5 });
    return el;
  };
  // Légende façon Reels natif (boîte blanche, texte noir gras)
  N.cap = (html, css, t, o = {}) => {
    const el = N.ab("ctr n-cap" + (o.dark ? " dark" : ""), `<span>${html}</span>`, css);
    N.hide(el);
    tl.set(el, { opacity: 1 }, t);
    tl.fromTo(K.$("span", el), { scale: 0.85, opacity: 0 }, { scale: 1, opacity: 1, duration: 0.28, ease: "back.out(2)" }, t);
    K.sfx(t, "pop", 0.14, 0, { f: 700 });
    return el;
  };
  N.out = (els, t, o = {}) => K.fout(els, t, { y: o.y ?? -30, d: o.d ?? 0.3 });
  N.iphone = (css, time = "9:41") => {
    const el = N.ab("n-iphone", `<div class="n-screen"><div class="n-status"><span>${time}</span>${STATUS}</div><div class="n-island"></div></div>`, css);
    return { el, screen: K.$(".n-screen", el), time: K.$(".n-status span", el) };
  };
  N.phoneLimo = (css, t) => {
    const ph = N.ab("n-phone", `<img src="assets/img/phone-limo.png" alt="L’application LIMO sur téléphone" />`, css);
    ph.setAttribute("data-layout-allow-overflow", "");
    N.hide(ph);
    tl.fromTo(ph, { opacity: 0, y: 500, rotation: 6 }, { opacity: 1, y: 0, rotation: -2, duration: 0.9, ease: "power4.out" }, t);
    K.sfx(t, "whoosh", 0.18, 0, { d: 0.6, f0: 200, f1: 1500, pk: 0.6 });
    return ph;
  };
  N.notif = (o, css, t) => {
    const el = N.ab("n-notif", `<img src="assets/img/limo-house-ad.png" alt="" /><div class="tx"><div class="tp">LIMO · ${o.title}<span>${o.time || "maintenant"}</span></div><b>${o.text}</b></div>`, css, o.parent);
    N.hide(el);
    tl.fromTo(el, { opacity: 0, y: -120, scale: 0.94 }, { opacity: 1, y: 0, scale: 1, duration: 0.5, ease: "back.out(1.4)" }, t);
    K.sfx(t, o.snd || "notif", o.g ?? 0.24);
    return el;
  };
  // Carte de fin sobre, au logo LIMO
  N.outro = (t, kind = "essai") => {
    const logo = N.ab("", `<img src="assets/img/limo-logo-ad.png" alt="LIMO" style="width:100%;height:100%" />`, { left: "290px", top: "360px", width: "500px", height: "189px" });
    N.hide(logo);
    tl.fromTo(logo, { opacity: 0, y: 30 }, { opacity: 1, y: 0, duration: 0.6, ease: "power3.out" }, t);
    K.sfx(t + 0.05, "thump", 0.3);
    const tag = N.text("ctr n-body", "Ton chef de cabinet immo.", { top: "600px", fontSize: "40px", fontWeight: "600", color: "#1b1f4b" }, t + 0.3);
    const C = {
      dm: ["ÉCRIS-MOI <span class='n-kw'>LIMO</span>", "EN MESSAGE PRIVÉ<span class='v'>.</span>", K.icon("send") + "Je t’ouvre ton accès"],
      comment: ["COMMENTE <span class='n-kw'>LIMO</span>", "JE T’ENVOIE L’ACCÈS<span class='v'>.</span>", K.icon("msg") + "Accès offert 14 jours"],
      demo: ["RÉSERVE TA DÉMO", "DE 15 MINUTES<span class='v'>.</span>", K.icon("clock") + "Réserver ma démo"],
      essai: ["ESSAIE-LE", "14 JOURS<span class='v'>.</span>", "Commencer gratuitement →"],
    }[kind];
    const h = N.head([C[0], C[1]], { top: "780px", fontSize: "78px" }, t + 0.55);
    const cta = N.ab("n-cta", `<span>${C[2]}</span>`, { left: "0", right: "0", top: "1130px" });
    N.hide(cta);
    tl.set(cta, { opacity: 1 }, t + 1.1);
    K.pop(K.$("span", cta), t + 1.1, { s: 0.8, d: 0.45, e: "back.out(1.6)" });
    K.sfx(t + 1.1, "cta", 0.18);
    const sub = N.text("ctr n-body", (kind === "demo" ? "<b>Lien en bio</b><br>" : "") + "Sans carte bancaire · Sans engagement<br><b>app.leadengineai.fr</b>", { top: "1290px", fontSize: "30px" }, t + 1.35);
    return t + 3.6;
  };
})();
