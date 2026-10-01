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
  A.gain = (icon, c, big, small) => `<span class="a-ic ${c}">${K.icon(icon)}</span><span><b>${big}</b><small>${small}</small></span>`;
})();
