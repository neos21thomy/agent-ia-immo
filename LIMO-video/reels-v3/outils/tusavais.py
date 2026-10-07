"""Série « AGENT IMMO, TU SAVAIS ÇA ? » : 5 épisodes éducatifs (~40 s) pour les conseillers immobiliers.
Structure fixe et reconnaissable : accroche (badge + info choc) → 4 points utiles numérotés avec visuels (≈ 70 %)
→ « J'ai demandé à LIMO de me sortir l'info et de me l'expliquer » + conversation (≈ 20 %) → appel à l'action (≈ 10 %).
Informations générales vérifiées (à adapter à chaque dossier, mention en bas d'écran). Exemples chiffrés fictifs.

Usage : python3 outils/tusavais.py   (réécrit reels/tsc-0N-*.html)
"""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from cine import COMMON, FACES  # noqa: E402
from premium2 import SHELL  # noqa: E402
from premium3 import CSS  # noqa: E402

DUR = 40.5
T_LIMO, T_CTA = 28.0, 35.5
CSS_T = """
      .zbg { position: absolute; inset: 0; background: radial-gradient(ellipse at 50% 20%, #2a2466 0%, #14123a 55%, #0b0a24 100%); }
      .zgrid { position: absolute; inset: 0; background-image: linear-gradient(rgba(255,255,255,.045) 1px, transparent 1px), linear-gradient(90deg, rgba(255,255,255,.045) 1px, transparent 1px); background-size: 90px 90px; }
      .zbadge { display: inline-flex; align-items: center; gap: 14px; padding: 16px 30px; border-radius: 999px; background: #ffe066; color: #14123a; font-family: Montserrat, sans-serif; font-weight: 800; font-size: 34px; letter-spacing: .04em; box-shadow: 0 16px 40px rgba(255,224,102,.25); }
      .zbadge i { font-style: normal; padding: 4px 14px; border-radius: 999px; background: #14123a; color: #ffe066; font-size: 28px; }
      .zh { font-family: Montserrat, sans-serif; font-weight: 800; color: #fff; line-height: 1.08; letter-spacing: -.01em; }
      .zh em { font-style: normal; color: #ffe066; }
      .znum { display: inline-flex; align-items: center; justify-content: center; width: 84px; height: 84px; border-radius: 24px; background: #6b4fe0; color: #fff; font-family: Montserrat, sans-serif; font-weight: 800; font-size: 46px; box-shadow: 0 14px 30px rgba(107,79,224,.45); }
      .zt { font-family: Montserrat, sans-serif; font-weight: 800; font-size: 66px; line-height: 1.1; color: #fff; }
      .zt em { font-style: normal; color: #ffe066; }
      .zb { font-family: Inter, sans-serif; font-size: 43px; line-height: 1.38; color: rgba(255,255,255,.88); }
      .zb b { color: #fff; } .zb em { font-style: normal; color: #ffe066; font-weight: 700; }
      .zc { border-radius: 34px; background: #ffffff; color: #1b1f4b; font-family: Inter, sans-serif; box-shadow: 0 40px 80px rgba(0,0,0,.35); }
      .zchip { display: inline-flex; align-items: center; gap: 10px; padding: 14px 24px; border-radius: 999px; background: rgba(255,255,255,.12); border: 2px solid rgba(255,255,255,.25); color: #fff; font-family: Inter, sans-serif; font-weight: 600; font-size: 34px; margin: 8px; }
      .zfoot { font-family: Inter, sans-serif; font-size: 25px; color: rgba(255,255,255,.55); text-align: center; }
      .zq { align-self: flex-end; max-width: 84%; padding: 24px 30px; border-radius: 34px 34px 10px 34px; background: #6b4fe0; color: #fff; font-family: Inter, sans-serif; font-size: 40px; line-height: 1.3; }
      .za { align-self: flex-start; max-width: 96%; padding: 28px 32px; border-radius: 34px 34px 34px 10px; background: #fff; color: #1b1f4b; font-family: Inter, sans-serif; font-size: 39px; line-height: 1.42; box-shadow: 0 30px 60px rgba(0,0,0,.3); }
      .za .zl { display: block; } .za b { color: #5b3fd6; }
      .zdots { align-self: flex-start; display: flex; gap: 10px; padding: 24px 28px; border-radius: 34px; background: #fff; }
      .zdots i { width: 15px; height: 15px; border-radius: 50%; background: #9a9cb5; display: block; }
"""

HELP = r"""
        tl.set([C.barT, C.barB], { opacity: 0 }, 0);
        const TOP = document.getElementById("root");
        const EO = "expo.out", EZ = "power2.inOut", BK = "back.out(1.5)";
        const zab = (css, html = "", p = TOP) => FX.ab(p, css, html);
        const zin = (e, t, o = {}) => { tl.set(e, { opacity: 0 }, 0); tl.fromTo(e, { opacity: 0, y: o.y ?? 40, scale: o.s ?? 1 }, { opacity: 1, y: 0, scale: 1, duration: o.d ?? 0.55, ease: o.e || EO, immediateRender: false }, t); };
        const zout = (e, t) => tl.to(e, { opacity: 0, y: -30, duration: 0.3, ease: "power2.in" }, t);
        // fond : dégradé nuit + grille qui dérive + halos
        zab({ inset: "0" }, `<div class="zbg"></div>`);
        const grid = zab({ left: "-90px", top: "-90px", width: "1260px", height: "2100px" }, `<div class="zgrid"></div>`);
        tl.fromTo(grid, { x: 0, y: 0 }, { x: 90, y: 90, duration: DUR, ease: "none" }, 0);
        FX.aurora(zab({ inset: "0" }), 0, DUR, { colors: ["#6b4fe0", "#2cc4b5", "#3a2a9a"], a: 0.28 });
        // badge de série, permanent
        const badge = zab({ left: "0", right: "0", top: "120px", textAlign: "center", zIndex: 30 }, `<span class="zbadge">AGENT IMMO, TU SAVAIS ÇA ? <i>#${EP.n}</i></span>`);
        zin(badge, 0.15, { y: -30, s: 0.9, e: BK });
        // barre de progression
        const prog = zab({ left: "60px", right: "60px", top: "70px", height: "8px", borderRadius: "6px", background: "rgba(255,255,255,.15)", overflow: "hidden", zIndex: 30 }, `<div class="pf" style="width:100%;height:100%;background:#ffe066;transform-origin:0 50%"></div>`);
        tl.set(K.$(".pf", prog), { scaleX: 0 }, 0); tl.to(K.$(".pf", prog), { scaleX: 1, duration: DUR - 0.2, ease: "none" }, 0);
        // mention en bas
        const foot = zab({ left: "60px", right: "60px", top: "1700px", zIndex: 30 }, `<div class="zfoot">${EP.foot || "Info générale, à vérifier selon ton dossier. Exemples fictifs."}</div>`);
        zin(foot, 4.2, { y: 10 }); tl.to(foot, { opacity: 0, duration: 0.3 }, __TCTA);

        // ── accroche
        const hk = zab({ left: "70px", right: "70px", top: "560px", textAlign: "center", zIndex: 20 }, `<div class="zh" style="font-size:${EP.hookFs || 92}px">${EP.hook}</div>`);
        zin(hk, 0.5, { y: 80, s: 1.08 }); K.sfx(0.5, "whoosh", 0.25, 0, { d: 0.4, f0: 300, f1: 2600, pk: 0.4 });
        tl.fromTo(hk, { scale: 1 }, { scale: 1.04, duration: 3.2, ease: "none", immediateRender: false }, 1.0);
        K.sfx(0.2, "thump", 0.3);
        zout(hk, 3.7);
        const hv = zab({ left: "0", right: "0", top: "1180px", textAlign: "center", zIndex: 19 }, EP.hookVis || "");
        zin(hv, 1.4, { y: 60, e: BK }); zout(hv, 3.7);

        // ── les 4 points
        EP.points.forEach((p, i) => {
          const t0 = 4.0 + i * 6.0, t1 = t0 + 6.0;
          const head = zab({ left: "70px", right: "70px", top: "290px", zIndex: 20 }, `<div style="display:flex;gap:28px;align-items:flex-start"><span class="znum">${i + 1}</span><div class="zt" style="flex:1">${p.t}</div></div><div class="zb" style="margin-top:26px">${p.b}</div>`);
          const num = K.$(".znum", head), tt = K.$(".zt", head), bb = K.$(".zb", head);
          tl.set(head, { opacity: 0 }, 0); tl.set(head, { opacity: 1 }, t0);
          zin(num, t0, { y: 0, s: 0.3, e: "back.out(2.5)", d: 0.45 }); zin(tt, t0 + 0.12, { y: 30 }); zin(bb, t0 + 0.55, { y: 20 });
          K.sfx(t0, "pop", 0.18, 0, { f: 900 });
          zout(head, t1 - 0.32);
          const vis = zab({ left: "0", right: "0", top: (p.vt || 900) + "px", textAlign: "center", zIndex: 18 }, `<div style="transform:scale(1.16);transform-origin:50% 0">${p.v}</div>`);
          zin(vis, t0 + 0.9, { y: 60, e: BK, d: 0.6 });
          K.$$(".zs", vis).forEach((e, k) => { zin(e, t0 + 1.4 + k * 0.35, { y: 20, s: 0.9, e: BK, d: 0.4 }); K.sfx(t0 + 1.4 + k * 0.35, "tick", 0.08, 0, { f: 2200 }); });
          K.$$(".zcount", vis).forEach((e) => K.count(e, parseFloat(e.dataset.to), t0 + 1.4, 1.4, (v) => Math.round(v).toLocaleString("fr-FR").replace(/ /g, " ") + (e.dataset.suf || ""), {}));
          K.$$(".zstrike", vis).forEach((e) => { tl.set(e, { scaleX: 0, transformOrigin: "0 50%" }, 0); tl.to(e, { scaleX: 1, duration: 0.35, ease: EO }, t0 + 2.6); K.sfx(t0 + 2.6, "swipe", 0.2); });
          zout(vis, t1 - 0.32);
          if (p.extra) p.extra(vis, t0);
        });

        // ── démonstration LIMO
        const ld = zab({ left: "70px", right: "70px", top: "260px", textAlign: "center", zIndex: 20 }, `<div class="zt" style="font-size:60px">J’ai demandé à <em>LIMO</em> de me sortir l’info<br>et de me l’expliquer :</div>`);
        zin(ld, __TLIMO + 0.1, { y: 30 }); zout(ld, __TCTA - 0.3);
        const chat = zab({ left: "50px", right: "50px", top: "600px", zIndex: 20, display: "flex", flexDirection: "column", gap: "22px" }, `<div class="zq">${EP.q}</div><div class="zdots"><i></i><i></i><i></i></div><div class="za"><span style="display:flex;align-items:center;gap:12px;font-weight:700;color:#6b4fe0;font-size:26px;margin-bottom:8px"><img src="assets/img/limo-house-ad.png" alt="" style="height:38px" />LIMO</span>${EP.a.map((l) => `<span class="zl">${l}</span>`).join("")}</div>`);
        const q = K.$(".zq", chat), dots = K.$(".zdots", chat), an = K.$(".za", chat);
        zin(q, __TLIMO + 0.9, { y: 30, e: BK }); K.sfx(__TLIMO + 0.9, "send", 0.3);
        tl.set(dots, { display: "none" }, 0); tl.set(dots, { display: "flex" }, __TLIMO + 1.6); tl.set(dots, { display: "none" }, __TLIMO + 2.6);
        K.$$("i", dots).forEach((d, k) => tl.fromTo(d, { opacity: 0.3 }, { opacity: 1, duration: 0.25, yoyo: true, repeat: 3, ease: "sine.inOut", immediateRender: false }, __TLIMO + 1.6 + k * 0.12));
        tl.set(an, { display: "none" }, 0); tl.set(an, { display: "block" }, __TLIMO + 2.6);
        zin(an, __TLIMO + 2.6, { y: 30, e: BK }); K.sfx(__TLIMO + 2.6, "receive", 0.3);
        K.$$(".zl", an).forEach((l, k) => zin(l, __TLIMO + 2.9 + k * 0.45, { y: 12, d: 0.35 }));
        zout(chat, __TCTA - 0.3);

        // ── appel à l'action
        const cta = zab({ left: "0", right: "0", top: "520px", textAlign: "center", zIndex: 20 }, `<div style="display:inline-block;padding:34px 60px;border-radius:40px;background:#fff"><img src="assets/img/limo-logo-ad.png" alt="LIMO" style="height:120px" /></div><div class="zt" style="margin-top:40px;font-size:56px">Le bras droit<br>du <em>conseiller immo.</em></div><div style="margin-top:50px"><span style="display:inline-block;padding:28px 54px;border-radius:999px;background:#ffe066;color:#14123a;font-family:Montserrat,sans-serif;font-weight:800;font-size:46px">Essai gratuit 14 jours</span></div><div class="zb" style="margin-top:24px;font-size:34px">Sans engagement · lien en bio</div><div class="zb" style="margin-top:70px;font-size:34px">Épisode suivant : <b>${EP.next}</b><br>Abonne-toi pour ne pas le rater 🔔</div>`);
        zin(cta, __TCTA, { y: 60, s: 0.95 }); K.sfx(__TCTA, "success", 0.2);
        window.__TE = __TCTA;
""".replace("__TLIMO", str(T_LIMO)).replace("__TCTA", str(T_CTA))

# visuels réutilisables (HTML)
def card(inner, w=900, pad="34px 40px"):
    return f'<div class="zc" style="display:inline-block;width:{w}px;padding:{pad};text-align:left">{inner}</div>'

def chips(items):
    return '<div style="max-width:960px;margin:0 auto">' + "".join(f'<span class="zchip zs">{x}</span>' for x in items) + "</div>"

def rows(items, w=900):
    return card("".join(f'<div class="zs" style="display:flex;align-items:center;gap:18px;padding:16px 0;border-top:{"0" if i == 0 else "1px solid #ecebf5"};font-size:34px"><span style="flex:none;width:52px;height:52px;border-radius:50%;background:{c};color:#fff;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:28px">{ic}</span><span>{tx}</span></div>' for i, (ic, c, tx) in enumerate(items)), w, "18px 34px")

EPS = {}

# ── 1 · Estimation : les ventes réelles (DVF)
pins = "".join(f'<div class="zs" style="position:absolute;left:{x}px;top:{y}px;padding:10px 16px;border-radius:14px;background:#6b4fe0;color:#fff;font-weight:800;font-size:26px;white-space:nowrap;box-shadow:0 8px 18px rgba(0,0,0,.25)">{p}</div>' for x, y, p in [(70, 60, "248 000 €"), (470, 120, "255 000 €"), (210, 300, "262 000 €"), (560, 360, "231 000 €")])
EPS["tsc-01-ventes-reelles-dvf"] = dict(n=1, next="Honoraires charge acquéreur ou vendeur",
    hook="Tu peux voir les <em>ventes réelles</em> signées autour d’une maison.<br><em>Gratuitement.</em>",
    hookVis=card('<div style="display:flex;align-items:center;gap:20px;font-size:36px;font-weight:700">🏛️ <span>Données publiques de l’État</span></div>', 760),
    points=[
        dict(t="C’est la base <em>DVF</em> de l’État", b="« Demandes de valeurs foncières » : les ventes enregistrées par l’administration fiscale, en <em>open data</em>.",
             v=card('<div style="font-size:30px;color:#6e6e80">Cherche</div><div style="font-family:Montserrat,sans-serif;font-weight:800;font-size:54px;margin-top:6px">DVF · data.gouv.fr</div><div style="margin-top:14px;font-size:30px;color:#6e6e80">Gratuit · sans inscription</div>', 760)),
        dict(t="Ce que tu y vois, <em>vente par vente</em>", b="", vt=520,
             v=chips(["💶 Prix de vente", "📅 Date", "📐 Surface bâtie", "🚪 Pièces", "🌳 Terrain", "🏠 Maison / appart"]) + '<div style="height:30px"></div>' + card(f'<div style="position:relative;height:460px;border-radius:24px;background:#eef0f7;overflow:hidden"><svg width="100%" height="100%" viewBox="0 0 820 460" style="position:absolute;inset:0"><path d="M0 140 C200 100 400 200 820 150" stroke="#fff" stroke-width="30" fill="none"/><path d="M300 0 C330 160 260 300 340 460" stroke="#fff" stroke-width="22" fill="none"/></svg>{pins}</div>', 900, "18px")),
        dict(t="5 ans d’historique, <em>mis à jour 2 fois par an</em>", b="Partout en France, <b>sauf</b> Alsace, Moselle et Mayotte.",
             v=card('<div style="display:flex;justify-content:space-between;align-items:center;font-family:Montserrat,sans-serif;font-weight:800;font-size:40px">' + "".join(f'<span class="zs" style="display:flex;flex-direction:column;align-items:center;gap:10px"><span style="width:26px;height:26px;border-radius:50%;background:#6b4fe0"></span>{y}</span>' for y in ["2021", "2022", "2023", "2024", "2025"]) + "</div>", 880)),
        dict(t="Ton arme en <em>RDV vendeur</em>", b="Le vendeur croit les prix des annonces. Toi, tu lui montres les prix <b>réellement signés</b>.",
             v=card('<div style="font-size:30px;color:#6e6e80">Annonce du voisin</div><div style="position:relative;display:inline-block;font-family:Montserrat,sans-serif;font-weight:800;font-size:64px;color:#c0282d">320 000 €<span class="zstrike" style="position:absolute;left:-6px;right:-6px;top:50%;height:8px;background:#c0282d;border-radius:4px"></span></div><div style="margin-top:22px;font-size:30px;color:#6e6e80">Vendue réellement (DVF)</div><div style="font-family:Montserrat,sans-serif;font-weight:800;font-size:72px;color:#15877d">262 000 €</div>', 760)),
    ],
    q="Ventes réelles autour du 12 rue des Tilleuls à Allassac ?",
    a=["<b>3 ventes</b> à moins de 500 m sur 24 mois :", "• 248 000 € · 110 m² · mars 2026", "• 255 000 € · 118 m² · nov. 2025", "• 262 000 € · 121 m² · juin 2025", "→ ≈ <b>2 200 €/m²</b> · fourchette conseillée <b>248–262 k€</b>"])

# ── 2 · Honoraires charge acquéreur / vendeur
EPS["tsc-02-honoraires-acquereur-vendeur"] = dict(n=2, next="Il manque une pièce au compromis",
    hook="Honoraires à la charge de <em>l’acquéreur</em> ou du <em>vendeur</em> :<br>tu sais vraiment ce que ça change ?", hookFs=84,
    hookVis=card('<div style="display:flex;justify-content:space-around;font-family:Montserrat,sans-serif;font-weight:800;font-size:44px"><span>👤 Acquéreur</span><span style="color:#9a9cb5">vs</span><span>🏠 Vendeur</span></div>', 820),
    points=[
        dict(t="Pour le vendeur : <em>rien</em> sur son net", b="Dans les deux cas, il touche le <b>même net vendeur</b>.",
             v=card('<div style="display:flex;gap:30px;text-align:center"><div class="zs" style="flex:1"><div style="font-size:28px;color:#6e6e80">Charge acquéreur</div><div style="font-family:Montserrat,sans-serif;font-weight:800;font-size:54px;margin-top:8px">250 000 €</div><div style="font-size:26px;color:#15877d;font-weight:700">net vendeur</div></div><div class="zs" style="flex:1"><div style="font-size:28px;color:#6e6e80">Charge vendeur</div><div style="font-family:Montserrat,sans-serif;font-weight:800;font-size:54px;margin-top:8px">250 000 €</div><div style="font-size:26px;color:#15877d;font-weight:700">net vendeur</div></div></div>', 900)),
        dict(t="Pour l’acquéreur : les <em>frais de notaire</em>", b="Charge acquéreur : les honoraires <b>sortent de la base</b> des droits de mutation.",
             v=card('<div class="zs" style="display:flex;justify-content:space-between;font-size:32px;padding:10px 0"><span>Base 262 500 € (honoraires inclus)</span><b>≈ 19 690 €</b></div><div class="zs" style="display:flex;justify-content:space-between;font-size:32px;padding:10px 0;border-top:1px solid #ecebf5"><span>Base 250 000 € (hors honoraires)</span><b>≈ 18 750 €</b></div><div class="zs" style="margin-top:14px;padding:18px;border-radius:20px;background:#e2f7f4;color:#0a5a52;font-family:Montserrat,sans-serif;font-weight:800;font-size:44px;text-align:center">≈ <span class="zcount" data-to="940" data-suf=" €">0 €</span> d’économie</div><div style="margin-top:10px;font-size:24px;color:#6e6e80">Frais ≈ 7,5 % dans l’ancien · exemple simplifié</div>', 900)),
        dict(t="Dans l’annonce, <em>l’affichage change</em>", b="Charge acquéreur : prix <b>honoraires inclus</b>, prix <b>hors honoraires</b> et le <b>%</b> d’honoraires.",
             v=card('<div style="font-family:Montserrat,sans-serif;font-weight:800;font-size:56px">262 500 € <span style="font-size:32px;color:#6e6e80">HAI</span></div><div class="zs" style="font-size:32px;margin-top:10px">250 000 € hors honoraires</div><div class="zs" style="font-size:32px;margin-top:6px">Honoraires : <b>5 % TTC</b> à la charge de l’acquéreur</div>', 880)),
        dict(t="Noir sur blanc : <em>mandat</em> puis <em>compromis</em>", b="Qui paie doit être écrit dans le mandat, puis repris à l’identique dans l’avant-contrat.",
             v=rows([("1", "#6b4fe0", "Mandat : honoraires et qui les paie"), ("2", "#6b4fe0", "Annonce : affichage conforme"), ("3", "#2cc4b5", "Compromis : même mention")])),
    ],
    q="Bien à 250 000 € net vendeur, 5 % d’honoraires : charge acquéreur ou vendeur ?",
    a=["<b>Charge acquéreur</b> : 262 500 € HAI.", "Frais de notaire calculés sur 250 000 € → ≈ <b>940 € d’économie</b> pour l’acheteur.", "Mention d’annonce prête :", "« 262 500 € HAI · 250 000 € HH · 5 % TTC charge acquéreur »"])

# ── 3 · Pièce manquante au compromis
EPS["tsc-03-piece-manquante-compromis"] = dict(n=3, next="3 sites gratuits avant de rentrer un terrain",
    hook="Il manque <em>une pièce</em> au compromis…<br>tu sais ce que ça déclenche ?",
    hookVis=card('<div style="display:flex;align-items:center;gap:20px;font-size:36px;font-weight:700"><span style="color:#c0282d">✖</span> Compromis · pièce manquante</div>', 760),
    points=[
        dict(t="Copro : le délai de rétractation <em>ne démarre pas</em>", b="Sans les documents obligatoires (règlement, PV d’AG, fiche synthétique…), les <b>10 jours</b> ne courent qu’à partir de leur remise.",
             v=card('<div style="display:flex;gap:10px;justify-content:center;flex-wrap:wrap">' + "".join(f'<span class="zs" style="width:66px;height:66px;border-radius:16px;background:{"#efeafe" if i else "#ffe8e8"};display:flex;align-items:center;justify-content:center;font-weight:800;font-size:28px;color:{"#6b4fe0" if i else "#c0282d"}">{"⏸" if i == 0 else i}</span>' for i in range(11)) + '</div><div style="margin-top:16px;text-align:center;font-size:30px;color:#6e6e80">Le compteur reste à zéro</div>', 900)),
        dict(t="Diagnostic absent = <em>vices cachés</em>", b="Le vendeur ne peut plus s’exonérer de la garantie des vices cachés sur ce point (amiante, termites, électricité…).",
             v=rows([("✓", "#2cc4b5", "DPE"), ("✓", "#2cc4b5", "Électricité · gaz"), ("✖", "#e5484d", "Termites : absent"), ("✓", "#2cc4b5", "Amiante · plomb")])),
        dict(t="État des risques <em>absent</em>", b="L’acquéreur peut demander <b>l’annulation</b> de la vente ou une <b>baisse du prix</b>.",
             v=card('<div style="display:flex;align-items:center;gap:22px"><span style="flex:none;width:90px;height:90px;border-radius:24px;background:#fff2dc;display:flex;align-items:center;justify-content:center;font-size:52px">⚠️</span><div><div style="font-family:Montserrat,sans-serif;font-weight:800;font-size:42px">ERP manquant</div><div class="zs" style="font-size:30px;color:#6e6e80;margin-top:6px">Résolution ou diminution du prix</div></div></div>', 860)),
        dict(t="Le réflexe : <em>check-list avant</em> la signature", b="Pas le jour J. Une pièce qui manque, c’est un dossier fragile.",
             v=rows([("✓", "#2cc4b5", "Diagnostics complets et à jour"), ("✓", "#2cc4b5", "ERP de moins de 6 mois"), ("✓", "#2cc4b5", "Documents de copropriété"), ("✓", "#2cc4b5", "Titre de propriété")])),
    ],
    q="Vérifie mon dossier de compromis · appartement Brive",
    a=["✅ DPE, électricité, gaz, amiante, plomb", "✅ Titre de propriété", "⚠️ <b>ERP daté de 8 mois</b> → à refaire (moins de 6 mois)", "❌ <b>PV d’AG 2025 manquant</b> → à demander au syndic"])

# ── 4 · Urbanisme et cadastre
EPS["tsc-04-urbanisme-cadastre"] = dict(n=4, next="Maison classée F ou G : l’audit énergétique",
    hook="Avant de rentrer un terrain :<br><em>3 sites gratuits</em> que tout agent immo devrait connaître.", hookFs=84,
    hookVis=chips(["🗺️ Cadastre", "🏗️ PLU", "⚠️ Risques"]),
    points=[
        dict(t="<em>cadastre.gouv.fr</em>", b="Parcelle, surface, plan. ⚠️ Le cadastre <b>ne fait pas foi</b> pour les limites : seul un <b>bornage</b> par géomètre-expert.",
             v=card('<svg viewBox="0 0 820 380" width="820" height="380"><rect width="820" height="380" rx="20" fill="#f4f1e8"/><path d="M60 60 L380 40 L420 300 L80 330 Z" fill="#e7f6ef" stroke="#2cc4b5" stroke-width="6"/><path d="M380 40 L760 70 L740 320 L420 300 Z" fill="#fff" stroke="#9a9cb5" stroke-width="4"/><text x="230" y="200" font-family="Montserrat" font-weight="800" font-size="44" fill="#15877d" text-anchor="middle">AB 123</text><text x="230" y="250" font-family="Inter" font-size="30" fill="#4f5378" text-anchor="middle">1 250 m²</text><text x="590" y="200" font-family="Montserrat" font-weight="800" font-size="36" fill="#9a9cb5" text-anchor="middle">AB 124</text></svg>', 880, "18px")),
        dict(t="<em>Géoportail de l’Urbanisme</em>", b="La zone du PLU : <b>U</b> urbaine · <b>AU</b> à urbaniser · <b>A</b> agricole · <b>N</b> naturelle. En A ou N, construire est très limité.",
             v=card('<div style="display:grid;grid-template-columns:1fr 1fr;gap:16px">' + "".join(f'<div class="zs" style="padding:22px;border-radius:20px;background:{bg};font-size:32px"><b style="font-family:Montserrat,sans-serif;font-size:46px;color:{c}">{z}</b><br>{lab}</div>' for z, lab, bg, c in [("U", "Urbaine", "#ffe8e8", "#c0282d"), ("AU", "À urbaniser", "#fff2dc", "#a35f00"), ("A", "Agricole", "#e9f7e4", "#3a7d2a"), ("N", "Naturelle", "#e2f7f4", "#0a5a52")]) + "</div>", 880, "22px")),
        dict(t="<em>Géorisques</em>", b="Inondation, argiles, radon… En zone argileuse <b>moyenne ou forte</b>, une <b>étude de sol</b> est obligatoire pour vendre un terrain constructible.",
             v=chips(["🌊 Inondation", "🧱 Argiles", "☢️ Radon", "🌍 Séisme"])),
        dict(t="Le bonus : le <em>certificat d’urbanisme</em>", b="Gratuit, demandé en mairie. Le CU d’information : réponse sous <b>1 mois</b>.",
             v=card('<div style="display:flex;align-items:center;gap:22px"><span style="flex:none;width:90px;height:90px;border-radius:24px;background:#efeafe;display:flex;align-items:center;justify-content:center;font-size:52px">📄</span><div><div style="font-family:Montserrat,sans-serif;font-weight:800;font-size:42px">CU d’information</div><div class="zs" style="font-size:30px;color:#6e6e80;margin-top:6px">Gratuit · réponse sous 1 mois</div></div></div>', 860)),
    ],
    q="Parcelle AB 123 à Voutezac : constructible ?",
    a=["Zone <b>UB</b> du PLU (urbaine) · <b>1 250 m²</b>", "Aléa argile <b>moyen</b> → étude de sol à prévoir pour la vente", "Hors zone inondable", "→ Prochaine étape : <b>CU d’information</b> en mairie"])

# ── 5 · Technique : DPE et audit énergétique
dpe = '<div style="display:flex;flex-direction:column;gap:8px">' + "".join(f'<div class="zs" style="width:{240 + i * 80}px;padding:8px 20px;border-radius:0 30px 30px 0;background:{c};color:#fff;font-family:Montserrat,sans-serif;font-weight:800;font-size:34px;display:flex;justify-content:space-between"><span>{l}</span><span style="font-size:24px">{m}</span></div>' for i, (l, c, m) in enumerate([("A", "#2e9e5b", ""), ("B", "#5bb55b", ""), ("C", "#a6cf4f", ""), ("D", "#f2d33a", "audit 2034"), ("E", "#f0a43a", "audit 2025"), ("F", "#e8703a", "audit 2023"), ("G", "#d6362f", "audit 2023")])) + "</div>"
EPS["tsc-05-audit-energetique"] = dict(n=5, next="Prospection : repérer les vendeurs avant les autres",
    hook="Maison classée <em>F ou G</em> à vendre ?<br>Il te manque peut-être un <em>document obligatoire.</em>",
    hookVis=card('<div style="display:flex;gap:14px;justify-content:center"><span style="padding:10px 26px;border-radius:14px;background:#e8703a;color:#fff;font-family:Montserrat,sans-serif;font-weight:800;font-size:54px">F</span><span style="padding:10px 26px;border-radius:14px;background:#d6362f;color:#fff;font-family:Montserrat,sans-serif;font-weight:800;font-size:54px">G</span></div>', 420),
    points=[
        dict(t="L’<em>audit énergétique</em>", b="Obligatoire pour vendre une maison (ou un immeuble en monopropriété) classée <b>F ou G</b> depuis 2023, <b>E</b> depuis 2025, <b>D</b> en 2034.", vt=860, v=card(dpe, 760, "26px")),
        dict(t="Valable <em>5 ans</em>, remis <em>dès la 1re visite</em>", b="Il doit être fourni à l’acquéreur dès la première visite, puis annexé à la promesse.",
             v=rows([("1", "#6b4fe0", "Mandat : vérifier la classe DPE"), ("2", "#6b4fe0", "F, G ou E : commander l’audit"), ("3", "#2cc4b5", "Le remettre dès la 1re visite")])),
        dict(t="Les vieux DPE <em>ne valent plus rien</em>", b="Les DPE réalisés <b>avant le 1er juillet 2021</b> ne sont plus valables depuis le <b>1er janvier 2025</b>.",
             v=card('<div style="font-size:30px;color:#6e6e80">DPE de 2019</div><div style="position:relative;display:inline-block;font-family:Montserrat,sans-serif;font-weight:800;font-size:60px;color:#c0282d">Valable ?<span class="zstrike" style="position:absolute;left:-6px;right:-6px;top:50%;height:8px;background:#c0282d;border-radius:4px"></span></div><div style="margin-top:16px;font-family:Montserrat,sans-serif;font-weight:800;font-size:46px;color:#15877d">→ à refaire</div>', 720)),
        dict(t="Côté <em>investisseur</em>", b="En location : logements <b>G</b> exclus depuis 2025, <b>F</b> en 2028, <b>E</b> en 2034. Un argument de prix… dans les deux sens.",
             v=card('<div style="display:flex;justify-content:space-around;text-align:center;font-family:Montserrat,sans-serif;font-weight:800">' + "".join(f'<div class="zs"><div style="font-size:30px;color:#6e6e80">{y}</div><div style="margin-top:8px;padding:8px 26px;border-radius:14px;background:{c};color:#fff;font-size:50px">{l}</div></div>' for y, l, c in [("2025", "G", "#d6362f"), ("2028", "F", "#e8703a"), ("2034", "E", "#f0a43a")]) + "</div>", 820)),
    ],
    q="Que dois-je fournir pour la maison classée F de M. Bernard ?",
    a=["<b>Audit énergétique obligatoire</b> (valable 5 ans), à remettre dès la 1re visite", "DPE de 2019 → <b>plus valable</b>, à refaire", "Investisseur : louable jusqu’en <b>2028</b> sans travaux"])

if __name__ == "__main__":
    for name, ep in EPS.items():
        pts = [{k: v for k, v in p.items()} for p in ep["points"]]
        epj = dict(ep, points=pts)
        body = "        const DUR = " + str(DUR) + ";\n        const EP = " + json.dumps(epj, ensure_ascii=False) + ";\n" + HELP
        html = SHELL.format(title=name, faces=FACES, css=(CSS + CSS_T).strip("\n"), body=(COMMON + body).strip("\n"), dur=DUR, name=name)
        (HERE.parent / "reels" / f"{name}.html").write_text(html, encoding="utf-8")
        print("reels/" + name + ".html")
