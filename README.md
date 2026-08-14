# CAOShurong

Electrical Engineering PhD researcher at CUHK. I maintain public tools for
reproducible engineering, Python packaging diagnostics, local-first data work,
and explainable security evidence.

I try to make each claim inspectable: public releases, runnable entry points,
documented limits, and direct links to upstream work. A download counter or a
self-submitted project listing is not presented as independent adoption.

## Maintained projects

| Project | What it does | Verifiable entry points |
| --- | --- | --- |
| **[BenchLineage](https://github.com/CAOShurong/benchlineage)** | Records experiment provenance, calibration, uncertainty and evidence, with portable ELN import/export. | [PyPI](https://pypi.org/project/benchlineage/) · [v0.3.5](https://github.com/CAOShurong/benchlineage/releases/tag/v0.3.5) · [five accepted ELN contributions](https://github.com/TheELNConsortium/TheELNFileFormat/pulls?q=is%3Apr+author%3ACAOShurong+is%3Amerged) |
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
by rejecting malformed streamed arrays. [BenchLineage PR #20](https://github.com/CAOShurong/benchlineage/pull/20)
closed issue #19 in [v0.3.5](https://github.com/CAOShurong/benchlineage/releases/tag/v0.3.5)
by adding explicit ELN data-license metadata, while [SlowImports PR #6](https://github.com/CAOShurong/slowimports/pull/6)
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
- **Review:** [CycloneDX Python PR #1016](https://github.com/CycloneDX/cyclonedx-python-lib/pull/1016)
  initially lost a strict-valid CycloneDX 1.7 relationship during model round
  trips. I reproduced the defect and requested bounded coverage; the external
  author implemented it. I reran 770 related and 6,994 full tests on exact head
  `ea7d2ca`, then approved that revision. The PR remains open and unaccepted.
- **Review:** [CycloneDX Python PR #1015](https://github.com/CycloneDX/cyclonedx-python-lib/pull/1015#pullrequestreview-4934063243)
  adds CycloneDX 1.7 standardized algorithm-family and elliptic-curve
  identifiers. I ran 344 focused and 7,305 full tests, flake8, mypy, package
  builds, and a clean-wheel JSON/XML validation and downgrade round trip, then
  approved exact head `fd0ec256`. The PR remains open and unaccepted; this is
  review evidence rather than merge authority or maintainership.
- **Review:** [CycloneDX Python PR #1007](https://github.com/CycloneDX/cyclonedx-python-lib/pull/1007#pullrequestreview-4934164425)
  removes quadratic dependency registration from `Bom.validate()`. I ran all
  6,961 tests, exercised the complexity guard across 20 hash seeds, compared
  base/candidate equality counts, and generated strict-valid 1.6 JSON at
  1,000, 2,000 and 4,000 components while preserving exact component and
  dependency reference sets. I approved exact head `caa74d7`; the PR remains
  open, and this is tested review evidence rather than assigned review duty,
  merge authority or maintainership.
- **Review:** [python-docx-template PR #661](https://github.com/elapouya/python-docx-template/pull/661)
  makes the intended license and test contents of source distributions explicit.
  I compared the published 0.20.2 source distribution with the exact PR head,
  rebuilt both package formats, ran 36 installed-wheel test scripts and the CLI
  path, and approved the third-party change. The PR remains open and unaccepted.
- **Review:** [python-docx-template PR #642](https://github.com/elapouya/python-docx-template/pull/642#pullrequestreview-4927259884)
  adds CLI template-syntax validation and JSON reports. On exact head `c1259ab`,
  I verified source and installed-wheel behavior, all 36 non-runner scripts,
  flake8 and package builds, then requested changes because two rejected
  validation invocations printed errors but returned success exit code 0. This
  is actionable review evidence, not approval, acceptance or maintainer authority.
- **Review:** [python-docx-template PR #648](https://github.com/elapouya/python-docx-template/pull/648#pullrequestreview-4927626895)
  preserves optional `Subdoc` imports while sorting package imports. I ran all
  37 test scripts, flake8, package builds and clean-wheel environments both
  with and without `docxcompose`; normal and subdocument outputs rendered and
  reopened successfully. I approved exact head `f583ed34`; all 14 upstream
  checks pass. The PR remains open, so this is review evidence rather than
  acceptance or maintainer authority.
- **Review:** [Argo CD PR #29175](https://github.com/argoproj/argo-cd/pull/29175#pullrequestreview-4928056635)
  proposed boolean parsing that diverged from bundled Dex v2.45.1. I reproduced
  three boundary failures and verified a `strconv.ParseBool` candidate with
  focused and full `util/dex` tests plus `go vet`, then requested compatible
  parsing and tests. This is actionable review evidence, not delegated Argo CD
  responsibility or acceptance.
- **Review:** [pandas PR #66623](https://github.com/pandas-dev/pandas/pull/66623#pullrequestreview-4928066161)
  improved Arrow-string memory accounting in a clean installed wheel, but two
  exact MultiIndex memory tests failed, the public doctest expectation was
  stale, and the branch conflicted with `main`. I submitted a tested
  `CHANGES_REQUESTED` review on exact head `ece0d447`. The PR remains open and
  this does not establish pandas maintainer authority.
- **Open maintainer-path work:** [python-docx-template PR #662](https://github.com/elapouya/python-docx-template/pull/662)
  fixes escaped Jinja delimiters split across Word runs for issue #548, including
  the original attached document and Python 3.9/3.13 regression runs. I also
  [triaged issue #627](https://github.com/elapouya/python-docx-template/issues/627#issuecomment-5280267748)
  with a two-page reproduction and an exact artifact request. The project owner
  [publicly asks maintainer candidates to contribute first](https://github.com/elapouya/python-docx-template/issues/631);
  these actions follow that path but do not grant me maintainer authority.
- **Merged:** [Keycloak PR #51697](https://github.com/keycloak/keycloak/pull/51697)
  reports OID4VCI credential-request errors consistently and adds regression
  coverage for missing claims metadata and invalid proof timing. It fixed
  help-wanted issue #51692, received maintainer approval, passed the upstream
  check matrix and was merged into the default branch.
- **Review:** [CycloneDX specification PR #1019](https://github.com/CycloneDX/specification/pull/1019)
  implements the schema defect I reported in issue #1018. I independently ran
  the Java, Node and Buf gates on its exact head, approved it, and closed my
  later duplicate #1020 to reduce maintainer work. The third-party PR remains
  open and unaccepted.
- **Merged:** [eLabFTW PR #7267](https://github.com/elabftw/elabftw/pull/7267)
  adds the licensed BenchLineage v0.3.5 demo as a cross-producer ELN import
  fixture after a maintainer welcomed the proposal in issue #7263. A real
  PHP/MySQL import selected an experiment and preserved all 20 linked uploads.
  Maintainer `NicolasCARPi` approved exact head `baeb6e37`; all ten checks passed,
  and merge `77b941e1` placed the byte-identical release asset on default `master`.
  This is accepted external integration work, not independent user adoption or
  eLabFTW maintainer authority.
- **Open:** [cibuildwheel PR #2966](https://github.com/pypa/cibuildwheel/pull/2966)
  removes an unconditional NuGet fallback source and adds regression coverage
  so configured package sources remain authoritative.
- **Merged after maintainer feedback:**
  [tox PR #4022](https://github.com/tox-dev/tox/pull/4022)
  provisions the requested tox version before reading version-specific
  configuration. I added exact `tox l` and `tox c` behavior coverage requested
  in review. Maintainer `gaborbernat` approved exact head `21de6da9`; all 30
  checks passed, merge `c3f8d227` entered default `main`, and issue #4021 closed.
- **Open:** [BuildKit PR #7038](https://github.com/moby/buildkit/pull/7038)
  makes `history.maxEntries=0` explicitly disable build-history persistence.
  The focused integration test passed across nine worker variants and the
  approved fork workflow matrix is green; no maintainer has accepted it yet.
- **Open:** [Airflow PR #71535](https://github.com/apache/airflow/pull/71535)
  refreshes a stale local bare Git origin when a requested bundle tracking ref
  cannot be resolved. Focused, module, type, packaging and real promotion paths
  passed locally; the large upstream matrix is still running, so this is not
  reported as accepted or fully green.
- **Open:** [Astropy PR #20234](https://github.com/astropy/astropy/pull/20234)
  rejects FITS tables with more than 999 physical columns before writing a
  partial file and adds the 999/1000 boundary regression. Astropy member
  `pllim` requested a plain-text changelog entry; I pushed the tested one-line
  change and resolved the sole review thread. The review was not an approval,
  and the PR remains unaccepted.
- **Open:** [Kustomize PR #6224](https://github.com/kubernetes-sigs/kustomize/pull/6224)
  adds legacy release-download support for pre-module tags and assets. A project
  member issued `/ok-to-test`, and all 23 executable source, platform and
  deployment checks pass. The official EasyCLA rerun still reports missing
  authorization, so this remains a blocked proposal rather than accepted work.
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
to that separate project; CycloneDX Python #1028, Keycloak #51697, eLabFTW
PR #7267 and tox #4022 are one accepted contribution each. They do **not** make
me a module
owner or core
maintainer. CycloneDX Python #1007/#1015/#1016 and specification #1019 are review
contributions; python-docx-template #661, #642 and #648, Argo CD #29175 and
pandas #66623 are independently tested reviews, while python-docx-template #662
and cibuildwheel #2966 remain
unaccepted proposals. The python-docx-template work follows a public
candidate route but is not a maintainer appointment. The eLabFTW fixture is cross-producer
integration evidence, not independent adoption.
Self-submissions
that list my own tools in
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
