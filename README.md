# CAOShurong

![Shurong Cao — Electrical Engineering PhD researcher](assets/banner.svg)

<p align="center">
  <sub>Electrical Engineering PhD researcher at CUHK · scientific computing · reproducible systems · open-source maintenance</sub>
</p>

I build trustworthy computational tools for scientific and engineering
workflows. My work sits at the intersection of experiment provenance,
software reliability, security evidence, and evaluation methodology.

My working style is evidence-first: define the failure mode, reproduce it,
test the boundary, and publish the smallest useful artifact. Claims are tied
to code, releases, or public upstream records; ownership, acceptance, and
independent use are kept distinct.

## Research interests

- **Reproducible engineering** — provenance, calibration, uncertainty, and
  portable evidence bundles for experiments.
- **Scientific data interoperability** — ELN formats, validation, and
  loss-aware exchange between research tools.
- **Software and supply-chain reliability** — package behavior, API changes,
  SBOM semantics, release checks, and failure boundaries.
- **Evaluation methodology** — answer-free model trials, outcome-based
  tutoring studies, and inspectable research workflows.

## Selected public tools

The following projects are the compact set I use to represent my current
engineering and research practice.

| Project | Research or engineering focus | Public entry points |
| --- | --- | --- |
| **[BenchLineage](https://github.com/CAOShurong/benchlineage)** | Experiment provenance, calibration, uncertainty, evidence bundles, and ELN import/export. | [PyPI](https://pypi.org/project/benchlineage/) · [v0.3.8](https://github.com/CAOShurong/benchlineage/releases/tag/v0.3.8) |
| **[VulnFuse](https://github.com/CAOShurong/vulnfuse)** | Explainable correlation of SARIF, SBOM, and multi-scanner security findings. | [browser workbench](https://caoshurong.github.io/vulnfuse/) · [v0.4.24](https://github.com/CAOShurong/vulnfuse/releases/tag/v0.4.24) · [security model](https://github.com/CAOShurong/vulnfuse/blob/main/SECURITY.md) |
| **[WillItBreak](https://github.com/CAOShurong/willitbreak)** | Call-site-aware API compatibility analysis with file and line-level reports. | [project README](https://github.com/CAOShurong/willitbreak#readme) |
| **[FrontierTrials](https://github.com/CAOShurong/frontiertrials)** | Reproducible capability trials for frontier models behind one configuration. | [try it](https://caoshurong.github.io/frontiertrials/try/) · [study report](https://caoshurong.github.io/frontiertrials/demo/trial-report.html) |
| **[TermScope](https://github.com/CAOShurong/termscope)** | Terminal telemetry for Arduino, ESP32, and STM32 over serial, pipes, or SSH. | [PyPI](https://pypi.org/project/termscope/) · [v0.4.1](https://github.com/CAOShurong/termscope/releases/tag/v0.4.1) |
| **[ColdShelf](https://github.com/CAOShurong/coldshelf)** | A private, searchable catalogue for unplugged drives and their evidence. | [latest release](https://github.com/CAOShurong/coldshelf/releases/latest) · [scope and limits](https://github.com/CAOShurong/coldshelf#scope-and-limitations) |
| **[contextcost](https://github.com/CAOShurong/contextcost)** | Measures repository context cost and verifies whether proposed cuts save real tokens. | [PyPI](https://pypi.org/project/contextcost/) · [v0.5.3](https://github.com/CAOShurong/contextcost/releases/tag/v0.5.3) · [GitHub Action](https://github.com/CAOShurong/contextcost/blob/main/action.yml) |

## Research prototypes

- **[OhmJudge](https://github.com/CAOShurong/ohmjudge)** — answer-free,
  auditable electrical-engineering model evaluations.
- **[DidYouLearn](https://github.com/CAOShurong/didyoulearn)** — outcome-based
  evaluation for AI tutors.
- **[EvalInt](https://github.com/CAOShurong/evalint)** — integrity checks for
  reference-scored LLM evaluation sets.
- **[ResearchBench](https://github.com/CAOShurong/researchbench)** — a running
  comparison of AI systems on real research tasks.

## Open-source record

The live public snapshot below separates accepted upstream work from proposals
that are still awaiting a maintainer decision.

| Signal | Snapshot |
| --- | ---: |
| Accepted external changes | **29 / 100** |
| Upstream repositories | **16** |
| Upstream owners | **15** |
| Open external proposals | **68** across **40** repositories and **35** owners |

Only PRs that GitHub reports as merged are included in the accepted count.
Detailed per-PR receipts, reviews, triage, and dated updates remain in
[CONTRIBUTIONS.md](CONTRIBUTIONS.md) and
[COMMUNITY_FOOTPRINT.md](COMMUNITY_FOOTPRINT.md); the compact evidence card is
generated from the [manifest](data/contributor-evidence.json) by the
[validator](scripts/generate_contributor_evidence.py).

## Evidence boundary

A merged upstream change demonstrates acceptance, not external maintainership.
Owner-controlled counters, downloads, and self-authored listings are not
presented as independent adoption. The portfolio is intentionally small:
useful artifacts, runnable entry points, explicit limits, and reproducible
public evidence matter more than repository volume.

[All repositories](https://github.com/CAOShurong?tab=repositories) ·
[Published Python packages](https://pypi.org/user/CAOShurong/)
