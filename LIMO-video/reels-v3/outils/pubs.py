"""Versions « publicité Meta » des meilleurs Reels : carte de fin « pub » (essai 14 jours, bouton cliquable
de la pub) remontée hors des zones d'interface. Les Reels source sont réutilisés tels quels.

Usage : python3 outils/pubs.py   (réécrit reels/pub-*.html)
"""
import pathlib
import re

PUBS = {
    "pub-01-trois-agences": "hook-02-trois-agences",
    "pub-02-ton-concurrent": "hook-05-ton-concurrent",
    "pub-03-qui-va-vendre": "hook-07-qui-va-vendre",
    "pub-04-entretien-embauche": "mascotte-02-entretien-embauche",
    "pub-05-mieux-que-ton-stagiaire": "mascotte-10-mieux-que-ton-stagiaire",
    "pub-06-rappelez-moi-en-mars": "nat-01-rappelez-moi-en-mars",
}

if __name__ == "__main__":
    for name, src in PUBS.items():
        h = pathlib.Path(f"reels/{src}.html").read_text(encoding="utf-8")
        h, n = re.subn(r'N\.outro\(([\d.]+), "\w+"\)', r'N.outro(\1, "pub")', h)
        assert n == 1, (src, n)
        h = h.replace(f"assets/audio/{src}.wav", f"assets/audio/{name}.wav")
        # police de l'accroche (absente des films « naturel » générés avant la série hooks)
        if "Montserrat Hook" not in h.split("</style>")[0]:
            h = h.replace("    <style>\n", '    <style>\n      @font-face { font-family: "Montserrat Hook"; src: url("assets/fonts/montserrat-latin-800-normal.woff2") format("woff2"); font-weight: 800; font-style: normal; }\n', 1)
        # mascotte : sous le bouton, au centre (visible aussi en 4:5)
        h = h.replace("x: 890 - (left + W / 2), y: 1610 - (top + H / 2), scale: s, rotation: -8", "x: 540 - (left + W / 2), y: 1370 - (top + H / 2), scale: s, rotation: 0").replace("const s = 260 / W;", "const s = 200 / W;")
        pathlib.Path(f"reels/{name}.html").write_text(h, encoding="utf-8")
        print(f"reels/{name}.html  ←  {src}")
