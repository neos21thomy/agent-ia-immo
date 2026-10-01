/* LIMO — traitement « cinéma » : caméra, grain, vignette, bandes cinéma, fuites de lumière, transitions.
   Grain et fuite de lumière adaptés des blocs du registre HyperFrames (grain-overlay, organic-light-leak-overlay),
   recolorés LIMO et pilotés par la timeline (déterministe). S'appuie sur K et N. */
(function () {
  "use strict";
  const C = (window.C = {});
  let tl, scene, top;
  const NOISE = "url(\"data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.75' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E\")";
  const ab = (parent, css, html) => {
    const e = document.createElement("div");
    Object.assign(e.style, { position: "absolute" }, css);
    if (html) e.innerHTML = html;
    e.setAttribute("data-layout-allow-overflow", "");
    e.setAttribute("data-layout-allow-occlusion", "");
    e.setAttribute("data-layout-allow-overlap", "");
    parent.appendChild(e);
    return e;
  };
  // scene = la section animée par la caméra ; les effets d'objectif vont au-dessus, hors caméra
  C.init = (timeline, sceneEl, dur, o = {}) => {
    tl = timeline;
    scene = sceneEl;
    top = document.getElementById("root");
    scene.style.transformOrigin = "540px 960px";
    // vignette
    C.vig = ab(top, { left: "0", top: "0", width: "1080px", height: "1920px", zIndex: 40, pointerEvents: "none", background: "radial-gradient(ellipse 75% 60% at 50% 48%, rgba(0,0,0,0) 55%, rgba(14,16,48,.32) 100%)" });
    // grain (sauts pilotés par la timeline)
    const g = ab(top, { left: "0", top: "0", width: "1080px", height: "1920px", zIndex: 41, overflow: "hidden", pointerEvents: "none", mixBlendMode: "overlay", opacity: String(o.grain ?? 0.22) });
    const tex = ab(g, { left: "-50%", top: "-50%", width: "200%", height: "200%", background: NOISE, backgroundSize: "256px 256px" });
    const P = [[0, 0], [-5, -5], [-10, 5], [5, -10], [-5, 15], [-10, 5], [15, 0], [0, 10], [-15, 0], [10, 5]];
    for (let i = 0, t = 0; t < dur; i++, t += 1 / 12) tl.set(tex, { xPercent: P[i % 10][0] / 2, yPercent: P[i % 10][1] / 2 }, t);
    C.grain = g;
    // bandes cinéma
    C.barT = ab(top, { left: "0", top: "0", width: "1080px", height: "200px", zIndex: 42, background: "#05060f" });
    C.barB = ab(top, { left: "0", top: "1720px", width: "1080px", height: "200px", zIndex: 42, background: "#05060f" });
    tl.set([C.barT, C.barB], { yPercent: 0 }, 0);
    return C;
  };
  C.bars = (t, open = true, d = 0.9) => {
    tl.to(C.barT, { yPercent: open ? -100 : 0, duration: d, ease: "power3.inOut" }, t);
    tl.to(C.barB, { yPercent: open ? 100 : 0, duration: d, ease: "power3.inOut" }, t);
  };
  // mouvement de caméra sur toute la scène
  C.cam = (t, to, d = 2, ease = "sine.inOut") => tl.to(scene, Object.assign({ duration: d, ease }, to), t);
  C.camSet = (t, v) => tl.set(scene, v, t);
  // fuite de lumière aux couleurs LIMO
  C.leak = (t, d = 2.4, o = {}) => {
    const L = ab(top, { left: "-20%", top: "-10%", width: "140%", height: "120%", zIndex: 39, pointerEvents: "none", mixBlendMode: "screen", opacity: "0" });
    const A = ab(L, { inset: "-20%", background: `radial-gradient(ellipse 52% 110% at 10% 58%, rgba(255,247,230,.9), transparent 45%), radial-gradient(ellipse 72% 120% at 24% 54%, ${o.c1 || "rgba(143,107,255,.75)"}, transparent 66%)`, filter: "blur(28px)" });
    const B = ab(L, { inset: "-20%", background: `radial-gradient(ellipse 58% 105% at 78% 34%, ${o.c2 || "rgba(44,196,181,.6)"}, rgba(107,79,224,.25) 48%, transparent 76%)`, filter: "blur(40px)" });
    tl.fromTo(L, { opacity: 0 }, { opacity: o.max ?? 0.85, duration: d * 0.3, ease: "sine.out" }, t);
    tl.to(L, { opacity: 0, duration: d * 0.4, ease: "sine.in" }, t + d * 0.6);
    tl.fromTo(A, { xPercent: -20, scale: 0.92, rotation: -4 }, { xPercent: 18, scale: 1.1, rotation: 2, duration: d, ease: "sine.inOut" }, t);
    tl.fromTo(B, { xPercent: 20, yPercent: -8 }, { xPercent: -16, yPercent: 8, duration: d, ease: "sine.inOut" }, t);
    K.sfx(t, "riser", 0.08, 0, { d: Math.min(1.2, d * 0.5) });
    return L;
  };
  C.flash = (t, color = "#ffffff", a = 0.9) => {
    const f = ab(top, { left: "0", top: "0", width: "1080px", height: "1920px", zIndex: 38, background: color, opacity: "0" });
    tl.fromTo(f, { opacity: a }, { opacity: 0, duration: 0.6, ease: "power2.out", immediateRender: false }, t);
    tl.set(f, { opacity: 0 }, 0);
    return f;
  };
  // fond plein écran (dans la scène)
  C.bg = (css, t = 0) => {
    const b = ab(scene, Object.assign({ left: "-200px", top: "-200px", width: "1480px", height: "2320px" }, css));
    if (t > 0) tl.set(b, { opacity: 0 }, 0), tl.set(b, { opacity: 1 }, t);
    return b;
  };
  // ouverture en cercle d'un calque (clip-path)
  C.iris = (el, t, d = 0.9, x = 540, y = 960) => {
    tl.fromTo(el, { clipPath: `circle(0px at ${x}px ${y}px)` }, { clipPath: `circle(1500px at ${x}px ${y}px)`, duration: d, ease: "power3.inOut" }, t);
    K.sfx(t, "whoosh", 0.22, 0, { d: d, f0: 200, f1: 2600, pk: 0.5 });
  };
  // grand titre cinéma : chaque mot sort du flou ; [mot] = mot en couleur d’accent (o.accent)
  C.title = (html, css, t, o = {}) => {
    const words = html.split(" ");
    const el = ab(scene, Object.assign({ left: "60px", right: "60px", textAlign: "center", fontFamily: o.serif ? "'Source Serif 4', serif" : "Montserrat, sans-serif", fontWeight: o.serif ? "600" : "800", lineHeight: "1.12", color: o.color || "#1b1f4b", letterSpacing: o.serif ? "0" : "-0.01em" }, css),
      words.map((w) => {
        const acc = /^\[.*\]$/.test(w);
        return `<span style="display:inline-block;margin:0 .14em${acc ? ";color:" + (o.accent || "#6b4fe0") : ""}">${acc ? w.slice(1, -1) : w}</span>`;
      }).join(""));
    const ws = K.$$("span", el);
    tl.set(el, { opacity: 0 }, 0);
    tl.set(el, { opacity: 1 }, t);
    tl.fromTo(ws, { opacity: 0, filter: "blur(18px)", y: 30, scale: 1.08 }, { opacity: 1, filter: "blur(0px)", y: 0, scale: 1, duration: o.d ?? 0.8, ease: "power3.out", stagger: o.st ?? 0.09 }, t);
    if (o.snd !== false) K.sfx(t, "whoosh", 0.08, 0, { d: 0.5, f0: 300, f1: 1800, pk: 0.5 });
    return el;
  };
  C.out = (els, t, d = 0.5) => tl.to(els, { opacity: 0, filter: "blur(14px)", scale: 1.04, duration: d, ease: "power2.in" }, t);
  // reflet lumineux qui balaie un élément
  C.sweep = (el, t, d = 1.0) => {
    const s = ab(el, { inset: "0", overflow: "hidden", pointerEvents: "none", mixBlendMode: "overlay" }, `<i style="position:absolute;top:-20%;bottom:-20%;left:-45%;width:40%;background:linear-gradient(100deg,rgba(255,255,255,0),rgba(255,255,255,.95),rgba(255,255,255,0));"></i>`);
    tl.fromTo(K.$("i", s), { xPercent: 0 }, { xPercent: 420, duration: d, ease: "power2.inOut" }, t);
    K.sfx(t, "sparkle", 0.1);
    return s;
  };
  C.ab = (css, html, parent) => {
    const e = ab(parent || scene, css, html);
    K.$$("*", e).forEach((x) => ["data-layout-allow-overlap", "data-layout-allow-occlusion"].forEach((a) => x.setAttribute(a, "")));
    return e;
  };
})();
