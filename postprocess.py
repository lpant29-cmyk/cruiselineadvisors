#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Injects site-wide navigation furniture into every generated page:
   - breadcrumb trail showing where the user is
   - a Back control
   - a back-to-top button
Idempotent: safe to run after every build."""
import os, re, glob, json, html

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.join(ROOT, "site")

LABELS = {
    "index": "Home",
    "cruise-lines": "Cruise lines",
    "directory": "All lines directory",
    "destinations": "Destinations",
    "guides": "Guides",
    "compare": "Compare",
    "updates": "Policy updates",
    "advisors": "Advisor network",
    "lines-deep": "Cruise lines",
    "legal": "Legal",
}

NAV_CSS = """
/* ═══ SITE NAVIGATION FURNITURE ═══ */
.crumbbar{position:sticky;top:54px;z-index:55;background:var(--mist,#E4EDEF);
  border-bottom:1px solid var(--line,#D5E0E3)}
.crumbin{max-width:1180px;margin:0 auto;padding:8px 18px;display:flex;align-items:center;gap:10px;
  font-size:.78rem;overflow-x:auto;scrollbar-width:none;white-space:nowrap}
.crumbin::-webkit-scrollbar{display:none}
.crumbback{flex:none;display:inline-flex;align-items:center;gap:.35em;background:#fff;
  border:1px solid var(--line,#D5E0E3);border-radius:99px;padding:.34em .8em;
  font-size:.76rem;font-weight:800;color:var(--ink,#08243B);text-decoration:none;cursor:pointer}
.crumbback:hover{border-color:var(--brass,#D9B25A);background:#fff}
.crumbtrail{display:flex;align-items:center;gap:6px;min-width:0;color:var(--muted,#556B78)}
.crumbtrail a{color:var(--lagoon,#1B7A8C);text-decoration:none;font-weight:600}
.crumbtrail a:hover{text-decoration:underline}
.crumbtrail .sep{opacity:.5}
.crumbtrail .cur{color:var(--ink,#08243B);font-weight:800;overflow:hidden;text-overflow:ellipsis}

.totop{position:fixed;right:16px;bottom:84px;z-index:75;width:46px;height:46px;border-radius:50%;
  background:var(--ink,#08243B);color:#fff;border:1px solid rgba(255,255,255,.22);font-size:1.15rem;
  cursor:pointer;opacity:0;pointer-events:none;transition:.25s;box-shadow:0 8px 20px rgba(4,18,28,.32)}
.totop.on{opacity:1;pointer-events:auto}
.totop:hover{background:var(--ink2,#0E3A5C);transform:translateY(-2px)}
@media(min-width:1000px){.totop{bottom:24px;right:24px;width:50px;height:50px}}
@media(max-width:999px){.crumbbar{top:54px}}
"""

NAV_JS = """
/* back-to-top */
(function(){var t=document.getElementById('totop');if(!t)return;
t.addEventListener('click',function(){window.scrollTo({top:0,behavior:'smooth'});});
window.addEventListener('scroll',function(){
  t.className=(window.scrollY>500)?'totop on':'totop';},{passive:true});})();
/* back control — uses history when available, else the parent section */
(function(){var b=document.getElementById('crumbback');if(!b)return;
b.addEventListener('click',function(e){
  if(window.history.length>1){e.preventDefault();window.history.back();}
});})();
"""


def crumbs_for(path):
    """Returns (trail_html, parent_href) for a page path relative to site/."""
    parts = path[:-5].split("/")
    depth = len(parts) - 1
    up = "../" * depth
    trail = ['<a href="%sindex.html">Home</a>' % up]
    parent = "%sindex.html" % up

    if depth == 0:
        if parts[0] == "index":
            return '<span class="cur">Home</span>', None
        label = LABELS.get(parts[0], parts[0].replace("-", " ").title())
        trail.append('<span class="sep">›</span><span class="cur">%s</span>' % html.escape(label))
        return "".join(trail), parent

    section = parts[0]
    sec_label = LABELS.get(section, section.replace("-", " ").title())
    # map folder to its hub page where one exists
    hub = {"lines-deep": "cruise-lines.html", "destinations": "destinations.html",
           "guides": "guides.html", "legal": None}.get(section)
    if hub:
        trail.append('<span class="sep">›</span><a href="%s%s">%s</a>' % (up, hub, html.escape(sec_label)))
        parent = "%s%s" % (up, hub)
    else:
        trail.append('<span class="sep">›</span><span>%s</span>' % html.escape(sec_label))

    leaf = parts[-1].replace("-", " ")
    leaf = leaf[:1].upper() + leaf[1:]
    trail.append('<span class="sep">›</span><span class="cur">%s</span>' % html.escape(leaf))
    return "".join(trail), parent


def process(path):
    full = os.path.join(SITE, path)
    d = open(full, encoding="utf-8").read()
    changed = False

    # 1) CSS
    if ".crumbbar{" not in d:
        if "</style>" in d:
            d = d.replace("</style>", NAV_CSS + "\n</style>", 1)
        else:
            d = d.replace("</head>", "<style>%s</style>\n</head>" % NAV_CSS, 1)
        changed = True

    # 2) breadcrumb bar right after </header> (or after <body> if no header)
    if 'class="crumbbar"' not in d:
        trail, parent = crumbs_for(path)
        back = ('<a class="crumbback" id="crumbback" href="%s">← Back</a>' % parent) if parent else ""
        bar = ('<div class="crumbbar"><div class="crumbin">%s'
               '<nav class="crumbtrail" aria-label="Breadcrumb">%s</nav></div></div>' % (back, trail))
        if "</header>" in d:
            d = d.replace("</header>", "</header>\n" + bar, 1)
        else:
            d = re.sub(r"(<body[^>]*>)", r"\1\n" + bar, d, count=1)
        changed = True

    # 3) back-to-top button
    if 'id="totop"' not in d:
        d = d.replace("</body>", '<button class="totop" id="totop" aria-label="Back to top">↑</button>\n</body>', 1)
        changed = True

    # 4) JS (guarded so it never throws if elements are absent)
    if "back-to-top" not in d:
        if "</body>" in d:
            d = d.replace("</body>", "<script>%s</script>\n</body>" % NAV_JS, 1)
        changed = True

    if changed:
        open(full, "w", encoding="utf-8").write(d)
    return changed


def main():
    files = sorted(f for f in glob.glob("**/*.html", recursive=True, root_dir=SITE))
    n = 0
    for f in files:
        if process(f):
            n += 1
    print("post-processed %d of %d pages" % (n, len(files)))
    # verification
    missing = []
    for f in files:
        d = open(os.path.join(SITE, f), encoding="utf-8").read()
        if 'id="totop"' not in d: missing.append((f, "totop"))
        if 'class="crumbbar"' not in d: missing.append((f, "crumbs"))
    print("missing furniture:", missing if missing else "none")


if __name__ == "__main__":
    main()
