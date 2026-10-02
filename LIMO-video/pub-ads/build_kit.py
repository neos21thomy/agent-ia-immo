"""Construit KIT-PUB-LIMO.xlsx (pilotage + textes Meta/Google + mots-clés) et les CSV d'import Google Ads Editor."""
import csv
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import CellIsRule, FormulaRule
from openpyxl.comments import Comment

F = "Arial"
H = Font(name=F, bold=True, color="FFFFFF", size=11)
HF = PatternFill("solid", fgColor="2A1F6B")
T = Font(name=F, bold=True, size=16, color="2A1F6B")
B = Font(name=F, size=10)
BB = Font(name=F, size=10, bold=True)
IN = Font(name=F, size=10, color="0000FF")
YEL = PatternFill("solid", fgColor="FFF6C8")
SOFT = PatternFill("solid", fgColor="F1EEFC")
thin = Side(style="thin", color="D5D0EE")
BOX = Border(left=thin, right=thin, top=thin, bottom=thin)
WR = Alignment(wrap_text=True, vertical="top")

URL = "https://app.leadengineai.fr"
HYP = "'Hypothèses'"
wb = Workbook()


def header(ws, row, cols, widths=None):
    for i, c in enumerate(cols, 1):
        cell = ws.cell(row=row, column=i, value=c)
        cell.font, cell.fill, cell.border = H, HF, BOX
        cell.alignment = Alignment(wrap_text=True, vertical="center")
    if widths:
        for i, w in enumerate(widths, 1):
            ws.column_dimensions[chr(64 + i)].width = w
    ws.row_dimensions[row].height = 32


def body(ws, r0, r1, c1):
    for r in range(r0, r1 + 1):
        for c in range(1, c1 + 1):
            cell = ws.cell(row=r, column=c)
            cell.border = BOX
            cell.alignment = WR
            if cell.font.name != F:
                cell.font = B


# ---------------------------------------------------------------- 1. Mode d'emploi
ws = wb.active
ws.title = "Mode d'emploi"
ws["A1"] = "KIT PUB LIMO — Meta Ads + Google Ads"; ws["A1"].font = T
ws["A2"] = "Le bras droit du conseiller immo · Essai 14 jours sans CB · Dès 49 €/mois"; ws["A2"].font = Font(name=F, italic=True, size=10, color="6B4FE0")
rows = [
    ("Onglet", "À quoi il sert", "Quand l'utiliser"),
    ("Checklist", "Tout ce qu'il faut installer AVANT de dépenser 1 €", "Jour 1, une seule fois"),
    ("Hypothèses", "Ton prix, ta rétention, ton taux essai→payant → calcule ton coût max par essai", "Jour 1, puis chaque mois avec tes vrais chiffres"),
    ("Pilotage", "Tableau hebdo : tu tapes 8 chiffres par canal, il calcule tout et te dit quoi faire", "Chaque lundi, 10 min"),
    ("Meta - Annonces", "Textes prêts à coller pour chaque vidéo + lien avec UTM", "À la création des pubs"),
    ("Google - Annonces", "15 titres + 4 descriptions + extensions (longueurs vérifiées)", "À la création de la campagne Search"),
    ("Mots-clés", "Mots-clés par groupe d'annonces + CPC max de départ", "Création campagne, puis revue hebdo"),
    ("Exclusions", "Mots-clés négatifs à ajouter dès le départ", "Création campagne"),
]
for i, r in enumerate(rows):
    for j, v in enumerate(r):
        c = ws.cell(row=4 + i, column=j + 1, value=v)
        c.font = H if i == 0 else (BB if j == 0 else B)
        if i == 0: c.fill = HF
        c.border, c.alignment = BOX, WR
ws["A13"] = "Légende des couleurs"; ws["A13"].font = BB
ws["A14"] = "Texte bleu sur fond jaune"; ws["A14"].font = IN; ws["A14"].fill = YEL
ws["B14"] = "= cellule à remplir par toi (chiffres de tes comptes pub / de l'app)"; ws["B14"].font = B
ws["A15"] = "Texte noir"; ws["A15"].font = B
ws["B15"] = "= formule calculée automatiquement, ne pas toucher"; ws["B15"].font = B
ws["A17"] = "Les chiffres de départ (prix, rétention, taux) sont des hypothèses à remplacer par tes vrais chiffres dès que tu les as."
ws["A17"].font = Font(name=F, size=10, italic=True, color="AA0000")
for col, w in zip("ABC", (24, 70, 40)): ws.column_dimensions[col].width = w

# ---------------------------------------------------------------- 2. Checklist
ck = wb.create_sheet("Checklist")
ck["A1"] = "Checklist d'installation — à faire avant de lancer"; ck["A1"].font = T
header(ck, 3, ["#", "Domaine", "Étape (où / comment)", "Pourquoi", "Statut"], [5, 16, 80, 50, 14])
steps = [
    ("Landing page", "Remplacer toute mention « 1 mois » par « 14 jours, sans carte bancaire » (titre, bouton, FAQ)", "Même promesse pub = page, sinon conversion en chute et refus Meta possible"),
    ("Landing page", "Bouton « Réserver une démo de 15 min » visible + formulaire d'essai en moins de 3 champs", "Chaque champ en plus fait perdre des inscrits"),
    ("Landing page", "Mentions légales, politique de confidentialité et CGV accessibles en bas de page", "Obligatoire + vérifié par Meta et Google"),
    ("Cookies", "Bandeau de consentement compatible Consent Mode v2 (ex. Axeptio, Didomi, Cookiebot)", "Obligatoire en Europe (RGPD/CNIL) ; sans lui Google limite le suivi"),
    ("Meta", "Créer le Business Manager (business.facebook.com), y rattacher la Page LIMO + le compte Instagram", "Base de tout"),
    ("Meta", "Activer la double authentification sur ton compte et le Business Manager", "Évite le piratage du compte pub (fréquent)"),
    ("Meta", "Créer le compte publicitaire, devise EUR, fuseau Europe/Paris, moyen de paiement", "Fuseau et devise ne se changent plus ensuite"),
    ("Meta", "Vérifier le domaine leadengineai.fr (Paramètres de l'entreprise → Sécurité de la marque → Domaines)", "Nécessaire pour configurer les conversions"),
    ("Meta", "Installer le Pixel Meta sur app.leadengineai.fr (toutes les pages)", "Mesure les visites et conversions"),
    ("Meta", "Activer la Conversions API (via Gestionnaire d'événements, intégration partenaire ou serveur)", "Récupère les conversions perdues (iPhone, bloqueurs)"),
    ("Meta", "Événements : Lead (démo réservée), CompleteRegistration (essai démarré), Subscribe (passage payant)", "C'est ce que l'algorithme va optimiser"),
    ("Meta", "Tester les événements avec l'outil « Tester les événements » du Gestionnaire d'événements", "Ne jamais lancer sans voir les événements remonter"),
    ("Google", "Créer le compte Google Ads (mode Expert, pas le mode simplifié) + facturation", "Le mode simplifié lance des campagnes automatiques coûteuses"),
    ("Google", "Installer la balise Google (GA4) sur app.leadengineai.fr et lier GA4 ↔ Google Ads", "Mesure et audiences"),
    ("Google", "Créer les conversions : essai démarré (principale), démo réservée (principale), passage payant (secondaire au début)", "Pour que Google optimise sur les essais"),
    ("Google", "Activer les conversions améliorées (e-mail haché au moment de l'inscription)", "Meilleure attribution"),
    ("Google", "Vérifier le Consent Mode v2 avec Tag Assistant", "Sans ça, perte de données en Europe"),
    ("Suivi", "Utiliser les liens avec UTM de l'onglet « Meta - Annonces » pour chaque pub", "Savoir quelle pub amène des clients payants"),
    ("Suivi", "Dans l'app : noter la source UTM de chaque inscrit (champ caché du formulaire)", "Relier dépense pub et clients payants"),
    ("Conformité", "Pas de promesse chiffrée non prouvée (ex. « +30 % de mandats ») ; données d'exemple = fictives", "Règles Meta/Google sur les allégations + droit de la conso"),
    ("Conformité", "Photos de clients (film signatures) : accord écrit des personnes, même floutées", "Droit à l'image"),
]
for i, (a, b, c) in enumerate(steps):
    r = 4 + i
    ck.cell(row=r, column=1, value=i + 1)
    ck.cell(row=r, column=2, value=a)
    ck.cell(row=r, column=3, value=b)
    ck.cell(row=r, column=4, value=c)
    s = ck.cell(row=r, column=5, value="À faire"); s.font, s.fill = IN, YEL
body(ck, 4, 3 + len(steps), 4)
for r in range(4, 4 + len(steps)):
    ck.cell(row=r, column=5).border = BOX
dv = DataValidation(type="list", formula1='"À faire,En cours,Fait"', allow_blank=False)
ck.add_data_validation(dv); dv.add(f"E4:E{3 + len(steps)}")
ck.conditional_formatting.add(f"E4:E{3+len(steps)}", CellIsRule(operator="equal", formula=['"Fait"'], fill=PatternFill("solid", fgColor="CDEFE9"), font=Font(name=F, color="0B6E63", bold=True)))
n = 3 + len(steps)
ck.cell(row=n + 2, column=2, value="Avancement").font = BB
c = ck.cell(row=n + 2, column=3, value=f'=COUNTIF(E4:E{n},"Fait")/COUNTA(E4:E{n})'); c.number_format = "0%"; c.font = BB
ck.freeze_panes = "A4"

# ---------------------------------------------------------------- 3. Hypothèses
hy = wb.create_sheet("Hypothèses")
hy["A1"] = "Hypothèses économiques"; hy["A1"].font = T
header(hy, 3, ["Paramètre", "Valeur", "Note"], [46, 16, 70])
hyp = [
    ("Prix de l'abonnement (€/mois)", 49, "Prix d'entrée LIMO (« dès 49 €/mois »). Source : Thomy."),
    ("Durée moyenne d'abonnement (mois)", 12, "HYPOTHÈSE — à remplacer par ta rétention réelle après 3-6 mois."),
    ("Taux essai → payant", 0.25, "HYPOTHÈSE — à remplacer par ton taux réel (onglet Pilotage)."),
    ("Mois d'abonnement acceptés pour payer l'acquisition", 3, "Règle de prudence : on récupère sa dépense pub en 3 mois."),
]
for i, (a, v, note) in enumerate(hyp):
    r = 4 + i
    hy.cell(row=r, column=1, value=a).font = B
    c = hy.cell(row=r, column=2, value=v); c.font, c.fill = IN, YEL
    hy.cell(row=r, column=3, value=note).font = B
hy["B6"].number_format = "0%"; hy["B4"].number_format = '#,##0 "€"'
calc = [
    ("Valeur d'un client (€)", "=B4*B5", "Prix × durée moyenne"),
    ("Coût d'acquisition max par client payant (€)", "=B4*B7", "Ce que tu peux payer pour 1 client"),
    ("Coût max par essai démarré (€)", "=B10*B6", "KPI n°1 : à surveiller chaque semaine"),
    ("Seuil « à couper » d'une pub sans essai (€ dépensés)", "=B11*2", "Une pub qui a dépensé ça sans aucun essai → on l'arrête"),
]
for i, (a, f, note) in enumerate(calc):
    r = 9 + i
    hy.cell(row=r, column=1, value=a).font = BB
    c = hy.cell(row=r, column=2, value=f); c.font = BB; c.number_format = '#,##0 "€"'; c.fill = SOFT
    hy.cell(row=r, column=3, value=note).font = B
body(hy, 4, 7, 3); body(hy, 9, 12, 3)
hy["A8"] = "Résultats calculés"; hy["A8"].font = Font(name=F, bold=True, color="6B4FE0")

# ---------------------------------------------------------------- 4. Pilotage
pi = wb.create_sheet("Pilotage")
pi["A1"] = "Pilotage hebdomadaire — remplis les colonnes jaunes chaque lundi"; pi["A1"].font = T
cols = ["Semaine (lundi)", "Canal", "Dépense (€)", "Impressions", "Vues 3 s (Meta)", "Clics lien", "Essais démarrés", "Démos réservées", "Clients payants",
        "CPM (€)", "Taux de hook", "CTR", "Coût par clic (€)", "Taux clic → essai", "Coût par essai (€)", "Coût par client (€)", "Verdict"]
header(pi, 3, cols)
for i, w in enumerate([14, 10, 11, 12, 12, 10, 11, 11, 11, 9, 10, 8, 11, 11, 12, 12, 34], 1):
    pi.column_dimensions[pi.cell(row=3, column=i).column_letter].width = w
dvc = DataValidation(type="list", formula1='"Meta,Google"'); pi.add_data_validation(dvc)
import datetime
start = datetime.date(2026, 10, 5)
example = {4: ("Meta", 175, 21000, 6300, 230, 6, 2, 1), 5: ("Google", 70, 1400, None, 48, 3, 1, 0)}
for r in range(4, 4 + 26):
    wk = start + datetime.timedelta(weeks=(r - 4) // 2)
    canal = "Meta" if r % 2 == 0 else "Google"
    pi.cell(row=r, column=1, value=wk).number_format = "dd/mm/yyyy"
    pi.cell(row=r, column=2, value=canal)
    dvc.add(f"B{r}")
    ex = example.get(r)
    for j in range(3, 10):
        c = pi.cell(row=r, column=j, value=(ex[j - 2] if ex else None))
        c.font, c.fill = IN, YEL
        c.number_format = '#,##0 "€"' if j == 3 else "#,##0"
    pi.cell(row=r, column=10, value=f'=IF(D{r}>0,C{r}/D{r}*1000,"")').number_format = '0.00 "€"'
    pi.cell(row=r, column=11, value=f'=IF(AND(B{r}="Meta",D{r}>0,E{r}<>""),E{r}/D{r},"")').number_format = "0.0%"
    pi.cell(row=r, column=12, value=f'=IF(D{r}>0,F{r}/D{r},"")').number_format = "0.00%"
    pi.cell(row=r, column=13, value=f'=IF(F{r}>0,C{r}/F{r},"")').number_format = '0.00 "€"'
    pi.cell(row=r, column=14, value=f'=IF(F{r}>0,G{r}/F{r},"")').number_format = "0.0%"
    pi.cell(row=r, column=15, value=f'=IF(G{r}>0,C{r}/G{r},"")').number_format = '0.00 "€"'
    pi.cell(row=r, column=16, value=f'=IF(I{r}>0,C{r}/I{r},"")').number_format = '0 "€"'
    pi.cell(row=r, column=17, value=(
        f'=IF(C{r}="","",IF(G{r}=0,IF(C{r}>={HYP}!$B$12,"🔴 Aucun essai : changer de visuel/angle","⏳ Trop tôt, laisser tourner"),'
        f'IF(O{r}<={HYP}!$B$11*0.8,"🟢 Rentable : +20 % de budget",IF(O{r}<={HYP}!$B$11,"🟡 Correct : tester 2 nouveaux visuels","🔴 Trop cher : couper les pires pubs"))))'))
    for j in range(1, 18):
        c = pi.cell(row=r, column=j); c.border = BOX
        if j < 3 or j > 9: c.font = B
pi.cell(row=4, column=1).comment = Comment("Lignes 4-5 = EXEMPLE de saisie (chiffres fictifs). Remplace-les par tes vrais chiffres.", "LIMO")
last = 3 + 26
tr = last + 2
pi.cell(row=tr, column=1, value="TOTAL").font = BB
for canal_i, canal in enumerate(["Meta", "Google", "Tous"]):
    r = tr + canal_i
    pi.cell(row=r, column=2, value=canal).font = BB
    for j in range(3, 10):
        L = pi.cell(row=4, column=j).column_letter
        f = f"=SUM({L}4:{L}{last})" if canal == "Tous" else f'=SUMIFS({L}4:{L}{last},$B$4:$B${last},"{canal}")'
        c = pi.cell(row=r, column=j, value=f); c.font = BB; c.fill = SOFT
        c.number_format = '#,##0 "€"' if j == 3 else "#,##0"
    pi.cell(row=r, column=15, value=f'=IF(G{r}>0,C{r}/G{r},"")').number_format = '0.00 "€"'
    pi.cell(row=r, column=16, value=f'=IF(I{r}>0,C{r}/I{r},"")').number_format = '0 "€"'
    pi.cell(row=r, column=14, value=f'=IF(F{r}>0,G{r}/F{r},"")').number_format = "0.0%"
    for j in range(1, 18): pi.cell(row=r, column=j).border = BOX
rr = tr + 4
pi.cell(row=rr, column=1, value="Taux essai → payant réel").font = BB
c = pi.cell(row=rr, column=3, value=f"=IF(G{tr+2}>0,I{tr+2}/G{tr+2},\"\")"); c.number_format = "0.0%"; c.font = BB
pi.cell(row=rr, column=4, value="→ à reporter dans Hypothèses!B6 quand tu as au moins 20 essais").font = Font(name=F, italic=True, size=9)
pi.cell(row=rr + 1, column=1, value="Repères").font = BB
pi.cell(row=rr + 1, column=3, value="Taux de hook Meta : viser > 25 % · CTR lien Meta : viser > 1 % · CTR Google Search : viser > 4 %").font = Font(name=F, size=9, italic=True)
pi.conditional_formatting.add(f"K4:K{last}", CellIsRule(operator="lessThan", formula=["0.25"], font=Font(name=F, color="C00000", bold=True)))
pi.conditional_formatting.add(f"O4:O{last}", FormulaRule(formula=[f'AND(O4<>"",O4>{HYP}!$B$11)'], fill=PatternFill("solid", fgColor="FBD5D5")))
pi.conditional_formatting.add(f"O4:O{last}", FormulaRule(formula=[f'AND(O4<>"",O4<={HYP}!$B$11)'], fill=PatternFill("solid", fgColor="CDEFE9")))
pi.freeze_panes = "C4"

# ---------------------------------------------------------------- 5. Meta - Annonces
me = wb.create_sheet("Meta - Annonces")
me["A1"] = "Annonces Meta — textes prêts à coller (Facebook + Instagram)"; me["A1"].font = T
me["A2"] = "Rappel : 9:16 pour Reels/Stories + 4:5 pour le fil, dans la même annonce (« personnaliser le visuel par placement »)."; me["A2"].font = Font(name=F, italic=True, size=9)
header(me, 4, ["#", "Campagne", "Vidéo (fichier)", "Angle", "Texte principal", "Titre (≤ 40 car.)", "Description", "Bouton", "Lien avec UTM", "Nb car. titre"],
       [4, 16, 34, 18, 70, 30, 26, 16, 60, 9])
L = "\n"
ads = [
    ("A – Premium", "premium-pack/prem-02-trois-erreurs.mp4", "Liste · 3 erreurs (40 s)",
     f"Conseiller immo, voici 3 erreurs qui te font perdre des mandats 👇{L}{L}1️⃣ Tu rappelles trop tard après l'estimation{L}2️⃣ Tes relances sont dans ta tête{L}3️⃣ Tes soirées partent dans l'administratif{L}{L}Limo corrige les trois. Essai gratuit 14 jours, sans carte bancaire.",
     "Ne perds plus un mandat par oubli", "Le bras droit du conseiller immo", "S'inscrire", "prem-trois-erreurs"),
    ("A – Premium", "premium-pack/prem-03-dimanche-soir.mp4", "POV · dimanche soir (23 s)",
     f"Dimanche, 22 h. Tu ressors tes notes pour savoir qui rappeler… 😩{L}{L}Ton collègue, lui, regarde un film. Son secret ? Limo prépare sa semaine : relances, rendez-vous, dossiers.{L}{L}Reprends tes dimanches. 14 jours offerts, sans CB.",
     "Reprends tes dimanches", "Essai gratuit 14 jours", "S'inscrire", "prem-dimanche-soir"),
    ("A – Premium", "premium-pack/prem-04-le-calcul.mp4", "Rationnel · le calcul (28 s)",
     f"Fais le calcul : 1 h d'administratif par jour, c'est plus de 200 h par an ⏱️{L}{L}Limo s'occupe des relances, des comptes rendus, des annonces et du suivi des dossiers. Toi, tu retournes sur le terrain.{L}{L}Dès 49 €/mois · essai 14 jours sans carte bancaire.",
     "Récupère tes heures d'admin", "Dès 49 €/mois · sans engagement", "S'inscrire", "prem-le-calcul"),
    ("A – Premium (vague 2)", "premium-pack/prem-01-regarde-ca.mp4", "Démo · regarde ça (30 s)",
     f"Conseiller immo, regarde ça 👀{L}{L}Tu demandes « rappelle-moi le bien de M. et Mme T. »… et Limo te sort tout : documents, propriétaires, estimation, diagnostics.{L}{L}Pendant ce temps, il relance tes acquéreurs, ton diagnostiqueur et complète le dossier notaire.{L}{L}Teste-le 14 jours, sans carte bancaire.",
     "Ton assistant connaît tes biens", "Essai gratuit 14 jours", "S'inscrire", "prem-regarde-ca"),
    ("A – Premium (vague 2)", "premium-pack/prem-05-une-journee.mp4", "Démo · une journée (34 s)",
     f"8 h : tes priorités sont prêtes.{L}10 h : tu dictes ton compte rendu dans la voiture, la fiche est créée.{L}14 h : nouveau mandat ? L'annonce est rédigée en 2 minutes.{L}18 h : diagnostiqueur relancé, notaire servi.{L}{L}Et toi ? Tu as passé ta journée avec tes clients. 🏡{L}{L}Limo, le bras droit du conseiller immo. Essai gratuit 14 jours.",
     "Une journée avec Limo", "Le bras droit du conseiller immo", "S'inscrire", "prem-une-journee"),
    ("A – Acquisition", "voix/voix-03-surcharge.mp4", "Surcharge (10 s)",
     f"Conseiller immo, surchargé ?{L}{L}Appels manqués, relances oubliées, dossiers incomplets… LIMO s'en occupe pour toi.{L}{L}✅ Relances automatiques{L}✅ Dossiers suivis jusqu'au notaire{L}✅ Estimations et annonces en quelques minutes{L}{L}Essai gratuit 14 jours, sans carte bancaire.",
     "LIMO, le bras droit du conseiller", "Dès 49 €/mois · sans engagement", "S'inscrire", "surcharge"),
    ("A – Acquisition", "voix/voix-01-julien.mp4", "Storytelling (59 s)",
     f"Julien a fait une super estimation. Puis il a oublié de rappeler.{L}{L}Quelques jours plus tard, un autre panneau était sur la maison.{L}{L}Le mandat ne se perd pas pendant l'estimation. Il se perd APRÈS.{L}{L}LIMO garde le fil de chaque vendeur, chaque relance, chaque dossier.{L}{L}👉 Réserve ta démo de 15 min.",
     "Ne perds plus un mandat par oubli", "Démo gratuite de 15 min", "Réserver", "julien"),
    ("A – Acquisition", "voix/voix-02-regarde-ca.mp4", "Démo produit (30 s)",
     f"Conseiller immo, regarde ça 👀{L}{L}Tu demandes « rappelle-moi le bien de M. et Mme T. » → LIMO te sort la fiche complète : documents, diagnostics, propriétaires, estimation.{L}{L}Et pendant ce temps, il relance tes acquéreurs et ton diagnostiqueur.{L}{L}Teste-le 14 jours, sans CB.",
     "Toute ton activité, au même endroit", "Essai gratuit 14 jours", "S'inscrire", "regarde-ca"),
    ("A – Acquisition", "pubs-30s/LIMO-pub30-01-mandats-perdus-9x16.mp4", "Perte de mandats (30 s)",
     f"Combien de mandats as-tu perdus cette année… juste par manque de suivi ?{L}{L}LIMO relance tes vendeurs au bon moment, prépare tes estimations et garde tous tes dossiers à jour.{L}{L}Plus de temps sur le terrain, moins de temps sur l'administratif.{L}{L}Essai gratuit 14 jours, sans carte bancaire.",
     "Arrête de perdre des mandats", "Dès 49 €/mois", "S'inscrire", "mandats-perdus"),
    ("A – Acquisition", "lifestyle/LIMO-life-02-pov-collegue-9x16.mp4", "POV / humour",
     f"POV : ton collègue a l'air moins débordé que toi… et il rentre plus tôt 😅{L}{L}Son secret ? LIMO, le bras droit du conseiller immo.{L}{L}Relances, dossiers, annonces, estimations : c'est fait.{L}{L}14 jours pour tester, sans CB.",
     "Son secret ? LIMO.", "Essai gratuit 14 jours", "En savoir plus", "pov-collegue"),
    ("B – Relance", "signatures/sign-01-derriere-chaque-signature.mp4", "Émotion (32 s)",
     f"Le jour de la signature, on oublie tout le reste.{L}{L}Les appels du soir, les relances, les compromis, les diagnostics, les échanges avec le notaire…{L}{L}LIMO s'occupe du reste, pour un suivi ultra pro du mandat à la signature.{L}{L}👉 Réserve ta démo de 15 min.",
     "Du mandat à la signature, sans oubli", "Démo gratuite de 15 min", "Réserver", "signatures"),
    ("B – Relance", "cine/LIMO-cine-03-le-calcul-9x16.mp4", "Rationnel (temps/argent)",
     f"Fais le calcul : combien d'heures par semaine passes-tu sur l'administratif ?{L}{L}LIMO te les rend : relances, dossiers, annonces et estimations automatisés.{L}{L}Tu as déjà vu LIMO passer. Il ne te reste qu'à l'essayer : 14 jours, sans carte bancaire.",
     "Récupère tes heures d'admin", "Dès 49 €/mois · sans engagement", "S'inscrire", "le-calcul"),
]
for i, a in enumerate(ads):
    r = 5 + i
    utm = f"{URL}/?utm_source=meta&utm_medium=paid_social&utm_campaign={'acquisition' if a[0].startswith('A') else 'relance'}&utm_content={a[7]}"
    vals = [i + 1, a[0], a[1], a[2], a[3], a[4], a[5], a[6], utm]
    for j, v in enumerate(vals, 1): me.cell(row=r, column=j, value=v)
    me.cell(row=r, column=10, value=f"=LEN(F{r})")
    me.row_dimensions[r].height = 190
    assert len(a[4]) <= 40, a[4]
body(me, 5, 4 + len(ads), 10)
me.conditional_formatting.add(f"J5:J{4+len(ads)}", CellIsRule(operator="greaterThan", formula=["40"], fill=PatternFill("solid", fgColor="FBD5D5")))
me.freeze_panes = "A5"
r = 6 + len(ads)
me.cell(row=r, column=2, value="Réglages campagne A").font = BB
me.cell(row=r, column=5, value="Objectif Ventes · Conversion : CompleteRegistration · France · 25-60 ans · ciblage large (Advantage+) · placements Advantage+ · 20 €/jour · ne rien modifier 5-7 jours").font = B
me.cell(row=r + 1, column=2, value="Réglages campagne B").font = BB
me.cell(row=r + 1, column=5, value="Objectif Prospects · Conversion : Lead · Audiences : vidéo vue à 50 % + interactions Page/Insta + visiteurs site 30 j · EXCLURE les inscrits · 5-8 €/jour").font = B
for rr_ in (r, r + 1): me.cell(row=rr_, column=5).alignment = WR

# ---------------------------------------------------------------- 6. Google - Annonces
go = wb.create_sheet("Google - Annonces")
go["A1"] = "Google Ads Search — annonce responsive (RSA)"; go["A1"].font = T
go["A2"] = "Limites Google : titre ≤ 30 caractères · description ≤ 90 · chemin ≤ 15. La colonne « Nb car. » se colore en rouge si ça dépasse."; go["A2"].font = Font(name=F, italic=True, size=9)
header(go, 4, ["Type", "Texte", "Nb car.", "Limite", "Épingler ?"], [16, 70, 9, 8, 22])
heads = [
    ("LIMO, logiciel immo IA", "Position 1"),
    ("Le bras droit du conseiller", ""),
    ("Essai gratuit 14 jours", ""),
    ("Sans carte bancaire", ""),
    ("Dès 49 €/mois", ""),
    ("Relances vendeurs auto", ""),
    ("Ne perdez plus un mandat", ""),
    ("Dossiers suivis au notaire", ""),
    ("Estimations en 2 minutes", ""),
    ("Annonces rédigées pour vous", ""),
    ("Fait pour les mandataires", ""),
    ("Démo gratuite de 15 min", ""),
    ("Plus de temps sur le terrain", ""),
    ("Tout votre suivi centralisé", ""),
    ("Sans engagement", ""),
]
descs = [
    "Relances, dossiers, estimations, annonces : LIMO s'occupe du reste. 14 jours sans CB.",
    "Le bras droit des conseillers immobiliers indépendants. Dès 49 €/mois, sans engagement.",
    "Ne perdez plus un vendeur par oubli : LIMO vous rappelle qui relancer, quand et comment.",
    "Réservez une démo de 15 min et découvrez comment gagner des heures d'admin chaque semaine.",
]
r = 5
for h, pin in heads:
    go.cell(row=r, column=1, value="Titre"); go.cell(row=r, column=2, value=h)
    go.cell(row=r, column=3, value=f"=LEN(B{r})"); go.cell(row=r, column=4, value=30); go.cell(row=r, column=5, value=pin)
    r += 1
for d in descs:
    go.cell(row=r, column=1, value="Description"); go.cell(row=r, column=2, value=d)
    go.cell(row=r, column=3, value=f"=LEN(B{r})"); go.cell(row=r, column=4, value=90)
    r += 1
for p in ["logiciel", "conseiller-immo"]:
    go.cell(row=r, column=1, value="Chemin d'URL"); go.cell(row=r, column=2, value=p)
    go.cell(row=r, column=3, value=f"=LEN(B{r})"); go.cell(row=r, column=4, value=15)
    r += 1
go.cell(row=r, column=1, value="URL finale"); go.cell(row=r, column=2, value=f"{URL}/?utm_source=google&utm_medium=cpc&utm_campaign=search-{{_campagne}}&utm_term={{keyword}}")
go.cell(row=r, column=5, value="Remplace {_campagne} par un paramètre personnalisé ou le nom de campagne")
endr = r
body(go, 5, endr, 5)
go.conditional_formatting.add(f"C5:C{endr}", FormulaRule(formula=["AND(C5<>\"\",C5>D5)"], fill=PatternFill("solid", fgColor="FBD5D5")))
for h, _ in heads: assert len(h) <= 30, h
for d in descs: assert len(d) <= 90, (len(d), d)
r = endr + 2
go.cell(row=r, column=1, value="EXTENSIONS").font = BB
r += 1
header_row = r
for j, v in enumerate(["Type", "Texte", "Nb car.", "Limite", "Détail / URL"], 1):
    c = go.cell(row=r, column=j, value=v); c.font, c.fill, c.border = H, HF, BOX
r += 1
ext = [
    ("Lien annexe", "Réserver une démo", 25, "Démo de 15 min en visio · " + URL + "/demo"),
    ("Lien annexe", "Tarifs", 25, "Dès 49 €/mois, sans engagement · " + URL + "/tarifs"),
    ("Lien annexe", "Fonctionnalités", 25, "Relances, dossiers, estimations · " + URL + "/fonctionnalites"),
    ("Lien annexe", "Essai gratuit 14 jours", 25, "Sans carte bancaire · " + URL + "/inscription"),
    ("Accroche", "Sans carte bancaire", 25, ""),
    ("Accroche", "Sans engagement", 25, ""),
    ("Accroche", "Support en français", 25, ""),
    ("Accroche", "Prêt en 2 minutes", 25, ""),
    ("Extrait structuré (Services)", "Relances, Estimations, Annonces, Dossiers, Suivi notaire", 25, "Chaque valeur ≤ 25 car."),
]
for t, txt, lim, det in ext:
    go.cell(row=r, column=1, value=t); go.cell(row=r, column=2, value=txt)
    go.cell(row=r, column=3, value=f"=LEN(B{r})" if not t.startswith("Extrait") else "—"); go.cell(row=r, column=4, value=lim); go.cell(row=r, column=5, value=det)
    if not t.startswith("Extrait"): assert len(txt) <= lim, txt
    r += 1
body(go, header_row + 1, r - 1, 5)
go.cell(row=r + 1, column=1, value="⚠️").font = BB
go.cell(row=r + 1, column=2, value="Les pages /demo, /tarifs, /fonctionnalites, /inscription sont des suggestions : remplace-les par les vraies URL de ton site (ou la page d'accueil).").font = Font(name=F, italic=True, size=9, color="AA0000")

# ---------------------------------------------------------------- 7. Mots-clés
kw = wb.create_sheet("Mots-clés")
kw["A1"] = "Mots-clés Google Search — campagne « LIMO – Search »"; kw["A1"].font = T
kw["A2"] = "[exact] = correspondance exacte · \"expression\" = expression. Commence avec ça, pas de requête large au départ."; kw["A2"].font = Font(name=F, italic=True, size=9)
header(kw, 4, ["Groupe d'annonces", "Mot-clé", "Type", "CPC max départ (€)", "Statut"], [26, 46, 12, 18, 14])
KW = {
    "Logiciel métier": ["logiciel agent immobilier", "logiciel conseiller immobilier", "logiciel mandataire immobilier", "crm immobilier",
                        "crm agent immobilier", "logiciel immobilier indépendant", "outil conseiller immobilier", "application agent immobilier",
                        "logiciel gestion mandats immobilier", "logiciel suivi vendeurs immobilier"],
    "Douleurs": ["relance vendeur immobilier", "suivi mandat immobilier", "logiciel estimation immobilière", "rédiger annonce immobilière",
                 "outil relance prospects immobilier", "organisation agent immobilier", "gestion dossier vente immobilière"],
    "IA": ["ia agent immobilier", "intelligence artificielle immobilier", "assistant ia immobilier", "ia conseiller immobilier",
           "chatgpt agent immobilier", "outil ia immobilier"],
    "Marque": ["limo immobilier", "limo immo", "leadengine ai"],
}
r = 5
for g, lst in KW.items():
    for k in lst:
        for t in (["Exact", "Expression"] if g != "Marque" else ["Exact"]):
            kw.cell(row=r, column=1, value=g); kw.cell(row=r, column=2, value=k); kw.cell(row=r, column=3, value=t)
            c = kw.cell(row=r, column=4, value=(0.5 if g == "Marque" else 2.0)); c.font, c.fill = IN, YEL; c.number_format = '0.00 "€"'
            s = kw.cell(row=r, column=5, value="Actif"); s.font, s.fill = IN, YEL
            r += 1
body(kw, 5, r - 1, 3)
for rr_ in range(5, r):
    for j in (4, 5): kw.cell(row=rr_, column=j).border = BOX
kw.cell(row=r + 1, column=1, value="Note").font = BB
kw.cell(row=r + 1, column=2, value="CPC max de départ = HYPOTHÈSE prudente ; ajuste selon le « CPC moyen » réel après 1 semaine. Marque = campagne séparée à petit budget. « chatgpt agent immobilier » : l'annonce ne doit pas laisser entendre que LIMO inclut ChatGPT.").font = Font(name=F, italic=True, size=9)
kw.cell(row=r + 1, column=2).alignment = WR
kw.freeze_panes = "A5"
kw_rows = [(kw.cell(row=i, column=1).value, kw.cell(row=i, column=2).value, kw.cell(row=i, column=3).value, kw.cell(row=i, column=4).value) for i in range(5, r)]

# ---------------------------------------------------------------- 8. Exclusions
ex = wb.create_sheet("Exclusions")
ex["A1"] = "Mots-clés négatifs — niveau campagne (requête large négative)"; ex["A1"].font = T
header(ex, 3, ["Mot-clé négatif", "Raison"], [30, 60])
NEG = [("emploi", "Chercheurs d'emploi"), ("recrutement", "Chercheurs d'emploi"), ("salaire", "Chercheurs d'emploi"), ("devenir", "« devenir agent immobilier »"),
       ("formation", "Futurs agents, pas clients"), ("stage", "Étudiants"), ("cpf", "Formation"), ("bts", "Études"), ("diplôme", "Études"), ("école", "Études"),
       ("location", "Particuliers locataires"), ("louer", "Particuliers"), ("appartement", "Particuliers acheteurs"), ("maison à vendre", "Particuliers acheteurs"),
       ("achat maison", "Particuliers"), ("prix m2", "Particuliers"), ("notaire frais", "Particuliers"), ("crack", "Téléchargement illégal"),
       ("pdf", "Recherche de documents"), ("modèle", "Recherche de modèles gratuits"), ("définition", "Recherche informationnelle"), ("avis client", "Particuliers"),
       ("syndic", "Hors cible"), ("gestion locative", "Hors cible (à revoir si LIMO l'adresse)")]
for i, (k, why) in enumerate(NEG):
    ex.cell(row=4 + i, column=1, value=k); ex.cell(row=4 + i, column=2, value=why)
body(ex, 4, 3 + len(NEG), 2)
ex.cell(row=5 + len(NEG), column=1, value="Chaque semaine : Google Ads → Mots-clés → Termes de recherche → ajouter ici tout terme hors sujet.").font = Font(name=F, italic=True, size=9)

for s in wb.worksheets:
    s.sheet_view.showGridLines = False
from openpyxl.workbook.properties import CalcProperties
wb.calculation = CalcProperties(fullCalcOnLoad=True)
wb.save("KIT-PUB-LIMO.xlsx")

# ---------------------------------------------------------------- CSV Google Ads Editor
with open("import-google-ads-mots-cles.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["Campaign", "Ad group", "Keyword", "Criterion Type", "Max CPC"])
    for g, k, t, cpc in kw_rows:
        camp = "LIMO - Marque" if g == "Marque" else "LIMO - Search"
        w.writerow([camp, g, k, {"Exact": "Exact", "Expression": "Phrase"}[t], f"{cpc:.2f}"])
with open("import-google-ads-exclusions.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["Campaign", "Keyword", "Criterion Type"])
    for k, _ in NEG:
        w.writerow(["LIMO - Search", k, "Campaign negative broad"])
print("ok", len(kw_rows), "mots-clés")
