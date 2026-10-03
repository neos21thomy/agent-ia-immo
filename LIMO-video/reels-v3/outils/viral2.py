"""Film viral V2 « LIMO t'appelle » : format mème de mascotte de marque (énergie hibou Duolingo).
La mascotte appelle son conseiller à 23 h 47 parce qu'il n'a pas rappelé sa vendeuse, il refuse l'appel,
elle le harcèle de notifications passives-agressives, surgit plein écran, il obéit, le mandat est signé,
elle danse, puis elle « appelle » le spectateur : décrocher = essayer LIMO. Coupes calées sur le tempo (122 BPM).
Sans voix : sous-titres façon TikTok, babillage de robot et bruitages de mème. Données affichées = fictives.

Usage : python3 outils/viral2.py   (depuis reels-v3/ ; réécrit reels/viral-02-limo-tappelle.html)
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from cine import COMMON, FACES  # noqa: E402
from lifestyle import V  # noqa: E402
from premium2 import SHELL  # noqa: E402
from premium3 import CSS  # noqa: E402
from premium4 import SH4  # noqa: E402

NAME = "viral-02-limo-tappelle"
DUR = 29.3
PRE = V("v1", "agent-voiture-grade", 12.6, 0.95, 1) + V("v2", "villa-recul-lent-grade", 17.0, 4.1, 2)
EXTRA_CSS = """
      .cap { display: inline-block; padding: 14px 26px 16px; border-radius: 18px; background: #fff; color: #111; font-family: Montserrat, sans-serif; font-weight: 800; font-size: 46px; line-height: 1.18; box-shadow: 0 10px 30px rgba(0,0,0,.25); }
      .meme { font-family: Montserrat, sans-serif; font-weight: 800; color: #fff; -webkit-text-stroke: 4px #000; paint-order: stroke fill; text-shadow: 0 8px 0 rgba(0,0,0,.35); line-height: 1; letter-spacing: -0.01em; }
      .ios { font-family: Inter, sans-serif; color: #fff; }
      .nt { display: flex; gap: 20px; align-items: center; padding: 22px 26px; border-radius: 34px; background: rgba(40,40,58,.62); backdrop-filter: blur(30px) saturate(1.6); -webkit-backdrop-filter: blur(30px) saturate(1.6); box-shadow: 0 16px 40px rgba(0,0,0,.3); }
      .nt img { width: 74px; height: 74px; border-radius: 18px; background: #fff; padding: 8px; flex: none; }
      .nt b { display: block; font-size: 27px; letter-spacing: .02em; opacity: .75; font-weight: 600; }
      .nt span { display: block; font-size: 33px; line-height: 1.25; font-weight: 600; }
      .btn { position: absolute; width: 170px; height: 170px; border-radius: 50%; display: flex; align-items: center; justify-content: center; }
      .btn svg { width: 80px; height: 80px; }
      .lbl { position: absolute; width: 260px; text-align: center; font-family: Inter, sans-serif; font-size: 30px; color: #fff; }
"""
BODY = SH4 + r"""
        const TOP = document.getElementById("root");
        tl.set([C.barT, C.barB], { opacity: 0 }, 0);
        const WALL = `<img src="assets/img/bien-mas-lavande.jpg" alt="" style="position:absolute;left:-120px;top:-120px;width:1320px;height:2160px;object-fit:cover;filter:blur(38px) brightness(.42) saturate(1.3)" /><div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(10,8,30,.35),rgba(10,8,30,.7))"></div>`;
        const PH_DOWN = `<svg viewBox="0 0 24 24" fill="#fff"><path d="M12 9c-1.6 0-3.15.25-4.6.72v3.1c0 .39-.23.74-.56.9-.98.49-1.87 1.12-2.66 1.85-.18.18-.43.28-.7.28-.28 0-.53-.11-.71-.29L.29 13.08a.996.996 0 0 1 0-1.41C3.34 8.78 7.46 7 12 7s8.66 1.78 11.71 4.67c.18.18.29.43.29.71 0 .28-.11.53-.29.71l-2.48 2.48c-.18.18-.43.29-.71.29-.27 0-.52-.11-.7-.28-.79-.74-1.69-1.36-2.67-1.85a.996.996 0 0 1-.56-.9v-3.1C15.15 9.25 13.6 9 12 9z"/></svg>`;
        const PH_UP = `<svg viewBox="0 0 24 24" fill="#fff"><path d="M20.01 15.38c-1.23 0-2.42-.2-3.53-.56a.977.977 0 0 0-1.01.24l-1.57 1.97c-2.83-1.35-5.48-3.9-6.89-6.83l1.95-1.66c.27-.28.35-.67.24-1.02-.37-1.11-.56-2.3-.56-3.53 0-.54-.45-.99-.99-.99H4.19C3.65 3 3 3.24 3 3.99 3 13.28 10.73 21 20.01 21c.71 0 .99-.63.99-1.18v-3.45c0-.54-.45-.99-.99-.99z"/></svg>`;
        const scr = (t0, t1, html = "", css = {}) => FX.layer(t0, t1, Object.assign({ background: "#07081a" }, css), html);
        const cap = (t0, t1, html, top = 210) => {
          const el = FX.ab(TOP, { left: "60px", right: "60px", top: top + "px", textAlign: "center", zIndex: 36 }, `<span class="cap">${html}</span>`);
          tl.set(el, { opacity: 0 }, 0);
          tl.fromTo(el, { opacity: 0, scale: 0.85 }, { opacity: 1, scale: 1, duration: 0.18, ease: "back.out(2.5)", immediateRender: false }, t0);
          tl.set(el, { opacity: 0 }, t1);
          return el;
        };
        const slamWord = (t, t1, txt, top, fs, color = "#fff") => {
          const el = FX.ab(TOP, { left: "30px", right: "30px", top: top + "px", textAlign: "center", zIndex: 36, fontSize: fs + "px" }, `<div class="meme" style="color:${color}">${txt}</div>`);
          tl.set(el, { opacity: 0 }, 0);
          tl.fromTo(el, { opacity: 0, scale: 2.2 }, { opacity: 1, scale: 1, duration: 0.14, ease: "power4.in", immediateRender: false }, t);
          tl.set(el, { opacity: 0 }, t1);
          K.sfx(t + 0.12, "slam", 0.42);
          return el;
        };
        const shakeEl = (el, t, amp = 18, n = 7) => { tl.fromTo(el, { x: 0 }, { x: amp, duration: 0.035, ease: "none", yoyo: true, repeat: n, immediateRender: false }, t); tl.set(el, { x: 0 }, t + 0.035 * (n + 1)); };
        const babble = (t, n = 5) => K.sfx(t, "chirp", 0.2, 0, { n });
        const hardCut = (t) => { C.flash(t, "#ffffff", 0.5); K.sfx(t, "whoosh", 0.18, 0, { d: 0.25, f0: 300, f1: 3200, pk: 0.4 }); };
        // écran d'appel entrant (plein écran, façon iPhone)
        const callScreen = (t0, t1, sub) => {
          const l = scr(t0, t1, WALL);
          FX.ab(l, { left: "0", right: "0", top: "360px", textAlign: "center" }, `<div class="ios" style="font-size:34px;opacity:.75">${sub}</div><div class="ios" style="font-size:96px;font-weight:600;margin-top:6px;letter-spacing:-.01em">LIMO</div>`);
          [0, 1, 2].forEach((i) => {
            const r = FX.ab(l, { left: "330px", top: "620px", width: "420px", height: "420px", borderRadius: "50%", border: "4px solid rgba(63,230,247,.55)" });
            tl.fromTo(r, { scale: 0.75, opacity: 0.9 }, { scale: 1.45, opacity: 0, duration: 1.4, ease: "power1.out", repeat: Math.floor((t1 - t0) / 1.4), immediateRender: false }, t0 + i * 0.46);
          });
          const no = FX.ab(l, { left: "150px", top: "1330px" }, `<div class="btn" style="background:#ff3b30">${PH_DOWN}</div><div class="lbl" style="left:-45px;top:190px">Refuser</div>`);
          const ok = FX.ab(l, { left: "760px", top: "1330px" }, `<div class="btn" style="background:#34c759">${PH_UP}</div><div class="lbl" style="left:-45px;top:190px">Accepter</div>`);
          K.sfx(t0 + 0.05, "ring", 0.3, 0, { d: Math.min(2.4, t1 - t0 - 0.3) });
          return { l, no: K.$(".btn", no), ok: K.$(".btn", ok), okW: ok, noW: no };
        };

        // ── S1 · 0–3,0 : LIMO t'appelle à 23:47 → tu refuses
        const c1 = callScreen(0, 3.0, "appel audio · 23:47");
        cap(0.05, 2.95, "quand t’as pas rappelé ta vendeuse<br>depuis 3 jours 💀", 170);
        K.sfx(0.05, "buzz", 0.25, 0, { d: 0.5 }); K.sfx(1.05, "buzz", 0.25, 0, { d: 0.5 });
        shakeEl(c1.l, 0.05, 8, 11); shakeEl(c1.l, 1.05, 8, 11);
        K.tapAt(c1.l, 235, 1415, 1.85);
        tl.to(c1.no, { scale: 0.85, duration: 0.08, yoyo: true, repeat: 1 }, 1.85);
        K.sfx(2.0, "scratch", 0.5);
        tl.to(c1.l, { filter: "grayscale(1) brightness(.6)", duration: 0.15 }, 2.0);
        slamWord(2.1, 2.95, "IL A REFUSÉ.", 1140, 92, "#ff5a4f");

        // ── S2 · 3,0–7,6 : l'écran verrouillé se remplit de notifications
        const s2 = scr(3.0, 7.6, WALL);
        FX.ab(s2, { left: "0", right: "0", top: "250px", textAlign: "center" }, `<div class="ios" style="font-size:38px;font-weight:600;opacity:.85">jeudi 8 octobre</div><div class="ios" style="font-size:210px;font-weight:700;line-height:1;margin-top:4px;letter-spacing:-.02em">23:48</div>`);
        const NT = [
          ["Mme Martin attend ton appel. 🙂", 3.25],
          ["Tu as refusé mon appel. 🙂", 3.75],
          ["Ce n’est pas grave. 🙂", 4.25],
          ["Je ne suis pas fâché. 🙂", 4.7],
          ["Le message est prêt. Tu cliques. C’est tout. 😐", 5.15],
          ["Ton concurrent, lui, l’a rappelée. 💀", 5.75],
        ];
        const stack = [];
        NT.forEach(([txt, t], i) => {
          const n = FX.ab(s2, { left: "60px", width: "960px", top: "560px", boxSizing: "border-box" }, `<div class="nt ios"><img src="assets/img/limo-house-ad.png" alt="" /><div style="flex:1;min-width:0"><b>LIMO · maintenant</b><span>${txt}</span></div></div>`);
          tl.set(n, { opacity: 0 }, 0);
          tl.fromTo(n, { opacity: 0, y: -90, scale: 0.92 }, { opacity: 1, y: 0, scale: 1, duration: 0.3, ease: "back.out(1.6)", immediateRender: false }, t);
          stack.forEach((p, k) => tl.to(p, { y: (stack.length - k) * 160, duration: 0.3, ease: "power3.out" }, t));
          stack.push(n);
          K.sfx(t, "notif", i === 5 ? 0.1 : 0.24);
        });
        tl.set(K.$(".nt", stack[5]), { background: "rgba(200,30,40,.78)" }, 5.75);
        K.sfx(5.8, "boom", 0.55);
        shakeEl(s2, 5.8, 22, 9);
        C.flash(5.8, "#ff3b30", 0.35);

        // ── S3 · 7,6–10,0 : la mascotte surgit plein écran
        const s3 = scr(7.6, 10.0);
        FX.aurora(s3, 7.5, 10.1, { colors: ["#ff3b6b", "#6b4fe0", "#ff8a3d"], a: 0.55 });
        hardCut(7.6);
        slamWord(7.8, 8.28, "RAPPELLE.", 260, 190);
        slamWord(8.3, 8.78, "LA.", 260, 230);
        slamWord(8.8, 9.95, "MAINTENANT.", 270, 124, "#ffe14d");
        [7.8, 8.3, 8.8].forEach((t) => { shakeEl(s3, t + 0.12, 26, 7); babble(t + 0.02, 3); });

        // ── S4 · 10,0–12,6 : il obéit, Mme Martin décroche
        const s4 = scr(10.0, 12.6, WALL);
        hardCut(10.0);
        cap(10.05, 12.55, "ok ok j’appelle 😭", 170);
        FX.ab(s4, { left: "0", right: "0", top: "330px", textAlign: "center" }, `<div style="margin:0 auto;width:200px;height:200px;border-radius:50%;background:linear-gradient(160deg,#c8b8ff,#7a62e6);display:flex;align-items:center;justify-content:center" class="ios"><b style="font-size:80px;font-weight:600">MM</b></div><div class="ios" style="font-size:80px;font-weight:600;margin-top:26px">Mme Martin</div><div class="ios tm" style="font-size:40px;opacity:.8;margin-top:8px;color:#34c759">00:00</div>`);
        K.count(K.$(".tm", s4), 9, 10.2, 2.3, (v) => "00:0" + Math.round(v), {});
        const tr = FX.glass(s4, { left: "80px", width: "920px", top: "800px", padding: "26px 30px" }, `<span style="display:block;font-size:24px;letter-spacing:.06em;color:rgba(255,255,255,.75)">LIMO · TRANSCRIPTION DE L’APPEL</span><span style="display:block;margin-top:10px;font-size:36px;line-height:1.35">« Merci de m’avoir rappelée ! Passez demain, <b style="color:#2cc4b5">on signe le mandat</b>. »</span>`);
        tl.set(tr, { opacity: 0 }, 0);
        tl.fromTo(tr, { opacity: 0, y: 50 }, { opacity: 1, y: 0, duration: 0.45, ease: "expo.out", immediateRender: false }, 10.9);
        FX.sheen(tr, 11.2);
        K.sfx(10.95, "success", 0.3);

        // ── S5 · 12,6–17,0 : depuis, il gère tout (coupes sur le tempo)
        cap(12.65, 16.95, "depuis, il gère <span style=\"color:#6b4fe0\">TOUT</span>", 170);
        const v1 = document.getElementById("v1");
        const kA = FX.layer(12.6, 13.55); shade(kA);
        tl.fromTo(v1, { scale: 1.12 }, { scale: 1.02, duration: 0.95, ease: "none" }, 12.6);
        card(kA, "pen", "Annonce rédigée", "Maison en pierre · prête à publier", { top: "420px" }, 12.7, { check: true });
        const kB = scr(13.55, 14.45); FX.aurora(kB, 13.5, 14.5, { colors: ["#ff8f8f", "#6b4fe0", "#3a2a9a"] }); hardCut(13.55);
        card(kB, "cake", "Anniversaire · M. Durand", "Message envoyé à 9:00 🎂", { top: "560px" }, 13.6, { check: true, bg: "rgba(255,143,143,.5)" });
        const kC = scr(14.45, 15.35); FX.aurora(kC, 14.4, 15.4, { colors: ["#2cc4b5", "#1d6f8a", "#3a2a9a"] }); hardCut(14.45);
        const kmv = FX.ab(kC, { left: "0", right: "0", top: "470px", textAlign: "center" }, `<div class="meme" style="font-size:170px"><span class="kv">0</span></div><div class="cap" style="margin-top:22px;font-size:40px">km calculés · frais prêts ✅</div>`);
        K.count(K.$(".kv", kmv), 1248, 14.5, 0.7, (v) => { const n = Math.round(v); return n >= 1000 ? Math.floor(n / 1000) + " " + String(n % 1000).padStart(3, "0") : String(n); }, { ticks: 8 });
        const kD = scr(15.35, 16.2); FX.aurora(kD, 15.3, 16.3, { colors: ["#6b4fe0", "#2cc4b5", "#3a2a9a"] }); hardCut(15.35);
        const mv = FX.ab(kD, { left: "0", right: "0", top: "470px", textAlign: "center" }, `<div class="meme" style="font-size:170px"><span class="kv">0</span></div><div class="cap" style="margin-top:22px;font-size:40px">mails triés · 3 réponses prêtes 📩</div>`);
        K.count(K.$(".kv", mv), 47, 15.4, 0.6, (v) => String(Math.round(v)), { ticks: 8 });
        const kE = scr(16.2, 17.0, WALL); hardCut(16.2);
        FX.ab(kE, { left: "0", right: "0", top: "400px", textAlign: "center" }, `<div class="ios" style="font-size:190px;font-weight:700;line-height:1">23:04</div><div class="cap" style="margin-top:30px;font-size:40px">12 relances programmées 🌙</div>`);
        K.sfx(16.25, "tick", 0.25, 0, { f: 1800 });

        // ── S6 · 17,0–21,0 : mandat signé, la mascotte danse
        const v2 = document.getElementById("v2");
        const kF = FX.layer(17.0, 21.0); shade(kF);
        C.flash(17.0, "#ffffff", 0.8);
        tl.fromTo(v2, { scale: 1.15 }, { scale: 1.0, duration: 4.0, ease: "power1.out" }, 17.0);
        cap(17.05, 20.95, "jour 12.", 170);
        const st = FX.ab(kF, { left: "0", right: "0", top: "380px", textAlign: "center" }, `<span style="display:inline-block;padding:18px 36px;border:9px solid #2cc4b5;border-radius:22px;background:rgba(5,6,15,.5);color:#2cc4b5;font-family:Montserrat,sans-serif;font-weight:800;font-size:84px;line-height:1.02;transform:rotate(-6deg)">MANDAT EXCLUSIF<br>SIGNÉ ✍️</span>`);
        tl.set(st, { opacity: 0 }, 0);
        tl.fromTo(st, { opacity: 0, scale: 2.6 }, { opacity: 1, scale: 1, duration: 0.22, ease: "power4.in", immediateRender: false }, 17.25);
        K.sfx(17.45, "stamp", 0.5); K.sfx(17.47, "boom", 0.35);
        shakeEl(kF, 17.47, 16, 7);
        [[17.5, 540, 1150, 1], [19.45, 540, 700, 2]].forEach(([t, x, y, k]) => { const sp = K.sparkles(TOP, x, y, 30, 470, 380, 11 + k); K.burst(sp, t); });

        // ── S7 · 21,0–24,1 : et toi ? LIMO t'appelle → décrocher
        const c7 = callScreen(21.0, 24.1, "appel audio · maintenant");
        hardCut(21.0);
        cap(21.05, 24.05, "et toi… tu décroches quand ? 👀", 170);
        tl.set(c7.no, { opacity: 0.35 }, 21.0);
        [21.5, 22.0, 22.5, 23.0].forEach((t) => tl.fromTo(c7.ok, { scale: 1 }, { scale: 1.14, duration: 0.2, ease: "power2.out", yoyo: true, repeat: 1, immediateRender: false }, t));
        K.tapAt(c7.l, 845, 1415, 23.5);
        K.sfx(23.6, "success", 0.35);
        C.flash(23.75, "#34c759", 0.55);

        // ── la mascotte (au-dessus de tous les calques)
        const M = N.mascot({ left: "390px", top: "760px", width: "300px" }, { expr: "angry" });
        TOP.appendChild(M.el); M.el.style.zIndex = "30";
        const go = (t, x, y, s, dd = 0.01) => M.move(t, { x, y, scale: s }, dd);
        go(0, 0, -100, 1.15);
        tl.set(M.el, { opacity: 1 }, 0);
        M.shake(0.1, 0.5); M.shake(1.1, 0.5); babble(0.6, 4); babble(1.4, 3);
        M.expr("sad", 2.02); M.expr("angry", 2.55); M.shake(2.55, 0.35);
        tl.set(M.el, { opacity: 0 }, 3.0);
        // S2 : elle surgit du bas de l'écran
        go(5.95, 0, 860, 1.4); tl.set(M.el, { opacity: 1 }, 6.0);
        M.move(6.05, { y: 770 }, 0.35); M.expr("angry", 6.05, false); babble(6.2, 4); M.shake(6.6, 0.6);
        M.move(7.1, { y: 730 }, 0.2);
        // S3 : plein écran
        go(7.6, 0, 110, 2.05); M.shake(7.92, 0.3); M.shake(8.42, 0.3); M.shake(8.92, 0.4);
        M.expr("happy", 9.35); babble(9.35, 2);
        const pl = N.say("S’il te plaît. 🙂", { left: "290px", top: "1500px", width: "500px", fontSize: "50px" }, 9.35, { tail: "up" });
        TOP.appendChild(pl); pl.style.zIndex = "34"; tl.set(pl, { opacity: 0 }, 9.98);
        // S4 : dans un coin, ravie
        go(10.0, 300, 520, 0.8); M.expr("happy", 10.0, false); M.hop(10.5, 60); M.expr("heart", 11.0); M.hop(11.3, 80);
        // S5 : montage
        go(12.6, -300, 470, 0.78); M.expr("think", 12.6, false);
        go(13.55, 0, 300, 1.2); M.expr("heart", 13.55, false); M.hop(13.9, 70);
        go(14.45, 0, 300, 1.2); M.expr("euro", 14.45, false);
        go(15.35, 0, 300, 1.2); M.expr("wink", 15.35, false);
        go(16.2, 0, 300, 1.2); M.expr("sleep", 16.2, false);
        // S6 : la danse (un pas par temps)
        go(17.0, 0, 330, 1.15); M.expr("heart", 17.45, false);
        for (let i = 0; i < 7; i++) { const t = 17.7 + i * 0.49; M.tilt(t, i % 2 ? -16 : 16, 0.2); if (i % 2 === 0) M.hop(t, 70); }
        M.tilt(21.0, 0, 0.1);
        M.expr("wink", 19.4, false); babble(19.4, 6);
        const tol = N.say("Je t’avais dit<br>de la rappeler. 🙂", { left: "190px", top: "820px", width: "700px", fontSize: "48px" }, 19.4, { tail: "down" });
        TOP.appendChild(tol); tol.style.zIndex = "34"; tl.set(tol, { opacity: 0 }, 20.98);
        // S7 : elle t'appelle, toi
        go(21.0, 0, -100, 1.15); M.expr("happy", 21.0, false); M.wave(21.3); babble(21.4, 4);
        M.expr("wink", 22.6); M.hop(23.5, 90);
        M.move(23.85, { opacity: 0, scale: 1.6 }, 0.2);
        outro(24.1);
"""

if __name__ == "__main__":
    html = SHELL.format(title="LIMO t'appelle", faces=FACES, css=(CSS + EXTRA_CSS).strip("\n"), body=(COMMON + BODY).strip("\n"), dur=DUR, name=NAME)
    html = html.replace('      <section id="s-main"', PRE + '      <section id="s-main"', 1)
    out = pathlib.Path(__file__).resolve().parent.parent / "reels" / f"{NAME}.html"
    out.write_text(html, encoding="utf-8")
    print("reels/" + NAME + ".html")
