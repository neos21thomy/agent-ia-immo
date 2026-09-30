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
