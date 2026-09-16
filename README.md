<a href="https://caoshurong.github.io/">
  <img src="https://raw.githubusercontent.com/CAOShurong/CAOShurong/57eee44075005963b73fe200ee93f847f836fc9a/assets/banner.svg" alt="ShurongCAO — PhD researcher in Electronic Engineering at CUHK. View my homepage." width="100%">
</a>

<p align="center">
  <a href="#selected-work">Selected work</a> ·
  <a href="#open-source-contributions">Open source</a> ·
  <a href="#research-background">Research background</a> ·
  <a href="mailto:shurongcao0819@gmail.com">Contact</a>
</p>

I am **ShurongCAO**, a PhD student in **Electronic Engineering at The Chinese University of Hong Kong**, with a B.Eng. from **Nanjing University**.

I build software for scientific and engineering work, from experiment provenance and AI evaluation to embedded systems. I also contribute to the tools underneath that work: numerical libraries, developer infrastructure, and software supply-chain tooling.

My interests connect **research questions with working systems**: how to make experiments reproducible, evaluate AI on meaningful tasks, and turn a difficult failure into a tested upstream fix.

## Selected work

| Project | What it does | Explore |
| :--- | :--- | :--- |
| **[BenchLineage](https://github.com/CAOShurong/benchlineage)** | Records experiment provenance, calibration, and uncertainty; exports reproducible evidence bundles and ELN exchange archives. | [Package](https://pypi.org/project/benchlineage/) · [Upstream ELN example](https://github.com/TheELNConsortium/TheELNFileFormat/tree/master/examples/BenchLineage) |
| **[OhmJudge](https://github.com/CAOShurong/ohmjudge)** | Generates electrical-engineering calculation tasks with executable local grading, for investigating AI reasoning. | [Methodology](https://github.com/CAOShurong/ohmjudge/blob/main/docs/METHODOLOGY.md) · [Try the collector](https://caoshurong.github.io/ohmjudge/demo/blind-collector.html) |
| **[FrontierTrials](https://github.com/CAOShurong/frontiertrials)** | Supports private, blind comparisons of AI products on your own tasks, directly in the browser. | [Try it](https://caoshurong.github.io/frontiertrials/try/) · [Example report](https://caoshurong.github.io/frontiertrials/demo/trial-report.html) |
| **[STM32 robot car](https://github.com/CAOShurong/Multi-function-tracking-car-based-on-STM32)** | Integrates line tracking, obstacle avoidance, ultrasonic ranging, Bluetooth control, and an OLED interface. | [Source & hardware](https://github.com/CAOShurong/Multi-function-tracking-car-based-on-STM32#readme) |

<details>
<summary>More tools</summary>

- **[ReproWeave](https://github.com/CAOShurong/reproweave)** — evidence maps and replication triage for research papers.
- **[TermScope](https://github.com/CAOShurong/termscope)** — live serial plotting over UART, pipes, and SSH.
- **[VulnFuse](https://github.com/CAOShurong/vulnfuse)** — explainable correlation across security scanner findings and software bills of materials.
- **[WillItBreak](https://github.com/CAOShurong/willitbreak)** — traces breaking dependency changes to the call sites they affect.

</details>

## Open-source contributions

I work across existing codebases to reproduce problems, trace their causes, and contribute scoped changes with tests and documentation. Selected contributions **merged by upstream projects**:

| Project | Accepted work |
| :--- | :--- |
| **Astropy** | [Preserve floating-point and complex precision in image block replication](https://github.com/astropy/astropy/pull/20364), avoiding unintended dtype promotion. |
| **GitHub MCP Server** | [Enable URL-based feature flags for headerless clients](https://github.com/github/github-mcp-server/pull/3146), preserving header precedence and OAuth resource queries. |
| **rclone** | [Add pattern-based transfer ordering](https://github.com/rclone/rclone/pull/9766); [retry S3 multipart responses with missing ETags](https://github.com/rclone/rclone/pull/9823). |
| **Syft** | [Detect ingress-nginx binaries across ARM64, ARMv7, and s390x](https://github.com/anchore/syft/pull/5179). |
| **The ELN Consortium** | [Contribute a reproducible BenchLineage exchange example](https://github.com/TheELNConsortium/TheELNFileFormat/pull/152), connecting experiment provenance with the ELN format. |

I continue to investigate issues and submit new pull requests. These live views track work in **external repositories**, with accepted contributions and ongoing proposals shown separately:

**[Merged contributions](https://github.com/search?q=author%3ACAOShurong+is%3Apr+is%3Amerged+-user%3ACAOShurong&type=pullrequests&s=updated&o=desc)** · **[Open pull requests](https://github.com/search?q=author%3ACAOShurong+is%3Apr+is%3Aopen+-user%3ACAOShurong&type=pullrequests&s=updated&o=desc)** · [Dated contribution archive](CONTRIBUTIONS.md)

## Research background

At CUHK, I am exploring semiconductor devices and integration, including BEOL-compatible processing, p-type oxides, and monolithic 3D integration. My earlier research includes wafer defect detection and industrial anomaly detection:

- **[FALCO-WAFER](https://doi.org/10.1109/ITC-Asia67627.2025.00016)** — lightweight wafer defect detection · IEEE ITC-Asia, 2025 · **Co-first author**.
- **[Texture-AD](https://arxiv.org/abs/2409.06367)** — an industrial anomaly-detection dataset and benchmark · arXiv, 2024 · **Co-author**.

My [academic homepage](https://caoshurong.github.io/) covers research directions, publications, and experience in more detail.

## Connect

I welcome **research collaborations, internships, and engineering projects**, especially around scientific software, AI evaluation, and research infrastructure. Based in **Hong Kong**; in-person collaboration in **Hong Kong or Shenzhen**, and remote collaboration with teams in **North America, Europe**, and elsewhere.

[Email](mailto:shurongcao0819@gmail.com) · [Academic homepage](https://caoshurong.github.io/) · [All repositories](https://github.com/CAOShurong?tab=repositories)
