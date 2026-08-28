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

## 各项目最近动态

从本机 11 个仓库的 git log 抽取的最新一次发版 / 提交（截至 2026-08-29；仅依赖更新会如实标注）。

| 项目 | 最近发版 | 最近动态 |
| --- | --- | --- |
| **BenchLineage** | [v0.3.8](https://github.com/CAOShurong/benchlineage/releases/tag/v0.3.8) (08-26) | README 新增「零安装试用」：`uvx benchlineage demo …` + `verify` 端到端验证 |
| **VulnFuse** | [v0.4.24](https://github.com/CAOShurong/vulnfuse/releases/tag/v0.4.24) (08-12) | 文档 prettier 表格对齐修复（08-26 仍有提交保持 main 可验证） |
| **WillItBreak** | [v0.1.3](https://github.com/CAOShurong/willitbreak/releases/tag/v0.1.3) (08-12) | `--ascii` 转义 Unicode 报告内容（#5） |
| **FrontierTrials** | [v0.4.1](https://github.com/CAOShurong/frontiertrials/releases/tag/v0.4.1) (08-12) | 批量作答：一次粘贴所有答案或拖入 txt/md 文件（08-26） |
| **TermScope** | [v0.4.1](https://github.com/CAOShurong/termscope/releases/tag/v0.4.1) (08-12) | 修复带标签遥测 token 边界（#8） |
| **ColdShelf** | [v0.1.7](https://github.com/CAOShurong/coldshelf/releases/tag/v0.1.7) (08-12) | 修复版本无关的安裝验证（#16） |
| **contextcost** | [v0.5.3](https://github.com/CAOShurong/contextcost/releases/tag/v0.5.3) (08-26) | GitHub Action 预算门控修复：PR `max-added` 输入从未接线致门控静默不跑，已接通（08-29） |
| **OhmJudge** | [v0.3.0](https://github.com/CAOShurong/ohmjudge/releases/tag/v0.3.0) (08-11) | 仅依赖维护：codeql-action 升至 v4.37.7（#5，08-23） |
| **DidYouLearn** | [v0.1.1](https://github.com/CAOShurong/didyoulearn/releases/tag/v0.1.1) (08-12) | 仅依赖维护：codeql-action 升至 v4.37.7（#9，08-23） |
| **EvalInt** | [v0.2.30](https://github.com/CAOShurong/evalint/releases/tag/v0.2.30) (08-12) | 审计 Promptfoo 命名指标（#59） |
| **ResearchBench** | [v0.1.0](https://github.com/CAOShurong/researchbench/releases/tag/v0.1.0) (08-21) | 文档刷新 handoff workspace 指纹（08-23） |

每条动态都对应一个真实 commit，未做美化；维护型提交如实写「仅依赖维护」。

## Open-source record

The live public snapshot below separates accepted upstream work from proposals
that are still awaiting a maintainer decision.

| Signal | Snapshot |
| --- | ---: |
| Accepted external changes | **29 / 100** |
| Upstream repositories | **16** |
| Upstream owners | **15** |
| Open external proposals | **70** across **40** repositories and **35** owners |

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

Detailed per-PR receipts, reviews, triage, and dated updates remain in
[CONTRIBUTIONS.md](CONTRIBUTIONS.md) and
[COMMUNITY_FOOTPRINT.md](COMMUNITY_FOOTPRINT.md); the compact evidence card is
generated from the [manifest](data/contributor-evidence.json) by the
[validator](scripts/generate_contributor_evidence.py).

[All repositories](https://github.com/CAOShurong?tab=repositories) ·
[Published Python packages](https://pypi.org/user/CAOShurong/)
