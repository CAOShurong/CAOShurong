# CAOShurong

Electrical Engineering PhD researcher at CUHK. I maintain public tools for
reproducible engineering, Python packaging diagnostics, local-first data work,
and explainable security evidence.

I try to make each claim inspectable: public releases, runnable entry points,
documented limits, and direct links to upstream work. A download counter or a
self-submitted project listing is not presented as independent adoption.

## Maintained projects

| Project | What it does | Verifiable entry points |
|---|---|---|
| **[BenchLineage](https://github.com/CAOShurong/benchlineage)** | Records experiment provenance, calibration, uncertainty and evidence, with portable ELN import/export. | [PyPI](https://pypi.org/project/benchlineage/) · [v0.3.4](https://github.com/CAOShurong/benchlineage/releases/tag/v0.3.4) · [five accepted ELN contributions](https://github.com/TheELNConsortium/TheELNFileFormat/pulls?q=is%3Apr+author%3ACAOShurong+is%3Amerged) |
| **[WheelWhy](https://github.com/CAOShurong/wheelwhy)** | Explains why a Python wheel matches or misses a declared interpreter and platform; it is not a full pip or uv resolver. | [v0.3.1](https://github.com/CAOShurong/wheelwhy/releases/tag/v0.3.1) · [external feedback and fix](https://github.com/CAOShurong/wheelwhy/issues/14) · [upstream follow-up](https://github.com/pypa/pip/issues/10793#issuecomment-5262361213) |
| **[ColdShelf](https://github.com/CAOShurong/coldshelf)** | Builds a private searchable catalog of unplugged drives, including snapshots, duplicate evidence and physical-location notes. | [latest release](https://github.com/CAOShurong/coldshelf/releases/latest) · [quick start](https://github.com/CAOShurong/coldshelf#quick-start) · [limitations](https://github.com/CAOShurong/coldshelf#scope-and-limitations) |
| **[VulnFuse](https://github.com/CAOShurong/vulnfuse)** | Correlates findings from SARIF, Trivy, Grype, Snyk, CycloneDX, OSV and CSV without hiding merge blockers or scanner disagreement. | [browser workbench](https://caoshurong.github.io/vulnfuse/) · [v0.4.24](https://github.com/CAOShurong/vulnfuse/releases/tag/v0.4.24) · [security model](https://github.com/CAOShurong/vulnfuse/blob/main/SECURITY.md) |
| **[TermScope](https://github.com/CAOShurong/termscope)** | Plots Arduino, ESP32 and STM32 telemetry in a terminal over serial, pipes or SSH, with CSV record/replay. | [PyPI](https://pypi.org/project/termscope/) · [v0.4.1](https://github.com/CAOShurong/termscope/releases/tag/v0.4.1) · [hardware reports wanted](https://github.com/CAOShurong/termscope/issues/2) |

[See all repositories](https://github.com/CAOShurong?tab=repositories) and
[published Python packages](https://pypi.org/user/CAOShurong/). The projects
above are the small set I currently use to represent my maintenance work.

Recent owned-project maintenance includes [VulnFuse PR #73](https://github.com/CAOShurong/vulnfuse/pull/73),
which closed issue #72 in v0.4.24 by preserving Trivy SARIF image identity for
OpenVEX correlation, and [TermScope PR #8](https://github.com/CAOShurong/termscope/pull/8),
which closed issues #6 and #7 in v0.4.1 by tightening labelled-telemetry token
boundaries. [JSONXray PR #7](https://github.com/CAOShurong/jsonxray/pull/7)
closed issues #5 and #6 in [v0.2.1](https://github.com/CAOShurong/jsonxray/releases/tag/v0.2.1)
by rejecting malformed streamed arrays. [BenchLineage PR #18](https://github.com/CAOShurong/benchlineage/pull/18)
closed issues #14-#17 in [v0.3.4](https://github.com/CAOShurong/benchlineage/releases/tag/v0.3.4)
by hardening Windows and Unicode interoperability, while [SlowImports PR #6](https://github.com/CAOShurong/slowimports/pull/6)
closed issues #4 and #5 in [v0.2.1](https://github.com/CAOShurong/slowimports/releases/tag/v0.2.1)
by preserving target failures and Unicode streams. These owner-authored and
owner-merged releases demonstrate active maintenance; they are not external
contributions or independent adoption.

## Upstream contributions

- **Merged:** [TheELNFileFormat PR #152](https://github.com/TheELNConsortium/TheELNFileFormat/pull/152)
  adds a reproducible BenchLineage-generated `.eln` fixture and mapping. It
  passed the upstream schema and validator checks and was approved and merged.
- **Merged:** [TheELNFileFormat PR #153](https://github.com/TheELNConsortium/TheELNFileFormat/pull/153)
  clarifies `@type`, `additionalType` and `genre` in the public specification.
  It was approved and merged, closing issue #105.
- **Merged:** [TheELNFileFormat PR #154](https://github.com/TheELNConsortium/TheELNFileFormat/pull/154)
  makes parameter checks handle array-valued `Dataset` and `File` types, with
  regression cases for both invalid and valid nodes. It was approved and merged.
- **Merged:** [TheELNFileFormat PR #155](https://github.com/TheELNConsortium/TheELNFileFormat/pull/155)
  clarifies how child `Dataset` relationships are represented in the public
  specification. It was approved and merged, closing issue #116.
- **Merged:** [TheELNFileFormat PR #156](https://github.com/TheELNConsortium/TheELNFileFormat/pull/156)
  validates the specification's single-root-folder archive requirement. It
  passed the upstream check and was approved and merged; related issue #67
  remains open.
- **Merged:** [CycloneDX Python PR #1028](https://github.com/CycloneDX/cyclonedx-python-lib/pull/1028)
  encodes local XML-schema paths as file URIs and adds a regression test for
  package paths containing `#`. All 47 public checks passed; a project member
  merged it, closed issue #551 and released it in v11.11.2.
- **Open:** [cibuildwheel PR #2966](https://github.com/pypa/cibuildwheel/pull/2966)
  removes an unconditional NuGet fallback source and adds regression coverage
  so configured package sources remain authoritative.
- **Merged:** [SampleDB PR #91](https://github.com/sciapp/sampledb/pull/91)
  fixes valid ELN imports that contain explicit ZIP directory entries while
  preserving rejection of genuine multi-root archives. It was merged into the
  upstream default branch; GitHub reported no reviews or checks for the PR.
- **Merged:** [SampleDB PR #92](https://github.com/sciapp/sampledb/pull/92)
  preserves flexible ELN metadata named `parts` while assigning collision-free
  keys to generated nested-Dataset relationships. It was merged into the
  upstream default branch; GitHub again reported no reviews or checks.

The five accepted TheELNFileFormat contributions make me a **repeat external
contributor** there. SampleDB #91 and #92 make me a repeat external contributor
to that separate project; CycloneDX Python #1028 is one accepted contribution.
They do **not** make me a module owner or core maintainer; cibuildwheel #2966
remains an unaccepted proposal. Self-submissions that list my own tools in
curated lists are excluded from this section because they are promotion, not
independent maintenance or adoption.

## Maintenance boundaries

- I am the **primary maintainer** of the owned repositories featured above.
- I describe external work as merged or open contributions unless a project
  publicly grants broader responsibility.
- Synthetic/demo data is labelled as such; it is not presented as a user study
  or production deployment.
- Security and research tools publish assumptions and failure boundaries.
- Stars, downloads, users, benchmarks and testimonials are never fabricated.

Focused bug reports, real platform results and reviewable pull requests are
welcome through each project's public Issues or Discussions.
