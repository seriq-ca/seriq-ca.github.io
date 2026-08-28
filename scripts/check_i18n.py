#!/usr/bin/env python3
"""Translation-parity check for the hand-rolled FR/EN setup.

Nothing in Jekyll enforces that a page has a counterpart in the other
language — a missing translation builds happily and fails silently. This
turns that into a build error.

Rules:
  * language is derived from path: anything under en/ is English, else French
  * every page must declare a `ref:` key
  * every `ref` must exist in both languages

Run locally with:  python3 scripts/check_i18n.py
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LANGS = ("fr", "en")
SKIP_DIRS = {"_site", "_includes", "_layouts", "vendor", "node_modules",
             ".git", ".jekyll-cache", "scripts", ".github"}
PAGE_SUFFIXES = {".md", ".markdown", ".html"}

FRONT_MATTER = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def page_files():
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or path.suffix not in PAGE_SUFFIXES:
            continue
        rel = path.relative_to(ROOT)
        if set(rel.parts) & SKIP_DIRS:
            continue
        # Posts are the meeting archive: untranslated by design (PLAN.md §6.3).
        if rel.parts[0] == "_posts":
            continue
        yield rel, path


def front_matter(path):
    text = path.read_text(encoding="utf-8")
    match = FRONT_MATTER.match(text)
    if not match:
        return None
    fields = {}
    for line in match.group(1).splitlines():
        if ":" in line and not line.startswith((" ", "\t", "#")):
            key, _, value = line.partition(":")
            fields[key.strip()] = value.strip().strip("\"'")
    return fields


def lang_of(rel):
    return "en" if rel.parts[0] == "en" else "fr"


def main():
    seen = {lang: {} for lang in LANGS}
    errors = []

    for rel, path in page_files():
        fields = front_matter(path)
        if fields is None:
            continue  # no front matter: not a rendered page
        ref = fields.get("ref")
        if not ref:
            errors.append(f"{rel}: missing `ref:` in front matter")
            continue
        lang = lang_of(rel)
        if ref in seen[lang]:
            errors.append(
                f"{rel}: duplicate ref '{ref}' in {lang} "
                f"(already used by {seen[lang][ref]})"
            )
        seen[lang][ref] = rel

    for lang in LANGS:
        other = "en" if lang == "fr" else "fr"
        for ref, rel in sorted(seen[lang].items()):
            if ref not in seen[other]:
                errors.append(
                    f"{rel}: ref '{ref}' has no {other.upper()} counterpart"
                )

    total = len(seen["fr"]) + len(seen["en"])
    if errors:
        print(f"Translation parity: {len(errors)} problem(s) across {total} page(s)\n")
        for err in errors:
            print(f"  ✗ {err}")
        print("\nEvery page needs a `ref:` key, present in both fr and en.")
        return 1

    print(f"Translation parity OK — {len(seen['fr'])} ref(s), "
          f"{total} page(s), no gaps.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
