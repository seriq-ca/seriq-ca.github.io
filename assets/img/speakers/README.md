Invited-speaker portraits, referenced by the `photo:` field in the per-event
files under `_data/speakers/`.

Unlike `assets/img/members/`, `photo:` here accepts two forms and
`_includes/speakers.html` tells them apart by looking for `://`:

  * a plain filename, resolved against this directory and self-hosted
  * an absolute URL, which hotlinks the speaker's own copy

Self-hosting is what the rest of the site does, and why is set out in
`assets/img/members/README.md`: hotlinked portraits break when the far side
moves them, and they tell that host the IP address of everyone who loads the
page. The template sends `referrerpolicy="no-referrer"`, which keeps the
referring URL out of the request; nothing keeps the IP out of it.

The remote form exists because speakers are guests rather than members — there
is not always someone to ask for a file, and a link to a portrait they already
publish is often all that is offered.

To self-host one, normalise it with the same command the members directory
documents, at the larger size a speaker card renders:

    magick <source> -auto-orient -resize 360x360^ -gravity north \
      -extent 360x360 -strip -quality 82 -interlace Plane <surname>.jpg

  * square, 360×360 — a speaker card renders the portrait at 120 CSS pixels
    rather than the members register's 48, so this covers displays up to 3×
  * `.jpg` for photographs, `.png` only for flat graphics
  * name the file after the speaker's surname, lowercased and stripped of
    accents and spaces: `lemire.jpg`
  * no leading underscore: Jekyll excludes `_*` from the build output

A speaker with no `photo:` renders a bare amber node instead, which is the
intended fallback rather than a broken state.

Current portraits:

  * Daniel Lemire — hotlinked from https://lemire.me/img/portrait2018.jpg
