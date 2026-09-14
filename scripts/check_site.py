"""Check the actual static website using only the Python standard library."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.ids = set()
        self.tags = []
        self.current = 0
        self.viewport = False

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        self.tags.append(tag)
        if "id" in attrs:
            assert attrs["id"] not in self.ids, f"Duplicate id: {attrs['id']}"
            self.ids.add(attrs["id"])
        for key in ("href", "src"):
            if key in attrs:
                self.links.append(attrs[key])
        self.current += attrs.get("aria-current") == "page"
        self.viewport |= tag == "meta" and attrs.get("name") == "viewport"


root = Path(__file__).resolve().parents[1] / "site"
pages = {}
for path in root.rglob("*.html"):
    page = Page()
    page.feed(path.read_text())
    pages[path.resolve()] = page
    assert page.viewport, f"Missing mobile viewport: {path}"
    assert all(tag in page.tags for tag in ("title", "h1", "nav", "main")), path
    assert page.current == 1, f"Expected one active navigation link: {path}"
    assert "script" not in page.tags, f"Site should work with HTML and CSS only: {path}"

expected_pages = {root / "index.html", root / "writing/index.html", root / "work/index.html"}
assert set(pages) == expected_pages, "Expected only About (home), Writing, and Work"
count = 0
for path, page in pages.items():
    for link in page.links:
        url = urlsplit(link)
        if url.scheme or url.netloc:
            assert url.scheme in ("https", "mailto"), f"Unexpected URL: {link}"
            continue
        assert not url.path.startswith("/"), f"Root-relative link breaks project sites: {link}"
        target = (path.parent / unquote(url.path)).resolve() if url.path else path
        if target.is_dir():
            target /= "index.html"
        assert target.is_relative_to(root), f"Link escapes website: {link}"
        assert target.exists(), f"Missing link from {path}: {link}"
        if url.fragment and target in pages:
            assert unquote(url.fragment) in pages[target].ids, f"Missing anchor: {link}"
        count += 1

assert (root / ".nojekyll").exists(), "Missing GitHub Pages marker"
assert not list(root.rglob("*.js")), "Unnecessary JavaScript found"
print(f"PASS: {len(pages)} static pages, {count} local links/assets, mobile metadata, and navigation.")
