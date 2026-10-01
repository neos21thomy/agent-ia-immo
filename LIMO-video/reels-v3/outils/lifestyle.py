"""Films « lifestyle » sur images réelles fournies (plans Higgsfield, vidéos d'illustration, photos de biens) :
L1 Pendant ce temps, L2 POV le collègue, L3 Biens d'exception. Données fictives (exemples).

Usage : python3 outils/lifestyle.py   (réécrit reels/life-*.html)
"""
import pathlib

from cine import COMMON, FACES, GLASS, SHELL

V = lambda i, src, start, dur, track, ms=0: (f'      <video id="{i}" class="clip" src="assets/video/{src}.mp4" data-start="{start}" data-duration="{dur}"'
                                             + (f' data-media-start="{ms}"' if ms else "") + f' data-track-index="{track}" muted playsinline style="position:absolute;left:0;top:0;width:1080px;height:1920px;object-fit:cover"></video>\n')

# fond lavande caché tant que les images réelles sont à l'écran ; dégradé de lisibilité ; photo en Ken Burns
TOOLS = r"""
        tl.set([K.$(".n-bg", root), ...K.$$(".n-arc", root)], { opacity: 0 }, 0);
        const shade = (t0, t1) => { const s = C.ab({ left: "0", top: "0", width: "1080px", height: "1920px", background: "linear-gradient(180deg, rgba(5,6,15,.6) 0%, rgba(5,6,15,0) 32%, rgba(5,6,15,0) 55%, rgba(5,6,15,.6) 100%)" }); tl.set(s, { opacity: 0 }, 0); tl.set(s, { opacity: 1 }, t0); tl.set(s, { opacity: 0 }, t1); return s; };
        const photo = (src, t0, t1, z = [1.0, 1.12], x = [0, -60]) => {
          const p = C.ab({ left: "-67px", top: "-120px", width: "1215px", height: "2160px" }, `<img src="assets/img/${src}.jpg" alt="" style="width:100%;height:100%;object-fit:cover" />`);
          tl.set(p, { opacity: 0 }, 0);
          tl.fromTo(p, { opacity: 0, scale: z[0], x: x[0] }, { opacity: 1, duration: 0.4, ease: "power1.out" }, t0);
          tl.fromTo(p, { scale: z[0], x: x[0] }, { scale: z[1], x: x[1], duration: t1 - t0 + 0.4, ease: "none", immediateRender: false }, t0);
          tl.to(p, { opacity: 0, duration: 0.4, ease: "power1.in" }, t1);
          return p;
        };
        const gchip = (html, top, t, t1, cls = "") => {
          const c = C.ab({ left: "0", right: "0", top: top + "px", textAlign: "center" }, `<span class="gchip ${cls}">${html}</span>`);
          tl.set(c, { opacity: 0 }, 0);
          K.pop(c, t, { s: 0.7 });
          K.sfx(t, "pop", 0.14, 0, { f: 800 });
          if (t1) tl.to(c, { opacity: 0, duration: 0.25 }, t1);
          return c;
        };
        const gcard = (ic, big, small, top, t, t1) => {
          const c = C.ab({ left: "120px", width: "840px", top: top + "px", padding: "26px 32px", display: "flex", alignItems: "center", gap: "22px" }, `<span style="flex:none;width:80px;height:80px;border-radius:22px;background:rgba(44,196,181,.4);display:flex;align-items:center;justify-content:center">${K.icon(ic)}</span><span style="min-width:0"><b style="display:block;font-family:Montserrat,sans-serif;font-weight:800;font-size:40px;line-height:1.1">${big}</b><span style="font-size:27px;color:rgba(255,255,255,.85)">${small}</span></span><span style="margin-left:auto;flex:none;width:54px;height:54px;border-radius:50%;background:#2cc4b5;display:flex;align-items:center;justify-content:center">${K.icon("check")}</span>`);
          c.classList.add("glass");
          K.$$("svg.i", c).forEach((g) => (g.style.cssText = "width:42px;height:42px;color:#fff"));
          tl.set(c, { opacity: 0 }, 0);
          tl.fromTo(c, { opacity: 0, y: 50, scale: 0.95 }, { opacity: 1, y: 0, scale: 1, duration: 0.45, ease: "back.out(1.6)" }, t);
          K.sfx(t, "success", 0.2);
          if (t1) tl.to(c, { opacity: 0, y: -20, duration: 0.25 }, t1);
          return c;
        };
        const sms = (html, side, top, t, t1) => {
          const out = side === "out";
          const b = C.ab({ left: out ? "260px" : "90px", width: "730px", top: top + "px", padding: "22px 28px", borderRadius: "34px", background: out ? "#0a84ff" : "rgba(255,255,255,.96)", color: out ? "#fff" : "#111", fontFamily: "Inter, sans-serif", fontSize: "34px", lineHeight: "1.32", boxShadow: "0 20px 50px rgba(0,0,0,.3)" }, html);
          tl.set(b, { opacity: 0 }, 0);
          tl.fromTo(b, { opacity: 0, y: 30, scale: 0.94 }, { opacity: 1, y: 0, scale: 1, duration: 0.35, ease: "back.out(1.8)" }, t);
          K.sfx(t, out ? "send" : "receive", 0.26);
          if (t1) tl.to(b, { opacity: 0, duration: 0.25 }, t1);
          return b;
        };
        C.bars(2.6, true, 0.9);
        const lightEnd = (t) => {
          C.flash(t, "#ffffff", 0.95);
          const light = C.bg({ background: "linear-gradient(180deg, #f5f3fe 0%, #ece7fb 100%)" });
          tl.set(light, { clipPath: "circle(0px at 540px 960px)" }, 0);
          C.iris(light, t, 0.8);
          C.leak(t + 0.1, 2.4);
        };
"""

PRE = {}
FILMS = {}

# ---------------------------------------------------------------- L1 · pendant ce temps
PRE["life-01-pendant-ce-temps"] = (V("v1", "agent-voiture", 0, 5, 1) + V("v2", "vendeuse-canape", 5, 5, 2)
                                   + V("v3", "agent-voiture", 10, 2.5, 3, 2.5) + V("v4", "femme-vent", 20.5, 5.3, 4, 2))
FILMS["life-01-pendant-ce-temps"] = ("LIMO, pendant ce temps", 30.0, GLASS, TOOLS + r"""
        shade(0, 12.5);
        const t0 = C.title("Ce conseiller vient de décrocher", { top: "290px", fontSize: "50px" }, 0.02, { color: "#ffffff", snd: false });
        const t1 = C.title("un [mandat]… depuis sa [voiture].", { top: "370px", fontSize: "72px" }, 0.35, { color: "#ffffff", accent: "#d9ceff" });
        [t0, t1].forEach((e) => e.classList.add("shade"));
        C.out([t0, t1], 4.6, 0.3);
        const n1 = A.over(N.notif({ title: "ESTIMATION", time: "17:42", text: "Avis de valeur prêt pour Mme Roy : 245 000 – 262 000 €. Tu l’envoies ?" }, { left: "90px", top: "1180px" }, 1.6));
        const c1 = gchip(`${K.icon("send")}Envoyé à Mme Roy`, 1420, 3.4, 4.7, "ok");
        tl.to(n1, { opacity: 0, y: -30, duration: 0.25 }, 4.7);
        // ---- chez la vendeuse
        const t2 = C.title("Pendant ce temps, [Mme] [Roy]…", { top: "300px", fontSize: "70px" }, 5.2, { color: "#ffffff", accent: "#d9ceff" });
        t2.classList.add("shade");
        const s1 = sms("Bonjour Madame Roy, voici l’estimation de votre maison : <b>245 000 – 262 000 €</b>, appuyée sur le cadastre et les ventes du quartier.", "in", 1120, 5.8, 9.8);
        const s2 = sms("Merci, c’est très clair ! On peut se voir jeudi pour le mandat ?", "out", 1450, 8.0, 9.8);
        C.out(t2, 9.6, 0.3);
        // ---- retour dans la voiture
        const n2 = A.over(N.notif({ title: "AGENDA", time: "17:51", text: "Mme Roy : signature du mandat jeudi à 10 h.", snd: "success", g: 0.3 }, { left: "90px", top: "1180px" }, 10.4));
        tl.to(n2, { opacity: 0, duration: 0.25 }, 12.3);
        // ---- LIMO prépare la suite pendant qu'il conduit
        const P = [["bien-pierre-balcon", "pen", "Annonce rédigée", "optimisée SEO, mentions légales incluses"], ["bien-mas-lavande", "image", "18 photos signées", "prêtes à publier"], ["bien-lac", "sofa", "Home staging virtuel", "la pièce meublée en un clic"], ["bien-terrasse-mer", "megaphone", "3 posts prêts", "Instagram, Facebook, LinkedIn"]];
        const tt = C.title("Et pendant qu’il conduit, [LIMO]…", { top: "300px", fontSize: "66px" }, 12.7, { color: "#ffffff", accent: "#d9ceff" });
        tt.classList.add("shade");
        P.forEach((p, i) => {
          const a = 12.5 + i * 2.0;
          photo(p[0], a, a + 2.0, [1.02, 1.1], [i % 2 ? -40 : 40, 0]);
          gcard(p[1], p[2], p[3], 1380, a + 0.4, a + 1.85);
        });
        shade(12.5, 25.6);
        // le texte reste sous les nouvelles photos : on le remonte au premier plan
        root.appendChild(tt);
        C.out(tt, 20.2, 0.3);
        const t3 = C.title("Toi, tu reprends ton [temps].", { top: "1380px", fontSize: "84px" }, 21.2, { color: "#ffffff", accent: "#d9ceff" });
        t3.classList.add("shade");
        C.out(t3, 25.2, 0.3);
        // ---- fin
        lightEnd(25.6);
        window.__TE = 26.0;
        N.outro(26.0, "pub");
        const m = N.mascot({ left: "440px", top: "1240px", width: "200px" });
        m.enter(27.6);
        m.wave(28.3);
""")

# ---------------------------------------------------------------- L2 · POV le collègue
PRE["life-02-pov-collegue"] = V("v1", "ugc-selfie", 0, 13, 1)
FILMS["life-02-pov-collegue"] = ("LIMO, POV le collègue", 19.8, GLASS, TOOLS + r"""
        const cap = (html, t, t1) => { const c = N.cap(html, { top: "250px" }, t); A.over(c); if (t1) N.out(c, t1, { y: -10, d: 0.15 }); return c; };
        // première légende visible dès l'image 1 (vignette)
        const c0 = N.ab("ctr n-cap", `<span>POV : ton collègue te montre<br>pourquoi il finit à 18 h.</span>`, { top: "250px" });
        A.over(c0);
        tl.fromTo(K.$("span", c0), { scale: 1.06 }, { scale: 1, duration: 0.4, ease: "power3.out" }, 0);
        K.sfx(0, "pop", 0.2, 0, { f: 700 });
        N.out(c0, 2.8, { y: -10, d: 0.15 });
        cap("Il a <b>12 agents IA</b><br>qui bossent pour lui.", 3.0, 5.8);
        cap("Ils lui trouvent des vendeurs,<br>écrivent ses annonces…", 6.0, 8.8);
        cap("…et relancent ses clients<br><b>pendant qu’il fait visiter.</b>", 9.0, 12.6);
        const F = [["radar", "v", "3 vendeurs", "repérés ce matin", 30, 1180, 3.6], ["pen", "t", "Annonce prête", "en 2 minutes", 520, 1380, 6.6], ["refresh", "v", "32 relances", "envoyées", 30, 1580, 9.6]];
        F.forEach((f) => { const e = A.float(A.gain(f[0], f[1], f[2], f[3]), { left: f[4] + "px", top: f[5] + "px" }, f[6]); tl.to(e, { opacity: 0, duration: 0.3 }, 12.6); });
        lightEnd(12.9);
        const h = N.head(["ILS TRAVAILLENT<span class='v'>.</span>", "TU SIGNES<span class='v'>.</span>"], { top: "180px", fontSize: "80px" }, 13.3, { bar: false });
        glow(140, 520, 800, 13.3);
        const ph = A.phone({ left: "300px", top: "500px", width: "480px" }, { time: "17:58" });
        A.page(ph, A.S.home());
        A.enter(ph, 13.4, { flatAt: 0.8 });
        N.out(h, 15.6, { y: -30 });
        A.leave(ph, 15.6);
        window.__TE = 16.0;
        N.outro(16.0, "pub");
        const m = N.mascot({ left: "440px", top: "1240px", width: "200px" });
        m.enter(17.6);
        m.wave(18.3);
""")

# ---------------------------------------------------------------- L3 · biens d'exception
FILMS["life-03-biens-exception"] = ("LIMO, biens d'exception", 22.0, GLASS, TOOLS + r"""
        const dark = C.bg({ background: "#05060f" });
        const B = [
          ["bien-lac", 0.0, 3.2, null],
          ["bien-terrasse-mer", 3.2, 6.6, ["pin", "Estimation & marché", "1 250 000 – 1 320 000 €"]],
          ["bien-mas-lavande", 6.6, 10.0, ["pen", "Rédacteur d’annonce", "« Mas en pierre, verrière sur lavande »"]],
          ["bien-pierre-balcon", 10.0, 13.4, ["image", "Habilleur de photos", "18 photos signées à ton nom"]],
          ["bien-chalet", 13.4, 16.8, ["magnet", "Matcheur acheteurs", "7 acquéreurs compatibles"]],
        ];
        B.forEach((b, i) => {
          photo(b[0], b[1], b[2], i % 2 ? [1.12, 1.0] : [1.0, 1.12], [0, i % 2 ? 40 : -40]);
          if (b[3]) gcard(b[3][0], b[3][1], b[3][2], 1380, b[1] + 0.5, b[2] - 0.2);
          if (i) K.sfx(b[1], "whoosh", 0.12, 0, { d: 0.4, f0: 300, f1: 1800, pk: 0.5 });
        });
        shade(0, 16.8);
        const t0 = C.title("Agent immobilier,", { top: "320px", fontSize: "54px" }, 0.02, { color: "#d9ceff", snd: false });
        const t1 = C.title("tu vends des [lieux] [uniques].", { top: "400px", fontSize: "86px" }, 0.3, { color: "#ffffff", accent: "#d9ceff" });
        [t0, t1].forEach((e) => e.classList.add("shade"));
        C.out([t0, t1], 2.9, 0.3);
        const exemple = C.ab({ left: "0", right: "0", top: "1560px", textAlign: "center", fontFamily: "Inter, sans-serif", fontSize: "22px", color: "rgba(255,255,255,.7)" }, "Exemples fictifs");
        tl.set(exemple, { opacity: 0 }, 0);
        tl.set(exemple, { opacity: 1 }, 3.6);
        tl.set(exemple, { opacity: 0 }, 16.6);
        const t2 = C.title("Ils méritent un [bras] [droit].", { top: "380px", fontSize: "84px" }, 14.0, { color: "#ffffff", accent: "#d9ceff" });
        t2.classList.add("shade");
        C.out(t2, 16.6, 0.3);
        lightEnd(17.0);
        window.__TE = 17.4;
        N.outro(17.4, "pub");
        const m = N.mascot({ left: "440px", top: "1240px", width: "200px" });
        m.enter(19.0);
        m.wave(19.7);
""")

if __name__ == "__main__":
    for name, (title, dur, css, body) in FILMS.items():
        html = SHELL.format(title=title, faces=FACES, css=css.strip("\n"), body=(COMMON + body).strip("\n"), dur=dur, name=name)
        if name in PRE:
            html = html.replace('      <section id="s-main"', PRE[name] + '      <section id="s-main"', 1)
        pathlib.Path(f"reels/{name}.html").write_text(html, encoding="utf-8")
        print("reels/" + name + ".html")
