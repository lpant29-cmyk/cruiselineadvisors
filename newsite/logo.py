# -*- coding: utf-8 -*-
"""The logo — one file. Clean nautical mark (navy badge + gold sun + ocean waves)
paired with the wordmark. Edit here to change the logo everywhere."""


def mark(px=38):
    """Return just the SVG badge mark at the given pixel size."""
    return (
        f'<svg class="cla-mark" width="{px}" height="{px}" viewBox="0 0 44 44" '
        'aria-hidden="true" focusable="false">'
        '<defs><linearGradient id="clm" x1="0" y1="0" x2="1" y2="1">'
        '<stop offset="0" stop-color="#123C5A"/><stop offset="1" stop-color="#0A2540"/>'
        '</linearGradient></defs>'
        '<rect width="44" height="44" rx="13" fill="url(#clm)"/>'
        '<circle cx="30" cy="15" r="5" fill="#E0A84E"/>'
        '<path d="M6 25q4-3.6 8 0t8 0 8 0 8 0" fill="none" stroke="#1FB6B6" stroke-width="2.4" stroke-linecap="round"/>'
        '<path d="M6 31q4-3.6 8 0t8 0 8 0 8 0" fill="none" stroke="#fff" stroke-width="2.4" stroke-linecap="round" opacity=".92"/>'
        '<path d="M6 37q4-3.6 8 0t8 0 8 0 8 0" fill="none" stroke="#E0A84E" stroke-width="2.4" stroke-linecap="round" opacity=".65"/>'
        '</svg>'
    )


def lockup(home_href, px=38):
    """Mark + wordmark, linked to the language home page."""
    return (
        f'<a class="brand" href="{home_href}" aria-label="CruiseLine Advisors — home">'
        f'{mark(px)}'
        '<span class="brand-txt">CruiseLine<span>Advisors</span></span>'
        '</a>'
    )
