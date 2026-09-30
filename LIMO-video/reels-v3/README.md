# LIMO — 5 Reels viraux (V3)

Cinq Reels Instagram 1080×1920 (30 i/s, avec effets sonores) qui montrent **les 11 outils de LIMO en situation**,
chacun dans un format viral différent. Les MP4 finaux sont dans `../rendus/v3/`.

| # | Fichier source | Format viral | Durée | Accroche |
|---|---|---|---|---|
| 1 | `reels/reel-1-pov.html` | POV « une journée avec » | 33,5 s | « POV : t'as un chef de cabinet IA. » |
| 2 | `reels/reel-2-speedrun.html` | Speedrun / chrono gaming | 33,1 s | « SPEEDRUN — toute la paperasse d'un mandat. » |
| 3 | `reels/reel-3-avant-apres.html` | Avant / après en écran partagé + score | 35,6 s | « Conseiller immo SANS LIMO vs AVEC LIMO » |
| 4 | `reels/reel-4-conversation.html` | Conversation / chat | 35,3 s | « J'ai laissé mon IA gérer ma journée d'agent immo… » |
| 5 | `reels/reel-5-top11.html` | Top / liste en décompte (thème clair) | 37 s | « 11 tâches que tu ne feras plus jamais à la main. » |

Chaque Reel finit sur la même carte : robot LIMO, « Ton chef de cabinet IA. », **« 14 jours gratuits · sans CB »**, app.leadengineai.fr.

## Les 11 outils montrés (données fictives)

| Outil | Ce qu'on voit à l'écran |
|---|---|
| Brief du jour | 5 priorités, « Rappeler M. Albert » cochée, compteur 5 → 4 à faire |
| Dictée vocale → fiche | Note vocale « Visite Martin… » → fiche vendeur remplie |
| Compromis PDF → fiche | `Compromis_Roche.pdf` scanné → acquéreurs, notaire, prix, honoraires, anniversaire |
| Estimation | Compteur jusqu'à 312 000 €, fourchette, 14 ventes DVF, confiance 84 % |
| Annonce | Titre + texte tapés, mentions légales (honoraires, DPE, GES), badges SEO |
| Posts réseaux | Instagram et Facebook **prêts à publier**, LinkedIn **publié** (seule publication directe réelle) |
| Photo habillée | Tampon « VENDU », logo et coordonnées sur la photo |
| SMS anniversaire | Message à Mme Roy tapé puis envoyé |
| Avis Google | Avis 5 étoiles de Marie L. → réponse proposée puis publiée |
| Détecteur de ventes | Carte de Brive, 3 nouveaux DPE (F, G, E), nouvelle piste à boîter |
| Question juridique | « Le DPE de 2020 est encore valable ? » → non, plus valable depuis le 1er janvier 2025 |

## Fabriquer un Reel

Prérequis : Node.js 22+, FFmpeg, Chrome ou Chromium, Python 3 avec `numpy` et `scipy`.

```bash
cd LIMO-video/reels-v3
npm install                       # installe puppeteer-core (lecture des sons de la composition)
bash outils/run.sh reel-2-speedrun            # sons → contrôle → rendu dans renders/reel-2-speedrun.mp4
bash outils/run.sh reel-2-speedrun --check    # contrôle seulement
```

`outils/run.sh` enchaîne quatre étapes :

1. copie `reels/<reel>.html` en `index.html` (HyperFrames ne travaille que sur `index.html`) ;
2. `outils/extract-sfx.mjs` ouvre la page dans Chrome et récupère la liste des sons déclarés par les animations ;
3. `outils/sfx.py` synthétise la piste `assets/audio/<reel>.wav` (sons calés à la milliseconde, sans échantillon externe) ;
4. `hyperframes check` puis `hyperframes render`.

## Modifier

- **Textes, ordre des outils, rythme** : dans `reels/<reel>.html` (tableaux `BEATS`, `SPLITS`, `ROUNDS`, `X` ou `ITEMS` selon le Reel).
- **Composants** (brief, estimation, carte…) et carte de fin : `assets/kit/kit.js` et `assets/kit/kit.css`, partagés par les 5 Reels.
- **Durée** : si une modification allonge un Reel, `extract-sfx.mjs` affiche « fin à X s » ;
  la durée de la vidéo doit valoir X + 3 s (attributs `data-duration` et constante `D` du Reel).
- **Sons** : ils suivent les animations automatiquement ; relancer `outils/run.sh` suffit.

## À savoir

- Données 100 % fictives (Famille Martin, Mme Roy, Me Faure, 22 rue des Démonstrations…).
- Speedrun : mention « Vidéo accélérée ×4 » affichée en permanence sous le chrono.
- Polices Anton, Source Serif 4, Caveat, Inter, Montserrat, JetBrains Mono : licence SIL OFL. GSAP : licence standard gratuite.
