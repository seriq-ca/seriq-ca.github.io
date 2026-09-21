source "https://rubygems.org"

gem "jekyll", "~> 4.3"

group :jekyll_plugins do
  gem "jekyll-feed", "~> 0.17"
  gem "jekyll-sitemap", "~> 1.4"
  # Real <lastmod> values in the sitemap: the file's last git commit time,
  # instead of jekyll-sitemap falling back to the date in an event's filename.
  # Requires full git history at build time (fetch-depth: 0 in the workflow).
  gem "jekyll-last-modified-at", "~> 1.3"
end
