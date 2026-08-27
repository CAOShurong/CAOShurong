# CAOShurong

![Shurong Cao — Electrical Engineering PhD researcher](assets/banner.svg)

<sub>Public evidence snapshot, generated deterministically from the
[manifest](data/contributor-evidence.json) by the
[validator](scripts/generate_contributor_evidence.py). A merged change is not
presented as maintainership; an owner-controlled counter is not presented as
adoption.</sub>

Electrical Engineering PhD researcher at CUHK. I maintain public tools for
reproducible engineering, Python packaging diagnostics, local-first data work,
and explainable security evidence.

I try to make each claim inspectable: public releases, runnable entry points,
documented limits, and direct links to upstream work. A download counter or a
self-submitted project listing is not presented as independent adoption.

## Featured projects

The six repositories pinned above are the current featured set:
BenchLineage, VulnFuse, WillItBreak, FrontierTrials, TermScope and ColdShelf.

| Project | What it does | Verifiable entry points |
| --- | --- | --- |
| **[BenchLineage](https://github.com/CAOShurong/benchlineage)** | Records experiment provenance, calibration, uncertainty and evidence, with portable ELN import/export. | [PyPI](https://pypi.org/project/benchlineage/) · [v0.3.8](https://github.com/CAOShurong/benchlineage/releases/tag/v0.3.8) · [five accepted ELN contributions](https://github.com/TheELNConsortium/TheELNFileFormat/pulls?q=is%3Apr+author%3ACAOShurong+is%3Amerged) |
| **[VulnFuse](https://github.com/CAOShurong/vulnfuse)** | Correlates findings from SARIF, Trivy, Grype, Snyk, CycloneDX, OSV and CSV without hiding merge blockers or scanner disagreement. | [browser workbench](https://caoshurong.github.io/vulnfuse/) · [v0.4.24](https://github.com/CAOShurong/vulnfuse/releases/tag/v0.4.24) · [security model](https://github.com/CAOShurong/vulnfuse/blob/main/SECURITY.md) |
| **[WillItBreak](https://github.com/CAOShurong/willitbreak)** | Diffs a package's public API between two versions and reports only the breaking changes that reach your call sites, with file and line numbers. Zero dependencies. | [README](https://github.com/CAOShurong/willitbreak#readme) |
| **[FrontierTrials](https://github.com/CAOShurong/frontiertrials)** | Runs capability trials against frontier models behind one config and compares the runs, privately. | [try it](https://caoshurong.github.io/frontiertrials/try/) · [study report](https://caoshurong.github.io/frontiertrials/demo/trial-report.html) |
| **[TermScope](https://github.com/CAOShurong/termscope)** | Plots Arduino, ESP32 and STM32 telemetry in a terminal over serial, pipes or SSH, with CSV record/replay. | [PyPI](https://pypi.org/project/termscope/) · [v0.4.1](https://github.com/CAOShurong/termscope/releases/tag/v0.4.1) · [hardware reports wanted](https://github.com/CAOShurong/termscope/issues/2) |

## Other maintained tools

| Project | What it does | Verifiable entry points |
| --- | --- | --- |
| **[ColdShelf](https://github.com/CAOShurong/coldshelf)** | Builds a private searchable catalog of unplugged drives, including snapshots, duplicate evidence and physical-location notes. | [latest release](https://github.com/CAOShurong/coldshelf/releases/latest) · [quick start](https://github.com/CAOShurong/coldshelf#quick-start) · [limitations](https://github.com/CAOShurong/coldshelf#scope-and-limitations) |
| **[contextcost](https://github.com/CAOShurong/contextcost)** | Measures how much LLM context a repository costs to read, identifies the generated/vendored/data files that waste it, and re-measures after a proposed cut so the saving is real, not estimated. | [PyPI](https://pypi.org/project/contextcost/) · [v0.5.3](https://github.com/CAOShurong/contextcost/releases/tag/v0.5.3) · [GitHub Action](https://github.com/CAOShurong/contextcost/blob/main/action.yml) · [MCP server](https://github.com/CAOShurong/contextcost?tab=readme-ov-file#model-context-protocol-mcp) |

## Research prototypes

Experimental projects — useful, but not yet stable or broadly validated.

| Project | What it does | Verifiable entry points |
| --- | --- | --- |
| **[OhmJudge](https://github.com/CAOShurong/ohmjudge)** | Answer-free, auditable electrical-engineering model evaluations — no API key required. | [README](https://github.com/CAOShurong/ohmjudge#readme) |
| **[DidYouLearn](https://github.com/CAOShurong/didyoulearn)** | Outcome-based evaluation for AI tutors — which one actually helps you understand. | [README](https://github.com/CAOShurong/didyoulearn#readme) |
| **[EvalInt](https://github.com/CAOShurong/evalint)** | Lint your LLM eval set: reliability, items scored against a reference. | [docs](https://github.com/CAOShurong/evalint/tree/main/docs) |
| **[ResearchBench](https://github.com/CAOShurong/researchbench)** | A working researcher's running comparison of AI systems on real research tasks — no API keys, no synthetic datasets, judgment by the person who needed the answer. | [design doc](https://github.com/CAOShurong/researchbench/blob/master/RESEARCH_BENCHMARK.md) |

[See all repositories](https://github.com/CAOShurong?tab=repositories) and
[published Python packages](https://pypi.org/user/CAOShurong/). The projects
above are the small set I currently use to represent my maintenance work.

## Latest changes

What actually landed in each repository lately — the newest release or
substantive commit per project, newest first, drawn from each repository's
own git log. Where only dependency or CI upkeep moved since a release, that
is what the row says. Refreshed 2026-08-27.

| Project | Latest | What landed |
| --- | --- | --- |
| **[contextcost](https://github.com/CAOShurong/contextcost)** | [v0.5.3](https://github.com/CAOShurong/contextcost/releases/tag/v0.5.3) · 2026-08-27 | README's "Why this exists" now opens with the real measured findings — plotly.js **42% (26.8M tokens)** and dask **46.5%** — so a cold visitor meets the wow number before any mechanism ([2f321e3](https://github.com/CAOShurong/contextcost/commit/2f321e3)). The PyPI project page (v0.5.3) still mirrors the repo README with the 17-repo hero table and recalibrated ±23% bound; v0.5.2 fixed the estimator breaching its own printed bound on lockfile-heavy repos (exact `cl100k_base` study across real repos). |
| **[BenchLineage](https://github.com/CAOShurong/benchlineage)** | [v0.3.8](https://github.com/CAOShurong/benchlineage/releases/tag/v0.3.8) · 2026-08-26 | One `_version.py` source now feeds `--version` and every bundle, ELN and report stamp — v0.3.6's wheel had shipped internally inconsistent metadata; new tests pin the consistency ([f035b14](https://github.com/CAOShurong/benchlineage/commit/f035b14)). A zero-install trial followed: `uvx benchlineage demo my-bench --seed 20260804` then `verify`, with the expected `"valid": true` stated up front ([81ee19a](https://github.com/CAOShurong/benchlineage/commit/81ee19a)). |
| **[VulnFuse](https://github.com/CAOShurong/vulnfuse)** | [v0.4.24](https://github.com/CAOShurong/vulnfuse/releases/tag/v0.4.24) · 2026-08-26 | Preserved scanner image identity when correlating Trivy SARIF findings (v0.4.24). Since the release: a `prettier` table-alignment fix in docs/demo/README.md that was breaking the `verify` check on main ([cd75268](https://github.com/CAOShurong/vulnfuse/commit/cd75268)); a synthetic three-scanner demo so the CLI can be tried with no scanner output at all ([90c9d42](https://github.com/CAOShurong/vulnfuse/commit/90c9d42)) and a README worked example walking that demo end to end — five findings become four explainable clusters, with evidence scores and scanner-agreement numbers quoted ([38a95b7](https://github.com/CAOShurong/vulnfuse/commit/38a95b7)). |
| **[WillItBreak](https://github.com/CAOShurong/willitbreak)** | [v0.1.3](https://github.com/CAOShurong/willitbreak/releases/tag/v0.1.3) · 2026-08-12 | `--ascii` now escapes Unicode report content instead of emitting it raw ([#5](https://github.com/CAOShurong/willitbreak/pull/5)). |
| **[FrontierTrials](https://github.com/CAOShurong/frontiertrials)** | [v0.4.1](https://github.com/CAOShurong/frontiertrials/releases/tag/v0.4.1) · 2026-08-26 | Bulk capture: paste every product answer once (separated by `===` name lines) or drop a `.txt`/`.md` file — manual per-product pasting is now the fallback ([f60d00a](https://github.com/CAOShurong/frontiertrials/commit/f60d00a)). |
| **[TermScope](https://github.com/CAOShurong/termscope)** | [v0.4.1](https://github.com/CAOShurong/termscope/releases/tag/v0.4.1) · 2026-08-12 | Fixed token boundaries in labelled telemetry output ([#8](https://github.com/CAOShurong/termscope/pull/8)). |
| **[ColdShelf](https://github.com/CAOShurong/coldshelf)** | [v0.1.7](https://github.com/CAOShurong/coldshelf/releases/tag/v0.1.7) · 2026-08-12 | Version-agnostic installation verification ([#16](https://github.com/CAOShurong/coldshelf/pull/16)). |
| **[EvalInt](https://github.com/CAOShurong/evalint)** | [v0.2.30](https://github.com/CAOShurong/evalint/releases/tag/v0.2.30) · 2026-08-12 | Promptfoo ingestion audited end to end: named metrics, test-case identity, and errors kept out of scores ([#55](https://github.com/CAOShurong/evalint/pull/55), [#57](https://github.com/CAOShurong/evalint/pull/57), [#59](https://github.com/CAOShurong/evalint/pull/59)). |
| **[DidYouLearn](https://github.com/CAOShurong/didyoulearn)** | [v0.1.1](https://github.com/CAOShurong/didyoulearn/releases/tag/v0.1.1) · 2026-08-12 | Release and package-publishing pipeline hardened; attestations moved to the current GitHub action. Only dependency upkeep since ([#9](https://github.com/CAOShurong/didyoulearn/pull/9)). |
| **[OhmJudge](https://github.com/CAOShurong/ohmjudge)** | [v0.3.0](https://github.com/CAOShurong/ohmjudge/releases/tag/v0.3.0) · 2026-08-11 | Answer-free blind response collection ([#1](https://github.com/CAOShurong/ohmjudge/pull/1)). Only dependency upkeep since ([#5](https://github.com/CAOShurong/ohmjudge/pull/5)); CodeQL workflow hardening noted earlier still stands. |
| **[ResearchBench](https://github.com/CAOShurong/researchbench)** | v0.1.0 · 2026-08-21 | Landscape research batch 2: PaperQA2, SciCode-Verified and MLAgentBench compared, with a synthesis note (2026-08-22). |

Upstream contributions (fixes, reviews and triage in other projects) are
tracked in [COMMUNITY_FOOTPRINT.md](COMMUNITY_FOOTPRINT.md) — 24 merged across
13 upstream owners; 68 open across 35 upstream owners (live GitHub counts).
Latest:
[cibuildwheel#2977](https://github.com/pypa/cibuildwheel/pull/2977), a docs-only
fix for four dead CircleCI/CPython documentation links (the replacement URLs
were checked live; exact head `0ac3d2da`; OPEN/MERGEABLE at the audit); then
[tox-dev/tox#4042](https://github.com/tox-dev/tox/pull/4042), a docs-only fix for
the dead virtualenv discovery link (old URL 404, replacement URL 200; exact
head `4ef082c9`; `tox run -e docs`, `tox run -e fix`, and targeted pre-commit
hooks reported passing; OPEN/MERGEABLE with reviewer `rahuldevikar` requested,
20 of 30 current contexts successful, 2 unrelated `tox env type` failures and
8 still running); before that,
[gitleaks#2249](https://github.com/gitleaks/gitleaks/pull/2249#pullrequestreview-5039796619), a verification review of an external author's fix for the file-read sibling of our own #2252 — a partial scan (an unreadable file) was silently reported as `no leaks found` exit 0. Reviewed from exact head `509fce15`: `go build`/`go vet`/`go test ./sources/` all clean, and the root cause (goroutine errors via `s.Sema.Go` are never read because no `.Wait()` is ever called) was independently confirmed by grep; recommended a sibling fix for the same defect class; before that,
[gitleaks#2252](https://github.com/gitleaks/gitleaks/pull/2252), a fix for a
CI-safety bug where a failing git scan is silently reported as a clean pass
(built `master`, reproduced a `0 commits scanned` run that still exits `0` with
"no leaks found"; root cause was the swallowed git-scan error in
`DetectSource` — fixed by propagating it so the existing non-zero exit path
fires, with a regression test that is RED on pristine `master` and GREEN with
the patch); before that,
[yq#2840](https://github.com/mikefarah/yq/pull/2840), a docs fix that replaces a dead
Snapcraft confinement link in the README (the old `docs.snapcraft.io/snap-confinement/6233`
URL now 404s; it now points at the live `snapcraft.io/docs/snap-confinement` page —
first contribution to mikefarah/yq);
[dask#12560](https://github.com/dask/dask/pull/12560#issuecomment-5425786759),
an exact-head verification review of the fix for `str.split(expand=True)`
silently reporting `object`/`str` metadata while computing `string` columns:
a pandas-vs-meta-vs-computed matrix across three input dtypes and two
`convert-string` settings shows every probe internally consistent at head,
the full dask-expr suite passes 4329 tests with zero failures, the red
`nightly` CI job is attributed to unrelated scipy-sparse deprecation fallout,
and the review documents a pre-existing hash-seed-dependent metadata leak on
main with a minimal reproducer;
[zarr-python#4290](https://github.com/zarr-developers/zarr-python/pull/4290),
which honors explicit rectilinear chunk-grid requests whose edges happen to be
uniform: since 3.3.0 a nested-sequence spec like `[[10, 10, 4]]` was silently
collapsed to a regular grid, and the two diverge under `resize` — the regular
grid extends the uniform pattern while the rectilinear grid appends an edge, so
append-only workloads got a chunk-rewriting layout they never asked for; and
[rclone#9823](https://github.com/rclone/rclone/pull/9823), a
fix for a nil-ETag panic in S3 multipart uploads (#9822): an UploadPart
success without an ETag header is now treated as retryable so the chunk is
resent instead of crashing the transfer.

## What I do

Three things, all publicly inspectable:

- **Build tools I use.** Reproducible-engineering, Python-packaging diagnostics,
  local-first data and explainable-security tooling, maintained openly with
  releases and runnable entry points (above).
- **Fix things where I am a user.** 24 accepted pull requests across 14
  upstream repositories — eLabFTW, TheELNFileFormat, SampleDB, Astropy,
  CycloneDX, Keycloak, Plotly.js, rclone, Syft, tox, regl-line2d,
  argoproj/argo-workflows and ORT. I reproduce each issue locally and ship a
  test with the fix.
- **Help maintainers decide.** Root-cause analyses on upstream issues and
  tested reviews of third-party changes in the same communities.

The full, dated log with per-PR detail is in
[CONTRIBUTIONS.md](CONTRIBUTIONS.md).
