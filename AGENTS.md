# Website working agreements

- The user requested plain HTML and CSS, with JavaScript only if necessary. This site currently needs no JavaScript and has no framework or package dependencies.
- Keep public website files in `site/`. GitHub Pages publishes only that folder.
- Match the minimal serif layout of https://terencechain.com/, including its system-aware light and dark themes, and use Longs's own content.
- Keep the reference's three-page structure: about at the homepage, writing, and work. Condense Longs's information to fit; do not add separate biography, projects, or contact pages.
- Use relative links so the site works on both account and repository GitHub Pages URLs.
- Preview locally and verify desktop, mobile, navigation, and direct page loads after changes.
- Run `python3 scripts/check_site.py` before handoff.
- Never run `git add`, `git commit`, or `git push` without the user's explicit prior approval. Ask for permission before each action.
