# Shurong Cao

Electrical Engineering PhD researcher at CUHK. I build open-source tools for
**trustworthy AI evaluation, reproducible experiments, security evidence, and
practical engineering debugging**.

My projects are usually local-first: the evidence stays inspectable, uncertainty
is shown instead of hidden, and a demo is labelled as a demo rather than passed
off as real-world adoption.

## Start here

| Project | The problem it solves | Use it now |
|---|---|---|
| **[VulnFuse](https://github.com/CAOShurong/vulnfuse)** | Correlates duplicate scanner findings, explains each merge or blocker, measures scanner overlap, compares runs, and exports one offline interactive report without uploading evidence. | [Browser workbench](https://caoshurong.github.io/vulnfuse/) · [v0.4.2](https://github.com/CAOShurong/vulnfuse/releases/tag/v0.4.2) |
| **[Decimen field fork](https://github.com/CAOShurong/decimen-optical-transfer)** | Moves files, stdin, or text from a browser, terminal, or SSH machine to a phone camera using fountain-coded QR—no sender-side browser, phone app, pairing, or receiver-side network path. | [Open receiver](https://caoshurong.github.io/decimen-optical-transfer/receive/) · [installable CLI v0.4.0](https://github.com/CAOShurong/decimen-optical-transfer/releases/tag/v0.4.0-field.1) |
| **[DidYouLearn](https://github.com/CAOShurong/didyoulearn)** | Tests whether an AI tutor produces unaided mastery, transfer, retention, and calibrated confidence—not merely a persuasive answer. | [Browser lab](https://caoshurong.github.io/didyoulearn/#lab) · [v0.1.0 wheel](https://github.com/CAOShurong/didyoulearn/releases/tag/v0.1.0) |
| **[FrontierTrials](https://github.com/CAOShurong/frontiertrials)** | Compares AI products on your own tasks using blind review, local history, and an auditable study mode. | [Personal lab](https://caoshurong.github.io/frontiertrials/try/) · [PyPI](https://pypi.org/project/frontiertrials/) |
| **[BenchLineage](https://github.com/CAOShurong/benchlineage)** | Keeps the chain from experiment intent and instrument identity to raw data, uncertainty, analysis, and report. | [Live demonstration](https://caoshurong.github.io/benchlineage/) · [PyPI](https://pypi.org/project/benchlineage/) |
| **[ReproWeave](https://github.com/CAOShurong/reproweave)** | Maps paper claims to evidence, dependencies, available resources, and a reviewable replication plan. | [Evidence-map demo](https://caoshurong.github.io/reproweave/) · [PyPI](https://pypi.org/project/reproweave/) |
| **[runproof](https://github.com/CAOShurong/runproof)** | Runs coding-agent work in isolated worktrees and accepts it only when user-declared checks pass. | [`pipx install runproof`](https://pypi.org/project/runproof/) |
| **[termscope](https://github.com/CAOShurong/termscope)** | Plots live Arduino, ESP32, or STM32 serial data in a terminal, including over SSH, and preserves Teleplot timestamps and batches. | [`pipx run termscope --demo`](https://pypi.org/project/termscope/) · [v0.2.0](https://github.com/CAOShurong/termscope/releases/tag/v0.2.0) |

## Hardware that exists off-screen

**[STM32F103 multifunction robot car](https://github.com/CAOShurong/Multi-function-tracking-car-based-on-STM32)**
is a photographed and video-demonstrated build with Bluetooth control,
ultrasonic ranging, obstacle avoidance, four-sensor line tracking, servo
scanning, and OLED output. Its complete STM32CubeIDE project, pin map, and
two-byte control protocol are now browsable instead of hidden inside a ZIP.

## Open-source contributions

**[Decimen Optical Transfer — field-use fork](https://github.com/CAOShurong/decimen-optical-transfer)**
adds an installable terminal sender and explicit mobile camera/lens selection
to Evan Crawley's MIT-licensed screen-to-camera file-transfer project. The CLI
sends files, binary stdin, or text from SSH and browserless machines through the
same gzip, SHA-256, and deterministic fountain protocol as the web receiver.
Release v0.4.0 was fresh-installed and exercised on Linux, Windows, and macOS;
it addresses real upstream requests rather than inventing a disconnected demo.
[Try the fork](https://caoshurong.github.io/decimen-optical-transfer/) or
[install the CLI](https://github.com/CAOShurong/decimen-optical-transfer/releases/tag/v0.4.0-field.1).

**[Teleplot PR #52](https://github.com/nesnes/teleplot/pull/52)** makes the
Enter key in Teleplot's VS Code serial sender honor the selected CR, LF, or
CRLF ending, matching the Send button. The patch was submitted upstream and is
awaiting maintainer review; it is not presented here as an upstream release.

## Smaller tools with narrow jobs

- **[jsonxray](https://github.com/CAOShurong/jsonxray)** — infer what is really
  inside JSONL/NDJSON, including outlier records, in constant memory.
- **[evalint](https://github.com/CAOShurong/evalint)** — lint an LLM evaluation
  set for weak reliability, wrong-answer agreement, and near-duplicates.
- **[willitbreak](https://github.com/CAOShurong/willitbreak)** — report only
  dependency API breaks that reach your Python call sites.
- **[slowimports](https://github.com/CAOShurong/slowimports)** — measure Python
  startup cost and identify imports that can safely become lazy.
- **[contextcost](https://github.com/CAOShurong/contextcost)** — measure the
  context cost of a repository and verify a proposed reduction with a second
  walk.
- **[OhmJudge](https://github.com/CAOShurong/ohmjudge)** — generate fresh EE
  calculation tasks and grade model answers locally with executable rules.

## What I try to make verifiable

- Hosted demonstrations use synthetic or fictional data when no real study has
  been run, and say so visibly.
- Research-oriented tools expose their assumptions, uncertainty, and evidence
  receipts instead of collapsing them into one confident score.
- Releases, documentation figures, and install paths are checked as real user
  entry points—not inferred from source code alone.
- Bug reports and small, reproducible contributions are welcome through each
  repository's Issues and Contributing pages.

I am especially interested in measurement provenance, AI evaluation that
survives scrutiny, embedded systems, and tools that turn a vague claim into a
check someone else can rerun.
