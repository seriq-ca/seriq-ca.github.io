#!/usr/bin/env python3
"""Import the SEMTL-era posts into the `semtl` collection.

The old site's 32 posts are ported into `_semtl/` and served from this site.
They stay English-only -- translating them was never the point of the archive --
so `check_i18n.py` exempts the collection, the same exemption `_posts` had on
the old site.

    python3 scripts/import_semtl_posts.py [--repo ~/Projects/semtl.github.io]

Re-running overwrites `_semtl/`. Edit this script, not the generated documents.

What it changes on the way through:

  * URLs are keyed on `event_date`, not the old front-matter `date:`. Jekyll
    built the old permalinks from `date:`, which on several posts is the day
    the post was written rather than the day the meeting happened -- the June
    2026 meeting lived at /2026/04/15/. The old URLs stay valid on
    semtl.github.io; nothing here has to reproduce that quirk.
  * Google Maps iframes are dropped, with the heading above them if that
    leaves the section empty. 26 third-party embeds is not a tracking surface
    worth inheriting for a map of a room.
  * Slides and images are left on semtl.github.io and rewritten to absolute
    URLs -- this site does not host the old assets.
  * The hotlinked Polytechnique campus map is switched to https and linked to
    the official campus-map page.
"""

import argparse
import pathlib
import re
import sys

OLD_SITE = "https://semtl.github.io"

# Polytechnique serves this file on its own campus-map page; the old posts just
# referenced it over plain http, which is mixed content on an https page.
POLY_MAP_OLD = "http://www.polymtl.ca/sites/amigow2020.polymtl.ca/files/plancampus700px_en.png"
POLY_MAP_NEW = "https://www.polymtl.ca/sites/amigow2020.polymtl.ca/files/plancampus700px_en.png"
POLY_MAP_PAGE = "https://www.polymtl.ca/renseignements-generaux/en/contact-information-access-maps/campus-map"

AUTHOR_DISPLAY = {"Bentley James Oakes": "Bentley Oakes"}
VENUE_DISPLAY = {"ETS": "ÉTS"}

IFRAME = re.compile(r"<iframe\b.*?</iframe>", re.S | re.I)
# The maps were sometimes wrapped in a bare positioning div.
DIV_WRAPPED_IFRAME = re.compile(r"<div\b[^>]*>\s*<iframe\b.*?</iframe>\s*</div>", re.S | re.I)
FRONT_MATTER = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.S)


def parse_front_matter(text):
    m = FRONT_MATTER.match(text)
    if not m:
        return {}, text
    fields = {}
    for line in m.group(1).splitlines():
        km = re.match(r"^(\w+):\s*(.*?)\s*$", line)
        if km:
            fields[km.group(1)] = km.group(2)
    return fields, text[m.end():]


def venue(raw):
    if not raw:
        return None
    v = raw.strip().strip("[]").split(",")[0].strip().strip("\"'")
    return VENUE_DISPLAY.get(v, v) or None


def author(raw):
    if not raw:
        return None
    name = raw.strip()
    return AUTHOR_DISPLAY.get(name, name) or None


def drop_empty_headings(body):
    """A heading whose whole section was an iframe is left dangling. Drop any
    heading immediately followed by another heading or the end of the body."""
    lines = body.split("\n")
    keep, i = [], 0
    while i < len(lines):
        line = lines[i]
        if re.match(r"^#{1,6}\s", line):
            j = i + 1
            while j < len(lines) and not lines[j].strip():
                j += 1
            if j >= len(lines) or re.match(r"^#{1,6}\s", lines[j]):
                i = j
                continue
        keep.append(line)
        i += 1
    return "\n".join(keep)


def convert_body(body):
    body = DIV_WRAPPED_IFRAME.sub("", body)
    body = IFRAME.sub("", body)

    body = body.replace(
        '<img src="%s"' % POLY_MAP_OLD,
        '<a href="%s"><img src="%s"' % (POLY_MAP_PAGE, POLY_MAP_NEW),
    )
    body = re.sub(
        r'(<a href="%s"><img src="%s"[^>]*?)/?>' % (re.escape(POLY_MAP_PAGE), re.escape(POLY_MAP_NEW)),
        r"\1/></a>",
        body,
    )
    body = body.replace('alt="polymtl_access"', 'alt="Polytechnique Montréal campus access map"')

    # Assets stay on the old site.
    body = re.sub(r'(src|href)="(/(?:slides|img)/)', r'\1="%s\2' % OLD_SITE, body)
    body = re.sub(r"\]\((/(?:slides|img)/)", r"](%s\1" % OLD_SITE, body)

    body = drop_empty_headings(body)
    body = re.sub(r"\n{3,}", "\n\n", body)
    return body.strip() + "\n"


def yaml_str(s):
    return '"%s"' % s.replace("\\", "\\\\").replace('"', '\\"')


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", default="~/Projects/semtl.github.io")
    args = ap.parse_args()

    repo = pathlib.Path(args.repo).expanduser()
    posts = sorted((repo / "_posts").glob("*.md"))
    if not posts:
        sys.exit("no posts found under %s/_posts" % repo)

    out_dir = pathlib.Path(__file__).resolve().parent.parent / "_semtl"
    for stale in out_dir.glob("*.md"):
        stale.unlink()
    out_dir.mkdir(exist_ok=True)

    seen, written = {}, 0
    for post in posts:
        fm, body = parse_front_matter(post.read_text(encoding="utf-8"))
        event_date = fm.get("event_date")
        if not event_date:
            sys.exit("%s: no event_date" % post.name)
        slug = re.sub(r"^\d{4}-\d{2}-\d{2}-", "", post.stem).lower()
        name = "%s-%s" % (event_date, slug)
        if name in seen:
            sys.exit("%s and %s both map to %s" % (post.name, seen[name], name))
        seen[name] = post.name

        head = [
            "---",
            "ref: events",
            "title: %s" % yaml_str(fm.get("title", "").strip()),
            "permalink: /semtl/%s/" % name,
            "event_date: %s" % event_date,
        ]
        v = venue(fm.get("tags"))
        if v:
            head.append("event_venue: %s" % yaml_str(v))
        a = author(fm.get("author"))
        if a:
            head.append("author: %s" % yaml_str(a))
        head.append("source_url: %s" % (OLD_SITE + "/%s/%s/%s/" % (
            fm.get("category", "meeting"),
            (fm.get("date") or post.stem[:10]).replace("-", "/"),
            re.sub(r"^\d{4}-\d{2}-\d{2}-", "", post.stem),
        )))
        head.append("---")

        (out_dir / (name + ".md")).write_text(
            "\n".join(head) + "\n\n" + convert_body(body), encoding="utf-8"
        )
        written += 1

    print("wrote %d documents to %s" % (written, out_dir))


if __name__ == "__main__":
    main()
