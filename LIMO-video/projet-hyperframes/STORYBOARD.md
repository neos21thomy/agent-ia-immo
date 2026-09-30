# STORYBOARD — LIMO Reel V2 (1080×1920, 30 fps, 24,5 s)

Composition monolithique (`index.html`) : le téléphone persiste sur les chapitres 1 à 4.
Tous les instants viennent du bloc JSON `<script id="cues">`, partagé avec `outils/sfx.py`.

## Frame 1 — Hook
status: animated
src: index.html#s-hook (0.00–2.75 s)
blueprint: kinetic-type-beats · rules: svg-path-draw (clock ring), waterfall-entry
beat: « 8H00. » dans un anneau cyan qui tourne ; « TA JOURNÉE / EST DÉJÀ TRIÉE. »
sound: tic à chaque graduation franchie, impact sourd d'ouverture, souffles sur les lignes.

## Frame 2 — Brief du matin
status: animated
src: index.html#s-app (2.50–7.05 s)
blueprint: device-surface-showcase + grid-card-assemble · rules: spring-pop-entrance, press-release-spring, svg-path-draw
beat: téléphone verrouillé (8:00) ; notification « Ton brief du matin est prêt » ; tap ; 5 cartes ; « Rappeler M. Albert » cochée ; 5 → 4 actions.
sound: montée du téléphone, carillon de notification, tap, pops des cartes, carillon de validation.

## Frame 3 — Chat & dictée
status: animated
src: index.html#s-app (7.05–11.05 s)
blueprint: prompt-type-submit-generate + agent-progress-theater · rules: card-morph-anchor (clip-path), sine-wave-loop
beat: pastille d'écoute (onde) qui s'ouvre en bulle ; LIMO répond ; 3 lignes cochées.
sound: bip micro, souffle de voix, mots, points de frappe, arpège de validation.

## Frame 4 — Estimation
status: animated
src: index.html#s-app (11.05–14.45 s)
blueprint: dataviz-countup · rules: counting-dynamic-scale, stat-bars-and-fills
beat: 389 000 € ; fourchette 372 000–405 000 € ; confiance 86 % ; sources.
sound: un tic par palier du compteur (même courbe que l'animation), carillon final.

## Frame 5 — Détecteur de ventes
status: animated
src: index.html#s-app (14.45–17.50 s)
rules: svg-path-draw, spring-pop-entrance, sine-wave-loop
beat: carte ; 3 nouveaux DPE (F, G, E) ; « Nouvelle piste » ; bouton Suivre.
sound: tracé de carte, sonar par épingle, pop du badge, tap.

## Frame 5b — Avec LIMO
status: animated
src: index.html#s-life (17.45–20.95 s)
rules: waterfall-entry, spring-pop-entrance, Ken Burns (scale lent)
beat: « MOINS D'ADMIN. / PLUS DE TERRAIN. » ; photo robot au bureau vue mer ; puces Relances prêtes · Estimations DVF · Suivi vendeur.
sound: souffle lumineux, nappe douce (accord fa maj7), pops des puces.

## Frame 6 — End card
status: animated
src: index.html#s-end (20.45–24.50 s)
blueprint: logo-assemble-lockup · rules: svg-path-draw, spring-pop-entrance, particle-burst
beat: le logo maison-réseau se dessine puis se pose sur le ventre du robot ; LIMO ; « Ton chef de cabinet IA. » ; « 14 jours gratuits · sans CB » ; app.leadengineai.fr
sound: montée, crépitement du réseau, impact + « boing » du robot, étincelles, carillon de l'offre.
