from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "data" / "contributor-evidence.json"
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

    canonical = json.dumps(
        data, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    return data, hashlib.sha256(canonical).hexdigest()


def summarize(data: dict[str, Any]) -> tuple[int, int, int]:
    contributions = data["contributions"]
    repositories = {item[0] for item in contributions}
    organizations = {repository.split("/", 1)[0] for repository in repositories}
    return len(contributions), len(repositories), len(organizations)


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
    parser.add_argument("--verify-live", action="store_true")
    args = parser.parse_args()

    data, digest = load_manifest()
    contributions, repositories, organizations = summarize(data)
    print(
        "contributor evidence manifest valid: "
        f"{contributions} merges / {repositories} repositories / "
        f"{organizations} owners / sha256:{digest}"
    )
    if args.verify_live:
        verify_live(data)
        print(f"live public contribution set matches manifest: {contributions}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
