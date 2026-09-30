# LIMO — Reels Instagram en motion design

Tout le matériel des Reels de l'application **LIMO** (app.leadengineai.fr), réalisés avec
[HyperFrames](https://github.com/heygen-com/hyperframes) (la vidéo est une page HTML animée, rendue en MP4).

## 📁 Contenu

| Dossier | Ce qu'il contient |
|---|---|
| `rendus/` | **`LIMO-reel-v2.mp4`** : version actuelle (24,5 s, effets sonores, offre 14 jours). `LIMO-reel-v1.mp4` : 1re version (20 s, sans son, offre « 1 mois », **obsolète**). `apercus/` : planches d'images clés |
| `projet-hyperframes/` | Source de la V2 : `index.html` (la composition), `assets/` (polices, GSAP, robot détouré, photo, `audio/sfx.wav`), `outils/sfx.py` (générateur des effets sonores), `BRIEF.md`, `STORYBOARD.md` |
| `sources/` | Fichiers fournis : `images/` (affiche robot, logo, pubs, landing mobile) et `videos/` (pub « Analyseur de dossier », vidéo UGC IA) |
| `archives/` | Sources de la V1 (zip) |

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
- Effets sonores **synthétisés** par `outils/sfx.py` : aucun échantillon externe, libres de droits.
- Polices Anton, Source Serif 4, Inter, Montserrat : licence SIL OFL. GSAP : licence standard gratuite.
- Le bilan interne LIMO (.docx) n'est **pas** versionné ici : ce dépôt est public.
- Ce dossier est exclu du déploiement du site (`.vercelignore` à la racine).
