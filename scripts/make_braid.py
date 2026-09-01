#!/usr/bin/env python3
"""Draw the header braid: two strands, wire blue and node amber.

Each strand is stroked twice — first in the ground colour as a casing, then in
its own colour — so the crossings read as over and under. That ties a tile to
the ground it sits on, which is why there is one file per theme.

Neither strand is always on top. The tile is cut at the two extremes, giving
two cells, each holding one crossing; the strand that goes over alternates
between them, so the pair actually interlaces rather than one lying on the
other. Within a cell the under strand is drawn whole and the over strand's
casing hides it at the crossing, which is what makes the strand read as
continuous where it disappears.

    python3 scripts/make_braid.py        # rewrites assets/img/braid*.svg
"""
import math
from pathlib import Path

PERIOD, AMPLITUDE, MIDLINE, HEIGHT = 26, 4.0, 7, 14
STROKE, CASING = 1.6, 5.0
STEP = 1.0  # sampling interval along x; the cosine is drawn as a polyline

# Wire blue and node amber, the site's two ornament colours (--wire, --node).
STRANDS_LIGHT = ["#0f3a86", "#bf7a00"]
STRANDS_DARK = ["#7ea6ff", "#f5b73f"]


def strand(phase, x0, x1):
    """One strand's polyline over [x0, x1], endpoints landing exactly."""
    points, x = [], x0
    while x < x1:
        points.append(x)
        x += STEP
    points.append(x1)
    return "".join(
        ("M" if i == 0 else "L")
        + f"{x:.2f} {MIDLINE + AMPLITUDE * math.cos(2 * math.pi * x / PERIOD + phase):.2f}"
        for i, x in enumerate(points))


def tile(strands, ground):
    blue, amber = strands
    mid = PERIOD / 2
    # (colour, phase, span) — every under piece first, then every over piece,
    # so an over piece's casing cuts the strand it crosses and nothing else.
    # Cut at the extremes, not at the crossings: each piece then holds one
    # whole crossing, and every cut falls where the two strands are furthest
    # apart, so a cut never lands on a crossing.
    pieces = [
        (blue,  0.0,      (mid, PERIOD)),   # under: amber goes over at 3P/4
        (amber, math.pi,  (0, mid)),        # under: blue goes over at P/4
        (blue,  0.0,      (0, mid)),        # over
        (amber, math.pi,  (mid, PERIOD)),   # over
    ]
    body = ""
    for colour, phase, (x0, x1) in pieces:
        d = strand(phase, x0, x1)
        # The casing is butt-ended so it stops dead at the cell boundary; the
        # colour is round-ended so a strand's two pieces overlap there instead
        # of meeting on a shared antialiased edge, which shows as a hairline.
        body += (f'\n  <path d="{d}" stroke="{ground}" stroke-width="{CASING}"/>'
                 f'\n  <path d="{d}" stroke="{colour}" stroke-width="{STROKE}"'
                 f' stroke-linecap="round"/>')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{PERIOD}" height="{HEIGHT}" '
            f'viewBox="0 0 {PERIOD} {HEIGHT}" fill="none" stroke-linecap="butt">'
            f'{body}\n</svg>\n')


if __name__ == "__main__":
    out = Path(__file__).resolve().parent.parent / "assets" / "img"
    (out / "braid.svg").write_text(tile(STRANDS_LIGHT, "#f2f4f7"))
    (out / "braid-dark.svg").write_text(tile(STRANDS_DARK, "#0b1016"))
    print("wrote assets/img/braid.svg and assets/img/braid-dark.svg")
