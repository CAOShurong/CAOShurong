# CAOShurong

![CAOShurong — PhD researcher in Electronic Engineering at CUHK](assets/banner.svg)

<p align="center">
  <a href="#selected-work">Selected work</a> ·
  <a href="#open-source-contributions">Open source</a> ·
  <a href="#collaboration">Collaboration</a>
</p>

I am **Shurong Cao**, a PhD researcher in Electronic Engineering at
**The Chinese University of Hong Kong**, following my bachelor's education at
**Nanjing University**.

I am drawn to difficult questions that do not stay neatly inside one field.
My work is an evolving mix of research, engineering, experimentation, and open
collaboration. Frontier AI is one space I am actively exploring: how advanced
systems reason and fail, how we should evaluate them, and how they can become
useful in real scientific and engineering work.

I care about turning promising ideas into things other people can inspect:
runnable software, explicit tests, reproducible evidence, public releases, and
honest records of what remains uncertain.

## Academic context

- **The Chinese University of Hong Kong** — PhD researcher in Electronic
  Engineering.
- **Nanjing University** — bachelor's degree.

This is the foundation of my work, not its boundary.

## Questions I am exploring

These are current questions rather than permanent labels:

- How can frontier AI systems support scientific and engineering reasoning
  without hiding uncertainty, limitations, or failure?
- What makes an experiment, benchmark, or software result genuinely
  reproducible as tools, data, and models change?
- How can ambiguous technical failures be turned into evidence that other
  researchers and maintainers can inspect and act on?
- What new questions become possible when research, software, and intelligent
  systems are designed together?

## Selected work

| Project | What you can inspect | Public entry points |
| --- | --- | --- |
| **[BenchLineage](https://github.com/CAOShurong/benchlineage)** | Experiment provenance, instrument identity, calibration, uncertainty budgets, evidence bundles, and ELN exchange. | [PyPI](https://pypi.org/project/benchlineage/) · [v0.3.8](https://github.com/CAOShurong/benchlineage/releases/tag/v0.3.8) |
| **[FrontierTrials](https://github.com/CAOShurong/frontiertrials)** | Local, reproducible capability trials for frontier AI systems, including blinded comparison and a structured study mode. | [try it](https://caoshurong.github.io/frontiertrials/try/) · [study report](https://caoshurong.github.io/frontiertrials/demo/trial-report.html) |
| **[ReproWeave](https://github.com/CAOShurong/reproweave)** | Evidence maps, rebuildability assessment, and replication triage for research papers, with clearly marked synthetic demo data. | [project](https://github.com/CAOShurong/reproweave#readme) · [v0.4.2](https://github.com/CAOShurong/reproweave/releases/tag/v0.4.2) |
| **[VulnFuse](https://github.com/CAOShurong/vulnfuse)** | Explainable correlation across SARIF, SBOM, and security-scanner findings. | [browser workbench](https://caoshurong.github.io/vulnfuse/) · [security model](https://github.com/CAOShurong/vulnfuse/blob/main/SECURITY.md) |
| **[STM32 multifunction robot car](https://github.com/CAOShurong/Multi-function-tracking-car-based-on-STM32)** | A physical embedded system integrating tracking, obstacle avoidance, ultrasonic sensing, Bluetooth control, a servo, and an OLED. | [source and documentation](https://github.com/CAOShurong/Multi-function-tracking-car-based-on-STM32#readme) · [v0.1.1](https://github.com/CAOShurong/Multi-function-tracking-car-based-on-STM32/releases/tag/v0.1.1) |
| **[contextcost](https://github.com/CAOShurong/contextcost)** | Measurement of repository context cost, with a CLI and GitHub Action that verify whether proposed cuts save real tokens. | [PyPI](https://pypi.org/project/contextcost/) · [GitHub Action](https://github.com/CAOShurong/contextcost/blob/main/action.yml) |

Together, these projects exercise research design, data validation, Python and
web tooling, embedded systems, packaging, CI, release engineering, and public
documentation.

<details>
<summary><strong>More projects and research prototypes</strong></summary>

- **[TermScope](https://github.com/CAOShurong/termscope)** — terminal telemetry
  for Arduino, ESP32, and STM32 over serial, pipes, or SSH.
- **[DidYouLearn](https://github.com/CAOShurong/didyoulearn)** — outcome-based
  evaluation for AI tutors.
- **[OhmJudge](https://github.com/CAOShurong/ohmjudge)** — answer-free,
  auditable electrical-engineering model evaluations.
- **[EvalInt](https://github.com/CAOShurong/evalint)** — integrity checks for
  reference-scored LLM evaluation sets.
- **[ResearchBench](https://github.com/CAOShurong/researchbench)** — a running
  comparison of AI systems on real research tasks.
- **[WillItBreak](https://github.com/CAOShurong/willitbreak)** — call-site-aware
  API compatibility analysis with file- and line-level reports.
- **[ColdShelf](https://github.com/CAOShurong/coldshelf)** — a private,
  searchable catalogue for offline drives and their evidence.

</details>

## What I bring to a collaboration

- **Research framing** — turning a broad question into a testable protocol,
  explicit criteria, and a result that can be challenged.
- **End-to-end building** — moving from reproduction and implementation through
  tests, packaging, CI, release, documentation, and a usable entry point.
- **Work across unfamiliar systems** — learning an existing codebase, locating
  the actual failure boundary, and making a scoped change that fits its rules.
- **Evidence-aware communication** — separating a proposal from an accepted
  result, a passing test from a general claim, and public evidence from
  owner-controlled metrics.

## Open-source contributions

I also contribute to projects outside my own repositories. The card below
counts only changes that independent upstream repositories report as merged.

![32 merged external contributions across 18 repositories and 17 upstream owners](assets/contributor-evidence.svg)

The current public record contains **32 merged upstream pull requests** across
**18 repositories** and **17 upstream owners**. Representative examples include:

- [TheELNFileFormat #157](https://github.com/TheELNConsortium/TheELNFileFormat/pull/157) — a reusable web `.eln` checker backed by the project's test suite.
- [CycloneDX Python #1028](https://github.com/CycloneDX/cyclonedx-python-lib/pull/1028) — encoded-path handling for XML schema loading, with regression coverage.
- [Astropy #20256](https://github.com/astropy/astropy/pull/20256) — degraded-accuracy handling for expired IERS predictive values, including tests and documentation.
- [Plotly.js #7959](https://github.com/plotly/plotly.js/pull/7959) — numeric color sorting in the parcats bundle, with implementation and tests.
- [rclone #9823](https://github.com/rclone/rclone/pull/9823) — retryable handling when a successful S3 `UploadPart` response omits an ETag.
- [Apache Magpie #1118](https://github.com/apache/magpie/pull/1118) — more stable per-PR progress for PR-management triage and its evaluation fixtures.

<details>
<summary><strong>Evidence, active proposals, and claim boundaries</strong></summary>

As of 2026-08-30, there are also **75 open external proposals** across **48
repositories** and **43 upstream owners**. They are ongoing proposals, not
accepted contributions, and are deliberately excluded from the merged count.

The accepted set is generated from a
[versioned manifest](data/contributor-evidence.json) and checked against live
GitHub state. Detailed PR receipts, reviews, and dated updates are recorded in
[CONTRIBUTIONS.md](CONTRIBUTIONS.md) and
[COMMUNITY_FOOTPRINT.md](COMMUNITY_FOOTPRINT.md).

A merged contribution demonstrates upstream acceptance; it does not imply
maintainership or independent adoption of my own projects.

</details>

## Collaboration

I welcome conversations about **research collaborations, internships, and
technically ambitious engineering projects**, especially where rigorous
investigation and practical building belong together.

I am based in **Hong Kong**. In-person work in **Hong Kong or Shenzhen** is
practical. For teams in **North America, Europe, and other regions**, remote
collaboration is generally the most workable arrangement; long-term relocation
outside Hong Kong may be difficult at present.

[Email me](mailto:shurongcao0819@gmail.com) ·
[Explore all repositories](https://github.com/CAOShurong?tab=repositories) ·
[Published Python packages](https://pypi.org/user/CAOShurong/)

<details>
<summary><strong>中文简介与合作方式</strong></summary>

我是曹书荣（CAOShurong），现为香港中文大学电子工程博士研究生，本科毕业于南京大学。我的工作横跨研究、工程实践、实验验证与开放协作；前沿人工智能是我正在深入探索的重要领域之一，但不是对未来方向的限制。

我欢迎研究合作、实习以及有挑战性的技术项目。目前常驻香港，香港和深圳适合线下合作；与北美、欧洲及其他地区的团队通常更适合远程合作，现阶段长期离开香港可能较为困难。

</details>
