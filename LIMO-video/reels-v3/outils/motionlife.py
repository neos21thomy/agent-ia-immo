"""« La vraie vie d'un conseiller immo » en MOTION DESIGN (retour de Thomy sur le Draw my life : « non, du motion design,
bien mieux »). Même histoire vraie, traitement pro : le ciel suit l'heure de la journée (aube → jour → coucher → nuit),
le soleil traverse l'écran puis la lune se lève, typographie cinétique géante (l'heure, puis la phrase révélée lettre
à lettre, le mot qui pique en couleur), illustrations plates animées (téléphone et notifications, café, polaroïds,
voiture, pile de papiers, cœurs, clés). Pas de pub : LIMO en petite signature à la fin. Musique, sans voix.

Usage : python3 outils/motionlife.py   (réécrit reels/motion-01-la-vraie-vie.html)
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from cine import COMMON, FACES  # noqa: E402
from premium2 import SHELL  # noqa: E402
from premium3 import CSS  # noqa: E402

NAME = "motion-01-la-vraie-vie"
DUR = 48.0
CSS_M = """
      .sky { position: absolute; inset: 0; }
      .tm { position: absolute; left: 0; right: 0; text-align: center; font-family: Montserrat, sans-serif; font-weight: 800; color: rgba(255,255,255,.95); letter-spacing: -.02em; text-shadow: 0 10px 40px rgba(0,0,0,.18); }
      .ph { position: absolute; width: 320px; height: 640px; border-radius: 54px; background: #1c1e2e; padding: 14px; box-shadow: 0 50px 90px rgba(10,10,40,.35); }
      .ph .scr { position: relative; width: 100%; height: 100%; border-radius: 42px; overflow: hidden; background: linear-gradient(160deg, #3b3f8c, #6b4fe0); }
      .ph .isl { position: absolute; left: 50%; top: 14px; width: 96px; height: 28px; margin-left: -48px; border-radius: 16px; background: #0b0c12; }
      .ntf { position: absolute; left: 14px; right: 14px; height: 92px; border-radius: 22px; background: rgba(255,255,255,.95); display: flex; align-items: center; gap: 12px; padding: 0 14px; box-shadow: 0 10px 20px rgba(0,0,0,.15); }
      .ntf i { flex: none; width: 52px; height: 52px; border-radius: 14px; background: #2cc4b5; }
      .ntf span { flex: 1; display: flex; flex-direction: column; gap: 9px; }
      .ntf b { display: block; height: 12px; width: 70%; border-radius: 6px; background: #1c1e2e; opacity: .8; }
      .ntf s { display: block; height: 10px; width: 92%; border-radius: 5px; background: #c9c9d4; }
      .bdg { position: absolute; width: 96px; height: 96px; border-radius: 50%; background: #ff4d4d; color: #fff; font-family: Montserrat, sans-serif; font-weight: 800; font-size: 50px; display: flex; align-items: center; justify-content: center; box-shadow: 0 10px 24px rgba(255,77,77,.45); }
      .card { position: absolute; border-radius: 26px; background: #fff; box-shadow: 0 30px 60px rgba(10,10,40,.25); }
      .bubble { position: relative; display: inline-block; padding: 30px 40px; border-radius: 44px 44px 44px 12px; background: #fff; color: #1c1e2e; font-family: Inter, sans-serif; font-weight: 600; font-size: 46px; line-height: 1.25; box-shadow: 0 30px 60px rgba(10,10,40,.3); }
      .sig { position: absolute; left: 0; right: 0; text-align: center; font-family: Inter, sans-serif; font-size: 27px; color: rgba(255,255,255,.75); }
"""

BODY = r"""
        tl.set([C.barT, C.barB], { opacity: 0 }, 0);
        const TOP = document.getElementById("root");
        const EO = "expo.out", EZ = "power2.inOut", BK = "back.out(1.5)";
        const ab = (css, html = "", p = TOP) => FX.ab(p, Object.assign({ position: "absolute" }, css), html);
        const show = (e, t, t1) => { tl.set(e, { opacity: 0 }, 0); tl.set(e, { opacity: 1 }, t); if (t1 != null) tl.set(e, { opacity: 0 }, t1); };
        const pop = (e, t, o = {}) => { tl.set(e, { opacity: 0 }, 0); tl.fromTo(e, { opacity: 0, scale: o.s ?? 0.5, y: o.y ?? 40, rotation: o.r ?? 0 }, { opacity: 1, scale: 1, y: 0, rotation: o.r2 ?? 0, duration: o.d ?? 0.6, ease: o.e || BK, immediateRender: false }, t); };
        const out = (e, t, d = 0.35) => tl.to(e, { opacity: 0, scale: 0.85, y: -40, filter: "blur(10px)", duration: d, ease: "power2.in" }, t);

        // ── le ciel : un dégradé par moment de la journée, en fondu
        const SK = [
          [0, "#0d1033", "#3a2a7a"], [3.0, "#e8665a", "#f7b26a"], [6.8, "#3a86d0", "#8cc8ef"], [10.6, "#2f7cd0", "#7ec4f2"],
          [14.6, "#2b78d6", "#86cdf4"], [18.4, "#3a78c9", "#9ccbea"], [22.4, "#d9783f", "#f3bf62"], [26.4, "#b8466f", "#f08a5d"],
          [30.2, "#0e1236", "#2a2166"], [34.0, "#e9953f", "#ffd27a"], [38.4, "#5a3fd0", "#2cc4b5"], [42.8, "#14123a", "#3a2a7a"],
        ];
        SK.forEach(([t, a, b], i) => {
          const s = ab({ inset: "0", background: `linear-gradient(180deg, ${a} 0%, ${b} 100%)` }); s.classList.add("sky");
          tl.set(s, { opacity: 0 }, 0); tl.to(s, { opacity: 1, duration: i ? 0.8 : 0.01, ease: "sine.inOut" }, Math.max(0, t - 0.4));
        });
        // étoiles (nuit)
        const stars = ab({ inset: "0" }, Array.from({ length: 40 }, (_, i) => `<i style="position:absolute;left:${(i * 137) % 1040 + 20}px;top:${(i * 263) % 900 + 60}px;width:${4 + (i % 3) * 2}px;height:${4 + (i % 3) * 2}px;border-radius:50%;background:#fff;opacity:${0.4 + (i % 4) * 0.15}"></i>`).join(""));
        tl.set(stars, { opacity: 0 }, 0); tl.to(stars, { opacity: 1, duration: 0.6 }, 0); tl.to(stars, { opacity: 0, duration: 0.6 }, 2.8); tl.to(stars, { opacity: 1, duration: 0.8 }, 30.0); tl.to(stars, { opacity: 0, duration: 0.6 }, 33.8); tl.to(stars, { opacity: 1, duration: 0.8 }, 42.6);
        // le soleil traverse la journée, puis la lune
        const sun = ab({ left: "0", top: "0", width: "160px", height: "160px", zIndex: 1, borderRadius: "50%", background: "radial-gradient(circle at 40% 40%, #fff6c9 0%, #ffd95a 55%, #ffb547 100%)", boxShadow: "0 0 120px 40px rgba(255,210,90,.45)" });
        tl.set(sun, { x: 40, y: 1500, opacity: 0 }, 0);
        tl.to(sun, { opacity: 1, duration: 0.4 }, 3.0);
        const SP = [[3.0, 40, 1250], [6.8, 30, 660], [10.6, 140, 40], [14.6, 460, 10], [18.4, 760, 40], [22.4, 1000, 760], [26.4, 1000, 1250]];
        SP.forEach(([t, x, y]) => tl.to(sun, { x, y, duration: 3.6, ease: "sine.inOut" }, t));
        tl.to(sun, { y: 1700, opacity: 0, duration: 1.0, ease: "power2.in" }, 29.8);
        const moon = ab({ left: "0", top: "0", width: "170px", height: "170px", borderRadius: "50%", background: "radial-gradient(circle at 35% 35%, #ffffff 0%, #fdf1c8 60%, #e8d79c 100%)", boxShadow: "0 0 90px 30px rgba(255,240,200,.25)" });
        tl.set(moon, { x: 820, y: 1500, opacity: 0 }, 0);
        tl.to(moon, { opacity: 1, y: 640, duration: 2.4, ease: "power2.out" }, 30.2); tl.to(moon, { opacity: 0, duration: 0.5 }, 33.8);
        // la ville en silhouette (fenêtres qui s'allument le soir)
        const city = ab({ left: "0", top: "1440px", width: "1080px", height: "480px" }, `<svg viewBox="0 0 1080 480" width="1080" height="480"><path d="M0 200 L60 200 L60 150 L110 110 L160 150 L160 200 L230 200 L230 120 L300 120 L300 200 L340 200 L340 90 L390 50 L440 90 L440 200 L520 200 L520 140 L600 140 L600 200 L650 200 L650 70 L740 70 L740 200 L790 200 L790 130 L840 95 L890 130 L890 200 L960 200 L960 150 L1080 150 L1080 480 L0 480 Z" fill="rgba(12,12,40,.38)"/>${[[80, 165], [250, 140], [270, 170], [360, 110], [410, 140], [545, 160], [670, 95], [700, 130], [670, 160], [815, 150], [990, 170]].map(([x, y]) => `<rect class="win" x="${x}" y="${y}" width="16" height="20" rx="3" fill="#ffd95a"/>`).join("")}<rect x="0" y="200" width="1080" height="280" fill="rgba(12,12,40,.5)"/></svg>`);
        const wins = K.$$(".win", city); tl.set(wins, { opacity: 0 }, 0); wins.forEach((w, i) => { tl.to(w, { opacity: 1, duration: 0.2 }, 27.2 + i * 0.12); tl.to(w, { opacity: 0, duration: 0.3 }, 33.8); tl.to(w, { opacity: 1, duration: 0.2 }, 42.8 + i * 0.05); });
        tl.fromTo(city, { y: 40 }, { y: 0, duration: 3, ease: "power2.out" }, 0);

        // ── typographie : l'heure géante + la phrase révélée
        const stamp = (t, t1, txt, top = 210, fs = 230) => {
          const e = ab({ left: "0", right: "0", top: top + "px", zIndex: 20 }, txt); e.classList.add("tm"); e.style.fontSize = fs + "px";
          tl.set(e, { opacity: 0 }, 0);
          tl.fromTo(e, { opacity: 0, y: 80, scale: 1.15, filter: "blur(12px)" }, { opacity: 1, y: 0, scale: 1, filter: "blur(0px)", duration: 0.55, ease: EO, immediateRender: false }, t);
          K.sfx(t, "whoosh", 0.18, 0, { d: 0.35, f0: 300, f1: 2600, pk: 0.4 });
          out(e, t1 - 0.35);
          return e;
        };
        const line = (t, t1, html, top, fs = 74, acc = "#ffe066", o = {}) => {
          const e = FX.rise(TOP, html, { top: top + "px", fontSize: fs + "px", zIndex: 21, textShadow: "0 6px 30px rgba(0,0,0,.25)", left: "50px", right: "50px" }, t, { accent: acc, snd: false, st: o.st ?? 0.02 });
          out(e, t1 - 0.35);
          return e;
        };
        const thump = (t, g = 0.3) => K.sfx(t, "thump", g);

        // ── 0 · titre
        const t0a = line(0.3, 3.2, "LA VRAIE VIE", 640, 120, "#ffe066");
        const t0b = line(0.75, 3.2, "D’UN [CONSEILLER]|[IMMO]", 790, 92, "#ffe066");
        const bar0 = ab({ left: "390px", top: "1010px", width: "300px", height: "10px", borderRadius: "6px", background: "#ffe066", zIndex: 21 });
        tl.set(bar0, { scaleX: 0 }, 0); tl.to(bar0, { scaleX: 1, duration: 0.6, ease: EO }, 1.3); out(bar0, 2.85);
        thump(0.3, 0.35);

        // ── 1 · 6:45, le téléphone vibre, 3 notifications
        stamp(3.0, 6.8, "6:45");
        line(3.5, 6.8, "Le réveil sonne.", 470);
        line(4.1, 6.8, "[Déjà] [3] [messages.]", 560, 74, "#ffe066");
        const p1 = ab({ left: "380px", top: "760px", zIndex: 10 }, `<div class="ph"><div class="scr"><div class="isl"></div>${[0, 1, 2].map((i) => `<div class="ntf n${i}" style="top:${90 + i * 108}px"><i></i><span><b></b><s></s></span></div>`).join("")}</div></div><div class="bdg" style="left:260px;top:-30px">3</div>`);
        pop(p1, 3.3, { y: 300, s: 0.9, e: EO, d: 0.8 });
        tl.to(p1, { x: 10, duration: 0.05, yoyo: true, repeat: 9, ease: "none" }, 4.0); K.sfx(4.0, "buzz", 0.35, 0, { d: 0.5 });
        K.$$(".ntf", p1).forEach((n, i) => { pop(n, 4.2 + i * 0.35, { y: -40, s: 0.8 }); K.sfx(4.2 + i * 0.35, "notif", 0.2); });
        pop(K.$(".bdg", p1), 5.2, { s: 0, y: 0, e: "back.out(3)" });
        out(p1, 6.45);

        // ── 2 · 8:00, le café refroidit
        stamp(6.8, 10.6, "8:00");
        line(7.3, 10.6, "Le café refroidit.", 470);
        line(7.9, 10.6, "[Un] [vendeur] [appelle.]", 560, 74, "#ffe066");
        const cup = ab({ left: "170px", top: "860px", width: "300px", height: "380px", zIndex: 10 }, `<svg viewBox="0 0 300 380" width="300" height="380"><g class="st" fill="none" stroke="rgba(255,255,255,.85)" stroke-width="10" stroke-linecap="round"><path d="M100 120 q-20 -30 0 -60 q20 -30 0 -60"/><path d="M150 120 q-20 -30 0 -60 q20 -30 0 -60"/><path d="M200 120 q-20 -30 0 -60 q20 -30 0 -60"/></g><path d="M250 190 q60 0 60 60 q0 60 -70 60" fill="none" stroke="#f4e9dc" stroke-width="24"/><path d="M40 150 h220 v170 q0 50 -50 50 h-120 q-50 0 -50 -50 Z" fill="#f4e9dc"/><ellipse cx="150" cy="150" rx="110" ry="22" fill="#6b4226"/><rect x="40" y="230" width="220" height="26" fill="#6b4fe0"/></svg>`);
        pop(cup, 7.1, { y: 120, e: EO, d: 0.7 });
        const steam = K.$(".st", cup); tl.fromTo(steam, { y: 10, opacity: 0.9 }, { y: -30, opacity: 0, duration: 2.2, ease: "power1.out", immediateRender: false }, 7.6);
        const p2 = ab({ left: "600px", top: "800px", zIndex: 10 }, `<div class="ph" style="width:260px;height:520px"><div class="scr" style="background:linear-gradient(160deg,#1f8a70,#2cc4b5);display:flex;flex-direction:column;align-items:center;justify-content:center;gap:24px"><div style="width:120px;height:120px;border-radius:50%;background:rgba(255,255,255,.9);color:#1f8a70;font-family:Montserrat,sans-serif;font-weight:800;font-size:44px;display:flex;align-items:center;justify-content:center">MV</div><div style="font-family:Inter,sans-serif;font-weight:600;font-size:30px;color:#fff">Vendeur</div><div style="width:110px;height:110px;border-radius:50%;background:#34c759;box-shadow:0 0 0 0 rgba(52,199,89,.6)" class="acc"></div></div></div>`);
        pop(p2, 7.9, { y: 200, r: 8, e: EO, d: 0.7 });
        [0, 1, 2].forEach((k) => { const r = ab({ left: "730px", top: "1060px", width: "20px", height: "20px", borderRadius: "50%", border: "6px solid rgba(255,255,255,.8)", zIndex: 9 }); tl.set(r, { opacity: 0 }, 0); tl.fromTo(r, { opacity: 0.9, scale: 1 }, { opacity: 0, scale: 22, duration: 1.4, ease: "power1.out", immediateRender: false }, 8.3 + k * 0.45); });
        K.sfx(8.3, "ring", 0.22, 0, { d: 1.6 });
        out(cup, 10.25); out(p2, 10.25);

        // ── 3 · 10:00, 40 ans de souvenirs
        stamp(10.6, 14.6, "10:00");
        line(11.1, 14.6, "Mme Dupuis te raconte", 470, 68);
        line(11.7, 14.6, "[40] [ans] [de] [souvenirs.]", 560, 74, "#ffe066");
        const house = (x, y, s, lit = false, z = 10) => ab({ left: x + "px", top: y + "px", width: 420 * s + "px", height: 400 * s + "px", zIndex: z }, `<svg viewBox="0 0 420 400" width="${420 * s}" height="${400 * s}"><rect x="290" y="40" width="44" height="90" fill="#8a3a3a"/><path d="M10 180 L210 20 L410 180 Z" fill="#e5484d"/><rect x="50" y="170" width="320" height="230" fill="#fff6ea"/><rect x="90" y="250" width="90" height="150" rx="8" fill="#6b4fe0"/><circle cx="160" cy="330" r="7" fill="#ffd95a"/><rect class="hw" x="230" y="220" width="100" height="90" rx="8" fill="${lit ? "#ffd95a" : "#bfe0f7"}"/><path d="M280 220 v90 M230 265 h100" stroke="#fff6ea" stroke-width="8"/></svg>`);
        const h3 = house(330, 900, 1.0);
        pop(h3, 11.0, { y: 160, e: EO, d: 0.8 });
        const POL = [[150, 880, -14, "#f7b26a"], [760, 860, 12, "#8cc8ef"], [180, 1220, 9, "#f08a5d"], [740, 1210, -10, "#b9a3ff"]];
        POL.forEach(([x, y, r, c], i) => {
          const p = ab({ left: x + "px", top: y + "px", width: "190px", height: "220px", zIndex: 11 }, `<div class="card" style="inset:0;padding:14px 14px 46px"><div style="width:100%;height:100%;border-radius:8px;background:linear-gradient(160deg, ${c}, #fff3)"></div></div>`);
          tl.set(p, { opacity: 0 }, 0);
          tl.fromTo(p, { opacity: 0, x: 540 - x - 95, y: 1050 - y, scale: 0.3, rotation: 0 }, { opacity: 1, x: 0, y: 0, scale: 1, rotation: r, duration: 0.8, ease: EO, immediateRender: false }, 12.2 + i * 0.25);
          tl.to(p, { y: -20, duration: 1.4, ease: "sine.inOut", yoyo: true, repeat: 1 }, 13.0);
          K.sfx(12.2 + i * 0.25, "shutter", 0.12);
          out(p, 14.25);
        });
        out(h3, 14.25);

        // ── 4 · 12:30, déjeuner dans la voiture
        stamp(14.6, 18.4, "12:30");
        line(15.1, 18.4, "Le déjeuner ?", 470);
        line(15.7, 18.4, "[Dans] [la] [voiture.]", 560, 74, "#ffe066");
        const road = ab({ left: "0", top: "1250px", width: "1080px", height: "14px", zIndex: 9 }, `<div style="width:100%;height:100%;background:repeating-linear-gradient(90deg,#fff 0 80px,transparent 80px 140px);opacity:.8"></div>`);
        show(road, 14.8, 18.4);
        tl.fromTo(K.$("div", road), { x: 0 }, { x: -560, duration: 3.6, ease: "none", immediateRender: false }, 14.8);
        const car = ab({ left: "280px", top: "1010px", width: "540px", height: "250px", zIndex: 10 }, `<svg viewBox="0 0 540 250" width="540" height="250"><path d="M30 150 Q30 110 80 105 L150 40 Q165 25 190 25 L360 25 Q385 25 400 45 L455 105 Q520 112 520 155 L520 185 Q520 200 505 200 L45 200 Q30 200 30 185 Z" fill="#2cc4b5"/><path d="M175 50 L130 105 L265 105 L265 50 Z M285 50 L285 105 L425 105 L380 50 Z" fill="#cfe8ff"/><rect x="40" y="140" width="40" height="18" rx="6" fill="#ffd95a"/><g class="wh"><circle cx="135" cy="200" r="46" fill="#1c1e2e"/><circle cx="135" cy="200" r="18" fill="#c9c9d4"/></g><g class="wh2"><circle cx="420" cy="200" r="46" fill="#1c1e2e"/><circle cx="420" cy="200" r="18" fill="#c9c9d4"/></g></svg>`);
        tl.set(car, { opacity: 0 }, 0); tl.fromTo(car, { opacity: 1, x: -900 }, { x: 0, duration: 0.9, ease: EO, immediateRender: false }, 15.0);
        tl.to(car, { y: -6, duration: 0.18, yoyo: true, repeat: 9, ease: "sine.inOut" }, 15.9);
        K.sfx(15.0, "whoosh", 0.3, 0, { d: 0.8, f0: 150, f1: 1800, pk: 0.6 });
        const sand = ab({ left: "640px", top: "820px", width: "400px", zIndex: 11 }, `<div class="bubble" style="font-size:64px;padding:18px 30px">🥪 vite !</div>`);
        pop(sand, 16.2, { s: 0.4, y: 30 }); K.sfx(16.2, "pop", 0.2);
        tl.to(car, { x: 1100, duration: 0.6, ease: "power3.in" }, 17.8); out(sand, 17.8);

        // ── 5 · 14:00, la visite
        stamp(18.4, 22.4, "14:00");
        line(18.9, 22.4, "Visite. Ils adorent.", 470);
        line(19.5, 22.4, "[Ils] [ne] [rappelleront] [jamais.]", 560, 70, "#ffe066");
        const HP = "M50 88 C10 60 0 35 18 18 C33 4 48 10 50 24 C52 10 67 4 82 18 C100 35 90 60 50 88 Z";
        const hearts = [[260, 1150], [420, 1050], [560, 1180], [700, 1080], [820, 1170]].map(([x, y], i) => {
          const h = ab({ left: x + "px", top: y + "px", width: "120px", height: "110px", zIndex: 10 }, `<svg viewBox="0 0 100 100" width="120" height="110"><path class="hp" d="${HP}" fill="#ff5d7d"/></svg>`);
          tl.set(h, { opacity: 0 }, 0);
          tl.fromTo(h, { opacity: 0, y: 200, scale: 0.4 }, { opacity: 1, y: -150, scale: 1, duration: 1.4, ease: "power2.out", immediateRender: false }, 19.0 + i * 0.15);
          K.sfx(19.0 + i * 0.15, "bloop-up", 0.1, 0, { f0: 500, f1: 1200, d: 0.1 });
          tl.to(K.$(".hp", h), { fill: "#9aa0b4", duration: 0.4 }, 21.0);
          tl.to(h, { y: 300, rotation: i % 2 ? 25 : -25, opacity: 0, duration: 0.9, ease: "power2.in" }, 21.2 + i * 0.05);
          return h;
        });
        const vu = ab({ left: "240px", top: "960px", width: "760px", zIndex: 12, textAlign: "right" }, `<div class="bubble" style="border-radius:44px 44px 12px 44px;background:#0a84ff;color:#fff">Alors, ça vous a plu ?</div><div style="position:absolute;right:10px;top:150px;font-family:Inter,sans-serif;font-size:30px;color:rgba(255,255,255,.85)">Vu ✓✓</div>`);
        pop(vu, 20.4, { y: 40 }); K.sfx(20.4, "send", 0.25); out(vu, 22.05);
        K.sfx(21.1, "bloop-down", 0.25, 0, { f0: 600, f1: 200, d: 0.4 });

        // ── 6 · 17:00, 47 pages
        stamp(22.4, 26.4, "17:00");
        line(22.9, 26.4, "Le notaire veut", 470);
        line(23.5, 26.4, "[47] [pages] pour hier.", 560, 78, "#ffe066");
        const pages = Array.from({ length: 9 }, (_, i) => {
          const p = ab({ left: 330 + ((i * 37) % 30) - 15 + "px", top: 1270 - i * 30 + "px", width: "420px", height: "120px", zIndex: 10 + i }, `<div class="card" style="inset:0;border-radius:10px;background:#fff;background-image:repeating-linear-gradient(180deg,transparent 0 22px,#e3e3ec 22px 28px);background-size:80% 100%;background-repeat:no-repeat;background-position:center 20px"></div>`);
          tl.set(p, { opacity: 0 }, 0);
          tl.fromTo(p, { opacity: 0, y: 260, rotation: (i % 2 ? 1 : -1) * 12 }, { opacity: 1, y: 0, rotation: (i % 3) - 1, duration: 0.45, ease: "back.out(1.6)", immediateRender: false }, 23.2 + i * 0.16);
          K.sfx(23.3 + i * 0.16, "clack", 0.1);
          out(p, 26.05);
          return p;
        });
        const cnt = ab({ left: "760px", top: "880px", zIndex: 30 }, `<div style="width:170px;height:170px;border-radius:50%;background:#ff4d4d;color:#fff;font-family:Montserrat,sans-serif;font-weight:800;font-size:78px;display:flex;align-items:center;justify-content:center;box-shadow:0 18px 40px rgba(255,77,77,.45)"><span class="n">0</span></div>`);
        pop(cnt, 23.3, { s: 0, y: 0, e: "back.out(2.5)" });
        K.count(K.$(".n", cnt), 47, 23.4, 1.5, (v) => String(Math.round(v)), {});
        tl.to(cnt, { rotation: 8, duration: 0.08, yoyo: true, repeat: 5 }, 24.9); out(cnt, 26.05);

        // ── 7 · 19:30, tu rentres, ton téléphone non
        stamp(26.4, 30.2, "19:30");
        line(26.9, 30.2, "Tu rentres.", 470);
        line(27.5, 30.2, "Ton téléphone, [lui,] [jamais.]", 560, 74, "#ffe066");
        const h7 = house(160, 920, 0.95, true);
        pop(h7, 26.7, { y: 160, e: EO, d: 0.8 });
        const p7 = ab({ left: "640px", top: "860px", zIndex: 11 }, `<div class="ph" style="width:250px;height:500px"><div class="scr"><div class="isl"></div><div style="position:absolute;inset:0;background:radial-gradient(circle at 50% 40%, rgba(255,255,255,.35), transparent 60%)"></div></div></div><div class="bdg" style="left:190px;top:-36px"><span class="n">0</span></div>`);
        pop(p7, 27.4, { y: 200, r: -8, e: EO, d: 0.7 });
        K.count(K.$(".n", p7), 12, 27.9, 1.6, (v) => String(Math.round(v)), {});
        for (let k = 0; k < 4; k++) K.sfx(28.0 + k * 0.4, "notif", 0.12);
        tl.to(p7, { x: 8, duration: 0.05, yoyo: true, repeat: 7, ease: "none" }, 28.6);
        out(h7, 29.85); out(p7, 29.85);

        // ── 8 · 22:47, la nuit
        stamp(30.2, 34.0, "22:47");
        const q = ab({ left: "90px", top: "880px", width: "900px", zIndex: 12 }, `<div class="bubble" style="font-size:54px;max-width:840px">La maison est toujours dispo ? 😅</div>`);
        pop(q, 31.0, { y: 60, s: 0.7 }); K.sfx(31.0, "receive", 0.35);
        const q2 = ab({ left: "90px", top: "1100px", width: "900px", zIndex: 12 }, `<div class="bubble" style="font-size:54px">On peut visiter demain 7h30 ?</div>`);
        pop(q2, 32.0, { y: 60, s: 0.7 }); K.sfx(32.0, "receive", 0.35);
        line(30.7, 34.0, "Toujours [connecté.]", 470, 74, "#ffe066");
        out(q, 33.65); out(q2, 33.65);

        // ── 9 · et puis un jour, les clés
        const slow = line(34.3, 38.4, "Et puis un jour…", 520, 80);
        line(35.3, 38.4, "tu tends [les] [clés.]", 640, 96, "#fff6c9");
        const keys = ab({ left: "390px", top: "880px", width: "300px", height: "300px", zIndex: 12, fontSize: "260px", lineHeight: "1", textAlign: "center" }, "🔑");
        tl.set(keys, { opacity: 0, transformOrigin: "50% 10%" }, 0);
        tl.fromTo(keys, { opacity: 0, y: -300, rotation: -40 }, { opacity: 1, y: 0, rotation: 0, duration: 1.0, ease: "elastic.out(1, 0.5)", immediateRender: false }, 35.6);
        tl.to(keys, { rotation: 8, duration: 0.8, ease: "sine.inOut", yoyo: true, repeat: 2 }, 36.6);
        K.sfx(35.7, "sparkle", 0.25);
        const sp = K.sparkles(TOP, 540, 1030, 28, 420, 340, 9); sp.forEach((s) => (s.el.style.zIndex = "13")); K.burst(sp, 36.0, false);
        out(keys, 38.05);

        // ── 10 · pourquoi
        line(38.7, 43.0, "Et tu te souviens", 520, 78);
        line(39.4, 43.0, "[pourquoi] [tu] [fais]|[ce] [métier.]", 620, 92, "#ffe066");
        const big = ab({ left: "340px", top: "930px", width: "400px", height: "380px", zIndex: 12 }, `<svg viewBox="0 0 100 100" width="400" height="380"><path d="${HP}" fill="#ff5d7d"/></svg>`);
        pop(big, 39.6, { s: 0, y: 0, e: "back.out(2)", d: 0.8 });
        tl.to(big, { scale: 1.08, duration: 0.45, ease: "sine.inOut", yoyo: true, repeat: 5 }, 40.4);
        K.sfx(39.6, "thump", 0.3); K.sfx(40.4, "thump", 0.15); K.sfx(40.9, "thump", 0.15);
        out(big, 42.65);

        // ── 11 · respect
        line(43.1, 99, "À tous les", 560, 78);
        line(43.5, 99, "[conseillers] [immo] :", 660, 92, "#ffe066");
        const rs = ab({ left: "0", right: "0", top: "800px", zIndex: 21, textAlign: "center", fontFamily: "Montserrat, sans-serif", fontWeight: "800", fontSize: "150px", color: "#fff" }, "RESPECT. 🫡");
        tl.set(rs, { opacity: 0 }, 0); tl.fromTo(rs, { opacity: 0, scale: 2.2 }, { opacity: 1, scale: 1, duration: 0.35, ease: "power4.in", immediateRender: false }, 44.3);
        K.sfx(44.62, "slam", 0.35);
        const tg = ab({ left: "0", right: "0", top: "1030px", zIndex: 21, textAlign: "center", fontFamily: "Inter, sans-serif", fontWeight: "600", fontSize: "44px", color: "rgba(255,255,255,.9)" }, "Tague un conseiller qui vit ça 👇");
        pop(tg, 45.2, { y: 20, s: 0.9, e: EO });
        const sig = ab({ left: "0", right: "0", top: "1760px", zIndex: 22 }, `<div style="display:inline-flex;align-items:center;gap:14px">avec ❤️ par <img src="assets/img/limo-logo-ad.png" alt="LIMO" style="height:44px;filter:brightness(0) invert(1);opacity:.85" /> · le bras droit du conseiller immo</div>`);
        sig.classList.add("sig"); tl.set(sig, { opacity: 0 }, 0); tl.to(sig, { opacity: 1, duration: 0.6 }, 45.6);
        window.__TE = 47.6;
"""

if __name__ == "__main__":
    html = SHELL.format(title="La vraie vie d'un conseiller immo", faces=FACES, css=(CSS + CSS_M).strip("\n"), body=(COMMON + BODY).strip("\n"), dur=DUR, name=NAME)
    (HERE.parent / "reels" / f"{NAME}.html").write_text(html, encoding="utf-8")
    print("reels/" + NAME + ".html")
