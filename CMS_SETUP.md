# Pages CMS — Works management

Repository: https://github.com/arof-log/site (branch `main`)

## Connect
1. Visit https://app.pagescms.org and sign in with GitHub.
2. Give the Pages CMS GitHub app access to `arof-log/site`.
3. Select repository `arof-log/site`, branch `main`, then open **Works**.
4. The Works collection reads `content/works/*.json`. Seven original records were migrated.

## Editing
- Use Works to add, edit, delete, search and sort individual entries.
- IDs should be unique lowercase letters/numbers/hyphens, and are used for file names.
- Set `published` off to hide an entry, and adjust `order` to control card order.
- The `featured` flag controls whether a published entry appears in the current Works gallery.
- Category choices reflect existing categories.
- Original missing values (`year`, `tags`) are intentionally blank.

## Images and detail pages
- CMS uploads images to `images/`.
- Images already hosted externally remain as their original URLs until changed.
- New media URLs are stored as `/images/...`; the Works renderer resolves them relative to the repository Pages URL.
- Set the detail page field to a valid URL/path (e.g. `detail-video.html`).
- Original seven detail page links were preserved, but their target HTML files were not found at repository root during migration.
- If you create detail pages, commit their HTML files at repository root.

## GitHub Pages publishing
1. In GitHub repository Settings > Pages, choose **GitHub Actions** as the build/deployment source.
2. Check Actions > **Deploy Pages CMS portfolio**. On every push to `main` (including CMS edits), the workflow creates `_site/works.json` using `scripts/build_works.py` and deploys `_site` to GitHub Pages.
3. Published site is normally https://arof-log.github.io/site/ (unless a custom domain is configured).
4. This pipeline deploys without committing generated files, preventing commit-trigger loops.

## Data flow
Pages CMS -> `content/works/<id>.json` -> GitHub Actions / `scripts/build_works.py` -> `_site/works.json` -> `js/script.js` -> existing `#works_inner .list` cards.

The original markup is preserved in `index.html` as a fallback until `works.json` loads. Swiper/Fancybox classes and styling are reused.

## Validation notes
- Source has seven cards; each mapped to a separate JSON record.
- No existing `.pages.yml` was found.
- The Pages CMS editor UI and final GitHub Pages deployment must be verified manually after configuring GitHub Pages.
