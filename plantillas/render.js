// Convierte cada HTML de slide en PNG (1080×1424 por defecto, o el tamaño que se pase como "ANCHOxALTO").
const { chromium } = require('playwright');

(async () => {
  const trabajos = JSON.parse(process.argv[2]);
  const browser = await chromium.launch();
  const [w, h] = (process.argv[3] || '1080x1424').split('x').map(Number);
  const page = await browser.newPage({ viewport: { width: w, height: h } });
  for (const [html, png] of trabajos) {
    await page.goto('file://' + html);
    await page.waitForLoadState('networkidle');
    await page.evaluate(() => document.fonts.ready);
    await page.screenshot({ path: png });
  }
  await browser.close();
})();
