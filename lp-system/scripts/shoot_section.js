const puppeteer = require('/tmp/shotkit/node_modules/puppeteer-core');
(async () => {
  const b = await puppeteer.launch({ executablePath:'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    headless:'new', protocolTimeout:120000, args:['--no-sandbox','--disable-gpu','--hide-scrollbars'] });
  for (const spec of process.argv.slice(2)) {
    const [name, w, url] = spec.split('|');
    const p = await b.newPage();
    await p.setViewport({ width:+w, height:1100, isMobile:+w<500, hasTouch:+w<500 });
    await p.goto(url,{waitUntil:'networkidle2'}); await new Promise(r=>setTimeout(r,500));
    await p.evaluate(async()=>{const s=window.innerHeight;
      for(let y=0;y<Math.min(document.body.scrollHeight,20000);y+=s){window.scrollTo(0,y);await new Promise(r=>setTimeout(r,60));}});
    await p.evaluate(()=>Promise.race([Promise.all([...document.images].filter(i=>!i.complete)
      .map(i=>new Promise(r=>{i.onload=i.onerror=r;}))),new Promise(r=>setTimeout(r,3500))]));
    const y = await p.evaluate(()=>{
      const r=document.getElementById('results'); if(!r) return 0;
      const top=r.getBoundingClientRect().top+window.scrollY;
      window.scrollTo(0, Math.max(0, top-8)); return Math.round(window.scrollY);
    });
    await new Promise(r=>setTimeout(r,500));
    await p.screenshot({ path:`/tmp/shots/${name}.png` });
    console.log(`${name}.png  scrolled to y=${y}`);
    await p.close();
  }
  await b.close();
})();
