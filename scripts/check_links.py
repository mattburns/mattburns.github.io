#!/usr/bin/env python3
"""Check internal links and images in the built site (public/).

Scans every HTML file for href/src/srcset attributes and verifies that
internal targets resolve to a file in public/. External URLs are not
fetched. Exits non-zero if any broken internal reference is found.

Known-lost media (files that never made it out of the old WordPress export)
are listed in scripts/known-missing.txt and reported as warnings only.

Usage: python3 scripts/check_links.py [public_dir]
"""
import os
import sys
import urllib.parse
from html.parser import HTMLParser

PUBLIC = sys.argv[1] if len(sys.argv) > 1 else "public"
BASE_HOSTS = {"mattburns.co.uk", "www.mattburns.co.uk", "mattburns.github.io"}
ALLOWLIST = os.path.join(os.path.dirname(__file__), "known-missing.txt")


class RefCollector(HTMLParser):
    def __init__(self):
        super().__init__()
        self.refs = []

    def handle_starttag(self, tag, attrs):
        for name, value in attrs:
            if value is None:
                continue
            if name in ("href", "src", "poster", "data-src"):
                self.refs.append(value)
            elif name == "srcset":
                for part in value.split(","):
                    url = part.strip().split(" ")[0]
                    if url:
                        self.refs.append(url)


def target_exists(path):
    """Resolve a root-relative URL path to a file under public/."""
    rel = urllib.parse.unquote(path).lstrip("/")
    full = os.path.join(PUBLIC, rel)
    if os.path.isfile(full):
        return True
    if os.path.isdir(full) and os.path.isfile(os.path.join(full, "index.html")):
        return True
    # Hugo writes uglyURL-less pages as dir/index.html; a link to /foo may
    # also be satisfied by /foo.html (e.g. 404.html).
    if os.path.isfile(full + ".html"):
        return True
    return False


def main():
    broken = []
    escaped = []
    checked = 0
    for root, _, names in os.walk(PUBLIC):
        for name in names:
            if not name.endswith((".html", ".xml")):
                continue
            page = os.path.join(root, name)
            try:
                text = open(page, encoding="utf-8", errors="replace").read()
            except OSError as e:
                print(f"read error {page}: {e}", file=sys.stderr)
                continue
            # Double-escaped entities render as literal "&nbsp;" text in the
            # browser (e.g. a template emitting entities without safeHTML).
            if name.endswith(".html") and "&amp;nbsp;" in text:
                escaped.append(os.path.relpath(page, PUBLIC))
            parser = RefCollector()
            try:
                parser.feed(text)
            except Exception as e:  # malformed html shouldn't kill the run
                print(f"parse error {page}: {e}", file=sys.stderr)
                continue
            page_rel = os.path.relpath(page, PUBLIC)
            for ref in parser.refs:
                url = urllib.parse.urlsplit(ref)
                if url.scheme in ("mailto", "tel", "javascript", "data"):
                    continue
                if url.netloc and url.netloc not in BASE_HOSTS:
                    continue  # external
                path = url.path
                if not path or path == "/":
                    continue
                if not path.startswith("/"):
                    # resolve relative to the page's directory
                    path = "/" + os.path.normpath(
                        os.path.join(os.path.dirname(page_rel), path)
                    ).replace(os.sep, "/")
                checked += 1
                if not target_exists(path):
                    broken.append((page_rel, ref))

    allowed = set()
    if os.path.isfile(ALLOWLIST):
        with open(ALLOWLIST) as f:
            allowed = {l.strip() for l in f if l.strip() and not l.startswith("#")}

    # Report each unique broken target once, with an example source page.
    seen = {}
    for page_rel, ref in broken:
        seen.setdefault(ref, []).append(page_rel)
    failures = 0
    for ref in sorted(seen):
        pages = seen[ref]
        if ref in allowed:
            print(f"KNOWN-MISSING {ref}  (on {len(pages)} page(s))")
        else:
            failures += 1
            print(f"BROKEN {ref}  (on {len(pages)} page(s), e.g. {pages[0]})")
    for page in escaped[:20]:
        print(f"ESCAPED-ENTITY &amp;nbsp; visible as text in {page}")
    print(f"\n{checked} internal refs checked, "
          f"{failures} broken, {len(seen) - failures} known-missing, "
          f"{len(escaped)} pages with double-escaped entities")
    return 1 if failures or escaped else 0


if __name__ == "__main__":
    sys.exit(main())
