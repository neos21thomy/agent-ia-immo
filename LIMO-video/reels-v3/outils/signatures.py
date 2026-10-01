"""Film émotionnel « Derrière chaque signature » sur les photos de signatures chez le notaire
fournies par Thomy (visages déjà floutés). Les photos restent hors du dépôt public
(assets/img/signatures/ est ignoré par git).

Usage : python3 outils/signatures.py   (réécrit reels/sign-01-derriere-chaque-signature.html)
"""
import pathlib

from cine import COMMON, FACES, GLASS, SHELL
from lifestyle import TOOLS

CSS = """
      .gchip.big { height: 96px; padding: 0 40px; border-radius: 48px; gap: 18px; font-size: 44px; font-weight: 800; background: rgba(255,255,255,.18); backdrop-filter: blur(6px); }
      .gchip.big svg.i { width: 44px; height: 44px; }
"""
NAME = "sign-01-derriere-chaque-signature"
BODY = TOOLS + r"""
        const dark = C.bg({ background: "#05060f" });
        const SRC = (n) => `assets/img/signatures/sign-${String(n).padStart(2, "0")}.jpg`;
        // fond : la photo en grand, floutée et assombrie
        const back = (n, t0, t1) => {
          const b = C.ab({ left: "-120px", top: "-120px", width: "1320px", height: "2160px" }, `<img src="${SRC(n)}" alt="" style="width:100%;height:100%;object-fit:cover;filter:blur(38px) brightness(.42) saturate(1.2)" />`);
          tl.set(b, { opacity: 0 }, 0);
          tl.to(b, { opacity: 1, duration: 0.5 }, t0);
          tl.to(b, { opacity: 0, duration: 0.5 }, t1);
          return b;
        };
        // polaroïd qui se pose sur la pile
        const pola = (n, t, rot, t1) => {
          const p = C.ab({ left: "160px", top: "600px", width: "760px" }, `<div style="background:#fbfaf7;padding:18px 18px 64px;border-radius:8px;box-shadow:0 40px 90px rgba(0,0,0,.6)"><img src="${SRC(n)}" alt="" style="display:block;width:100%;height:860px;object-fit:cover;border-radius:3px" /></div>`);
          tl.set(p, { opacity: 0 }, 0);
          tl.fromTo(p, { opacity: 0, scale: 1.28, rotation: rot * 2.5, y: -40 }, { opacity: 1, scale: 1, rotation: rot, y: 0, duration: 0.55, ease: "power3.out" }, t);
          tl.to(p, { scale: 1.04, duration: 1.6, ease: "none" }, t + 0.55);
          K.sfx(t + 0.3, "thump", 0.16);
          tl.to(p, { opacity: 0, duration: 0.35 }, t1);
          return p;
        };
        const PILE = [2, 1, 4, 6, 7, 11, 3, 9];
        const R = [-4, 3, -2, 4, -3, 2, -4, 3];
        PILE.forEach((n, i) => {
          const t = 2.4 + i * 1.35;
          back(n, t, t + 1.6);
          pola(n, t, R[i], i === PILE.length - 1 ? 13.5 : t + 1.9);
        });
        // accroche
        const h0 = C.title("Conseiller immo,", { top: "300px", fontSize: "52px" }, 0.2, { color: "#d9ceff", snd: false });
        const h1 = C.title("tu te souviens de ce [moment] ?", { top: "380px", fontSize: "76px" }, 0.6, { color: "#ffffff", accent: "#d9ceff" });
        C.out([h0, h1], 2.6, 0.3);
        const L = [
          ["Le jour de la [signature].", 3.0, 5.6],
          ["Des familles [heureuses].", 5.8, 8.3],
          ["Un projet de vie qui se [concrétise].", 8.5, 10.9],
          ["Et derrière chaque pouce levé…", 11.1, 13.4],
        ];
        L.forEach((l) => {
          const e = C.title(l[0], { top: "330px", fontSize: "66px" }, l[1], { color: "#ffffff", accent: "#d9ceff", snd: false });
          e.classList.add("shade");
          C.out(e, l[2], 0.3);
        });
        // le travail invisible
        back(9, 13.4, 17.0);
        const w = C.title("…des semaines de [travail] [invisible].", { top: "330px", fontSize: "66px" }, 13.6, { color: "#ffffff", accent: "#ff9b9b" });
        w.classList.add("shade");
        C.out(w, 16.8, 0.3);
        [["phone", "Appels le soir"], ["refresh", "Relances"], ["home", "Visites"], ["pen", "Compromis"], ["image", "Diagnostics"], ["send", "Échanges notaire"]]
          .forEach((c, i) => gchip(`${K.icon(c[0])}${c[1]}`, 620 + i * 140, 14.1 + i * 0.32, 16.8, "big"));
        // la mosaïque
        const t2 = C.title("Ton métier, c’est [ça].", { top: "330px", fontSize: "84px" }, 17.3, { color: "#ffffff", accent: "#d9ceff" });
        const t3 = C.title("Des moments qui comptent.", { top: "1540px", fontSize: "48px" }, 18.6, { color: "#d9ceff", snd: false });
        const tiles = [];
        for (let i = 0; i < 12; i++) {
          const c = C.ab({ left: 39 + (i % 4) * 254 + "px", top: 560 + Math.floor(i / 4) * 314 + "px", width: "240px", height: "300px", borderRadius: "16px", overflow: "hidden", boxShadow: "0 18px 40px rgba(0,0,0,.5)" }, `<img src="${SRC(i + 1)}" alt="" style="width:100%;height:100%;object-fit:cover" />`);
          tl.set(c, { opacity: 0 }, 0);
          tl.fromTo(c, { opacity: 0, scale: 0.6, y: 40 }, { opacity: 1, scale: 1, y: 0, duration: 0.45, ease: "back.out(1.5)" }, 17.2 + i * 0.07);
          tiles.push(c);
        }
        K.sfx(17.2, "success", 0.2);
        tl.to(tiles, { scale: 1.03, duration: 2.3, ease: "none" }, 18.5);
        C.out([t2, t3, ...tiles], 20.8, 0.3);
        // LIMO
        lightEnd(21.2);
        const logo = C.ab({ left: "240px", top: "440px", width: "600px", height: "227px" }, `<img src="assets/img/limo-logo-ad.png" alt="LIMO" style="width:100%;height:100%" />`);
        tl.set(logo, { opacity: 0 }, 0);
        tl.fromTo(logo, { opacity: 0, scale: 1.25, filter: "blur(14px)" }, { opacity: 1, scale: 1, filter: "blur(0px)", duration: 0.8, ease: "power3.out" }, 21.6);
        K.sfx(21.7, "thump", 0.4);
        C.sweep(logo, 22.4, 0.9);
        const e1 = C.title("LIMO s’occupe du [reste].", { top: "760px", fontSize: "70px" }, 22.4);
        const pills = ["Relances automatiques", "Dossiers complets", "Documents classés", "Suivi jusqu’au notaire"].map((txt, i) => {
          const p = C.ab({ left: "0", right: "0", top: 900 + i * 104 + "px", textAlign: "center" }, `<span style="display:inline-flex;align-items:center;gap:14px;padding:16px 30px;border-radius:999px;background:#fff;box-shadow:0 12px 30px rgba(60,40,140,.14);font-family:Montserrat,sans-serif;font-weight:800;font-size:34px;color:#1c1f4a"><span style="width:30px;height:30px;border-radius:50%;background:#2cc4b5;display:inline-block"></span>${txt}</span>`);
          tl.set(p, { opacity: 0 }, 0);
          K.pop(p, 23.0 + i * 0.35, { s: 0.7 });
          K.sfx(23.0 + i * 0.35, "pop", 0.12, 0, { f: 900 });
          return p;
        });
        const e2 = C.title("Pour un suivi [ultra] [pro],", { top: "1360px", fontSize: "56px" }, 24.6, { snd: false });
        const e3 = C.title("du mandat à la signature.", { top: "1436px", fontSize: "56px" }, 25.0, { snd: false });
        C.out([logo, e1, e2, e3, ...pills], 27.2, 0.3);
        window.__TE = 27.5;
        N.outro(27.5, "essai");
        const m = N.mascot({ left: "440px", top: "1500px", width: "200px" });
        m.enter(29.0);
        m.wave(29.7);
"""

if __name__ == "__main__":
    html = SHELL.format(title="LIMO, derrière chaque signature", faces=FACES, css=(GLASS + CSS).strip("\n"), body=(COMMON + BODY).strip("\n"), dur=32.0, name=NAME)
    pathlib.Path(f"reels/{NAME}.html").write_text(html, encoding="utf-8")
    print("reels/" + NAME + ".html")
