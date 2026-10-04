"""Vidéo « site internet » V3 TUTORIEL, 16:9 (1920×1080) : comment utiliser LIMO, geste par geste (demande de Thomy :
« plus tutoriel »). Un doigt virtuel navigue dans l'application recréée (accueil → menu « Plus » → « Mes agents » → agent),
appuie, et l'écran réagit (pages qui s'ouvrent, texte qui se tape, résultats qui apparaissent). À gauche : « TUTO n/8 »,
le titre et 3 consignes-gestes qui passent en ✓ une fois faites. La mascotte-guide suit chaque consigne dans sa zone.
Sans voix ni musique. Fonctions = liste officielle de l'appli. Données affichées = exemples fictifs.

Usage : python3 outils/site3.py   (réécrit reels/site-03-tuto-limo.html)
"""
import importlib.util
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from cine import FACES  # noqa: E402

_sp = importlib.util.spec_from_file_location("site_v1", HERE / "site.py")
_m = importlib.util.module_from_spec(_sp)
_sp.loader.exec_module(_m)
SHELL16 = _m.SHELL16

NAME = "site-03-tuto-limo"
T0, CHD = 6.0, 12.0
DUR = round(T0 + 8 * CHD + 7.0 + 6.5, 2)
EXTRA = """
      .st {{ display: flex; align-items: center; gap: 22px; font-family: Inter, sans-serif; font-size: 34px; line-height: 1.25; color: #1b1f4b; font-weight: 600; }}
      .st .nb {{ position: relative; flex: none; width: 62px; height: 62px; border-radius: 50%; background: #6b4fe0; color: #fff; display: flex; align-items: center; justify-content: center; font-family: Montserrat, sans-serif; font-weight: 800; font-size: 30px; }}
      .st .nb .ok {{ position: absolute; inset: 0; border-radius: 50%; background: #2cc4b5; display: flex; align-items: center; justify-content: center; }}
      .st .nb .ok svg.i {{ width: 32px; height: 32px; stroke-width: 3.2; color: #fff; }}
      .nav span {{ padding: 9px 14px; }}
      .toast svg.i {{ flex: none; width: 30px; height: 30px; stroke-width: 3; color: #2cc4b5; }}
      .sub {{ font-family: Montserrat, sans-serif; font-weight: 800; font-size: 26px; letter-spacing: .12em; color: #6b4fe0; }}
      .path {{ display: inline-flex; align-items: center; gap: 10px; margin-top: 20px; padding: 10px 20px; border-radius: 16px; background: #fff; border: 1px solid #e4e0f6; font-family: Inter, sans-serif; font-size: 26px; font-weight: 600; color: #4f5378; }}
      .cur {{ position: absolute; left: 0; top: 0; width: 64px; height: 64px; border-radius: 50%; background: rgba(255,255,255,.55); border: 4px solid rgba(107,79,224,.85); box-shadow: 0 8px 22px rgba(27,31,75,.35); z-index: 40; }}
      .cur i {{ position: absolute; inset: -4px; border-radius: 50%; border: 4px solid rgba(107,79,224,.7); }}
      .inp {{ display: flex; align-items: center; gap: 12px; min-height: 76px; padding: 14px 20px; border-radius: 20px; background: #fff; border: 2px solid #e4e0f6; font-size: 23px; color: #1b1f4b; line-height: 1.4; }}
      .inp .ph {{ color: #9a9cb5; }}
      .ag {{ display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }}
      .ag div {{ display: flex; align-items: center; gap: 12px; height: 92px; padding: 0 14px; border-radius: 22px; background: #fff; border: 1px solid #efedf8; box-shadow: 0 6px 18px rgba(27,31,75,.06); font-size: 19px; font-weight: 600; line-height: 1.2; color: #1b1f4b; }}
      .ag .a-ic {{ width: 50px; height: 50px; border-radius: 16px; }}
      .ag .a-ic svg.i {{ width: 28px; height: 28px; }}
      .drop {{ display: flex; flex-direction: column; align-items: center; justify-content: center; gap: 10px; height: 170px; border-radius: 24px; border: 3px dashed #c9bff3; background: #f8f6ff; color: #6b4fe0; font-size: 23px; font-weight: 600; }}
      .drop svg.i {{ width: 44px; height: 44px; }}
      .mic {{ margin: 30px auto 10px; width: 170px; height: 170px; border-radius: 50%; background: #6b4fe0; color: #fff; display: flex; align-items: center; justify-content: center; box-shadow: 0 16px 40px rgba(107,79,224,.4); }}
      .mic svg.i {{ width: 80px; height: 80px; }}
      .wv {{ display: flex; align-items: center; justify-content: center; gap: 6px; height: 70px; }}
      .wv i {{ display: block; width: 8px; height: 100%; border-radius: 4px; background: #6b4fe0; }}
      .toast {{ display: flex; align-items: center; gap: 12px; padding: 18px 22px; border-radius: 20px; background: #1b1f4b; color: #fff; font-size: 22px; font-weight: 600; }}
    </style>"""

BODY = r"""
        tl.set([K.$(".n-bg", root), ...K.$$(".n-arc", root)], { opacity: 0 }, 0);
        const EZ = "power2.inOut", EO = "power2.out";
        const ab = (css, html, parent = root) => { const e = N.ab("", html, css, parent); [e, ...K.$$("*", e)].forEach((x) => ["data-layout-allow-overflow", "data-layout-allow-overlap", "data-layout-allow-occlusion"].forEach((a) => x.setAttribute(a, ""))); return e; };
        const fin = (e, t, d = 0.6, y = 24) => { tl.set(e, { opacity: 0 }, 0); tl.fromTo(e, { opacity: 0, y }, { opacity: 1, y: 0, duration: d, ease: EO, immediateRender: false }, t); };
        const fout = (e, t, d = 0.45) => tl.to(e, { opacity: 0, duration: d, ease: EZ }, t);
        const T0 = __T0, CHD = __CHD, SY = [560, 690, 820];
        const tc = (i) => T0 + i * CHD, ts = (i, k) => tc(i) + 1.0 + k * 3.6;

        // ── écrans de l'application
        const back = (t) => `<div class="a-back">${K.icon("chev")}${t}</div>`;
        const AGL = [["target", "v", "Détecteur de ventes"], ["search", "t", "Pige des particuliers"], ["pin", "o", "Estimation & marché"], ["pen", "v", "Rédacteur d’annonce"], ["clip", "g", "Analyseur de dossier"], ["image", "t", "Habilleur de photos"],
          ["car", "o", "Frais kilométriques"], ["magnet", "v", "Matcheur acheteurs"], ["megaphone", "t", "Diffuseur réseaux"], ["sofa", "g", "Home staging virtuel"], ["wrench", "o", "Mes artisans"], ["msg", "v", "Messages Insta & FB"]];
        const HTML = {
          home: () => A.S.home(),
          agents: () => back("Mes agents") + `<div class="ag">${AGL.map((a) => `<div><span class="a-ic ${a[1]}">${K.icon(a[0])}</span><span>${a[2]}</span></div>`).join("")}</div>`,
          relances: () => back("Relances du jour") + `<div style="display:flex;gap:10px;margin:4px 0 14px"><span class="a-tag">${K.icon("refresh")}32 contacts</span><span class="a-tag t">${K.icon("check")}Messages prêts</span></div>` +
            A.row("users", "v", "M. Vidal", "Estimation · il y a 47 j", "", `<span class="a-tag t">Prêt</span>`) +
            `<div class="a-card a-msg pv" style="position:absolute;left:26px;right:26px;top:238px;z-index:5;font-size:21px;box-shadow:0 18px 40px rgba(27,31,75,.25);border:2px solid #6b4fe0">« Bonjour M. Vidal, suite à notre estimation, souhaitez-vous que l’on fasse le point sur votre projet ? »</div>` +
            A.row("users", "v", "Famille Martin", "Vendre au printemps", "", `<span class="a-tag t">Prêt</span>`) + A.row("users", "v", "Mme Roy", "Succession en cours", "", `<span class="a-tag t">Prêt</span>`) +
            `<div class="a-btn snd" style="margin-top:8px">${K.icon("send")}<span class="bt">Envoyer les 32 relances</span></div>`,
          dictee: () => back("Compte rendu de visite") + `<div class="mic">${K.icon("mic")}</div><div class="wv">${Array.from({ length: 22 }, () => "<i></i>").join("")}</div><div class="tmr" style="text-align:center;font-size:26px;font-weight:700;color:#6b4fe0">0:00</div>` +
            `<div class="a-h2 rv">Fiche mise à jour</div>` + A.row("users", "v", "Famille Durand", "Acheteurs · Vignols").replace('class="a-card a-row"', 'class="a-card a-row rv"') + A.row("home", "t", "Coup de cœur jardin", "Hésitent sur la cuisine").replace('class="a-card a-row"', 'class="a-card a-row rv"') + A.row("clock", "o", "Rappel jeudi 18 h", "Envoyer 2 biens similaires").replace('class="a-card a-row"', 'class="a-card a-row rv"'),
          doc: () => back("Analyseur de dossier") + `<div class="drop">${K.icon("file")}Déposer un PDF</div><div class="a-card rv pdf" style="display:flex;align-items:center;gap:16px;padding:18px 20px;margin-top:-170px"><span class="a-ic r">${K.icon("file")}</span><span style="flex:1"><b style="font-size:23px">Compromis.pdf</b><small style="display:block;font-size:19px;color:#6e6e80">12 pages · analyse…</small><div class="a-bar" style="margin-top:8px"><i class="pb" style="width:100%"></i></div></span></div><div style="height:60px"></div>` +
            `<div class="a-h2 rv">Fiche remplie automatiquement</div>` + [["users", "v", "Vendeurs : M. et Mme T.", "Acquéreurs : Famille Lambert"], ["euro", "t", "Prix : 245 000 €", "Dépôt de garantie 5 %"], ["scale", "g", "Notaire : Me Faure", "Signature prévue le 14/11"], ["alert", "o", "Prêt : 60 jours", "Condition suspensive"]].map((r) => A.row(r[0], r[1], r[2], r[3], "", `<span class="ok">${K.icon("check")}</span>`).replace('class="a-card a-row"', 'class="a-card a-row rv"')).join(""),
          detect: () => A.S.detect(),
          estim: () => back("Estimation & marché") + `<div class="inp ad"><span class="ph">Adresse du bien…</span><span class="ty"></span></div><div class="inp sf" style="margin-top:10px"><span class="ph">Surface…</span><span class="ty"></span></div><div class="a-btn go" style="margin-top:14px">${K.icon("calc")}Estimer</div>` +
            `<div class="a-card rv" style="padding:20px 22px;margin-top:16px"><small style="font-size:19px;color:#6e6e80">Maison · Allassac · 120 m²</small><div style="margin-top:4px;font-family:Montserrat,sans-serif;font-weight:800;font-size:42px;color:#6b4fe0">239 – 252 k€</div><div class="a-bar" style="margin-top:12px"><i class="eb" style="width:100%"></i></div></div>` +
            [["pin", "v", "Cadastre · 1 250 m²", "Parcelle vérifiée"], ["bank", "t", "3 ventes DVF comparables", "Dans un rayon de 2 km"]].map((r) => A.row(...r).replace('class="a-card a-row"', 'class="a-card a-row rv"')).join(""),
          annonce: () => back("Rédacteur d’annonce") + `<div class="inp nt" style="align-items:flex-start;min-height:120px"><span class="ph">Tes infos en vrac…</span><span class="ty"></span></div><div class="a-btn go" style="margin-top:14px">${K.icon("pen")}Rédiger l’annonce</div>` +
            `<div class="a-card rv" style="padding:18px 20px;margin-top:16px"><div class="a-ph" style="height:150px;margin-bottom:12px">${K.houseArt(480, 150, "an")}</div><div style="font-family:'Source Serif 4',serif;font-size:27px;font-weight:600;line-height:1.2">Maison familiale au calme avec grand terrain</div><div style="margin-top:8px;font-size:19px;line-height:1.45;color:#3a3a3c">À Vignols, 120 m² lumineux, 4 chambres, séjour traversant sur 1 500 m² de terrain.</div></div>` +
            `<div class="rv" style="display:flex;gap:10px;margin-top:12px"><span class="a-tag t">${K.icon("check")}Mentions légales</span><span class="a-tag">${K.icon("check")}Prête à publier</span></div>`,
          km: () => back("Frais kilométriques") + `<div class="a-card" style="padding:22px;margin-bottom:14px;text-align:center"><small style="font-size:20px;color:#6e6e80">Octobre</small><div class="km" style="margin-top:4px;font-family:Montserrat,sans-serif;font-weight:800;font-size:60px;color:#1b1f4b">0 km</div></div>` +
            A.row("car", "v", "Brive → Allassac", "Visite · 18 km", "9:40") + A.row("car", "v", "Allassac → Voutezac", "Estimation · 11 km", "14:10") + A.row("car", "v", "Voutezac → Brive", "Retour · 21 km", "17:30") +
            `<div class="a-btn go" style="margin-top:10px">${K.icon("send")}Exporter pour mon comptable</div><div class="toast rv" style="margin-top:14px">${K.icon("check")}Export envoyé à ton comptable</div>`,
        };

        // ── le téléphone (560 px d'origine, réduit à 90 %)
        const ph = A.phone({ left: "1262px", top: "22px", width: "560px" }, { time: "8:00" });
        tl.set(ph.wrap, { scale: 0.9, transformOrigin: "0 0" }, 0);
        const P = {};
        Object.keys(HTML).forEach((k) => (P[k] = A.page(ph, HTML[k]())));
        K.$$(".rv", ph.view).forEach((e) => tl.set(e, { opacity: 0 }, 0));
        A.enter(ph, T0 - 0.8, { ry: -24, ry2: -10, flatAt: 0.9 });
        let curPg = P.home;
        const go = (to, t, bk = false) => { A.go(ph, curPg, to, t, { back: bk }); curPg = to; };
        const reveal = (els, t, st = 0.25) => [].concat(els).forEach((e, i) => { tl.fromTo(e, { opacity: 0, y: 14 }, { opacity: 1, y: 0, duration: 0.4, ease: EO, immediateRender: false }, t + i * st); });
        const GLOW = "0 0 0 4px rgba(107,79,224,.6), 0 16px 34px rgba(107,79,224,.28)";
        const glow = (els, t, d = 2.2) => [].concat(els).forEach((e) => { const bs = getComputedStyle(e).boxShadow; tl.to(e, { boxShadow: GLOW, duration: 0.35, ease: EZ }, t); tl.to(e, { boxShadow: bs === "none" ? "0 0 0 0px rgba(107,79,224,0)" : bs, duration: 0.35, ease: EZ }, t + d); });

        // ── le doigt virtuel (dans l'écran) : il se déplace vers un élément et appuie
        const cur = K.h("div", "cur", "<i></i>", ph.scr);
        const ring = K.$("i", cur);
        tl.set(cur, { opacity: 0, x: 240, y: 700 }, 0); tl.set(ring, { opacity: 0 }, 0);
        const posOf = (el) => { let x = 0, y = 0, e = el; while (e && e !== ph.scr) { x += e.offsetLeft; y += e.offsetTop; e = e.offsetParent; } return { x: x + el.offsetWidth / 2 - 32, y: y + el.offsetHeight / 2 - 32 }; };
        const show = (t) => tl.to(cur, { opacity: 1, duration: 0.3, ease: EO }, t);
        const hide = (t) => tl.to(cur, { opacity: 0, duration: 0.3, ease: EZ }, t);
        const tap = (el, t) => {
          tl.to(cur, { x: () => posOf(el).x, y: () => posOf(el).y, duration: 0.55, ease: EZ }, t - 0.6);
          tl.to(cur, { scale: 0.78, duration: 0.09, ease: "power2.in", yoyo: true, repeat: 1 }, t);
          tl.fromTo(ring, { opacity: 0.9, scale: 1 }, { opacity: 0, scale: 2.2, duration: 0.5, ease: EO, immediateRender: false }, t);
          K.sfx(t, "tap", 0.3);
        };
        const tabs = K.$$(".a-tab > div", ph.scr); // Accueil, Contacts, +, Mandats, Plus
        const tile = (n) => K.$$(".ag > div", P.agents)[n];
        // ouvrir un agent : Plus → Mes agents → tuile
        const openAgent = (n, page, t) => { tap(tabs[4], t); go(P.agents, t + 0.3); tap(tile(n), t + 1.5); go(page, t + 1.8); };
        const home = (t) => { if (curPg !== P.home) go(P.home, t, true); };

        // ── chapitres (texte de gauche)
        const CH = [
          ["L’accueil", "TA JOURNÉE", "Comprendre ton écran d’accueil", null, ["Ouvre LIMO : tes priorités du jour s’affichent", "Chaque action a son heure, dans l’ordre", "En bas : tout LIMO à portée de pouce"]],
          ["Relances", "RELANCER", "Relancer en 1 clic", "Accueil → Relancer 32 contacts", ["Appuie sur « Relancer 32 contacts »", "Ouvre un contact : le message est déjà écrit", "Appuie sur « Envoyer » : c’est parti"]],
          ["Compte rendu", "SE SOUVENIR", "Dicter un compte rendu de visite", "Bouton ＋", ["Après la visite, appuie sur ＋", "Appuie sur le micro et parle", "La fiche client se met à jour toute seule"]],
          ["Dossier", "LIRE UN DOSSIER", "Analyser un compromis", "Plus → Mes agents → Analyseur", ["Ouvre « Plus », puis l’Analyseur de dossier", "Dépose ton compromis en PDF", "Les infos sont extraites : vérifie, valide"]],
          ["Détecteur", "TROUVER DES VENDEURS", "Repérer les vendeurs probables", "Plus → Mes agents → Détecteur", ["Ouvre le Détecteur de ventes", "Les points violets : vendeurs probables", "Appuie sur un bien pour voir le signal"]],
          ["Estimation", "ESTIMER", "Estimer un bien", "Plus → Mes agents → Estimation", ["Ouvre l’agent Estimation & marché", "Entre l’adresse et la surface", "Appuie sur « Estimer » : la fourchette s’affiche"]],
          ["Annonce", "RÉDIGER", "Rédiger une annonce", "Plus → Mes agents → Rédacteur", ["Ouvre le Rédacteur d’annonce", "Écris tes infos en vrac", "Appuie sur « Rédiger » : prête, mentions incluses"]],
          ["Frais km", "GÉRER", "Tes frais kilométriques", "Plus → Mes agents → Frais km", ["Ouvre l’agent Frais kilométriques", "Tes trajets sont notés tout seuls", "Appuie sur « Exporter » pour ton comptable"]],
        ];
        CH.forEach((c, i) => {
          const t0 = tc(i), t1 = tc(i + 1);
          const box = ab({ left: "120px", top: "110px", width: "880px" }, `<div class="kick">TUTO ${i + 1} / 8 · ${c[1]}</div><div class="ttl" style="margin-top:16px;font-size:66px">${c[2]}</div>${c[3] ? `<div class="path">${K.icon("chev")}${c[3]}</div>` : ""}`);
          K.$$(".path svg.i", box).forEach((s) => (s.style.cssText = "width:24px;height:24px;color:#6b4fe0;transform:rotate(0deg)"));
          tl.set(box, { opacity: 0 }, 0); tl.to(box, { opacity: 1, duration: 0.01 }, t0);
          fin(K.$(".kick", box), t0 + 0.1, 0.5, 12); fin(K.$(".ttl", box), t0 + 0.2, 0.6, 22); if (c[3]) fin(K.$(".path", box), t0 + 0.6, 0.5, 10);
          fout(box, t1 - 0.45);
          const sb = ab({ left: "120px", top: "478px" }, `<div class="sub">EN 3 GESTES :</div>`); fin(sb, t0 + 0.7, 0.4, 10); fout(sb, t1 - 0.45);
          c[4].forEach((txt, k) => {
            const st = ab({ left: "120px", top: SY[k] + "px", width: "840px" }, `<div class="st"><span class="nb">${k + 1}<span class="ok">${K.icon("check")}</span></span><span class="tx">${txt}</span></div>`);
            const ok = K.$(".ok", st);
            tl.set(ok, { opacity: 0, scale: 0.6 }, 0);
            fin(st, ts(i, k), 0.5, 14);
            tl.to(ok, { opacity: 1, scale: 1, duration: 0.35, ease: EO }, (k < 2 ? ts(i, k + 1) : t1 - 1.0) - 0.3);
            if (k < 2) tl.to(K.$(".tx", st), { opacity: 0.5, duration: 0.4, ease: EZ }, ts(i, k + 1));
            fout(st, t1 - 0.45);
          });
        });

        // ── les gestes dans l'appli, chapitre par chapitre
        const S = (i, k) => ts(i, k);
        // 1 · accueil
        glow(K.$(".a-prio", P.home), S(0, 0) + 0.3, 2.6);
        glow(K.$$(".a-row", P.home).slice(0, 4), S(0, 1) + 0.3, 2.6);
        glow(K.$(".a-tab", ph.scr), S(0, 2) + 0.3, 2.4);
        show(S(0, 2)); tl.to(cur, { x: () => posOf(tabs[0]).x, y: () => posOf(tabs[0]).y, duration: 0.5, ease: EZ }, S(0, 2) + 0.2);
        [0, 2, 4].forEach((n, j) => tl.to(cur, { x: () => posOf(tabs[n]).x, y: () => posOf(tabs[n]).y, duration: 0.5, ease: EZ }, S(0, 2) + 0.9 + j * 0.7));
        // 2 · relances
        tap(K.$$(".a-row", P.home)[0], S(1, 0) + 0.8); go(P.relances, S(1, 0) + 1.1);
        tap(K.$$(".a-row", P.relances)[0], S(1, 1) + 0.7); const pv = K.$(".pv", P.relances); A.over(pv); K.$$(".a-row", P.relances).forEach((r) => A.over(r)); tl.set(pv, { opacity: 0 }, 0); tl.fromTo(pv, { opacity: 0, y: -10, scale: 0.96 }, { opacity: 1, y: 0, scale: 1, duration: 0.45, ease: EO, immediateRender: false }, S(1, 1) + 0.9); tl.to(pv, { opacity: 0, duration: 0.3, ease: EZ }, S(1, 2) + 0.2); glow(K.$$(".a-row", P.relances)[0], S(1, 1) + 0.9, 2.0);
        const snd = K.$(".snd", P.relances);
        tap(snd, S(1, 2) + 0.8); tl.to(snd, { backgroundColor: "#2cc4b5", duration: 0.3, ease: EZ }, S(1, 2) + 1.0); tl.set(K.$(".bt", snd), { textContent: "32 relances envoyées ✓" }, S(1, 2) + 1.0); K.sfx(S(1, 2) + 1.0, "success", 0.12);
        home(tc(2) - 0.6);
        // 3 · compte rendu dicté
        tap(tabs[2], S(2, 0) + 0.8); go(P.dictee, S(2, 0) + 1.1);
        const mic = K.$(".mic", P.dictee);
        tap(mic, S(2, 1) + 0.8); tl.to(mic, { scale: 1.08, duration: 0.4, ease: "sine.inOut", yoyo: true, repeat: 5 }, S(2, 1) + 0.9);
        K.$$(".wv i", P.dictee).forEach((b, j) => { tl.set(b, { scaleY: 0.15 }, 0); for (let q = 0; q < 6; q++) tl.to(b, { scaleY: 0.2 + 0.8 * Math.abs(Math.sin(j * 0.6 + q * 1.4)), duration: 0.4, ease: "sine.inOut" }, S(2, 1) + 0.9 + q * 0.4); tl.to(b, { scaleY: 0.15, duration: 0.3, ease: EZ }, S(2, 1) + 3.3); });
        K.count(K.$(".tmr", P.dictee), 38, S(2, 1) + 0.9, 2.4, (v) => "0:" + String(Math.round(v)).padStart(2, "0"), {});
        hide(S(2, 2)); reveal(K.$$(".rv", P.dictee), S(2, 2) + 0.2, 0.45); K.sfx(S(2, 2) + 0.4, "success", 0.1);
        show(tc(3) - 1.0); home(tc(3) - 0.6);
        // 4 · analyseur de dossier
        openAgent(4, P.doc, S(3, 0) + 0.6);
        const drop = K.$(".drop", P.doc);
        tap(drop, S(3, 1) + 0.8); tl.to(drop, { opacity: 0, duration: 0.3, ease: EZ }, S(3, 1) + 1.0); reveal(K.$(".pdf", P.doc), S(3, 1) + 1.1);
        const pb = K.$(".pb", P.doc); tl.set(pb, { scaleX: 0, transformOrigin: "0 50%" }, 0); tl.to(pb, { scaleX: 1, duration: 1.6, ease: EZ }, S(3, 1) + 1.3);
        hide(S(3, 2)); reveal(K.$$(".a-h2.rv, .a-row.rv", P.doc), S(3, 2) + 0.2, 0.4); K.sfx(S(3, 2) + 0.4, "success", 0.1);
        show(tc(4) - 1.0); home(tc(4) - 0.6);
        // 5 · détecteur de ventes
        openAgent(0, P.detect, S(4, 0) + 0.6);
        glow(K.$(".a-map", P.detect), S(4, 1) + 0.3, 2.8);
        K.$$(".a-pin.hot", P.detect).forEach((p) => tl.to(p, { scale: 1.5, duration: 0.35, ease: "sine.inOut", yoyo: true, repeat: 5 }, S(4, 1) + 0.4));
        const r0 = K.$$(".a-row", P.detect)[0]; tap(r0, S(4, 2) + 0.8); glow(r0, S(4, 2) + 1.0, 2.0); glow(K.$(".a-tag", r0), S(4, 2) + 1.0, 2.0);
        home(tc(5) - 0.6);
        // 6 · estimation
        openAgent(2, P.estim, S(5, 0) + 0.6);
        tap(K.$(".ad", P.estim), S(5, 1) + 0.6); tl.set(K.$(".ad .ph", P.estim), { display: "none" }, S(5, 1) + 0.7); K.type(K.$(".ad .ty", P.estim), "12 rue des Tilleuls, Allassac", S(5, 1) + 0.7, 1.2, 0.04);
        tap(K.$(".sf", P.estim), S(5, 1) + 2.4); tl.set(K.$(".sf .ph", P.estim), { display: "none" }, S(5, 1) + 2.5); K.type(K.$(".sf .ty", P.estim), "120 m²", S(5, 1) + 2.5, 0.5, 0.04);
        tap(K.$(".go", P.estim), S(5, 2) + 0.8); reveal(K.$$(".rv", P.estim), S(5, 2) + 1.1, 0.35);
        const eb = K.$(".eb", P.estim); tl.set(eb, { scaleX: 0, transformOrigin: "0 50%" }, 0); tl.to(eb, { scaleX: 1, duration: 1.0, ease: EO }, S(5, 2) + 1.4); K.sfx(S(5, 2) + 1.2, "success", 0.1);
        home(tc(6) - 0.6);
        // 7 · rédacteur d'annonce
        openAgent(3, P.annonce, S(6, 0) + 0.6);
        tap(K.$(".nt", P.annonce), S(6, 1) + 0.6); tl.set(K.$(".nt .ph", P.annonce), { display: "none" }, S(6, 1) + 0.7); K.type(K.$(".nt .ty", P.annonce), "maison vignols 120m2 4 ch terrain 1500m2 calme, séjour traversant", S(6, 1) + 0.7, 2.2, 0.03);
        tap(K.$(".go", P.annonce), S(6, 2) + 0.8); reveal(K.$$(".rv", P.annonce), S(6, 2) + 1.1, 0.4); K.sfx(S(6, 2) + 1.2, "success", 0.1);
        home(tc(7) - 0.6);
        // 8 · frais kilométriques
        openAgent(6, P.km, S(7, 0) + 0.6);
        glow(K.$$(".a-row", P.km), S(7, 1) + 0.3, 2.6);
        K.count(K.$(".km", P.km), 1240, S(7, 1) + 0.4, 1.6, (v) => { const n = Math.round(v); return (n >= 1000 ? Math.floor(n / 1000) + " " + String(n % 1000).padStart(3, "0") : n) + " km"; }, { ticks: 10 });
        tap(K.$(".go", P.km), S(7, 2) + 0.8); reveal(K.$(".toast", P.km), S(7, 2) + 1.1); K.sfx(S(7, 2) + 1.1, "success", 0.12);
        hide(tc(8) - 0.8);
        tl.to(ph.wrap, { opacity: 0, y: 40, duration: 0.6, ease: EZ }, tc(8) - 0.4);
        // le doigt apparaît dès le premier geste du chapitre 2
        show(S(1, 0) + 0.1);

        // ── barre des tutos
        const nav = ab({ left: "120px", top: "985px" }, `<div class="nav" style="gap:10px;font-size:19px">${CH.map((c) => `<span>${c[0]}</span>`).join("")}</div>`);
        fin(nav, T0, 0.6, 10); fout(nav, tc(8) - 0.4);
        const navS = K.$$(".nav span", nav);
        CH.forEach((c, i) => {
          tl.to(navS[i], { backgroundColor: "#6b4fe0", color: "#ffffff", borderColor: "#6b4fe0", duration: 0.4, ease: EZ }, tc(i));
          tl.to(navS[i], { backgroundColor: "rgba(255,255,255,0.7)", color: "#4f5378", borderColor: "#e4e0f6", duration: 0.4, ease: EZ }, tc(i + 1));
        });

        // ── la mascotte-guide (zone x 1050–1230) : elle suit la consigne en cours
        const M = N.mascot({ left: "0px", top: "0px", width: "170px" }, { expr: "happy" });
        const at = (t, x, y, s = 1, d = 0.6) => tl.to(M.el, { x, y, scale: s, duration: d, ease: EZ }, t);
        const lg = ab({ left: "0", right: "0", top: "170px", textAlign: "center" }, `<img src="assets/img/limo-logo-ad.png" alt="LIMO" style="height:150px" /><div style="margin-top:26px;font-family:Montserrat,sans-serif;font-weight:700;font-size:46px;color:#1b1f4b">Le tuto LIMO</div><div style="margin-top:16px;font-family:Inter,sans-serif;font-size:32px;color:#4f5378">8 gestes pour gagner des heures chaque semaine.</div>`);
        fin(lg, 0.4, 0.8, 20); fout(lg, T0 - 0.9, 0.5);
        tl.set(M.el, { opacity: 0, x: 875, y: 600, scale: 1.25 }, 0);
        tl.fromTo(M.el, { opacity: 0, y: 700 }, { opacity: 1, y: 600, duration: 0.8, ease: EO, immediateRender: false }, 1.2);
        M.wave(2.0); M.blink(3.2); M.expr("wink", 3.6, false); M.hop(4.2, 50); M.expr("happy", 4.6, false);
        at(T0 - 0.8, 1060, 300, 1, 0.8);
        M.float(T0, 8 * CHD - 0.5, 7);
        const EXP = ["happy", "wink", "wow", "think", "wow", "euro", "heart", "wink"];
        CH.forEach((c, i) => {
          at(tc(i) + 0.1, 1060, 300, 1, 0.6); M.hop(tc(i) + 0.7, 40); M.expr("happy", tc(i) + 0.1, false);
          [0, 1, 2].forEach((k) => {
            const t = ts(i, k);
            at(t - 0.1, 1070, SY[k] - 70, 1, 0.55);
            M.tilt(t + 0.5, 12, 0.3); M.tilt(t + 2.2, 0, 0.3);
            M.expr(k === 2 ? EXP[i] : (k ? "wink" : "think"), t + 0.3, false);
            if (k === 1) M.blink(t + 1.6);
          });
        });
        at(tc(8) - 0.2, 875, 840, 0.9, 0.7); M.expr("heart", tc(8) + 0.4, false);
        [0, 1, 2].forEach((k) => M.hop(tc(8) + 1.2 + k * 1.6, 40));

        // ── récap : les 12 agents
        const AG = [["target", "Détecteur de ventes", "Les diagnostics d’hier, les ventes de demain"], ["search", "Pige des particuliers", "Leurs annonces deviennent tes mandats"], ["pin", "Estimation & marché", "Cadastre, DVF, diagnostics"], ["pen", "Rédacteur d’annonce", "Optimisée, mentions incluses"],
          ["clip", "Analyseur de dossier", "Un PDF, la fiche remplie"], ["image", "Habilleur de photos", "Tes photos signées"], ["car", "Frais kilométriques", "Prêts pour le comptable"], ["magnet", "Matcheur acheteurs", "Le bon acheteur, tout de suite"],
          ["megaphone", "Diffuseur réseaux", "3 posts depuis un lien"], ["sofa", "Home staging virtuel", "Meubler, vider, repeindre"], ["wrench", "Mes artisans", "Le bon artisan, près du bien"], ["msg", "Messages Insta & Facebook", "Prospects repérés"]];
        const tr = tc(8);
        const rt = ab({ left: "0", right: "0", top: "60px", textAlign: "center" }, `<div class="ttl" style="font-size:64px">Et ce n’est qu’un début : <em>12 agents.</em></div>`);
        fin(rt, tr + 0.2, 0.7, 20); fout(rt, tr + 6.6);
        AG.forEach((a, i) => {
          const x = 140 + (i % 4) * 420, y = 210 + Math.floor(i / 4) * 190;
          const tE = ab({ left: x + "px", top: y + "px" }, `<div class="tile"><span class="ic">${K.icon(a[0])}</span><span><b>${a[1]}</b><small>${a[2]}</small></span></div>`);
          fin(tE, tr + 0.6 + i * 0.12, 0.5, 18); fout(tE, tr + 6.6);
        });
        K.sfx(tr + 0.6, "sparkle", 0.08);
        tl.to(M.el, { opacity: 0, duration: 0.4, ease: EZ }, tr + 6.5);

        // ── fin
        const te = tr + 7.0;
        const end = ab({ left: "0", right: "0", top: "150px", textAlign: "center" }, `<div class="ttl" style="font-size:88px">À toi de jouer.<br><em>LIMO fait le reste.</em></div><div style="margin-top:46px"><img src="assets/img/limo-logo-ad.png" alt="LIMO" style="height:120px" /></div><div style="margin-top:44px"><span class="cta" style="font-size:44px;padding:30px 56px">Essai gratuit 14 jours →</span></div><div style="margin-top:32px;font-family:Inter,sans-serif;font-size:36px;color:#4f5378">Sans engagement · dès 49 €/mois · <b style="color:#1b1f4b">app.leadengineai.fr</b></div>`);
        fin(end, te + 0.2, 0.8, 24);
        const M2 = N.mascot({ left: "1560px", top: "640px", width: "210px" }, { expr: "happy" });
        tl.set(M2.el, { opacity: 0 }, 0); tl.fromTo(M2.el, { opacity: 0, y: 60 }, { opacity: 1, y: 0, duration: 0.6, ease: EO, immediateRender: false }, te + 0.8);
        M2.wave(te + 1.4); M2.hop(te + 3.0, 50); M2.blink(te + 4.2); M2.expr("wink", te + 4.6, false);
        K.sfx(te + 0.3, "success", 0.1);
""".replace("__T0", str(T0)).replace("__CHD", str(CHD))

if __name__ == "__main__":
    shell = SHELL16.replace("    </style>", EXTRA, 1).replace("tout ce qu'il fait pour toi", "le tuto")
    html = shell.format(faces=FACES, dur=DUR, name=NAME, body=BODY.strip("\n"))
    (HERE.parent / "reels" / f"{NAME}.html").write_text(html, encoding="utf-8")
    print("reels/" + NAME + ".html", DUR)
