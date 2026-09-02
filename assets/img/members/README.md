Member portraits, referenced by the `photo:` field in `_data/members.yml`.

Every portrait is self-hosted. The SEMTL site hotlinked personal pages and a
Google Scholar endpoint; those break, and they leak visitors' IP addresses to
third parties. The values here are plain filenames and the template resolves
them against this directory — there is no remote branch any more, so a URL in
`photo:` will not work.

  * square, 144×144 — the page renders them at 48 CSS pixels, so this covers
    displays up to 3×
  * `.jpg` for photographs, `.png` only for flat graphics
  * name the file after the member's surname, lowercased and stripped of
    accents and spaces: `baudry.jpg`, `elboussaidi.jpg`
  * no leading underscore: Jekyll excludes `_*` from the build output

A member with no `photo:` renders a bare amber node instead, which is the
intended fallback rather than a broken state.

The current set was taken from members' own and institutional pages, then
normalised with:

    magick <source> -auto-orient -resize 144x144^ -gravity north \
      -extent 144x144 -strip -quality 82 -interlace Plane <surname>.jpg

`-gravity north` rather than `center` because portrait sources are usually
taller than wide with the face in the upper half; centring cuts foreheads.
Flat graphics keep PNG and drop the JPEG-only flags.

Ask each member for a photo they are happy to publish, along with the
re-confirmation of their listing.
