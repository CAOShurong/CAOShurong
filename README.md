# Shurong Cao

Electrical Engineering PhD researcher at CUHK. I build open-source tools for
practical file and data problems, developer diagnostics, trustworthy AI
evaluation, and reproducible engineering work.

The common thread is inspectability: local-first operation where it matters,
explicit limitations, real downloadable entry points, and demo data labelled
as demo data rather than presented as adoption.

## Featured tools

| Project | Use it when... | Start here |
|---|---|---|
| **[ColdShelf](https://github.com/CAOShurong/coldshelf)** | You need to find a file on an unplugged external drive without reconnecting every disk. It keeps a private catalog with search, snapshots, duplicate evidence, physical-location notes, and QR labels. | [v0.1.4 downloads](https://github.com/CAOShurong/coldshelf/releases/tag/v0.1.4) · [5-minute demo](https://github.com/CAOShurong/coldshelf#quick-start) · [feedback](https://github.com/CAOShurong/coldshelf/discussions/5) |
| **[ByteThere](https://github.com/CAOShurong/bytethere)** | You are about to wipe, move, or archive a drive and need a read-only preflight for OneDrive/iCloud placeholders, broken links, incompatible names, case or Unicode collisions, path limits, and allocation anomalies. It checks metadata; it does **not** prove backup completeness or file readability. | [v0.1.0 downloads](https://github.com/CAOShurong/bytethere/releases/tag/v0.1.0) · [field-test discussion](https://github.com/CAOShurong/bytethere/discussions/1) |
| **[OpaqueDrop](https://github.com/CAOShurong/opaquedrop)** | You want an accountless, self-hosted inbound file request where filenames and bytes are encrypted in the sender's browser to a recipient-held key. The server stores ciphertext, but hosted JavaScript remains in the server operator's trust boundary. | [v0.1.0 downloads](https://github.com/CAOShurong/opaquedrop/releases/tag/v0.1.0) · [threat model](https://github.com/CAOShurong/opaquedrop/blob/main/docs/THREAT_MODEL.md) · [feedback](https://github.com/CAOShurong/opaquedrop/discussions/1) |
| **[WheelWhy](https://github.com/CAOShurong/wheelwhy)** | A Python wheel is rejected and you need a human-readable explanation of which Python, ABI, platform, or `Requires-Python` rule missed. It explains compatibility; it is not a full pip or uv resolver. | [v0.1.0 downloads](https://github.com/CAOShurong/wheelwhy/releases/tag/v0.1.0) · [bring a real wheel error](https://github.com/CAOShurong/wheelwhy/discussions/6) |
| **[VulnFuse](https://github.com/CAOShurong/vulnfuse)** | Several security scanners report overlapping findings and you need explainable correlation, merge blockers, scanner-overlap evidence, run comparison, and one offline report. | [browser workbench](https://caoshurong.github.io/vulnfuse/) · [v0.4.2](https://github.com/CAOShurong/vulnfuse/releases/tag/v0.4.2) |
| **[TermScope](https://github.com/CAOShurong/termscope)** | You need live Arduino, ESP32, or STM32 telemetry in a terminal, including over pipes or SSH, with CSV record/replay and Teleplot stream support. | [`pipx run termscope --demo`](https://pypi.org/project/termscope/) · [v0.2.0](https://github.com/CAOShurong/termscope/releases/tag/v0.2.0) · [hardware reports wanted](https://github.com/CAOShurong/termscope/issues/2) |

## More focused tools

### Developer diagnostics and verifiable automation

- **[RunProof](https://github.com/CAOShurong/runproof)** runs coding-agent work
  in isolated worktrees and accepts it only when user-declared checks pass.
- **[WillItBreak](https://github.com/CAOShurong/willitbreak)** reports only
  dependency API breaks that reach your Python call sites.
- **[SlowImports](https://github.com/CAOShurong/slowimports)** measures Python
  startup cost and identifies imports that can safely become lazy.
- **[JSONXray](https://github.com/CAOShurong/jsonxray)** infers the real schema
  of JSONL/NDJSON streams and points back to outlier records.
- **[ContextCost](https://github.com/CAOShurong/contextcost)** measures what a
  repository costs an AI coding agent to read and verifies proposed reductions.
- **[AI Project Factory](https://github.com/CAOShurong/ai-project-factory)**
  keeps a model-neutral fact and handoff layer across Codex, Claude, and bare
  API workflows.

### Research and evaluation

- **[DidYouLearn](https://github.com/CAOShurong/didyoulearn)** evaluates whether
  an AI tutor produces unaided mastery, transfer, retention, and calibrated
  confidence—not merely a persuasive answer.
- **[FrontierTrials](https://github.com/CAOShurong/frontiertrials)** supports
  private blind comparisons of AI products on your own tasks.
- **[EvalInt](https://github.com/CAOShurong/evalint)** checks LLM evaluation
  sets for weak reliability, suspicious wrong-answer agreement, and
  near-duplicates.
- **[BenchLineage](https://github.com/CAOShurong/benchlineage)** connects
  experiment intent, instrument identity, raw data, uncertainty, analysis, and
  reports.
- **[ReproWeave](https://github.com/CAOShurong/reproweave)** maps paper claims
  to evidence, dependencies, available resources, and a reviewable replication
  plan.
- **[OhmJudge](https://github.com/CAOShurong/ohmjudge)** generates fresh
  electrical-engineering tasks and grades answers locally with executable
  rules.

## Hardware and offline transfer

The **[STM32F103 multifunction robot
car](https://github.com/CAOShurong/Multi-function-tracking-car-based-on-STM32)**
is a photographed and video-demonstrated build with Bluetooth control,
ultrasonic ranging, obstacle avoidance, four-sensor line tracking, servo
scanning, and OLED output. The repository includes the STM32CubeIDE project,
pin map, and two-byte control protocol.

The **[Decimen Optical Transfer field
fork](https://github.com/CAOShurong/decimen-optical-transfer)** adds an
installable terminal and SSH sender plus explicit mobile camera selection to
Evan Crawley's MIT-licensed screen-to-camera transfer project. It sends files,
binary stdin, or text through fountain-coded animated QR without a
receiver-side network path. [Try the receiver](https://caoshurong.github.io/decimen-optical-transfer/receive/)
or [download v0.4.0-field.1](https://github.com/CAOShurong/decimen-optical-transfer/releases/tag/v0.4.0-field.1).

## Open-source contributions

- **[Teleplot PR #52](https://github.com/nesnes/teleplot/pull/52)** makes the
  Enter key in Teleplot's VS Code serial sender honor the selected CR, LF, or
  CRLF ending, matching the Send button. It is awaiting maintainer review and
  is not presented as an upstream release.
- **[Awesome Software Supply Chain Security PR
  #95](https://github.com/bureado/awesome-software-supply-chain-security/pull/95)**,
  **[Awesome SBOM PR #66](https://github.com/awesomeSBOM/awesome-sbom/pull/66)**,
  and **[Awesome CLI Apps PR
  #356](https://github.com/toolleeo/awesome-cli-apps-in-a-csv/pull/356)** are
  transparent submissions for VulnFuse and TermScope, currently awaiting
  upstream review.

## What I try to make verifiable

- Hosted demonstrations use synthetic or fictional data when no real study has
  been run, and say so visibly.
- Security and research tools publish their threat models, assumptions, and
  failure boundaries instead of collapsing them into one confident claim.
- Releases, installation paths, checksums, and important failure modes are
  exercised through public artifacts, not inferred from source code alone.
- Stars, downloads, users, benchmarks, and testimonials are never fabricated.

Bug reports, real platform results, redacted failure cases, and focused pull
requests are welcome through each project's Issues or Discussions area.
