"""Films LIMO dans la charte « naturelle » (lavande, marine, violet, turquoise ; SMS, notes, notifications iOS).

Usage : python3 outils/naturel.py   (réécrit reels/nat-*.html)
"""
import pathlib

FACES = "".join(
    f"""      @font-face {{ font-family: "{f}"; src: url("assets/fonts/{file}") format("woff2"); font-weight: {w}; font-style: normal; }}\n"""
    for f, file, w in [("Anton", "anton-latin-400-normal.woff2", 400), ("Source Serif 4", "source-serif-4-latin-400-normal.woff2", 400), ("Caveat", "caveat-latin-700-normal.woff2", 700)]
)

SHELL = """<!doctype html>
<html lang="fr">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=1080, height=1920" />
    <title>LIMO — {title}</title>
    <script src="assets/lib/gsap.min.js"></script>
    <link rel="stylesheet" href="assets/kit/kit.css" />
    <link rel="stylesheet" href="assets/kit/naturel.css" />
    <style>
{faces}{css}
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="{dur}" data-width="1080" data-height="1920">
      <section id="s-main" class="clip" data-start="0" data-duration="{dur}" data-track-index="0"></section>
      <audio id="sfx" src="assets/audio/{name}.wav" data-start="0" data-duration="{dur}" data-track-index="10" data-volume="1"></audio>
    </div>
    <script src="assets/kit/kit.js"></script>
    <script src="assets/kit/naturel.js"></script>
    <script>
      (function () {{
        const tl = gsap.timeline({{ paused: true }});
        K.init(tl);
        const root = document.getElementById("s-main");
        const D = {dur};
        N.init(tl, root, D);
{body}
        window.__timelines["main"] = tl;
      }})();
    </script>
  </body>
</html>
"""

FILMS = {}

# ---------------------------------------------------------------- A · « Rappelez-moi en mars »
FILMS["nat-01-rappelez-moi-en-mars"] = ("Rappelez-moi en mars", 16.6, "", """
        const cap1 = N.cap("Ce SMS, tout agent immo<br>l’a déjà reçu.", { top: "150px" }, 0.15);
        const ip = N.iphone({ left: "110px", top: "400px", width: "860px", height: "1500px" }, "9:12");
        N.hide(ip.el);
        tl.fromTo(ip.el, { opacity: 0, y: 300 }, { opacity: 1, y: 0, duration: 0.7, ease: "power3.out" }, 0.05);
        const sc = ip.screen;
        const head = K.h("div", "n-mhead", `<div class="av">MM</div><b>M. et Mme Martin · vendeurs</b>`, sc);
        const th = K.h("div", "n-thread", null, sc);
        const d1 = K.h("div", "n-day", "Lun. 12 janvier · 18:40", th);
        const b1 = K.h("div", "n-bub in", "Bonjour, on réfléchit encore. Rappelez-moi en mars, on sera prêts à vendre.", th);
        const b2 = K.h("div", "n-bub out", "Parfait, je vous rappelle en mars !", th);
        const d2 = K.h("div", "n-day", "Ven. 18 avril · 9:12", th);
        const dots = K.h("div", "n-dots", "<i></i><i></i><i></i>", th);
        const b3 = K.h("div", "n-bub in", "Bonjour, finalement nous avons signé avec une autre agence. Bonne continuation.", th);
        [b1, b2, d2, dots, b3].forEach(N.hide);
        K.fin(b1, 0.7, { y: 20, d: 0.35 });
        K.sfx(0.7, "receive", 0.26);
        K.fin(b2, 1.5, { y: 20, d: 0.35 });
        K.sfx(1.5, "send", 0.22);
        N.out(cap1, 2.4, { y: -10, d: 0.2 });
        const cap2 = N.cap("On est en avril.<br>Tu l’as rappelé ?", { top: "150px" }, 2.6);
        K.fin(d2, 2.7, { y: 10, d: 0.3 });
        [2.7, 3.0, 3.3].forEach((x, i) => K.sfx(x, i % 2 ? "tock" : "tick", 0.16));
        tl.fromTo(dots, { opacity: 0 }, { opacity: 1, duration: 0.15 }, 3.6);
        K.$$("i", dots).forEach((d, i) => tl.fromTo(d, { y: 0 }, { y: -8, duration: 0.14, yoyo: true, repeat: 3, ease: "sine.inOut" }, 3.65 + i * 0.07));
        tl.set(dots, { display: "none" }, 4.4);
        K.fin(b3, 4.4, { y: 20, d: 0.35 });
        K.sfx(4.4, "receive", 0.3);
        tl.fromTo(ip.el, { x: 0 }, { x: 8, duration: 0.05, ease: "none", yoyo: true, repeat: 5, immediateRender: false }, 4.6);
        N.out(cap2, 5.2, { y: -10, d: 0.2 });
        const cap3 = N.cap("Mandat perdu.<br>Pas à cause du prix.", { top: "150px" }, 5.4, { dark: true });
        K.sfx(5.4, "thump", 0.3);
        N.out([cap3, ip.el], 7.4, { y: 60, d: 0.4 });
        // LIMO
        const h = N.head(["LIMO, LUI<span class='v'>,</span>", "N’OUBLIE PAS<span class='v'>.</span>"], { top: "170px", fontSize: "92px" }, 7.8);
        const ph = N.phoneLimo({ left: "213px", top: "560px" }, 8.2);
        const n1 = N.notif({ title: "RAPPEL", time: "1er mars", text: "M. et Mme Martin : ils vendent en mars. C’est le moment d’appeler." }, { left: "90px", top: "640px" }, 9.1);
        const n2 = N.notif({ title: "AGENDA", time: "3 mars", text: "Estimation chez les Martin : jeudi, 10 h.", snd: "notif", g: 0.2 }, { left: "90px", top: "860px" }, 10.3);
        const n3 = N.notif({ title: "MANDAT", time: "10 mars", text: "Mandat exclusif signé : famille Martin.", snd: "success", g: 0.3 }, { left: "90px", top: "1060px" }, 11.3);
        N.out([h, ph, n1, n2, n3], 12.7, { y: -30 });
        window.__TE = 13.0;
        N.outro(13.0, "dm");
""")

# ---------------------------------------------------------------- B · le dimanche soir
FILMS["nat-02-dimanche-soir"] = ("Le dimanche soir d’un agent immo", 16.2, "", """
        const cap1 = N.cap("Dimanche, 21 h 47.<br>Ta tête est déjà à lundi.", { top: "140px" }, 0.15);
        const ip = N.iphone({ left: "110px", top: "380px", width: "860px", height: "1500px" }, "21:47");
        N.hide(ip.el);
        tl.fromTo(ip.el, { opacity: 0, y: 300 }, { opacity: 1, y: 0, duration: 0.7, ease: "power3.out" }, 0.05);
        const notes = K.h("div", "n-notes", `<h3>Lundi</h3><div class="dt">Dimanche 21:47</div>`, ip.screen);
        const L = ["Rappeler les Martin", "Compromis Roche", "Annonce Brive + DPE", "Avis Google", "Post LinkedIn", "Anniv. Mme Roy"];
        const rows = L.map((l, i) => {
          const r = K.h("div", "n-li", `<span class="c"><i>${K.icon("check")}</i></span><span class="t"></span><span class="tag">fait par LIMO</span>`, notes);
          tl.set(K.$(".c i", r), { scale: 0 }, 0);
          tl.set(K.$(".tag", r), { opacity: 0, x: 20 }, 0);
          N.hide(r);
          const t = 0.8 + i * 0.62;
          tl.set(r, { opacity: 1 }, t);
          K.type(K.$(".t", r), l, t, 0.45, 0.035);
          return r;
        });
        N.out(cap1, 4.6, { y: -10, d: 0.2 });
        const cap2 = N.cap("Et si c’était déjà fait ?", { top: "140px" }, 4.8, { dark: true });
        rows.forEach((r, i) => {
          const t = 5.5 + i * 0.4;
          tl.to(K.$(".c i", r), { scale: 1, duration: 0.25, ease: "back.out(2.4)" }, t);
          tl.to(K.$(".t", r), { color: "#8e8e93", duration: 0.2 }, t);
          tl.to(K.$(".tag", r), { opacity: 1, x: 0, duration: 0.3, ease: "power3.out" }, t + 0.05);
          K.sfx(t, "tick", 0.2, 0, { f: 1700 + i * 150 });
        });
        N.out([cap2, ip.el], 8.4, { y: 60, d: 0.4 });
        const h = N.head(["TON LUNDI", "EST DÉJÀ PRÊT<span class='v'>.</span>"], { top: "220px", fontSize: "96px" }, 8.8);
        const photo = N.ab("", `<img src="assets/img/bureau-robot.jpg" alt="Le robot LIMO au bureau" style="width:100%;height:100%;object-fit:cover" />`, { left: "90px", top: "620px", width: "900px", height: "541px", borderRadius: "36px", overflow: "hidden", boxShadow: "0 30px 60px rgba(27,31,75,.25)" });
        N.hide(photo);
        tl.fromTo(photo, { opacity: 0, y: 60 }, { opacity: 1, y: 0, duration: 0.6, ease: "power3.out" }, 9.1);
        tl.fromTo(K.$("img", photo), { scale: 1.02 }, { scale: 1.1, duration: 4, ease: "none" }, 9.1);
        const s = N.text("ctr n-body", "LIMO prépare tes relances, tes annonces<br>et tes messages. <b>Toi, tu profites.</b>", { top: "1220px", fontSize: "36px" }, 9.8);
        N.out([h, photo, s], 12.4);
        window.__TE = 12.6;
        N.outro(12.6, "essai");
""")

# ---------------------------------------------------------------- C · 842 contacts
FILMS["nat-03-842-contacts"] = ("Ton CRM stocke, LIMO travaille", 16.0, """
      .n-ct { display: flex; align-items: center; gap: 22px; height: 118px; padding: 0 44px; border-bottom: 1px solid #efeff4; font-family: Inter, sans-serif; font-size: 38px; color: #000; }
      .n-ct .av { flex: none; width: 64px; height: 64px; border-radius: 50%; background: #6f7488; color: #fff; display: flex; align-items: center; justify-content: center; font-size: 24px; font-weight: 700; }
      .n-ct span { margin-left: auto; font-size: 25px; color: #6e6e73; }
      #big { top: 620px; font-family: Montserrat, sans-serif; font-weight: 700; font-size: 230px; color: var(--navy); line-height: 1; }
      #big small { font-size: 80px; color: var(--mut); font-weight: 600; }
""", """
        const cap1 = N.cap("Ton CRM a <b>842</b> contacts.", { top: "140px" }, 0.15);
        const ip = N.iphone({ left: "110px", top: "380px", width: "860px", height: "1500px" }, "8:30");
        N.hide(ip.el);
        tl.fromTo(ip.el, { opacity: 0, y: 300 }, { opacity: 1, y: 0, duration: 0.7, ease: "power3.out" }, 0.05);
        const hd = K.h("div", "n-mhead", `<b style="font-size:40px;font-weight:800">Contacts</b><b style="color:#6e6e73">842 contacts</b>`, ip.screen);
        const vp = K.h("div", "", null, ip.screen);
        Object.assign(vp.style, { position: "absolute", left: "0", right: "0", top: "266px", bottom: "0", overflow: "hidden" });
        const list = K.h("div", "", null, vp);
        Object.assign(list.style, { position: "absolute", left: "0", right: "0", top: "0" });
        list.setAttribute("data-layout-allow-occlusion", "");
        list.setAttribute("data-layout-allow-overflow", "");
        const FN = ["Albert", "Bernard", "Blanc", "Boyer", "Chevalier", "Clément", "Da Silva", "Delmas", "Durand", "Fabre", "Faure", "Fournier", "Garnier", "Girard", "Lambert", "Laurent", "Lefebvre", "Leroy", "Martin", "Mercier", "Moreau", "Morel", "Perrin", "Petit", "Renaud", "Robin", "Roche", "Roussel", "Roy", "Vidal"];
        const PR = ["M.", "Mme", "M. et Mme"];
        const last = ["Vendeur · 2023", "Acquéreur · 2024", "Estimation · 2022", "Vendeur · 2021", "Visite · 2024"];
        FN.forEach((n, i) => K.h("div", "n-ct", `<div class="av">${n[0]}</div>${PR[i % 3]} ${n}<span>${last[i % 5]}</span>`, list).setAttribute("data-layout-allow-occlusion", ""));
        list.querySelectorAll("*").forEach((e) => e.setAttribute("data-layout-allow-occlusion", ""));
        tl.fromTo(list, { y: 0 }, { y: -2300, duration: 2.6, ease: "power2.inOut" }, 0.7);
        K.sfx(0.7, "whoosh", 0.14, 0, { d: 2.4, f0: 300, f1: 1400, pk: 0.5 });
        N.out(cap1, 2.8, { y: -10, d: 0.2 });
        const cap2 = N.cap("Combien t’en as rappelé<br>ce mois-ci ?", { top: "140px" }, 3.0, { dark: true });
        N.out([ip.el], 4.6, { y: 60, d: 0.4 });
        const big = N.ab("ctr", `<span>0</span><small> / 842</small>`, {});
        big.id = "big";
        N.hide(big);
        tl.set(big, { opacity: 1 }, 4.9);
        K.count(K.$("span", big), 12, 4.9, 0.8, (v) => String(Math.round(v)));
        K.sfx(5.75, "thump", 0.35);
        const s1 = N.text("ctr n-body", "Les autres attendent. Et signent ailleurs.", { top: "900px", fontSize: "40px" }, 5.8);
        N.out([cap2, big, s1], 7.4);
        const h = N.head(["TON CRM STOCKE<span class='v'>.</span>", "<em>LIMO TRAVAILLE.</em>"], { top: "190px", fontSize: "86px" }, 7.6);
        const ph = N.phoneLimo({ left: "213px", top: "560px" }, 8.2);
        const n1 = N.notif({ title: "BRIEF DU MATIN", time: "8:00", text: "5 actions prioritaires aujourd’hui. On commence par M. Albert." }, { left: "90px", top: "680px" }, 9.3);
        N.out([h, ph, n1], 12.0, { y: -30 });
        window.__TE = 12.4;
        N.outro(12.4, "demo");
""")


# ---------------------------------------------------------------- 4 · le compromis de 12 pages
FILMS["nat-04-compromis-12-pages"] = ("Le compromis de 12 pages", 15.6, """
      .pg { position: absolute; left: 70px; width: 680px; height: 900px; background: #fff; border-radius: 10px; box-shadow: 0 6px 20px rgba(0,0,0,.12); padding: 60px 56px; }
      .pg i { display: block; height: 14px; border-radius: 7px; background: #dcdce2; margin-bottom: 22px; }
      .pg i.h { height: 22px; width: 60%; background: #b8b8c2; margin-bottom: 40px; }
      #pc { position: absolute; left: 0; right: 0; bottom: 40px; text-align: center; font-family: Inter, sans-serif; font-weight: 600; font-size: 28px; color: #6e6e73; }
""", """
        const cap1 = N.cap("12 pages. Tu recopies encore<br>tout ça à la main ?", { top: "140px" }, 0.15);
        const ip = N.iphone({ left: "110px", top: "400px", width: "860px", height: "1480px" }, "18:05");
        N.hide(ip.el);
        tl.fromTo(ip.el, { opacity: 0, y: 300 }, { opacity: 1, y: 0, duration: 0.7, ease: "power3.out" }, 0.05);
        const hd = K.h("div", "n-mhead", `<b style="font-size:34px;font-weight:700">Compromis_Roche.pdf</b><b style="color:#6e6e73">12 pages</b>`, ip.screen);
        const vp = K.h("div", "", null, ip.screen);
        Object.assign(vp.style, { position: "absolute", left: "0", right: "0", top: "266px", bottom: "0", overflow: "hidden", background: "#f2f2f7" });
        const pages = [];
        for (let p = 0; p < 12; p++) {
          const g = K.h("div", "pg", `<i class="h"></i>` + Array.from({ length: 22 }, (_, k) => `<i style="width:${60 + ((k * 37 + p * 11) % 40)}%"></i>`).join(""), vp);
          g.style.top = 40 + p * 960 + "px";
          g.setAttribute("data-layout-allow-occlusion", "");
          g.setAttribute("data-layout-allow-overflow", "");
          pages.push(g);
        }
        const strip = K.h("div", "", null, vp);
        pages.forEach((g) => strip.appendChild(g));
        const pc = K.h("div", "", "Page 1 / 12", ip.screen);
        pc.id = "pc";
        tl.fromTo(strip, { y: 0 }, { y: -960 * 11, duration: 3.6, ease: "power2.inOut" }, 0.9);
        const PP = { p: 1 };
        tl.to(PP, { p: 12, duration: 3.6, ease: "power2.inOut", onUpdate: () => { pc.textContent = `Page ${Math.round(PP.p)} / 12`; } }, 0.9);
        for (let k = 0; k < 11; k++) K.sfx(1.0 + k * 0.3, "tick", 0.1, 0, { f: 2400 });
        N.out(cap1, 2.6, { y: -10, d: 0.2 });
        const cap2 = N.cap("Noms, prix, notaire, dates…<br>30 minutes de saisie.", { top: "140px" }, 2.8, { dark: true });
        N.out([cap2, ip.el], 5.0, { y: 60, d: 0.4 });
        const h = N.head(["LIMO LE LIT", "POUR TOI<span class='v'>.</span>"], { top: "200px", fontSize: "92px" }, 5.3);
        const card = N.ab("n-card", [["Acquéreurs", "M. et Mme Roche"], ["Notaire", "Me Faure"], ["Prix", "245 000 €"], ["Honoraires", "12 000 € TTC"], ["Signature", "14 mars"]].map((r) => `<div class="n-row"><span>${r[0]}</span><b>${r[1]}</b><i class="ok">${K.icon("check")}</i></div>`).join(""), { left: "110px", top: "640px", width: "860px" });
        N.hide(card);
        tl.fromTo(card, { opacity: 0, y: 60 }, { opacity: 1, y: 0, duration: 0.5, ease: "power3.out" }, 6.0);
        K.$$(".n-row", card).forEach((r, i) => {
          tl.fromTo(K.$(".ok", r), { scale: 0 }, { scale: 1, duration: 0.25, ease: "back.out(2.4)" }, 6.5 + i * 0.3);
          K.sfx(6.5 + i * 0.3, "tick", 0.2, 0, { f: 1600 + i * 180 });
        });
        const ch = N.ab("ctr", `<span class="n-chip">${K.icon("check")}Fiche remplie automatiquement</span>`, { top: "1180px" });
        N.hide(ch);
        tl.set(ch, { opacity: 1 }, 8.2);
        K.pop(K.$("span", ch), 8.2);
        K.sfx(8.2, "success", 0.22);
        const n1 = N.notif({ title: "COMPROMIS", text: "Compromis Roche lu : fiche vendeur et acquéreur remplies." }, { left: "90px", top: "1330px" }, 8.8);
        N.out([h, card, ch, n1], 11.6);
        window.__TE = 12.0;
        N.outro(12.0, "demo");
""")

# ---------------------------------------------------------------- 5 · la note vocale
FILMS["nat-05-note-vocale"] = ("Je noterai ça ce soir", 15.4, "", """
        const cap1 = N.cap("Tu sors de visite.<br>« Je noterai ça ce soir. »", { top: "140px" }, 0.15);
        const ip = N.iphone({ left: "110px", top: "400px", width: "860px", height: "1480px" }, "11:42");
        N.hide(ip.el);
        tl.fromTo(ip.el, { opacity: 0, y: 300 }, { opacity: 1, y: 0, duration: 0.7, ease: "power3.out" }, 0.05);
        K.h("div", "n-mhead", `<div class="av" style="background:#fff;padding:6px"><img src="assets/img/limo-house-ad.png" alt="" style="width:100%;height:100%;object-fit:contain" /></div><b>LIMO</b>`, ip.screen);
        const th = K.h("div", "n-thread", null, ip.screen);
        K.h("div", "n-day", "Aujourd’hui · 11:42", th);
        const wv = Array.from({ length: 26 }, (_, i) => `<i style="height:${12 + Math.round(34 * Math.abs(Math.sin(i * 1.3 + 0.4)))}px"></i>`).join("");
        const v = K.h("div", "n-bub out", `<div style="display:flex;align-items:center;gap:18px">${K.icon("mic")}<div class="n-wave">${wv}</div><span style="font-size:30px">0:14</span></div>`, th);
        K.$("svg.i", v).style.cssText = "width:40px;height:40px;flex:none";
        N.hide(v);
        K.fin(v, 1.1, { y: 20, d: 0.35 });
        K.sfx(1.1, "send", 0.22);
        K.$$(".n-wave i", v).forEach((b, i) => tl.fromTo(b, { scaleY: 1 }, { scaleY: 0.4, duration: 0.18, yoyo: true, repeat: 5, ease: "sine.inOut", immediateRender: false }, 1.3 + (i % 5) * 0.04));
        K.sfx(1.3, "voice", 0.08, 0, { d: 1.1 });
        N.out(cap1, 2.8, { y: -10, d: 0.2 });
        const cap2 = N.cap("Spoiler : tu ne le noteras pas.<br>Sauf si LIMO le fait.", { top: "140px" }, 3.0, { dark: true });
        const dots = K.h("div", "n-dots", "<i></i><i></i><i></i>", th);
        N.hide(dots);
        tl.set(dots, { opacity: 1 }, 3.8);
        K.$$("i", dots).forEach((d, i) => tl.fromTo(d, { y: 0 }, { y: -8, duration: 0.14, yoyo: true, repeat: 3, ease: "sine.inOut" }, 3.85 + i * 0.07));
        tl.set(dots, { display: "none" }, 4.6);
        const r = K.h("div", "n-bub in", "C’est noté. <b>Fiche vendeur créée</b> : famille Martin, maison 120 m² à Brive, vente prévue en mars. <b>Relance le 1er mars.</b>", th);
        N.hide(r);
        K.fin(r, 4.6, { y: 20, d: 0.35 });
        K.sfx(4.6, "receive", 0.28);
        N.out([cap2, ip.el], 7.2, { y: 60, d: 0.4 });
        const h = N.head(["TU PARLES<span class='v'>.</span>", "LIMO NOTE<span class='v'>.</span>"], { top: "200px", fontSize: "96px" }, 7.5);
        const ph = N.phoneLimo({ left: "213px", top: "580px" }, 7.9);
        const n1 = N.notif({ title: "FICHE VENDEUR", text: "Famille Martin · maison 120 m² · relance le 1er mars." }, { left: "90px", top: "700px" }, 8.8);
        N.out([h, ph, n1], 11.4, { y: -30 });
        window.__TE = 11.8;
        N.outro(11.8, "essai");
""")

# ---------------------------------------------------------------- 6 · l'avis Google
FILMS["nat-06-avis-sans-reponse"] = ("5 étoiles sans réponse", 15.8, "", """
        const cap1 = N.cap("Ce client t’a laissé 5 étoiles…", { top: "200px" }, 0.15);
        const rv = N.ab("n-card", `<div style="padding:40px 44px"><div style="display:flex;align-items:center;gap:22px"><div style="width:84px;height:84px;border-radius:50%;background:#b86e00;color:#fff;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:34px">ML</div><div><b style="font-size:36px">Marie L.</b><div style="display:flex;align-items:center;gap:14px;margin-top:6px"><span class="n-stars">${K.icon("star").repeat(5)}</span><span style="font-size:26px;color:#6e6e73">il y a 12 jours</span></div></div></div><div style="margin-top:28px;font-size:38px;line-height:1.35">« Accompagnement au top, maison vendue en 3 semaines. Merci ! »</div><div class="nr" style="margin-top:30px;font-size:28px;color:#c0392b;font-weight:600">Aucune réponse du propriétaire</div></div>`, { left: "90px", top: "440px", width: "900px" });
        N.hide(rv);
        tl.fromTo(rv, { opacity: 0, y: 60 }, { opacity: 1, y: 0, duration: 0.6, ease: "power3.out" }, 0.3);
        K.$$(".n-stars svg", rv).forEach((s, i) => { tl.fromTo(s, { scale: 0 }, { scale: 1, duration: 0.2, ease: "back.out(3)" }, 0.8 + i * 0.1); K.sfx(0.8 + i * 0.1, "pop", 0.1, 0, { f: 700 + i * 90 }); });
        N.out(cap1, 2.4, { y: -10, d: 0.2 });
        const cap2 = N.cap("…il y a 12 jours.<br>Toujours pas de réponse.", { top: "200px" }, 2.6, { dark: true });
        tl.fromTo(K.$(".nr", rv), { opacity: 1 }, { opacity: 0.3, duration: 0.25, yoyo: true, repeat: 3 }, 2.8);
        K.sfx(2.8, "buzz", 0.12);
        N.out(cap2, 4.4, { y: -10, d: 0.2 });
        tl.to(rv, { y: 60, duration: 0.6, ease: "power3.inOut" }, 4.4);
        tl.to(K.$(".nr", rv), { opacity: 0, duration: 0.2 }, 4.4);
        const h = N.head(["LIMO RÉDIGE", "LA RÉPONSE<span class='v'>.</span>"], { top: "150px", fontSize: "82px" }, 4.8, { bar: false });
        const rp = N.ab("n-card", `<div style="padding:36px 44px"><div style="font-size:26px;font-weight:700;color:#6b4fe0">Réponse proposée par LIMO</div><div class="t" style="margin-top:14px;font-size:36px;line-height:1.35;min-height:150px"></div><div style="display:flex;justify-content:flex-end;margin-top:18px"><span class="btn" style="height:72px;padding:0 34px;border-radius:36px;background:#6b4fe0;color:#fff;font-size:30px;font-weight:700;display:flex;align-items:center">Publier</span></div></div>`, { left: "90px", top: "980px", width: "900px" });
        N.hide(rp);
        tl.fromTo(rp, { opacity: 0, y: 60 }, { opacity: 1, y: 0, duration: 0.5, ease: "power3.out" }, 5.2);
        K.type(K.$(".t", rp), "Merci Marie ! Ravi de vous avoir accompagnés. Belle installation dans votre nouvelle maison !", 5.6, 1.8, 0.035);
        K.tapAt(rp, 800, 290, 7.9);
        const ch = N.ab("ctr", `<span class="n-chip">${K.icon("check")}Réponse publiée</span>`, { top: "1450px" });
        N.hide(ch);
        tl.set(ch, { opacity: 1 }, 8.2);
        K.pop(K.$("span", ch), 8.2);
        K.sfx(8.2, "success", 0.24);
        const s = N.text("ctr n-body", "Google adore les agences qui répondent.<br><b>Tes futurs vendeurs aussi.</b>", { top: "1560px", fontSize: "34px" }, 9.0);
        N.out([h, rv, rp, ch, s], 11.8);
        window.__TE = 12.2;
        N.outro(12.2, "comment");
""")

# ---------------------------------------------------------------- 7 · l'annonce de 22 h
FILMS["nat-07-annonce-22h"] = ("22 h 13, l’annonce", 15.8, """
      .cur { display: inline-block; width: 4px; height: 44px; background: #f5b700; vertical-align: -8px; margin-left: 2px; }
""", """
        const cap1 = N.cap("22 h 13. Toujours pas<br>d’accroche pour l’annonce.", { top: "140px" }, 0.15);
        const ip = N.iphone({ left: "110px", top: "400px", width: "860px", height: "1480px" }, "22:13");
        N.hide(ip.el);
        tl.fromTo(ip.el, { opacity: 0, y: 300 }, { opacity: 1, y: 0, duration: 0.7, ease: "power3.out" }, 0.05);
        const nt = K.h("div", "n-notes", `<h3>Annonce maison Brive</h3><div class="dt">22:13</div><div style="font-size:40px;line-height:1.4"><span class="t"></span><span class="cur"></span></div>`, ip.screen);
        const tt = K.$(".t", nt);
        const cur = K.$(".cur", nt);
        tl.fromTo(cur, { opacity: 1 }, { opacity: 0, duration: 0.3, repeat: 13, yoyo: true, ease: "steps(1)" }, 0.8);
        const drafts = ["Charmante maison idéalement située…", "Belle maison de 120 m² avec jar…", "Maison… "];
        let tt0 = 0.9;
        const P = { i: 0 };
        drafts.forEach((d, k) => {
          const P1 = { n: 0 };
          tl.to(P1, { n: d.length, duration: 0.7, ease: "none", onUpdate: () => { tt.textContent = d.slice(0, Math.round(P1.n)); } }, tt0);
          for (let x = 0; x < 6; x++) K.sfx(tt0 + x * 0.11, "type", 0.05, 0, { f: 2800 + x * 60 });
          const P2 = { n: d.length };
          tl.to(P2, { n: 0, duration: 0.4, ease: "none", onUpdate: () => { tt.textContent = d.slice(0, Math.round(P2.n)); } }, tt0 + 0.95);
          tt0 += 1.5;
        });
        N.out(cap1, 3.0, { y: -10, d: 0.2 });
        const cap2 = N.cap("Et les mentions légales,<br>t’es sûr de les avoir ?", { top: "140px" }, 3.2, { dark: true });
        N.out([cap2, ip.el], 5.3, { y: 60, d: 0.4 });
        const h = N.head(["L’ANNONCE", "EST PRÊTE<span class='v'>.</span>"], { top: "180px", fontSize: "96px" }, 5.6);
        const an = N.ab("n-card", `<div style="padding:40px 44px"><div style="font-family:'Source Serif 4',serif;font-size:46px;font-weight:600;line-height:1.2;color:#1b1f4b" class="ti"></div><div class="bo" style="margin-top:18px;font-size:32px;line-height:1.4;color:#3a3a3c;min-height:140px"></div><div class="lg" style="margin-top:20px;padding-top:18px;border-top:1px solid #efeff4;font-size:24px;line-height:1.4;color:#6e6e73">312 000 € honoraires inclus · 4 % TTC à la charge de l’acquéreur · DPE C · GES A</div><div class="cs" style="display:flex;gap:14px;margin-top:22px"><span class="n-chip">${K.icon("check")}Mentions légales</span><span class="n-chip">${K.icon("check")}Prête à publier</span></div></div>`, { left: "90px", top: "620px", width: "900px" });
        N.hide(an);
        tl.fromTo(an, { opacity: 0, y: 60 }, { opacity: 1, y: 0, duration: 0.5, ease: "power3.out" }, 6.1);
        K.type(K.$(".ti", an), "Maison familiale lumineuse avec jardin", 6.5, 0.7, 0.05);
        K.type(K.$(".bo", an), "À 5 min du centre de Brive, 120 m², 4 chambres, séjour traversant et jardin de 700 m² sans vis-à-vis.", 7.2, 1.3, 0.04);
        N.hide(K.$(".lg", an));
        K.fin(K.$(".lg", an), 8.6, { y: 8 });
        N.hide(K.$(".cs", an));
        tl.set(K.$(".cs", an), { opacity: 1 }, 9.0);
        K.pop(K.$$(".cs .n-chip", an), 9.0, { st: 0.12 });
        K.sfx(9.0, "success", 0.22);
        N.out([h, an], 11.8);
        window.__TE = 12.2;
        N.outro(12.2, "essai");
""")

# ---------------------------------------------------------------- 8 · le quiz DPE
FILMS["nat-08-quiz-dpe"] = ("Le DPE de 2020", 16.8, """
      .opt { left: 110px; width: 860px; height: 116px; border-radius: 30px; background: #fff; box-shadow: 0 10px 30px rgba(27,31,75,.12);
        display: flex; align-items: center; gap: 26px; padding: 0 34px; font-family: Montserrat, sans-serif; font-weight: 600; font-size: 36px; color: var(--navy); }
      .opt .l { flex: none; width: 64px; height: 64px; border-radius: 50%; background: var(--lav2); color: var(--vio); display: flex; align-items: center; justify-content: center; font-weight: 800; }
      #tm, [id="tm"] { top: 1250px; font-family: Montserrat, sans-serif; font-weight: 700; font-size: 120px; color: var(--vio); }
""", """
        const cap1 = N.cap("La question qui fait douter<br>même les pros.", { top: "140px" }, 0.15);
        const q = N.ab("n-card", `<div style="padding:34px 40px;display:flex;gap:22px;align-items:flex-start"><div style="flex:none;width:76px;height:76px;border-radius:50%;background:#5f6477;color:#fff;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:30px">MD</div><div><div style="font-size:26px;color:#6e6e73;font-weight:600">M. Delmas · vendeur</div><div style="margin-top:10px;font-size:42px;line-height:1.3">« Notre DPE date de 2020. Il est encore bon pour vendre ? »</div></div></div>`, { left: "90px", top: "400px", width: "900px" });
        N.hide(q);
        tl.fromTo(q, { opacity: 0, y: 60 }, { opacity: 1, y: 0, duration: 0.5, ease: "power3.out" }, 0.4);
        K.sfx(0.4, "receive", 0.28);
        N.out(cap1, 2.2, { y: -10, d: 0.2 });
        const cap2 = N.cap("Tu réponds quoi ?", { top: "140px" }, 2.4, { dark: true });
        const O = [["A", "Oui, un DPE vaut 10 ans"], ["B", "Non, il faut le refaire"], ["C", "Ça dépend du logement"]];
        const opts = O.map((o, i) => {
          const e = N.ab("opt", `<span class="l">${o[0]}</span>${o[1]}`, { top: 760 + i * 140 + "px" });
          N.hide(e);
          K.fin(e, 2.7 + i * 0.2, { y: 20, d: 0.35 });
          K.sfx(2.7 + i * 0.2, "pop", 0.12, 0, { f: 600 + i * 100 });
          return e;
        });
        ["3", "2", "1"].forEach((x, i) => {
          const tm = N.ab("ctr", x, {});
          tm.id = "tm";
          N.hide(tm);
          const t = 3.6 + i * 0.7;
          tl.fromTo(tm, { opacity: 1, scale: 1.4 }, { opacity: 1, scale: 1, duration: 0.3, ease: "back.out(2)" }, t);
          tl.set(tm, { opacity: 0 }, t + 0.68);
          K.sfx(t, "beep", 0.18, 0, { f: 880 });
        });
        tl.to([opts[0], opts[2]], { opacity: 0.35, duration: 0.3 }, 5.7);
        tl.to(opts[1], { backgroundColor: "#2cc4b5", color: "#fff", scale: 1.03, duration: 0.3 }, 5.7);
        K.sfx(5.7, "success", 0.26);
        N.out([cap2], 5.7, { y: -10, d: 0.2 });
        const cap3 = N.cap("Réponse B.", { top: "140px" }, 5.9, { dark: true });
        const ans = N.ab("n-card", `<div style="padding:34px 40px"><div style="display:flex;align-items:center;gap:16px"><img src="assets/img/limo-house-ad.png" alt="" style="width:56px;height:56px;object-fit:contain" /><b style="font-size:28px;color:#6b4fe0">LIMO</b></div><div style="margin-top:14px;font-size:36px;line-height:1.38">Un DPE réalisé en 2020 <b>n’est plus valable depuis le 1er janvier 2025</b>. Il faut en refaire un avant la mise en vente.</div></div>`, { left: "90px", top: "1210px", width: "900px" });
        N.hide(ans);
        tl.fromTo(ans, { opacity: 0, y: 60 }, { opacity: 1, y: 0, duration: 0.5, ease: "power3.out" }, 6.4);
        K.sfx(6.4, "receive", 0.22);
        N.out(cap3, 8.6, { y: -10, d: 0.2 });
        const cap4 = N.cap("T’avais bon ?<br>Dis-le en commentaire.", { top: "140px" }, 8.8);
        N.out([cap4, q, ...opts, ans], 11.8);
        const h = N.head(["LIMO RÉPOND", "À TES QUESTIONS<span class='v'>.</span>"], { top: "560px", fontSize: "80px" }, 12.0, { bar: false });
        N.out(h, 13.1);
        window.__TE = 13.2;
        N.outro(13.2, "dm");
""")

# ---------------------------------------------------------------- 9 · l'anniversaire
FILMS["nat-09-anniversaire"] = ("L’anniversaire de Mme Roy", 16.2, "", """
        const cap1 = N.cap("Ta cliente de 2022 fête<br>son anniversaire aujourd’hui.", { top: "140px" }, 0.15);
        const ip = N.iphone({ left: "110px", top: "420px", width: "860px", height: "1460px" }, "9:30");
        N.hide(ip.el);
        tl.fromTo(ip.el, { opacity: 0, y: 300 }, { opacity: 1, y: 0, duration: 0.7, ease: "power3.out" }, 0.05);
        K.h("div", "n-mhead", `<div class="av">MR</div><b>Mme Roy</b>`, ip.screen);
        const th = K.h("div", "n-thread", null, ip.screen);
        K.h("div", "n-day", "Aujourd’hui · 9:30", th);
        const n0 = N.notif({ title: "ANNIVERSAIRE", text: "C’est l’anniversaire de Mme Roy. SMS prêt, tu veux l’envoyer ?" }, { left: "90px", top: "780px" }, 1.0);
        n0.setAttribute("data-layout-allow-overlap", "");
        const b1 = K.h("div", "n-bub out", "Bonjour Madame Roy, joyeux anniversaire ! Belle journée à vous.", th);
        N.hide(b1);
        tl.to(n0, { opacity: 0, y: -60, duration: 0.3, ease: "power2.in" }, 2.8);
        K.fin(b1, 3.0, { y: 20, d: 0.35 });
        K.sfx(3.0, "send", 0.24);
        N.out(cap1, 3.8, { y: -10, d: 0.2 });
        const cap2 = N.cap("10 minutes plus tard…", { top: "140px" }, 4.0, { dark: true });
        const dots = K.h("div", "n-dots", "<i></i><i></i><i></i>", th);
        N.hide(dots);
        tl.set(dots, { opacity: 1 }, 4.6);
        K.$$("i", dots).forEach((d, i) => tl.fromTo(d, { y: 0 }, { y: -8, duration: 0.14, yoyo: true, repeat: 3, ease: "sine.inOut" }, 4.65 + i * 0.07));
        tl.set(dots, { display: "none" }, 5.4);
        const b2 = K.h("div", "n-bub in", "Oh merci, c’est gentil ! D’ailleurs ma fille veut vendre son appartement. Je lui donne votre numéro ?", th);
        N.hide(b2);
        K.fin(b2, 5.4, { y: 20, d: 0.35 });
        K.sfx(5.4, "receive", 0.3);
        N.out(cap2, 6.6, { y: -10, d: 0.2 });
        const cap3 = N.cap("Un SMS.<br>Un nouveau mandat.", { top: "140px" }, 6.8, { dark: true });
        K.sfx(6.8, "thump", 0.3);
        N.out([cap3, ip.el], 8.8, { y: 60, d: 0.4 });
        const h = N.head(["LIMO N’OUBLIE", "PERSONNE<span class='v'>.</span>"], { top: "560px", fontSize: "96px" }, 9.1);
        const s = N.text("ctr n-body", "Anniversaires, relances, dates de signature :<br><b>tes clients se souviennent de toi.</b>", { top: "900px", fontSize: "36px" }, 9.9);
        N.out([h, s], 12.2);
        window.__TE = 12.6;
        N.outro(12.6, "essai");
""")

# ---------------------------------------------------------------- 10 · le collègue
FILMS["nat-10-ton-collegue"] = ("POV : ton collègue part à 18 h", 16.0, """
      .lock { position: absolute; inset: 0; background: linear-gradient(180deg, #8f7cf0 0%, #6b4fe0 45%, #2a2d6b 100%); }
      .lock .tm { position: absolute; left: 0; right: 0; top: 190px; text-align: center; font-family: Inter, sans-serif; font-weight: 700; font-size: 190px; color: #fff; letter-spacing: -0.02em; }
      .lock .dt { position: absolute; left: 0; right: 0; top: 150px; text-align: center; font-family: Inter, sans-serif; font-weight: 600; font-size: 34px; color: rgba(255,255,255,.9); }
""", """
        const cap1 = N.cap("POV : ton collègue part à 18 h…", { top: "140px" }, 0.15);
        const ip = N.iphone({ left: "110px", top: "400px", width: "860px", height: "1480px" }, "");
        N.hide(ip.el);
        tl.fromTo(ip.el, { opacity: 0, y: 300 }, { opacity: 1, y: 0, duration: 0.7, ease: "power3.out" }, 0.05);
        const lk = K.h("div", "lock", `<div class="dt">mardi</div><div class="tm">18:02</div>`, ip.screen);
        ip.screen.insertBefore(lk, ip.screen.firstChild);
        K.$(".n-status", ip.screen).style.color = "#fff";
        N.out(cap1, 1.9, { y: -10, d: 0.2 });
        const cap2 = N.cap("…et il signe plus de mandats que toi.", { top: "140px" }, 2.1, { dark: true });
        const L = [["BRIEF DE DEMAIN", "6 actions prêtes. On commence par M. Albert."], ["RELANCE", "Famille Martin : rappel programmé le 1er mars."], ["ANNONCE", "Maison Brive : annonce prête à publier."], ["AVIS GOOGLE", "Réponse à Marie L. publiée."]];
        const ns = L.map((l, i) => N.notif({ title: l[0], time: "18:0" + (i + 1), text: l[1], g: 0.18 }, { left: "140px", top: 900 + i * 190 + "px", width: "800px" }, 2.9 + i * 0.55));
        N.out(cap2, 5.4, { y: -10, d: 0.2 });
        const cap3 = N.cap("Son secret ?", { top: "140px" }, 5.6, { dark: true });
        K.sfx(5.6, "riser", 0.12, 0, { d: 0.8 });
        N.out([cap3, ip.el, ...ns], 7.2, { y: 40, d: 0.4 });
        const lg = N.ab("", `<img src="assets/img/limo-logo-ad.png" alt="LIMO" style="width:100%;height:100%" />`, { left: "190px", top: "620px", width: "700px", height: "265px" });
        N.hide(lg);
        tl.fromTo(lg, { opacity: 0, scale: 0.8 }, { opacity: 1, scale: 1, duration: 0.7, ease: "power3.out" }, 7.5);
        K.sfx(7.55, "thump", 0.4);
        const s = N.text("ctr n-body", "Son bras droit, c’est LIMO.<br><b>Et bientôt le tien.</b>", { top: "960px", fontSize: "44px" }, 8.3);
        N.out([lg, s], 10.8);
        window.__TE = 11.2;
        N.outro(11.2, "dm");
""")

if __name__ == "__main__":
    for name, (title, dur, css, body) in FILMS.items():
        html = SHELL.format(title=title, faces=FACES, css=css.strip("\n"), body=body.strip("\n"), dur=dur, name=name)
        pathlib.Path(f"reels/{name}.html").write_text(html, encoding="utf-8")
        print("reels/" + name + ".html")
