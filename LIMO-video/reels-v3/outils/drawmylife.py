"""« Draw my life : conseiller immo » : la vraie journée d'un conseiller immobilier, racontée façon Draw my life
(dessins au feutre tracés en direct, écriture manuscrite, mots forts surlignés), pour être partagée par les conseillers.
Pas de pub : LIMO n'apparaît qu'en petite signature à la fin. Musique douce, bruit de feutre, sans voix.

Usage : python3 outils/drawmylife.py   (réécrit reels/draw-01-la-vie-dun-conseiller.html)
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from cine import COMMON, FACES  # noqa: E402
from premium2 import SHELL  # noqa: E402
from premium3 import CSS  # noqa: E402

NAME = "draw-01-la-vie-dun-conseiller"
DUR = 57.0
CSS_D = """
      .pap { position: absolute; inset: 0; background: radial-gradient(ellipse at 50% 45%, #fffdf8 0%, #f8f4ea 70%, #efe9da 100%); }
      .hw { position: absolute; left: 70px; right: 70px; text-align: center; font-family: Caveat, cursive; font-weight: 700; color: #232323; line-height: 1.08; }
      .hw .wd { display: inline-block; margin: 0 .12em; }
      .hw .k { color: #5b3fd6; background: linear-gradient(180deg, rgba(255,224,102,0) 55%, rgba(255,224,102,.95) 55%, rgba(255,224,102,.95) 92%, rgba(255,224,102,0) 92%); padding: 0 .06em; }
      .hw .r { color: #d6362f; }
      .hw .sm { font-size: .62em; color: #555; }
"""

BODY = r"""
        tl.set([C.barT, C.barB, C.vig], { opacity: 0 }, 0);
        const TOP = document.getElementById("root");
        const EO = "power2.out", EZ = "power2.inOut";
        FX.ab(TOP, { left: "0", top: "0", width: "1080px", height: "1920px" }, `<div class="pap"></div>`);
        const INK = "#232323";
        // ── primitives au feutre (traits tracés en direct : classe ln ; aplats : classe fl)
        const L = (d, c = INK, w = 7) => `<path class="ln" d="${d}" stroke="${c}" stroke-width="${w}" fill="none" stroke-linecap="round" stroke-linejoin="round" pathLength="1" stroke-dasharray="1"/>`;
        const O = (cx, cy, r, c = INK, w = 7) => `<circle class="ln" cx="${cx}" cy="${cy}" r="${r}" stroke="${c}" stroke-width="${w}" fill="none" pathLength="1" stroke-dasharray="1"/>`;
        const FL = (inner) => `<g class="fl">${inner}</g>`;
        const T = (x, y, s, txt, c = INK, a = "middle") => `<text class="fl" x="${x}" y="${y}" font-family="Caveat" font-weight="700" font-size="${s}" fill="${c}" text-anchor="${a}">${txt}</text>`;
        const face = (x, y, s, m = "smile") => {
          const e = `<circle class="fl" cx="${x - 12 * s}" cy="${y - 6 * s}" r="${4.5 * s}" fill="${INK}"/><circle class="fl" cx="${x + 12 * s}" cy="${y - 6 * s}" r="${4.5 * s}" fill="${INK}"/>`;
          const mo = { smile: `M${x - 13 * s} ${y + 10 * s} Q${x} ${y + 22 * s} ${x + 13 * s} ${y + 10 * s}`, frown: `M${x - 12 * s} ${y + 18 * s} Q${x} ${y + 8 * s} ${x + 12 * s} ${y + 18 * s}`, flat: `M${x - 11 * s} ${y + 14 * s} L${x + 11 * s} ${y + 14 * s}`, o: `M${x - 6 * s} ${y + 14 * s} a${6 * s} ${6 * s} 0 1 0 ${12 * s} 0 a${6 * s} ${6 * s} 0 1 0 ${-12 * s} 0` }[m];
          return e + L(mo, INK, 5 * Math.max(0.8, s));
        };
        const person = (cx, by, s = 1, pose = "down", m = "smile", c = INK) => {
          const hy = by - 250 * s, sh = by - 190 * s, hip = by - 90 * s;
          const arms = {
            down: `M${cx} ${sh} L${cx - 55 * s} ${by - 115 * s} M${cx} ${sh} L${cx + 55 * s} ${by - 115 * s}`,
            up: `M${cx} ${sh} L${cx - 70 * s} ${by - 300 * s} M${cx} ${sh} L${cx + 70 * s} ${by - 300 * s}`,
            phone: `M${cx} ${sh} L${cx - 55 * s} ${by - 115 * s} M${cx} ${sh} L${cx + 50 * s} ${by - 205 * s} L${cx + 30 * s} ${by - 245 * s}`,
            give: `M${cx} ${sh} L${cx - 55 * s} ${by - 115 * s} M${cx} ${sh} L${cx + 95 * s} ${by - 185 * s}`,
            wave: `M${cx} ${sh} L${cx - 55 * s} ${by - 115 * s} M${cx} ${sh} L${cx + 60 * s} ${by - 250 * s} M${cx + 50 * s} ${by - 280 * s} q10 -10 20 0 M${cx + 78 * s} ${by - 262 * s} q10 -10 20 0`,
          }[pose];
          return O(cx, hy, 36 * s, c) + face(cx, hy, s, m) + L(`M${cx} ${hy + 36 * s} L${cx} ${hip}`, c) + L(arms, c) + L(`M${cx} ${hip} L${cx - 42 * s} ${by} M${cx} ${hip} L${cx + 42 * s} ${by}`, c);
        };
        const house = (x, y, w, h, c = INK) => L(`M${x} ${y} L${x} ${y + h} L${x + w} ${y + h} L${x + w} ${y}`, c) + L(`M${x - 30} ${y + 10} L${x + w / 2} ${y - h * 0.62} L${x + w + 30} ${y + 10}`, c) + L(`M${x + w * 0.18} ${y + h} L${x + w * 0.18} ${y + h * 0.45} L${x + w * 0.4} ${y + h * 0.45} L${x + w * 0.4} ${y + h}`, c) + L(`M${x + w * 0.58} ${y + h * 0.22} h${w * 0.26} v${h * 0.26} h${-w * 0.26} Z M${x + w * 0.71} ${y + h * 0.22} v${h * 0.26} M${x + w * 0.58} ${y + h * 0.35} h${w * 0.26}`, c, 6);
        const phone = (x, y, w = 150, h = 270, badge = "") => L(`M${x + 22} ${y} h${w - 44} q22 0 22 22 v${h - 44} q0 22 -22 22 h${-(w - 44)} q-22 0 -22 -22 v${-(h - 44)} q0 -22 22 -22 Z`) + L(`M${x + w * 0.38} ${y + 18} h${w * 0.24}`, INK, 5) + (badge ? FL(`<circle cx="${x + w - 6}" cy="${y + 6}" r="34" fill="#e5484d"/>`) + T(x + w - 6, y + 22, 48, badge, "#fff") : "");
        const bubble = (x, y, w, h, txt, s = 56, tail = "left") => L(`M${x + 30} ${y} h${w - 60} q30 0 30 30 v${h - 60} q0 30 -30 30 h${tail === "left" ? -(w - 120) : -30} l${tail === "left" ? -40 : 10} 40 l${tail === "left" ? 0 : -10} -40 h${tail === "left" ? -50 : -(w - 90)} q-30 0 -30 -30 v${-(h - 60)} q0 -30 30 -30 Z`) + T(x + w / 2, y + h / 2 + s * 0.33, s, txt);
        const heart = (x, y, s, c = "#e5484d", fill = true) => (fill ? FL(`<path d="M${x} ${y + 30 * s} C${x - 60 * s} ${y - 20 * s} ${x - 30 * s} ${y - 70 * s} ${x} ${y - 35 * s} C${x + 30 * s} ${y - 70 * s} ${x + 60 * s} ${y - 20 * s} ${x} ${y + 30 * s} Z" fill="${c}" opacity=".85"/>`) : "") + L(`M${x} ${y + 30 * s} C${x - 60 * s} ${y - 20 * s} ${x - 30 * s} ${y - 70 * s} ${x} ${y - 35 * s} C${x + 30 * s} ${y - 70 * s} ${x + 60 * s} ${y - 20 * s} ${x} ${y + 30 * s} Z`, c, 6);
        const moon = (x, y, r) => FL(`<circle cx="${x}" cy="${y}" r="${r}" fill="#ffe9a3"/><circle cx="${x - r * 0.3}" cy="${y - r * 0.2}" r="${r * 0.16}" fill="#f2d27a"/><circle cx="${x + r * 0.28}" cy="${y + r * 0.3}" r="${r * 0.12}" fill="#f2d27a"/>`) + O(x, y, r);
        const star = (x, y) => L(`M${x - 14} ${y} L${x + 14} ${y} M${x} ${y - 14} L${x} ${y + 14}`, INK, 5);
        const sun = (x, y, r) => FL(`<circle cx="${x}" cy="${y}" r="${r}" fill="#ffd95a"/>`) + O(x, y, r) + L(Array.from({ length: 8 }, (_, i) => { const a = (i * Math.PI) / 4; return `M${x + Math.cos(a) * (r + 18)} ${y + Math.sin(a) * (r + 18)} L${x + Math.cos(a) * (r + 48)} ${y + Math.sin(a) * (r + 48)}`; }).join(" "), INK, 6);
        const clock = (x, y, r, hA, mA) => O(x, y, r) + L(`M${x} ${y} L${x + Math.sin(hA) * r * 0.5} ${y - Math.cos(hA) * r * 0.5} M${x} ${y} L${x + Math.sin(mA) * r * 0.78} ${y - Math.cos(mA) * r * 0.78}`, INK, 6);
        const car = (x, y, w = 420) => L(`M${x} ${y + 100} L${x} ${y + 55} Q${x + 10} ${y + 40} ${x + 60} ${y + 36} L${x + 110} ${y} L${x + w - 150} ${y} L${x + w - 90} ${y + 36} Q${x + w - 10} ${y + 44} ${x + w} ${y + 70} L${x + w} ${y + 100} Z`) + L(`M${x + 125} ${y + 12} L${x + 95} ${y + 36} L${x + w / 2 - 10} ${y + 36} L${x + w / 2 - 10} ${y + 12} Z M${x + w / 2 + 10} ${y + 12} L${x + w / 2 + 10} ${y + 36} L${x + w - 105} ${y + 36} L${x + w - 150} ${y + 12} Z`, INK, 5) + O(x + 95, y + 102, 34) + O(x + w - 95, y + 102, 34);
        const papers = (x, y) => [0, 1, 2, 3, 4, 5].map((i) => L(`M${x + i * 6} ${y - i * 34} h300 v26 h-300 Z`)).join("") + L(`M${x + 40} ${y - 220} h210 M${x + 40} ${y - 250} h170 M${x + 40} ${y - 280} h200`, "#777", 5) + L(`M${x + 30} ${y - 210} h250 v-110 h-250 Z`);
        const keys = (x, y) => O(x, y, 26) + L(`M${x + 24} ${y + 10} L${x + 110} ${y + 50} M${x + 80} ${y + 36} l-10 22 M${x + 98} ${y + 44} l-10 22`, "#b88a14", 7) + O(x - 10, y + 40, 18, "#b88a14", 6);

        // ── une scène : dessin tracé en direct + texte manuscrit mot à mot
        const scene = (t0, t1, text, svg, o = {}) => {
          const g = FX.ab(TOP, { left: "0", top: "0", width: "1080px", height: "1920px" }, `<svg viewBox="0 0 1080 1920" width="1080" height="1920" style="position:absolute;inset:0"><g transform="translate(540 1230) scale(1.22) translate(-540 -1150)">${svg}</g></svg>`);
          const hw = FX.ab(g, { top: (o.top || 230) + "px", fontSize: (o.fs || 96) + "px" }, text);
          hw.classList.add("hw");
          tl.set(g, { opacity: 0 }, 0); tl.set(g, { opacity: 1 }, t0);
          // mots, un par un
          const words = [];
          K.$$(".hw > *", g).forEach((n) => words.push(n));
          words.forEach((w, i) => { tl.set(w, { opacity: 0 }, 0); tl.fromTo(w, { opacity: 0, y: 10 }, { opacity: 1, y: 0, duration: 0.2, ease: EO, immediateRender: false }, t0 + 0.15 + i * (o.ws || 0.11)); });
          // traits
          const D = o.dd || 1.8, t = t0 + (o.dt ?? 0.5), lns = K.$$(".ln", g);
          lns.forEach((l, i) => { tl.set(l, { strokeDashoffset: 1 }, 0); tl.to(l, { strokeDashoffset: 0, duration: Math.max(0.18, (D / lns.length) * 1.7), ease: "power1.inOut" }, t + (i * D) / lns.length); });
          K.$$(".fl", g).forEach((f) => { tl.set(f, { opacity: 0 }, 0); tl.to(f, { opacity: 1, duration: 0.35, ease: EO }, t + D * 0.85); });
          K.sfx(t, "marker", 0.22, 0, { d: D + 0.2 });
          if (t1 != null) tl.to(g, { opacity: 0, x: -50, duration: 0.35, ease: "power2.in" }, t1 - 0.35);
          return g;
        };
        // texte : chaque mot devient un <span class="wd"> (groupes [..] = surligné, {..} = rouge)
        const W = (s) => s.split("|").map((line) => line.trim().split(" ").map((w) => {
          if (/^\[.*\]$/.test(w)) return `<span class="wd k">${w.slice(1, -1).replace(/_/g, " ")}</span>`;
          if (/^\{.*\}$/.test(w)) return `<span class="wd r">${w.slice(1, -1).replace(/_/g, " ")}</span>`;
          return `<span class="wd">${w.replace(/_/g, " ")}</span>`;
        }).join("")).join("<br>");

        // ── 0 · titre
        scene(0, 5, `<span class="wd sm">Draw my life :</span><br>` + W("[conseiller_immo] ✏️"), house(250, 1010, 330, 280) + person(780, 1420, 1.1, "wave") + sun(860, 760, 60) + L("M120 1430 H960", INK, 6), { fs: 120, top: 280, dd: 2.2 });
        // ── 1 · le réveil
        scene(5, 9.5, W("6h45._Le_réveil_sonne. | {Déjà_3_messages.}"), L("M160 1300 h600 v120 M160 1300 v120 M160 1260 v160") + L("M260 1300 q120 -70 260 -10 q120 50 240 10", INK, 6) + O(250, 1225, 42) + face(250, 1225, 1.1, "o") + phone(770, 900, 150, 270, "3") + T(380, 1150, 64, "Zzz…", "#888"), { dd: 1.6 });
        // ── 2 · le café
        scene(9.5, 14, W("8h._Le_café_refroidit. | {Un_vendeur_appelle.}"), L("M220 1190 L245 1380 L375 1380 L400 1190 Z M400 1240 q60 0 60 50 q0 50 -70 50") + T(310, 1150, 56, "brr…", "#3a7bd5") + person(720, 1430, 1.1, "phone", "flat") + phone(735, 1135, 50, 90) + bubble(470, 820, 300, 150, "Allô ?", 64), { dd: 1.6 });
        // ── 3 · l'estimation
        scene(14, 19, W("10h._Estimation. | Mme_Dupuis_te_raconte | [40_ans_de_souvenirs.]"), house(140, 1050, 300, 260) + heart(290, 1120, 0.45) + person(640, 1440, 1.0, "down", "smile") + person(880, 1440, 0.95, "down", "smile") + L("M915 1250 L960 1440", "#8a5a2b", 6) + L("M560 1460 H980", INK, 5), { top: 230, dd: 2.0 });
        // ── 4 · le déjeuner
        scene(19, 23.5, W("12h30._Le_déjeuner_? | {Dans_la_voiture.}"), car(300, 1180, 480) + L("M430 1205 L490 1205", INK, 5) + bubble(160, 860, 330, 160, "🥪 vite !", 60, "right") + clock(840, 900, 80, 0.2, 3.1) + L("M120 1320 H980", INK, 5), { dd: 1.7 });
        // ── 5 · la visite
        scene(23.5, 28, W("14h._Visite._Ils_adorent. | {Ils_ne_rappelleront_jamais.}"), person(300, 1430, 1.0, "up", "smile") + person(480, 1430, 0.95, "up", "smile") + heart(260, 1060, 0.35) + heart(520, 1040, 0.3) + phone(760, 1050, 160, 290) + T(840, 1220, 80, "…", "#888"), { dd: 1.8 });
        // ── 6 · le notaire
        scene(28, 32.5, W("17h._Le_notaire_veut | {47_pages} _pour_hier."), papers(380, 1420) + O(530, 980, 42) + face(530, 980, 1.1, "frown") + L("M590 950 q10 20 0 30", "#3a7bd5", 5) + T(820, 1150, 64, "47 p.", "#d6362f"), { dd: 1.9 });
        // ── 7 · le retour
        scene(32.5, 37, W("19h30._Tu_rentres. | Ton_téléphone, | {lui,_ne_rentre_jamais.}"), house(180, 1140, 320, 260) + moon(820, 860, 70) + star(650, 820) + star(940, 1010) + phone(700, 1120, 160, 290, "12") + L("M100 1400 H560", INK, 5), { top: 220, dd: 1.8 });
        // ── 8 · 22h47
        scene(37, 41.5, W("22h47 : | « La_maison_est_toujours | dispo_? »"), L("M160 1340 h560 v100 M160 1340 v100 M160 1300 v140") + O(250, 1265, 42) + face(250, 1265, 1.1, "o") + L("M270 1340 q140 -50 300 -5 q80 25 150 5", INK, 6) + phone(800, 1080, 140, 250, "1") + moon(860, 840, 55), { dd: 1.7 });
        // ── 9 · les clés
        scene(41.5, 46.5, W("Et_puis_un_jour… | tu_tends | [les_clés.]"), person(250, 1450, 1.0, "give", "smile") + keys(380, 1240) + person(600, 1450, 1.0, "up", "smile") + person(780, 1450, 0.95, "up", "smile") + person(690, 1450, 0.6, "up", "smile") + house(720, 880, 220, 180) + L("M140 1470 H960", INK, 5), { top: 230, dd: 2.2 });
        // ── 10 · pourquoi
        scene(46.5, 51.5, W("Une_famille_pleure_de_joie. | Et_tu_te_souviens | [pourquoi_tu_fais_ce_métier.]"), heart(540, 1230, 3.4) + house(450, 1130, 180, 150, "#fff"), { top: 210, fs: 88, dd: 2.0 });
        // ── 11 · respect
        scene(51.5, null, W("À_tous_les_conseillers_immo_: | [respect.] _🫡") + `<div class="wd" style="display:block;margin-top:40px;font-size:.62em;color:#444">Tague un conseiller<br>qui vit ça chaque jour 👇</div>`, person(380, 1500, 1.0, "wave", "smile") + person(560, 1500, 1.0, "up", "smile") + person(740, 1500, 1.0, "wave", "smile") + L("M200 1520 H880", INK, 5), { top: 260, fs: 92, dd: 1.8 });
        const sig = FX.ab(TOP, { left: "0", right: "0", top: "1745px", textAlign: "center", zIndex: 30 }, `<div style="display:inline-flex;align-items:center;gap:14px;font-family:Inter,sans-serif;font-size:26px;color:#777"><span>avec ❤️ par</span><img src="assets/img/limo-logo-ad.png" alt="LIMO" style="height:44px" /><span>· le bras droit du conseiller immo</span></div>`);
        tl.set(sig, { opacity: 0 }, 0); tl.to(sig, { opacity: 1, duration: 0.6, ease: EO }, 54.0);
        window.__TE = 56.5;
"""

if __name__ == "__main__":
    html = SHELL.format(title="Draw my life : conseiller immo", faces=FACES, css=(CSS + CSS_D).strip("\n"), body=(COMMON + BODY).strip("\n"), dur=DUR, name=NAME)
    (HERE.parent / "reels" / f"{NAME}.html").write_text(html, encoding="utf-8")
    print("reels/" + NAME + ".html")
