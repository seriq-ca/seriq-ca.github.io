#!/usr/bin/env python3
"""Draw the header braid: four strands, one per partner institution.

Each strand is stroked twice — first in the ground colour as a casing, then in
its own colour — so the crossings read as over and under. That ties a tile to
the ground it sits on, which is why there is one file per theme.

    python3 scripts/make_braid.py        # rewrites assets/img/braid*.svg
"""
import math
from pathlib import Path

PERIOD, AMPLITUDE, MIDLINE, HEIGHT = 64, 3.6, 7, 14
STROKE, CASING = 1.6, 5.0

# Université de Montréal, Polytechnique Montréal, McGill, ÉTS. Placeholders
# drawn from the site palette, not the institutions' own brand colours.
STRANDS_LIGHT = ["#0f3a86", "#bf7a00", "#0f7a6b", "#a33a2f"]
STRANDS_DARK = ["#7ea6ff", "#f5b73f", "#56c9b4", "#ef8a7c"]


def strand(phase):
    points, x = [], 0.0
    while x < PERIOD:
        points.append((x, MIDLINE + AMPLITUDE * math.cos(2 * math.pi * x / PERIOD + phase)))
        x += 2
    points.append((PERIOD, MIDLINE + AMPLITUDE * math.cos(2 * math.pi + phase)))
    return "".join(("M" if i == 0 else "L") + f"{x:.2f} {y:.2f}"
                   for i, (x, y) in enumerate(points))


def tile(strands, ground):
    body = ""
    for colour, phase in zip(strands, [0, math.pi / 2, math.pi, 3 * math.pi / 2]):
        d = strand(phase)
        body += (f'\n  <path d="{d}" stroke="{ground}" stroke-width="{CASING}"/>'
                 f'\n  <path d="{d}" stroke="{colour}" stroke-width="{STROKE}"/>')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{PERIOD}" height="{HEIGHT}" '
            f'viewBox="0 0 {PERIOD} {HEIGHT}" fill="none" stroke-linecap="round">'
            f'{body}\n</svg>\n')


if __name__ == "__main__":
    out = Path(__file__).resolve().parent.parent / "assets" / "img"
    (out / "braid.svg").write_text(tile(STRANDS_LIGHT, "#f2f4f7"))
    (out / "braid-dark.svg").write_text(tile(STRANDS_DARK, "#0b1016"))
    print("wrote assets/img/braid.svg and assets/img/braid-dark.svg")
