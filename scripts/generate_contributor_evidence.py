from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "data" / "contributor-evidence.json"
OUTPUT = ROOT / "assets" / "contributor-evidence.svg"
TRACK_ORDER = ("scientific", "supply_chain", "systems")


def load_manifest(path: Path = MANIFEST) -> tuple[dict[str, Any], str]:
    raw = path.read_bytes()
    data = json.loads(raw)
    if data.get("schema_version") != 1:
        raise ValueError("unsupported schema_version")

    contributions = data.get("contributions", [])
    tracks = data.get("tracks", {})
    if set(tracks) != set(TRACK_ORDER):
        raise ValueError("track definitions do not match the required three lanes")

    seen: set[tuple[str, int]] = set()
    for repository, number, track in contributions:
        owner, _, name = repository.partition("/")
        if not owner or not name or owner.casefold() == "caoshurong":
            raise ValueError(f"not an external repository: {repository}")
        if track not in tracks:
            raise ValueError(f"unknown track: {track}")
        key = (repository, int(number))
        if key in seen:
            raise ValueError(f"duplicate contribution: {repository}#{number}")
        seen.add(key)

    if len(data.get("boundaries", [])) < 3:
        raise ValueError("claim boundaries are required")
    canonical = json.dumps(
        data, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    return data, hashlib.sha256(canonical).hexdigest()


def render(data: dict[str, Any], digest: str) -> str:
    contributions = data["contributions"]
    repositories = {item[0] for item in contributions}
    organizations = {repo.split("/", 1)[0] for repo in repositories}
    repository_counts = Counter(item[0] for item in contributions)
    metrics = (
        (len(contributions), "MERGED EXTERNAL", "accepted changes"),
        (len(organizations), "UPSTREAM ORGS", "external owners"),
        (len(repositories), "UPSTREAM REPOS", "independent codebases"),
    )

    metric_markup = []
    for index, (value, label, note) in enumerate(metrics):
        x = 72 + index * 492
        metric_markup.append(
            f'<g transform="translate({x} 264)"><rect width="452" height="142" rx="18" '
            f'fill="#0b1324" stroke="#23314a"/><path d="M22 20h42" stroke="#22d3ee" '
            f'stroke-width="3"/><text x="24" y="78" class="metric">{value}</text>'
            f'<text x="124" y="65" class="metric-label">{label}</text>'
            f'<text x="124" y="91" class="muted">{note}</text></g>'
        )

    selected_repositories = sorted(
        repositories,
        key=lambda repository: (-repository_counts[repository], repository.casefold()),
    )[:8]
    repository_markup = []
    for index, repository in enumerate(selected_repositories):
        column = index % 4
        row = index // 4
        x = 72 + column * 369
        y = 486 + row * 72
        repository_markup.append(
            f'<g transform="translate({x} {y})"><rect width="345" height="52" rx="12" '
            f'fill="#0a1425" stroke="#243750"/><circle cx="24" cy="26" r="4" '
            f'fill="#67e8f9"/><text x="42" y="32" class="repository">{repository}</text></g>'
        )

    observed = data["observed_at"].replace("T", " ").replace("Z", " UTC")
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="760" viewBox="0 0 1600 760" role="img" aria-labelledby="title desc">
<title id="title">CAOShurong contributor evidence graph</title>
<desc id="desc">A deterministic profile card showing {len(contributions)} merged external contributions across {len(organizations)} organizations and {len(repositories)} repositories.</desc>
<defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#050914"/><stop offset=".55" stop-color="#071321"/><stop offset="1" stop-color="#0a1020"/></linearGradient><radialGradient id="glow" cx=".82" cy=".08" r=".75"><stop offset="0" stop-color="#0e7490" stop-opacity=".28"/><stop offset="1" stop-color="#0e7490" stop-opacity="0"/></radialGradient><pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse"><path d="M40 0H0V40" fill="none" stroke="#24324a" stroke-opacity=".24"/></pattern><filter id="shadow" x="-20%" y="-20%" width="140%" height="140%"><feDropShadow dx="0" dy="14" stdDeviation="18" flood-color="#000814" flood-opacity=".6"/></filter></defs>
<style>text{{font-family:Inter,ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;fill:#e6edf7}}.kicker{{font-size:18px;font-weight:700;letter-spacing:3.5px;fill:#67e8f9}}.title{{font-family:Georgia,"Times New Roman",serif;font-size:48px;font-weight:700;letter-spacing:-.6px}}.subtitle{{font-size:20px;fill:#9baac0}}.motto{{font-size:17px;font-weight:700;fill:#34d399;letter-spacing:1px}}.metric{{font-size:62px;font-weight:800;fill:#f8fafc}}.metric-label{{font-size:18px;font-weight:800;letter-spacing:1.4px;fill:#dbeafe}}.muted{{font-size:17px;fill:#8292aa}}.section{{font-size:16px;font-weight:800;letter-spacing:3px;fill:#7dd3fc}}.repository{{font-size:16px;font-weight:650;fill:#d8e4f4}}.statement{{font-family:Georgia,"Times New Roman",serif;font-size:27px;font-style:italic;fill:#cbd5e1}}.footer{{font-family:"Cascadia Mono","SFMono-Regular",Consolas,monospace;font-size:13px;fill:#64748b}}</style>
<rect x="1" y="1" width="1598" height="758" rx="26" fill="url(#bg)" stroke="#25334a" stroke-width="2"/><rect x="1" y="1" width="1598" height="758" rx="26" fill="url(#glow)"/><rect x="1" y="1" width="1598" height="758" rx="26" fill="url(#grid)"/>
<g filter="url(#shadow)"><path d="M72 63h90" stroke="#22d3ee" stroke-width="4"/><text x="72" y="105" class="kicker">CAOSHURONG // PUBLIC CONTRIBUTIONS</text><text x="72" y="165" class="title">Open-source work, verified upstream</text><text x="72" y="204" class="subtitle">Only changes merged by independent repositories are counted here.</text><text x="1528" y="105" text-anchor="end" class="motto">PUBLIC RECORD · DATED SNAPSHOT</text>{''.join(metric_markup)}<text x="72" y="448" class="section">REPRESENTATIVE UPSTREAMS</text>{''.join(repository_markup)}<text x="800" y="662" text-anchor="middle" class="statement">Different codebases. Different questions. One public record.</text></g>
<text x="72" y="718" class="footer">SNAPSHOT {observed} · MANIFEST SHA256 {digest[:16]} · DETERMINISTIC SVG</text><text x="1528" y="718" text-anchor="end" class="footer">MERGE ≠ MAINTAINERSHIP · COUNTER ≠ ADOPTION</text>
</svg>
'''


def verify_live(data: dict[str, Any]) -> None:
    query = """
    query($cursor: String) {
      user(login: "CAOShurong") {
        pullRequests(
          first: 100
          after: $cursor
          states: MERGED
          orderBy: {field: UPDATED_AT, direction: DESC}
        ) {
          nodes { number repository { nameWithOwner owner { login } } }
          pageInfo { hasNextPage endCursor }
        }
      }
    }
    """
    live: set[tuple[str, int]] = set()
    cursor: str | None = None
    while True:
        command = ["gh", "api", "graphql", "-f", f"query={query}"]
        if cursor is not None:
            command.extend(["-F", f"cursor={cursor}"])
        completed = subprocess.run(
            command,
            check=True,
            capture_output=True,
            text=True,
            encoding="utf-8",
        )
        connection = json.loads(completed.stdout)["data"]["user"]["pullRequests"]
        for item in connection["nodes"]:
            repository = item["repository"]
            if repository["owner"]["login"].casefold() != "caoshurong":
                live.add((repository["nameWithOwner"], int(item["number"])))
        page_info = connection["pageInfo"]
        if not page_info["hasNextPage"]:
            break
        cursor = page_info["endCursor"]
    manifest = {(item[0], int(item[1])) for item in data["contributions"]}
    if live != manifest:
        missing = sorted(live - manifest)
        stale = sorted(manifest - live)
        raise ValueError(
            "public snapshot differs from manifest; "
            f"missing_from_manifest={missing}, no_longer_live={stale}"
        )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--verify-live", action="store_true")
    args = parser.parse_args()
    data, digest = load_manifest()
    if args.verify_live:
        verify_live(data)
        print(f"live public contribution set matches manifest: {len(data['contributions'])}")
    rendered = render(data, digest)
    if args.check:
        if not OUTPUT.exists() or OUTPUT.read_text(encoding="utf-8") != rendered:
            print(f"stale generated asset: {OUTPUT}")
            return 1
        print(f"contributor evidence is current: {digest}")
        return 0
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(rendered, encoding="utf-8", newline="\n")
    print(f"wrote {OUTPUT} from sha256:{digest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
