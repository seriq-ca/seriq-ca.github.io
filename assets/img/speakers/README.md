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

To self-host one, square it from the top and shrink it, never enlarging:

    magick <source> -auto-orient -gravity north \
      -extent "$(magick identify -format '%[fx:min(w,h)]x%[fx:min(w,h)]' <source>)" \
      +repage -resize 240x240\> -strip -quality 80 -interlace Plane <surname>.jpg

  * 240×240 for a speaker card, which renders at 120 CSS pixels; 112×112 for
    the event pages' panel portraits (`.portrait-sm`), which render at 56.
    Both cover 2× displays and keep each file to a few kilobytes.
  * `.jpg` for photographs, `.png` only for flat graphics
  * name the file after the speaker's surname, lowercased and stripped of
    accents and spaces: `lemire.jpg`
  * no leading underscore: Jekyll excludes `_*` from the build output

A speaker with no `photo:` renders a bare amber node instead, which is the
intended fallback rather than a broken state.

Current portraits, all self-hosted:

  * Daniel Lemire — `lemire.jpg`, from https://lemire.me/img/portrait2026.jpg
  * Lionel Briand — `briand.jpg`, from his conf.researchr.org profile image
  * Marsha Chechik — `chechik.jpg`, from
    https://discover.research.utoronto.ca/24922-marsha-chechik/thumbnail,
    kept at its native 180×180
  * Yves Daoust — `daoust.jpg`, cropped from
    https://www.fermedhiver.com/wp-content/uploads/2023/05/CEO_CTO_FermedHiver-min-scaled.jpg
    (he is on the left, per the caption on fermedhiver.com)
  * Frédéric Bouchard — `bouchard.jpg`, from his fas.umontreal.ca portrait.
    fas.umontreal.ca resolves to a private address on the UdeM network, which
    made Chrome ask for local network access when it was hotlinked.
  * Daria Camilla Boffito — `boffito.jpg`, from her polymtl.ca expertise page
  * Brigitte Pientka — `pientka.jpg`, from https://www.cs.mcgill.ca/media/professors/Pientka.jpg
  * Alan Carter — `carter.jpg`, a 270×270 square cropped around his face from
    his etsmtl.ca portrait (P20220119-Carter-Alan-002.jpg). The etsmtl.ca
    hotlink showed as a broken image on phones.
