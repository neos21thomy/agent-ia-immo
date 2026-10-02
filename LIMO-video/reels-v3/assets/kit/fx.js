/* LIMO — pack premium : sous-titres karaoké mot à mot, titres lettre par lettre, transitions « whip pan »
   (flou de bougé horizontal SVG), plongée dans l'écran du téléphone, fond aurore, cartes en verre dépoli.
   Techniques adaptées des blocs du registre HyperFrames (caption-pill-karaoke, whip-pan, parallax-device-dive,
   liquid-glass-notification), réécrites en 9:16 et pilotées par la timeline (déterministe, sans aléatoire). */
(function () {
  "use strict";
  const FX = (window.FX = {});
  let tl, root, defs, nid = 0;
  const NS = "http://www.w3.org/2000/svg";
  const allow = (e) => {
    [e, ...e.querySelectorAll("*")].forEach((x) => ["data-layout-allow-overflow", "data-layout-allow-overlap", "data-layout-allow-occlusion"].forEach((a) => x.setAttribute(a, "")));
    return e;
  };
  const ab = (parent, css, html) => {
    const e = document.createElement("div");
    Object.assign(e.style, { position: "absolute" }, css);
    if (html) e.innerHTML = html;
    parent.appendChild(e);
    return allow(e);
  };
  FX.init = (timeline) => {
    tl = timeline;
    root = document.getElementById("root");
    const svg = document.createElementNS(NS, "svg");
    svg.setAttribute("width", "0");
    svg.setAttribute("height", "0");
    svg.style.position = "absolute";
    defs = document.createElementNS(NS, "defs");
    svg.appendChild(defs);
    root.appendChild(svg);
  };
  FX.ab = ab;

  // ---- calque plein écran (une « scène ») visible entre t0 et t1
  FX.layer = (t0, t1, css = {}, html = "", under = false) => {
    const sec = document.getElementById("s-main");
    const l = ab(under ? sec : root, Object.assign({ left: "0", top: "0", width: "1080px", height: "1920px", overflow: "hidden" }, css), html);
    tl.set(l, { opacity: 0 }, 0);
    tl.set(l, { opacity: 1 }, t0);
    if (t1 != null) tl.set(l, { opacity: 0 }, t1);
    if (under) sec.insertBefore(l, sec.firstChild);
    return l;
  };

  // ---- fond aurore : 3 halos flous qui dérivent lentement
  FX.aurora = (parent, t0, t1, o = {}) => {
    const c = o.colors || ["#6b4fe0", "#2cc4b5", "#3a2a9a"];
    const bg = ab(parent, { inset: "0", background: o.base || "radial-gradient(ellipse at 50% 30%, #1b1745 0%, #07081a 70%)" });
    const P = [[-180, 120, 900], [420, 860, 820], [-80, 1300, 760]];
    P.forEach((p, i) => {
      const b = ab(bg, { left: p[0] + "px", top: p[1] + "px", width: p[2] + "px", height: p[2] + "px", borderRadius: "50%", background: `radial-gradient(circle, ${c[i]} 0%, rgba(0,0,0,0) 68%)`, opacity: String(o.a ?? 0.55), filter: "blur(30px)" });
      const dx = [160, -140, 120][i], dy = [90, -120, -80][i];
      tl.fromTo(b, { x: 0, y: 0, scale: 1 }, { x: dx, y: dy, scale: 1.18, duration: t1 - t0, ease: "sine.inOut" }, t0);
    });
    return bg;
  };

  // ---- carte verre dépoli (reflet supérieur + bord lumineux)
  FX.glass = (parent, css, html, o = {}) => {
    const g = ab(parent, Object.assign({
      borderRadius: "34px", padding: "26px 30px", color: "#fff",
      background: "linear-gradient(160deg, rgba(255,255,255,.26) 0%, rgba(255,255,255,.08) 55%, rgba(255,255,255,.14) 100%)",
      border: "1.5px solid rgba(255,255,255,.38)",
      boxShadow: "inset 0 1.5px 0 rgba(255,255,255,.55), inset 0 -18px 40px rgba(255,255,255,.05), 0 30px 70px rgba(4,4,20,.45)",
      backdropFilter: "blur(26px) saturate(1.7)", WebkitBackdropFilter: "blur(26px) saturate(1.7)",
      fontFamily: "Inter, sans-serif", overflow: "hidden",
    }, css), html + `<i class="fx-sheen" style="position:absolute;top:-30%;bottom:-30%;left:-60%;width:45%;background:linear-gradient(100deg,rgba(255,255,255,0),rgba(255,255,255,.38),rgba(255,255,255,0));transform:rotate(8deg)"></i>`);
    tl.set(g.querySelector(".fx-sheen"), { xPercent: 0 }, 0);
    return g;
  };
  FX.sheen = (g, t, d = 1.1) => tl.fromTo(g.querySelector(".fx-sheen"), { xPercent: 0 }, { xPercent: 420, duration: d, ease: "power2.inOut" }, t);

  // ---- titre lettre par lettre (révélation sous masque) ; [mot] = couleur d'accent
  FX.rise = (parent, html, css, t, o = {}) => {
    const lines = html.split("|");
    const el = ab(parent, Object.assign({ left: "60px", right: "60px", textAlign: "center", fontFamily: "Montserrat, sans-serif", fontWeight: "800", color: o.color || "#fff", lineHeight: "1.06", letterSpacing: "-0.015em" }, css),
      lines.map((ln) => `<div style="overflow:hidden;padding:0 .06em .08em">${ln.split(" ").map((w) => {
        const m = /^\[(.*)\]([.,;:!?…]*)$/.exec(w);
        const word = m ? m[1] : w, tail = m ? m[2] : "";
        const ch = (s, acc) => [...s].map((c) => `<span class="fx-c" style="display:inline-block${acc ? ";color:" + (o.accent || "#2cc4b5") : ""}">${c}</span>`).join("");
        return `<span style="display:inline-block;white-space:nowrap;margin:0 .13em">${ch(word, !!m)}${ch(tail, false)}</span>`;
      }).join("")}</div>`).join(""));
    const cs = el.querySelectorAll(".fx-c");
    tl.set(cs, { yPercent: 115, opacity: 0 }, 0);
    tl.to(cs, { yPercent: 0, opacity: 1, duration: 0.55, ease: "expo.out", stagger: o.st ?? 0.022 }, t);
    if (o.snd !== false) K.sfx(t, "whoosh", 0.14, 0, { d: 0.45, f0: 400, f1: 2200, pk: 0.4 });
    return el;
  };
  FX.fall = (els, t, d = 0.35) => {
    const cs = [].concat(els).flatMap((e) => [...e.querySelectorAll(".fx-c")]);
    tl.to(cs, { yPercent: -115, opacity: 0, duration: d, ease: "power3.in", stagger: 0.008 }, t);
  };

  // ---- whip pan : la scène sortante file vers la gauche avec un flou de bougé, l'entrante arrive de la droite
  const blur = () => {
    const id = "fxw" + nid++;
    const f = document.createElementNS(NS, "filter");
    f.setAttribute("id", id);
    f.setAttribute("x", "-20%"); f.setAttribute("y", "0"); f.setAttribute("width", "140%"); f.setAttribute("height", "100%");
    const g = document.createElementNS(NS, "feGaussianBlur");
    g.setAttribute("stdDeviation", "0 0");
    f.appendChild(g);
    defs.appendChild(f);
    return { id, g };
  };
  FX.whip = (from, to, t, d = 0.42, dir = 1) => {
    const a = blur(), b = blur();
    [].concat(from).forEach((e) => (e.style.filter = `url(#${a.id})`));
    [].concat(to).forEach((e) => (e.style.filter = `url(#${b.id})`));
    tl.set(a.g, { attr: { stdDeviation: "0 0" } }, 0);
    tl.set(b.g, { attr: { stdDeviation: "0 0" } }, 0);
    tl.fromTo(from, { x: 0 }, { x: -1250 * dir, duration: d, ease: "power3.in", immediateRender: false }, t);
    tl.to(a.g, { attr: { stdDeviation: "90 0" }, duration: d, ease: "power2.in" }, t);
    tl.set(from, { opacity: 0 }, t + d);
    tl.set(to, { opacity: 1 }, t + d * 0.55);
    tl.fromTo(to, { x: 1250 * dir }, { x: 0, duration: d * 1.3, ease: "power3.out", immediateRender: false }, t + d * 0.55);
    tl.fromTo(b.g, { attr: { stdDeviation: "90 0" } }, { attr: { stdDeviation: "0 0" }, duration: d * 1.3, ease: "power2.out", immediateRender: false }, t + d * 0.55);
    K.sfx(t, "whoosh", 0.32, 0, { d: d * 1.6, f0: 160, f1: 3200, pk: 0.5 });
  };

  // ---- plongée dans l'écran : la caméra fonce vers un point du téléphone, flash, scène suivante
  FX.dive = (el, x, y, t, d = 0.75, scale = 5.5) => {
    el.style.transformOrigin = `${x}px ${y}px`;
    tl.to(el, { scale, duration: d, ease: "power3.in" }, t);
    tl.to(el, { filter: "blur(10px)", duration: d * 0.4, ease: "power1.in" }, t + d * 0.6);
    const f = ab(root, { left: "0", top: "0", width: "1080px", height: "1920px", background: "#ffffff", zIndex: 37 });
    tl.set(f, { opacity: 0 }, 0);
    tl.to(f, { opacity: 0.85, duration: d * 0.25, ease: "power2.in" }, t + d * 0.75);
    tl.to(f, { opacity: 0, duration: 0.5, ease: "power2.out" }, t + d);
    K.sfx(t, "whoosh", 0.3, 0, { d: d, f0: 120, f1: 2600, pk: 0.8 });
    K.sfx(t + d, "thump", 0.3);
  };

  // ---- sous-titres karaoké : groupes de 4 mots max, le mot prononcé s'allume
  // segs = [[t0, t1, "texte"]] (temps absolus du film) ; les temps des mots sont répartis selon leur longueur
  FX.karaoke = (segs, o = {}) => {
    const top = o.top ?? 1440, maxW = o.max ?? 4;
    const keys = (o.keys || []).map((k) => k.toLowerCase());
    segs.forEach(([t0, t1, txt]) => {
      const words = txt.split(" ");
      const w8 = words.map((w) => w.replace(/[^\p{L}\p{N}]/gu, "").length + 1.5);
      const tot = w8.reduce((a, b) => a + b, 0);
      let acc = t0;
      const tw = words.map((w, i) => { const s = acc; acc += (t1 - t0) * w8[i] / tot; return [s, acc]; });
      for (let i = 0; i < words.length; i += maxW) {
        const gw = words.slice(i, i + maxW), gt = tw.slice(i, i + maxW);
        const g0 = gt[0][0], g1 = Math.min(gt[gt.length - 1][1] + 0.12, i + maxW < words.length ? tw[i + maxW][0] : t1 + 0.25);
        const box = ab(root, { left: "0", right: "0", top: top + "px", textAlign: "center", zIndex: 36 },
          `<span class="fx-pill" style="display:inline-block;padding:16px 30px 18px;border-radius:26px;background:${o.light ? "rgba(255,255,255,.94)" : "rgba(10,10,30,.72)"};box-shadow:0 14px 34px rgba(0,0,0,.28);font-family:Montserrat,sans-serif;font-weight:800;font-size:${o.fs || 54}px;line-height:1.15;white-space:nowrap">${gw.map((w) => `<span class="fx-w" style="display:inline-block;margin:0 .17em;color:${o.light ? "#a6a8c2" : "rgba(255,255,255,.45)"}">${w}</span>`).join("")}</span>`);
        tl.set(box, { opacity: 0 }, 0);
        tl.fromTo(box, { opacity: 0, y: 18, scale: 0.96 }, { opacity: 1, y: 0, scale: 1, duration: 0.16, ease: "power2.out", immediateRender: false }, g0);
        tl.to(box, { opacity: 0, duration: 0.1 }, g1);
        box.querySelectorAll(".fx-w").forEach((s, j) => {
          const key = keys.some((k) => gw[j].toLowerCase().includes(k));
          const on = key ? (o.accent || "#2cc4b5") : (o.light ? "#1b1f4b" : "#ffffff");
          tl.to(s, { color: on, y: -5, duration: 0.08, ease: "power1.out" }, gt[j][0]);
          tl.to(s, { y: 0, duration: 0.12, ease: "power1.out" }, gt[j][1]);
        });
      }
    });
  };
})();
