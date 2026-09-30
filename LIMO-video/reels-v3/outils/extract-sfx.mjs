// Ouvre une composition dans Chrome sans écran et récupère la liste des sons déclarés
// par les animations (window.__sfx, alimentée par K.sfx dans assets/kit/kit.js).
// Usage : node outils/extract-sfx.mjs reel-1-pov.html .sfx/reel-1-pov.json
import fs from "node:fs";
import path from "node:path";
import url from "node:url";
import puppeteer from "puppeteer-core";

const [, , htmlArg, outArg] = process.argv;
if (!htmlArg || !outArg) {
  console.error("Usage : node outils/extract-sfx.mjs <composition.html> <sortie.json>");
  process.exit(2);
}
// Navigateur : HYPERFRAMES_BROWSER_PATH ou CHROME_PATH s'ils sont définis, sinon le Google Chrome installé.
const executablePath = process.env.HYPERFRAMES_BROWSER_PATH || process.env.CHROME_PATH;
const where = executablePath ? { executablePath, headless: /headless[_-]shell/.test(executablePath) ? "shell" : true } : { channel: "chrome", headless: true };
const browser = await puppeteer.launch({ ...where, args: ["--no-sandbox", "--allow-file-access-from-files"] });
const page = await browser.newPage();
const errors = [];
page.on("pageerror", (e) => errors.push(String(e)));
await page.evaluateOnNewDocument(() => {
  window.__timelines = {};
});
await page.goto(url.pathToFileURL(path.resolve(htmlArg)).href, { waitUntil: "load" });
for (let i = 0; i < 200 && !(await page.evaluate(() => !!(window.__timelines && window.__timelines.main))); i++) {
  await new Promise((r) => setTimeout(r, 100));
}
const data = await page.evaluate(() => ({
  duration: parseFloat(document.getElementById("root").dataset.duration),
  timeline: window.__timelines.main ? window.__timelines.main.duration() : null,
  endCardAt: window.__TE ?? null,
  events: window.__sfx || [],
}));
await browser.close();
if (errors.length) {
  console.error("Erreurs JavaScript :\n" + errors.join("\n"));
  process.exit(1);
}
fs.mkdirSync(path.dirname(outArg), { recursive: true });
fs.writeFileSync(outArg, JSON.stringify(data));
console.log(`${data.events.length} sons → ${outArg} (vidéo ${data.duration} s, timeline ${data.timeline?.toFixed(2)} s, fin à ${data.endCardAt?.toFixed(2)} s)`);
