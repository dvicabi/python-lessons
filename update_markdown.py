import os
import argparse
from datetime import datetime

EXCLUDE_DIRS = {
    ".git", ".github", "node_modules", "venv", ".venv", "__pycache__",
    "assets", "images", "img", "static", "media", "screenshots", "dist", "build"
}
INCLUDE_EXT = {".md"}
SKIP_TAG = "<!-- DC_SKIP -->"

HEADER_ANCHOR_START = "<!-- DC_HEADER_START -->"
HEADER_ANCHOR_END   = "<!-- DC_HEADER_END -->"
FOOTER_ANCHOR_START = "<!-- DC_FOOTER_START -->"
FOOTER_ANCHOR_END   = "<!-- DC_FOOTER_END -->"

def load_snippet(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def insert_after_front_matter(content: str, header_block: str) -> str:
    # שומר YAML Front-Matter אם קיים
    if content.startswith("---\n"):
        idx = content.find("\n---", 4)
        if idx != -1:
            idx_end = idx + len("\n---")
            prefix = content[:idx_end].rstrip() + "\n\n"
            body = content[idx_end:].lstrip()
            return f"{prefix}{header_block}\n{body}"
    return f"{header_block}\n{content.lstrip()}"

def should_skip_file(path: str, content: str, skip_readmes: bool) -> bool:
    name = os.path.basename(path).lower()
    if SKIP_TAG in content:
        return True
    if skip_readmes and name in {"readme.md"}:
        return True
    return False

def process_file(path: str, header_block: str, footer_block: str, dry_run: bool, skip_readmes: bool) -> bool:
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    if should_skip_file(path, content, skip_readmes):
        return False

    has_header = (HEADER_ANCHOR_START in content and HEADER_ANCHOR_END in content)
    has_footer = (FOOTER_ANCHOR_START in content and FOOTER_ANCHOR_END in content)

    changed = False

    if not has_header:
        content = insert_after_front_matter(content, header_block)
        changed = True

    if not has_footer:
        if not content.endswith("\n"):
            content += "\n"
        content = f"{content.rstrip()}\n\n{footer_block}\n"
        changed = True

    if changed and not dry_run:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)

    return changed

def main():
    parser = argparse.ArgumentParser(description="Add bilingual header/footer to Markdown files recursively.")
    parser.add_argument("--root", default=".", help="Repository root to scan.")
    parser.add_argument("--dry-run", action="store_true", help="Scan only; do not write changes.")
    parser.add_argument("--git", action="store_true", help="Run git add/commit/push after changes.")
    parser.add_argument("--branch", default="main", help="Branch to push (default: main).")
    parser.add_argument("--include-readmes", action="store_true", help="Also update README.md files.")
    args = parser.parse_args()

    year = str(datetime.now().year)
    header = load_snippet("header.md").replace("{{YEAR}}", year)
    footer = load_snippet("footer.md").replace("{{YEAR}}", year)

    touched = []

    for root, dirs, files in os.walk(args.root):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        for fname in files:
            _, ext = os.path.splitext(fname)
            if ext.lower() not in INCLUDE_EXT:
                continue
            if fname.lower() in {"header.md", "footer.md"}:
                continue
            full = os.path.join(root, fname)
            try:
                if process_file(full, header, footer, dry_run=args.dry_run, skip_readmes=not args.include_readmes):
                    touched.append(full)
            except Exception as e:
                print(f"⚠️  Failed on {full}: {e}")

    if args.dry_run:
        print("\nDRY RUN: files that WOULD change:")
        for p in touched:
            print(" -", p)
    else:
        print("\nUpdated files:")
        for p in touched:
            print(" -", p)

    if args.git and not args.dry_run and touched:
        os.system("git add .")
        os.system('git commit -m "chore(md): add DC header/footer across repo"')
        os.system(f"git push origin {args.branch}")

if __name__ == "__main__":
    main()
