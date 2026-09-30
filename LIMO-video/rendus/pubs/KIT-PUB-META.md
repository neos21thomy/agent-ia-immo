# 📣 Kit publicité Meta (Facebook + Instagram) : LIMO, essai 14 jours

6 publicités prêtes à importer dans le Gestionnaire de publicités Meta, chacune en **deux formats** :

| Format | Dossier | Emplacements |
|---|---|---|
| **9:16** (1080×1920) | `9x16/` | Reels, Stories (Instagram et Facebook) |
| **4:5** (1080×1350) | `4x5/` | Fil Instagram et Facebook, Explorer |

Toutes les pubs ont la musique intégrée. La carte de fin « **ESSAIE LIMO, 14 JOURS OFFERTS** » est remontée pour rester visible au-dessus du bouton de la pub et du texte Meta.

---

## ⚠️ 0. À corriger AVANT de lancer (sinon la pub contredit la page)

La landing `app.leadengineai.fr` affiche **« Essayer gratuitement 1 mois »**. Ce site n'est pas dans le dépôt auquel j'ai accès, donc la correction est à faire de ton côté :

- [ ] Remplacer le texte du bouton : « Essayer gratuitement 1 mois » → **« Essayer gratuitement 14 jours »**.
- [ ] Ajouter la mention sous le bouton : **« Sans carte bancaire · Sans engagement »**.
- [ ] Vérifier la durée d'essai réellement paramétrée dans l'outil de paiement ou d'inscription (ex. Stripe : `trial_period_days = 14`).
- [ ] Vérifier la même mention dans les e-mails de bienvenue, la page tarifs et les CGV.
- [ ] Installer le **pixel Meta** (ou l'API Conversions) sur l'app, avec l'événement **`CompleteRegistration`** à la création du compte d'essai.

---

## 🧱 1. Structure de campagne conseillée

| Élément | Réglage |
|---|---|
| Objectif | **Prospects** avec conversion sur le site (`CompleteRegistration`). Sans pixel : **Trafic**, optimisé sur les vues de page de destination |
| Budget | **20 €/jour** au niveau campagne (Advantage+ budget), 7 jours de test = 140 € |
| Ensemble de pubs | 1 seul au départ, audience large (voir ci-dessous) |
| Pubs | Les 6 ci-dessous, chacune avec ses deux formats (9:16 + 4:5) dans la même pub |
| Emplacements | Advantage+ (automatique) |
| Catégorie spéciale | Aucune en principe : LIMO est un logiciel pour pros, pas une offre de logement. Si Meta l'impose, choisir « Logement » (le ciblage sera simplement plus large) |

### 🎯 Audience

- **Lieu :** France (ou commencer par la Nouvelle-Aquitaine et l'Occitanie pour un test local, puis élargir).
- **Âge :** 25 – 60 ans.
- **Intérêts** (Advantage+ audience, en suggestions) : Immobilier, Agent immobilier, Mandataire immobilier, Négociation immobilière, Propriétés Privées, IAD France, SAFTI, Capifrance, Orpi, Century 21, SeLoger, Leboncoin Immobilier.
- **Exclusions :** tes clients actuels (liste e-mail) et les personnes déjà inscrites (audience pixel « CompleteRegistration » sur 180 jours).
- **Reciblage** (à ajouter après 7 jours, 5 €/jour) : personnes qui ont vu 50 % d'une vidéo ou visité la page sans s'inscrire. Pub à utiliser : `pub-04` (entretien d'embauche) ou `pub-06`.

---

## ✍️ 2. Les 6 publicités (textes prêts à coller)

URL de destination (à suivre dans les statistiques) :
`https://app.leadengineai.fr/?utm_source=meta&utm_medium=paid&utm_campaign=limo_essai14&utm_content=pubXX`
(remplace `pubXX` par `pub01`, `pub02`…)

### PUB 01 · « Ton vendeur a appelé 3 agences » (`LIMO-pub-01-trois-agences`)
- **Texte principal :** Ton vendeur a demandé une estimation à 3 agences hier soir. Il signera avec celle qui répond en premier. 📲
LIMO, ton chef de cabinet IA, te prépare la réponse en quelques minutes, même quand tu es en visite.
✅ 14 jours offerts · sans carte bancaire · sans engagement
- **Titre :** Réponds avant les autres agences
- **Description :** Essai gratuit 14 jours
- **Bouton :** S'inscrire

### PUB 02 · « Ton concurrent utilise déjà ça » (`LIMO-pub-02-ton-concurrent`)
- **Texte principal :** Ton concurrent a déjà son brief du matin, ses relances prêtes et ses annonces rédigées avant 9 h. Il ne te le dira pas. 🤫
LIMO, c'est le chef de cabinet IA des conseillers immobiliers.
✅ Teste-le 14 jours gratuitement, sans carte bancaire.
- **Titre :** Le secret des agents qui signent plus
- **Description :** 14 jours offerts, sans CB
- **Bouton :** En savoir plus

### PUB 03 · « Qui va vendre dans ta rue ? » (`LIMO-pub-03-qui-va-vendre`)
- **Texte principal :** Et si tu savais qui va vendre dans ton secteur avant les autres agences ? 📍
Le détecteur de LIMO repère les signaux de vente autour de toi et te dit qui appeler.
✅ Essai gratuit 14 jours · sans carte bancaire · sans engagement
- **Titre :** Appelle avant les autres agences
- **Description :** Détecteur de vendeurs inclus
- **Bouton :** S'inscrire

### PUB 04 · Mascotte « Entretien d'embauche » (`LIMO-pub-04-entretien-embauche`)
- **Texte principal :** On a fait passer un entretien à ton futur assistant. 🤖
Horaires : 24 h/24. Congés : jamais. Salaire : dès 49 €/mois.
Il écrit tes annonces, relance tes vendeurs et prépare ta journée.
✅ Embauche-le 14 jours gratuitement, sans carte bancaire.
- **Titre :** Ton assistant immo pour 49 €/mois
- **Description :** 14 jours offerts
- **Bouton :** S'inscrire

### PUB 05 · Mascotte « Mieux que ton stagiaire » (`LIMO-pub-05-mieux-que-ton-stagiaire`)
- **Texte principal :** 3 trucs que LIMO fait mieux que ton stagiaire : il ne dort jamais, il n'oublie aucune relance et il ne demande pas d'augmentation. 😄
(Garde quand même ton stagiaire : il fait très bien le café.)
✅ 14 jours gratuits · sans carte bancaire · sans engagement
- **Titre :** L'assistant IA des agents immo
- **Description :** Essai gratuit 14 jours
- **Bouton :** En savoir plus

### PUB 06 · « Rappelez-moi en mars » (`LIMO-pub-06-rappelez-moi-en-mars`)
- **Texte principal :** « Rappelez-moi en mars. » En avril : « On a signé avec une autre agence. » 😬
Ce n'est pas le prix qui t'a fait perdre ce mandat, c'est l'oubli.
LIMO te rappelle qui relancer, et quand. Tu n'oublies plus personne.
✅ 14 jours offerts, sans carte bancaire.
- **Titre :** Plus aucun mandat perdu par oubli
- **Description :** Essai gratuit 14 jours
- **Bouton :** S'inscrire

---

## 📊 3. Plan de test sur 7 jours

| Jour | Action |
|---|---|
| J1 | Lancer les 6 pubs, **ne rien toucher pendant 72 h** (phase d'apprentissage) |
| J4 | Couper les pubs avec un CTR (lien) < 0,8 % ou un taux d'accroche < 20 %, après 1 500 impressions minimum |
| J7 | Garder les 2 meilleures (coût par inscription le plus bas) et augmenter le budget de 20 % tous les 3 jours |
| J8 | Ajouter le reciblage (5 €/jour) |

**Indicateurs à suivre** (colonnes personnalisées du Gestionnaire) :

| Indicateur | Calcul | Objectif |
|---|---|---|
| Taux d'accroche | vues de 3 s ÷ impressions | > 25 % |
| Rétention | vues ThruPlay ÷ vues de 3 s | > 15 % |
| CTR (lien) | clics sur le lien ÷ impressions | > 1 % |
| Coût par inscription | dépense ÷ `CompleteRegistration` | à comparer à ta marge : 49 €/mois × durée d'abonnement moyenne |

---

## ⚖️ 4. Conformité

- L'offre annoncée (14 jours, sans CB, sans engagement) doit être **exactement** celle de la page d'inscription (voir la section 0).
- Les noms, chiffres et situations des vidéos sont **fictifs**. Les écrans d'estimation et de carte portent la mention « Exemple fictif », et les temps du duel sont « indicatifs ».
- N'ajoute pas de faux témoignages ni de résultats chiffrés non prouvés (« +40 % de mandats »…) dans les textes.
- Le prix « dès 49 €/mois » doit correspondre à la grille affichée sur le site.
- Les pubs sont diffusées au nom de ta page LeadEngine AI / LIMO, pas au nom de Propriétés Privées : n'utilise pas leur logo ni leur marque.
- Sources des vidéos : `reels-v3/reels/pub-*.html`, générées par `reels-v3/outils/pubs.py` à partir des Reels originaux.
