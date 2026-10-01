"""Dossier de tri : toutes les vidéos LIMO au même endroit, pour choisir celles à publier.

Crée LIMO-video/A-TRIER/ :
  1-cette-discussion/          toutes les vidéos rendues ici, à plat, préfixées par série (liens physiques : 0 octet en plus)
  2-autre-discussion-limo-app/ vidéos venues de l'autre discussion
  3-A-PUBLIER/, 4-A-JETER/     dossiers vides pour ranger à la main
  TRI.html                     page de tri : lire chaque vidéo, cliquer Publier / Peut-être / Non, copier la sélection
  LISTE-DE-TRI.md              la même liste en cases à cocher

Usage (depuis reels-v3/) : python3 outils/tri.py
"""
import html
import json
import os
import pathlib
import shutil
import subprocess

from catalogue import MUSIC_DIR, SERIES, R, dur

T = R.parent / "A-TRIER"
A = T / "1-cette-discussion"
B = T / "2-autre-discussion-limo-app"
VG = T / "vignettes"

PREFIX = {"pubs/9x16": "01-pub", "mascotte": "02-mascotte", "hooks": "03-hook", "naturel": "04-naturel", "films": "05-film",
          "premium": "06-premium", "serie": "07-serie", "v3-15s": "08-v3-15s", "v3": "09-v3-long", ".": "10-ancienne"}
OTHER = [("pub-analyseur-de-dossier", "Pub « Analyseur de dossier » (fournie)", "Vidéo de l'autre discussion"),
         ("ugc-ia-cafe", "Vidéo UGC IA au café (fournie)", "Vidéo de l'autre discussion")]


def link(src, dst):
    if dst.exists():
        dst.unlink()
    try:
        os.link(src, dst)
    except OSError:
        shutil.copy2(src, dst)


def thumb(src, name):
    t = VG / f"{name}.jpg"
    if not t.exists():
        subprocess.run(["ffmpeg", "-nostdin", "-y", "-loglevel", "error", "-ss", "1.5", "-i", str(src), "-frames:v", "1", "-vf", "scale=270:-2", "-q:v", "4", str(t)], check=True)
    return t.relative_to(T).as_posix()


def short(name):
    for p in ("LIMO-pub-", "LIMO-mascotte-", "LIMO-hook-", "LIMO-nat-", "LIMO-film-", "LIMO-premium-", "LIMO-serie-", "LIMO-15s-", "LIMO-v3-", "LIMO-"):
        if name.startswith(p):
            return name[len(p):]
    return name


def main():
    for d in (A, B, VG, T / "3-A-PUBLIER", T / "4-A-JETER"):
        d.mkdir(parents=True, exist_ok=True)
    items = []
    for folder, title, status, desc, vids in SERIES:
        pre = PREFIX[folder]
        for name, hook, cta in vids:
            src = R / folder / f"{name}.mp4"
            if not src.exists():
                continue
            base = f"{pre}_{short(name).replace('-9x16', '')}"
            versions = []
            if folder == "pubs/9x16":
                link(src, A / f"{base}_9x16.mp4")
                versions.append(("9:16", f"1-cette-discussion/{base}_9x16.mp4"))
                s45 = R / "pubs/4x5" / f"{name.replace('-9x16', '-4x5')}.mp4"
                if s45.exists():
                    link(s45, A / f"{base}_4x5.mp4")
                    versions.append(("4:5", f"1-cette-discussion/{base}_4x5.mp4"))
            else:
                link(src, A / f"{base}.mp4")
                versions.append(("Bruitages", f"1-cette-discussion/{base}.mp4"))
                sm = R / MUSIC_DIR.get(folder, folder) / f"{name}-musique.mp4"
                if sm.exists():
                    link(sm, A / f"{base}_musique.mp4")
                    versions.append(("Musique", f"1-cette-discussion/{base}_musique.mp4"))
            items.append(dict(id=base, serie=title, status=status, hook=hook, cta=cta, d=round(dur(src), 1), v=versions, thumb=thumb(src, base)))
    for name, title, note in OTHER:
        src = R.parent / "sources" / "videos" / f"{name}.mp4"
        if src.exists():
            link(src, B / f"{name}.mp4")
            items.append(dict(id=name, serie="📁 Autre discussion (LIMO app)", status="À trier", hook=title, cta=note, d=round(dur(src), 1),
                              v=[("Vidéo", f"2-autre-discussion-limo-app/{name}.mp4")], thumb=thumb(src, name)))
    nfiles = len(list(A.glob("*.mp4"))) + len(list(B.glob("*.mp4")))

    (B / "LISEZ-MOI.md").write_text(
        "# Vidéos de l'autre discussion (LIMO app)\n\n"
        "Les 2 vidéos ici sont celles que tu as envoyées au début de la discussion « Infos sur Limo ».\n\n"
        "Les vidéos créées dans l'autre discussion ne sont pas dans ce dépôt GitHub : je ne peux pas les récupérer moi-même.\n"
        "Pour les ajouter : télécharge-les depuis l'autre discussion et envoie-les dans celle-ci (ou demande à l'autre discussion\n"
        "de les pousser sur la branche `claude/youthful-dijkstra-mq852y`, dossier `LIMO-video/A-TRIER/2-autre-discussion-limo-app/`).\n"
        "Je les ajouterai ensuite à la page de tri.\n", encoding="utf-8")
    for d, txt in ((T / "3-A-PUBLIER", "Glisse ici les vidéos que tu gardes pour publier."), (T / "4-A-JETER", "Glisse ici les vidéos que tu ne gardes pas.")):
        (d / "LISEZ-MOI.txt").write_text(txt + "\n", encoding="utf-8")

    # ---------- liste à cocher
    md = ["# 🗂️ Liste de tri des vidéos LIMO", "",
          f"**{len(items)} vidéos** ({nfiles} fichiers) : coche ce que tu publies. Plus pratique : ouvre **`TRI.html`** dans ton navigateur.", "",
          "| Publier | Vidéo | Série | Durée | Accroche | Fin | Fichiers |", "|---|---|---|---|---|---|---|"]
    for it in items:
        files = " · ".join(f"[{k}]({p})" for k, p in it["v"])
        md.append(f"| ☐ | `{it['id']}` | {it['serie']} | {it['d']} s | {it['hook']} | {it['cta']} | {files} |")
    (T / "LISTE-DE-TRI.md").write_text("\n".join(md) + "\n", encoding="utf-8")

    # ---------- page de tri
    data = json.dumps(items, ensure_ascii=False)
    page = """<!doctype html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Tri des vidéos LIMO</title><style>
:root{--bg:#f4f2fc;--fg:#1b1f4b;--mut:#5d6285;--card:#fff;--line:#e4e0f5;--vio:#6b4fe0;--ok:#15877d;--may:#a8670a;--no:#c0282d}
@media (prefers-color-scheme:dark){:root{--bg:#12132a;--fg:#eceafd;--mut:#a9abc9;--card:#1d1f3d;--line:#2d2f55;--vio:#9d86ff;--ok:#4fd8c9;--may:#f2b25c;--no:#ff7b7f}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--fg);font:15px/1.45 system-ui,-apple-system,Segoe UI,sans-serif}
header{position:sticky;top:0;z-index:5;background:var(--bg);border-bottom:1px solid var(--line);padding:12px 16px}
.w{max-width:1240px;margin:0 auto}h1{font-size:22px;margin:0 0 4px}.sub{color:var(--mut);margin:0 0 10px;font-size:14px}
.bar{display:flex;flex-wrap:wrap;gap:8px;align-items:center}.tab{border:1px solid var(--line);background:var(--card);color:var(--fg);border-radius:20px;padding:6px 12px;cursor:pointer;font:inherit;font-size:14px}
.tab.on{background:var(--vio);border-color:var(--vio);color:#fff}select,.act{font:inherit;font-size:14px;border-radius:20px;border:1px solid var(--line);background:var(--card);color:var(--fg);padding:6px 12px}
.act{cursor:pointer}.act.p{background:var(--vio);color:#fff;border-color:var(--vio)}
main{padding:16px}.g{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:16px}
.c{background:var(--card);border-radius:16px;overflow:hidden;border:2px solid transparent;box-shadow:0 6px 18px rgba(27,31,75,.08);display:flex;flex-direction:column}
.c.s-pub{border-color:var(--ok)}.c.s-may{border-color:var(--may)}.c.s-no{opacity:.5}
video{width:100%;aspect-ratio:9/16;background:#000;display:block;object-fit:contain}.b{padding:10px 12px;display:flex;flex-direction:column;gap:6px;flex:1}
.id{font-weight:700;font-size:14px;word-break:break-word}.se{font-size:12px;color:var(--mut)}.h{font-size:13px;margin:0}.m{font-size:12px;color:var(--mut)}
.vs{display:flex;flex-wrap:wrap;gap:6px}.vs button{font:inherit;font-size:12px;border:1px solid var(--line);background:transparent;color:var(--vio);border-radius:12px;padding:2px 9px;cursor:pointer}.vs button.on{background:var(--vio);color:#fff}
.ch{display:grid;grid-template-columns:repeat(3,1fr);gap:6px;margin-top:auto}.ch button{font:inherit;font-size:13px;font-weight:600;border-radius:10px;border:1px solid var(--line);background:transparent;color:var(--fg);padding:8px 4px;cursor:pointer}
.ch .pub.on{background:var(--ok);border-color:var(--ok);color:#fff}.ch .may.on{background:var(--may);border-color:var(--may);color:#fff}.ch .no.on{background:var(--no);border-color:var(--no);color:#fff}
.cnt{font-size:13px;color:var(--mut);margin-left:auto}#toast{position:fixed;left:50%;bottom:20px;transform:translateX(-50%);background:var(--fg);color:var(--bg);padding:10px 16px;border-radius:12px;font-size:14px;display:none}
@media (max-width:520px){.g{grid-template-columns:repeat(2,1fr);gap:10px}.cnt{margin-left:0;width:100%}}
</style></head><body><header><div class="w"><h1>🗂️ Tri des vidéos LIMO</h1>
<p class="sub">Lis chaque vidéo, puis clique <b>Publier</b>, <b>Peut-être</b> ou <b>Non</b>. Tes choix restent enregistrés dans ce navigateur. « Copier ma sélection » copie la liste des vidéos à publier.</p>
<div class="bar" id="tabs"></div><div class="bar" style="margin-top:8px"><select id="serie"></select>
<button class="act p" id="copy">📋 Copier ma sélection</button><button class="act" id="reset">Tout remettre à zéro</button><span class="cnt" id="cnt"></span></div></div></header>
<main><div class="w g" id="grid"></div></main><div id="toast"></div>
<script>
const ITEMS = __DATA__;
const KEY = "limo-tri-v1";
let S = {}; try { S = JSON.parse(localStorage.getItem(KEY) || "{}") || {}; } catch (e) { S = {}; }
const save = () => { try { localStorage.setItem(KEY, JSON.stringify(S)); } catch (e) {} };
const LABEL = { all: "Toutes", todo: "Pas encore triées", pub: "✅ À publier", may: "🤔 Peut-être", no: "❌ Non" };
let tab = "all", serie = "";
const tabs = document.getElementById("tabs"), grid = document.getElementById("grid"), sel = document.getElementById("serie");
sel.innerHTML = '<option value="">Toutes les séries</option>' + [...new Set(ITEMS.map((i) => i.serie))].map((s) => `<option>${s}</option>`).join("");
sel.onchange = () => { serie = sel.value; draw(); };
function esc(s) { return String(s).replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" })[c]); }
function draw() {
  const n = { all: ITEMS.length, todo: 0, pub: 0, may: 0, no: 0 };
  ITEMS.forEach((i) => { const s = S[i.id]; if (s) n[s]++; else n.todo++; });
  tabs.innerHTML = Object.keys(LABEL).map((k) => `<button class="tab ${k === tab ? "on" : ""}" data-t="${k}">${LABEL[k]} (${n[k]})</button>`).join("");
  tabs.querySelectorAll(".tab").forEach((b) => (b.onclick = () => { tab = b.dataset.t; draw(); }));
  document.getElementById("cnt").textContent = `${n.pub} à publier · ${n.may} peut-être · ${n.no} non · ${n.todo} à trier`;
  const list = ITEMS.filter((i) => (!serie || i.serie === serie) && (tab === "all" || (tab === "todo" ? !S[i.id] : S[i.id] === tab)));
  grid.innerHTML = list.map((i) => `<article class="c ${S[i.id] ? "s-" + S[i.id] : ""}" data-id="${esc(i.id)}">
<video src="${esc(i.v[i.v.length - 1][1])}" poster="${esc(i.thumb)}" controls preload="none" playsinline></video>
<div class="b"><div class="id">${esc(i.id)}</div><div class="se">${esc(i.serie)}</div><p class="h">${esc(i.hook)}</p>
<div class="m">${i.d} s · ${esc(i.cta)}</div>
<div class="vs">${i.v.map((v, k) => `<button class="${k === i.v.length - 1 ? "on" : ""}" data-src="${esc(v[1])}">${esc(v[0])}</button>`).join("")}</div>
<div class="ch"><button class="pub ${S[i.id] === "pub" ? "on" : ""}" data-s="pub">Publier</button><button class="may ${S[i.id] === "may" ? "on" : ""}" data-s="may">Peut-être</button><button class="no ${S[i.id] === "no" ? "on" : ""}" data-s="no">Non</button></div></div></article>`).join("") || '<p class="sub">Aucune vidéo ici.</p>';
  grid.querySelectorAll(".c").forEach((c) => {
    const id = c.dataset.id, vid = c.querySelector("video");
    c.querySelectorAll(".vs button").forEach((b) => (b.onclick = () => { c.querySelectorAll(".vs button").forEach((x) => x.classList.remove("on")); b.classList.add("on"); vid.src = b.dataset.src; vid.play().catch(() => {}); }));
    c.querySelectorAll(".ch button").forEach((b) => (b.onclick = () => { S[id] = S[id] === b.dataset.s ? undefined : b.dataset.s; if (!S[id]) delete S[id]; save(); draw(); }));
  });
}
function toast(t) { const e = document.getElementById("toast"); e.textContent = t; e.style.display = "block"; setTimeout(() => (e.style.display = "none"), 2200); }
document.getElementById("copy").onclick = () => {
  const pub = ITEMS.filter((i) => S[i.id] === "pub"), may = ITEMS.filter((i) => S[i.id] === "may");
  const txt = "Vidéos LIMO à publier (" + pub.length + ") :\\n" + pub.map((i) => "- " + i.id + " : " + i.hook).join("\\n") + (may.length ? "\\n\\nPeut-être (" + may.length + ") :\\n" + may.map((i) => "- " + i.id).join("\\n") : "");
  (navigator.clipboard ? navigator.clipboard.writeText(txt) : Promise.reject()).then(() => toast("Sélection copiée : colle-la dans la discussion"), () => { prompt("Copie ta sélection :", txt); });
};
document.getElementById("reset").onclick = () => { if (confirm("Effacer tous tes choix ?")) { S = {}; save(); draw(); } };
draw();
</script></body></html>"""
    (T / "TRI.html").write_text(page.replace("__DATA__", data), encoding="utf-8")
    print(f"{len(items)} vidéos, {nfiles} fichiers → {T}")


if __name__ == "__main__":
    main()
