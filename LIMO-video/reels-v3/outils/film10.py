"""« La vidéo 10/10 » : film héros LIMO (~33 s, 9:16), écrit comme une keynote.
Fond nuit #05050f + halos violet / turquoise, typographie Montserrat 800, cartes iOS, téléphone en 3D. Aucune photo.

  0,0  22:47, l'écran verrouillé se remplit : 6 notifications de la vraie vie d'un conseiller
  2,4  « Ton métier, c'est vendre. Pas ça. »
  4,1  les notifications sont aspirées dans une sphère : « Et si tout ça… était déjà géré ? »
  6,4  flash, LIMO, « Le bras droit du conseiller immo. »               (entrée de la batterie)
  9,2  téléphone 3D : tu dictes ta visite, la fiche et la relance se préparent
 14,4  les 6 notifications reviennent, chacune avec sa réponse prête ; « Tout valider » → 6/6
 19,6  carte : ventes réelles (DVF), vendeurs probables, estimation 248 – 262 k€
 23,8  coucher de soleil, l'horloge passe de 22:47 à 18:30 : « Tu rentres à l'heure. »
 27,6  LIMO · essai gratuit 14 jours · sans engagement · dès 49 €/mois · app.leadengineai.fr

Données fictives. Usage : python3 outils/film10.py   (réécrit reels/hero-01-ton-metier-cest-vendre.html)
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from cine import COMMON, FACES  # noqa: E402
from premium2 import SHELL  # noqa: E402
from premium3 import CSS  # noqa: E402

NAME = "hero-01-ton-metier-cest-vendre"
DUR = 33.0

CSS_H = """
      .hn { position: absolute; left: 60px; width: 960px; height: 170px; box-sizing: border-box; border-radius: 44px; padding: 24px 30px; display: flex; gap: 24px; align-items: flex-start; background: rgba(44,44,60,.66); border: 1px solid rgba(255,255,255,.1); box-shadow: 0 24px 60px rgba(0,0,0,.4); font-family: Inter, sans-serif; color: #fff; }
      .hn .ic { flex: none; width: 76px; height: 76px; border-radius: 20px; display: flex; align-items: center; justify-content: center; }
      .hn .ic svg { width: 46px; height: 46px; }
      .hn .tx { flex: 1; min-width: 0; }
      .hn .hd { display: flex; justify-content: space-between; align-items: baseline; gap: 16px; }
      .hn .hd b { font-size: 31px; font-weight: 700; white-space: nowrap; }
      .hn .hd span { font-size: 24px; color: rgba(255,255,255,.5); white-space: nowrap; }
      .hn .ms { margin-top: 6px; font-size: 29px; line-height: 1.3; color: rgba(255,255,255,.86); display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; }
      .hr { position: absolute; left: 60px; width: 960px; height: 136px; }
      .hr .fc { position: absolute; inset: 0; box-sizing: border-box; border-radius: 38px; padding: 22px 28px; display: flex; gap: 22px; align-items: center; font-family: Inter, sans-serif; color: #fff; }
      .hr .fr { background: rgba(44,44,60,.7); border: 1px solid rgba(255,255,255,.1); }
      .hr .bk { background: linear-gradient(120deg, rgba(107,79,224,.32), rgba(30,28,64,.85) 60%); border: 1.5px solid rgba(185,166,255,.45); box-shadow: 0 20px 50px rgba(0,0,0,.35); }
      .hr .ic { flex: none; width: 70px; height: 70px; border-radius: 18px; display: flex; align-items: center; justify-content: center; }
      .hr .ic svg { width: 42px; height: 42px; }
      .hr .lh { flex: none; width: 70px; height: 70px; border-radius: 50%; background: #fff; display: flex; align-items: center; justify-content: center; }
      .hr .lh img { width: 50px; height: 50px; }
      .hr .tx { flex: 1; min-width: 0; }
      .hr .hd { display: flex; justify-content: space-between; align-items: center; gap: 14px; }
      .hr .hd b { font-size: 26px; font-weight: 700; color: rgba(255,255,255,.7); white-space: nowrap; }
      .hr .ms { margin-top: 6px; font-size: 30px; line-height: 1.25; font-weight: 600; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
      .hr .fr .ms { font-weight: 400; color: rgba(255,255,255,.82); }
      .hr .st { position: relative; flex: none; width: 150px; height: 40px; }
      .hr .st i { position: absolute; right: 0; top: 0; height: 40px; padding: 0 18px; border-radius: 20px; font-style: normal; font-family: Montserrat, sans-serif; font-weight: 800; font-size: 20px; letter-spacing: .06em; display: flex; align-items: center; white-space: nowrap; }
      .hr .st .p { background: rgba(143,107,255,.3); color: #d9ceff; }
      .hr .st .d { background: #2cc4b5; color: #052a27; }
      .hph { position: absolute; width: 580px; height: 1180px; box-sizing: border-box; padding: 16px; border-radius: 92px; background: linear-gradient(145deg, #4a4a5c 0%, #101018 30%, #1c1c28 70%, #3a3a4c 100%); box-shadow: 0 70px 140px rgba(0,0,0,.65), inset 0 0 0 2px rgba(255,255,255,.14); }
      .hsc { position: relative; width: 100%; height: 100%; border-radius: 76px; overflow: hidden; background: linear-gradient(180deg, #17163a 0%, #0b0b1e 100%); font-family: Inter, sans-serif; color: #fff; }
      .hisl { position: absolute; left: 50%; top: 32px; width: 150px; height: 44px; margin-left: -75px; border-radius: 22px; background: #000; }
      .hbub { position: absolute; left: 34px; right: 34px; top: 690px; padding: 24px 28px; border-radius: 30px; background: rgba(255,255,255,.08); border: 1px solid rgba(255,255,255,.12); font-size: 27px; line-height: 1.42; color: rgba(255,255,255,.92); min-height: 160px; box-sizing: border-box; }
      .hres { position: absolute; left: 34px; right: 34px; padding: 24px 26px; border-radius: 30px; background: #ffffff; color: #17163a; box-shadow: 0 24px 50px rgba(0,0,0,.4); box-sizing: border-box; }
      .hres .k { display: flex; align-items: center; gap: 12px; font-family: Montserrat, sans-serif; font-weight: 800; font-size: 21px; letter-spacing: .06em; color: #15877d; }
      .hres .k i { font-style: normal; width: 34px; height: 34px; border-radius: 50%; background: #2cc4b5; color: #fff; display: flex; align-items: center; justify-content: center; font-size: 20px; }
      .hres .t { margin-top: 10px; font-size: 32px; font-weight: 700; }
      .hres .s { margin-top: 6px; font-size: 23px; color: #5d6285; }
      .hchip { display: inline-block; margin: 10px 8px 0 0; padding: 8px 16px; border-radius: 16px; background: #efeafe; color: #4b32b8; font-size: 22px; font-weight: 600; }
      .hpin { position: absolute; padding: 10px 18px; border-radius: 16px; background: #ffffff; color: #17163a; font-family: Montserrat, sans-serif; font-weight: 800; font-size: 27px; white-space: nowrap; box-shadow: 0 10px 24px rgba(0,0,0,.4); }
      .hpin:after { content: ""; position: absolute; left: 50%; bottom: -10px; margin-left: -10px; border: 10px solid transparent; border-bottom: 0; border-top-color: #ffffff; }
      .hdg { display: inline-block; height: 1em; overflow: hidden; vertical-align: top; }
      .hdg span { display: block; }
      .hdg b { display: block; height: 1em; font-weight: inherit; }
"""

BODY = r"""
        tl.set([C.barT, C.barB], { opacity: 0 }, 0);
        tl.set([K.$(".n-bg", root), ...K.$$(".n-arc", root)], { opacity: 0 }, 0);
        const TOP = document.getElementById("root");
        const EO = "expo.out", BK = "back.out(1.6)";
        const hab = (css, html = "", p = TOP) => FX.ab(p, css, html);
        const hin = (e, t, o = {}) => { tl.set(e, { opacity: 0 }, 0); tl.fromTo(e, { opacity: 0, y: o.y ?? 40, scale: o.s ?? 1 }, { opacity: 1, y: 0, scale: 1, duration: o.d ?? 0.55, ease: o.e || EO, immediateRender: false }, t); };
        const hout = (e, t, d = 0.35) => tl.to(e, { opacity: 0, y: -30, duration: d, ease: "power2.in" }, t);
        const hshow = (e, t0, t1) => { tl.set(e, { opacity: 0 }, 0); tl.set(e, { opacity: 1 }, t0); if (t1 != null) tl.set(e, { opacity: 0 }, t1); };

        // ── fond : nuit profonde + deux halos qui respirent pendant tout le film
        hab({ inset: "0", background: "#05050f" });
        const halo1 = hab({ left: "-320px", top: "-160px", width: "1100px", height: "1100px", borderRadius: "50%", background: "radial-gradient(circle, rgba(107,79,224,.9) 0%, rgba(107,79,224,0) 66%)", filter: "blur(40px)" });
        const halo2 = hab({ left: "360px", top: "1040px", width: "1050px", height: "1050px", borderRadius: "50%", background: "radial-gradient(circle, rgba(44,196,181,.75) 0%, rgba(44,196,181,0) 66%)", filter: "blur(40px)" });
        tl.set([halo1, halo2], { opacity: 0.16 }, 0);
        tl.fromTo(halo1, { x: 0, y: 0, scale: 1 }, { x: 180, y: 120, scale: 1.15, duration: DUR, ease: "sine.inOut" }, 0);
        tl.fromTo(halo2, { x: 0, y: 0, scale: 1 }, { x: -160, y: -140, scale: 1.12, duration: DUR, ease: "sine.inOut" }, 0);
        tl.to([halo1, halo2], { opacity: 0.42, duration: 1.2, ease: "power2.out" }, 6.4);

        // icônes d'apps (style iOS)
        const ICO = {
          msg: ['linear-gradient(180deg,#6ef08a,#29c24a)', '<svg viewBox="0 0 24 24"><path d="M12 4.2c-5 0-9 3.1-9 7 0 2.2 1.3 4.2 3.4 5.5L5.7 20l4-2.1c.7.2 1.5.3 2.3.3 5 0 9-3.1 9-7s-4-7-9-7z" fill="#fff"/></svg>', "Messages"],
          mail: ['linear-gradient(180deg,#4fb2ff,#0a6cff)', '<svg viewBox="0 0 24 24"><rect x="3" y="6" width="18" height="12.5" rx="2.2" fill="#fff"/><path d="M3.8 7.2l8.2 6.1 8.2-6.1" stroke="#0a6cff" stroke-width="1.7" fill="none" stroke-linejoin="round"/></svg>', "Mail"],
          wa: ['linear-gradient(180deg,#5be37d,#1fb855)', '<svg viewBox="0 0 24 24"><path d="M12 3.5a8.5 8.5 0 0 0-7.3 12.8L3.5 20.5l4.3-1.1A8.5 8.5 0 1 0 12 3.5z" fill="none" stroke="#fff" stroke-width="1.9"/><path d="M9.2 8.2c.3-.4.7-.4.9 0l.8 1.7c.1.3 0 .6-.2.8l-.5.5c.6 1.2 1.6 2.2 2.8 2.8l.5-.5c.2-.2.5-.3.8-.2l1.7.8c.4.2.4.6 0 .9-.9.8-2.2 1-3.4.3a9 9 0 0 1-3.8-3.8c-.6-1.2-.5-2.5.4-3.3z" fill="#fff"/></svg>', "WhatsApp"],
        };
        // les 6 messages de la vraie vie… et ce que LIMO a préparé pour chacun
        const QN = [
          ["msg", "Mme Garnier", "La maison est toujours dispo ? On peut visiter demain 7 h 30 ?", "Réponse prête : visite samedi 10 h"],
          ["msg", "M. Leroy", "Vous deviez me rappeler… 🙃", "Rappel planifié : jeudi 18 h"],
          ["mail", "Me Faure · notaire", "Il manque le PV d’AG pour le compromis Martin.", "Mail au syndic prêt : PV d’AG"],
          ["msg", "M. Bernard", "Mon voisin a vendu 340 000 €, on met pareil ?", "3 ventes réelles prêtes à envoyer"],
          ["mail", "Cabinet comptable", "Vos frais km d’octobre avant ce soir svp 🙏", "1 240 km notés : export prêt"],
          ["wa", "Famille Petit", "Vous auriez d’autres biens avec un plus grand jardin ?", "3 biens compatibles trouvés"],
        ];
        const icon = (k) => `<div class="ic" style="background:${ICO[k][0]}">${ICO[k][1]}</div>`;

        // ══ 1 · 22:47, l'écran verrouillé déborde ══════════════════════════════
        const lock = hab({ inset: "0" });
        hshow(lock, 0, 5.2);
        const date = hab({ left: "0", right: "0", top: "250px", textAlign: "center", fontFamily: "Inter, sans-serif", fontWeight: "600", fontSize: "38px", color: "rgba(255,255,255,.72)" }, "mardi 6 octobre", lock);
        const clk = hab({ left: "0", right: "0", top: "296px", textAlign: "center", fontFamily: "Inter, sans-serif", fontWeight: "700", fontSize: "220px", lineHeight: "1", letterSpacing: "-0.03em", color: "#ffffff" }, "22:47", lock);
        tl.fromTo([date, clk], { opacity: 0, y: -20 }, { opacity: 1, y: 0, duration: 0.5, ease: "power2.out", stagger: 0.06 }, 0.0);
        const Y0 = 560, STEP = 182, ARR = [0.3, 0.8, 1.2, 1.5, 1.74, 1.94];
        const notes = QN.map((n, i) => {
          const c = hab({ left: "60px", top: Y0 + "px" }, `${icon(n[0])}<div class="tx"><div class="hd"><b>${n[1]}</b><span>${ICO[n[0]][2]} · maintenant</span></div><div class="ms">${n[2]}</div></div>`, lock);
          c.classList.add("hn");
          const t = ARR[i];
          tl.set(c, { opacity: 0 }, 0);
          tl.fromTo(c, { opacity: 0, yPercent: -30, scale: 0.9 }, { opacity: 1, yPercent: 0, scale: 1, duration: 0.42, ease: "back.out(1.4)", immediateRender: false }, t);
          K.sfx(t, "notif", 0.16 + i * 0.035, ((i % 3) - 1) * 0.25);
          K.sfx(t, "buzz", 0.06 + i * 0.015);
          return c;
        });
        // chaque nouvelle notification pousse les précédentes vers le bas
        notes.forEach((c, i) => {
          for (let j = i + 1; j < notes.length; j++) tl.to(c, { y: (j - i) * STEP, duration: 0.36, ease: "power3.out" }, ARR[j]);
        });
        // le téléphone vibre de plus en plus
        [1.5, 1.74, 1.94].forEach((t, k) => tl.fromTo(lock, { x: 0 }, { x: 5 + k * 2, duration: 0.04, ease: "none", yoyo: true, repeat: 5, immediateRender: false }, t));
        tl.set(lock, { x: 0 }, 2.3);
        // tout s'assombrit : la phrase
        tl.to([...notes, date, clk], { opacity: 0.16, filter: "blur(7px)", duration: 0.55, ease: "power2.out" }, 2.35);
        const ht1 = FX.rise(TOP, "Ton métier,|c’est [vendre.]", { top: "720px", fontSize: "106px", textShadow: "0 10px 40px rgba(0,0,0,.6)" }, 2.45, { accent: "#2cc4b5" });
        K.sfx(2.45, "thump", 0.22);
        const ht2 = FX.rise(TOP, "Pas ça.", { top: "1000px", fontSize: "150px", textShadow: "0 10px 40px rgba(0,0,0,.6)" }, 3.15, { color: "#b9a6ff", snd: false, st: 0.05 });
        K.sfx(3.15, "slam", 0.2);
        FX.fall([ht1, ht2], 4.0);

        // ══ 2 · tout est aspiré : « Et si tout ça… était déjà géré ? » ═══════════
        const OX = 540, OY = 960;
        tl.to([date, clk], { opacity: 0, duration: 0.3 }, 4.05);
        notes.forEach((c, i) => {
          const t = 4.15 + i * 0.06;
          tl.to(c, { opacity: 0.85, filter: "blur(0px)", duration: 0.15 }, 4.05);
          tl.to(c, { y: OY - (Y0 + 85), scale: 0.06, rotation: i % 2 ? 9 : -9, opacity: 0, duration: 0.62, ease: "power3.in" }, t);
        });
        K.sfx(4.15, "whoosh", 0.3, 0, { d: 0.7, f0: 2600, f1: 200, pk: 0.85 });
        const orbH = hab({ left: OX - 380 + "px", top: OY - 380 + "px", width: "760px", height: "760px", borderRadius: "50%", background: "radial-gradient(circle, rgba(143,107,255,.55) 0%, rgba(44,196,181,.18) 40%, rgba(0,0,0,0) 68%)", filter: "blur(10px)" });
        const orb = hab({ left: OX - 130 + "px", top: OY - 130 + "px", width: "260px", height: "260px", borderRadius: "50%", background: "radial-gradient(circle at 38% 32%, #ffffff 0%, #e4dcff 16%, #8f6bff 46%, #4a2fc4 70%, rgba(44,196,181,.55) 100%)", boxShadow: "0 0 80px 20px rgba(143,107,255,.55), 0 0 200px 60px rgba(44,196,181,.18)" });
        tl.set([orb, orbH], { opacity: 0 }, 0);
        tl.fromTo([orb, orbH], { opacity: 0, scale: 0 }, { opacity: 1, scale: 1, duration: 0.7, ease: "back.out(1.6)", immediateRender: false }, 4.62);
        K.sfx(4.7, "thump", 0.2);
        tl.to(orb, { scale: 1.1, duration: 0.32, ease: "sine.inOut", yoyo: true, repeat: 1 }, 5.35);
        tl.to(orbH, { scale: 1.25, duration: 0.65, ease: "sine.inOut" }, 5.35);
        const hq1 = FX.rise(TOP, "Et si tout ça…", { top: "1230px", fontSize: "78px" }, 4.85, { color: "#ffffff" });
        const hq2 = FX.rise(TOP, "…était [déjà] [géré] ?", { top: "1330px", fontSize: "78px" }, 5.45, { accent: "#2cc4b5", snd: false });
        K.sfx(4.9, "riser", 0.14, 0, { d: 1.5 });
        FX.fall([hq1, hq2], 6.05, 0.3);
        tl.to(orb, { scale: 9, opacity: 0, duration: 0.42, ease: "power3.in" }, 6.05);
        tl.to(orbH, { scale: 3, opacity: 0, duration: 0.42, ease: "power3.in" }, 6.05);
        C.flash(6.42, "#efeaff", 0.95);
        K.sfx(6.42, "boom", 0.32);

        // ══ 3 · LIMO ═════════════════════════════════════════════════════════
        const house = hab({ left: "330px", top: "430px", width: "420px", height: "372px" }, `<img src="assets/img/limo-house.png" alt="LIMO" style="width:100%;height:100%" />`);
        tl.set(house, { opacity: 0 }, 0);
        tl.fromTo(house, { opacity: 0, scale: 0.6, filter: "blur(14px)" }, { opacity: 1, scale: 1, filter: "blur(0px)", duration: 1.0, ease: EO, immediateRender: false }, 6.45);
        tl.to(house, { y: -14, duration: 0.95, ease: "sine.inOut", yoyo: true, repeat: 1 }, 7.0);
        const spk = K.sparkles(TOP, 540, 610, 16, 330, 260, 3);
        spk.forEach((s) => { s.el.style.zIndex = 5; tl.set(s.el, { opacity: 0 }, 0); });
        K.burst(spk, 6.55);
        const wm = FX.rise(TOP, "LIMO", { top: "860px", fontSize: "210px", letterSpacing: ".06em" }, 6.75, { st: 0.07, snd: false });
        K.sfx(6.75, "cta", 0.22);
        const tg = FX.rise(TOP, "Le bras droit du|[conseiller] [immo.]", { top: "1130px", fontSize: "66px" }, 7.35, { color: "#d9d4ff", accent: "#2cc4b5", snd: false });
        K.sfx(7.35, "whoosh", 0.12, 0, { d: 0.45, f0: 400, f1: 2200, pk: 0.4 });
        FX.fall([wm, tg], 8.95, 0.3);
        tl.to(house, { opacity: 0, scale: 0.85, y: -80, duration: 0.35, ease: "power2.in" }, 8.95);

        // ══ 4 · tu dictes, il retient tout (téléphone 3D) ════════════════════
        const BARS = Array.from({ length: 26 }, (_, i) => `<i style="position:absolute;left:${i * 17}px;top:0;width:9px;height:90px;border-radius:5px;background:linear-gradient(180deg,#b9a6ff,#2cc4b5)"></i>`).join("");
        const ph = hab({ left: "250px", top: "420px" }, `<div class="hsc">
<div style="position:absolute;left:54px;top:36px;font-size:25px;font-weight:700">17:05</div>
<div style="position:absolute;right:54px;top:40px;display:flex;gap:8px;align-items:center"><span style="display:flex;gap:3px;align-items:flex-end">${[8, 12, 16, 20].map((h) => `<i style="display:block;width:5px;height:${h}px;border-radius:2px;background:#fff"></i>`).join("")}</span><span style="display:block;width:40px;height:20px;border-radius:6px;border:2px solid rgba(255,255,255,.6);padding:2px;box-sizing:border-box"><i style="display:block;width:70%;height:100%;border-radius:3px;background:#fff"></i></span></div>
<div style="position:absolute;left:44px;top:120px;display:flex;align-items:center;gap:14px"><span style="width:52px;height:52px;border-radius:50%;background:#fff;display:flex;align-items:center;justify-content:center"><img src="assets/img/limo-house-ad.png" alt="" style="width:38px;height:38px" /></span><div><div style="font-size:36px;font-weight:800">Dictée</div><div style="font-size:21px;color:#a9abc9;margin-top:2px">Visite · 16 rue des Acacias, Allassac</div></div></div>
<div class="hmic" style="position:absolute;left:174px;top:270px;width:200px;height:200px">
<i class="hrg" style="position:absolute;inset:0;border-radius:50%;border:3px solid rgba(185,166,255,.7)"></i><i class="hrg" style="position:absolute;inset:0;border-radius:50%;border:3px solid rgba(44,196,181,.6)"></i>
<span style="position:absolute;inset:0;border-radius:50%;background:radial-gradient(circle at 38% 30%,#a58bff,#6b4fe0 60%,#4a2fc4);box-shadow:0 20px 60px rgba(107,79,224,.6);display:flex;align-items:center;justify-content:center"><svg viewBox="0 0 24 24" width="84" height="84"><rect x="8.5" y="3" width="7" height="12" rx="3.5" fill="#fff"/><path d="M5.5 11.5a6.5 6.5 0 0 0 13 0M12 18v3" stroke="#fff" stroke-width="1.8" fill="none" stroke-linecap="round"/></svg></span></div>
<div class="hwv" style="position:absolute;left:53px;top:520px;width:442px;height:90px">${BARS}</div>
<div class="hlb" style="position:absolute;left:0;right:0;top:628px;text-align:center;font-size:23px;color:#a9abc9;letter-spacing:.04em">LIMO t’écoute…</div>
<div class="hbub"><span class="hty"></span></div>
<div class="hres hr1" style="top:520px"><div class="k"><i>✓</i>FICHE MISE À JOUR</div><div class="t">Famille Durand</div><div><span class="hchip">Budget 260 k€</span><span class="hchip">Grand jardin</span><span class="hchip">Allassac · Brive</span></div></div>
<div class="hres hr2" style="top:790px"><div class="k"><i>✓</i>RELANCE PRÊTE</div><div class="t">Jeudi 18:00 · Durand</div><div class="s">Message préparé, tu n’as qu’à valider.</div></div>
<i class="hgl" style="position:absolute;top:-20%;bottom:-20%;left:-70%;width:40%;background:linear-gradient(100deg,rgba(255,255,255,0),rgba(255,255,255,.14),rgba(255,255,255,0));transform:rotate(10deg)"></i>
</div><i class="hisl"></i>`);
        ph.classList.add("hph");
        const phs = hab({ left: "300px", top: "1560px", width: "480px", height: "70px", borderRadius: "50%", background: "radial-gradient(ellipse, rgba(0,0,0,.7), rgba(0,0,0,0) 70%)", filter: "blur(8px)" });
        hshow(phs, 9.3, 14.1);
        tl.set(ph, { opacity: 0, transformPerspective: 2200, transformOrigin: "50% 50%" }, 0);
        tl.fromTo(ph, { opacity: 0, y: 760, rotationX: 26, rotationY: -26, rotationZ: 5 }, { opacity: 1, y: 0, rotationX: 7, rotationY: -13, rotationZ: 0, duration: 1.05, ease: EO, immediateRender: false }, 9.15);
        tl.to(ph, { rotationX: 2, rotationY: -4, y: -12, duration: 3.75, ease: "sine.inOut" }, 10.2);
        K.sfx(9.15, "whoosh", 0.26, 0, { d: 0.6, f0: 200, f1: 1800, pk: 0.6 });
        const hd1 = FX.rise(TOP, "Tu [dictes].", { top: "250px", fontSize: "92px" }, 9.4, { accent: "#b9a6ff", snd: false });
        FX.fall(hd1, 11.8);
        const hd2 = FX.rise(TOP, "Il retient [tout].", { top: "250px", fontSize: "92px" }, 11.95, { accent: "#2cc4b5", snd: false });
        FX.fall(hd2, 13.95);
        // micro : anneaux + ondes
        const mic = K.$(".hmic", ph), wv = K.$(".hwv", ph), lb = K.$(".hlb", ph), bub = K.$(".hbub", ph);
        tl.set([mic, wv, lb, bub], { opacity: 0 }, 0);
        tl.fromTo(mic, { opacity: 0, scale: 0.5 }, { opacity: 1, scale: 1, duration: 0.45, ease: BK, immediateRender: false }, 9.8);
        K.sfx(9.85, "bloop-up", 0.3);
        K.$$(".hrg", ph).forEach((r, k) => tl.fromTo(r, { scale: 1, opacity: 0.9 }, { scale: 1.7, opacity: 0, duration: 0.9, ease: "power1.out", repeat: 1, immediateRender: false }, 10.0 + k * 0.45));
        tl.fromTo([wv, lb], { opacity: 0 }, { opacity: 1, duration: 0.3, immediateRender: false }, 10.0);
        K.$$("i", wv).forEach((b, i) => {
          tl.set(b, { scaleY: 0.15, transformOrigin: "50% 50%" }, 0);
          const a = 0.25 + ((i * 37) % 10) / 13, d = 0.16 + ((i * 7) % 5) * 0.035;
          tl.fromTo(b, { scaleY: 0.15 }, { scaleY: a, duration: d, ease: "sine.inOut", yoyo: true, repeat: Math.floor(1.9 / d) | 1, immediateRender: false }, 10.0 + (i % 4) * 0.03);
        });
        K.sfx(10.0, "voice", 0.07, 0, { d: 1.9 });
        tl.fromTo(bub, { opacity: 0, y: 30 }, { opacity: 1, y: 0, duration: 0.35, ease: "power2.out", immediateRender: false }, 10.05);
        K.type(K.$(".hty", ph), "« Visite avec la famille Durand. Ils adorent le jardin, budget 260 k€. Les rappeler jeudi après 18 h. »", 10.1, 1.9, 0.035);
        // la dictée remonte, la fiche et la relance apparaissent
        tl.to([mic, wv, lb], { opacity: 0, y: -60, scale: 0.9, duration: 0.35, ease: "power2.in" }, 12.05);
        K.sfx(12.05, "bloop-down", 0.2);
        tl.to(bub, { y: -500, duration: 0.55, ease: "power3.inOut" }, 12.1);
        const r1 = K.$(".hr1", ph), r2 = K.$(".hr2", ph);
        tl.set([r1, r2], { opacity: 0 }, 0);
        tl.fromTo(r1, { opacity: 0, y: 80, scale: 0.94 }, { opacity: 1, y: 0, scale: 1, duration: 0.5, ease: BK, immediateRender: false }, 12.55);
        K.sfx(12.6, "success", 0.24);
        tl.fromTo(K.$$(".hchip", r1), { opacity: 0, scale: 0.6 }, { opacity: 1, scale: 1, duration: 0.3, ease: "back.out(2)", stagger: 0.12, immediateRender: false }, 12.85);
        tl.fromTo(r2, { opacity: 0, y: 80, scale: 0.94 }, { opacity: 1, y: 0, scale: 1, duration: 0.5, ease: BK, immediateRender: false }, 13.2);
        K.sfx(13.25, "success", 0.24, 0.2);
        tl.fromTo(K.$(".hgl", ph), { xPercent: 0 }, { xPercent: 420, duration: 1.2, ease: "power2.inOut" }, 13.3);
        tl.to(ph, { x: -260, y: 80, rotationY: 34, scale: 0.86, opacity: 0, duration: 0.45, ease: "power3.in" }, 14.0);
        K.sfx(14.0, "whoosh", 0.22, -0.3, { d: 0.45, f0: 1800, f1: 300, pk: 0.5 });

        // ══ 5 · il prépare tout, tu valides ══════════════════════════════════
        const hp1 = FX.rise(TOP, "Il prépare [tout].", { top: "250px", fontSize: "88px" }, 14.5, { accent: "#b9a6ff" });
        FX.fall(hp1, 17.4);
        const hp2 = FX.rise(TOP, "Tu valides.|[C’est] [fait.]", { top: "236px", fontSize: "92px" }, 17.55, { accent: "#2cc4b5", snd: false });
        const RY = 490, RS = 150;
        const rows = QN.map((n, i) => {
          const r = hab({ left: "60px", top: RY + i * RS + "px" }, `<div class="fc fr">${icon(n[0])}<div class="tx"><div class="hd"><b style="color:#fff">${n[1]}</b></div><div class="ms">${n[2]}</div></div></div><div class="fc bk"><span class="lh"><img src="assets/img/limo-house-ad.png" alt="" /></span><div class="tx"><div class="hd"><b>${n[1]}</b><span class="st"><i class="p">PRÊT</i><i class="d">✓ FAIT</i></span></div><div class="ms">${n[3]}</div></div></div>`);
          r.classList.add("hr");
          const fr = K.$(".fr", r), bk = K.$(".bk", r);
          tl.set(r, { opacity: 0, transformPerspective: 1400 }, 0);
          tl.set(bk, { opacity: 0 }, 0);
          tl.set(K.$(".st .d", r), { opacity: 0 }, 0);
          tl.fromTo(r, { opacity: 0, y: 50, scale: 0.96 }, { opacity: 1, y: 0, scale: 1, duration: 0.45, ease: EO, immediateRender: false }, 14.6 + i * 0.07);
          const tf = 15.35 + i * 0.3;
          tl.to(r, { rotationX: 90, duration: 0.15, ease: "power2.in" }, tf);
          tl.set(fr, { opacity: 0 }, tf + 0.15);
          tl.set(bk, { opacity: 1 }, tf + 0.15);
          tl.fromTo(r, { rotationX: -90 }, { rotationX: 0, duration: 0.3, ease: "back.out(1.7)", immediateRender: false }, tf + 0.15);
          K.sfx(tf + 0.1, "pop", 0.16, ((i % 3) - 1) * 0.3, { f: 520 + i * 70 });
          return r;
        });
        K.sfx(14.6, "whoosh", 0.18, 0, { d: 0.5, f0: 300, f1: 2400, pk: 0.5 });
        const btn = hab({ left: "240px", top: "1400px", width: "600px", height: "108px", borderRadius: "54px", background: "linear-gradient(100deg,#7b5cff,#5b3fd6)", boxShadow: "0 20px 50px rgba(107,79,224,.5)", fontFamily: "Montserrat, sans-serif", fontWeight: "800", fontSize: "40px", color: "#fff", overflow: "hidden" },
          `<span class="b1" style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center">Tout valider · 6</span><span class="b2" style="position:absolute;inset:0;display:flex;align-items:center;justify-content:center;background:#2cc4b5;color:#052a27">✓ 6 / 6 réglés</span>`);
        tl.set(K.$(".b2", btn), { opacity: 0 }, 0);
        hin(btn, 17.15, { y: 40, s: 0.85, e: BK, d: 0.45 });
        // le doigt touche « Tout valider »
        const tch = hab({ left: "500px", top: "1414px", width: "80px", height: "80px", borderRadius: "50%", background: "rgba(255,255,255,.55)", border: "3px solid rgba(255,255,255,.9)", zIndex: 6 });
        tl.set(tch, { opacity: 0 }, 0);
        tl.fromTo(tch, { opacity: 0, scale: 1.6 }, { opacity: 1, scale: 1, duration: 0.22, ease: "power2.out", immediateRender: false }, 17.75);
        tl.to(tch, { opacity: 0, scale: 1.8, duration: 0.35, ease: "power2.out" }, 18.0);
        tl.to(btn, { scale: 0.94, duration: 0.1, ease: "power2.out", yoyo: true, repeat: 1 }, 17.9);
        K.sfx(17.92, "tap", 0.4);
        tl.set(K.$(".b2", btn), { opacity: 1 }, 18.05);
        rows.forEach((r, i) => {
          const t = 18.1 + i * 0.09;
          tl.to(K.$(".st .p", r), { opacity: 0, duration: 0.12 }, t);
          tl.fromTo(K.$(".st .d", r), { opacity: 0, scale: 0.5 }, { opacity: 1, scale: 1, duration: 0.3, ease: "back.out(2.2)", immediateRender: false }, t);
          tl.fromTo(K.$(".bk", r), { borderColor: "rgba(185,166,255,.45)" }, { borderColor: "rgba(44,196,181,.95)", duration: 0.25, immediateRender: false }, t);
          K.sfx(t, "tick", 0.14, 0, { f: 1500 + i * 220 });
        });
        K.sfx(18.65, "fanfare", 0.2);
        const spk2 = K.sparkles(TOP, 540, 1454, 14, 380, 160, 5);
        spk2.forEach((s) => { s.el.style.zIndex = 7; tl.set(s.el, { opacity: 0 }, 0); });
        K.burst(spk2, 18.1, false);
        FX.fall(hp2, 19.35, 0.3);
        tl.to([...rows, btn], { opacity: 0, y: -40, duration: 0.35, ease: "power2.in", stagger: 0.03 }, 19.3);

        // ══ 6 · il repère les vendeurs, il estime au juste prix ══════════════
        const hm1 = FX.rise(TOP, "Il repère|les [vendeurs].", { top: "236px", fontSize: "92px" }, 19.75, { accent: "#2cc4b5" });
        FX.fall(hm1, 21.75);
        const hm2 = FX.rise(TOP, "Il estime|au [juste] [prix].", { top: "236px", fontSize: "92px" }, 21.9, { accent: "#b9a6ff", snd: false });
        FX.fall(hm2, 23.6, 0.3);
        const map = hab({ left: "60px", top: "480px", width: "960px", height: "740px", borderRadius: "48px", overflow: "hidden", background: "#11112a", border: "1.5px solid rgba(255,255,255,.12)", boxShadow: "0 40px 100px rgba(0,0,0,.55)" });
        const mapIn = hab({ inset: "0" }, `<svg viewBox="0 0 960 740" width="960" height="740" style="position:absolute;inset:0">
<rect width="960" height="740" fill="#11112a"/>
${[[40, 40, 250, 170], [320, 30, 270, 190], [630, 50, 290, 150], [30, 270, 210, 200], [290, 300, 230, 160], [580, 250, 340, 210], [60, 540, 300, 170], [420, 520, 220, 190], [700, 520, 230, 180]].map((b) => `<rect x="${b[0]}" y="${b[1]}" width="${b[2]}" height="${b[3]}" rx="22" fill="#1a1a3c"/>`).join("")}
<rect x="300" y="310" width="120" height="70" rx="14" fill="#15302c"/>
<path d="M-20 235 C200 215 420 260 980 225" stroke="#2b2b55" stroke-width="34" fill="none"/>
<path d="M270 -20 C290 200 255 420 300 760" stroke="#2b2b55" stroke-width="28" fill="none"/>
<path d="M560 -20 C545 260 600 480 560 760" stroke="#2b2b55" stroke-width="22" fill="none"/>
<path d="M-20 505 C240 480 520 530 980 490" stroke="#2b2b55" stroke-width="24" fill="none"/>
<path d="M-40 690 C200 640 420 720 1000 650" stroke="#173b52" stroke-width="46" fill="none"/>
<g class="hcmp" stroke="#b9a6ff" stroke-width="4" stroke-dasharray="10 10" fill="none" opacity=".9"><path d="M470 400 L180 170"/><path d="M470 400 L700 140"/><path d="M470 400 L420 560"/></g>
</svg>`, map);
        hin(map, 19.85, { y: 60, s: 0.95, d: 0.6 });
        tl.fromTo(mapIn, { scale: 1.08 }, { scale: 1.0, duration: 3.9, ease: "power1.out" }, 19.85);
        const PINS = [[180, 170, "248 k€"], [700, 140, "255 k€"], [420, 560, "262 k€"], [820, 400, "231 k€"], [110, 430, "239 k€"]];
        PINS.forEach((p, k) => {
          const e = hab({ left: p[0] - 60 + "px", top: p[1] - 64 + "px" }, p[2], mapIn);
          e.classList.add("hpin");
          tl.set(e, { opacity: 0 }, 0);
          tl.fromTo(e, { opacity: 0, y: 20, scale: 0.5 }, { opacity: 1, y: 0, scale: 1, duration: 0.35, ease: "back.out(2)", immediateRender: false }, 20.2 + k * 0.16);
          K.sfx(20.2 + k * 0.16, "pop", 0.12, (p[0] - 480) / 600, { f: 700 + k * 90 });
        });
        const DVF = hab({ left: "36px", top: "36px", padding: "10px 20px", borderRadius: "18px", background: "rgba(255,255,255,.1)", border: "1px solid rgba(255,255,255,.18)", fontFamily: "Inter, sans-serif", fontWeight: "600", fontSize: "23px", color: "#d9d4ff" }, "Ventes réelles · DVF", mapIn);
        hin(DVF, 20.15, { y: 10 });
        const SELL = [[330, 110], [770, 300], [130, 640]];
        SELL.forEach((p, k) => {
          const t = 20.95 + k * 0.22;
          const g = hab({ left: p[0] - 18 + "px", top: p[1] - 18 + "px", width: "36px", height: "36px" }, `<i style="position:absolute;inset:0;border-radius:50%;border:3px solid #2cc4b5"></i><i style="position:absolute;inset:0;border-radius:50%;border:3px solid #2cc4b5"></i><span style="position:absolute;inset:6px;border-radius:50%;background:#2cc4b5;box-shadow:0 0 18px #2cc4b5"></span>`, mapIn);
          tl.set(g, { opacity: 0 }, 0);
          tl.fromTo(g, { opacity: 0, scale: 0 }, { opacity: 1, scale: 1, duration: 0.35, ease: "back.out(2.4)", immediateRender: false }, t);
          K.$$("i", g).forEach((r, j) => tl.fromTo(r, { scale: 1, opacity: 0.9 }, { scale: 3.2, opacity: 0, duration: 1.1, ease: "power1.out", repeat: 1, immediateRender: false }, t + 0.1 + j * 0.55));
          K.sfx(t, "sonar", 0.1, (p[0] - 480) / 600, { f: 1318.5 });
        });
        const lbl = hab({ left: "360px", top: "142px", padding: "12px 20px", borderRadius: "18px", background: "rgba(10,40,38,.92)", border: "1.5px solid #2cc4b5", fontFamily: "Inter, sans-serif", fontSize: "23px", color: "#d6fffa", whiteSpace: "nowrap" }, "<b>Vendeur probable</b> · DPE réalisé hier", mapIn);
        hin(lbl, 21.15, { y: 14, s: 0.9, e: BK, d: 0.4 });
        // le bien à estimer + ses ventes comparables
        const cmp = K.$(".hcmp", mapIn);
        tl.set(cmp, { opacity: 0 }, 0);
        tl.to(cmp, { opacity: 0.9, duration: 0.3 }, 22.0);
        tl.fromTo(cmp, { strokeDashoffset: 120 }, { strokeDashoffset: 0, duration: 1.6, ease: "none", immediateRender: false }, 22.0);
        const tgt = hab({ left: "440px", top: "370px", width: "60px", height: "60px", borderRadius: "50%", background: "#8f6bff", border: "5px solid #fff", boxShadow: "0 0 0 10px rgba(143,107,255,.35), 0 10px 30px rgba(0,0,0,.5)" }, "", mapIn);
        tl.set(tgt, { opacity: 0 }, 0);
        tl.fromTo(tgt, { opacity: 0, scale: 0 }, { opacity: 1, scale: 1, duration: 0.4, ease: "back.out(2.4)", immediateRender: false }, 21.95);
        K.sfx(21.95, "bloop-up", 0.22);
        tl.to([lbl, ...K.$$(".hpin", mapIn).filter((e, k) => k > 2)], { opacity: 0.25, duration: 0.3 }, 22.3);
        const est = hab({ left: "60px", top: "1250px", width: "960px", height: "240px", boxSizing: "border-box", padding: "26px 40px", borderRadius: "40px", background: "#ffffff", color: "#17163a", fontFamily: "Inter, sans-serif", boxShadow: "0 30px 80px rgba(0,0,0,.5)" },
          `<div style="font-family:Montserrat,sans-serif;font-weight:800;font-size:22px;letter-spacing:.08em;color:#6b4fe0">ESTIMATION · 12 RUE DES TILLEULS, ALLASSAC</div><div style="margin-top:6px;font-family:Montserrat,sans-serif;font-weight:800;font-size:96px;line-height:1.05;letter-spacing:-.01em"><span class="e1">0</span> – <span class="e2">0</span> k€</div><div style="margin-top:4px;font-size:25px;color:#5d6285">Sur 3 ventes réelles voisines · cadastre · diagnostics</div>`);
        hin(est, 22.2, { y: 60, e: BK, d: 0.5 });
        K.count(K.$(".e1", est), 248, 22.35, 1.1, (v) => String(Math.round(v)), { ticks: 10 });
        K.count(K.$(".e2", est), 262, 22.35, 1.1, (v) => String(Math.round(v)), { ticks: 0 });
        K.sfx(23.5, "success", 0.22);
        tl.to([map, est], { opacity: 0, scale: 0.96, filter: "blur(10px)", duration: 0.45, ease: "power2.in" }, 23.55);

        // ══ 7 · 18:30, tu rentres à l'heure ═══════════════════════════════════
        const sun = hab({ inset: "0", background: "linear-gradient(180deg, #120d2e 0%, #36194d 34%, #8e3a4f 66%, #e07a47 88%, #f6b065 100%)" });
        const sunO = hab({ left: "140px", top: "1380px", width: "800px", height: "800px", borderRadius: "50%", background: "radial-gradient(circle, rgba(255,226,170,.95) 0%, rgba(255,170,100,.4) 35%, rgba(0,0,0,0) 68%)", filter: "blur(6px)" });
        tl.set([sun, sunO], { opacity: 0 }, 0);
        tl.to(sun, { opacity: 1, duration: 0.8, ease: "power1.inOut" }, 23.75);
        tl.fromTo(sunO, { opacity: 0, y: 160 }, { opacity: 1, y: 0, duration: 2.6, ease: "power2.out", immediateRender: false }, 23.85);
        K.sfx(23.8, "pad", 0.14, 0, { d: 3.4 });
        const dt2 = hab({ left: "0", right: "0", top: "420px", textAlign: "center", fontFamily: "Inter, sans-serif", fontWeight: "600", fontSize: "38px", color: "rgba(255,240,225,.8)" }, "mardi 6 octobre");
        const DG = [["2", "1"], ["2", "8"], null, ["4", "3"], ["7", "0"]];
        const ck = hab({ left: "0", right: "0", top: "468px", textAlign: "center", fontFamily: "Inter, sans-serif", fontWeight: "700", fontSize: "230px", lineHeight: "1", letterSpacing: "-0.03em", color: "#ffffff", textShadow: "0 10px 50px rgba(80,20,40,.5)" },
          DG.map((d) => (d ? `<span class="hdg"><span><b>${d[0]}</b><b>${d[1]}</b></span></span>` : `<span class="hdg"><span><b>:</b></span></span>`)).join(""));
        hin([dt2, ck], 24.05, { y: -20, d: 0.5 });
        K.$$(".hdg > span", ck).forEach((c, i) => {
          if (!DG[i]) return;
          const t = 24.55 + i * 0.1;
          tl.fromTo(c, { yPercent: 0 }, { yPercent: -50, duration: 0.65, ease: "power3.inOut", immediateRender: false }, t);
          K.sfx(t + 0.35, "tick", 0.14, 0, { f: 1800 - i * 120 });
        });
        K.sfx(25.2, "notif", 0.12);
        const hs1 = FX.rise(TOP, "Tu rentres|[à] [l’heure].", { top: "830px", fontSize: "112px", textShadow: "0 10px 40px rgba(60,10,30,.45)" }, 25.0, { accent: "#ffd9a0" });
        const hs2 = hab({ left: "60px", right: "60px", top: "1110px", textAlign: "center", fontFamily: "Inter, sans-serif", fontWeight: "500", fontSize: "46px", color: "#fff1e2" }, "Et ton téléphone, enfin, se tait.");
        hin(hs2, 25.65, { y: 20 });
        const dnd = hab({ left: "250px", top: "1240px", width: "580px", height: "104px", boxSizing: "border-box", padding: "0 26px", borderRadius: "52px", display: "flex", alignItems: "center", gap: "20px", background: "rgba(30,14,40,.45)", border: "1.5px solid rgba(255,255,255,.3)", fontFamily: "Inter, sans-serif", fontWeight: "600", fontSize: "34px", color: "#ffffff" },
          `<span style="flex:none;width:62px;height:62px;border-radius:50%;background:#6b4fe0;display:flex;align-items:center;justify-content:center"><svg viewBox="0 0 24 24" width="34" height="34"><path d="M20 14.5A8.5 8.5 0 0 1 9.5 4a8.5 8.5 0 1 0 10.5 10.5z" fill="#fff"/></svg></span><span style="flex:1">Ne pas déranger</span><span class="sw" style="position:relative;flex:none;width:96px;height:56px;border-radius:28px;background:rgba(255,255,255,.25)"><i style="position:absolute;left:4px;top:4px;width:48px;height:48px;border-radius:50%;background:#fff;display:block"></i></span>`);
        hin(dnd, 26.1, { y: 30, e: BK, d: 0.45 });
        const sw = K.$(".sw", dnd);
        tl.to(sw, { backgroundColor: "#2cc4b5", duration: 0.25 }, 26.6);
        tl.to(K.$("i", sw), { x: 40, duration: 0.25, ease: "power2.out" }, 26.6);
        K.sfx(26.6, "pop", 0.18, 0, { f: 760 });
        FX.fall(hs1, 27.35, 0.3);
        tl.to([dt2, ck, hs2, dnd], { opacity: 0, y: -30, duration: 0.35, ease: "power2.in" }, 27.35);
        tl.to([sun, sunO], { opacity: 0, duration: 0.8, ease: "power1.inOut" }, 27.4);

        // ══ 8 · appel à l'action ═════════════════════════════════════════════
        const TE = 27.6;
        const house2 = hab({ left: "405px", top: "300px", width: "270px", height: "240px" }, `<img src="assets/img/limo-house.png" alt="LIMO" style="width:100%;height:100%" />`);
        tl.set(house2, { opacity: 0 }, 0);
        tl.fromTo(house2, { opacity: 0, scale: 0.6, y: 30 }, { opacity: 1, scale: 1, y: 0, duration: 0.7, ease: BK, immediateRender: false }, TE);
        tl.to(house2, { y: -10, duration: 1.2, ease: "sine.inOut", yoyo: true, repeat: 3 }, TE + 0.8);
        K.sfx(TE, "cta", 0.22);
        const wm2 = FX.rise(TOP, "LIMO", { top: "545px", fontSize: "150px", letterSpacing: ".06em" }, TE + 0.15, { st: 0.06, snd: false });
        const tg2 = FX.rise(TOP, "Le bras droit du|[conseiller] [immo.]", { top: "735px", fontSize: "56px" }, TE + 0.45, { color: "#d9d4ff", accent: "#2cc4b5", snd: false });
        const pill = hab({ left: "0", right: "0", top: "925px", textAlign: "center" }, `<span class="pl" style="position:relative;display:inline-block;overflow:hidden;padding:30px 66px;border-radius:999px;background:#ffffff;color:#17163a;font-family:Montserrat,sans-serif;font-weight:800;font-size:54px;box-shadow:0 24px 70px rgba(143,107,255,.45)">Essai gratuit 14 jours<i class="sh" style="position:absolute;top:-40%;bottom:-40%;left:-40%;width:30%;background:linear-gradient(100deg,rgba(255,255,255,0),rgba(185,166,255,.6),rgba(255,255,255,0));transform:rotate(12deg)"></i></span>`);
        hin(pill, TE + 0.85, { y: 40, s: 0.9, e: BK, d: 0.5 });
        K.sfx(TE + 0.85, "pop", 0.2, 0, { f: 620 });
        tl.fromTo(K.$(".sh", pill), { xPercent: 0 }, { xPercent: 700, duration: 1.1, ease: "power2.inOut", immediateRender: false }, TE + 1.6);
        tl.fromTo(K.$(".sh", pill), { xPercent: 0 }, { xPercent: 700, duration: 1.1, ease: "power2.inOut", immediateRender: false }, TE + 3.4);
        const sub = hab({ left: "60px", right: "60px", top: "1095px", textAlign: "center", fontFamily: "Inter, sans-serif", fontWeight: "500", fontSize: "40px", color: "#c9c9e8" }, "Sans engagement · dès 49 €/mois");
        hin(sub, TE + 1.15, { y: 20 });
        const url = hab({ left: "0", right: "0", top: "1170px", textAlign: "center" }, `<span style="position:relative;display:inline-block;font-family:Montserrat,sans-serif;font-weight:800;font-size:50px;color:#ffffff">app.leadengineai.fr<i class="ul" style="position:absolute;left:0;right:0;bottom:-10px;height:6px;border-radius:3px;background:linear-gradient(90deg,#8f6bff,#2cc4b5);display:block"></i></span>`);
        hin(url, TE + 1.4, { y: 20 });
        tl.set(K.$(".ul", url), { scaleX: 0, transformOrigin: "0 50%" }, 0);
        tl.to(K.$(".ul", url), { scaleX: 1, duration: 0.6, ease: EO }, TE + 1.7);
        const M = N.mascot({ left: "450px", top: "1270px", width: "180px" });
        TOP.appendChild(M.el);
        M.enter(TE + 1.9);
        M.wave(TE + 2.6);
        M.blink(TE + 3.6);
        M.float(TE + 3.8, 1.5, 8);
        window.__TE = TE;
"""

if __name__ == "__main__":
    body = "        const DUR = " + str(DUR) + ";\n" + BODY
    html = SHELL.format(title=NAME, faces=FACES, css=(CSS + CSS_H).strip("\n"), body=(COMMON + body).strip("\n"), dur=DUR, name=NAME)
    (HERE.parent / "reels" / f"{NAME}.html").write_text(html, encoding="utf-8")
    print("reels/" + NAME + ".html")
