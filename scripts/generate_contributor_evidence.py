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
    return data, hashlib.sha256(raw).hexdigest()


def render(data: dict[str, Any], digest: str) -> str:
    contributions = data["contributions"]
    repositories = {item[0] for item in contributions}
    organizations = {repo.split("/", 1)[0] for repo in repositories}
    counts = Counter(item[2] for item in contributions)
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

    stages = ("PUBLIC SIGNAL", "REPRODUCER", "EXACT HEAD", "TEST MATRIX", "MERGE / RELEASE")
    chain_markup = []
    for index, stage in enumerate(stages):
        x = 82 + index * 300
        if index:
            chain_markup.append(
                f'<path d="M{x - 118} 508h76" stroke="#22d3ee" stroke-width="2" '
                'stroke-dasharray="7 8"/>'
            )
        chain_markup.append(
            f'<g transform="translate({x} 472)"><circle cx="0" cy="36" r="31" '
            f'fill="#0e1b2e" stroke="#22d3ee" stroke-width="2"/>'
            f'<text x="0" y="42" text-anchor="middle" class="node-number">0{index + 1}</text>'
            f'<text x="0" y="91" text-anchor="middle" class="node-label">{stage}</text></g>'
        )

    track_markup = []
    for index, track_id in enumerate(TRACK_ORDER):
        label, summary, accent = data["tracks"][track_id]
        x = 72 + index * 492
        track_markup.append(
            f'<g transform="translate({x} 642)"><rect width="452" height="155" rx="18" '
            f'fill="#09111f" stroke="#22314a"/><rect width="7" height="155" rx="3.5" '
            f'fill="{accent}"/><text x="30" y="46" class="track-label" fill="{accent}">{label}</text>'
            f'<text x="30" y="84" class="track-count">{counts[track_id]:02d}</text>'
            f'<text x="92" y="82" class="muted">merged changes</text>'
            f'<text x="30" y="123" class="track-summary">{summary}</text></g>'
        )

    observed = data["observed_at"].replace("T", " ").replace("Z", " UTC")
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="900" viewBox="0 0 1600 900" role="img" aria-labelledby="title desc">
<title id="title">CAOShurong contributor evidence graph</title>
<desc id="desc">A deterministic profile card showing {len(contributions)} merged external contributions across {len(organizations)} organizations and {len(repositories)} repositories.</desc>
<defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#050914"/><stop offset=".55" stop-color="#071321"/><stop offset="1" stop-color="#0a1020"/></linearGradient><radialGradient id="glow" cx=".82" cy=".08" r=".75"><stop offset="0" stop-color="#0e7490" stop-opacity=".28"/><stop offset="1" stop-color="#0e7490" stop-opacity="0"/></radialGradient><pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse"><path d="M40 0H0V40" fill="none" stroke="#24324a" stroke-opacity=".24"/></pattern><filter id="shadow" x="-20%" y="-20%" width="140%" height="140%"><feDropShadow dx="0" dy="14" stdDeviation="18" flood-color="#000814" flood-opacity=".6"/></filter></defs>
<style>text{{font-family:Inter,ui-sans-serif,system-ui,-apple-system,"Segoe UI",sans-serif;fill:#e6edf7}}.kicker{{font-size:18px;font-weight:700;letter-spacing:3.5px;fill:#67e8f9}}.title{{font-size:54px;font-weight:750;letter-spacing:-1.4px}}.subtitle{{font-size:21px;fill:#9baac0}}.motto{{font-size:19px;font-weight:700;fill:#34d399;letter-spacing:.8px}}.metric{{font-size:62px;font-weight:800;fill:#f8fafc}}.metric-label{{font-size:18px;font-weight:800;letter-spacing:1.4px;fill:#dbeafe}}.muted{{font-size:17px;fill:#8292aa}}.section{{font-size:16px;font-weight:800;letter-spacing:3px;fill:#7dd3fc}}.node-number{{font-size:17px;font-weight:800;fill:#67e8f9}}.node-label{{font-size:14px;font-weight:700;letter-spacing:1px;fill:#cbd5e1}}.track-label{{font-size:15px;font-weight:800;letter-spacing:1.2px}}.track-count{{font-size:38px;font-weight:800;fill:#f8fafc}}.track-summary{{font-size:17px;fill:#aebbd0}}.footer{{font-family:"Cascadia Mono","SFMono-Regular",Consolas,monospace;font-size:13px;fill:#64748b}}</style>
<rect x="1" y="1" width="1598" height="898" rx="26" fill="url(#bg)" stroke="#25334a" stroke-width="2"/><rect x="1" y="1" width="1598" height="898" rx="26" fill="url(#glow)"/><rect x="1" y="1" width="1598" height="898" rx="26" fill="url(#grid)"/>
<g filter="url(#shadow)"><path d="M72 63h90" stroke="#22d3ee" stroke-width="4"/><text x="72" y="105" class="kicker">CAOSHURONG // CONTRIBUTOR EVIDENCE</text><text x="72" y="169" class="title">EVIDENCE-FIRST ENGINEER</text><text x="72" y="210" class="subtitle">EE PhD researcher at CUHK · reproducible systems · open-source verification</text><text x="1330" y="105" text-anchor="end" class="motto">NO RUN → NO CLAIM</text>{''.join(metric_markup)}<text x="72" y="452" class="section">THE VERIFICATION PATH</text>{''.join(chain_markup)}{''.join(track_markup)}</g>
<text x="72" y="854" class="footer">PUBLIC SNAPSHOT {observed} · MANIFEST SHA256 {digest[:16]} · DETERMINISTIC SVG</text><text x="1528" y="854" text-anchor="end" class="footer">MERGE ≠ MAINTAINERSHIP · COUNTER ≠ ADOPTION</text>
</svg>
'''


def verify_live(data: dict[str, Any]) -> None:
    completed = subprocess.run(
        [
            "gh",
            "search",
            "prs",
            "--author",
            "CAOShurong",
            "--merged",
            "--limit",
            "1000",
            "--json",
            "repository,number",
        ],
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    live = {
        (item["repository"]["nameWithOwner"], int(item["number"]))
        for item in json.loads(completed.stdout)
        if not item["repository"]["nameWithOwner"].casefold().startswith("caoshurong/")
    }
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
