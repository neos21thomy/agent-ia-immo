/* LIMO — kit de composants pour Reels HyperFrames.
   - Tout est déterministe (aucun hasard, aucune horloge) et « seek-safe » (fromTo à l'entrée, to ensuite).
   - Chaque composant : K.xxx(parent, options) → { el, play(t) → instant de fin }.
   - Chaque animation déclare ses sons via K.sfx(t, type, gain, pan, extra) → window.__sfx,
     lu par outils/extract-sfx.mjs puis synthétisé par outils/sfx.py (son parfaitement calé). */
(function () {
  "use strict";
  const NS = "http://www.w3.org/2000/svg";
  const K = (window.K = {});
  const events = (window.__sfx = window.__sfx || []);
  let tl = null;
  let uidN = 0;
  const uid = () => "u" + uidN++;

  K.init = (timeline) => {
    tl = timeline;
    K.tl = timeline;
    injectSprite();
    return K;
  };
  K.sfx = (t, k, g = 1, p = 0, x) => {
    events.push(Object.assign({ t: Math.round(t * 1000) / 1000, k, g, p }, x || {}));
  };
  K.h = (tag, cls, html, parent) => {
    const e = document.createElement(tag);
    if (cls) e.className = cls;
    if (html != null) e.innerHTML = html;
    if (parent) parent.appendChild(e);
    return e;
  };
  K.$ = (s, r = document) => r.querySelector(s);
  K.$$ = (s, r = document) => Array.from(r.querySelectorAll(s));
  K.icon = (n) => `<svg class="i"><use href="#i-${n}"/></svg>`;
  K.nb = (s) => s.replace(/(\d) (\d{3})/g, "$1 $2").replace(/ (€|%)/g, " $1");
  const CHK = `<span class="ring"></span><span class="bg"></span><svg viewBox="0 0 40 40"><path d="M12 20.5l6 6L28.5 14.5" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/></svg>`;
  K.CHK = CHK;
  const ROBOT = `<svg viewBox="0 0 64 64"><line x1="32" y1="19" x2="32" y2="12" stroke="#15131f" stroke-width="2.4"/><circle cx="32" cy="10" r="3.6" fill="#00C6FC"/><ellipse cx="32" cy="36" rx="19" ry="17" fill="#F5F4FA"/><rect x="18.5" y="27" width="27" height="14.5" rx="7.2" fill="#0B0B12"/><path d="M23.8 35.6a2.9 2.9 0 0 1 5.8 0M34.4 35.6a2.9 2.9 0 0 1 5.8 0" fill="none" stroke="#00C6FC" stroke-width="2.3" stroke-linecap="round"/></svg>`;
  K.ROBOT = ROBOT;
  const STATUS = `<svg viewBox="0 0 112 24" fill="currentColor"><rect x="0" y="15" width="5" height="7" rx="1.5"/><rect x="8" y="11" width="5" height="11" rx="1.5"/><rect x="16" y="7" width="5" height="15" rx="1.5"/><rect x="24" y="3" width="5" height="19" rx="1.5"/><path d="M40 10.5a14 14 0 0 1 20 0M44 14.5a8 8 0 0 1 12 0M48.5 18.5a2 2 0 0 1 3 0" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round"/><rect x="70" y="4" width="36" height="17" rx="5" fill="none" stroke="currentColor" stroke-opacity=".55" stroke-width="2"/><rect x="73" y="7" width="27" height="11" rx="2.5"/><rect x="108" y="9.5" width="2.5" height="6" rx="1" fill-opacity=".55"/></svg>`;

  /* ------------------------------------------------------------ icônes */
  const ICONS = {
    reply: '<path d="M9 14 4 9l5-5"/><path d="M4 9h10.5a5.5 5.5 0 0 1 0 11H11"/>',
    file: '<path d="M15 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7Z"/><path d="M14 2v4a2 2 0 0 0 2 2h4"/><path d="M16 13H8"/><path d="M16 17H8"/>',
    cake: '<path d="M20 21v-8a2 2 0 0 0-2-2H6a2 2 0 0 0-2 2v8"/><path d="M4 16s.5-1 2-1 2.5 2 4 2 2.5-2 4-2 2.5 2 4 2 2-1 2-1"/><path d="M2 21h20"/><path d="M7 8v3"/><path d="M12 8v3"/><path d="M17 8v3"/>',
    zap: '<path d="M4 14a1 1 0 0 1-.78-1.63l9.9-10.2a.5.5 0 0 1 .86.46l-1.92 6.02A1 1 0 0 0 13 10h7a1 1 0 0 1 .78 1.63l-9.9 10.2a.5.5 0 0 1-.86-.46l1.92-6.02A1 1 0 0 0 11 14z"/>',
    bank: '<path d="M3 22h18"/><path d="M6 18v-7"/><path d="M10 18v-7"/><path d="M14 18v-7"/><path d="M18 18v-7"/><path d="M12 2 20 7H4z"/>',
    users: '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/>',
    mic: '<path d="M12 2a3 3 0 0 0-3 3v7a3 3 0 0 0 6 0V5a3 3 0 0 0-3-3Z"/><path d="M19 10v2a7 7 0 0 1-14 0v-2"/><path d="M12 19v3"/>',
    clock: '<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>',
    pin: '<path d="M20 10c0 5-5.5 10.2-7.4 11.8a1 1 0 0 1-1.2 0C9.5 20.2 4 15 4 10a8 8 0 0 1 16 0"/><circle cx="12" cy="10" r="3"/>',
    radar: '<circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/><path d="m13.4 10.6 5.7-5.7"/>',
    mail: '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7"/>',
    home: '<path d="M15 21v-8a1 1 0 0 0-1-1h-4a1 1 0 0 0-1 1v8"/><path d="M3 10a2 2 0 0 1 .7-1.5l7-6a2 2 0 0 1 2.6 0l7 6A2 2 0 0 1 21 10v9a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/>',
    phone: '<path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.8 19.8 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.12 4.18 2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.13.96.36 1.9.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.91.34 1.85.57 2.81.7A2 2 0 0 1 22 16.92z"/>',
    msg: '<path d="M7.9 20A9 9 0 1 0 4 16.1L2 22Z"/>',
    wa: '<path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>',
    send: '<path d="m22 2-7 20-4-9-9-4Z"/><path d="M22 2 11 13"/>',
    scale: '<path d="m16 16 3-8 3 8c-.87.65-1.92 1-3 1s-2.13-.35-3-1Z"/><path d="m2 16 3-8 3 8c-.87.65-1.92 1-3 1s-2.13-.35-3-1Z"/><path d="M7 21h10"/><path d="M12 3v18"/><path d="M3 7h2c2 0 5-1 7-2 2 1 5 2 7 2h2"/>',
    camera: '<path d="M14.5 4h-5L7 7H4a2 2 0 0 0-2 2v9a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V9a2 2 0 0 0-2-2h-3l-2.5-3z"/><circle cx="12" cy="13" r="3"/>',
    sparkles: '<path d="M9.94 15.5A2 2 0 0 0 8.5 14.06l-6.14-1.58a.5.5 0 0 1 0-.96L8.5 9.94A2 2 0 0 0 9.94 8.5l1.58-6.14a.5.5 0 0 1 .96 0L14.06 8.5A2 2 0 0 0 15.5 9.94l6.14 1.58a.5.5 0 0 1 0 .96L15.5 14.06a2 2 0 0 0-1.44 1.44l-1.58 6.14a.5.5 0 0 1-.96 0z"/>',
    check: '<path d="M20 6 9 17l-5-5"/>',
    plus: '<path d="M12 5v14"/><path d="M5 12h14"/>',
    car: '<path d="M19 17h2c.6 0 1-.4 1-1v-3c0-.9-.7-1.7-1.5-1.9C18.7 10.6 16 10 16 10s-1.3-1.4-2.2-2.3c-.5-.4-1.1-.7-1.8-.7H5c-.6 0-1.1.4-1.4.9l-1.4 2.9A3.7 3.7 0 0 0 2 12v4c0 .6.4 1 1 1h2"/><circle cx="7" cy="17" r="2"/><path d="M9 17h6"/><circle cx="17" cy="17" r="2"/>',
    magnet: '<path d="m6 15-4-4 6.75-6.77a7.79 7.79 0 0 1 11 11L13 22l-4-4 6.39-6.36a2.14 2.14 0 0 0-3-3L6 15"/><path d="m5 8 4 4"/><path d="m12 15 4 4"/>',
    megaphone: '<path d="m3 11 18-5v12L3 14v-3z"/><path d="M11.6 16.8a3 3 0 1 1-5.8-1.6"/>',
    sofa: '<path d="M20 9V6a2 2 0 0 0-2-2H6a2 2 0 0 0-2 2v3"/><path d="M2 16a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2v-5a2 2 0 0 0-4 0v1.5a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5V11a2 2 0 0 0-4 0z"/><path d="M4 18v2"/><path d="M20 18v2"/>',
    wrench: '<path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z"/>',
    target: '<circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/>',
    clip: '<rect width="8" height="4" x="8" y="2" rx="1"/><path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2"/>',
    refresh: '<path d="M3 12a9 9 0 0 1 15-6.7L21 8"/><path d="M21 3v5h-5"/><path d="M21 12a9 9 0 0 1-15 6.7L3 16"/><path d="M3 21v-5h5"/>',
    euro: '<path d="M18 7c-1.2-1.3-2.9-2-4.8-2C9.4 5 6.5 8.1 6.5 12s2.9 7 6.7 7c1.9 0 3.6-.7 4.8-2"/><path d="M4 10h9"/><path d="M4 14h9"/>',
    gift: '<rect x="3" y="8" width="18" height="4" rx="1"/><path d="M12 8v13"/><path d="M19 12v7a2 2 0 0 1-2 2H7a2 2 0 0 1-2-2v-7"/><path d="M7.5 8a2.5 2.5 0 0 1 0-5C10 3 12 8 12 8s2-5 4.5-5a2.5 2.5 0 0 1 0 5"/>',
    shield: '<path d="M20 13c0 5-3.5 7.5-7.66 8.95a1 1 0 0 1-.67-.01C7.5 20.5 4 18 4 13V6a1 1 0 0 1 1-1c2 0 4.5-1.2 6.24-2.72a1.17 1.17 0 0 1 1.52 0C14.51 3.81 17 5 19 5a1 1 0 0 1 1 1z"/>',
    chev: '<path d="m9 18 6-6-6-6"/>',
    x: '<path d="M18 6 6 18"/><path d="m6 6 12 12"/>',
    pen: '<path d="M12 20h9"/><path d="M16.5 3.5a2.12 2.12 0 0 1 3 3L7 19l-4 1 1-4Z"/>',
    bell: '<path d="M6 8a6 6 0 0 1 12 0c0 7 3 9 3 9H3s3-2 3-9"/><path d="M10.3 21a1.94 1.94 0 0 0 3.4 0"/>',
    search: '<circle cx="11" cy="11" r="8"/><path d="m21 21-4.3-4.3"/>',
    timer: '<path d="M10 2h4"/><path d="M12 14l3-3"/><circle cx="12" cy="14" r="8"/>',
    trophy: '<path d="M6 9H4.5a2.5 2.5 0 0 1 0-5H6"/><path d="M18 9h1.5a2.5 2.5 0 0 0 0-5H18"/><path d="M4 22h16"/><path d="M10 14.66V17c0 .55-.47.98-.97 1.21C7.85 18.75 7 20.24 7 22"/><path d="M14 14.66V17c0 .55.47.98.97 1.21C16.15 18.75 17 20.24 17 22"/><path d="M18 2H6v7a6 6 0 0 0 12 0V2Z"/>',
    alert: '<path d="m21.73 18-8-14a2 2 0 0 0-3.48 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.73-3"/><path d="M12 9v4"/><path d="M12 17h.01"/>',
    calc: '<rect x="4" y="2" width="16" height="20" rx="2"/><path d="M8 6h8"/><path d="M16 14v4"/><path d="M16 10h.01"/><path d="M12 10h.01"/><path d="M8 10h.01"/><path d="M12 14h.01"/><path d="M8 14h.01"/><path d="M12 18h.01"/><path d="M8 18h.01"/>',
    note: '<path d="M15.5 3H5a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2V8.5Z"/><path d="M15 3v6h6"/>',
    tabs: '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="M2 9h20"/><path d="M6 6.5h.01"/><path d="M9 6.5h.01"/>',
    book: '<path d="M2 6h4"/><path d="M2 10h4"/><path d="M2 14h4"/><path d="M2 18h4"/><rect x="4" y="2" width="16" height="20" rx="2"/><path d="M16 2v20"/>',
    help: '<circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"/><path d="M12 17h.01"/>',
    hourglass: '<path d="M5 22h14"/><path d="M5 2h14"/><path d="M17 22v-4.17a2 2 0 0 0-.59-1.42L12 12l-4.41 4.41A2 2 0 0 0 7 17.83V22"/><path d="M7 2v4.17a2 2 0 0 0 .59 1.42L12 12l4.41-4.41A2 2 0 0 0 17 6.17V2"/>',
    image: '<rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="9" cy="9" r="2"/><path d="m21 15-3.1-3.1a2 2 0 0 0-2.8 0L6 21"/>',
    star: '<path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/>',
  };
  function injectSprite() {
    if (document.getElementById("k-sprite")) return;
    const s = document.createElementNS(NS, "svg");
    s.setAttribute("id", "k-sprite");
    s.setAttribute("width", "0");
    s.setAttribute("height", "0");
    s.setAttribute("aria-hidden", "true");
    s.style.position = "absolute";
    s.innerHTML = "<defs>" + Object.entries(ICONS).map(([k, v]) => `<symbol id="i-${k}" viewBox="0 0 24 24">${v}</symbol>`).join("") + "</defs>";
    document.body.insertBefore(s, document.body.firstChild);
  }

  /* ------------------------------------------------------------ illustration maison */
  K.houseArt = (w, h, id) => {
    const g = "sky" + (id || uid());
    return `<svg viewBox="0 0 400 300" width="${w}" height="${h}" preserveAspectRatio="xMidYMid slice"><defs><linearGradient id="${g}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#8fd3ff"/><stop offset="1" stop-color="#fde6c8"/></linearGradient></defs><rect width="400" height="300" fill="url(#${g})"/><circle cx="318" cy="66" r="28" fill="#fff3c4"/><path d="M0 214 Q100 176 200 204 T400 194 V300 H0Z" fill="#a8d69a"/><rect x="0" y="244" width="400" height="56" fill="#86c47a"/><rect x="66" y="206" width="8" height="42" fill="#7a5a3a"/><circle cx="70" cy="192" r="34" fill="#5fae5a"/><rect x="328" y="214" width="7" height="34" fill="#7a5a3a"/><circle cx="331" cy="202" r="26" fill="#6cb866"/><rect x="120" y="140" width="160" height="108" fill="#f6efe3"/><polygon points="108,146 200,84 292,146" fill="#c8553d"/><rect x="244" y="96" width="16" height="30" fill="#a8432f"/><rect x="185" y="194" width="30" height="54" rx="3" fill="#6b4f3a"/><rect x="138" y="164" width="32" height="26" rx="3" fill="#ffe29a"/><rect x="230" y="164" width="32" height="26" rx="3" fill="#ffe29a"/><path d="M154 164v26M138 177h32M246 164v26M230 177h32" stroke="#f6efe3" stroke-width="3"/><rect x="110" y="246" width="180" height="6" fill="#d8cbb4"/></svg>`;
  };

  /* ------------------------------------------------------------ animations de base */
  K.fin = (el, t, o = {}) => tl.fromTo(el, { opacity: 0, y: o.y ?? 26 }, { opacity: 1, y: 0, duration: o.d ?? 0.45, ease: o.e ?? "power3.out", stagger: o.st ?? 0 }, t);
  K.pop = (el, t, o = {}) => tl.fromTo(el, { opacity: 0, scale: o.s ?? 0.55 }, { opacity: 1, scale: 1, duration: o.d ?? 0.42, ease: o.e ?? "back.out(1.9)", stagger: o.st ?? 0 }, t);
  K.fout = (el, t, o = {}) => tl.to(el, { opacity: 0, y: o.y ?? -26, duration: o.d ?? 0.28, ease: "power2.in" }, t);
  K.type = (el, text, t, dur, g = 0.05) => {
    el.textContent = "";
    const P = { n: 0 };
    tl.to(P, { n: text.length, duration: dur, ease: "none", onUpdate: () => { el.textContent = text.slice(0, Math.round(P.n)); } }, t);
    const step = Math.max(0.05, dur / 16);
    for (let i = 0, x = t; x < t + dur - 0.02; i++, x += step) K.sfx(x, "type", g, ((i * 5) % 7 - 3) / 8, { f: 2600 + ((i * 7) % 5) * 180 });
  };
  const INV = {
    "power3.out": (v) => 1 - Math.pow(1 - v, 1 / 4),
    "power2.out": (v) => 1 - Math.pow(1 - v, 1 / 3),
    "power1.out": (v) => 1 - Math.sqrt(1 - v),
    none: (v) => v,
  };
  K.eur = (v) => String(Math.round(v / 100) * 100).replace(/\B(?=(\d{3})+(?!\d))/g, " ") + " €";
  K.count = (el, to, t, dur, fmt, o = {}) => {
    const ease = o.ease || "power3.out";
    const P = { v: o.from || 0 };
    el.textContent = fmt(P.v);
    tl.to(P, { v: to, duration: dur, ease, onUpdate: () => { el.textContent = fmt(P.v); } }, t);
    const n = o.ticks ?? 16;
    for (let k = 1; k <= n; k++) K.sfx(t + dur * INV[ease](k / n), "tick", (o.g ?? 0.1) + 0.06 * (k / n), 0, { f: 1200 + 1400 * (k / n) });
  };
  K.checkAnim = (chk, t, snd = "success", g = 0.24) => {
    tl.fromTo(chk.querySelector(".bg"), { scale: 0 }, { scale: 1, duration: 0.34, ease: "back.out(2.2)" }, t);
    tl.fromTo(chk.querySelector("path"), { strokeDashoffset: 1 }, { strokeDashoffset: 0, duration: 0.26, ease: "power2.out" }, t + 0.1);
    if (snd) K.sfx(t, snd, g);
  };
  K.tapAt = (host, x, y, t) => {
    const tp = K.h("span", "k-tap", null, host);
    tp.style.left = x + "px";
    tp.style.top = y + "px";
    tl.fromTo(tp, { scale: 0.4, opacity: 0 }, { scale: 0.6, opacity: 1, duration: 0.06, ease: "none" }, t);
    tl.to(tp, { scale: 2.6, opacity: 0, duration: 0.5, ease: "power2.out" }, t + 0.06);
    K.sfx(t, "tap", 0.4);
  };
  K.dots = (el, t, dur) => {
    tl.fromTo(el, { opacity: 0 }, { opacity: 1, duration: 0.16 }, t);
    K.$$("i", el).forEach((d, i) => tl.fromTo(d, { y: 0 }, { y: -9, duration: 0.14, ease: "sine.inOut", yoyo: true, repeat: Math.max(1, Math.floor((dur - 0.1) / 0.28) * 2 - 1) }, t + 0.05 + i * 0.07));
    tl.to(el, { opacity: 0, duration: 0.14 }, t + dur);
  };

  /* ------------------------------------------------------------ décor */
  K.bg = (parent, o = {}) => {
    const dur = o.dur || 30;
    const light = o.light;
    const grid = K.h("div", "k-grid", null, parent);
    const a = K.h("div", "k-glow", null, parent);
    const b = K.h("div", "k-glow", null, parent);
    [grid, a, b].forEach((x) => x.setAttribute("data-layout-allow-overflow", ""));
    Object.assign(a.style, { left: "260px", top: "-420px", width: "1300px", height: "1300px", background: light ? "radial-gradient(circle, rgba(107,79,224,.18) 0%, rgba(107,79,224,0) 62%)" : "radial-gradient(circle, rgba(0,198,252,.2) 0%, rgba(0,198,252,0) 62%)" });
    Object.assign(b.style, { left: "-640px", top: "960px", width: "1400px", height: "1400px", background: light ? "radial-gradient(circle, rgba(0,168,216,.14) 0%, rgba(0,168,216,0) 62%)" : "radial-gradient(circle, rgba(120,90,252,.17) 0%, rgba(120,90,252,0) 62%)" });
    tl.fromTo(grid, { y: 0 }, { y: -48, duration: dur, ease: "none" }, 0);
    tl.fromTo(a, { opacity: 0, scale: 1 }, { opacity: 1, scale: 1.1, duration: 2.2, ease: "sine.inOut" }, 0);
    tl.to(a, { scale: 1, duration: 2.2, ease: "sine.inOut", yoyo: true, repeat: Math.max(1, Math.floor((dur - 2.4) / 2.2) - 1) }, 2.2);
    tl.fromTo(b, { opacity: 0, x: -60, y: 60 }, { opacity: 1, x: 60, y: -60, duration: dur, ease: "none" }, 0);
    return { grid, a, b };
  };
  K.wordmark = (parent, o = {}) => {
    const s = o.size || 46;
    const el = K.h("div", "k-wm", `<span class="t" style="font-size:${s}px;letter-spacing:.06em">LIM</span><svg viewBox="0 0 36 36" style="width:${s * 0.78}px;height:${s * 0.78}px;margin-left:2px"><circle cx="18" cy="18" r="13.8" fill="none" stroke="#00C6FC" stroke-width="6.4"/></svg>`, parent);
    el.style.position = "absolute";
    el.style.left = (o.x ?? 84) + "px";
    el.style.top = (o.y ?? 150) + "px";
    return el;
  };
  K.phone = (parent, o = {}) => {
    let host = parent;
    if (o.scale && o.scale !== 1) {
      host = K.h("div", "abs", null, parent);
      Object.assign(host.style, { left: "0", top: "0", width: "1080px", height: "1920px", transformOrigin: `540px ${o.y ?? 690}px`, transform: `scale(${o.scale})` });
      host.setAttribute("data-layout-allow-overflow", "");
    }
    const ph = K.h("div", "k-phone", null, host);
    ph.setAttribute("data-layout-allow-overflow", "");
    ph.style.left = (o.x ?? 190) + "px";
    ph.style.top = (o.y ?? 690) + "px";
    ph.innerHTML = `<div class="k-screen"><div class="k-status"><span class="k-time">${o.time || "8:00"}</span><span class="k-island"></span>${STATUS}</div><div class="k-slot"></div></div>`;
    return { el: ph, screen: K.$(".k-screen", ph), slot: K.$(".k-slot", ph), time: K.$(".k-time", ph) };
  };
  K.stage = (parent, o = {}) => {
    const outer = K.h("div", "abs", null, parent);
    Object.assign(outer.style, { left: (o.x ?? 0) + "px", top: (o.y ?? 0) + "px", width: "608px", height: (o.h ?? 600) + "px", transformOrigin: "0 0", transform: `scale(${o.scale ?? 1})` });
    const inner = K.h("div", "abs k-stage", null, outer);
    Object.assign(inner.style, { left: "0", top: "0", width: "608px", height: (o.h ?? 600) + "px" });
    return inner;
  };
  K.lines = (parent, lines, o = {}) => {
    const el = K.h("div", "abs", null, parent);
    Object.assign(el.style, { left: (o.x ?? 84) + "px", top: (o.y ?? 236) + "px", width: (o.w ?? 912) + "px", fontFamily: "Anton, sans-serif", fontSize: (o.size ?? 112) + "px", color: "var(--fg)", textAlign: o.align || "left" });
    el.innerHTML = lines.map((l) => `<span class="mask" data-layout-allow-overflow style="line-height:1.32;margin-bottom:-.22em"><span data-layout-allow-occlusion ${l.cls ? `class="${l.cls}"` : ""}>${l.t ?? l}</span></span>`).join("");
    return el;
  };
  K.linesIn = (el, t, snd = true) => {
    const ss = K.$$(".mask > span", el);
    tl.fromTo(ss, { yPercent: 115 }, { yPercent: 0, duration: 0.6, ease: "expo.out", stagger: 0.08 }, t);
    if (snd) ss.forEach((s, i) => K.sfx(t - 0.04 + i * 0.08, "whoosh", 0.12, i % 2 ? 0.3 : -0.3, { d: 0.32, f0: 700, f1: 5000, pk: 0.7 }));
  };
  K.sparkles = (parent, cx, cy, n, rx, ry, seed) => {
    const colors = ["#00C6FC", "#FFFFFF", "#9EEBFF"];
    const out = [];
    for (let i = 0; i < n; i++) {
      const size = 14 + ((i * 7 + seed) % 4) * 5;
      const s = document.createElementNS(NS, "svg");
      s.setAttribute("viewBox", "0 0 20 20");
      s.setAttribute("class", "k-spk");
      Object.assign(s.style, { left: cx - size / 2 + "px", top: cy - size / 2 + "px", width: size + "px", height: size + "px" });
      s.innerHTML = `<path d="M10 0 L12.2 7.8 L20 10 L12.2 12.2 L10 20 L7.8 12.2 L0 10 L7.8 7.8 Z" fill="${colors[(i + seed) % 3]}"/>`;
      parent.appendChild(s);
      const a = (i / n) * Math.PI * 2 + (((i * 5 + seed) % 7) - 3) * 0.06;
      const r = 1 + ((i * 37 + seed * 11) % 50) / 100;
      out.push({ el: s, dx: Math.cos(a) * rx * r, dy: Math.sin(a) * ry * r, rot: (i % 2 ? 1 : -1) * (60 + ((i * 13) % 50)) });
    }
    return out;
  };
  K.burst = (list, t, snd = true) => {
    list.forEach((s, i) => {
      const t0 = t + (i % 5) * 0.015;
      tl.fromTo(s.el, { x: 0, y: 0, scale: 0, rotation: 0, opacity: 1 }, { x: s.dx * 0.72, y: s.dy * 0.72, scale: 1, rotation: s.rot * 0.6, duration: 0.34, ease: "power2.out" }, t0);
      tl.to(s.el, { x: s.dx, y: s.dy, scale: 0.3, rotation: s.rot, opacity: 0, duration: 0.55, ease: "power1.in" }, t0 + 0.34);
    });
    if (snd) K.sfx(t, "sparkle", 0.2);
  };

  /* ------------------------------------------------------------ 1 · brief du matin */
  K.brief = (parent, o = {}) => {
    const rows = o.rows || [
      ["reply", "Rappeler M. Albert", "Il attend ton appel", "9:30", 1],
      ["home", "Visite chez les Martin", "Maison 120 m² · Brive", "10:45"],
      ["file", "Mandat Dupont : J-15", "Proposer le renouvellement", "11:30"],
      ["cake", "Anniversaire de Mme Roy", "SMS prêt à envoyer", "12:00"],
      ["zap", "DPE caduc · maison Delmas", "Réalisé avant juillet 2021", "15:00"],
    ];
    const el = K.h("div", "kb", null, parent);
    el.innerHTML = `<div class="k-head"><div><div class="k-title">Aujourd’hui</div><div class="k-sub">${o.sub || "8:00 · ton brief est prêt"}</div></div><div class="kb-count" data-layout-allow-overlap><span class="c1" data-layout-allow-overlap>5 à faire</span><span class="c2" data-layout-allow-overlap>4 à faire</span></div></div><div class="kb-list">${rows
      .map((r, i) => `<div class="kb-row k-card"><div class="k-ic ${r[4] ? "cy" : ""}">${K.icon(r[0])}</div><div class="kb-t"><b>${r[1]}${i === 0 ? '<i class="kb-strike"></i>' : ""}</b><span>${r[2]}</span></div><div class="kb-time">${r[3]}</div><div class="k-chk">${i === 0 ? CHK : '<span class="ring"></span>'}</div></div>`)
      .join("")}</div>`;
    const play = (t) => {
      K.fin(K.$(".k-head", el), t, { y: 16 });
      const rs = K.$$(".kb-row", el);
      K.fin(rs, t + 0.12, { y: 34, st: 0.08 });
      rs.forEach((r, i) => K.sfx(t + 0.16 + i * 0.08, "pop", 0.07, -0.4 + i * 0.2, { f: 440 + i * 60 }));
      K.tapAt(rs[0], 568, 46, t + 1.0);
      K.checkAnim(K.$(".k-chk", rs[0]), t + 1.06);
      tl.fromTo(K.$(".kb-strike", rs[0]), { scaleX: 0 }, { scaleX: 1, duration: 0.34, ease: "power2.inOut" }, t + 1.16);
      tl.to([K.$(".kb-t", rs[0]), K.$(".k-ic", rs[0]), K.$(".kb-time", rs[0])], { opacity: 0.4, duration: 0.3 }, t + 1.2);
      tl.to(K.$(".c1", el), { yPercent: -100, opacity: 0, duration: 0.26, ease: "power2.in" }, t + 1.3);
      tl.fromTo(K.$(".c2", el), { yPercent: 100, opacity: 0 }, { yPercent: 0, opacity: 1, duration: 0.34, ease: "back.out(1.6)" }, t + 1.34);
      K.sfx(t + 1.34, "tick", 0.12, 0, { f: 1900 });
      return t + 1.75;
    };
    return { el, play };
  };

  /* ------------------------------------------------------------ 2 · dictée → fiche */
  K.dictee = (parent, o = {}) => {
    const text = o.text || "Visite Martin : maison 120 m² à Brive, ils vendent en mars.";
    const rows = o.rows || [["Vendeurs", "Famille Martin"], ["Bien", "Maison 120 m² · Brive"], ["Projet", "Vente en mars"], ["Relance", "Dans 7 jours"]];
    const el = K.h("div", "kd", null, parent);
    el.innerHTML = `<div class="kd-bubble"><div class="kd-txt">${text.split(" ").map((w) => `<span class="w" style="display:inline-block">${w}</span>`).join(" ")}</div><div class="kd-listen">${K.icon("mic")}<div class="kd-wave">${"<i></i>".repeat(16)}</div></div></div><div class="kd-card k-card"><div class="kd-card-h"><div class="k-ic cy">${K.icon("users")}</div><b>${o.title || "Fiche vendeur créée"}</b><div class="k-chk">${CHK}</div></div>${rows.map((r) => `<div class="kd-row"><span>${r[0]}</span><b>${r[1]}</b></div>`).join("")}</div>`;
    const bub = K.$(".kd-bubble", el);
    tl.set(bub, { clipPath: "inset(39px 0px 39px 268px round 36px 36px 36px 36px)" }, 0);
    const play = (t) => {
      tl.fromTo(bub, { opacity: 0, scale: 0.86 }, { opacity: 1, scale: 1, duration: 0.36, ease: "back.out(1.8)" }, t);
      K.sfx(t, "bloop-up", 0.3);
      K.$$(".kd-wave i", el).forEach((b, i) => {
        const amp = 0.3 + 0.7 * Math.abs(Math.sin(i * 1.37 + 0.4));
        const d = 0.13 + (0.05 * ((i * 7) % 5)) / 4;
        tl.fromTo(b, { scaleY: 0.18 }, { scaleY: amp, duration: d, ease: "sine.inOut", yoyo: true, repeat: Math.max(1, Math.floor(0.7 / d) - 1) }, t + 0.06 + (i % 4) * 0.02);
      });
      K.sfx(t + 0.08, "voice", 0.06, 0, { d: 0.7 });
      tl.to(bub, { clipPath: "inset(0px 0px 0px 0px round 28px 28px 10px 28px)", duration: 0.45, ease: "power3.inOut" }, t + 0.8);
      tl.to(K.$(".kd-listen", el), { opacity: 0, duration: 0.18 }, t + 0.8);
      K.sfx(t + 0.78, "bloop-down", 0.2);
      const ws = K.$$(".w", el);
      tl.fromTo(ws, { opacity: 0, y: 8 }, { opacity: 1, y: 0, duration: 0.28, ease: "power2.out", stagger: 0.03 }, t + 0.85);
      ws.forEach((w, i) => { if (i % 2 === 0) K.sfx(t + 0.85 + i * 0.03, "type", 0.05, 0, { f: 3000 + (i % 3) * 200 }); });
      const card = K.$(".kd-card", el);
      K.fin(card, t + 1.4, { y: 30 });
      K.sfx(t + 1.4, "receive", 0.2);
      K.fin(K.$$(".kd-row", el), t + 1.5, { y: 12, st: 0.07, d: 0.3 });
      K.checkAnim(K.$(".k-chk", card), t + 1.82);
      return t + 2.25;
    };
    return { el, play };
  };

  K.fiche = (parent, o = {}) => {
    const rows = o.rows || [["Vendeurs", "Famille Martin"], ["Bien", "Maison 120 m² · Brive"], ["Projet", "Vente en mars"], ["Relance", "Dans 7 jours"]];
    const el = K.h("div", "kd-card k-card", `<div class="kd-card-h"><div class="k-ic cy">${K.icon("users")}</div><b>${o.title || "Fiche vendeur créée"}</b><div class="k-chk">${CHK}</div></div>${rows.map((r) => `<div class="kd-row"><span>${r[0]}</span><b>${r[1]}</b></div>`).join("")}`, parent);
    el.style.top = "0px";
    const play = (t) => {
      K.fin(el, t, { y: 26 });
      K.sfx(t, "receive", 0.2);
      K.fin(K.$$(".kd-row", el), t + 0.1, { y: 12, st: 0.07, d: 0.3 });
      K.checkAnim(K.$(".k-chk", el), t + 0.45);
      return t + 0.95;
    };
    return { el, play };
  };

  /* ------------------------------------------------------------ 3 · document → fiche */
  K.doc = (parent, o = {}) => {
    const rows = o.rows || [["Acquéreurs", "M. et Mme Roche"], ["Notaire", "Me Faure"], ["Prix", "245 000 €"], ["Honoraires", "12 000 € TTC"], ["Anniversaire", "14 mars"]];
    const el = K.h("div", "kdoc", null, parent);
    if (o.fieldsOnly) {
      el.innerHTML = `<div class="kdoc-fields k-card" style="top:0">${rows.map((r) => `<div class="kdoc-row"><span>${r[0]}</span><b>${K.nb(r[1])}</b><div class="k-chk">${CHK}</div></div>`).join("")}</div><div class="kdoc-foot" style="top:356px"><span class="k-chip ok">${K.icon("check")}Fiche remplie automatiquement</span></div>`;
      const playF = (t) => {
        K.fin(K.$(".kdoc-fields", el), t, { y: 24 });
        K.sfx(t, "receive", 0.2);
        K.$$(".kdoc-row", el).forEach((r, i) => {
          tl.fromTo(r, { opacity: 0, x: -14 }, { opacity: 1, x: 0, duration: 0.3, ease: "power2.out" }, t + 0.1 + i * 0.12);
          K.checkAnim(K.$(".k-chk", r), t + 0.16 + i * 0.12, "tick", 0.12);
        });
        K.pop(K.$(".kdoc-foot .k-chip", el), t + 0.85);
        K.sfx(t + 0.85, "success", 0.2);
        return t + 1.3;
      };
      return { el, play: playF };
    }
    el.innerHTML = `<div class="kdoc-file k-card"><div class="kdoc-pdf">PDF</div><div class="kdoc-name"><b>${o.file || "Compromis_Roche.pdf"}</b><span>12 pages · déposé à l’instant</span></div><i class="kdoc-scan"></i></div><div class="kdoc-fields k-card">${rows.map((r) => `<div class="kdoc-row"><span>${r[0]}</span><b>${K.nb(r[1])}</b><div class="k-chk">${CHK}</div></div>`).join("")}</div><div class="kdoc-foot"><span class="k-chip ok">${K.icon("check")}Fiche remplie automatiquement</span></div>`;
    const play = (t) => {
      tl.fromTo(K.$(".kdoc-file", el), { opacity: 0, y: -70 }, { opacity: 1, y: 0, duration: 0.45, ease: "back.out(1.6)" }, t);
      K.sfx(t + 0.2, "drop", 0.3);
      const sc = K.$(".kdoc-scan", el);
      tl.fromTo(sc, { y: 0, opacity: 0 }, { y: 114, opacity: 1, duration: 0.6, ease: "power1.inOut" }, t + 0.35);
      tl.to(sc, { opacity: 0, duration: 0.15 }, t + 0.95);
      K.sfx(t + 0.35, "scan", 0.12, 0, { d: 0.6 });
      K.fin(K.$(".kdoc-fields", el), t + 0.82, { y: 24 });
      K.$$(".kdoc-row", el).forEach((r, i) => {
        tl.fromTo(r, { opacity: 0, x: -14 }, { opacity: 1, x: 0, duration: 0.3, ease: "power2.out" }, t + 0.92 + i * 0.13);
        K.checkAnim(K.$(".k-chk", r), t + 0.98 + i * 0.13, "tick", 0.12);
      });
      K.pop(K.$(".kdoc-foot .k-chip", el), t + 1.72);
      K.sfx(t + 1.72, "success", 0.22);
      return t + 2.15;
    };
    return { el, play };
  };

  /* ------------------------------------------------------------ 4 · estimation */
  K.estim = (parent, o = {}) => {
    const el = K.h("div", "ke", null, parent);
    el.innerHTML = `<div class="ke-h"><div class="k-title">Estimation</div><div class="k-sub">${o.addr || "12 rue des Lilas · Brive · maison 120 m²"}</div></div><div class="ke-hero k-card"><div class="ke-lbl">VALEUR ESTIMÉE</div><div class="ke-num"><span>0 €</span></div><div class="ke-range"><i class="track"></i><i class="fill"></i><i class="mk"></i></div><div class="ke-rl"><span>${K.nb("298 000 €")}</span><span>${K.nb("326 000 €")}</span></div></div><div class="ke-stats"><span class="k-chip">${K.icon("bank")}14 ventes DVF</span><span class="k-chip ok">Confiance ${K.nb("84 %")}</span><span class="k-chip vi">Net vendeur 297 k€</span></div>`;
    const play = (t) => {
      K.fin(K.$(".ke-h", el), t, { y: 16 });
      K.fin(K.$(".ke-hero", el), t + 0.1, { y: 26 });
      const num = K.$(".ke-num span", el);
      K.count(num, 312000, t + 0.25, 1.1, K.eur);
      tl.fromTo(num, { scale: 0.64 }, { scale: 1, duration: 1.1, ease: "power3.out" }, t + 0.25);
      tl.fromTo(K.$(".ke-range .fill", el), { scaleX: 0 }, { scaleX: 1, duration: 0.7, ease: "power3.out" }, t + 0.55);
      tl.fromTo(K.$(".ke-range .mk", el), { x: -203, opacity: 0 }, { x: 0, opacity: 1, duration: 0.75, ease: "power3.out" }, t + 0.6);
      K.sfx(t + 0.55, "whoosh", 0.12, 0.3, { d: 0.4, f0: 500, f1: 4000, pk: 0.4 });
      K.fin(K.$(".ke-rl", el), t + 0.95, { y: 8 });
      const chips = K.$$(".ke-stats .k-chip", el);
      K.pop(chips, t + 1.3, { st: 0.09 });
      chips.forEach((c, i) => K.sfx(t + 1.3 + i * 0.09, "pop", 0.13, -0.4 + i * 0.4, { f: 560 + i * 110 }));
      return t + 1.9;
    };
    return { el, play };
  };

  /* ------------------------------------------------------------ 5 · détecteur de ventes */
  K.detect = (parent, o = {}) => {
    const pins = [
      [170, 120, "F", "#F0822D", "#1B1B1B"],
      [382, 214, "G", "#E53935", "#FFFFFF"],
      [505, 96, "E", "#F4C20D", "#1B1B1B"],
    ];
    const roads = ["M0 44 L604 22", "M0 147 L604 126", "M204 0 L228 296", "M404 0 L420 296", "M0 279 L604 255", "M150 296 L470 0"];
    const big = ["M0 88 L604 64", "M62 0 L146 296", "M318 0 L296 296", "M0 183 C 200 170, 400 196, 604 160", "M474 0 L556 296"];
    const el = K.h("div", "kt", null, parent);
    el.innerHTML = `<div class="kt-h"><div class="k-title">Détecteur de ventes</div><div class="k-sub">Brive · 7 derniers jours</div></div><div class="kt-map" data-layout-allow-overflow><svg viewBox="0 0 604 296"><path class="kt-river" d="M-20 226 C 90 204, 160 262, 260 238 S 430 172, 520 196 S 620 226, 640 218" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/>${roads.map((d) => `<path class="kt-road s" d="${d}" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/>`).join("")}${big.map((d) => `<path class="kt-road" d="${d}" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/>`).join("")}${pins
      .map((p) => `<g class="kt-pin" data-x="${p[0]}" data-y="${p[1]}"><circle class="pl" cx="${p[0]}" cy="${p[1]}" r="12" fill="none" stroke="#00C6FC" stroke-width="3" opacity="0"/><circle cx="${p[0]}" cy="${p[1]}" r="22" fill="rgba(0,198,252,0.2)"/><circle cx="${p[0]}" cy="${p[1]}" r="10" fill="#00C6FC" stroke="#FFFFFF" stroke-width="3"/><rect x="${p[0] + 16}" y="${p[1] - 40}" width="36" height="30" rx="8" fill="${p[3]}"/><text x="${p[0] + 34}" y="${p[1] - 18}" text-anchor="middle" fill="${p[4]}" font-family="Inter" font-weight="700" font-size="19">${p[2]}</text></g>`)
      .join("")}</svg><div class="kt-badge">${K.icon("radar")}3 nouveaux DPE</div></div><div class="kt-lead k-card"><div class="k-ic cy">${K.icon("pin")}</div><div class="tx"><b>Nouvelle piste</b><span>22 rue des Démonstrations · DPE F</span></div><span class="k-chip vi">Boîtage J+7</span></div>`;
    const play = (t) => {
      K.fin(K.$(".kt-h", el), t, { y: 16 });
      K.fin(K.$(".kt-map", el), t + 0.08, { y: 20 });
      tl.fromTo(K.$(".kt-river", el), { strokeDashoffset: 1 }, { strokeDashoffset: 0, duration: 0.8, ease: "power2.inOut" }, t + 0.15);
      tl.fromTo(K.$$(".kt-road", el), { strokeDashoffset: 1 }, { strokeDashoffset: 0, duration: 0.6, ease: "power2.inOut", stagger: 0.035 }, t + 0.2);
      K.sfx(t + 0.15, "whoosh", 0.14, 0, { d: 0.9, f0: 250, f1: 2400, pk: 0.55 });
      K.$$(".kt-pin", el).forEach((g, i) => {
        const x = g.dataset.x;
        const y = g.dataset.y;
        const tp = t + 0.62 + i * 0.14;
        tl.fromTo(g, { scale: 0, svgOrigin: `${x} ${y}` }, { scale: 1, svgOrigin: `${x} ${y}`, duration: 0.42, ease: "back.out(2.2)" }, tp);
        const pl = K.$(".pl", g);
        tl.fromTo(pl, { opacity: 0, attr: { r: 12 } }, { opacity: 0.85, attr: { r: 12 }, duration: 0.02, ease: "none" }, tp + 0.1);
        tl.to(pl, { opacity: 0, attr: { r: 42 }, duration: 0.8, ease: "power1.out", repeat: 1 }, tp + 0.12);
        K.sfx(tp, "sonar", 0.18, [-0.5, 0.1, 0.5][i], { f: [1318.5, 1174.7, 1568][i] });
      });
      K.pop(K.$(".kt-badge", el), t + 1.05, { s: 0.7 });
      K.sfx(t + 1.05, "pop", 0.18, -0.4, { f: 680 });
      K.fin(K.$(".kt-lead", el), t + 1.3, { y: 40 });
      K.sfx(t + 1.3, "whoosh", 0.14, 0, { d: 0.4, f0: 300, f1: 2200, pk: 0.5 });
      K.pop(K.$(".kt-lead .k-chip", el), t + 1.52);
      return t + 2.0;
    };
    return { el, play };
  };

  /* ------------------------------------------------------------ 6 · annonce SEO */
  K.annonce = (parent, o = {}) => {
    const title = o.title || "Maison familiale lumineuse avec jardin";
    const body = o.body || "À 5 min du centre de Brive, maison de 120 m² : 4 chambres, séjour traversant et jardin de 700 m² sans vis-à-vis.";
    const el = K.h("div", "ka k-card", null, parent);
    el.innerHTML = `<div class="ka-top"><span class="k-chip vi">${K.icon("pen")}Annonce générée</span><span class="k-chip ok">${K.icon("clock")}10 s</span></div><div class="ka-title"></div><div class="ka-body"></div><div class="ka-legal">${K.nb("312 000 €")} honoraires inclus · 4 % TTC à la charge de l’acquéreur · DPE C · GES A</div><div class="ka-badges"><span class="k-chip ok">${K.icon("check")}SEO optimisé</span><span class="k-chip ok">${K.icon("check")}Mentions légales</span></div>`;
    const play = (t) => {
      K.fin(el, t, { y: 24 });
      K.pop(K.$$(".ka-top .k-chip", el), t + 0.1, { st: 0.08 });
      K.type(K.$(".ka-title", el), title, t + 0.2, 0.45, 0.06);
      K.type(K.$(".ka-body", el), K.nb(body), t + 0.62, 1.0, 0.045);
      K.fin(K.$(".ka-legal", el), t + 1.55, { y: 8 });
      K.pop(K.$$(".ka-badges .k-chip", el), t + 1.7, { st: 0.1 });
      K.sfx(t + 1.7, "success", 0.2);
      return t + 2.2;
    };
    return { el, play };
  };

  /* ------------------------------------------------------------ 7 · posts réseaux */
  K.posts = (parent, o = {}) => {
    const nets = [
      ["Instagram", "#E1306C", "Prêt à publier", 0, "À vendre à Brive : maison 120 m² avec jardin"],
      ["Facebook", "#1877F2", "Prêt à publier", 0, "Nouveauté : maison familiale lumineuse"],
      ["LinkedIn", "#0A66C2", "Publié", 1, "Nouveau mandat exclusif à Brive"],
    ];
    const id = uid();
    const el = K.h("div", "kp", null, parent);
    el.innerHTML =
      nets.map((n, i) => `<div class="kp-tile k-card"><div class="kp-net"><i style="background:${n[1]}"></i>${n[0]}</div><div class="kp-img">${K.houseArt(166, 150, id + "p" + i)}</div><div class="kp-cap">${n[4]}</div><div class="kp-bar"></div><div class="kp-bar" style="width:70%"></div><div class="kp-st ${n[3] ? "ok" : ""}">${n[3] ? K.icon("check") : ""}${n[2]}</div></div>`).join("") +
      `<div class="kp-note">Instagram et Facebook : prêts à copier · LinkedIn : publié en direct</div>`;
    const play = (t) => {
      const tiles = K.$$(".kp-tile", el);
      K.pop(tiles, t, { s: 0.7, st: 0.12 });
      tiles.forEach((x, i) => K.sfx(t + i * 0.12, "pop", 0.15, -0.5 + i * 0.5, { f: 520 + i * 90 }));
      const st = K.$$(".kp-st", el);
      K.fin(st.slice(0, 2), t + 0.6, { y: 8, st: 0.08 });
      tl.fromTo(st[2], { opacity: 0, scale: 1.7 }, { opacity: 1, scale: 1, duration: 0.3, ease: "power4.in" }, t + 1.0);
      K.sfx(t + 1.28, "success", 0.22, 0.5);
      K.fin(K.$(".kp-note", el), t + 1.2, { y: 8 });
      return t + 1.7;
    };
    return { el, play };
  };

  /* ------------------------------------------------------------ 8 · photo habillée « VENDU » */
  K.photo = (parent, o = {}) => {
    const el = K.h("div", "kph", null, parent);
    el.innerHTML = `<div class="kph-frame" data-layout-allow-overflow>${K.houseArt(608, 400, uid())}<div class="kph-logo">TON LOGO</div><div class="kph-banner">Ton nom <span>06 00 00 00 00</span></div><div class="kph-stamp">${o.stamp || "VENDU"}</div><i class="kph-flash"></i></div>`;
    const play = (t) => {
      const fr = K.$(".kph-frame", el);
      tl.fromTo(fr, { opacity: 0, scale: 0.94 }, { opacity: 1, scale: 1, duration: 0.4, ease: "power3.out" }, t);
      const fl = K.$(".kph-flash", el);
      tl.fromTo(fl, { opacity: 0 }, { opacity: 0.9, duration: 0.04, ease: "none" }, t + 0.05);
      tl.to(fl, { opacity: 0, duration: 0.35, ease: "power1.out" }, t + 0.09);
      K.sfx(t + 0.05, "shutter", 0.3);
      tl.fromTo(K.$(".kph-banner", el), { y: 62 }, { y: 0, duration: 0.35, ease: "power3.out" }, t + 0.35);
      K.sfx(t + 0.35, "whoosh", 0.12, 0, { d: 0.3, f0: 800, f1: 3000, pk: 0.5 });
      K.pop(K.$(".kph-logo", el), t + 0.5, { s: 0.6 });
      tl.fromTo(K.$(".kph-stamp", el), { opacity: 0, scale: 2.3, rotation: -4 }, { opacity: 1, scale: 1, rotation: -12, duration: 0.26, ease: "power4.in" }, t + 0.8);
      tl.fromTo(fr, { x: 0 }, { x: 7, duration: 0.04, ease: "none", yoyo: true, repeat: 5 }, t + 1.06);
      K.sfx(t + 1.06, "stamp", 0.45);
      return t + 1.55;
    };
    return { el, play };
  };

  /* ------------------------------------------------------------ 9 · avis Google */
  K.avis = (parent, o = {}) => {
    const star = `<svg viewBox="0 0 24 24"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z" fill="#F5B400"/></svg>`;
    const reply = o.reply || "Merci Marie ! Ravi de vous avoir accompagnés. Belle installation dans votre nouvelle maison !";
    const el = K.h("div", "kv", null, parent);
    el.innerHTML = `<div class="kv-rev k-card"><div class="kv-who"><div class="kv-av">ML</div><div><b>Marie L.</b><div class="kv-stars">${star.repeat(5)}</div></div><div class="kv-src">Avis Google · il y a 2 h</div></div><div class="kv-txt">« Accompagnement au top, maison vendue en 3 semaines. Merci ! »</div></div><div class="kv-rep k-card"><div class="kv-rep-h">${K.icon("sparkles")}Réponse proposée par LIMO</div><div class="kv-rep-t"></div></div><div class="kv-foot"><span class="k-chip ok">${K.icon("check")}Réponse publiée</span></div>`;
    const play = (t) => {
      K.fin(K.$(".kv-rev", el), t, { y: 24 });
      K.sfx(t, "pop", 0.14, 0, { f: 600 });
      const ss = K.$$(".kv-stars svg", el);
      K.pop(ss, t + 0.15, { s: 0.2, st: 0.06, d: 0.3 });
      ss.forEach((s, i) => K.sfx(t + 0.15 + i * 0.06, "tick", 0.09, -0.4 + i * 0.2, { f: 1800 + i * 220 }));
      K.fin(K.$(".kv-rep", el), t + 0.6, { y: 24 });
      K.sfx(t + 0.6, "whoosh", 0.12, 0, { d: 0.35, f0: 400, f1: 2400, pk: 0.5 });
      K.type(K.$(".kv-rep-t", el), reply, t + 0.7, 0.85, 0.045);
      K.pop(K.$(".kv-foot .k-chip", el), t + 1.65);
      K.sfx(t + 1.65, "success", 0.22);
      return t + 2.1;
    };
    return { el, play };
  };

  /* ------------------------------------------------------------ 10 · SMS en 1 tap */
  K.sms = (parent, o = {}) => {
    const msg = o.msg || "Bonjour Madame Roy, joyeux anniversaire ! Belle journée à vous.";
    const el = K.h("div", "ks", null, parent);
    el.innerHTML = `<div class="ks-to">À : <b>Mme Roy</b><span class="k-chip vi">${K.icon("cake")}Anniversaire</span></div><div class="ks-compose"><div class="ks-txt"></div><div class="ks-send">${K.icon("send")}</div></div><div class="ks-sent">${msg}</div><div class="ks-ok">${K.icon("check")}Envoyé</div><div class="ks-acts"><span class="k-chip">${K.icon("phone")}Appeler</span><span class="k-chip">${K.icon("msg")}SMS</span><span class="k-chip">${K.icon("wa")}WhatsApp</span><span class="k-chip">${K.icon("mail")}Email</span></div>`;
    const play = (t) => {
      K.fin(K.$(".ks-to", el), t, { y: 14 });
      K.fin(K.$(".ks-compose", el), t + 0.08, { y: 18 });
      const tx = K.$(".ks-txt", el);
      K.type(tx, msg, t + 0.2, 0.8, 0.045);
      const sb = K.$(".ks-send", el);
      tl.fromTo(sb, { scale: 1 }, { scale: 0.84, duration: 0.08, ease: "power2.in" }, t + 1.05);
      tl.to(sb, { scale: 1, duration: 0.26, ease: "back.out(3)" }, t + 1.13);
      K.sfx(t + 1.05, "tap", 0.35);
      tl.to(tx, { opacity: 0, duration: 0.14 }, t + 1.12);
      tl.fromTo(K.$(".ks-sent", el), { opacity: 0, y: 40, scale: 0.9 }, { opacity: 1, y: 0, scale: 1, duration: 0.36, ease: "back.out(1.6)" }, t + 1.15);
      K.sfx(t + 1.15, "send", 0.28);
      K.fin(K.$(".ks-ok", el), t + 1.4, { y: 6 });
      const acts = K.$$(".ks-acts .k-chip", el);
      K.pop(acts, t + 1.5, { st: 0.07 });
      acts.forEach((a, i) => K.sfx(t + 1.5 + i * 0.07, "pop", 0.08, -0.5 + i * 0.33, { f: 620 + i * 80 }));
      return t + 2.0;
    };
    return { el, play };
  };

  /* ------------------------------------------------------------ 11 · droit immobilier */
  K.droit = (parent, o = {}) => {
    const el = K.h("div", "kl", null, parent);
    if (o.answerOnly) {
      el.innerHTML = `<div class="kl-a k-card" style="top:0"><p><b>Non.</b> Un DPE réalisé en 2020 n’est plus valable depuis le 1er janvier 2025 : il faut en refaire un avant la mise en vente.</p><span class="k-chip ok">${K.icon("scale")}Réglementation 2025-2026</span></div>`;
      const playA = (t) => {
        K.fin(K.$(".kl-a", el), t, { y: 20 });
        K.sfx(t, "receive", 0.22);
        K.pop(K.$(".kl-a .k-chip", el), t + 0.55);
        K.sfx(t + 0.55, "success", 0.16);
        return t + 1.05;
      };
      return { el, play: playA };
    }
    el.innerHTML = `<div class="kl-q">${o.q || "Le DPE de 2020 de mon vendeur est encore valable ?"}</div><div class="kl-dots k-dots"><i></i><i></i><i></i></div><div class="kl-a k-card"><p><b>Non.</b> Un DPE réalisé en 2020 n’est plus valable depuis le 1er janvier 2025 : il faut en refaire un avant la mise en vente.</p><span class="k-chip ok">${K.icon("scale")}Réglementation 2025-2026</span></div>`;
    const play = (t) => {
      tl.fromTo(K.$(".kl-q", el), { opacity: 0, y: 30, scale: 0.92 }, { opacity: 1, y: 0, scale: 1, duration: 0.36, ease: "back.out(1.6)" }, t);
      K.sfx(t, "send", 0.26);
      K.dots(K.$(".kl-dots", el), t + 0.3, 0.45);
      K.fin(K.$(".kl-a", el), t + 0.8, { y: 20 });
      K.sfx(t + 0.8, "receive", 0.22);
      K.pop(K.$(".kl-a .k-chip", el), t + 1.35);
      K.sfx(t + 1.35, "success", 0.16);
      return t + 1.9;
    };
    return { el, play };
  };

  /* ------------------------------------------------------------ notification */
  K.notif = (parent, o = {}) => {
    const el = K.h("div", "kn", `<div class="kn-ic">${ROBOT}</div><div class="kn-b"><div class="kn-top"><b>LIMO</b><span>${o.when || "maintenant"}</span></div><div class="kn-t">${o.title || "Ton brief du matin est prêt"}</div><div class="kn-x">${o.text || "5 actions prioritaires · 1 rappel urgent"}</div></div>`, parent);
    const play = (t) => {
      tl.fromTo(el, { opacity: 0, y: -150, scale: 0.94 }, { opacity: 1, y: 0, scale: 1, duration: 0.55, ease: "back.out(1.5)" }, t);
      K.sfx(t + 0.1, "notif", 0.3);
      return t + 0.6;
    };
    return { el, play };
  };

  /* ------------------------------------------------------------ écran de fin : robot + offre */
  K.endCard = (parent, t, o = {}) => {
    const glow = K.h("div", "kend-glow", null, parent);
    const shadow = K.h("div", "kend-shadow", null, parent);
    const rob = K.h("div", "kend-robot", `<img src="assets/img/limo-robot.png" alt="Robot mascotte LIMO" />`, parent);
    const spkR = K.sparkles(parent, 540, 540, 14, 250, 250, 1);
    const wm = K.h("div", "k-wm kend-wm", `<span class="t"><span class="lm" data-layout-allow-overflow><span data-layout-allow-occlusion>L</span></span><span class="lm" data-layout-allow-overflow><span data-layout-allow-occlusion>I</span></span><span class="lm" data-layout-allow-overflow><span data-layout-allow-occlusion>M</span></span></span><svg viewBox="0 0 128 128"><circle cx="64" cy="64" r="52" fill="none" style="stroke:var(--cyan)" stroke-width="23" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1" transform="rotate(-90 64 64)"/></svg>`, parent);
    const tag = K.h("div", "kend-tag", o.tag || "Le bras droit du conseiller immo.", parent);
    const cta = K.h("div", "kend-cta", `<span class="kend-sheen"></span><span class="t">${o.cta || "14 jours gratuits"}</span>`, parent);
    cta.setAttribute("data-layout-allow-overflow", "");
    const spkC = K.sparkles(parent, 540, 1174, 16, 380, 120, 3);
    const url = K.h("div", "kend-url", "app.leadengineai.fr", parent);
    tl.fromTo(glow, { opacity: 0, scale: 0.7 }, { opacity: 1, scale: 1, duration: 1.0, ease: "power2.out" }, t);
    K.sfx(t, "riser", 0.16, 0, { d: 0.45 });
    tl.fromTo(rob, { opacity: 0, scale: 0.5, y: 70 }, { opacity: 1, scale: 1, y: 0, duration: 0.6, ease: "back.out(1.7)" }, t + 0.1);
    tl.fromTo(shadow, { opacity: 0, scale: 0.5 }, { opacity: 1, scale: 1, duration: 0.5, ease: "power2.out" }, t + 0.15);
    K.sfx(t + 0.18, "thump", 0.5);
    K.sfx(t + 0.22, "bloop-up", 0.26, 0, { f0: 260, f1: 780, d: 0.16 });
    K.burst(spkR, t + 0.2);
    tl.fromTo(K.$("img", rob), { y: 0, rotation: 0 }, { y: -12, rotation: 1.6, duration: 0.8, ease: "sine.inOut", yoyo: true, repeat: 1 }, t + 0.72);
    tl.to(shadow, { scale: 0.86, opacity: 0.7, duration: 0.8, ease: "sine.inOut", yoyo: true, repeat: 1 }, t + 0.72);
    tl.fromTo(K.$$(".lm > span", wm), { yPercent: 110 }, { yPercent: 0, duration: 0.6, ease: "expo.out", stagger: 0.07 }, t + 0.45);
    tl.fromTo(K.$("circle", wm), { strokeDashoffset: 1 }, { strokeDashoffset: 0, duration: 0.55, ease: "power2.inOut" }, t + 0.6);
    K.sfx(t + 0.42, "whoosh", 0.12, 0, { d: 0.4, f0: 600, f1: 3500, pk: 0.5 });
    K.fin(tag, t + 0.85, { y: 18, d: 0.5 });
    K.pop(cta, t + 1.1, { s: 0.7, d: 0.55, e: "back.out(1.7)" });
    K.sfx(t + 1.1, "pop", 0.24, 0, { f: 500 });
    K.sfx(t + 1.18, "cta", 0.2);
    K.burst(spkC, t + 1.15);
    tl.fromTo(K.$(".kend-sheen", cta), { x: -200 }, { x: 760, duration: 0.9, ease: "power2.inOut" }, t + 1.5);
    K.sfx(t + 1.5, "whoosh", 0.05, 0, { d: 0.8, f0: 3000, f1: 9000, pk: 0.5 });
    K.fin(url, t + 1.35, { y: 10 });
    return t + 3.0;
  };
})();
