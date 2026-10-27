#!/usr/bin/env python3
"""Dependency-free structural guard for the portfolio's static front door.

This intentionally does not infer deployed freshness, visual quality,
cross-repository promises, accessibility conformance, or release readiness.
"""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
import sys

ROOT = Path(__file__).resolve().parents[1]


class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids = set()
        self.fragments = []
        self.assets = []
        self.errors = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a:
            if a["id"] in self.ids:
                self.errors.append(f"duplicate element id: {a['id']}")
            self.ids.add(a["id"])
        if tag == "img":
            if not a.get("alt") and a.get("alt") != "":
                self.errors.append(f"image missing alt attribute: {a.get('src')}")
            if not a.get("src"):
                self.errors.append("image missing src")
            else:
                self.assets.append(a["src"])
        if tag == "a":
            href = a.get("href", "")
            if not href:
                self.errors.append("anchor has no href")
            elif href.startswith("#") and len(href) > 1:
                self.fragments.append(href[1:])
            else:
                self.assets.append(href)
        if tag in ("link", "script") and (a.get("href") or a.get("src")):
            self.assets.append(a.get("href") or a.get("src"))


def check():
    problems = []
    for rel in ("README.md", "README.zh-CN.md",
                "docs/PUBLIC-PRESENTATION.md",
                "docs/PUBLIC-PRESENTATION.zh-CN.md"):
        if not (ROOT / rel).is_file():
            problems.append(f"required entry point missing: {rel}")
    html = (ROOT / "index.html").read_text(encoding="utf-8")
    page = Page()
    page.feed(html)
    page.close()
    problems.extend(page.errors)
    if "<html" not in html or not page.ids:
        problems.append("main page is missing expected semantic structure")
    for fragment in page.fragments:
        if unquote(fragment) not in page.ids:
            problems.append(f"unresolved in-page fragment: #{fragment}")
    for link in page.assets:
        parts = urlsplit(link)
        if parts.scheme or parts.netloc or link.startswith(("mailto:", "tel:", "data:", "/")):
            continue  # External live URLs need separate deployment/release validation.
        path = unquote(parts.path)
        if not path or path.startswith("#"):
            continue
        target = (ROOT / path).resolve()
        if not target.is_relative_to(ROOT) or not target.is_file():
            problems.append(f"missing or unsafe local asset/link: {link}")
    for file, needle in (("README.md", "PUBLIC-PRESENTATION.md"),
                         ("README.zh-CN.md", "PUBLIC-PRESENTATION.zh-CN.md")):
        if needle not in (ROOT / file).read_text(encoding="utf-8"):
            problems.append(f"{file} does not link to the public presentation standard")
    if problems:
        for p in problems:
            print("ERROR:", p, file=sys.stderr)
        return 1
    print(f"OK: {len(page.ids)} ids, {len(page.fragments)} anchors and {len(page.assets)} link/asset references inspected")
    print("NOTE: release claims, screenshot provenance, languages and deployed bytes still need manual review")
    return 0


if __name__ == "__main__":
    raise SystemExit(check())
