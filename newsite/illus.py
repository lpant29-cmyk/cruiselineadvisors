# -*- coding: utf-8 -*-
"""Self-hosted, zero-copyright illustrative artwork (inline SVG). Used on ship pages as a decorative
banner until/unless the user supplies licensed real photos. On-brand with the site's ocean palette.
It is clearly stylised/illustrative, never presented as a photo of the actual ship."""

_LABEL = {"en": "Illustrative", "es": "Ilustrativo"}


def ship_banner(lang):
    """A wide flat-design ocean scene with a stylised modern cruise ship, decorative only."""
    return f'''<div class="illus-band" role="img" aria-label="{_LABEL[lang]} ocean scene">
<svg viewBox="0 0 1200 260" preserveAspectRatio="xMidYMid slice" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="ib-sky" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#CFF1F8"/><stop offset="1" stop-color="#8FD9F0"/>
    </linearGradient>
    <linearGradient id="ib-sea" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#2FC4C0"/><stop offset="1" stop-color="#0C6E86"/>
    </linearGradient>
  </defs>
  <rect width="1200" height="260" fill="url(#ib-sky)"/>
  <circle cx="990" cy="82" r="46" fill="#FFE7A8"/>
  <circle cx="990" cy="82" r="60" fill="#FFE7A8" opacity="0.35"/>
  <!-- distant clouds -->
  <g fill="#ffffff" opacity="0.8">
    <ellipse cx="230" cy="70" rx="70" ry="20"/><ellipse cx="300" cy="70" rx="55" ry="16"/>
    <ellipse cx="700" cy="46" rx="60" ry="17"/><ellipse cx="760" cy="46" rx="42" ry="13"/>
  </g>
  <!-- ship -->
  <g transform="translate(430,74)">
    <!-- hull -->
    <path d="M20 96 L360 96 L332 150 L70 150 Z" fill="#0A2C42"/>
    <path d="M20 96 L360 96 L356 108 L24 108 Z" fill="#123C5A"/>
    <!-- superstructure decks -->
    <rect x="52" y="60" width="276" height="38" rx="6" fill="#ffffff"/>
    <rect x="70" y="36" width="240" height="26" rx="5" fill="#F4FAFB"/>
    <rect x="96" y="18" width="188" height="20" rx="4" fill="#ffffff"/>
    <!-- windows -->
    <g fill="#2FC4C0">
      <rect x="66" y="70" width="14" height="10" rx="2"/><rect x="88" y="70" width="14" height="10" rx="2"/>
      <rect x="110" y="70" width="14" height="10" rx="2"/><rect x="132" y="70" width="14" height="10" rx="2"/>
      <rect x="154" y="70" width="14" height="10" rx="2"/><rect x="176" y="70" width="14" height="10" rx="2"/>
      <rect x="198" y="70" width="14" height="10" rx="2"/><rect x="220" y="70" width="14" height="10" rx="2"/>
      <rect x="242" y="70" width="14" height="10" rx="2"/><rect x="264" y="70" width="14" height="10" rx="2"/>
      <rect x="286" y="70" width="14" height="10" rx="2"/>
    </g>
    <!-- funnel -->
    <rect x="150" y="-6" width="44" height="30" rx="6" fill="#F0891F"/>
    <rect x="150" y="-6" width="44" height="10" rx="5" fill="#FFB23E"/>
    <!-- mast -->
    <rect x="112" y="-2" width="4" height="22" fill="#0A2C42"/>
  </g>
  <!-- sea -->
  <rect y="176" width="1200" height="84" fill="url(#ib-sea)"/>
  <path d="M0 176 Q150 160 300 176 T600 176 T900 176 T1200 176 V200 H0 Z" fill="#2FC4C0" opacity="0.7"/>
  <path d="M0 196 Q150 182 300 196 T600 196 T900 196 T1200 196 V260 H0 Z" fill="#12919A" opacity="0.55"/>
  <!-- dolphin -->
  <path d="M250 210 q18 -34 44 -14 q-10 -4 -20 6 q16 -6 22 4 q-22 8 -46 4 z" fill="#0A2C42"/>
</svg>
<span class="illus-tag">{_LABEL[lang]}</span>
</div>'''
