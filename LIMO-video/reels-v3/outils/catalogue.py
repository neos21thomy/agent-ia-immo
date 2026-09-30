"""Catalogue de toutes les vidéos LIMO : rendus/CATALOGUE.html (lecteur local) et rendus/CATALOGUE.md (GitHub).

Usage (depuis reels-v3/) : python3 outils/catalogue.py
Les vignettes sont extraites à 1,5 s dans rendus/apercus/vignettes/.
"""
import html
import pathlib
import subprocess

R = pathlib.Path(__file__).resolve().parents[2] / "rendus"
V = R / "apercus" / "vignettes"

# (dossier, titre, statut, description, [(fichier sans extension, accroche, appel à l'action)])
SERIES = [
    ("mascotte", "🤖 Série « Mascotte » : 10 Reels", "⭐ À publier en priorité",
     "La mascotte officielle LIMO parle aux agents immo : yeux animés (12 expressions), bulles, petits bips de robot. Charte lavande LIMO.",
     [("LIMO-mascotte-01-salut-agent-immo", "« Ton nouvel assistant est arrivé. » La mascotte se présente : annonces, relances, avis, brief", "Message privé « LIMO »"),
      ("LIMO-mascotte-02-entretien-embauche", "« Poste : assistant d'agent immo. » Entretien d'embauche : 24 h/24, congés ?, dès 49 €/mois, tampon EMBAUCHÉ", "Essai 14 jours"),
      ("LIMO-mascotte-03-3h-du-matin", "« 3 h du matin. Toi, tu dors. Lui, non. » Notifications de nuit, le jour se lève", "Essai 14 jours"),
      ("LIMO-mascotte-04-il-reagit", "« LIMO réagit à tes habitudes. » Yeux ronds, X, triste, énervé… puis « Laisse-moi faire »", "Commentaire « LIMO »"),
      ("LIMO-mascotte-05-vrai-ou-faux", "« Vrai ou faux ? » 2 questions (DPE 2019, prix honoraires inclus) avec explication", "Commentaire « LIMO »"),
      ("LIMO-mascotte-06-pendant-ton-cafe", "« Pendant ton café, j'ai fait ça. » Chrono 0:00 → 5:00, 6 tâches cochées", "Démo 15 min"),
      ("LIMO-mascotte-07-ne-me-dis-pas", "« Ne me dis pas que tu fais encore ça… » Post-it, Excel 2019, carnet : zappés", "Message privé « LIMO »"),
      ("LIMO-mascotte-08-duel", "« Agent seul VS agent + LIMO » Course de barres, 2 h 35 contre 9 min (temps indicatifs)", "Essai 14 jours"),
      ("LIMO-mascotte-09-pov-installation", "« POV : un agent immo m'installe. » 842 contacts, 37 relances, « Tu fais quoi de ton après-midi ? »", "Message privé « LIMO »"),
      ("LIMO-mascotte-10-mieux-que-ton-stagiaire", "« 3 trucs que je fais mieux que ton stagiaire. » Chute : « il fait très bien le café »", "Démo 15 min")]),
    ("hooks", "🪝 Série « Hooks » : 10 Reels", "⭐ À publier en priorité",
     "Accroche en grandes capitales lisible dès la première image (vignette), puis démo LIMO.",
     [("LIMO-hook-01-ia-remplace", "« L'IA va remplacer les agents immo (barré) » → seulement ceux qui ne l'utilisent pas", "Commentaire « LIMO »"),
      ("LIMO-hook-02-trois-agences", "« Ton vendeur a appelé 3 agences. » J+2 / +14 h / 4 min avec LIMO", "Essai 14 jours"),
      ("LIMO-hook-03-dix-secondes", "« Agent immo ? Donne-moi 10 secondes. » Compte à rebours, 6 tâches faites", "Démo 15 min"),
      ("LIMO-hook-04-red-flags", "« 3 red flags qui font fuir tes vendeurs. » Chaque flag rouge devient vert", "Commentaire « LIMO »"),
      ("LIMO-hook-05-ton-concurrent", "« Ton concurrent utilise déjà ça. » Téléphone flouté puis révélé", "Message privé « LIMO »"),
      ("LIMO-hook-06-elle-vaut-combien", "« Elle vaut combien, ma maison ? » Fourchette en 30 s pendant la visite", "Démo 15 min"),
      ("LIMO-hook-07-qui-va-vendre", "« Et si tu savais qui va vendre dans ta rue ? » Carte + détecteur", "Message privé « LIMO »"),
      ("LIMO-hook-08-avant-8h", "« Ce que font les agents qui signent le plus avant 8 h. » Brief du jour", "Essai 14 jours"),
      ("LIMO-hook-09-ne-like-pas", "« Ne like pas cette vidéo… si tu aimes écrire tes annonces à 23 h. »", "Commentaire « LIMO »"),
      ("LIMO-hook-10-le-test", "« Test : t'as besoin d'un assistant ? » 5 situations, score /5", "Message privé « LIMO »")]),
    ("naturel", "🌿 Série « LIMO naturel » : 10 Reels", "⭐ À publier",
     "Formats natifs iPhone (SMS, Notes, Contacts, notifications) partant d'un moment vécu par tous les agents.",
     [("LIMO-nat-01-rappelez-moi-en-mars", "« Ce SMS, tout agent immo l'a déjà reçu. » Rappelez-moi en mars → signé ailleurs", "Message privé « LIMO »"),
      ("LIMO-nat-02-dimanche-soir", "« Dimanche, 21 h 47. Ta tête est déjà à lundi. »", "Essai 14 jours"),
      ("LIMO-nat-03-842-contacts", "« Ton CRM a 842 contacts. Combien t'en as rappelé ? »", "Démo 15 min"),
      ("LIMO-nat-04-compromis-12-pages", "« 12 pages. Tu recopies encore tout ça à la main ? »", "Démo 15 min"),
      ("LIMO-nat-05-note-vocale", "« Tu sors de visite. “Je noterai ça ce soir.” »", "Essai 14 jours"),
      ("LIMO-nat-06-avis-sans-reponse", "« Ce client t'a laissé 5 étoiles… il y a 12 jours. »", "Commentaire « LIMO »"),
      ("LIMO-nat-07-annonce-22h", "« 22 h 13. Toujours pas d'accroche pour l'annonce. »", "Essai 14 jours"),
      ("LIMO-nat-08-quiz-dpe", "« Le DPE de 2020 est encore bon ? » Quiz A/B/C", "Message privé « LIMO »"),
      ("LIMO-nat-09-anniversaire", "« Ta cliente de 2022 fête son anniversaire. »", "Essai 14 jours"),
      ("LIMO-nat-10-ton-collegue", "« POV : ton collègue part à 18 h… et signe plus que toi. »", "Message privé « LIMO »")]),
    ("films", "🎯 Campagne « 10 films » (style sombre)", "Style ancien (sombre)",
     "Films de conversion, chacun sur un levier (peur, temps, calcul, preuve, prix…).",
     [("LIMO-film-01-mandat-perdu", "Peur de perdre : « on a signé avec une autre agence »", "Message privé « LIMO »"),
      ("LIMO-film-02-dimanche-18h", "Temps libre : 6 tâches du dimanche cochées", "Essai 14 jours"),
      ("LIMO-film-03-le-calcul", "Rationnel : 6 h 45 perdues par semaine (exemple)", "Démo 15 min"),
      ("LIMO-film-04-fais-le-test", "Identification : 5 situations, score 5/5", "Commentaire « LIMO »"),
      ("LIMO-film-05-ton-telephone-bosse", "Preuve : les notifications LIMO de la journée", "Essai 14 jours"),
      ("LIMO-film-06-tout-en-un", "Simplicité : 11 outils dans la maison LIMO", "Démo 15 min"),
      ("LIMO-film-07-mythes-realite", "Objections : compliqué, cher, remplacé", "Message privé « LIMO »"),
      ("LIMO-film-08-manifeste", "Émotion : « pas devenu agent immo pour remplir des cases »", "Essai 14 jours"),
      ("LIMO-film-09-prix-cafe", "Prix : 49 €/mois = 1,63 €/jour", "Essai 14 jours"),
      ("LIMO-film-10-visite-au-mandat", "Démonstration : de la visite dictée au mandat", "Démo 15 min")]),
    ("premium", "⭐ Films premium (style sombre)", "Style ancien (sombre)",
     "Avec les visuels fournis : vrai écran LIMO, maison lumineuse, robot au bureau vue mer.",
     [("LIMO-premium-22s", "« 21 h 47. Et tu recopies encore un compromis… »", "Essai 14 jours"),
      ("LIMO-premium-15s", "Version courte du film premium", "Essai 14 jours")]),
    ("serie", "📈 Série « Conseiller augmenté »", "Style ancien (sombre)",
     "Série évolutive en niveaux ; seul le niveau 1 est réalisé.",
     [("LIMO-serie-niveau-1-le-declic", "« En 2007, t'aurais refusé le smartphone ? » La frise des outils jusqu'à l'IA", "Essai 14 jours")]),
    ("v3-15s", "⚡ V3 en 15 s (style sombre)", "Style ancien (sombre)",
     "Les 5 formats V3 recentrés sur le métier. Versions musique dans v3-15s-musique/.",
     [("LIMO-15s-1-POV-agent-immo", "« POV : t'es agent immo. Zéro paperasse. »", "Essai 14 jours"),
      ("LIMO-15s-2-speedrun", "« Speedrun : toute la paperasse d'un agent immo. »", "Essai 14 jours"),
      ("LIMO-15s-3-sans-vs-avec", "« Agent immo sans LIMO vs avec LIMO »", "Essai 14 jours"),
      ("LIMO-15s-4-conversation", "« J'ai testé l'IA faite pour notre métier… »", "Essai 14 jours"),
      ("LIMO-15s-5-top-3", "« 3 tâches que tu ne feras plus à la main. »", "Essai 14 jours")]),
    ("v3", "🚀 V3 : 5 Reels longs (style sombre)", "Style ancien (sombre)",
     "33 à 37 s, les 11 outils à chaque fois. Versions musique dans v3-musique/.",
     [("LIMO-v3-1-POV-journee", "« POV : t'as un chef de cabinet IA. »", "Essai 14 jours"),
      ("LIMO-v3-2-speedrun", "Speedrun 3-2-1-GO, 11 manches", "Essai 14 jours"),
      ("LIMO-v3-3-sans-vs-avec", "Écran partagé galère / LIMO, score 0-11", "Essai 14 jours"),
      ("LIMO-v3-4-conversation", "« J'ai laissé mon IA gérer ma journée d'agent immo… »", "Essai 14 jours"),
      ("LIMO-v3-5-top-11", "« 11 tâches que tu ne feras plus jamais à la main »", "Essai 14 jours")]),
    (".", "🗄️ Premières versions", "Obsolète",
     "V1 annonce « 1 mois » (obsolète) ; V2 : 24,5 s, 4 outils, 14 jours.",
     [("LIMO-reel-v2", "V2 : brief, dictée, estimation, détecteur", "Essai 14 jours"),
      ("LIMO-reel-v1", "V1 (offre « 1 mois » : ne pas publier)", "—")]),
]
MUSIC_DIR = {"v3": "v3-musique", "v3-15s": "v3-15s-musique"}


def dur(p):
    out = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(p)], capture_output=True, text=True).stdout
    return float(out.strip() or 0)


def main():
    V.mkdir(parents=True, exist_ok=True)
    rows, total = [], 0
    for folder, title, status, desc, vids in SERIES:
        items = []
        for name, hook, cta in vids:
            f = R / folder / f"{name}.mp4"
            if not f.exists():
                print("absent :", f)
                continue
            mdir = MUSIC_DIR.get(folder, folder)
            fm = R / mdir / f"{name}-musique.mp4"
            thumb = V / f"{name}.jpg"
            if not thumb.exists():
                subprocess.run(["ffmpeg", "-nostdin", "-y", "-loglevel", "error", "-ss", "1.5", "-i", str(f), "-frames:v", "1", "-vf", "scale=270:480", "-q:v", "4", str(thumb)], check=True)
            rel = lambda p: p.relative_to(R).as_posix()
            items.append(dict(name=name, hook=hook, cta=cta, file=rel(f), music=rel(fm) if fm.exists() else None, thumb=rel(thumb), d=dur(f)))
            total += 1 + (1 if fm.exists() else 0)
        rows.append((folder, title, status, desc, items))

    # ---------- Markdown (lisible sur GitHub)
    md = ["# 🎬 Catalogue des vidéos LIMO", "",
          f"Toutes les vidéos Instagram (1080×1920, 30 i/s) de LIMO, au même endroit : **{total} fichiers MP4**.",
          "Chaque vidéo existe en version **bruitages seuls** (pour poser un son tendance dans Instagram) et, le plus souvent, en version **`-musique`**.",
          "Ouvre `CATALOGUE.html` dans ce dossier pour les regarder toutes directement dans ton navigateur.", "",
          "**Rappels :** essai **14 jours sans CB** (la landing indique encore « 1 mois » : à corriger) · noms et chiffres fictifs · prix « dès 49 €/mois ».", ""]
    md.append("| Série | Statut | Vidéos |\n|---|---|---|")
    for folder, title, status, desc, items in rows:
        md.append(f"| {title} | {status} | {len(items)} |")
    md.append("")
    for folder, title, status, desc, items in rows:
        md += [f"## {title}", "", f"**{status}** · {desc}", "", "| Aperçu | Vidéo | Durée | Accroche / contenu | Fin | Musique |", "|---|---|---|---|---|---|"]
        for it in items:
            mus = f"[▶ musique]({it['music']})" if it["music"] else "—"
            md.append(f"| <img src=\"{it['thumb']}\" width=\"90\"> | [{it['name']}]({it['file']}) | {it['d']:.1f} s | {it['hook']} | {it['cta']} | {mus} |")
        md.append("")
    (R / "CATALOGUE.md").write_text("\n".join(md), encoding="utf-8")

    # ---------- HTML (lecteur local)
    e = html.escape
    secs = []
    for folder, title, status, desc, items in rows:
        cards = "".join(
            f"""<article class="c"><video src="{e(it['file'])}" poster="{e(it['thumb'])}" controls preload="none" playsinline></video>
<div class="b"><h3>{e(it['name'].replace('LIMO-', ''))}</h3><p class="h">{e(it['hook'])}</p>
<p class="m"><span>{it['d']:.1f} s</span><span class="cta">{e(it['cta'])}</span></p>
<p class="l"><a href="{e(it['file'])}" download>Bruitages</a>{f'<a href="{e(it["music"])}" download>Musique</a>' if it['music'] else ''}</p></div></article>"""
            for it in items)
        tag = "prio" if "priorit" in status else ("old" if "Obsol" in status or "ancien" in status else "ok")
        secs.append(f"""<section><h2>{e(title)} <em class="{tag}">{e(status)}</em></h2><p class="d">{e(desc)} · dossier <code>{e(folder)}/</code></p><div class="g">{cards}</div></section>""")
    page = f"""<!doctype html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Catalogue vidéos LIMO</title><style>
:root{{--bg:#f4f2fc;--fg:#1b1f4b;--mut:#5d6285;--card:#fff;--vio:#6b4fe0;--teal:#15877d}}
@media (prefers-color-scheme:dark){{:root{{--bg:#12132a;--fg:#eceafd;--mut:#a9abc9;--card:#1d1f3d;--vio:#9d86ff;--teal:#4fd8c9}}}}
body{{margin:0;background:var(--bg);color:var(--fg);font:16px/1.45 system-ui,-apple-system,Segoe UI,sans-serif}}
header,section{{max-width:1200px;margin:0 auto;padding:16px}}
h1{{font-size:30px;margin:18px 0 6px}} h2{{font-size:22px;margin:28px 0 4px}} h3{{font-size:15px;margin:0 0 6px}}
.d,.intro{{color:var(--mut)}} em{{font-style:normal;font-size:12px;padding:3px 10px;border-radius:12px;margin-left:8px;vertical-align:3px}}
em.prio{{background:var(--vio);color:#fff}} em.ok{{background:rgba(44,196,181,.2);color:var(--teal)}} em.old{{background:rgba(127,127,127,.2);color:var(--mut)}}
.g{{display:grid;grid-template-columns:repeat(auto-fill,minmax(210px,1fr));gap:16px}}
.c{{background:var(--card);border-radius:18px;overflow:hidden;box-shadow:0 8px 24px rgba(27,31,75,.1)}}
video{{width:100%;aspect-ratio:9/16;display:block;background:#000}} .b{{padding:12px 14px}}
.h{{margin:0 0 8px;font-size:14px}} .m{{display:flex;justify-content:space-between;gap:8px;margin:0 0 8px;font-size:13px;color:var(--mut)}}
.cta{{color:var(--vio);font-weight:600}} .l a{{display:inline-block;margin-right:8px;font-size:13px;color:var(--vio)}}
</style></head><body><header><h1>🎬 Catalogue des vidéos LIMO</h1>
<p class="intro">{total} fichiers MP4 (1080×1920, 30 i/s). Clique sur une vidéo pour la lire. Les séries marquées « À publier en priorité » sont les plus récentes.
Essai <b>14 jours sans CB</b> · noms et chiffres fictifs.</p></header>{''.join(secs)}</body></html>"""
    (R / "CATALOGUE.html").write_text(page, encoding="utf-8")
    print(f"{total} vidéos → {R / 'CATALOGUE.md'} et CATALOGUE.html")


if __name__ == "__main__":
    main()
