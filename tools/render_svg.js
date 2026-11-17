// Render SVG figures to PNG for visual checking.
// Usage: node tools/render_svg.js figures/fig-01-1-x.svg [more.svg ...]   -> writes <out_dir>/<name>.png
// Output dir: $RENDER_OUT or ./build/figure-previews
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
(async () => {
  const out = process.env.RENDER_OUT || path.join(process.cwd(), 'build', 'figure-previews');
  fs.mkdirSync(out, { recursive: true });
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 900, height: 700 }, deviceScaleFactor: 1 });
  for (const f of process.argv.slice(2)) {
    const svg = fs.readFileSync(f, 'utf8');
    await p.setContent(`<html><body style="margin:0;background:#fff"><div id="w" style="width:800px;padding:10px">${svg}</div></body></html>`);
    await p.addStyleTag({ content: '#w svg{width:800px;height:auto;display:block}' });
    const el = await p.$('#w');
    const dst = path.join(out, path.basename(f).replace(/\.svg$/, '.png'));
    await el.screenshot({ path: dst });
    console.log(dst);
  }
  await b.close();
})();
