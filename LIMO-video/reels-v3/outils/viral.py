"""Film viral « POV : ton assistant immo ne te lâche plus » : format mascotte de marque attachante et insistante
(dans l'esprit des mascottes virales type hibou Duolingo). La mascotte LIMO harcèle gentiment son conseiller
jour après jour (relance, annonce, relances de nuit, anniversaire) jusqu'au mandat signé, puis s'adresse au
spectateur. Sans voix : bulles, textes « mème » et bruitages. Données affichées = exemples fictifs.

Usage : python3 outils/viral.py   (réécrit reels/viral-01-il-te-lache-plus.html)
"""
import pathlib

from cine import COMMON, FACES
from lifestyle import V
from premium2 import SHELL
from premium3 import CSS
from premium4 import SH4

NAME = "viral-01-il-te-lache-plus"
PRE = V("v1", "agent-voiture-grade", 9.0, 5.0, 1)
EXTRA_CSS = """
      .meme { font-family: Montserrat, sans-serif; font-weight: 800; color: #fff; -webkit-text-stroke: 3px #000; paint-order: stroke fill; text-shadow: 0 6px 0 rgba(0,0,0,.35); line-height: 1.05; }
      .meme b { color: #ffe14d; }
"""
BODY = SH4 + r"""
        const sec = (t0, t1, css = {}, html = "") => {
          const l = C.ab(Object.assign({ left: "0", top: "0", width: "1080px", height: "1920px", overflow: "hidden" }, css), html);
          tl.set(l, { opacity: 0 }, 0); tl.set(l, { opacity: 1 }, t0); if (t1 != null) tl.set(l, { opacity: 0 }, t1);
          return l;
        };
        const meme = (t, t1, html, top = 190, fs = 66) => {
          const e = FX.ab(root, { left: "50px", right: "50px", top: top + "px", textAlign: "center", zIndex: 31, fontSize: fs + "px" }, `<div class="meme">${html}</div>`);
          tl.set(e, { opacity: 0 }, 0);
          tl.fromTo(e, { opacity: 0, scale: 1.4 }, { opacity: 1, scale: 1, duration: 0.2, ease: "power4.out", immediateRender: false }, t);
          tl.to(e, { opacity: 0, duration: 0.1 }, t1);
          K.sfx(t, "thump", 0.25);
          return e;
        };
        const bub = (html, css, t, t1, o) => { const e = N.say(html, css, t, o); tl.to(e, { opacity: 0, scale: 0.9, duration: 0.15 }, t1); return e; };
        const cutTo = (t) => { C.flash(t, "#ffffff", 0.6); K.sfx(t, "whoosh", 0.16, 0, { d: 0.3, f0: 250, f1: 2600, pk: 0.4 }); };

        // ── fonds et contenus (sous la mascotte)
        const s0 = sec(0, 3.2); FX.aurora(s0, 0, 3.3, { colors: ["#6b4fe0", "#2cc4b5", "#3a2a9a"] });
        const s1 = sec(3.2, 9.0); FX.aurora(s1, 3.1, 9.1, { colors: ["#1d2a7a", "#4b2a9a", "#0f3d6a"], a: 0.5 });
        const NT = [["APPEL À FAIRE", "Mme Martin attend ton appel.", 3.6], ["RAPPEL", "Toujours rien ? Je dis ça, je dis rien.", 4.7], ["MESSAGE PRÊT", "Je t’ai écrit le message. Tu cliques juste.", 5.8], ["ENVOYÉ", "Message envoyé. Je savais que t’y arriverais.", 7.0]];
        NT.forEach((n, i) => N.notif({ title: n[0], time: "", text: n[1], parent: s1, snd: i === 3 ? "success" : "notif", g: 0.26 }, { left: "70px", top: 380 + i * 175 + "px" }, n[2]));
        const s2 = sec(9.0, 14.0); FX.ab(s2, { inset: "0", background: "linear-gradient(180deg, rgba(5,6,15,.55) 0%, rgba(5,6,15,0) 30%, rgba(5,6,15,0) 60%, rgba(5,6,15,.6) 100%)" });
        tl.fromTo(document.getElementById("v1"), { scale: 1.15 }, { scale: 1.04, duration: 5, ease: "power1.out" }, 9.0);
        const ann = FX.glass(s2, { left: "90px", width: "900px", top: "400px", padding: "26px 30px" }, `<span style="display:block;font-size:24px;letter-spacing:.06em;color:rgba(255,255,255,.75)">LIMO · ANNONCE RÉDIGÉE</span><b style="display:block;margin-top:8px;font-family:Montserrat,sans-serif;font-weight:800;font-size:40px;line-height:1.15">Maison en pierre, vue sur la vallée</b><span style="display:block;margin-top:10px;font-size:28px;line-height:1.4;color:rgba(255,255,255,.9)">4 chambres, grand terrain, calme absolu à 10 min de Brive…</span><span class="pb" style="display:inline-block;margin-top:14px;padding:10px 26px;border-radius:999px;background:#2cc4b5;font-family:Montserrat,sans-serif;font-weight:800;font-size:28px">Prête à publier</span>`);
        tl.set(ann, { opacity: 0 }, 0); tl.fromTo(ann, { opacity: 0, y: 60 }, { opacity: 1, y: 0, duration: 0.5, ease: "expo.out" }, 11.0);
        tl.set(K.$(".pb", ann), { opacity: 0 }, 0); tl.fromTo(K.$(".pb", ann), { opacity: 0, scale: 0.6 }, { opacity: 1, scale: 1, duration: 0.35, ease: "back.out(2.2)" }, 12.2); K.sfx(12.2, "success", 0.24);
        const s3 = sec(14.0, 19.0); FX.aurora(s3, 13.9, 19.1, { colors: ["#1d2a7a", "#2b1f5e", "#0f2a4a"], a: 0.5 });
        const clk = FX.glass(s3, { left: "0", right: "0", margin: "0 auto", width: "520px", top: "300px", padding: "22px 0", textAlign: "center", fontFamily: "Montserrat, sans-serif", fontWeight: "800", fontSize: "150px", lineHeight: "1", borderRadius: "40px" }, "23:04");
        tl.set(clk, { opacity: 0 }, 0); tl.fromTo(clk, { opacity: 0, scale: 0.8 }, { opacity: 1, scale: 1, duration: 0.45, ease: "expo.out" }, 14.2);
        card(s3, "refresh", "12 relances programmées", "Envoi demain à 9:00", { top: "720px" }, 16.6, { check: true });
        const s4 = sec(19.0, 23.5); FX.aurora(s4, 18.9, 23.6, { colors: ["#ff8f8f", "#6b4fe0", "#3a2a9a"], a: 0.45 });
        const bd = bday(s4, "M. Durand", 19.4, 360);
        tapSend(bd[1], 21.4);
        const s5 = sec(23.5, 28.5, {}, `<img src="assets/img/bien-mas-lavande.jpg" alt="" style="position:absolute;left:-60px;top:-100px;width:1200px;height:2120px;object-fit:cover" /><div style="position:absolute;inset:0;background:rgba(5,6,15,.45)"></div>`);
        tl.fromTo(K.$("img", s5), { scale: 1.2 }, { scale: 1.04, duration: 5, ease: "power1.out" }, 23.5);
        const st = FX.ab(s5, { left: "0", right: "0", top: "420px", textAlign: "center" }, `<span style="display:inline-block;padding:18px 36px;border:8px solid #2cc4b5;border-radius:22px;background:rgba(5,6,15,.45);color:#2cc4b5;font-family:Montserrat,sans-serif;font-weight:800;font-size:72px;line-height:1.05;transform:rotate(-6deg)">MANDAT EXCLUSIF<br>SIGNÉ</span>`);
        tl.set(st, { opacity: 0 }, 0); tl.fromTo(st, { opacity: 0, scale: 2.4 }, { opacity: 1, scale: 1, duration: 0.25, ease: "power4.in" }, 23.8);
        K.sfx(24.05, "slam", 0.4); tl.to(st, { x: 12, duration: 0.04, yoyo: true, repeat: 7, ease: "none" }, 24.05);
        const s6 = sec(28.5, 32.2); FX.aurora(s6, 28.4, 32.3, { colors: ["#2cc4b5", "#6b4fe0", "#1d6f8a"] });
        [s1, s2, s3, s4, s5, s6].forEach((s, i) => cutTo([3.2, 9.0, 14.0, 19.0, 23.5, 28.5][i]));

        // ── la mascotte (au-dessus des fonds)
        const M = N.mascot({ left: "390px", top: "780px", width: "300px" });
        const mo = M.el || M.out || K.$(".m-out:last-of-type", root);
        M.enter(0.15);
        M.move(0.15, { scale: 1.7 }, 0.01);
        M.expr("think", 1.2); M.expr("angry", 2.3); M.shake(2.3);
        M.move(3.2, { x: 330, y: 520, scale: 0.75 }, 0.4); M.expr("wow", 3.6); M.expr("angry", 4.7); M.expr("wink", 5.8); M.expr("happy", 7.0); M.hop(7.0, 60);
        M.move(9.0, { x: -300, y: 520, scale: 0.72 }, 0.35); M.wave(9.4); M.expr("happy", 9.4); M.expr("wink", 12.2);
        M.move(14.0, { x: 0, y: 360, scale: 0.95 }, 0.4); M.expr("sleep", 14.4); M.expr("wink", 16.6);
        M.move(19.0, { x: 0, y: 420, scale: 0.9 }, 0.4); M.expr("heart", 19.6); M.hop(21.5, 110);
        M.move(23.5, { x: 0, y: 380, scale: 1.05 }, 0.35); M.expr("euro", 24.2); M.hop(24.6, 120); M.tilt(25.2, 12); M.tilt(25.6, -12); M.tilt(26.0, 12); M.tilt(26.4, 0); M.expr("happy", 26.4);
        M.move(28.5, { x: 0, y: 0, scale: 1.6 }, 0.45); M.expr("wink", 28.9); M.glow(29.0);
        M.move(31.9, { opacity: 0 }, 0.25);
        // confettis à la signature et à l'anniversaire
        [[21.5, 540, 1250], [24.1, 540, 900]].forEach(([t, x, y], k) => {
          const sp = K.sparkles(root, x, y, 26, 420, 360, 7 + k);
          K.burst(sp, t);
        });

        // ── bulles (au-dessus de la mascotte) et textes mème
        bub("T’as rappelé<br>Mme Martin ?", { left: "300px", top: "330px", width: "480px", fontSize: "50px" }, 1.0, 3.05, { tail: "down" });
        bub("Pendant que tu conduis,<br>j’écris ton annonce.", { left: "300px", top: "1140px", width: "700px", fontSize: "40px" }, 9.5, 13.85, { tail: "left" });
        bub("Va dormir.<br>Je gère les relances.", { left: "190px", top: "880px", width: "700px", fontSize: "44px" }, 15.0, 18.85, { tail: "down" });
        bub("Je t’avais dit<br>de la rappeler.", { left: "190px", top: "780px", width: "700px", fontSize: "48px" }, 25.4, 28.35, { tail: "down" });
        bub("Et toi ?<br>Tu attends quoi pour m’essayer ?", { left: "140px", top: "300px", width: "800px", fontSize: "50px" }, 29.0, 31.85, { tail: "down" });
        meme(0.1, 3.1, "POV : ton assistant immo<br><b>ne te lâche plus</b>", 150, 62);
        meme(3.3, 8.9, "Jour 1", 190, 80);
        meme(9.1, 13.9, "Jour 3", 190, 80);
        meme(14.1, 18.9, "Jour 5", 150, 70);
        meme(19.1, 23.4, "Jour 8", 190, 80);
        meme(23.6, 28.4, "Jour 12", 190, 80);
        outro(32.2);
"""

if __name__ == "__main__":
    html = SHELL.format(title="LIMO, il te lâche plus", faces=FACES, css=(CSS + EXTRA_CSS).strip("\n"), body=(COMMON + BODY).strip("\n"), dur=37.5, name=NAME)
    html = html.replace('      <section id="s-main"', PRE + '      <section id="s-main"', 1)
    pathlib.Path(f"reels/{NAME}.html").write_text(html, encoding="utf-8")
    print("reels/" + NAME + ".html")
