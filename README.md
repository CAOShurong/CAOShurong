<a href="https://caoshurong.github.io/">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/CAOShurong/CAOShurong/63043b89f88a6c29f582cb81b0d5ef545e6673ff/assets/banner-dark.svg">
  <img src="https://raw.githubusercontent.com/CAOShurong/CAOShurong/63043b89f88a6c29f582cb81b0d5ef545e6673ff/assets/banner.svg" alt="ShurongCAO — Research, software, open source. PhD student in Electronic Engineering at CUHK." width="100%">
</picture>
</a>

[Homepage](https://caoshurong.github.io/) &nbsp; / &nbsp; [Contributions](#open-source-contributions) &nbsp; / &nbsp; [Projects](#selected-work) &nbsp; / &nbsp; [Email](mailto:shurongcao0819@gmail.com)

I am **ShurongCAO**, a PhD student in Electronic Engineering at **The Chinese University of Hong Kong**, previously at **Nanjing University**. I build research software and embedded systems, and contribute to the open-source infrastructure behind scientific and engineering work.

## Open-source contributions

<!-- upstream-stats:start -->

**42 merged pull requests · 24 upstream repositories**<br>
<sub>External repositories only · Updated 16 September 2026</sub>

<!-- upstream-stats:end -->

Selected problems I have worked on, with changes **accepted upstream**.

**Astropy · Keeping scientific arrays at the intended precision**<br>
Fixed unexpected dtype promotion in image block replication, preserving floating-point and complex precision and avoiding the associated memory increase. [Merged PR #20364](https://github.com/astropy/astropy/pull/20364)

**GitHub MCP Server · Making feature controls work across clients**<br>
Added URL-based feature flags for clients that cannot set headers, while preserving header precedence and OAuth resource queries. [Merged PR #3146](https://github.com/github/github-mcp-server/pull/3146)

**rclone · Controlling transfer order and recovering failed uploads**<br>
Added pattern-based transfer ordering and fixed a crash when S3 multipart responses omit an ETag, allowing the affected part to retry. [#9766](https://github.com/rclone/rclone/pull/9766) · [#9823](https://github.com/rclone/rclone/pull/9823)

**Syft · Recognizing software across CPU architectures**<br>
Extended ingress-nginx binary detection to ARM64, ARMv7, and s390x, verified against the published binaries. [Merged PR #5179](https://github.com/anchore/syft/pull/5179)

I am actively investigating issues and submitting new work. **[Merged contributions](https://github.com/search?q=author%3ACAOShurong+is%3Apr+is%3Amerged+-user%3ACAOShurong&type=pullrequests&s=updated&o=desc)** and **[open pull requests](https://github.com/search?q=author%3ACAOShurong+is%3Apr+is%3Aopen+-user%3ACAOShurong&type=pullrequests&s=updated&o=desc)** link to the current record in external repositories.

## Selected work

<table>
<tr>
<td width="50%" valign="top">
<sub>EXPERIMENT PROVENANCE</sub>
<h3><a href="https://github.com/CAOShurong/benchlineage">BenchLineage</a></h3>
<p>Keep the path from instrument and calibration to raw measurement, uncertainty, and published result inspectable.</p>
<p>A contributed exchange example is included in <a href="https://github.com/TheELNConsortium/TheELNFileFormat/tree/master/examples/BenchLineage">The ELN Consortium's format repository</a>.</p>
<p><a href="https://pypi.org/project/benchlineage/">Package</a> · <a href="https://caoshurong.github.io/benchlineage/">Demo</a></p>
</td>
<td width="50%" valign="top">
<sub>AI REASONING IN ENGINEERING</sub>
<h3><a href="https://github.com/CAOShurong/ohmjudge">OhmJudge</a></h3>
<p>Evaluate AI on fresh electrical-engineering calculations, with seeded task generation and executable local grading.</p>
<p>Explicit checks for numerical answers, units, and tolerances. An early research tool.</p>
<p><a href="https://github.com/CAOShurong/ohmjudge/blob/main/docs/METHODOLOGY.md">Methodology</a> · <a href="https://caoshurong.github.io/ohmjudge/demo/blind-collector.html">Try it</a></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<sub>HUMAN EVALUATION OF AI</sub>
<h3><a href="https://github.com/CAOShurong/frontiertrials">FrontierTrials</a></h3>
<p>Compare AI products on your own tasks through blind comparisons, saved protocols, and inspectable reports.</p>
<p>A private browser lab, with a separate CLI workflow for structured studies.</p>
<p><a href="https://caoshurong.github.io/frontiertrials/try/">Try the lab</a> · <a href="https://caoshurong.github.io/frontiertrials/demo/trial-report.html">Example report</a></p>
</td>
<td width="50%" valign="top">
<sub>EMBEDDED SYSTEMS</sub>
<h3><a href="https://github.com/CAOShurong/Multi-function-tracking-car-based-on-STM32">STM32 robot car</a></h3>
<p>Bring sensing, control, and a physical interface together: line tracking, obstacle avoidance, ultrasonic ranging, Bluetooth, and OLED.</p>
<p>Hardware integration alongside the research software.</p>
<p><a href="https://github.com/CAOShurong/Multi-function-tracking-car-based-on-STM32#readme">Source &amp; hardware</a></p>
</td>
</tr>
</table>

More: [TermScope](https://github.com/CAOShurong/termscope) · [ReproWeave](https://github.com/CAOShurong/reproweave) · [VulnFuse](https://github.com/CAOShurong/vulnfuse) · [All repositories](https://github.com/CAOShurong?tab=repositories)

## Research background

At CUHK, I am exploring semiconductor devices and integration. Earlier work includes **[FALCO-WAFER](https://caoshurong.github.io/publications/#falco-wafer)** (IEEE ITC-Asia 2025, co-first author) and **[Texture-AD](https://arxiv.org/abs/2409.06367)** (industrial anomaly detection, co-author).

[My academic website](https://caoshurong.github.io/) covers EE research directions, publications, and experience.

---

Open to **research collaborations, internships, and engineering projects**. Based in Hong Kong; in-person in **Hong Kong or Shenzhen**, remote with teams in **North America, Europe**, and elsewhere. [Get in touch](mailto:shurongcao0819@gmail.com).
