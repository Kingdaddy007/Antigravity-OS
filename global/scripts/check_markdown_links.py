from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(r"{{USER_HOME_PATH}}\antigravitygold")
PAT = re.compile(r"\[[^\]]*\]\(([^\)]+\.md)\)", re.IGNORECASE)


def resolve_link(source_file: Path, link: str) -> Path:
    l = link.strip()
    if l.lower().startswith("file:///"):
        return Path(l[8:]).resolve()

    if len(l) > 2 and l[1] == ":" and l[2] in {"/", "\\"}:
        return Path(l).resolve()

    if l.startswith("./"):
        l = l[2:]
    return (source_file.parent / l).resolve()


def main() -> None:
    missing: list[dict[str, str]] = []
    total = 0

    for p in ROOT.rglob("*.md"):
        if ".git" in p.parts or ".ruff_cache" in p.parts:
            continue

        text = p.read_text(encoding="utf-8", errors="ignore")
        for link in PAT.findall(text):
            clean = link.strip()
            if clean.startswith("http://") or clean.startswith("https://"):
                continue

            total += 1
            target = resolve_link(p, clean)
            if target.suffix.lower() == ".md" and not target.exists():
                missing.append({"from": p.relative_to(ROOT).as_posix(), "link": link})

    print(
        json.dumps(
            {
                "total_markdown_links": total,
                "missing_markdown_links": len(missing),
                "samples": missing[:100],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
