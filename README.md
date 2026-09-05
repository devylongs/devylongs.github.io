# Longs Pemun Gotar — personal website

A small personal website inspired by [gakonst.com](https://gakonst.com/): black background, serif type, a centered column, and simple navigation. Built entirely with HTML and CSS. No JavaScript, framework, package installation, or build step is needed.

## Edit the site

- `site/index.html`: name, introduction, and links.
- `site/about/index.html`: background and experience.
- `site/projects/index.html`: Gean, Tokkenly, Gean Labs, and BlockFuse Labs.
- `site/contact/index.html`: public contact links.
- `site/styles.css`: shared styles and mobile breakpoints.

The initial copy is a draft based on your workspace's professional profile and the public [Gean repository](https://github.com/geanlabs/gean). Review it before publishing. The contact page includes your supplied email, `longs@geanlabs.com`, and X profile, `https://x.com/devlongs_`.

Gean Labs links use [geanlabs.com](https://geanlabs.com). Tokkenly's description is based on its [public website](https://tokkenly-website.kvng.workers.dev/) and is framed as a project you are building. Links explicitly labeled as open-source work still point to GitHub.

Each HTML file contains its own navigation so every page works independently. When renaming a page or changing the name, update all four files. Keep the current page's `aria-current="page"` attribute on the matching navigation link.

## Preview and check

From this directory:

```sh
python3 -m http.server 4173 --bind 127.0.0.1 --directory site
```

Open http://127.0.0.1:4173/ and refresh after editing. Stop the server with Ctrl+C. Python is only a local preview tool; the published website runs directly in a browser.

Check all local page links, CSS paths, anchors, and mobile metadata:

```sh
python3 scripts/check_site.py
```

## Deploy to GitHub Pages

1. Use this `personal-site` directory as the root of a dedicated GitHub repository. The workflow expects `site/` and `.github/` at the repository root.
2. For an account homepage, name the repository `devylongs.github.io`. Any other repository name also works; it will be hosted under that repository's path.
3. In the repository, select **Settings → Pages → Build and deployment → Source → GitHub Actions**.
4. Once the files are in the repository's `main` branch, run **Actions → Deploy to GitHub Pages → Run workflow**, or let the workflow run on the next push to `main`.
5. Open the URL shown by the completed deployment.

The workflow validates the HTML and uploads only `site/`. It uses GitHub's built-in deployment token and requires no extra secrets. Change the workflow's branch filter if your default branch is not `main`.

Relative links support both `https://devylongs.github.io/` and `https://devylongs.github.io/<repository>/`. No URL rewriting or single-page-app fallback is required.

See GitHub's [publishing-source instructions](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site) and [custom workflow documentation](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages).

Git staging, commits, and pushes require your explicit approval under this workspace's working agreements.
