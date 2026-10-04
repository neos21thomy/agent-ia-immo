"""Film V6 « Moi, avant / aujourd'hui » : version NATURELLE façon story Instagram d'un conseiller (demande de Thomy :
pas de voix, pas de musique, rendu naturel). Uniquement ses vidéos et photos de Corrèze en plein écran, textes courts
à la 1re personne au style natif Instagram, fondus discrets, aucune carte d'interface ; la marque n'arrive qu'à la fin.
Données affichées = exemples fictifs.

Usage : python3 outils/viral6.py   (réécrit reels/viral-06-moi-avant-aujourdhui.html)
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from cine import COMMON, FACES  # noqa: E402
from lifestyle import V  # noqa: E402
from premium2 import SHELL  # noqa: E402
from premium3 import CSS  # noqa: E402
from premium4 import SH4  # noqa: E402

NAME = "viral-06-moi-avant-aujourdhui"
T_OUT = 28.2
DUR = 33.5
PRE = (V("v1", "agent-deborde", 0, 4.0, 1) + V("v2", "maison-contemporaine", 19.1, 4.6, 2)
       + V("v3", "piscine-liberte", 23.1, 2.7, 3)
       + V("v3b", "piscine-liberte", 25.8, 2.6, 4, 4.65).replace(' data-track-index="4"', ' data-playback-rate="0.75" data-track-index="4"'))
EXTRA_CSS = """
      .ig { display: inline; padding: 6px 18px; line-height: 1.62; border-radius: 12px; background: rgba(0,0,0,.6); color: #fff; font-family: Inter, sans-serif; font-weight: 600; font-size: 50px; -webkit-box-decoration-break: clone; box-decoration-break: clone; }
"""
BODY = SH4 + r"""
        const TOP = document.getElementById("root");
        tl.set([C.barT, C.barB], { opacity: 0 }, 0);
        // plan en fondu court (0,3 s), comme un montage fait au téléphone
        const shot = (t0, t1, html = "") => {
          const l = FX.ab(TOP, { left: "0", top: "0", width: "1080px", height: "1920px", overflow: "hidden" }, html);
          tl.set(l, { opacity: 0 }, 0);
          tl.to(l, { opacity: 1, duration: 0.3, ease: "none" }, Math.max(0, t0 - 0.15));
          tl.to(l, { opacity: 0, duration: 0.3, ease: "none" }, t1 - 0.15);
          return l;
        };
        const pano = (src, x0, x1, t0, t1) => {
          const l = shot(t0, t1, `<img src="assets/img/${src}.jpg" alt="" style="position:absolute;left:0;top:0;height:1920px" />`);
          tl.fromTo(K.$("img", l), { x: -x0 }, { x: -x1, duration: t1 - t0 + 0.3, ease: "none" }, t0 - 0.15);
          return l;
        };
        const push = (id, t0, t1) => tl.fromTo(document.getElementById(id), { scale: 1.0 }, { scale: 1.05, duration: t1 - t0, ease: "none" }, t0);
        // texte au style natif Instagram, posé d'un coup (comme tapé dans l'appli)
        const say = (t0, t1, html, top = 760) => {
          const e = FX.ab(TOP, { left: "70px", right: "70px", top: top + "px", textAlign: "center", zIndex: 34 }, `<span class="ig">${html}</span>`);
          tl.set(e, { opacity: 0 }, 0);
          tl.to(e, { opacity: 1, duration: 0.12, ease: "none" }, t0);
          tl.to(e, { opacity: 0, duration: 0.12, ease: "none" }, t1 - 0.12);
        };

        shot(0, 3.8); push("v1", 0, 3.8);
        say(0.3, 3.75, "Moi, avant :<br>19 h, encore au bureau.");
        pano("correze-pont", 1300, 1600, 3.8, 7.8);
        say(4.1, 7.75, "Aujourd’hui, LIMO suit<br>mes 12 mandats.");
        pano("correze-ruelle", 1100, 1400, 7.8, 11.6);
        say(8.1, 11.55, "L’annonce de la maison de bourg ?<br>Déjà rédigée.");
        pano("correze-riviere", 1050, 1300, 11.6, 15.6);
        say(11.9, 15.55, "Mes 3 acquéreurs ?<br>Relancés pendant que je roulais.");
        pano("correze-halle", 700, 950, 15.6, 19.4);
        say(15.9, 19.35, "Mon estimation de 14 h ?<br>Prête avant moi.");
        shot(19.4, 23.4); push("v2", 19.4, 23.4);
        say(19.7, 23.35, "Le compromis ?<br>Diagnostics 6/6 reçus.");
        shot(23.4, T_OUT);
        say(23.8, T_OUT - 0.05, "Et moi…<br>je profite. ☀️", 230);
        outro(T_OUT);
""".replace("T_OUT", str(T_OUT))

if __name__ == "__main__":
    html = SHELL.format(title="Moi, avant / aujourd'hui", faces=FACES, css=(CSS + EXTRA_CSS).strip("\n"), body=(COMMON + BODY).strip("\n"), dur=DUR, name=NAME)
    html = html.replace('      <section id="s-main"', PRE + '      <section id="s-main"', 1)
    (HERE.parent / "reels" / f"{NAME}.html").write_text(html, encoding="utf-8")
    print("reels/" + NAME + ".html")
