"""Film V3 « J'ai préparé ta journée » : la mascotte LIMO, apaisante et bienveillante, arrive le matin et
présente en détail tout ce qu'elle a déjà fait pour le conseiller (relance, annonce, estimation, mails,
anniversaire, frais kilométriques, relances, publication), puis lui rend son temps : « consacre-toi à l'essentiel ».
Format POV + liste qui se coche (très regardé jusqu'au bout). Sans voix. Données affichées = exemples fictifs.

Usage : python3 outils/viral3.py   (réécrit reels/viral-03-jai-prepare-ta-journee.html)
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from cine import COMMON, FACES  # noqa: E402
from lifestyle import V  # noqa: E402
from premium2 import SHELL  # noqa: E402
from premium3 import CSS  # noqa: E402
from premium4 import SH4  # noqa: E402

NAME = "viral-03-jai-prepare-ta-journee"
T_OUT = 27.6
DUR = round(T_OUT + 5.3, 2)
PRE = V("v1", "vendeuse-canape-grade", 22.4, 5.0, 1)
EXTRA_CSS = """
      .cap { display: inline-block; padding: 14px 26px 16px; border-radius: 18px; background: #fff; color: #111; font-family: Montserrat, sans-serif; font-weight: 800; font-size: 44px; line-height: 1.2; box-shadow: 0 10px 30px rgba(0,0,0,.2); }
      .row { display: flex; align-items: center; gap: 22px; padding: 34px 0; border-top: 1px solid rgba(255,255,255,.16); }
      .row:first-of-type { border-top: 0; }
      .row .ic { flex: none; width: 104px; height: 104px; border-radius: 28px; display: flex; align-items: center; justify-content: center; }
      .row .ic svg { width: 56px; height: 56px; color: #fff; }
      .row .tx { flex: 1; min-width: 0; }
      .row .tx b { display: block; font-family: Montserrat, sans-serif; font-weight: 800; font-size: 44px; line-height: 1.12; }
      .row .tx span { display: block; margin-top: 6px; font-family: Inter, sans-serif; font-size: 33px; line-height: 1.3; color: rgba(255,255,255,.85); }
      .row .ok { flex: none; width: 70px; height: 70px; border-radius: 50%; background: #2cc4b5; display: flex; align-items: center; justify-content: center; }
      .row .ok svg { width: 34px; height: 34px; color: #fff; }
"""
BODY = SH4 + r"""
        const TOP = document.getElementById("root");
        tl.set([C.barT, C.barB], { opacity: 0 }, 0);
        const WARM = `<img src="assets/img/bien-mas-lavande.jpg" alt="" style="position:absolute;left:-120px;top:-120px;width:1320px;height:2160px;object-fit:cover;filter:blur(36px) brightness(.55) saturate(1.2)" /><div style="position:absolute;inset:0;background:linear-gradient(180deg,rgba(243,163,91,.35) 0%,rgba(107,79,224,.35) 55%,rgba(10,8,30,.7) 100%)"></div>`;
        const cap = (t0, t1, html, top = 170) => {
          const el = FX.ab(TOP, { left: "60px", right: "60px", top: top + "px", textAlign: "center", zIndex: 36 }, `<span class="cap">${html}</span>`);
          tl.set(el, { opacity: 0 }, 0);
          tl.fromTo(el, { opacity: 0, y: 16 }, { opacity: 1, y: 0, duration: 0.45, ease: "power2.out", immediateRender: false }, t0);
          tl.to(el, { opacity: 0, duration: 0.3 }, t1 - 0.3);
          return el;
        };
        const soft = (t) => K.sfx(t, "sparkle", 0.08);
        // panneau « j'ai fait ça pour toi » : une ligne détaillée qui se coche toutes les 2,1 s
        const panel = (l, title, rows, t0) => {
          const g = FX.glass(l, { left: "50px", width: "980px", top: "500px", padding: "30px 36px 14px", boxSizing: "border-box" },
            `<div class="hd" style="font-family:Montserrat,sans-serif;font-weight:800;font-size:50px;padding-bottom:14px">${title}</div>` +
            rows.map((r) => `<div class="row"><span class="ic" style="background:${r[3]}">${K.icon(r[0])}</span><span class="tx"><b>${r[1]}</b><span>${r[2]}</span></span><span class="ok">${K.icon("check")}</span></div>`).join(""));
          tl.set(g, { opacity: 0 }, 0);
          tl.fromTo(g, { opacity: 0, y: 40 }, { opacity: 1, y: 0, duration: 0.7, ease: "power3.out", immediateRender: false }, t0);
          K.sfx(t0, "pad", 0.12, 0, { d: 2.4 });
          const ts = [];
          K.$$(".row", g).forEach((r, i) => {
            const t = t0 + 0.6 + i * 2.1;
            ts.push(t);
            tl.set(r, { opacity: 0 }, 0);
            tl.fromTo(r, { opacity: 0, x: 40 }, { opacity: 1, x: 0, duration: 0.55, ease: "power3.out", immediateRender: false }, t);
            const ok = K.$(".ok", r);
            tl.set(ok, { scale: 0 }, 0);
            tl.to(ok, { scale: 1, duration: 0.4, ease: "back.out(2.2)" }, t + 1.0);
            K.sfx(t + 1.0, "success", 0.14);
            FX.sheen(g, t + 1.0, 0.9);
          });
          return ts;
        };

        // ── S1 · 0–3,6 : le matin, LIMO arrive en douceur
        const s1 = FX.layer(0, 3.6, {}, WARM);
        cap(0.2, 3.5, "POV : ton assistant immo<br>s’est levé avant toi ☕");
        FX.ab(s1, { left: "0", right: "0", top: "1380px", textAlign: "center" }, `<div style="font-family:Inter,sans-serif;font-weight:700;font-size:120px;color:#fff;line-height:1">7:42</div><div style="font-family:Inter,sans-serif;font-size:34px;color:rgba(255,255,255,.85);margin-top:6px">mardi 6 octobre</div>`);
        K.sfx(0.1, "pad", 0.16, 0, { d: 3.2 });
        C.leak(0.2, 3.0);

        // ── P1 · 3,6–13,0
        const p1 = FX.layer(3.6, 13.0, {}, WARM);
        const T1 = panel(p1, "Pendant que tu dormais, j’ai :", [
          ["reply", "Relancé Mme Martin", "SMS envoyé à 8:00 · elle confirme la visite jeudi à 14&nbsp;h", "rgba(44,196,181,.45)"],
          ["pen", "Rédigé l’annonce du mas en pierre", "165&nbsp;m² · 5&nbsp;chambres · 2&nbsp;400&nbsp;m² de terrain · prête à publier", "rgba(107,79,224,.55)"],
          ["calc", "Préparé ton estimation de 10&nbsp;h", "3 ventes comparables · fourchette 285&nbsp;000&nbsp;–&nbsp;305&nbsp;000&nbsp;€", "rgba(243,163,91,.55)"],
          ["mail", "Trié tes 47 mails", "3 réponses prêtes à valider · 44 archivés", "rgba(90,140,255,.5)"],
        ], 3.7);
        // ── P2 · 13,0–22,4
        const p2 = FX.layer(13.0, 22.4, {}, WARM);
        FX.whip(p1, p2, 12.8);
        const T2 = panel(p2, "Et pour la suite, j’ai :", [
          ["cake", "Souhaité l’anniversaire de M.&nbsp;Durand", "message personnalisé, envoyé à 9:00", "rgba(255,143,143,.55)"],
          ["car", "Calculé tes frais kilométriques", "1&nbsp;248&nbsp;km en octobre · tableau prêt pour ta compta", "rgba(44,196,181,.45)"],
          ["refresh", "Programmé tes 12 relances", "acquéreurs et vendeurs · aucune oubliée", "rgba(107,79,224,.55)"],
          ["megaphone", "Préparé ta publication Instagram", "nouveau mandat · photos et texte · prête à poster", "rgba(243,163,91,.55)"],
        ], 13.4);

        // ── S3 · 22,4–27,6 : toi, consacre-toi à l'essentiel
        const v1 = document.getElementById("v1");
        const s3 = FX.layer(22.4, T_OUT); shade(s3);
        FX.whip(p2, [v1, s3], 22.2);
        tl.fromTo(v1, { scale: 1.08 }, { scale: 1.0, duration: 5.2, ease: "power1.out" }, 22.4);
        cap(22.6, T_OUT, "toi, consacre-toi à l’essentiel :");
        FX.rise(s3, "[tes] [clients.]", { top: "300px", fontSize: "120px", textShadow: "0 8px 30px rgba(0,0,0,.45)" }, 23.1, { accent: "#ffffff" });

        // ── la mascotte, douce et souriante (au-dessus des calques)
        const M = N.mascot({ left: "390px", top: "760px", width: "300px" }, { expr: "happy" });
        TOP.appendChild(M.el); M.el.style.zIndex = "30";
        M.enter(0.3);
        M.move(0.3, { y: -60, scale: 1.25 }, 0.01);
        M.wave(1.0); M.blink(2.4);
        const hi = N.say("Bonjour Julien ☀️<br>J’ai préparé ta journée.", { left: "190px", top: "380px", width: "700px", fontSize: "48px" }, 1.3, { tail: "down", n: 3, g: 0.08 });
        TOP.appendChild(hi); hi.style.zIndex = "34"; tl.to(hi, { opacity: 0, duration: 0.3 }, 3.3);
        // sur les panneaux : en haut, elle hoche la tête à chaque ligne cochée
        M.move(3.5, { x: 0, y: -600, scale: 0.68 }, 0.6);
        [...T1, ...T2].forEach((t, i) => { M.hop(t + 1.0, 26); if (i % 3 === 1) M.blink(t + 1.6); });
        M.expr("wink", 12.0); M.expr("happy", 13.3, false); M.expr("heart", 21.0);
        // sur le plan réel : dans un coin, elle salue
        M.move(22.4, { x: 340, y: 560, scale: 0.58 }, 0.01); M.expr("happy", 22.4, false); M.wave(24.0);
        const rest = N.say("Le reste,<br>je m’en occupe. 🙂", { left: "250px", top: "1290px", width: "580px", fontSize: "44px" }, 24.4, { tail: "down", n: 3, g: 0.08 });
        TOP.appendChild(rest); rest.style.zIndex = "34"; tl.to(rest, { opacity: 0, duration: 0.25 }, T_OUT - 0.3);
        M.move(T_OUT - 0.3, { opacity: 0 }, 0.25);
        outro(T_OUT);
""".replace("T_OUT", str(T_OUT))

if __name__ == "__main__":
    html = SHELL.format(title="LIMO, j'ai préparé ta journée", faces=FACES, css=(CSS + EXTRA_CSS).strip("\n"), body=(COMMON + BODY).strip("\n"), dur=DUR, name=NAME)
    html = html.replace('      <section id="s-main"', PRE + '      <section id="s-main"', 1)
    out = pathlib.Path(__file__).resolve().parent.parent / "reels" / f"{NAME}.html"
    out.write_text(html, encoding="utf-8")
    print("reels/" + NAME + ".html")
