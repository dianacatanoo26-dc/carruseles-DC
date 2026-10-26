// Convierte cada HTML de slide en PNG de 1080×1424. Lo llama generar.py.
const { chromium } = require('playwright');

(async () => {
  const trabajos = JSON.parse(process.argv[2]);
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1424 } });
  for (const [html, png] of trabajos) {
    await page.goto('file://' + html);
    await page.waitForLoadState('networkidle');
    await page.evaluate(() => document.fonts.ready);
    await page.screenshot({ path: png });
  }
  await browser.close();
})();
