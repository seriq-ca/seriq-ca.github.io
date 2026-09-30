#!/usr/bin/env python3
"""Export the header logo as standalone files for the press kit.

The header draws the logo inline from _includes/logo.html and colours it with
CSS tokens, so a copy taken out of the page has no colours. This bakes in the
light and dark theme values of --wire, --node and --node-line, one file per
theme: "light" is the logo for light backgrounds, "dark" for dark ones.

The viewBox is widened by a margin: the node casing is stroked on the node's
edge, so half of it falls outside the header's tight viewBox. The PNGs are
rasterised with Inkscape, transparent and on the theme's --paper ground.

It also rewrites assets/img/logo.png, the site logo named in the schema.org
metadata: the light logo on its ground at 1200x806, the margin chosen so the
frame keeps that aspect.

    python3 scripts/make_logo.py        # rewrites assets/img/press/* and logo.png
"""
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "_includes" / "logo.html"
OUT = ROOT / "assets" / "img" / "press"

# --wire, --node, --node-line, --paper in each theme (_sass/_tokens.scss).
THEMES = {
    "light": {"wire": "#0f3a86", "node": "#f2a413", "line": "#12161c", "ground": "#f2f4f7"},
    "dark": {"wire": "#7ea6ff", "node": "#f5b73f", "line": "#e6ebf2", "ground": "#0b1016"},
}
MARGIN = 36        # clears the node casing, which overhangs the viewBox by 18
GROUND_PAD = 220   # extra space around the logo on the PNG with a ground
PNG_WIDTH = 2400
SITE_LOGO = ROOT / "assets" / "img" / "logo.png"
SITE_LOGO_WIDTH = 1200
SITE_LOGO_PAD = 212.4  # (3635 + 2p) / (2302 + 2p) = 1200 / 806


def standalone(markup, colours, pad):
    x, y, w, h = map(float, re.search(r'viewBox="([^"]+)"', markup)[1].split())
    box = f"{x - pad:g} {y - pad:g} {w + 2 * pad:g} {h + 2 * pad:g}"
    style = (
        "<style>"
        f".logo__word,.logo__run{{fill:{colours['wire']}}}"
        f".logo__node{{fill:{colours['node']}}}"
        f".logo__node rect{{stroke:{colours['line']};stroke-width:36}}"
        "</style>")
    markup = re.sub(r'viewBox="[^"]+"', f'viewBox="{box}"', markup, count=1)
    markup = re.sub(r'\s*focusable="false"', "", markup)
    return markup.replace("<defs>", "<defs>\n    " + style, 1)


def with_ground(markup, colour):
    x, y, w, h = re.search(r'viewBox="([^"]+)"', markup)[1].split()
    rect = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{colour}"/>'
    return markup.replace("</defs>", "</defs>\n  " + rect, 1)


def rasterise(svg, png, width=PNG_WIDTH):
    subprocess.run(
        ["inkscape", str(svg), "--export-type=png", f"--export-filename={png}",
         f"--export-width={width}"],
        check=True, capture_output=True)


def main():
    markup = SOURCE.read_text().strip()
    OUT.mkdir(parents=True, exist_ok=True)
    for theme, colours in THEMES.items():
        name = f"seriq-logo-{theme}"
        svg = OUT / f"{name}.svg"
        svg.write_text(standalone(markup, colours, MARGIN) + "\n")
        rasterise(svg, OUT / f"{name}.png")

        grounded = OUT / f"{name}-ground.svg"
        grounded.write_text(with_ground(standalone(markup, colours, MARGIN + GROUND_PAD),
                                        colours["ground"]))
        rasterise(grounded, OUT / f"{name}-ground.png")
        grounded.unlink()

    light = THEMES["light"]
    site = OUT / "site-logo.svg"
    site.write_text(with_ground(standalone(markup, light, SITE_LOGO_PAD), light["ground"]))
    rasterise(site, SITE_LOGO, SITE_LOGO_WIDTH)
    site.unlink()


if __name__ == "__main__":
    main()
