"""Build the WOW website into static HTML.

Usage:  python3 build/build.py
Writes every page into the site root (one folder up from this file).
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)

import pages_platform  # noqa: E402
import pages_main  # noqa: E402
import pages_more  # noqa: E402


def main():
    pages = {}
    for mod in (pages_main, pages_more, pages_platform):
        pages.update(mod.build_all())
    for rel, html in pages.items():
        out = os.path.join(ROOT, rel)
        os.makedirs(os.path.dirname(out), exist_ok=True)
        with open(out, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"  wrote {rel}  ({len(html) // 1024} KB)")
    print(f"Built {len(pages)} pages.")


if __name__ == "__main__":
    main()
