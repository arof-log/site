#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p _site
cp index.html _site/
for dir in css js fonts images; do
  if [ -d "$dir" ]; then cp -a "$dir" _site/; fi
done
find . -maxdepth 1 -type f -name 'detail-*.html' -exec cp {} _site/ \;
python3 scripts/build_works.py
touch _site/.nojekyll
echo "Cloudflare Pages output ready: _site/"
