"""Vidéo « site internet » V2, 16:9 (1920×1080) : tout ce que LIMO fait, plus intuitive (retours de Thomy sur la V1 :
« le robot ne bouge pas, il cache du texte, pas assez intuitif »).
- Chaque chapitre : « Avant : » le problème, puis « Avec LIMO » en 3 étapes numérotées qui s'allument une à une.
- À chaque étape, l'élément correspondant de l'application est mis en lumière (le reste s'assombrit).
- La mascotte a sa propre zone (entre le texte et le téléphone) : elle se déplace à la hauteur de l'étape en cours,
  se penche vers le téléphone, change d'expression ; elle ne recouvre jamais de texte.
Sans voix ni musique. Fonctions = liste officielle de l'appli. Données affichées = exemples fictifs.

Usage : python3 outils/site2.py   (réécrit reels/site-02-tout-ce-que-fait-limo.html)
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from cine import FACES  # noqa: E402
import importlib.util  # noqa: E402
_sp = importlib.util.spec_from_file_location("site_v1", HERE / "site.py")
_m = importlib.util.module_from_spec(_sp)
_sp.loader.exec_module(_m)
SHELL16 = _m.SHELL16

NAME = "site-02-tout-ce-que-fait-limo"
T0, CHD = 6.0, 9.5
DUR = round(T0 + 8 * CHD + 7.0 + 6.5, 2)
EXTRA = """
      .pb {{ font-family: Inter, sans-serif; font-size: 30px; color: #6e6e80; }}
      .pb b {{ color: #c0282d; font-weight: 600; }}
      .avec {{ font-family: Montserrat, sans-serif; font-weight: 800; font-size: 28px; letter-spacing: .1em; color: #6b4fe0; }}
      .st {{ display: flex; align-items: center; gap: 22px; font-family: Inter, sans-serif; font-size: 36px; line-height: 1.25; color: #1b1f4b; font-weight: 600; }}
      .st .nb {{ flex: none; width: 62px; height: 62px; border-radius: 50%; background: #6b4fe0; color: #fff; display: flex; align-items: center; justify-content: center; font-family: Montserrat, sans-serif; font-weight: 800; font-size: 30px; }}
    </style>"""

BODY = r"""
        tl.set([K.$(".n-bg", root), ...K.$$(".n-arc", root)], { opacity: 0 }, 0);
        const EZ = "power2.inOut", EO = "power2.out";
        const ab = (css, html, parent = root) => { const e = N.ab("", html, css, parent); [e, ...K.$$("*", e)].forEach((x) => ["data-layout-allow-overflow", "data-layout-allow-overlap", "data-layout-allow-occlusion"].forEach((a) => x.setAttribute(a, ""))); return e; };
        const fin = (e, t, d = 0.6, y = 24) => { tl.set(e, { opacity: 0 }, 0); tl.fromTo(e, { opacity: 0, y }, { opacity: 1, y: 0, duration: d, ease: EO, immediateRender: false }, t); };
        const fout = (e, t, d = 0.45) => tl.to(e, { opacity: 0, duration: d, ease: EZ }, t);
        const T0 = __T0, CHD = __CHD, SY = [560, 690, 820];

        // ── écrans de l'appli absents de A.S (même style)
        const PG = {
          doc: () => `<div class="a-back">${K.icon("chev")}Analyseur de dossier</div><div class="a-card" style="display:flex;align-items:center;gap:16px;padding:18px 20px;margin-bottom:14px"><span class="a-ic r">${K.icon("file")}</span><span><b style="font-size:23px">Compromis.pdf</b><small style="display:block;font-size:19px;color:#6e6e80">12 pages · déposé</small></span></div><div class="a-h2">Fiche remplie automatiquement</div>` +
            A.row("users", "v", "Vendeurs : M. et Mme T.", "Acquéreurs : Famille Lambert") + A.row("euro", "t", "Prix : 245 000 €", "Dépôt de garantie 5 %") + A.row("scale", "g", "Notaire : Me Faure", "Signature prévue le 14/11") + A.row("alert", "o", "Prêt : 60 jours", "Condition suspensive") +
            `<div class="a-h2">Messages Insta & Facebook</div>` + A.row("msg", "v", "14 messages relevés", "3 vendeurs potentiels repérés", "", `<span class="a-tag t">À rappeler</span>`),
          estim: () => `<div class="a-back">${K.icon("chev")}Estimation</div><div class="a-card" style="padding:24px 24px 26px;margin-bottom:14px"><small style="font-size:20px;color:#6e6e80">Maison · Allassac · 120 m²</small><div style="margin-top:6px;font-family:Montserrat,sans-serif;font-weight:800;font-size:46px;color:#6b4fe0">239 – 252 k€</div><div class="a-bar" style="margin-top:16px"><i class="eb" style="width:100%"></i></div></div>` +
            A.row("pin", "v", "Cadastre · 1 250 m²", "Parcelle vérifiée") + A.row("bank", "t", "3 ventes DVF comparables", "Dans un rayon de 2 km") + A.row("zap", "o", "DPE C", "Diagnostic officiel"),
          admin: () => `<div class="a-back">${K.icon("chev")}Frais kilométriques</div><div class="a-card" style="padding:24px;margin-bottom:14px;text-align:center"><small style="font-size:20px;color:#6e6e80">Octobre</small><div class="km" style="margin-top:4px;font-family:Montserrat,sans-serif;font-weight:800;font-size:64px;color:#1b1f4b">0 km</div><span class="a-tag t" style="margin-top:10px">${K.icon("check")}Prêt pour le comptable</span></div>` +
            A.row("car", "v", "Brive → Allassac", "Visite · 18 km", "9:40") + A.row("car", "v", "Allassac → Voutezac", "Estimation · 11 km", "14:10") + `<div class="a-h2">Mes artisans</div>` + A.row("wrench", "t", "Plombier à 4 km", "4,8 ★ · disponible jeudi"),
        };
        // sélection des éléments à mettre en lumière dans une page
        const pick = (pg, sel, idx) => { const l = K.$$(sel, pg); return idx ? idx.map((i) => l[i]).filter(Boolean) : l; };

        // ── chapitres : nav, kicker, titre, « avant », page, 3 étapes [texte, (page) => éléments]
        const CH = [
          ["Organise", "ORGANISER TA JOURNÉE", "Ta journée<br><em>est déjà prête.</em>", "chaque matin, tu triais tout à la main.", "home", [
            ["Tu ouvres LIMO le matin", (p) => pick(p, ".a-hello")], ["Tes 5 priorités sont déjà là", (p) => pick(p, ".a-prio")], ["Dans l’ordre, avec l’heure", (p) => pick(p, ".a-row", [0, 1, 2])]]],
          ["Se souvient", "TOUT RETENIR", "Il n’oublie <em>rien,</em><br>ni personne.", "les infos de visite restaient dans ta tête.", "dictee", [
            ["Après la visite, tu parles 30 s", (p) => pick(p, ".a-msg")], ["La fiche se met à jour seule", (p) => pick(p, ".a-row", [0, 1])], ["Il te rappelle quand agir", (p) => pick(p, ".a-row", [2])]]],
          ["Lit", "LIRE À TA PLACE", "Il lit tes dossiers<br><em>à ta place.</em>", "tu recopiais les dossiers ligne par ligne.", "doc", [
            ["Tu déposes le compromis (PDF)", (p) => pick(p, ".a-card", [0])], ["La fiche se remplit toute seule", (p) => pick(p, ".a-row", [0, 1, 2, 3])], ["Il relève aussi tes messages Insta & Facebook", (p) => pick(p, ".a-row", [4])]]],
          ["Relance", "RELANCER", "Il relance<br><em>au bon moment.</em>", "les relances passaient à la trappe.", "relances", [
            ["Il sait qui relancer", (p) => pick(p, ".a-row", [0, 1, 2, 3])], ["Les messages sont déjà écrits", (p) => pick(p, ".a-tag", [0, 1])], ["Un clic : c’est envoyé", (p) => pick(p, ".a-btn")]]],
          ["Trouve", "TROUVER DES MANDATS", "Il trouve<br><em>tes prochains vendeurs.</em>", "tu découvrais les vendeurs après les autres.", "detect", [
            ["Il surveille ton secteur", (p) => pick(p, ".a-map")], ["Il repère les vendeurs probables", (p) => pick(p, ".a-row", [0, 1])], ["Signal fort = à appeler en premier", (p) => pick(p, ".a-row .a-tag")]]],
          ["Estime", "ESTIMER", "Il estime avec<br><em>les vraies données.</em>", "des heures à chercher des comparables.", "estim", [
            ["Cadastre, ventes DVF, DPE", (p) => pick(p, ".a-row", [0, 1, 2])], ["Il calcule une fourchette juste", (p) => pick(p, ".a-card", [0])], ["Prête à montrer au vendeur", (p) => pick(p, ".a-card", [0])]]],
          ["Rédige & publie", "RÉDIGER ET PUBLIER", "Il écrit, tu n’as plus<br><em>qu’à publier.</em>", "une annonce, c’était une soirée.", "annonce", [
            ["Ton annonce, rédigée pour toi", (p) => pick(p, ".a-card")], ["Mentions légales incluses", (p) => pick(p, ".a-tag", [0])], ["Prête à publier, posts réseaux compris", (p) => pick(p, ".a-tag", [1])]]],
          ["Gère", "GÉRER L’ADMINISTRATIF", "La paperasse ?<br><em>Il s’en occupe.</em>", "les frais km, c’était le casse-tête du mois.", "admin", [
            ["Tes trajets notés tout seuls", (p) => pick(p, ".a-row", [0, 1])], ["Frais km calculés pour ton comptable", (p) => pick(p, ".a-card", [0])], ["Le bon artisan, près du bien", (p) => pick(p, ".a-row", [2])]]],
        ];
        const tc = (i) => T0 + i * CHD;
        const ts = (i, k) => tc(i) + 2.4 + k * 2.3;

        // ── le téléphone (560 px d'origine, réduit à 88 %)
        const ph = A.phone({ left: "1260px", top: "34px", width: "560px" }, { time: "8:00" });
        tl.set(ph.wrap, { scale: 0.88, transformOrigin: "0 0" }, 0);
        const pages = CH.map((c) => A.page(ph, A.S[c[4]] ? A.S[c[4]]() : PG[c[4]]()));
        A.enter(ph, T0 - 0.6, { ry: -24, ry2: -10, flatAt: 0.9 });
        CH.forEach((c, i) => { if (i) A.go(ph, pages[i - 1], pages[i], tc(i) + 0.1); });
        tl.to(ph.wrap, { opacity: 0, y: 40, duration: 0.6, ease: EZ }, tc(8) - 0.4);

        // ── mise en lumière : les autres blocs s'assombrissent, la cible s'entoure de violet
        const GLOW = "0 0 0 4px rgba(107,79,224,.6), 0 16px 34px rgba(107,79,224,.28)";
        CH.forEach((c, i) => {
          const pg = pages[i], tops = [...pg.children];
          let prev = [];
          c[5].forEach(([, get], k) => {
            const t = ts(i, k), tg = get(pg);
            prev.forEach((e) => tl.to(e, { scale: 1, boxShadow: e.__bs, duration: 0.3, ease: EZ }, t - 0.05));
            tops.forEach((top) => tl.to(top, { opacity: tg.some((e) => top === e || top.contains(e)) ? 1 : 0.28, duration: 0.4, ease: EZ }, t));
            tg.forEach((e) => { e.__bs = e.__bs || getComputedStyle(e).boxShadow; if (e.__bs === "none") e.__bs = "0 0 0 0px rgba(107,79,224,0)"; tl.to(e, { scale: 1.035, boxShadow: GLOW, duration: 0.45, ease: EZ }, t); });
            prev = tg;
          });
          const tEnd = tc(i + 1) - 0.4;
          prev.forEach((e) => tl.to(e, { scale: 1, boxShadow: e.__bs, duration: 0.3, ease: EZ }, tEnd));
          tops.forEach((top) => tl.to(top, { opacity: 1, duration: 0.3, ease: EZ }, tEnd));
        });
        // gestes dans l'appli
        const btn = K.$(".a-btn", pages[3]);
        A.tap(ph, 280, 92 + btn.offsetTop + 41, ts(3, 2) + 0.6);
        const eb = K.$(".eb", pages[5]); tl.set(eb, { scaleX: 0 }, 0); tl.to(eb, { scaleX: 1, duration: 1.2, ease: EO }, ts(5, 1) + 0.2);
        K.count(K.$(".km", pages[7]), 1240, ts(7, 1) + 0.1, 1.4, (v) => { const n = Math.round(v); return (n >= 1000 ? Math.floor(n / 1000) + " " + String(n % 1000).padStart(3, "0") : n) + " km"; }, { ticks: 10 });

        // ── texte de gauche
        CH.forEach((c, i) => {
          const t0 = tc(i), t1 = tc(i + 1);
          const box = ab({ left: "120px", top: "120px", width: "860px" },
            `<div class="kick">CHAPITRE ${i + 1} / 8 · ${c[1]}</div><div class="ttl" style="margin-top:18px;font-size:72px">${c[2]}</div><div class="pb" style="margin-top:22px">Avant : <b>${c[3]}</b></div>`);
          tl.set(box, { opacity: 0 }, 0); tl.to(box, { opacity: 1, duration: 0.01 }, t0);
          fin(K.$(".kick", box), t0 + 0.1, 0.5, 12); fin(K.$(".ttl", box), t0 + 0.25, 0.7, 24); fin(K.$(".pb", box), t0 + 1.0, 0.5, 12);
          fout(box, t1 - 0.45);
          const av = ab({ left: "120px", top: "478px" }, `<div class="avec">AVEC LIMO :</div>`); fin(av, t0 + 1.7, 0.4, 10); fout(av, t1 - 0.45);
          c[5].forEach(([txt], k) => {
            const st = ab({ left: "120px", top: SY[k] + "px", width: "820px" }, `<div class="st"><span class="nb">${k + 1}</span><span>${txt}</span></div>`);
            fin(st, ts(i, k), 0.5, 14);
            K.sfx(ts(i, k), "tick", 0.06, 0, { f: 2200 });
            if (k < 2) tl.to(st, { opacity: 0.4, duration: 0.4, ease: EZ }, ts(i, k + 1));
            fout(st, t1 - 0.45);
          });
        });

        // ── barre de chapitres
        const nav = ab({ left: "120px", top: "985px" }, `<div class="nav">${CH.map((c) => `<span>${c[0]}</span>`).join("")}</div>`);
        fin(nav, T0, 0.6, 10); fout(nav, tc(8) - 0.4);
        const navS = K.$$(".nav span", nav);
        CH.forEach((c, i) => {
          tl.to(navS[i], { backgroundColor: "#6b4fe0", color: "#ffffff", borderColor: "#6b4fe0", duration: 0.4, ease: EZ }, tc(i));
          tl.to(navS[i], { backgroundColor: "rgba(255,255,255,0.7)", color: "#4f5378", borderColor: "#e4e0f6", duration: 0.4, ease: EZ }, tc(i + 1));
        });

        // ── la mascotte-guide : zone réservée x 1000–1230, elle suit l'étape en cours
        // repère : le coin haut-gauche de la mascotte (largeur 170, hauteur ≈ 206)
        const M = N.mascot({ left: "0px", top: "0px", width: "170px" }, { expr: "happy" });
        const at = (t, x, y, s = 1, d = 0.6) => tl.to(M.el, { x, y, scale: s, duration: d, ease: EZ }, t);
        // intro : au centre, salue, puis présente
        const lg = ab({ left: "0", right: "0", top: "170px", textAlign: "center" }, `<img src="assets/img/limo-logo-ad.png" alt="LIMO" style="height:150px" /><div style="margin-top:26px;font-family:Montserrat,sans-serif;font-weight:700;font-size:46px;color:#1b1f4b">Le bras droit du conseiller immo.</div><div style="margin-top:16px;font-family:Inter,sans-serif;font-size:32px;color:#4f5378">8 choses que LIMO fait pour toi, chaque jour.</div>`);
        fin(lg, 0.4, 0.8, 20); fout(lg, T0 - 0.9, 0.5);
        tl.set(M.el, { opacity: 0, x: 875, y: 600, scale: 1.25 }, 0);
        tl.fromTo(M.el, { opacity: 0, y: 700 }, { opacity: 1, y: 600, duration: 0.8, ease: EO, immediateRender: false }, 1.2);
        M.wave(2.0); M.blink(3.2); M.expr("wink", 3.6, false); M.hop(4.2, 50); M.expr("happy", 4.6, false);
        // va se placer dans sa zone, à côté du téléphone
        at(T0 - 0.8, 1040, SY[0] - 60, 1, 0.8);
        M.float(T0, 8 * CHD - 0.5, 7);
        const EXP = ["happy", "think", "wow", "wink", "euro", "think", "heart", "wink"];
        CH.forEach((c, i) => {
          // début de chapitre : petit saut d'accueil
          at(tc(i) + 0.1, 1040, 300, 1, 0.6); M.hop(tc(i) + 0.7, 40); M.expr("happy", tc(i) + 0.1, false);
          c[5].forEach((s, k) => {
            const t = ts(i, k);
            at(t - 0.1, 1050, SY[k] - 70, 1, 0.55);       // descend à la hauteur de l'étape
            M.tilt(t + 0.45, 12, 0.3); M.tilt(t + 1.6, 0, 0.3); // se penche vers le téléphone
            M.expr(k === 2 ? EXP[i] : (k ? "wink" : "think"), t + 0.3, false);
            if (k === 2) M.blink(t + 1.2);
          });
        });
        // récap : sous la grille
        at(tc(8) - 0.2, 875, 840, 0.9, 0.7); M.expr("heart", tc(8) + 0.4, false);
        [0, 1, 2].forEach((k) => M.hop(tc(8) + 1.2 + k * 1.6, 40));

        // ── récap : les 12 agents
        const AG = [["target", "Détecteur de ventes", "Les diagnostics d’hier, les ventes de demain"], ["search", "Pige des particuliers", "Leurs annonces deviennent tes mandats"], ["pin", "Estimation & marché", "Cadastre, DVF, diagnostics"], ["pen", "Rédacteur d’annonce", "Optimisée, mentions incluses"],
          ["clip", "Analyseur de dossier", "Un PDF, la fiche remplie"], ["image", "Habilleur de photos", "Tes photos signées"], ["car", "Frais kilométriques", "Prêts pour le comptable"], ["magnet", "Matcheur acheteurs", "Le bon acheteur, tout de suite"],
          ["megaphone", "Diffuseur réseaux", "3 posts depuis un lien"], ["sofa", "Home staging virtuel", "Meubler, vider, repeindre"], ["wrench", "Mes artisans", "Le bon artisan, près du bien"], ["msg", "Messages Insta & Facebook", "Prospects repérés"]];
        const tr = tc(8);
        const rt = ab({ left: "0", right: "0", top: "60px", textAlign: "center" }, `<div class="ttl" style="font-size:64px">12 agents. <em>Un seul assistant.</em></div>`);
        fin(rt, tr + 0.2, 0.7, 20); fout(rt, tr + 6.6);
        AG.forEach((a, i) => {
          const x = 140 + (i % 4) * 420, y = 210 + Math.floor(i / 4) * 190;
          const tE = ab({ left: x + "px", top: y + "px" }, `<div class="tile"><span class="ic">${K.icon(a[0])}</span><span><b>${a[1]}</b><small>${a[2]}</small></span></div>`);
          fin(tE, tr + 0.6 + i * 0.12, 0.5, 18); fout(tE, tr + 6.6);
        });
        K.sfx(tr + 0.6, "sparkle", 0.08);
        tl.to(M.el, { opacity: 0, duration: 0.4, ease: EZ }, tr + 6.5);

        // ── fin : appel à l'action
        const te = tr + 7.0;
        const end = ab({ left: "0", right: "0", top: "150px", textAlign: "center" }, `<div class="ttl" style="font-size:88px">Toi, tu fais le terrain.<br><em>LIMO fait le reste.</em></div><div style="margin-top:46px"><img src="assets/img/limo-logo-ad.png" alt="LIMO" style="height:120px" /></div><div style="margin-top:44px"><span class="cta" style="font-size:44px;padding:30px 56px">Essai gratuit 14 jours →</span></div><div style="margin-top:32px;font-family:Inter,sans-serif;font-size:36px;color:#4f5378">Sans engagement · dès 49 €/mois · <b style="color:#1b1f4b">app.leadengineai.fr</b></div>`);
        fin(end, te + 0.2, 0.8, 24);
        const M2 = N.mascot({ left: "1560px", top: "640px", width: "210px" }, { expr: "happy" });
        tl.set(M2.el, { opacity: 0 }, 0); tl.fromTo(M2.el, { opacity: 0, y: 60 }, { opacity: 1, y: 0, duration: 0.6, ease: EO, immediateRender: false }, te + 0.8);
        M2.wave(te + 1.4); M2.hop(te + 3.0, 50); M2.blink(te + 4.2); M2.expr("wink", te + 4.6, false);
        K.sfx(te + 0.3, "success", 0.1);
""".replace("__T0", str(T0)).replace("__CHD", str(CHD))

if __name__ == "__main__":
    shell = SHELL16.replace("    </style>", EXTRA, 1).replace("tout ce qu'il fait pour toi", "tout ce qu'il fait pour toi (V2)")
    html = shell.format(faces=FACES, dur=DUR, name=NAME, body=BODY.strip("\n"))
    (HERE.parent / "reels" / f"{NAME}.html").write_text(html, encoding="utf-8")
    print("reels/" + NAME + ".html", DUR)
