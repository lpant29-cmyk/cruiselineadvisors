// Screenshot + pre-push audit for cruiselineadvisors pages.
// Drives the Chrome already installed on this machine (no bundled download).
//
// Checks the operator's standing design rule, per page, at phone and desktop:
//   - horizontal scrolling on phone, and WHICH element causes it
//   - broken / zero-size images, and placeholder tokens left in the markup
//   - the same photo repeated inside one card strip
//   - a call button visible without scrolling
//   - fares older than MAX_AGE days, and any "from $" on an indexed page
//   - text sitting on a photo with no dark overlay behind it
//
// usage: node audit.js <out-dir> <label>=<url> [<label>=<url> ...]
const puppeteer = require('/tmp/shotkit/node_modules/puppeteer-core');

const CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
const MAX_AGE_DAYS = 3;
const VIEWPORTS = [
  { tag: 'phone', width: 390, height: 844, mobile: true },
  { tag: 'desk', width: 1280, height: 900, mobile: false },
];

const audit = (maxAgeDays) => {
  const vw = document.documentElement.clientWidth;
  const out = { vw, scrollW: document.documentElement.scrollWidth, overflowers: [] };

  // what actually sticks out past the viewport (ignore fixed/sticky bars)
  if (out.scrollW > vw + 1) {
    document.querySelectorAll('body *').forEach((el) => {
      const r = el.getBoundingClientRect();
      const pos = getComputedStyle(el).position;
      if (pos === 'fixed' || pos === 'sticky') return;
      // An element inside a deliberate horizontal scroller (e.g. a wide facts
      // table in .cmp-scroll{overflow-x:auto}) is contained by design and does
      // not scroll the page. Flagging those buries the one element that does.
      for (let a = el.parentElement; a && a !== document.body; a = a.parentElement) {
        const ox = getComputedStyle(a).overflowX;
        if (ox === 'auto' || ox === 'scroll' || ox === 'hidden') return;
      }
      if (r.width === 0 || r.right <= vw + 1) return;
      if (el.querySelector('*') && [...el.children].some((c) => c.getBoundingClientRect().right > vw + 1)) return;
      out.overflowers.push({
        tag: el.tagName.toLowerCase(),
        cls: (el.className && el.className.toString().slice(0, 60)) || '',
        right: Math.round(r.right), w: Math.round(r.width),
        text: (el.textContent || '').trim().slice(0, 50),
      });
    });
    out.overflowers = out.overflowers.slice(0, 8);
  }

  // images
  const imgs = [...document.images];
  out.imgTotal = imgs.length;
  // naturalWidth is 0 for a lazy image that simply has not entered the viewport
  // yet, which made every below-the-fold photo look broken. Report the srcs and
  // let the node side settle it with a real HTTP request.
  out.imgSrcs = [...new Set(imgs.map((i) => i.getAttribute('src')).filter(Boolean))];
  out.imgBroken = [];
  // same photo repeated inside one strip/grid
  out.repeatedInStrip = [];
  document.querySelectorAll('.sgrid, .dealgrid, #dealGrid, .cards, .strip, .rowlist').forEach((grid) => {
    const srcs = [...grid.querySelectorAll('img')].map((i) => i.getAttribute('src'));
    const dupes = srcs.filter((s, i) => s && srcs.indexOf(s) !== i);
    if (dupes.length) {
      out.repeatedInStrip.push({ grid: grid.className || grid.id, dupes: [...new Set(dupes)].slice(0, 3) });
    }
  });

  // placeholder tokens that must never reach a built page
  const html = document.documentElement.outerHTML;
  out.tokens = ['IMG SLOT', 'asset:', 'Not yet verified', 'No verificado', 'VERIFY-BEFORE-PUBLISH',
    'Lorem ipsum', '[Your Company]', 'example.com']
    .filter((t) => html.includes(t));

  // a call action visible in the first screen, without scrolling
  const tel = [...document.querySelectorAll('a[href^="tel:"]')];
  out.telTotal = tel.length;
  out.telAboveFold = tel.filter((a) => {
    const r = a.getBoundingClientRect();
    return r.top < window.innerHeight && r.bottom > 0 && r.width > 0 && r.height > 0;
  }).length;
  out.callLabels = [...new Set(tel.map((a) => (a.textContent || '').replace(/\s+/g, ' ').trim().slice(0, 44)))].slice(0, 8);

  // fares and their stamps
  out.fares = [];
  try {
    const stamps = [];
    const scan = (o) => {
      if (!o || typeof o !== 'object') return;
      if (o.stamp) stamps.push({ stamp: o.stamp, from: o.from === undefined ? null : o.from, noPrice: !!o.noPrice });
    };
    if (typeof DEALS !== 'undefined') DEALS.forEach(scan);
    if (typeof ITINERARIES !== 'undefined') ITINERARIES.forEach(scan);
    if (typeof SAILINGS !== 'undefined') SAILINGS.forEach(scan);
    const today = new Date();
    out.fares = stamps.map((s) => ({
      ...s,
      ageDays: Math.floor((today - new Date(s.stamp + 'T00:00:00')) / 86400000),
    }));
    out.staleShown = out.fares.filter((f) => f.ageDays > maxAgeDays && !f.noPrice && f.from != null).length;
  } catch (e) { out.fareErr = String(e).slice(0, 80); }

  // visible "$" inside <main> (the indexed-page rule; /go/ pages are exempt)
  const main = document.querySelector('main') || document.body;
  out.dollarInMain = (main.innerText.match(/\$\s?\d/g) || []).length;

  // text drawn over a photo with no dark layer between
  out.textOnPhoto = [];
  document.querySelectorAll('.hero, .imgbox, .banner, .phero').forEach((box) => {
    const hasImg = box.querySelector('img') || /url\(/.test(getComputedStyle(box).backgroundImage);
    if (!hasImg) return;
    const shade = box.querySelector('.shade, .overlay, .scrim, .tint');
    const txt = [...box.querySelectorAll('h1,h2,h3,p,span')]
      .filter((e) => (e.textContent || '').trim().length > 12 && e.getBoundingClientRect().width > 0);
    if (txt.length && !shade) {
      out.textOnPhoto.push({ box: box.className.toString().slice(0, 40), sample: txt[0].textContent.trim().slice(0, 44) });
    }
  });

  // console errors are collected on the node side
  return out;
};

(async () => {
  const [outDir, ...pairs] = process.argv.slice(2);
  const browser = await puppeteer.launch({
    executablePath: CHROME, headless: 'new', protocolTimeout: 180000,
    args: ['--no-sandbox', '--disable-gpu', '--hide-scrollbars'],
  });
  const results = [];
  for (const pair of pairs) {
    const i = pair.indexOf('=');
    const label = pair.slice(0, i), url = pair.slice(i + 1);
    for (const vp of VIEWPORTS) {
      const page = await browser.newPage();
      const errors = [];
      page.on('pageerror', (e) => errors.push(String(e).slice(0, 120)));
      page.on('console', (m) => { if (m.type() === 'error') errors.push('console: ' + m.text().slice(0, 100)); });
      await page.setViewport({ width: vp.width, height: vp.height, isMobile: vp.mobile, hasTouch: vp.mobile,
        deviceScaleFactor: 1 });
      await page.goto(url, { waitUntil: 'networkidle2', timeout: 45000 });
      // Scroll the whole page first: loading="lazy" images below the fold are
      // not fetched otherwise, so the screenshot showed empty frames on cards
      // that are perfectly fine, which is a false defect in a design review.
      await page.evaluate(async () => {
        const step = window.innerHeight;
        const maxY = Math.min(document.body.scrollHeight, 40000);
        for (let y = 0; y < maxY; y += step) {
          window.scrollTo(0, y); await new Promise((r) => setTimeout(r, 60));
        }
        window.scrollTo(0, 0);
      });
      // Bounded wait: an image that never re-enters the viewport would otherwise
      // never settle and the whole run would hang on the protocol timeout.
      await page.evaluate(() => Promise.race([
        Promise.all([...document.images].filter((i) => !i.complete)
          .map((i) => new Promise((r) => { i.onload = i.onerror = r; }))),
        new Promise((r) => setTimeout(r, 4000)),
      ]));
      await new Promise((r) => setTimeout(r, 500));
      const data = await page.evaluate(audit, MAX_AGE_DAYS);
      // settle each image with a HEAD request against the same origin
      const base = new URL(url);
      for (const src of data.imgSrcs || []) {
        try {
          const abs = new URL(src, base).href;
          const res = await page.evaluate(async (u) => {
            try { const r = await fetch(u, { method: 'HEAD' }); return r.status; } catch (e) { return 0; }
          }, abs);
          if (res !== 200) data.imgBroken.push(`${src} -> HTTP ${res}`);
        } catch (e) { data.imgBroken.push(`${src} -> ${String(e).slice(0, 40)}`); }
      }
      const file = `${outDir}/${label}-${vp.tag}.png`;
      await page.screenshot({ path: file, fullPage: true });
      results.push({ label, vp: vp.tag, url, file, errors, ...data });
      await page.close();
    }
  }
  await browser.close();

  for (const r of results) {
    const bad = [];
    if (r.vp === 'phone' && r.scrollW > r.vw + 1) bad.push(`H-SCROLL ${r.scrollW}>${r.vw}`);
    if (r.imgBroken.length) bad.push(`BROKEN-IMG ${r.imgBroken.length}`);
    if (r.tokens.length) bad.push(`TOKENS ${r.tokens.join(',')}`);
    if (r.repeatedInStrip.length) bad.push(`REPEAT-PHOTO ${r.repeatedInStrip.length}`);
    if (!r.telAboveFold) bad.push('NO-CALL-ABOVE-FOLD');
    if (r.staleShown) bad.push(`STALE-FARES ${r.staleShown}`);
    if (r.textOnPhoto.length) bad.push(`TEXT-ON-PHOTO ${r.textOnPhoto.length}`);
    if (r.errors.length) bad.push(`JS-ERR ${r.errors.length}`);
    console.log(`\n${r.label} [${r.vp}] ${bad.length ? 'FAIL: ' + bad.join(' | ') : 'ok'}`);
    console.log(`   ${r.file}`);
    console.log(`   imgs=${r.imgTotal} broken=${r.imgBroken.length} tel=${r.telTotal} (${r.telAboveFold} above fold) ` +
      `fares=${r.fares.length} stale=${r.staleShown || 0} $inMain=${r.dollarInMain}`);
    if (r.callLabels.length) console.log(`   call labels: ${JSON.stringify(r.callLabels)}`);
    if (r.overflowers.length) r.overflowers.forEach((o) =>
      console.log(`   overflow: <${o.tag} class="${o.cls}"> right=${o.right} w=${o.w} "${o.text}"`));
    if (r.imgBroken.length) r.imgBroken.forEach((s) => console.log(`   broken img: ${s}`));
    if (r.repeatedInStrip.length) r.repeatedInStrip.forEach((d) =>
      console.log(`   repeated photo in .${d.grid}: ${d.dupes.join(', ')}`));
    if (r.textOnPhoto.length) r.textOnPhoto.forEach((t) =>
      console.log(`   text on photo (.${t.box}): "${t.sample}"`));
    if (r.errors.length) r.errors.slice(0, 4).forEach((e) => console.log(`   JS: ${e}`));
  }
})();
