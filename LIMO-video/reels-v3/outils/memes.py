"""Série « C'est tellement moi » : 6 mèmes courts (12–15 s) racontés à la 1re personne par un conseiller immobilier.
Chaque film : la situation vécue (faux SMS réalistes, plans réels) → « Moi : » (réaction) → « Depuis LIMO : » (la solution
concrète dans l'appli) → chute. Style naturel (textes au style Instagram), sans voix ni musique : seulement les bruitages
de notification. Fin courte : logo, essai gratuit 14 jours, lien en bio. Données affichées = exemples fictifs.

Usage : python3 outils/memes.py   (réécrit reels/meme-*.html)
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

CSS_M = """
      .ig { display: inline; padding: 6px 18px; line-height: 1.62; border-radius: 12px; background: rgba(0,0,0,.62); color: #fff; font-family: Inter, sans-serif; font-weight: 600; font-size: 52px; -webkit-box-decoration-break: clone; box-decoration-break: clone; }
      .ig.w { background: #fff; color: #111; }
      .chat { position: absolute; inset: 0; background: #ffffff; font-family: Inter, sans-serif; }
      .chat .hd { position: absolute; left: 0; right: 0; top: 0; height: 330px; background: #f6f6f8; border-bottom: 1px solid #e3e3e8; display: flex; flex-direction: column; align-items: center; justify-content: flex-end; padding-bottom: 26px; }
      .chat .av { width: 120px; height: 120px; border-radius: 50%; background: linear-gradient(160deg,#b7bcc8,#8e93a3); color: #fff; display: flex; align-items: center; justify-content: center; font-size: 48px; font-weight: 600; }
      .chat .nm { margin-top: 12px; font-size: 34px; font-weight: 600; color: #111; }
      .chat .sb { font-size: 25px; color: #8a8a90; }
      .chat .tm { text-align: center; margin: 30px 0 16px; font-size: 25px; color: #8a8a90; }
      .chat .lst { position: absolute; left: 40px; right: 40px; top: 360px; display: flex; flex-direction: column; gap: 14px; }
      .bub { max-width: 78%; padding: 22px 30px; border-radius: 40px; font-size: 40px; line-height: 1.32; }
      .bub.in { align-self: flex-start; background: #e9e9eb; color: #111; border-bottom-left-radius: 12px; }
      .bub.out { align-self: flex-end; background: #0a84ff; color: #fff; border-bottom-right-radius: 12px; }
      .dots { align-self: flex-start; display: flex; gap: 10px; padding: 26px 30px; border-radius: 40px; background: #e9e9eb; }
      .dots i { width: 16px; height: 16px; border-radius: 50%; background: #9a9aa0; display: block; }
      .lim { position: absolute; inset: 0; background: radial-gradient(ellipse at 50% 30%, #ffffff 0%, #f1eefc 55%, #e7e1fa 100%); }
      .lim .box { position: absolute; left: 64px; top: 0; width: 560px; transform-origin: 0 0; transform: scale(1.7); font-family: Inter, sans-serif; color: #1b1f4b; }
      .lim .lg { display: flex; align-items: center; gap: 12px; margin-bottom: 14px; font-size: 20px; font-weight: 600; color: #6b4fe0; }
      .lim .lg img { height: 40px; }
      .end { position: absolute; inset: 0; background: radial-gradient(ellipse at 50% 35%, #ffffff 0%, #f1eefc 60%, #e7e1fa 100%); text-align: center; font-family: Inter, sans-serif; color: #1b1f4b; }
"""

HELP = SH4 + r"""
        const TOP = document.getElementById("root");
        tl.set([C.barT, C.barB], { opacity: 0 }, 0);
        const EO = "power2.out", EZ = "power2.inOut";
        const scn = (t0, t1, html = "", css = {}) => {
          const l = FX.ab(TOP, Object.assign({ left: "0", top: "0", width: "1080px", height: "1920px", overflow: "hidden" }, css), html);
          tl.set(l, { opacity: 0 }, 0); tl.set(l, { opacity: 1 }, t0); tl.set(l, { opacity: 0 }, t1);
          return l;
        };
        const push = (id, t0, t1, a = 1.0, b = 1.06) => tl.fromTo(document.getElementById(id), { scale: a }, { scale: b, duration: t1 - t0, ease: "none" }, t0);
        const say = (t0, t1, html, top = 200, w = false) => {
          const e = FX.ab(TOP, { left: "60px", right: "60px", top: top + "px", textAlign: "center", zIndex: 34 }, `<span class="ig${w ? " w" : ""}">${html}</span>`);
          tl.set(e, { opacity: 0 }, 0); tl.set(e, { opacity: 1 }, t0); tl.set(e, { opacity: 0 }, t1);
          K.sfx(t0, "pop", 0.05, 0, { f: 800 });
          return e;
        };
        // écran de messages façon iPhone ; msgs = [[t, texte, "in"|"out"]]
        const chat = (t0, t1, who, ini, sub, time, msgs) => {
          const l = scn(t0, t1, `<div class="chat"><div class="hd"><div class="av">${ini}</div><div class="nm">${who}</div><div class="sb">${sub}</div></div><div class="lst"><div class="tm">${time}</div></div></div>`);
          const lst = K.$(".lst", l);
          msgs.forEach(([t, txt, side]) => {
            if (side === "in") {
              const d = K.h("div", "dots", "<i></i><i></i><i></i>", lst);
              tl.set(d, { display: "none" }, 0); tl.set(d, { display: "flex" }, t - 0.9); tl.set(d, { display: "none" }, t);
              K.$$("i", d).forEach((i, k) => tl.fromTo(i, { opacity: 0.3 }, { opacity: 1, duration: 0.25, yoyo: true, repeat: 3, ease: "sine.inOut", immediateRender: false }, t - 0.9 + k * 0.12));
            }
            const b = K.h("div", "bub " + side, txt, lst);
            tl.set(b, { display: "none" }, 0); tl.set(b, { display: "block" }, t);
            tl.fromTo(b, { opacity: 0, y: 20, scale: 0.96 }, { opacity: 1, y: 0, scale: 1, duration: 0.25, ease: EO, immediateRender: false }, t);
            K.sfx(t, side === "in" ? "receive" : "send", 0.3);
          });
          return l;
        };
        // écran LIMO (composants de l'appli, agrandis ×1,5) ; cartes qui apparaissent une à une
        const limo = (t0, t1, top, parts) => {
          const l = scn(t0, t1, `<div class="lim"><div class="box" style="top:${top}px"><div class="lg"><img src="assets/img/limo-logo-ad.png" alt="LIMO" /></div>${parts.map((p) => `<div class="pt" style="margin-bottom:12px">${p[1]}</div>`).join("")}</div></div>`);
          K.$$(".pt", l).forEach((e, i) => { tl.set(e, { opacity: 0 }, 0); tl.fromTo(e, { opacity: 0, y: 16 }, { opacity: 1, y: 0, duration: 0.3, ease: EO, immediateRender: false }, parts[i][0]); K.sfx(parts[i][0], i ? "tick" : "success", i ? 0.08 : 0.18, 0, { f: 2200 }); });
          return l;
        };
        const out = (txt) => `<div style="display:flex;justify-content:flex-end"><div class="bub out" style="font-size:22px;padding:14px 18px;border-radius:24px;border-bottom-right-radius:8px;max-width:88%">${txt}</div></div>`;
        const okc = (txt, c = "t") => `<span class="a-tag ${c}">${K.icon("check")}${txt}</span>`;
        // fin courte
        const endc = (t0) => {
          const l = scn(t0, 99, `<div class="end"><div style="margin-top:560px"><img src="assets/img/limo-logo-ad.png" alt="LIMO" style="height:150px" /></div><div style="margin-top:26px;font-family:Montserrat,sans-serif;font-weight:700;font-size:44px">Le bras droit du conseiller immo.</div><div style="margin-top:60px"><span style="display:inline-block;padding:28px 54px;border-radius:999px;background:#6b4fe0;color:#fff;font-family:Montserrat,sans-serif;font-weight:800;font-size:46px">Essai gratuit 14 jours</span></div><div style="margin-top:26px;font-size:34px;color:#4f5378">Sans engagement · lien en bio</div></div>`);
          tl.fromTo(K.$(".end", l), { opacity: 0 }, { opacity: 1, duration: 0.3, ease: EO, immediateRender: false }, t0);
          const M = N.mascot({ left: "440px", top: "1340px", width: "200px" }, { expr: "happy" });
          TOP.appendChild(M.el); M.el.style.zIndex = "35";
          tl.set(M.el, { opacity: 0 }, 0); tl.to(M.el, { opacity: 1, duration: 0.3 }, t0 + 0.3); M.wave(t0 + 0.6); M.expr("wink", t0 + 1.6, false);
          K.sfx(t0, "whoosh", 0.12, 0, { d: 0.3, f0: 400, f1: 2400, pk: 0.4 });
        };
"""

FILMS = {}

# 1 · le SMS de 22h47
FILMS["meme-01-le-sms-de-22h47"] = (14.6, V("v1", "ugc-selfie", 6.6, 2.0, 1, 3.0), r"""
        scn(0, 3.0, `<img src="assets/img/bien-mas-lavande.jpg" alt="" style="position:absolute;left:-200px;top:0;height:1920px;filter:blur(18px) brightness(.45)" />`);
        say(0.2, 3.0, "POV : 22h47.<br>T’es enfin posé en famille. 🍝", 760);
        K.sfx(1.6, "buzz", 0.4, 0, { d: 0.5 }); K.sfx(2.2, "buzz", 0.4, 0, { d: 0.5 });
        chat(3.0, 6.6, "M. Garnier", "MG", "Acquéreur", "Aujourd’hui 22:47", [[3.6, "Bonsoir ! La maison de Vignols est toujours dispo ?", "in"], [5.2, "On peut visiter demain 7h30 ? On part au boulot après 😅", "in"]]);
        scn(6.6, 8.6); push("v1", 6.6, 8.6);
        say(6.7, 8.6, "Moi, la fourchette à la main :", 230);
        limo(8.6, 12.3, 440, [[8.8, `<div class="sub" style="font-family:Montserrat,sans-serif;font-weight:800;font-size:20px;letter-spacing:.1em;color:#6b4fe0">DEPUIS LIMO :</div>`], [9.2, out("Bonsoir M. Garnier ! Oui, toujours disponible 😊 Je vous propose samedi 10h ou lundi 18h. Belle soirée !")], [10.1, okc("Réponse prête · envoyée en 1 clic")]]);
        say(10.8, 12.3, "Et moi, je finis mon dessert. 🍰", 1420, true);
        endc(12.3);
""")

# 2 · « rappelez-moi en mars »
FILMS["meme-02-rappelez-moi-en-mars"] = (15.0, V("v1", "agent-deborde", 7.2, 2.2, 1), r"""
        chat(0, 3.6, "Mme Leroy", "ML", "Vendeuse · Allassac", "12 octobre", [[0.7, "On réfléchit encore avec mon mari…", "in"], [2.1, "Rappelez-moi en mars 🙂", "in"]]);
        say(0.1, 3.6, "Octobre :", 1500, true);
        const p = scn(3.6, 7.2, `<img src="assets/img/correze-ruelle.jpg" alt="" style="position:absolute;left:0;top:0;height:1920px" />`);
        tl.fromTo(K.$("img", p), { x: -1150 }, { x: -1350, duration: 3.6, ease: "none" }, 3.6);
        say(3.7, 7.2, "Mars :", 230);
        say(4.6, 7.2, "Panneau d’une autre agence<br>sur sa maison. 🙃", 1380);
        scn(7.2, 9.4); push("v1", 7.2, 9.4);
        say(7.3, 9.4, "Moi, qui avais noté ça…<br>sur un post-it. 🟨", 230);
        limo(9.4, 12.7, 470, [[9.6, `<div class="a-card a-row" style="padding:18px 20px"><span class="a-ic o">${K.icon("bell")}</span><span class="tx"><b>1er mars · Rappeler Mme Leroy</b><small>Veut vendre au printemps · Allassac</small></span></div>`], [10.3, out("Bonjour Madame Leroy, le printemps arrive 🌷 Avez-vous avancé sur votre projet de vente ?")], [11.1, okc("Rappel + message prêts, tout seuls")]]);
        say(9.5, 12.7, "Depuis LIMO :", 230);
        endc(12.7);
""")

# 3 · « ma maison vaut plus »
FILMS["meme-03-ma-maison-vaut-plus"] = (14.6, V("v1", "ugc-selfie", 5.4, 2.2, 1, 3.4), r"""
        chat(0, 5.4, "M. Bernard", "MB", "Vendeur · Brive", "Aujourd’hui 18:05", [[0.6, "J’ai vu sur un site que ma maison vaut 320 000 € 🧐", "in"], [2.4, "Mon voisin a vendu 300 000 la sienne et elle est moins bien", "in"], [4.0, "Donc on met 340 000 ?", "in"]]);
        scn(5.4, 7.6); push("v1", 5.4, 7.6);
        say(5.5, 7.6, "Moi, après 3 h<br>d’étude de marché :", 230);
        limo(7.6, 12.3, 440, [[7.8, `<div class="a-card" style="padding:20px 22px"><small style="font-size:18px;color:#6e6e80">Maison · Brive · 110 m²</small><div style="margin-top:4px;font-family:Montserrat,sans-serif;font-weight:800;font-size:40px;color:#6b4fe0">248 – 262 k€</div></div>`], [8.6, A.row("bank", "t", "3 ventes DVF à moins de 500 m", "Prix réels, datés, vérifiables")], [9.3, A.row("pin", "v", "Cadastre + DPE vérifiés", "Données officielles")], [10.0, okc("Envoyé au vendeur, preuves à l’appui")]]);
        say(7.7, 12.3, "Depuis LIMO :", 230);
        say(10.7, 12.3, "Les chiffres parlent. Pas moi. 😌", 1500, true);
        endc(12.3);
""")

# 4 · les frais km le 30
FILMS["meme-04-frais-km-le-30"] = (13.6, V("v1", "agent-deborde", 0, 3.2, 1) + V("v2", "agent-voiture-grade", 3.2, 2.8, 2), r"""
        scn(0, 3.2); push("v1", 0, 3.2);
        say(0.2, 3.2, "POV : le 30 du mois.<br>Ton comptable veut<br>tes frais km. 📎", 230);
        scn(3.2, 6.0); push("v2", 3.2, 6.0);
        say(3.3, 6.0, "Moi : « Le 4… j’étais à Allassac ?<br>Ou à Voutezac ? » 🤔", 230);
        const l = limo(6.0, 11.3, 420, [[6.2, `<div class="a-card" style="padding:22px;text-align:center"><small style="font-size:18px;color:#6e6e80">Octobre</small><div class="km" style="font-family:Montserrat,sans-serif;font-weight:800;font-size:54px">0 km</div></div>`], [6.9, A.row("car", "v", "Brive → Allassac", "4 oct. · visite · 18 km", "9:40")], [7.4, A.row("car", "v", "Allassac → Voutezac", "4 oct. · estimation · 11 km", "14:10")], [8.6, okc("Export prêt pour le comptable")]]);
        K.count(K.$(".km", l), 1240, 6.4, 1.4, (v) => { const n = Math.round(v); return (n >= 1000 ? Math.floor(n / 1000) + " " + String(n % 1000).padStart(3, "0") : n) + " km"; }, { ticks: 10 });
        say(6.1, 11.3, "Depuis LIMO :", 200);
        say(9.4, 11.3, "Noté au fil de l’eau.<br>Le 30, je dors. 😴", 1450, true);
        endc(11.3);
""")

# 5 · le compromis du dimanche soir
FILMS["meme-05-le-compromis-du-dimanche"] = (14.6, V("v1", "agent-deborde", 3.4, 2.2, 1, 1.6), r"""
        const d = scn(0, 3.4, `<div style="position:absolute;inset:0;background:linear-gradient(180deg,#0e1030,#1b1446)"></div>`);
        say(0.2, 3.4, "Dimanche, 21h. 🍿", 330);
        const n = FX.ab(d, { left: "60px", right: "60px", top: "760px" }, `<div style="display:flex;gap:22px;align-items:center;padding:26px 30px;border-radius:34px;background:rgba(255,255,255,.92);font-family:Inter,sans-serif;color:#111"><span style="flex:none;width:84px;height:84px;border-radius:20px;background:#0a84ff;color:#fff;display:flex;align-items:center;justify-content:center;font-size:40px">✉️</span><span><b style="display:block;font-size:30px">Me Faure · Notaire</b><span style="font-size:30px">Compromis Vignols.pdf (47 pages) — retour demain 9h svp</span></span></div>`);
        tl.set(n, { opacity: 0 }, 0); tl.fromTo(n, { opacity: 0, y: -40 }, { opacity: 1, y: 0, duration: 0.3, ease: EO, immediateRender: false }, 1.2); K.sfx(1.2, "notif", 0.4);
        scn(3.4, 5.6); push("v1", 3.4, 5.6);
        say(3.5, 5.6, "Moi, qui avais prévu un film :", 230);
        limo(5.6, 12.3, 440, [[5.8, `<div class="a-card" style="display:flex;align-items:center;gap:14px;padding:16px 18px"><span class="a-ic r">${K.icon("file")}</span><span><b style="font-size:21px">Compromis Vignols.pdf</b><small style="display:block;font-size:17px;color:#6e6e80">47 pages · analysé</small></span></div>`], [6.6, A.row("euro", "t", "Prix : 245 000 €", "Conforme au mandat")], [7.2, A.row("clock", "v", "Signature : 14 novembre", "Chez Me Faure")], [7.8, A.row("alert", "o", "2 points à vérifier", "Condition de prêt · servitude")], [8.6, okc("Résumé prêt pour demain 9h")]]);
        say(5.7, 12.3, "Depuis LIMO :", 200);
        say(10.4, 12.3, "Et le film, je le regarde. 🍿", 1500, true);
        endc(12.3);
""")

# 6 · « vous avez d'autres biens comme ça ? »
FILMS["meme-06-dautres-biens-comme-ca"] = (14.6, V("v1", "maison-contemporaine", 0, 3.4, 1) + V("v2", "ugc-selfie", 5.8, 2.2, 2, 3.2), r"""
        scn(0, 3.4); push("v1", 0, 3.4, 1.0, 1.08);
        say(0.2, 3.4, "En pleine visite,<br>l’acquéreur me sort :", 230);
        const q = scn(3.4, 5.8, `<div style="position:absolute;inset:0;background:#111"></div>`);
        say(3.5, 5.8, "« Vous auriez d’autres biens<br>un peu comme ça…<br>mais avec un plus grand jardin ? »", 760, true);
        scn(5.8, 8.0); push("v2", 5.8, 8.0);
        say(5.9, 8.0, "Moi, qui fouille dans ma tête<br>mes 47 mandats :", 230);
        limo(8.0, 12.3, 440, [[8.2, `<div class="a-h2" style="margin:0 0 6px">3 biens correspondants</div>`], [8.6, A.row("home", "v", "Longère · Voutezac", "Jardin 2 400 m²", "", `<span class="a-tag t">92 %</span>`)], [9.0, A.row("home", "v", "Maison · Allassac", "Jardin 1 800 m²", "", `<span class="a-tag t">88 %</span>`)], [9.4, A.row("home", "v", "Maison · Vignols", "Jardin 1 500 m²", "", `<span class="a-tag t">81 %</span>`)], [10.1, okc("Envoyés à l’acquéreur avant la fin de la visite")]]);
        say(8.1, 12.3, "Depuis LIMO :", 200);
        endc(12.3);
""")

if __name__ == "__main__":
    for name, (dur, pre, body) in FILMS.items():
        html = SHELL.format(title=name, faces=FACES, css=(CSS + CSS_M).strip("\n"), body=(COMMON + HELP + body).strip("\n"), dur=dur, name=name)
        html = html.replace('      <section id="s-main"', pre + '      <section id="s-main"', 1)
        (HERE.parent / "reels" / f"{name}.html").write_text(html, encoding="utf-8")
        print("reels/" + name + ".html")
