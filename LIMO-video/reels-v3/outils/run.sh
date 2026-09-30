#!/usr/bin/env bash
# Chaîne complète pour un Reel : sons → contrôle → rendu.
# Les sources sont dans reels/ ; HyperFrames ne travaille que sur index.html à la racine,
# donc le Reel choisi y est copié (les chemins assets/... sont relatifs à la racine).
# Usage : outils/run.sh reel-1-pov            (contrôle + rendu)
#         outils/run.sh reel-1-pov --check    (contrôle seulement)
set -euo pipefail
cd "$(dirname "$0")/.."
R="${1:?nom du reel, ex. reel-1-pov}"
cp "reels/$R.html" index.html
node outils/extract-sfx.mjs index.html ".sfx/$R.json"
python3 outils/sfx.py ".sfx/$R.json" "assets/audio/$R.wav"
npx --yes hyperframes@0.8.96 check .
if [ "${2:-}" != "--check" ]; then
  mkdir -p renders
  npx --yes hyperframes@0.8.96 render -o "renders/$R.mp4" -q delivery -f 30
fi
