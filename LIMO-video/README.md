# LIMO — Reels Instagram en motion design

Tout le matériel des Reels de l'application **LIMO** (app.leadengineai.fr), réalisés avec
[HyperFrames](https://github.com/heygen-com/hyperframes) (la vidéo est une page HTML animée, rendue en MP4).

## 📁 Contenu

| Dossier | Ce qu'il contient |
|---|---|
| `rendus/v3/` | **Les 5 Reels viraux V3** (33 à 37 s, effets sonores, offre 14 jours) : ce sont les versions à publier |
| `rendus/` | `LIMO-reel-v2.mp4` : V2 (24,5 s, 4 outils, offre 14 jours). `LIMO-reel-v1.mp4` : 1re version (20 s, sans son, offre « 1 mois », **obsolète**). `apercus/` : planches d'images clés de chaque version |
| `reels-v3/` | Source des 5 Reels V3 : `reels/` (un fichier par Reel), `assets/kit/` (composants partagés), `outils/run.sh` (sons → contrôle → rendu). Mode d'emploi : `reels-v3/README.md` |
| `projet-hyperframes/` | Source de la V2 : `index.html` (la composition), `assets/` (polices, GSAP, robot détouré, photo, `audio/sfx.wav`), `outils/sfx.py` (générateur des effets sonores), `BRIEF.md`, `STORYBOARD.md` |
| `sources/` | Fichiers fournis : `images/` (affiche robot, logo, pubs, landing mobile) et `videos/` (pub « Analyseur de dossier », vidéo UGC IA) |
| `archives/` | Sources de la V1 (zip) |

## 📚 Catalogue de toutes les vidéos

- **`rendus/CATALOGUE.html`** : ouvre-le dans ton navigateur, toutes les vidéos se lisent sur une seule page (aperçu, accroche, fin, liens de téléchargement).
- **`rendus/CATALOGUE.md`** : le même catalogue, lisible directement sur GitHub.
- **`rendus/PROMPTS-MASCOTTE-GPT-HIGGSFIELD.md`** : prompts prêts à coller pour générer des images (ChatGPT) et des plans animés (Higgsfield) de la mascotte.
- Pour le mettre à jour : `cd reels-v3 && python3 outils/catalogue.py`.

## 🤖 Série « Mascotte » : 10 Reels (`rendus/mascotte/`), avec la mascotte officielle

La mascotte officielle (`sources/images/mascotte-limo-officielle.webp`) est animée : visière vidée, **yeux redessinés en SVG avec 12 expressions**
(content, ouverts, clin d'œil, ronds, triste, énervé, K.-O., cœurs, €, endormi, pensif, cligne), antenne qui s'allume, flottement, sauts, salut.
Elle parle en bulles avec des petits bips de robot. Chaque film fait de 14,6 à 17,6 s et existe en version bruitages seuls et en version `-musique`.

| # | Fichier `LIMO-mascotte-…` | Accroche | Fin |
|---|---|---|---|
| 1 | `01-salut-agent-immo` | « Ton nouvel assistant est arrivé. » Il se présente | Message privé « LIMO » |
| 2 | `02-entretien-embauche` | « Poste : assistant d'agent immo. » Tampon EMBAUCHÉ | Essai 14 jours |
| 3 | `03-3h-du-matin` | « 3 h du matin. Toi, tu dors. Lui, non. » | Essai 14 jours |
| 4 | `04-il-reagit` | « LIMO réagit à tes habitudes. » | Commentaire « LIMO » |
| 5 | `05-vrai-ou-faux` | « Vrai ou faux ? » (DPE, prix honoraires inclus) | Commentaire « LIMO » |
| 6 | `06-pendant-ton-cafe` | « Pendant ton café, j'ai fait ça. » | Démo 15 min |
| 7 | `07-ne-me-dis-pas` | « Ne me dis pas que tu fais encore ça… » | Message privé « LIMO » |
| 8 | `08-duel` | « Agent seul VS agent + LIMO » | Essai 14 jours |
| 9 | `09-pov-installation` | « POV : un agent immo m'installe. » | Message privé « LIMO » |
| 10 | `10-mieux-que-ton-stagiaire` | « 3 trucs que je fais mieux que ton stagiaire. » | Démo 15 min |

**Ordre conseillé** : 2, 4, 10, 3, 5, 1, 7, 9, 6, 8. L'entretien d'embauche (2) et « mieux que ton stagiaire » (10) sont les plus partageables.

Sources : `reels-v3/reels/mascotte-*.html`, générés par `reels-v3/outils/mascotte.py` (fonctions `N.mascot` et `N.say` du kit naturel).

## 🪝 Série « Hooks » : 10 Reels (`rendus/hooks/`), accroche lisible dès la 1re image

Même charte que la série naturelle. L'accroche est **déjà à l'écran sur la première image** (donc aussi sur la vignette),
en grandes capitales marine avec un mot surligné en violet. Elle s'adresse directement à l'agent immo.
Chaque film fait de 14 à 15,6 s et existe en version bruitages seuls et en version `-musique`.

| # | Fichier `LIMO-hook-…` | Hook (image 1) | Mécanique | Fin |
|---|---|---|---|---|
| 1 | `01-ia-remplace` | « L'IA va remplacer ~~les agents immo~~ » | Contre-pied : « seulement ceux qui ne l'utilisent pas » | Commentaire « LIMO » |
| 2 | `02-trois-agences` | « Ton vendeur a appelé 3 agences. » | Devinette : J+2 / +14 h / 4 min avec LIMO | Essai 14 jours |
| 3 | `03-dix-secondes` | « Agent immo ? Donne-moi 10 secondes. » | Compte à rebours, 6 tâches cochées | Démo 15 min |
| 4 | `04-red-flags` | « 3 red flags qui font fuir tes vendeurs. » | Tendance « red flags », chaque flag devient vert | Commentaire « LIMO » |
| 5 | `05-ton-concurrent` | « Ton concurrent utilise déjà ça. » | Téléphone flouté, « Tu veux voir ? », révélation | Message privé « LIMO » |
| 6 | `06-elle-vaut-combien` | « "Elle vaut combien, ma maison ?" » | Réponse en visite : fourchette en 30 s | Démo 15 min |
| 7 | `07-qui-va-vendre` | « Et si tu savais qui va vendre dans ta rue ? » | Carte Brive / Allassac / Voutezac, détecteur | Message privé « LIMO » |
| 8 | `08-avant-8h` | « Ce que font les agents qui signent le plus avant 8 h. » | Brief du jour prêt à 7 h 58 | Essai 14 jours |
| 9 | `09-ne-like-pas` | « Ne like pas cette vidéo… si tu aimes écrire tes annonces à 23 h. » | Psychologie inversée, puis « là, tu peux liker » | Commentaire « LIMO » |
| 10 | `10-le-test` | « Test : t'as besoin d'un assistant ? » | 5 situations cochées, score /5 | Message privé « LIMO » |

**Ordre conseillé** : 1, 4, 5, 2, 9, 7, 3, 10, 6, 8. Les 1, 4, 9 et 10 déclenchent le plus de commentaires,
et les 2, 5 et 7 sont les plus forts en publicité sponsorisée.
Les chiffres et les noms sont fictifs ; les écrans d'estimation et de carte portent la mention « Exemple fictif ».

**Couverture Instagram** : choisis l'image vers 1,5 s (le mot violet et la phrase sous le hook sont alors affichés).

Sources : `reels-v3/reels/hook-*.html`, générés par `reels-v3/outils/hooks.py` (fonctions `N.hook` et `N.chip` du kit naturel).

## 🌿 Série finale « LIMO naturel » : 10 Reels (`rendus/naturel/`), à publier en priorité

Même charte que les pubs LIMO : fond lavande, titres marine en capitales, point violet, trait turquoise, logo maison.
Les films utilisent des formats natifs (SMS, Notes, Contacts, notifications iPhone) et partent d'un moment vécu par tous les agents.
Chacun existe en version bruitages seuls et en version `-musique`.

| # | Fichier `LIMO-nat-…` | Accroche (première seconde) | Fin |
|---|---|---|---|
| 1 | `01-rappelez-moi-en-mars` | « Ce SMS, tout agent immo l'a déjà reçu. » « Rappelez-moi en mars. » Avril : signé ailleurs | Message privé « LIMO » |
| 2 | `02-dimanche-soir` | « Dimanche, 21 h 47. Ta tête est déjà à lundi. » Liste de notes cochée « fait par LIMO » | Essai 14 jours |
| 3 | `03-842-contacts` | « Ton CRM a 842 contacts. Combien t'en as rappelé ce mois-ci ? » 12 / 842 | Démo 15 min |
| 4 | `04-compromis-12-pages` | « 12 pages. Tu recopies encore tout ça à la main ? » | Démo 15 min |
| 5 | `05-note-vocale` | « Tu sors de visite. "Je noterai ça ce soir." » Spoiler : non | Essai 14 jours |
| 6 | `06-avis-sans-reponse` | « Ce client t'a laissé 5 étoiles… il y a 12 jours. » | Commentaire « LIMO » |
| 7 | `07-annonce-22h` | « 22 h 13. Toujours pas d'accroche pour l'annonce. » | Essai 14 jours |
| 8 | `08-quiz-dpe` | « Le DPE de 2020 est encore bon ? Tu réponds quoi ? » A/B/C, compte à rebours | Message privé « LIMO » |
| 9 | `09-anniversaire` | « Ta cliente de 2022 fête son anniversaire. » Un SMS, un nouveau mandat | Essai 14 jours |
| 10 | `10-ton-collegue` | « POV : ton collègue part à 18 h… et il signe plus de mandats que toi. » | Message privé « LIMO » |

**Ordre de publication conseillé** (un tous les 2 jours) : 1, 8, 10, 3, 5, 9, 4, 6, 2, 7.
Le quiz DPE (8) et « Ton collègue » (10) sont les plus partageables. Le 1 est le plus fort en pub.

Sources : `reels-v3/reels/nat-*.html`, générés par `reels-v3/outils/naturel.py` avec le kit `assets/kit/naturel.css` / `naturel.js`.

## 🎯 Campagne « 10 films » pour faire contacter les agents immo (`rendus/films/`)

Chaque film vise un levier différent et finit sur un **appel au contact**. Chacun existe en version bruitages seuls et en version `-musique`.

| # | Fichier | Durée | Levier | Accroche | Appel à l'action |
|---|---|---|---|---|---|
| 1 | `LIMO-film-01-mandat-perdu` | 19 s | Peur de perdre | SMS « on a signé avec une autre agence », on rembobine, avec LIMO : mandat signé | Message privé « LIMO » |
| 2 | `LIMO-film-02-dimanche-18h` | 16,2 s | Temps libre | 6 tâches tombent le dimanche, LIMO les coche toutes | Essai 14 jours |
| 3 | `LIMO-film-03-le-calcul` | 17,1 s | Rationnel | 6 h 45 perdues par semaine, ≈ 310 h par an (exemple indicatif) | Démo 15 min |
| 4 | `LIMO-film-04-fais-le-test` | 14,4 s | Identification | 5 situations cochées, score 5/5 | Commentaire « LIMO » |
| 5 | `LIMO-film-05-ton-telephone-bosse` | 14,8 s | Preuve | Les notifications LIMO de la journée sur le vrai écran | Essai 14 jours |
| 6 | `LIMO-film-06-tout-en-un` | 12 s | Simplicité | 11 outils qui s'assemblent dans la maison LIMO | Démo 15 min |
| 7 | `LIMO-film-07-mythes-realite` | 15,5 s | Objections | Trop compliqué, trop cher (dès 49 €/mois), l'IA va me remplacer | Message privé « LIMO » |
| 8 | `LIMO-film-08-manifeste` | 15,4 s | Émotion | « Tu n'es pas devenu agent immo pour remplir des cases. » | Essai 14 jours |
| 9 | `LIMO-film-09-prix-cafe` | 16 s | Prix | 49 €/mois = 1,63 €/jour, face à 10 000 € d'honoraires (exemple) | Essai 14 jours |
| 10 | `LIMO-film-10-visite-au-mandat` | 14,6 s | Démonstration | De la visite dictée au mandat signé, sans rien ressaisir | Démo 15 min |

**Pour que les contacts arrivent :**
- Messages privés et commentaires « LIMO » : réponds vite (automatise-le avec une réponse enregistrée ou ManyChat). Le film le promet : « je t'ouvre ton accès ».
- « Lien en bio » (films 3, 6 et 10) : mets le lien de réservation de démo en bio.
- En pub : commence par les films 1, 5 et 7 (peur, preuve, objections), puis garde celui qui a le coût par contact le plus bas.

Sources : `reels-v3/reels/film-*.html`, générés par `reels-v3/outils/films.py` avec le kit `assets/kit/premium.css` / `premium.js`.
Prix « dès 49 €/mois » : grille 49/79/119 €/mois du bilan LIMO. Les chiffres des films 3 et 9 sont affichés comme des exemples indicatifs.

## ⭐ Films premium (`rendus/premium/`) : à mettre en avant

Construits avec **les visuels fournis** : le vrai écran LIMO détouré de la pub « Ton CRM stocke », la maison lumineuse du logo et la photo du robot au bureau vue mer.
Il y a quatre fichiers : 22 s et 15 s, chacun en version bruitages seuls et en version `-musique`.

| Temps (22 s) | Scène |
|---|---|
| 0 – 2,9 s | « 21 H 47. Et tu recopies encore un compromis… » |
| 2,9 – 6,4 s | « Pendant que tu cherches qui relancer… » (photo du robot au bureau) « …d'autres ont déjà pris de l'avance. » |
| 6,4 – 13,3 s | Le vrai écran LIMO : notification « M. Albert attend ton rappel aujourd'hui », zoom sur « Nouveau mandat détecté » puis « Anniversaire client » |
| 13,3 – 16,4 s | « TON CRM STOCKE. LIMO TRAVAILLE. Plus aucune vente ne se perd par oubli. » |
| 16,4 – 18,4 s | La maison lumineuse, LIMO, chef de cabinet immo |
| 18,4 – 22,5 s | « Essaie-le 14 jours. » Bouton « Commencer gratuitement », sans carte bancaire, sans engagement |

Sources : `reels-v3/reels/premium-hero.html` et `premium-15s.html`. Nouveaux visuels dans `reels-v3/assets/img/` : `phone-limo.png`, `limo-house.png`, `bureau-robot.jpg`.

## 🚀 La V3 : 5 Reels, 5 formats viraux, les 11 outils à chaque fois

Chaque Reel montre **les 11 outils en situation** (brief du jour, dictée → fiche, compromis PDF → fiche,
estimation, annonce, posts réseaux, photo « VENDU », SMS anniversaire, avis Google, détecteur de ventes,
question juridique) et finit sur « 14 jours gratuits · sans CB ».

| Fichier (`rendus/v3/`) | Format | Durée | Ce qui accroche |
|---|---|---|---|
| `LIMO-v3-1-POV-journee.mp4` | POV « une journée avec » | 33,5 s | « POV : t'as un chef de cabinet IA. » L'horloge défile de 7 h 59 à 19 h 30, le téléphone enchaîne les outils, chute « Tout est fait. Tu rentres. » |
| `LIMO-v3-2-speedrun.mp4` | Speedrun / chrono | 33,1 s | Compte à rebours 3-2-1-GO, 11 manches chronométrées, « NOUVEAU RECORD », « Et toi, t'es à combien ? » (réponses en commentaire) |
| `LIMO-v3-3-sans-vs-avec.mp4` | Avant / après + score | 35,6 s | Écran partagé : la galère en haut (post-it perdu, 12 pages à recopier…), LIMO en bas, score 0-11, « Le match est plié. » |
| `LIMO-v3-4-conversation.mp4` | Conversation / chat | 35,3 s | « J'ai laissé mon IA gérer ma journée d'agent immo… » : chaque demande reçoit sa réponse, chute « T'es qui en fait ? » |
| `LIMO-v3-5-top-11.mp4` | Top / décompte (thème clair) | 37 s | « 11 tâches que tu ne feras plus jamais à la main », décompte 11 → 1, « Lequel tu testes en premier ? » |

### Versions 15 s ciblées agents immo (`rendus/v3-15s/`)

Mêmes 5 formats, recentrés sur les tâches du métier. Chaque accroche interpelle directement l'agent, et la carte de fin dit « L'IA des agents immo. ».

| Fichier | Durée | Accroche | Outils montrés |
|---|---|---|---|
| `LIMO-15s-1-POV-agent-immo.mp4` | 15,1 s | « POV : t'es agent immo. Zéro paperasse. » | Relances, compte rendu de visite dicté, compromis, annonce + mentions légales |
| `LIMO-15s-2-speedrun.mp4` | 14,9 s | « Speedrun : toute la paperasse d'un agent immo. » | Compte rendu de visite, compromis → fiche, avis de valeur |
| `LIMO-15s-3-sans-vs-avec.mp4` | 15 s | « Agent immo sans LIMO vs avec LIMO » | Relances vendeurs, saisie du compromis, vérification DPE |
| `LIMO-15s-4-conversation.mp4` | 14,5 s | « Agents immo : j'ai testé l'IA faite pour notre métier… » | Relances du jour, compromis PDF, question DPE |
| `LIMO-15s-5-top-3.mp4` | 15,2 s | « Agent immo ? 3 tâches que tu ne feras plus à la main. » | Compromis, annonces, relances |

Sources : `reels-v3/reels/short-*.html` (même chaîne `outils/run.sh short-1-pov`).

### Série « Conseiller augmenté » (`rendus/serie/`)

Une série en 5 niveaux qui avance d'épisode en épisode. Chaque vidéo s'ouvre sur une barre « NIVEAU X/5 ».

| Niveau | Fichier | Durée | Message |
|---|---|---|---|
| 1 · Le déclic | `LIMO-serie-niveau-1-le-declic.mp4` | 19,5 s | « En 2007, t'aurais refusé le smartphone ? » La frise fax → portails → smartphone → visite virtuelle → IA : à chaque époque, les outils ont été adoptés. « L'IA fait déjà partie de ta vie. Conseiller immo ? Utilise LIMO. » |
| 2 · Le constat | à venir | | Les IA grand public ne connaissent ni tes clients, ni tes mandats (citer ChatGPT/Gemini/Claude seulement si c'est vérifié) |
| 3 · La réponse | à venir | | LIMO : l'IA faite pour le métier |

Source : `reels-v3/reels/serie-n1-declic.html`.

### Versions avec musique (`rendus/v3-musique/`, `rendus/v3-15s-musique/`, `rendus/serie/*-musique.mp4`)

Chaque vidéo existe en deux versions : **bruitages seuls** (pour poser un son tendance dans Instagram) et **bruitages + musique** (suffixe `-musique`).
Les musiques sont composées par `reels-v3/outils/music.py`, synthétisées sans aucun échantillon externe, donc libres de droits.
Elles sont calées sur le rythme de chaque vidéo : intro filtrée pendant l'accroche, groove qui démarre à la fin de l'accroche, frappe finale sur la carte LIMO.

| Style | Vidéos |
|---|---|
| House 122 BPM | POV (long et 15 s) |
| Synthwave rapide 140 BPM | Speedrun (long et 15 s) |
| Trap 140 BPM | Sans vs Avec (long et 15 s) |
| Lo-fi 88 BPM | Conversation (long et 15 s) |
| Pop house 124 BPM | Top 11 / Top 3 |
| Montée cinématique 100 BPM, drop sur « L'IA fait déjà partie de ta vie » | Série niveau 1 |

Refaire une version : `python3 reels-v3/outils/music.py <reel> reels-v3/.sfx/<reel>.json reels-v3/assets/audio/<reel>.wav sortie.wav`, puis remplacer la piste audio du MP4 avec FFmpeg.

**Conseils de publication**

- Un Reel tous les 2-3 jours plutôt que les 5 d'un coup ; commencer par le 3 (avant/après), le plus parlant.
- Couverture : choisir dans Instagram l'image de l'accroche (première seconde).
- Les effets sonores sont intégrés. Pour ajouter une musique tendance dans Instagram, la mettre à 10-20 % du volume.
- Reels 2 et 5 : épingler un premier commentaire qui relance la question posée à la fin.

## 🎬 La V2 en bref (1080×1920, 30 i/s, 24,5 s)

| Temps | Scène |
|---|---|
| 0 – 2,7 s | Accroche « 8H00. Ta journée est déjà triée. » (horloge qui tourne, tic à chaque graduation) |
| 2,5 – 7 s | 01 · Brief du matin : écran verrouillé → notification LIMO → tap → 5 priorités, « Rappeler M. Albert » cochée |
| 7 – 11 s | 02 · Chat & dictée : le micro écoute, la bulle s'ouvre, LIMO met le dossier à jour |
| 11 – 14,5 s | 03 · Estimation : 389 000 €, fourchette, confiance 86 %, sources DVF / IGN / ADEME |
| 14,5 – 17,5 s | 04 · Détecteur de ventes : carte, 3 nouveaux DPE (F, G, E), nouvelle piste |
| 17,5 – 20,5 s | Avec LIMO : « Moins d'admin. Plus de terrain. » sur la photo du robot au bureau vue mer |
| 20,5 – 24,5 s | Fin : le logo se dessine et se pose sur le ventre du robot, LIMO, « 14 jours gratuits · sans CB » |

## 🔁 Refaire le rendu

Prérequis : Node.js 22+, FFmpeg, Python 3 avec `numpy` et `scipy`.

```bash
cd LIMO-video/projet-hyperframes
python3 outils/sfx.py                      # régénère les effets sonores (si les temps changent)
npx hyperframes@0.8.96 check .             # contrôle qualité (mise en page, contraste, animations)
npx hyperframes@0.8.96 render -o renders/LIMO-reel.mp4 -q delivery -f 30
```

## ✏️ Modifier

- **Timings** : bloc JSON `<script id="cues">` dans `index.html`. Les animations **et** les sons
  lisent ce même bloc : on décale une scène, on relance `outils/sfx.py`, tout reste synchronisé.
- **Textes** (accroche, titres, offre) : directement dans `index.html`.

## ⚖️ À savoir

- Données affichées **100 % fictives** (compte démo « Jean & Marie TYPE », noms d'exemple).
- Offre affichée dans les Reels : **14 jours gratuits, sans CB**. La landing page indiquait encore « Essayer gratuitement 1 mois » :
  à aligner avant de publier, sinon l'écart entre la pub et le site peut être reproché (publicité trompeuse).
- Posts réseaux : seul LinkedIn apparaît « Publié » (publication directe réelle) ; Instagram et Facebook sont « Prêts à publier ».
- Speedrun : la mention « Vidéo accélérée ×4 » reste affichée sous le chrono.
- Effets sonores **synthétisés** par `outils/sfx.py` : aucun échantillon externe, libres de droits.
- Polices Anton, Source Serif 4, Inter, Montserrat : licence SIL OFL. GSAP : licence standard gratuite.
- Le bilan interne LIMO (.docx) n'est **pas** versionné ici : ce dépôt est public.
- Ce dossier est exclu du déploiement du site (`.vercelignore` à la racine).
