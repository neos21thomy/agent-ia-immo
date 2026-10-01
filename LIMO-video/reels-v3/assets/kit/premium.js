/* LIMO — aides « premium » pour les films de conversion (s'appuie sur K, kit.js). */
(function () {
  "use strict";
  const P = (window.P = {});
  let tl, root;
  P.init = (timeline, r, dur) => {
    tl = timeline;
    root = r;
    K.bg(root, { dur: dur || 20 });
    return P;
  };
  P.ab = (cls, html, css, parent) => {
    const e = K.h("div", "ab " + (cls || ""), html == null ? null : html, parent || root);
    if (css) Object.assign(e.style, css);
    return e;
  };
  P.lines = (arr) => arr.map((l) => `<span class="pmask" data-layout-allow-overflow><span data-layout-allow-occlusion data-layout-allow-overlap>${l}</span></span>`).join("");
  // Titre qui monte ligne par ligne ; caché avant son entrée (évite le texte « sous » d'autres calques)
  P.title = (arr, css, t, o = {}) => {
    const el = P.ab(o.cls || "ctr p-big", P.lines(arr), css);
    const s = K.$$(".pmask > span", el);
    tl.set(el, { opacity: 0 }, 0);
    tl.set(el, { opacity: 1 }, Math.max(0.001, t - 0.02));
    tl.fromTo(s, { yPercent: 110 }, { yPercent: 0, duration: 0.6, ease: "expo.out", stagger: o.st ?? 0.1 }, t);
    if (o.snd !== false) s.forEach((x, i) => K.sfx(t + i * (o.st ?? 0.1), "whoosh", 0.1, i % 2 ? 0.3 : -0.3, { d: 0.3, f0: 700, f1: 4500, pk: 0.6 }));
    if (o.slam) K.sfx(t, "slam", o.slam);
    return el;
  };
  P.text = (cls, html, css, t, o = {}) => {
    const el = P.ab(cls, html, css);
    tl.set(el, { opacity: 0 }, 0);
    K.fin(el, t, { y: o.y ?? 20, d: o.d ?? 0.45 });
    return el;
  };
  P.out = (els, t, o = {}) => K.fout(els, t, { y: o.y ?? -40, d: o.d ?? 0.3 });
  P.notif = (o, css, t) => {
    const el = P.ab("p-notif", `<div class="bl ${o.c || ""}">${K.icon(o.icon || "bell")}</div><div class="tx"><div class="tp">${o.title}<span>${o.time || "Maintenant"}</span></div><b>${o.text}</b></div>`, css, o.parent);
    tl.set(el, { opacity: 0 }, 0);
    tl.fromTo(el, { opacity: 0, y: -140, scale: 0.9 }, { opacity: 1, y: 0, scale: 1, duration: 0.5, ease: "back.out(1.6)" }, t);
    K.sfx(t, o.snd || "notif", o.g ?? 0.26, o.pan || 0);
    return el;
  };
  P.phone = (css, t, o = {}) => {
    const halo = P.ab("p-halo", null, { left: (parseFloat(css.left) - 170) + "px", top: (parseFloat(css.top) - 110) + "px", width: "1000px", height: "1400px" });
    halo.setAttribute("data-layout-allow-overflow", "");
    const ph = P.ab("p-phone", `<img src="assets/img/phone-limo.png" alt="L’application LIMO sur téléphone" />`, css);
    ph.setAttribute("data-layout-allow-overflow", "");
    tl.set([ph, halo], { opacity: 0 }, 0);
    tl.fromTo(halo, { opacity: 0, scale: 0.7 }, { opacity: 1, scale: 1, duration: 0.8, ease: "power2.out" }, t);
    tl.fromTo(ph, { y: 1500, rotation: 8, opacity: 0 }, { y: 0, rotation: o.rot ?? -3, opacity: 1, duration: 0.9, ease: "power4.out" }, t);
    K.sfx(t, "whoosh", 0.26, 0, { d: 0.7, f0: 180, f1: 1500, pk: 0.6 });
    return { ph, halo };
  };
  P.pill = (kind, icon, text, css, t, o = {}) => {
    const w = P.ab(o.cls || "ctr", `<span class="p-pill ${kind}">${icon ? K.icon(icon) : ""}${text}</span>`, css);
    tl.set(w, { opacity: 0 }, 0);
    tl.set(w, { opacity: 1 }, t);
    K.pop(K.$("span", w), t, { s: 0.6 });
    if (o.snd !== false) K.sfx(t, kind === "red" ? "buzz" : kind === "ok" ? "success" : "pop", kind === "red" ? 0.14 : 0.2);
    return w;
  };
  P.photo = (css, t, o = {}) => {
    const el = P.ab("p-photo", `<img src="assets/img/${o.src || "bureau-robot.jpg"}" alt="${o.alt || "Le robot LIMO au bureau, vue sur la mer"}" />`, css);
    tl.set(el, { opacity: 0 }, 0);
    tl.fromTo(el, { opacity: 0, y: 90, scale: 0.94 }, { opacity: 1, y: 0, scale: 1, duration: 0.7, ease: "power3.out" }, t);
    tl.fromTo(K.$("img", el), { scale: 1.02 }, { scale: 1.12, duration: o.kb ?? 4, ease: "none" }, t);
    K.sfx(t, "whoosh", 0.18, 0, { d: 0.6, f0: 200, f1: 1800, pk: 0.6 });
    return el;
  };
  /* Carte de fin avec appel à l'action.
     kind : "dm" (message privé), "comment", "demo" (démo 15 min), "essai" (14 jours) */
  P.outro = (t, kind = "essai", o = {}) => {
    const house = P.ab("p-house", `<img src="assets/img/limo-house.png" alt="Logo LIMO" />`, { left: "390px", top: "180px", width: "300px", height: "265px" });
    const wm = P.ab("ctr p-wm", "LIMO", { top: "460px", fontSize: "92px" });
    const tag = P.ab("ctr p-kick", "LE BRAS DROIT DU CONSEILLER IMMO", { top: "590px", fontSize: "22px" });
    tl.set([house, wm, tag], { opacity: 0 }, 0);
    tl.fromTo(house, { opacity: 0, scale: 0.6, filter: "blur(16px)" }, { opacity: 1, scale: 1, filter: "blur(0px)", duration: 0.7, ease: "power3.out" }, t);
    tl.fromTo(wm, { opacity: 0, scaleX: 1.3 }, { opacity: 1, scaleX: 1, duration: 0.7, ease: "power3.out" }, t + 0.2);
    K.fin(tag, t + 0.4, { y: 10 });
    K.sfx(t, "riser", 0.12, 0, { d: 0.4 });
    K.sfx(t + 0.35, "thump", 0.42);
    const C = {
      dm: { h: ["Écris-moi <span class='p-kw'>LIMO</span>", "<em>en message privé.</em>"], btn: [K.icon("send"), "Je t’ouvre ton accès"], sub: "Réponse perso · 14 jours offerts" },
      comment: { h: ["Commente <span class='p-kw'>LIMO</span>", "<em>je t’envoie l’accès.</em>"], btn: [K.icon("msg"), "Commente « LIMO »"], sub: "Accès offert 14 jours" },
      demo: { h: ["Réserve ta démo", "<em>de 15 minutes.</em>"], btn: [K.icon("clock"), "Réserver ma démo →"], sub: "Lien en bio" },
      essai: { h: ["Essaie-le", "<em>14 jours.</em>"], btn: ["", "Commencer gratuitement →"], sub: "" },
    }[kind];
    const h = P.title(C.h, { top: "700px", fontSize: kind === "essai" ? "104px" : kind === "demo" ? "96px" : "80px" }, t + 0.55, { st: 0.1, slam: 0.3 });
    const three = C.h.length === 3;
    const cta = P.ab("p-cta", `<i class="sh"></i>${C.btn[0]}${C.btn[1]}`, { top: three ? "1170px" : kind === "demo" ? "1000px" : "1110px" });
    tl.set(cta, { opacity: 0 }, 0);
    K.pop(cta, t + 1.1, { s: 0.7, d: 0.55, e: "back.out(1.7)" });
    K.sfx(t + 1.1, "cta", 0.22);
    tl.fromTo(K.$("i.sh", cta), { x: -160 }, { x: 960, duration: 0.9, ease: "power2.inOut" }, t + 1.6);
    tl.to(cta, { scale: 1.05, duration: 0.35, ease: "sine.inOut", yoyo: true, repeat: 3 }, t + 1.7);
    const top2 = three ? 1340 : kind === "demo" ? 1170 : 1280;
    const chips = P.ab("ctr p-chips", `<span>${K.icon("check")}Sans carte bancaire</span><span>${K.icon("check")}Sans engagement</span>`, { top: top2 + "px" });
    tl.set(chips, { opacity: 0 }, 0);
    tl.set(chips, { opacity: 1 }, t + 1.35);
    K.fin(K.$$("span", chips), t + 1.35, { y: 12, st: 0.1 });
    const sub = C.sub ? P.text("ctr p-sm", C.sub, { top: top2 + 90 + "px", fontSize: "30px" }, t + 1.55) : null;
    const url = P.text("ctr p-sm", "app.leadengineai.fr", { top: top2 + (C.sub ? 150 : 100) + "px", fontSize: "32px", color: "#fff" }, t + 1.65);
    K.burst(K.sparkles(root, 540, top2 - 105, 14, 440, 110, 4), t + 1.15);
    return t + (o.hold ?? 3.6);
  };
  P.flash = (t, color = "#ff5a67") => {
    const f = P.ab("", null, { left: "0", top: "0", width: "1080px", height: "1920px", background: color });
    tl.set(f, { opacity: 0 }, 0);
    tl.fromTo(f, { opacity: 0.35 }, { opacity: 0, duration: 0.5, ease: "power2.out" }, t);
    return f;
  };
})();
