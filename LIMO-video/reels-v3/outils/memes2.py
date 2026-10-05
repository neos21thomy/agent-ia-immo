"""Série « C'est tellement moi » V2 : 100 % conversations iPhone (le format que Thomy a aimé), avec musique.
Retours de Thomy sur la V1 : enlever les plans qui font « IA » (conseiller au bureau, selfie, maison générée), garder
les messages, ajouter de la musique, faire plus beau.
Chaque film : le message du client (la galère) → « Ce que j'ai envie de répondre : » (brouillon tapé puis effacé)
→ « Ce que LIMO m'a préparé : » (suggestion au-dessus du clavier, un tap, envoyé) → le client répond, ravi → chute → fin.
Données affichées = exemples fictifs.

Usage : python3 outils/memes2.py   (réécrit reels/meme2-*.html)
"""
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from cine import COMMON, FACES  # noqa: E402
from premium2 import SHELL  # noqa: E402
from premium3 import CSS  # noqa: E402
from premium4 import SH4  # noqa: E402

DUR = 16.4
CSS_M = """
      .ig { display: inline; padding: 6px 18px; line-height: 1.6; border-radius: 12px; background: rgba(0,0,0,.78); color: #fff; font-family: Inter, sans-serif; font-weight: 700; font-size: 46px; -webkit-box-decoration-break: clone; box-decoration-break: clone; }
      .ig.w { background: #6b4fe0; }
      .xch { position: absolute; inset: 0; background: #fff; font-family: Inter, sans-serif; overflow: hidden; }
      .xch .xhd { z-index: 5; position: absolute; left: 0; right: 0; top: 0; height: 330px; background: #f6f6f8; border-bottom: 1px solid #e0e0e6; display: flex; flex-direction: column; align-items: center; justify-content: flex-end; padding-bottom: 22px; }
      .xch .xst { position: absolute; left: 70px; right: 60px; top: 30px; display: flex; justify-content: space-between; font-size: 34px; font-weight: 600; color: #111; }
      .xch .xbk { position: absolute; left: 40px; top: 170px; font-size: 60px; color: #0a84ff; }
      .xch .xav { width: 120px; height: 120px; border-radius: 50%; background: linear-gradient(160deg,#a9afbd,#7f8596); color: #fff; display: flex; align-items: center; justify-content: center; font-size: 46px; font-weight: 600; }
      .xch .xnm { margin-top: 10px; font-size: 30px; font-weight: 500; color: #111; }
      .xch .xlst { position: absolute; left: 36px; right: 36px; top: 500px; display: flex; flex-direction: column; gap: 12px; }
      .xch .xtm { text-align: center; font-size: 24px; color: #8a8a90; margin-bottom: 8px; }
      .xbb { position: relative; max-width: 80%; padding: 20px 28px; border-radius: 38px; font-size: 37px; line-height: 1.3; }
      .xbb.xin { align-self: flex-start; background: #e9e9eb; color: #111; border-bottom-left-radius: 10px; }
      .xbb.xout { align-self: flex-end; background: #0a84ff; color: #fff; border-bottom-right-radius: 10px; }
      .xbb .xtb { position: absolute; top: -34px; width: 62px; height: 62px; border-radius: 50%; background: #e9e9eb; border: 4px solid #fff; display: flex; align-items: center; justify-content: center; font-size: 32px; }
      .xbb.xout .xtb { left: -30px; } .xbb.xin .xtb { right: -30px; background: #0a84ff; }
      .xlu { align-self: flex-end; font-size: 23px; color: #8a8a90; margin-top: -4px; }
      .xatt { display: flex; align-items: center; gap: 18px; }
      .xatt i { flex: none; width: 70px; height: 84px; border-radius: 10px; background: #fff; color: #e5484d; font-style: normal; font-weight: 800; font-size: 22px; display: flex; align-items: flex-end; justify-content: center; padding-bottom: 8px; }
      .xdt { align-self: flex-start; display: flex; gap: 9px; padding: 24px 28px; border-radius: 38px; background: #e9e9eb; }
      .xdt i { width: 15px; height: 15px; border-radius: 50%; background: #9a9aa0; display: block; }
      .xkb { position: absolute; left: 0; right: 0; bottom: 0; height: 760px; }
      .xkb .xbar { position: absolute; left: 0; right: 0; top: 0; height: 120px; background: #fff; display: flex; align-items: center; gap: 18px; padding: 0 30px; }
      .xkb .xpl { flex: none; width: 70px; height: 70px; border-radius: 50%; background: #e9e9eb; color: #8a8a90; display: flex; align-items: center; justify-content: center; font-size: 46px; }
      .xkb .xin { flex: 1; min-height: 76px; border: 2px solid #d6d6dc; border-radius: 40px; padding: 14px 26px; font-size: 34px; color: #111; display: flex; align-items: center; }
      .xkb .xin .xph { color: #a0a0a6; }
      .xkb .xkeys { position: absolute; left: 0; right: 0; top: 120px; bottom: 0; background: #d3d5db; padding: 22px 8px 0; display: flex; flex-direction: column; gap: 22px; }
      .xkb .xr { display: flex; justify-content: center; gap: 12px; }
      .xkb .xr span { width: 92px; height: 104px; border-radius: 12px; background: #fff; box-shadow: 0 2px 0 #9ea1a8; display: flex; align-items: center; justify-content: center; font-size: 42px; color: #111; }
      .xkb .xr span.xw { width: 520px; font-size: 32px; color: #333; } .xkb .xr span.xg { background: #adb1ba; width: 140px; font-size: 30px; }
      .xsg { position: absolute; left: 30px; right: 30px; padding: 22px 26px; border-radius: 30px; background: #f3effe; border: 3px solid #6b4fe0; box-shadow: 0 18px 40px rgba(107,79,224,.25); font-family: Inter, sans-serif; color: #1b1f4b; }
      .xsg .xlg { display: flex; align-items: center; gap: 12px; font-size: 25px; font-weight: 700; color: #6b4fe0; margin-bottom: 10px; }
      .xsg .xlg img { height: 40px; }
      .xsg p { font-size: 33px; line-height: 1.32; margin: 0; }
      .xtap { position: absolute; width: 90px; height: 90px; margin: -45px 0 0 -45px; border-radius: 50%; background: rgba(10,132,255,.25); border: 4px solid rgba(10,132,255,.6); z-index: 50; }
      .xbn { position: absolute; left: 24px; right: 24px; top: 24px; display: flex; gap: 20px; align-items: center; padding: 24px 26px; border-radius: 36px; background: rgba(245,245,248,.97); box-shadow: 0 18px 50px rgba(0,0,0,.25); font-family: Inter, sans-serif; color: #111; z-index: 40; }
      .xbn img { flex: none; width: 84px; height: 84px; border-radius: 20px; background: #fff; padding: 8px; }
      .end { position: absolute; inset: 0; background: radial-gradient(ellipse at 50% 35%, #ffffff 0%, #f1eefc 60%, #e7e1fa 100%); text-align: center; font-family: Inter, sans-serif; color: #1b1f4b; }
"""

HELP = SH4 + r"""
        const TOP = document.getElementById("root");
        tl.set([C.barT, C.barB], { opacity: 0 }, 0);
        const EO = "power2.out", EZ = "power2.inOut";
        const cap = (t0, t1, html, top = 360, w = false) => {
          const e = FX.ab(TOP, { left: "50px", right: "50px", top: top + "px", textAlign: "center", zIndex: 45 }, `<span class="ig${w ? " w" : ""}">${html}</span>`);
          tl.set(e, { opacity: 0 }, 0);
          tl.fromTo(e, { opacity: 0, scale: 0.9 }, { opacity: 1, scale: 1, duration: 0.18, ease: EO, immediateRender: false }, t0);
          tl.set(e, { opacity: 0 }, t1);
          return e;
        };
        // la conversation
        const conv = (who, ini, time) => {
          const l = FX.ab(TOP, { left: "0", top: "0", width: "1080px", height: "1920px" }, `<div class="xch"><div class="xhd"><div class="xst"><span>${time}</span><span>●●● 5G ▮</span></div><div class="xbk">‹</div><div class="xav">${ini}</div><div class="xnm">${who} ›</div></div><div class="xlst"><div class="xtm">${"Aujourd’hui " + time}</div></div>
<div class="xkb"><div class="xbar"><span class="xpl">+</span><div class="xin"><span class="xph">iMessage</span><span class="xdr"></span></div></div><div class="xkeys">
<div class="xr">${"AZERTYUIOP".split("").map((k) => `<span>${k}</span>`).join("")}</div><div class="xr">${"QSDFGHJKLM".split("").map((k) => `<span>${k}</span>`).join("")}</div><div class="xr"><span class="xg">⇧</span>${"WXCVBN".split("").map((k) => `<span>${k}</span>`).join("")}<span class="xg">⌫</span></div><div class="xr"><span class="xg">123</span><span class="xw">espace</span><span class="xg">envoyer</span></div></div></div></div>`);
          const kb = K.$(".xkb", l);
          tl.set(kb, { y: 640 }, 0);
          return { l, lst: K.$(".xlst", l), kb, dr: K.$(".xdr", l), ph: K.$(".xph", l) };
        };
        const msg = (c, t, html, side, o = {}) => {
          if (side === "in" && !o.nodots) {
            const d = K.h("div", "xdt", "<i></i><i></i><i></i>", c.lst);
            tl.set(d, { display: "none" }, 0); tl.set(d, { display: "flex" }, t - 1.0); tl.set(d, { display: "none" }, t);
            K.$$("i", d).forEach((i, k) => tl.fromTo(i, { opacity: 0.3 }, { opacity: 1, duration: 0.25, yoyo: true, repeat: 3, ease: "sine.inOut", immediateRender: false }, t - 1.0 + k * 0.12));
          }
          const b = K.h("div", "xbb x" + side, html, c.lst);
          [b, ...K.$$("*", b)].forEach((x) => { x.setAttribute("data-layout-allow-occlusion", ""); x.setAttribute("data-layout-allow-overlap", ""); });
          tl.set(b, { display: "none" }, 0); tl.set(b, { display: "block" }, t);
          tl.fromTo(b, { opacity: 0, y: 24, scale: 0.94 }, { opacity: 1, y: 0, scale: 1, duration: 0.28, ease: "back.out(1.6)", immediateRender: false }, t);
          K.sfx(t, side === "in" ? "receive" : "send", 0.32);
          return b;
        };
        const tapback = (b, t, emo) => {
          const e = K.h("span", "xtb", emo, b);
          tl.set(e, { opacity: 0, scale: 0 }, 0); tl.to(e, { opacity: 1, scale: 1, duration: 0.3, ease: "back.out(2.4)" }, t); K.sfx(t, "pop", 0.2, 0, { f: 900 });
        };
        const lu = (c, t, txt) => { const e = K.h("div", "xlu", txt, c.lst); tl.set(e, { display: "none" }, 0); tl.set(e, { display: "block" }, t); };
        const kbUp = (c, t) => { tl.to(c.kb, { y: 0, duration: 0.35, ease: EO }, t); tl.to(c.lst, { y: -160, duration: 0.35, ease: EO }, t); };
        const kbDown = (c, t) => { tl.to(c.kb, { y: 640, duration: 0.35, ease: EZ }, t); tl.to(c.lst, { y: 0, duration: 0.35, ease: EZ }, t); };
        // brouillon tapé puis effacé
        const draft = (c, t, txt, dur = 1.8) => {
          tl.set(c.ph, { display: "none" }, t);
          K.type(c.dr, txt, t, dur, 0.05);
          tl.to(c.dr, { clipPath: "inset(0% 100% 0% 0%)", duration: 0.6, ease: "power1.in" }, t + dur + 0.6);
          tl.set(c.dr, { textContent: "", clipPath: "inset(0% 0% 0% 0%)" }, t + dur + 1.25);
          tl.set(c.ph, { display: "inline" }, t + dur + 1.25);
          for (let k = 0; k < 5; k++) K.sfx(t + dur + 0.6 + k * 0.11, "type", 0.12, 0, { f: 2000 });
        };
        // suggestion LIMO au-dessus du clavier, puis tap → envoyé
        const sugg = (c, t, tTap, html) => {
          const s = FX.ab(c.l, { top: "790px" }, `<div class="xlg"><img src="assets/img/limo-logo-ad.png" alt="LIMO" />Réponse préparée par LIMO ✨</div><p>${html}</p>`);
          s.classList.add("xsg");
          tl.set(s, { opacity: 0 }, 0);
          tl.fromTo(s, { opacity: 0, y: 40 }, { opacity: 1, y: 0, duration: 0.35, ease: EO, immediateRender: false }, t);
          K.sfx(t, "success", 0.18);
          const tp = FX.ab(c.l, { left: "540px", top: "950px" }); tp.classList.add("xtap");
          tl.set(tp, { opacity: 0 }, 0);
          tl.fromTo(tp, { opacity: 0, scale: 0.4 }, { opacity: 1, scale: 0.8, duration: 0.1, ease: "none", immediateRender: false }, tTap);
          tl.to(tp, { opacity: 0, scale: 1.8, duration: 0.45, ease: EO }, tTap + 0.1);
          K.sfx(tTap, "tap", 0.35);
          tl.to(s, { opacity: 0, y: -60, scale: 0.9, duration: 0.25, ease: "power2.xin" }, tTap + 0.15);
          return s;
        };
        const endc = (t0) => {
          window.__TE = t0;
          const l = FX.ab(TOP, { left: "0", top: "0", width: "1080px", height: "1920px", zIndex: 60 }, `<div class="end"><div style="margin-top:560px"><img src="assets/img/limo-logo-ad.png" alt="LIMO" style="height:150px" /></div><div style="margin-top:26px;font-family:Montserrat,sans-serif;font-weight:700;font-size:44px">Le bras droit du conseiller immo.</div><div style="margin-top:60px"><span style="display:inline-block;padding:28px 54px;border-radius:999px;background:#6b4fe0;color:#fff;font-family:Montserrat,sans-serif;font-weight:800;font-size:46px">Essai gratuit 14 jours</span></div><div style="margin-top:26px;font-size:34px;color:#4f5378">Sans engagement · lien en bio</div></div>`);
          tl.set(l, { opacity: 0 }, 0); tl.to(l, { opacity: 1, duration: 0.3, ease: EO }, t0);
          const M = N.mascot({ left: "440px", top: "1340px", width: "200px" }, { expr: "happy" });
          TOP.appendChild(M.el); M.el.style.zIndex = "61";
          tl.set(M.el, { opacity: 0 }, 0); tl.to(M.el, { opacity: 1, duration: 0.3 }, t0 + 0.3); M.wave(t0 + 0.6); M.expr("wink", t0 + 1.6, false);
          K.sfx(t0, "whoosh", 0.12, 0, { d: 0.3, f0: 400, f1: 2400, pk: 0.4 });
        };
        const pdf = (name, sub) => `<div class="xatt"><i>PDF</i><span><b style="display:block">${name}</b><span style="font-size:27px;opacity:.85">${sub}</span></span></div>`;
        // déroulé commun : hook, 2 messages, brouillon, suggestion, envoi, réponse, chute
        const story = (o) => {
          const c = conv(o.who, o.ini, o.time);
          cap(0.15, 2.9, o.hook);
          o.ins.forEach((m, i) => msg(c, 0.9 + i * 1.3, m, "in"));
          kbUp(c, 3.4);
          cap(3.5, 6.6, "Ce que j’ai envie de répondre :", 820);
          draft(c, 3.7, o.want, 1.7);
          cap(6.7, 9.0, "Ce que LIMO m’a préparé :", 690, true);
          sugg(c, 6.8, 8.6, o.limo);
          const me = msg(c, 8.8, o.limoOut || o.limo, "out");
          kbDown(c, 9.0);
          lu(c, 9.4, "Lu " + o.time2);
          const r = msg(c, 10.8, o.reply, "in");
          tapback(me, 11.3, o.xtb || "❤️");
          cap(12.0, 13.9, o.punch, 1500, true);
          endc(13.9);
        };
"""

def pdf(name, sub):
    return f'<div class="xatt"><i>PDF</i><span><b style="display:block">{name}</b><span style="font-size:27px;opacity:.85">{sub}</span></span></div>'


FILMS = {
    "meme2-01-le-sms-de-22h47": dict(who="M. Garnier", ini="MG", time="22:47", time2="22:48", hook="22h47. Enfin posé en famille. 🍝",
        ins=["Bonsoir ! La maison de Vignols est toujours dispo ?", "On peut visiter demain 7h30 ? On part au boulot après 😅"],
        want="7h30 ?? Je dors encore moi 😩", limo="Bonsoir M. Garnier ! Toujours disponible 😊 Je vous propose samedi 10h ou lundi 18h. Belle soirée !",
        reply="Samedi 10h parfait, merci !! 🙏", punch="Et moi, je finis mon dessert. 🍰"),
    "meme2-02-rappelez-moi-en-mars": dict(who="Mme Leroy", ini="ML", time="09:12", time2="09:13", hook="Elle avait dit : « rappelez-moi en mars ». 🙂",
        ins=["Bonjour ! Vous vous souvenez de nous ? 😊", "On avait parlé de vendre au printemps…"],
        want="Euh… c’était quelle maison déjà ? 😬", limo="Bonjour Madame Leroy ! Bien sûr : la maison d’Allassac, 4 chambres, vente au printemps. On passe l’estimer jeudi ?",
        reply="Oh vous vous en souvenez ! Jeudi c’est parfait 🥰", tb="😍", punch="Le post-it, lui, aurait oublié. 🟨"),
    "meme2-03-ma-maison-vaut-plus": dict(who="M. Bernard", ini="MB", time="18:05", time2="18:06", hook="Le vendeur qui a « vu sur Internet ». 🧐",
        ins=["J’ai vu sur un site que ma maison vaut 320 000 €", "Donc on met 340 000 ? Mon voisin a vendu 300 000 😤"],
        want="Votre voisin avait une piscine 🙃", limo="Je vous envoie les 3 ventes réelles à moins de 500 m (DVF) : de 248 000 à 262 000 €. On en parle demain ?",
        reply="Ah oui… effectivement 😅 OK pour demain", tb="👍", punch="Les chiffres parlent. Pas moi. 😌"),
    "meme2-04-frais-km": dict(who="Mon comptable 📊", ini="EC", time="10:30", time2="10:31", hook="Le 30 du mois. 📎",
        ins=["Bonjour, il me manque vos frais km d’octobre 🙏", "Avant ce soir si possible !"],
        want="Euh… le 4 j’étais où déjà ? 🤔", limo="Bonjour ! Voici le tableau : 1 240 km en octobre, trajet par trajet. Bonne journée !",
        limoOut=pdf("Frais-km-octobre.pdf", "1 240 km · 38 trajets"), reply="Déjà ?! Merci, c’est parfait 😳", tb="🙏", punch="Le 30, je dors. 😴"),
    "meme2-05-le-compromis-du-dimanche": dict(who="Me Faure · Notaire", ini="MF", time="21:04", time2="21:06", hook="Dimanche, 21h. Le notaire. 🍿",
        ins=[pdf("Compromis-Vignols.pdf", "47 pages"), "Retour demain 9h svp. Bon dimanche !"],
        want="Un dimanche à 21h… sérieux ? 🙃", limo="Bonsoir Maître, relu ✅ 2 points à vérifier : condition de prêt (60 j) et servitude de passage. Bonne soirée !",
        reply="Parfait, merci pour la réactivité 👌", tb="👍", punch="Et le film, je le regarde. 🍿"),
    "meme2-06-dautres-biens-comme-ca": dict(who="Famille Petit", ini="FP", time="17:40", time2="17:41", hook="Juste après la visite… 🏡",
        ins=["Merci pour la visite ! 😊", "Vous auriez d’autres biens comme ça mais avec un plus grand jardin ?"],
        want="Laissez-moi fouiller dans mes 47 mandats 😅", limo="Oui ! 3 biens pour vous : longère à Voutezac (2 400 m²), maison à Allassac (1 800 m²) et à Vignols (1 500 m²). Visite samedi ?",
        reply="OUI !! Samedi 😍😍", tb="😍", punch="Avant la fin de la visite. 😎"),
}

if __name__ == "__main__":
    import json
    for name, o in FILMS.items():
        body = "        story(" + json.dumps(o, ensure_ascii=False) + ");\n"
        html = SHELL.format(title=name, faces=FACES, css=(CSS + CSS_M).strip("\n"), body=(COMMON + HELP + body).strip("\n"), dur=DUR, name=name)
        (HERE.parent / "reels" / f"{name}.html").write_text(html, encoding="utf-8")
        print("reels/" + name + ".html")
