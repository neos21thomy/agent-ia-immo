# Visuels IA à générer pour les films LIMO (Higgsfield / ChatGPT / Kling…)

## Règles pour tous les plans
- **Format vertical 9:16** (1080×1920 minimum), vidéo de **5 à 8 s**, mouvement de caméra **lent**.
- **Aucun texte, aucun logo, aucune marque** à l'image (j'ajoute tout en motion design).
- Lumière naturelle, rendu « film » réaliste, pas d'aspect pub stock trop lisse.
- Décor **France / Corrèze** : maisons en pierre, toits d'ardoise, petites villes, campagne verte.
- **Garder les mêmes personnages** d'un plan à l'autre (même prompt de description, ou fonction « personnage » de Higgsfield) :
  - **Julien** : conseiller immobilier, 35 ans, cheveux châtains courts, barbe de 3 jours, chemise bleu clair, veste marine.
  - **Sophie** : conseillère immobilière, 40 ans, cheveux mi-longs châtains, pull beige, sourire chaleureux.
- Nom de fichier : numéro du plan (ex. `P03-dimanche-midi.mp4`).

---

## Priorité 1 · Les moments « au cœur » (scripts E1 à E6)

| # | Plan | Prompt (à coller, en anglais pour de meilleurs résultats) |
|---|---|---|
| P01 | Julien seul le soir devant l'ordinateur | `Vertical 9:16 cinematic shot, French real estate agent man 35, short brown hair, light stubble, light blue shirt, alone at a kitchen table at 11pm, laptop light on his tired face, papers around, dark warm house, children's drawings on the fridge in the background, slow push-in, realistic film look, no text` |
| P02 | Téléphone à côté de l'assiette, repas de famille | `Vertical 9:16, Sunday family lunch in a French countryside house, close-up of a smartphone vibrating next to a plate, blurred family laughing in the background, the father's hand hesitating to pick it up, natural window light, shallow depth of field, no text` |
| P03 | Panneau d'une autre agence devant une maison | `Vertical 9:16, old stone house in Corrèze France with slate roof, a generic "À VENDRE" sign on the gate without any brand, a man in a navy jacket stops on the sidewalk and looks at it, disappointed, overcast light, slow dolly, no logo` |
| P04 | Compromis qui tombe à l'eau | `Vertical 9:16, real estate agent woman 40, shoulder-length brown hair, beige sweater, reading a message on her phone in her car, her face falls, rain drops on the windshield, muted colors, cinematic, no text` |
| P05 | Remise des clés à une famille | `Vertical 9:16, emotional moment, real estate agent woman hands house keys to a young couple with a small child in front of a renovated stone house, golden hour, the couple smiles with emotion, slow motion close-up on the keys passing hands, no text` |
| P06 | Mains + trousseau de clés (gros plan) | `Vertical 9:16 macro shot, a set of house keys being placed in an open palm, warm golden light, bokeh background of a stone house entrance, slow motion, no text` |
| P07 | Julien au volant entre deux rendez-vous | `Vertical 9:16, real estate agent man 35, light blue shirt, driving through green French countryside roads, talking hands-free, relaxed smile, sunlight flickering through trees, inside-car shot, no text` |
| P08 | Estimation chez une vendeuse âgée | `Vertical 9:16, real estate agent woman sitting at a kitchen table with an elderly French woman, old photo albums open, the elderly woman tells a story, warm light, documents on the table, intimate and respectful, no text` |
| P09 | Ferme l'ordinateur, rejoint sa famille | `Vertical 9:16, man closes his laptop in the evening, stands up and walks to the living room where his kids are playing, warm lamp light, relieved smile, slow tracking shot, no text` |
| P10 | Seul dans un bureau vide | `Vertical 9:16, independent real estate agent alone in a small empty office at dusk, city lights outside the window, coffee cup, lots of files, quiet loneliness, cinematic blue hour, no text` |

## Priorité 2 · Ambiances pour les films « produit »

| # | Plan | Prompt |
|---|---|---|
| P11 | Brive / Corrèze vue du ciel | `Vertical 9:16 drone shot over a small French town with slate roofs and a church tower, Corrèze region, green hills, morning mist, slow forward motion, no text` |
| P12 | Visite d'une maison avec des acquéreurs | `Vertical 9:16, real estate agent man shows a bright living room to a couple, they look around delighted, sunlight through large windows, handheld natural movement, no text` |
| P13 | Poignée de main après signature | `Vertical 9:16, handshake between a real estate agent and a happy client in front of a notary office door, slow motion, warm daylight, no logo, no text` |
| P14 | Café du matin + planning | `Vertical 9:16, morning routine, real estate agent woman with coffee looking at her phone calmly, notebook and car keys on the table, soft morning light, peaceful, no text` |
| P15 | Fête d'anniversaire d'un client (lien avec la fonction anniversaires) | `Vertical 9:16, elderly man smiling while reading a birthday message on his phone in his garden, warm afternoon light, close-up, no text` |

## Images fixes (si pas de vidéo) · mêmes prompts, en photo 1080×1920
- Intérieurs de maisons de Corrèze (séjour pierre apparente, cuisine rénovée, chambre sous toit).
- Façades : maison en pierre, longère, villa moderne avec piscine, appartement centre-ville de Brive.
- Mains : signature d'un document, clés, stylo sur un compromis.

---

## Bonus : la mascotte
- La mascotte LIMO **dans des scènes réelles** (sur le bureau d'un conseiller, sur le tableau de bord d'une voiture, qui tend des clés…).
  Voir `rendus/PROMPTS-MASCOTTE-GPT-HIGGSFIELD.md`.
