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
  // Accroche « hook » : visible dès la première image (vignette), petit coup de poing, surlignage violet
  N.hook = (lines, css, o = {}) => {
    const el = N.ab("ctr n-hook", lines.map((l) => `<span class="hk">${l}</span>`).join(""), css);
    el.setAttribute("data-layout-allow-overflow", "");
    tl.fromTo(el, { scale: 1.12 }, { scale: 1, duration: 0.45, ease: "power3.out" }, 0);
    K.sfx(0.0, "slam", o.g ?? 0.34);
    const hl = o.hl ?? 0.35;
    K.$$(".hl", el).forEach((h, i) => {
      tl.fromTo(h, { backgroundSize: "0% 100%", color: "#1b1f4b" }, { backgroundSize: "100% 100%", color: "#ffffff", duration: 0.35, ease: "power2.out" }, hl + i * 0.12);
      K.sfx(hl + i * 0.12, "whoosh", 0.1, 0, { d: 0.3, f0: 800, f1: 4200, pk: 0.6 });
    });
    const st = o.st ?? 1.2;
    K.$$(".st", el).forEach((s, i) => {
      tl.fromTo(K.$("i", s), { scaleX: 0 }, { scaleX: 1, duration: 0.28, ease: "power2.out" }, st + i * 0.14);
      K.sfx(st + i * 0.14, "clack", 0.2);
    });
    return el;
  };
  // Pastille turquoise ; à t = 0 elle est déjà là (vignette)
  N.chip = (html, css, t = 0) => {
    const el = N.ab("ctr", `<span class="n-chip">${html}</span>`, css);
    if (t > 0) {
      N.hide(el);
      tl.set(el, { opacity: 1 }, t);
      K.pop(K.$("span", el), t);
      K.sfx(t, "pop", 0.14);
    }
    return el;
  };
  /* Mascotte officielle : corps (visière vide) + yeux SVG animables.
     Repère SVG = image 747 × 904 ; yeux centrés en (215, 393) et (412, 393). */
  const EYE = "#3fe6f7";
  const EL = [215, 412], EY = 393;
  const EYES = {
    happy: EL.map((x) => `<path d="M${x - 42} ${EY + 14} A42 42 0 0 1 ${x + 42} ${EY + 14}" fill="none" stroke="${EYE}" stroke-width="17" stroke-linecap="round"/>`).join(""),
    open: EL.map((x) => `<rect x="${x - 24}" y="${EY - 44}" width="48" height="80" rx="24" fill="${EYE}"/>`).join(""),
    blink: EL.map((x) => `<path d="M${x - 34} ${EY + 6} H${x + 34}" stroke="${EYE}" stroke-width="15" stroke-linecap="round"/>`).join(""),
    wow: EL.map((x) => `<circle cx="${x}" cy="${EY}" r="40" fill="none" stroke="${EYE}" stroke-width="15"/>`).join(""),
    sad: EL.map((x, i) => `<path d="M${x - 40} ${EY - 4} A42 42 0 0 0 ${x + 40} ${EY - 4}" fill="none" stroke="${EYE}" stroke-width="15" stroke-linecap="round" transform="rotate(${i ? -12 : 12} ${x} ${EY})"/>`).join(""),
    angry: EL.map((x, i) => `<rect x="${x - 26}" y="${EY - 30}" width="52" height="60" rx="18" fill="${EYE}"/><path d="M${x - 44} ${EY - (i ? 20 : 52)} L${x + 44} ${EY - (i ? 52 : 20)}" stroke="#050607" stroke-width="30" stroke-linecap="round"/>`).join(""),
    dizzy: EL.map((x) => `<path d="M${x - 30} ${EY - 30} L${x + 30} ${EY + 30} M${x + 30} ${EY - 30} L${x - 30} ${EY + 30}" stroke="${EYE}" stroke-width="15" stroke-linecap="round"/>`).join(""),
    heart: EL.map((x) => `<path transform="translate(${x - 44} ${EY - 40}) scale(3.7)" d="M12 21s-7.5-4.6-9.6-9.2C.9 8.5 2.9 4.5 6.6 4.5c2.2 0 3.7 1.3 4.4 2.5.7-1.2 2.2-2.5 4.4-2.5 3.7 0 5.7 4 4.2 7.3C19.5 16.4 12 21 12 21z" fill="#ff6b9a"/>`).join(""),
    euro: EL.map((x) => `<text x="${x}" y="${EY + 36}" text-anchor="middle" font-family="Montserrat Hook, Montserrat, sans-serif" font-weight="800" font-size="110" fill="${EYE}">€</text>`).join(""),
    wink: `<path d="M${EL[0] - 42} ${EY + 14} A42 42 0 0 1 ${EL[0] + 42} ${EY + 14}" fill="none" stroke="${EYE}" stroke-width="17" stroke-linecap="round"/><path d="M${EL[1] - 34} ${EY + 6} H${EL[1] + 34}" stroke="${EYE}" stroke-width="15" stroke-linecap="round"/>`,
    sleep: EL.map((x) => `<path d="M${x - 40} ${EY - 6} A42 42 0 0 0 ${x + 40} ${EY - 6}" fill="none" stroke="${EYE}" stroke-width="13" stroke-linecap="round" opacity=".7"/>`).join(""),
    think: EL.map((x) => `<rect x="${x - 24}" y="${EY - 44}" width="48" height="80" rx="24" fill="${EYE}" transform="translate(18 -14)"/>`).join(""),
  };
  N.mascot = (css, o = {}) => {
    const W = parseFloat(css.width);
    const out = N.ab("m-out", `<div class="m-shadow"></div><div class="m-in"><img src="assets/img/mascotte-corps.png" alt="La mascotte LIMO" /><svg viewBox="0 0 747 904"><defs><filter id="mg${W}" filterUnits="userSpaceOnUse" x="0" y="0" width="747" height="904"><feGaussianBlur stdDeviation="7" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter><radialGradient id="ma${W}"><stop offset="0" stop-color="#bff7ff"/><stop offset="1" stop-color="#3fe6f7" stop-opacity="0"/></radialGradient></defs><circle class="ant" cx="367" cy="30" r="70" fill="url(#ma${W})"/>${Object.entries(EYES).map(([k, v]) => `<g class="e e-${k}" filter="url(#mg${W})">${v}</g>`).join("")}</svg></div>`, Object.assign({ height: (W * 904) / 747 + "px" }, css));
    out.setAttribute("data-layout-allow-overflow", "");
    out.setAttribute("data-layout-allow-overlap", "");
    const inn = K.$(".m-in", out);
    const M = { el: out, inner: inn, cur: o.expr || "happy" };
    K.$$(".e", out).forEach((g) => tl.set(g, { opacity: g.classList.contains("e-" + M.cur) ? 1 : 0 }, 0));
    tl.set(K.$(".ant", out), { opacity: 0 }, 0);
    M.expr = (name, t, snd = true) => {
      K.$$(".e", out).forEach((g) => tl.set(g, { opacity: g.classList.contains("e-" + name) ? 1 : 0 }, t));
      if (snd) K.sfx(t, "chirp", 0.1, 0, { n: 2 });
      M.cur = name;
      return M;
    };
    M.blink = (t) => {
      const c = M.cur;
      K.$$(".e", out).forEach((g) => tl.set(g, { opacity: g.classList.contains("e-blink") ? 1 : 0 }, t));
      K.$$(".e", out).forEach((g) => tl.set(g, { opacity: g.classList.contains("e-" + c) ? 1 : 0 }, t + 0.12));
      return M;
    };
    M.enter = (t, from = {}) => {
      N.hide(out);
      tl.fromTo(out, Object.assign({ opacity: 0, scale: 0.3, y: 120 }, from), { opacity: 1, scale: 1, y: 0, x: 0, duration: 0.6, ease: "back.out(1.8)" }, t);
      K.sfx(t, "bloop-up", 0.3, 0, { f0: 300, f1: 1100, d: 0.18 });
      return M;
    };
    M.float = (t, d, amp = 14) => {
      const n = Math.max(1, Math.floor(d / 1.2));
      tl.fromTo(inn, { y: 0 }, { y: -amp, duration: 0.6, ease: "sine.inOut", yoyo: true, repeat: n * 2 - 1, immediateRender: false }, t);
      return M;
    };
    M.hop = (t, h = 90) => {
      tl.to(inn, { scaleY: 0.88, scaleX: 1.08, duration: 0.1, ease: "power2.out" }, t);
      tl.to(inn, { scaleY: 1.04, scaleX: 0.97, y: -h, duration: 0.22, ease: "power2.out" }, t + 0.1);
      tl.to(inn, { scaleY: 1, scaleX: 1, y: 0, duration: 0.28, ease: "bounce.out" }, t + 0.32);
      K.sfx(t + 0.08, "bloop-up", 0.16, 0, { f0: 500, f1: 1200, d: 0.1 });
      return M;
    };
    M.tilt = (t, deg = 10, d = 0.35) => { tl.to(inn, { rotation: deg, duration: d, ease: "back.out(2)" }, t); return M; };
    M.shake = (t, d = 0.4) => {
      tl.fromTo(inn, { x: 0 }, { x: 14, duration: 0.05, ease: "none", yoyo: true, repeat: Math.round(d / 0.05), immediateRender: false }, t);
      return M;
    };
    M.wave = (t) => {
      tl.to(inn, { rotation: -10, duration: 0.18, ease: "sine.inOut" }, t);
      tl.to(inn, { rotation: 10, duration: 0.3, ease: "sine.inOut", yoyo: true, repeat: 2 }, t + 0.18);
      tl.to(inn, { rotation: 0, duration: 0.2, ease: "sine.inOut" }, t + 1.1);
      return M;
    };
    M.glow = (t, d = 1.2) => {
      tl.fromTo(K.$(".ant", out), { opacity: 0 }, { opacity: 1, duration: 0.2, yoyo: true, repeat: Math.max(1, Math.round(d / 0.2)) - 1 + (Math.round(d / 0.2) % 2 ? 0 : 1) }, t);
      tl.set(K.$(".ant", out), { opacity: 0 }, t + d + 0.25);
      K.sfx(t, "sonar", 0.1, 0, { f: 1760 });
      return M;
    };
    M.move = (t, css2, d = 0.6) => { tl.to(out, Object.assign({ duration: d, ease: "power3.inOut" }, css2), t); return M; };
    return M;
  };
  // Bulle de dialogue (la mascotte parle) ; tail : "down" | "left" | "right" | "up"
  N.say = (html, css, t, o = {}) => {
    const tail = o.tail || "down";
    const tp = { down: "left:50%;bottom:-18px;margin-left:-22px", up: "left:50%;top:-18px;margin-left:-22px", left: "left:-18px;top:50%;margin-top:-22px", right: "right:-18px;top:50%;margin-top:-22px" }[tail] + (o.tx ? `;left:${o.tx}` : "");
    const el = N.ab("n-bub2 " + (o.cls || ""), `<i class="tl" style="${tp}"></i><span style="position:relative">${html}</span>`, css);
    N.hide(el);
    tl.fromTo(el, { opacity: 0, scale: 0.6 }, { opacity: 1, scale: 1, duration: 0.35, ease: "back.out(2)" }, t);
    K.sfx(t, "chirp", o.g ?? 0.14, 0, { n: o.n ?? 4 });
    return el;
  };
  // Carte de fin sobre, au logo LIMO
  N.outro = (t, kind = "essai", o = {}) => {
    // pub : carte remontée pour rester hors des zones couvertes par l'interface des pubs Reels/Stories
    const dy = o.dy ?? (kind === "pub" || kind === "contact" ? -150 : 0);
    const Y = (v) => v + dy + "px";
    const logo = N.ab("", `<img src="assets/img/limo-logo-ad.png" alt="LIMO" style="width:100%;height:100%" />`, { left: "290px", top: Y(360), width: "500px", height: "189px" });
    N.hide(logo);
    tl.fromTo(logo, { opacity: 0, y: 30 }, { opacity: 1, y: 0, duration: 0.6, ease: "power3.out" }, t);
    K.sfx(t + 0.05, "thump", 0.3);
    const tag = N.text("ctr n-body", "Ton chef de cabinet immo.", { top: Y(600), fontSize: "40px", fontWeight: "600", color: "#1b1f4b" }, t + 0.3);
    const C = {
      dm: ["ÉCRIS-MOI <span class='n-kw'>LIMO</span>", "EN MESSAGE PRIVÉ<span class='v'>.</span>", K.icon("send") + "Je t’ouvre ton accès"],
      comment: ["COMMENTE <span class='n-kw'>LIMO</span>", "JE T’ENVOIE L’ACCÈS<span class='v'>.</span>", K.icon("msg") + "Accès offert 14 jours"],
      demo: ["RÉSERVE TA DÉMO", "DE 15 MINUTES<span class='v'>.</span>", K.icon("clock") + "Réserver ma démo"],
      essai: ["ESSAIE-LE", "14 JOURS<span class='v'>.</span>", "Commencer gratuitement →"],
      pub: ["ESSAIE LIMO", "14 JOURS OFFERTS<span class='v'>.</span>", "Essai gratuit en 2 minutes →"],
      contact: ["CONTACTE-NOUS", "ET DÉCOUVRE LIMO<span class='v'>.</span>", K.icon("send") + "Découvrir LIMO →"],
    }[kind];
    const h = N.head([C[0], C[1]], { top: Y(780), fontSize: "78px" }, t + 0.55);
    const cta = N.ab("n-cta", `<span>${C[2]}</span>`, { left: "0", right: "0", top: Y(1130) });
    N.hide(cta);
    tl.set(cta, { opacity: 1 }, t + 1.1);
    K.pop(K.$("span", cta), t + 1.1, { s: 0.8, d: 0.45, e: "back.out(1.6)" });
    K.sfx(t + 1.1, "cta", 0.18);
    const sub = N.text("ctr n-body", (kind === "demo" ? "<b>Lien en bio</b><br>" : "") + (kind === "contact" ? "<b>14 jours offerts</b> · " : "") + "Sans carte bancaire · Sans engagement<br><b>app.leadengineai.fr</b>", { top: Y(1290), fontSize: "30px" }, t + 1.35);
    return t + 3.6;
  };
})();
