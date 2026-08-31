Member portraits, referenced by the `photo:` field in `_data/members.yml`.

Interim state: `photo:` currently holds absolute URLs pointing at institutional
and personal pages, so the page shows portraits before members have supplied
their own. The template treats any value containing `://` as a remote URL and
anything else as a filename in this directory, so replacing a URL with a
filename is the whole migration.

The target is self-hosted only. The SEMTL site hotlinked personal pages and a Google Scholar
endpoint; those break, and they leak visitors' IP addresses to third parties.

  * square, 144×144 or larger — the page renders them at 72 CSS pixels
  * `.jpg` for photographs, `.png` only for flat graphics
  * name the file after the member: `baudry.jpg`
  * no leading underscore: Jekyll excludes `_*` from the build output

Ask each member for a photo they are happy to publish, along with the
re-confirmation of their listing.
