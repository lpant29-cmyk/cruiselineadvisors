# -*- coding: utf-8 -*-
"""CSS for the credentials band and the credential badges, in ONE place.

Lifted out of theme.py on 2026-10-21 because the /go/ ad pages now carry
the same band (every campaign destination has to show the licence and the
ASTA membership) and those pages do not load theme.py. Two copies of these
rules would have drifted the first time one surface was restyled, so both
surfaces read this string: theme.py splices it into the main stylesheet,
lp-system/scripts/generate.py injects it into each /go/ page head.

The band's own look is carried by .credband descendant selectors, so it
renders the same wherever it is placed. Only the outer section padding
comes from the host surface (.section on the main site, .blk on /go/),
which is why credentials_band() takes the class name as an argument.
"""

CRED_CSS = """/* operator credential badges (ASTA + FL Seller of Travel). The credentials
   belong to the operating entity, so the row leads with "Operated by". */
.trustbadges{margin-top:1rem;padding-top:.9rem;border-top:1px solid rgba(255,255,255,.1)}
.tb-op{margin-bottom:.6rem;color:#87B0BA;font-size:.75rem}
.tb-op b{color:#CDE7EB}
.tb-row{display:flex;flex-wrap:wrap;align-items:center;gap:.7rem 1.1rem}
.ftr .tb{display:inline-flex;align-items:center;gap:.55rem;padding:.5rem .8rem;border-radius:10px;
  background:rgba(255,255,255,.95);text-decoration:none;line-height:1.2;transition:transform .15s ease,box-shadow .15s ease}
.ftr .tb:hover{transform:translateY(-1px);box-shadow:0 4px 14px rgba(0,0,0,.25)}
.ftr .tb:focus-visible{outline:2px solid #E0A84E;outline-offset:2px}
.tb-asta img{display:block;width:auto;height:30px;max-width:100%}
.tb-cap{position:absolute;width:1px;height:1px;padding:0;margin:-1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap;border:0}
.ftr .tb-fsot{background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.22)}
.ftr .tb-fsot:hover{background:rgba(255,255,255,.14)}
.tb-fsot-txt{color:#CDE7EB;font-size:.76rem;font-weight:700;letter-spacing:.01em}
@media(min-width:900px){.tb-asta img{height:34px}}
.ftr .tb-bah{background:rgba(255,255,255,.95);padding:.4rem .7rem}
.tb-bah img{display:block;width:auto;height:34px;max-width:100%}
.ftr .tb-romance{background:rgba(255,255,255,.95);padding:.25rem .45rem}
.tb-romance img{display:block;width:auto;height:40px;max-width:100%}
/* Sitewide credentials band (before footer) --------------------------------- */
.credband{background:#0c2735;text-align:center;border-top:1px solid rgba(127,212,208,.16)}
.credband .credband-head .eyebrow{color:#7FD4D0;letter-spacing:.09em;text-transform:uppercase;font-size:.78rem;font-weight:800}
.credband .credband-head h2{color:#fff;margin:.35rem 0 0;font-size:clamp(1.3rem,3.5vw,1.9rem)}
.credband .credband-head p{color:#9fc0cb;max-width:60ch;margin:.6rem auto 0;line-height:1.6}
.credband .trustbadges{border-top:0;margin-top:1.5rem;padding-top:0}
.credband .tb-op{color:#9fc0cb;margin-bottom:1.1rem;font-size:.85rem}
.credband .tb-op b{color:#fff}
.credband .tb-row{justify-content:center;align-items:center;gap:1.1rem 1.9rem}
.credband .tb{display:inline-flex;align-items:center;transition:transform .15s ease}
.credband a.tb:hover{transform:translateY(-2px)}
.credband .tb-asta{background:#fff;border-radius:12px;padding:.6rem .9rem}
.credband .tb-asta img{display:block;width:auto;height:54px;max-width:100%}
.credband .tb-fsot{background:#12384a;border:1px solid rgba(127,212,208,.4);border-radius:12px;padding:.85rem 1.1rem}
.credband .tb-fsot-txt{color:#CDE7EB;font-weight:700;font-size:.95rem;letter-spacing:.01em}
.credband .tb-bah{background:#fff;border-radius:12px;padding:.55rem .85rem}
.credband .tb-bah img{display:block;width:auto;height:60px;max-width:100%}
.credband .tb-romance{background:#fff;border-radius:12px;padding:.4rem .6rem}
.credband .tb-romance img{display:block;width:auto;height:72px;max-width:100%}
.credband .tb-note{color:#87a7b2;max-width:70ch;margin:1.3rem auto 0}
@media(min-width:900px){.credband .tb-asta img{height:62px}.credband .tb-bah img{height:66px}.credband .tb-romance img{height:82px}}
.tb-note{margin-top:.65rem;color:#87B0BA;font-size:.74rem;line-height:1.55;max-width:60ch}
.tb-group + .tb-group{margin-top:1.1rem;padding-top:1rem;border-top:1px solid rgba(255,255,255,.1)}
.tb-disclaim{color:#6E96A2;font-size:.7rem;max-width:72ch}
/* TRUE accreditation (CCRA), held by the operating entity. Treated as an IMAGE
   badge, so it gets the white chip ASTA and the Bahamas diploma get, not the
   dark text pill the Seller of Travel reference gets. The official mark is dark
   navy and near-black on transparent: on the band's own #0c2735 it would be
   invisible, so the chip supplies the white ground the artwork expects. The code
   sits beside it in the same dark ink, because it is the thing a visitor copies
   into the CCRA checker. */
.tb-true img{display:block;width:auto;height:24px;max-width:100%}
.tb-true-txt{color:#1b3340;font-size:.76rem;font-weight:800;letter-spacing:.02em;white-space:nowrap}
.ftr .tb-true{background:rgba(255,255,255,.95);padding:.45rem .75rem;gap:.5rem}
.credband .tb-true{background:#fff;border-radius:12px;padding:.6rem .9rem;gap:.7rem}
.credband .tb-true img{height:42px}
.credband .tb-true-txt{font-size:.88rem}
@media(min-width:900px){.credband .tb-true img{height:48px}}
@media(max-width:380px){.credband .tb-true{gap:.45rem;padding:.5rem .7rem}
  .credband .tb-true img{height:34px}.credband .tb-true-txt{font-size:.78rem}}
"""
