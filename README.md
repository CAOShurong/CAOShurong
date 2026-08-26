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
| **[contextcost](https://github.com/CAOShurong/contextcost)** | Measures how much LLM context a repository costs to read, identifies the generated/vendored/data files that waste it, and re-measures after a proposed cut so the saving is real, not estimated. | [PyPI](https://pypi.org/project/contextcost/) · [v0.5.2](https://github.com/CAOShurong/contextcost/releases/tag/v0.5.2) · [GitHub Action](https://github.com/CAOShurong/contextcost/blob/main/action.yml) · [MCP server](https://github.com/CAOShurong/contextcost?tab=readme-ov-file#model-context-protocol-mcp) |

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
is what the row says. Refreshed 2026-08-26.

| Project | Latest | What landed |
| --- | --- | --- |
| **[contextcost](https://github.com/CAOShurong/contextcost)** | [v0.5.2](https://github.com/CAOShurong/contextcost/releases/tag/v0.5.2) · 2026-08-26 | Fixed the estimator exceeding its own published error bound on lockfile-heavy repositories; shipped an exact-tokenizer (`cl100k_base`) counting study across real repos. |
| **[BenchLineage](https://github.com/CAOShurong/benchlineage)** | [v0.3.8](https://github.com/CAOShurong/benchlineage/releases/tag/v0.3.8) · 2026-08-26 | One `_version.py` source now feeds `--version` and every bundle, ELN and report stamp — v0.3.6's wheel had shipped internally inconsistent metadata; new tests pin the consistency. |
| **[VulnFuse](https://github.com/CAOShurong/vulnfuse)** | [v0.4.24](https://github.com/CAOShurong/vulnfuse/releases/tag/v0.4.24) · 2026-08-12 | Preserved scanner image identity when correlating Trivy SARIF findings; routine dependency upkeep since. |
| **[WillItBreak](https://github.com/CAOShurong/willitbreak)** | [v0.1.3](https://github.com/CAOShurong/willitbreak/releases/tag/v0.1.3) · 2026-08-12 | `--ascii` now escapes Unicode report content instead of emitting it raw ([#5](https://github.com/CAOShurong/willitbreak/pull/5)). |
| **[FrontierTrials](https://github.com/CAOShurong/frontiertrials)** | [v0.4.1](https://github.com/CAOShurong/frontiertrials/releases/tag/v0.4.1) · 2026-08-26 | Bulk capture: paste every product answer once (separated by `===` name lines) or drop a `.txt`/`.md` file — manual per-product pasting is now the fallback ([f60d00a](https://github.com/CAOShurong/frontiertrials/commit/f60d00a)). |
| **[TermScope](https://github.com/CAOShurong/termscope)** | [v0.4.1](https://github.com/CAOShurong/termscope/releases/tag/v0.4.1) · 2026-08-12 | Fixed token boundaries in labelled telemetry output ([#8](https://github.com/CAOShurong/termscope/pull/8)). |
| **[ColdShelf](https://github.com/CAOShurong/coldshelf)** | [v0.1.7](https://github.com/CAOShurong/coldshelf/releases/tag/v0.1.7) · 2026-08-12 | Version-agnostic installation verification ([#16](https://github.com/CAOShurong/coldshelf/pull/16)). |
| **[EvalInt](https://github.com/CAOShurong/evalint)** | [v0.2.30](https://github.com/CAOShurong/evalint/releases/tag/v0.2.30) · 2026-08-12 | Promptfoo ingestion audited end to end: named metrics, test-case identity, and errors kept out of scores ([#55](https://github.com/CAOShurong/evalint/pull/55), [#57](https://github.com/CAOShurong/evalint/pull/57), [#59](https://github.com/CAOShurong/evalint/pull/59)). |
| **[DidYouLearn](https://github.com/CAOShurong/didyoulearn)** | [v0.1.1](https://github.com/CAOShurong/didyoulearn/releases/tag/v0.1.1) · 2026-08-12 | Release and package-publishing pipeline hardened; attestations moved to the current GitHub action. |
| **[OhmJudge](https://github.com/CAOShurong/ohmjudge)** | [v0.3.0](https://github.com/CAOShurong/ohmjudge/releases/tag/v0.3.0) · 2026-08-11 | Answer-free blind response collection ([#1](https://github.com/CAOShurong/ohmjudge/pull/1)); CodeQL workflow hardening since. |
| **[ResearchBench](https://github.com/CAOShurong/researchbench)** | v0.1.0 · 2026-08-21 | Landscape research batch 2: PaperQA2, SciCode-Verified and MLAgentBench compared, with a synthesis note (2026-08-22). |

Upstream contributions (fixes, reviews and triage in other projects) are
tracked in [COMMUNITY_FOOTPRINT.md](COMMUNITY_FOOTPRINT.md) — 22 merged, 65 open across 33 upstream organisations (live GitHub counts). Latest:
[xarray#11543](https://github.com/pydata/xarray/pull/11543), an independent
exact-head verification review of the fix for silently byte-swapped netCDF4
attribute writes: the corruption was reproduced on pristine base (`>f8 [0,1]`
stored as `[0, 3.03865e-319]` with no warning), cured at head across every
probed case (including classic-format output and scalar/read-only attribute
edge cases), the new regression test fails on base and passes on head, and the
431-test backend selection shows zero behavioural drift;
[rclone#9823](https://github.com/rclone/rclone/pull/9823), a
fix for a nil-ETag panic in S3 multipart uploads (#9822): an UploadPart
success without an ETag header is now treated as retryable so the chunk is
resent instead of crashing the transfer; and [zerolog#795](https://github.com/rs/zerolog/pull/795),
which repoints the README benchmark reference after its host died (NXDOMAIN).

## What I do

Three things, all publicly inspectable:

- **Build tools I use.** Reproducible-engineering, Python-packaging diagnostics,
  local-first data and explainable-security tooling, maintained openly with
  releases and runnable entry points (above).
- **Fix things where I am a user.** 22 accepted pull requests across 12
  upstream projects — eLabFTW, TheELNFileFormat, SampleDB, Astropy, CycloneDX,
  Keycloak, Plotly.js, rclone, Syft, tox, regl-line2d and
  argoproj/argo-workflows. I reproduce each issue locally and ship a test with
  the fix.
- **Help maintainers decide.** Root-cause analyses on upstream issues and
  tested reviews of third-party changes in the same communities.

The full, dated log with per-PR detail is in
[CONTRIBUTIONS.md](CONTRIBUTIONS.md).
