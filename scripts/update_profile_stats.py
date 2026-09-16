"""Refresh only the profile's marked upstream totals from public GitHub state."""
from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

from verify_contributor_evidence import fetch_merged_external, load_manifest

ROOT = Path(__file__).resolve().parents[1]
START = "<!-- upstream-stats:start -->"
END = "<!-- upstream-stats:end -->"


def update_readme(text: str, live: set[tuple[str, int]], date: str) -> str:
    if text.count(START) != 1 or text.count(END) != 1:
        raise ValueError("expected exactly one upstream statistics block")
    before, rest = text.split(START)
    old, after = rest.split(END)
    if not live:
        raise ValueError("refusing to replace contribution totals with an empty result")
    repositories = {repo.casefold() for repo, _ in live}
    summary = f"**{len(live)} merged pull requests · {len(repositories)} upstream repositories**"
    # Avoid timestamp-only commits when totals have not changed.
    if summary in old:
        return text
    block = f"\n\n{summary}<br>\n<sub>External repositories only · Updated {date}</sub>\n\n"
    return before + START + block + END + after


def main() -> None:
    live = fetch_merged_external()
    manifest, _ = load_manifest()
    archived = {(repo, int(number)) for repo, number, _ in manifest["contributions"]}
    if not archived.issubset(live):
        raise ValueError("archived merges absent from live result; leaving README unchanged")
    path = ROOT / "README.md"
    text = path.read_text(encoding="utf-8")
    updated = update_readme(text, live, datetime.now(timezone.utc).strftime("%d %B %Y"))
    if updated != text:
        path.write_text(updated, encoding="utf-8", newline="\n")
        print("Updated upstream totals.")
    else:
        print("Upstream totals unchanged.")


if __name__ == "__main__":
    main()
