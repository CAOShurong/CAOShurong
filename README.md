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
| **[ResearchBench](https://github.com/CAOShurong/researchbench)** | A research-capability evaluation framework prototype for AI academic and research abilities: paper comprehension, idea generation, literature synthesis, experimental design, peer review, code reproduction, and open question identification. Currently uses placeholder keyword scoring; expert-validated datasets and evidence-based evaluation are planned. | [v0.1.0](https://github.com/CAOShurong/researchbench/releases/tag/v0.1.0) · [design document](https://github.com/CAOShurong/researchbench/blob/master/RESEARCH_BENCHMARK.md) · [7 task categories](https://github.com/CAOShurong/researchbench#task-categories) |
| **[BenchLineage](https://github.com/CAOShurong/benchlineage)** | Records experiment provenance, calibration, uncertainty and evidence, with portable ELN import/export. | [PyPI](https://pypi.org/project/benchlineage/) · [v0.3.7](https://github.com/CAOShurong/benchlineage/releases/tag/v0.3.7) · [five accepted ELN contributions](https://github.com/TheELNConsortium/TheELNFileFormat/pulls?q=is%3Apr+author%3ACAOShurong+is%3Amerged) |
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

A 2026-08-15 public snapshot recorded 692 rolling-month non-mirror PyPI events
for BenchLineage. These are download events, including automation, not unique
users. A byte-identical v0.3.5 fixture is exercised by eLabFTW's default-branch
importer tests, and TheELN also keeps a BenchLineage fixture in its test matrix.
Both integrations were proposed and authored by me, so they are durable
cross-project compatibility contracts rather than independent adoption.

## Account-wide governance and current boundaries

The account-wide [`CAOShurong/.github`](https://github.com/CAOShurong/.github)
defaults now include a public [CODE_OF_CONDUCT.md](https://github.com/CAOShurong/.github/blob/main/CODE_OF_CONDUCT.md)
and [SECURITY.md](https://github.com/CAOShurong/.github/blob/main/SECURITY.md),
after [PR #2](https://github.com/CAOShurong/.github/pull/2) merged at
`e3621e3294926080a1e7ef3700cf9797246dfd21`. In the 2026-08-15 health
snapshot, 20 of 23 owned non-fork repositories scored 100%; the other three
lacked a detected license. This is owner governance only, not external
maintainer authority or independent adoption.

The current public inventory is 57 repositories: 24 non-fork repositories and
33 contribution or legacy forks. The `manual-approval` and `gitui` forks are
work carriers for upstream contributions, not owned projects or adoption.

At the same snapshot, 20 authored pull requests remained open alongside 17
accepted external contributions. [manual-approval #234](https://github.com/trstringer/manual-approval/pull/234)
is open, non-draft and mergeable at head `6bd8130`; its three upstream
`github-actions` suites are `action_required` with zero jobs. A separate
[fork CI run](https://github.com/CAOShurong/manual-approval/actions/runs/31874648952)
passed on that exact head, but that is not upstream CI acceptance or
maintainer evidence. [TheELN issue #67](https://github.com/TheELNConsortium/TheELNFileFormat/issues/67)
contains a bounded offer to help, not delegated responsibility. [tox #4020](https://github.com/tox-dev/tox/pull/4020)
is covered by a policy that does not expose transient agent comments, so their
absence is not treated as review or acceptance. [CycloneDX Rust Cargo #875](https://github.com/CycloneDX/cyclonedx-rust-cargo/pull/875)
remains a no-action maintainer-scope reference, not applicant acceptance or
authority.

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
- **Merged:** [TheELNFileFormat PR #157](https://github.com/TheELNConsortium/TheELNFileFormat/pull/157)
  adds a web `.eln` checker that reuses the test suite checks. Maintainer
  `SteffenBrinckmann` reviewed six requested changes; I implemented all of
  them (a unified `runChecks` entry point, path/upload support, Streamlit
  alignment, ordered results, tests, and the consortium logo), and he merged
  it as `401e7aa5`. This makes me a six-time accepted TheELN contributor.
- **Merged:** [Anchore Syft PR #5179](https://github.com/anchore/syft/pull/5179)
  adds detection for the multi-arch ingress-nginx v1.9.6 binaries across amd64,
  arm64, arm/v7 and s390x, each producing exactly one 1.9.6 package in real CLI
  scans. Maintainer `wagoodman` approved and merged it as `5c6cf08a`. This is
  a first contribution to Anchore Syft; it is not Syft maintainership, assigned
  review duty or independent adoption.
- **Merged:** [Plotly.js PR #7959](https://github.com/plotly/plotly.js/pull/7959)
  fixes numeric `bundlecolors` sorting for parallel-categories paths (issue
  #7952). Reviewer `camdecoster` requested NaN handling, I implemented it with
  the JSDoc and a Jasmine regression test, and he dismissed his earlier
  comment, approved and merged it as `95bfea16`. This is a first contribution
  to Plotly.js; it is not maintainership, assigned review duty or adoption.
- **Merged:** [eLabFTW PR #7306](https://github.com/elabftw/elabftw/pull/7306)
  trims whitespace from CSV column names so headers like ` title ` are matched
  to the expected `title` column instead of failing with a misleading error.
  Maintainer `NicolasCARPi` approved and merged it. It applies to both the
  main CSV importer and the compounds importer, and addresses issue #7024.
- **Merged:** [eLabFTW PR #7319](https://github.com/elabftw/elabftw/pull/7319)
  fixes the show-mode page-width regression reported in issue #7302: the
  dashboard quick links carry `mode=show`, which re-applied the
  `max-width-70` width cap for users preferring the tabular display,
  while the same filter built from the search page rendered full width.
  I traced it to the `enableWide` condition (PR #7041 gated only the
  no-mode branch), fixed the one-line condition, and maintainer
  `NicolasCARPi` merged it as `197e71d1`, closing issue #7302. This is the
  third accepted eLabFTW contribution after #7267 and #7306.
- **Merged:** [eLabFTW PR #7307](https://github.com/elabftw/elabftw/pull/7307)
  makes `prune:entries` remove orphaned `tags2entity` rows together with the
  soft-deleted entity rows in one transaction, addressing issue #6952.
  Maintainer `NicolasCARPi` requested changes (race condition, scalability,
  missing regression test), I addressed all three, and he approved and merged
  it as `8db29efc`. This is the fourth accepted eLabFTW contribution
  (#7267, #7306, #7319, #7307) and the first there to complete a full
  maintainer changes-requested cycle.
- **Merged:** [CycloneDX Python PR #1028](https://github.com/CycloneDX/cyclonedx-python-lib/pull/1028)
  encodes local XML-schema paths as file URIs and adds a regression test for
  package paths containing `#`. All 47 public checks passed; a project member
  merged it, closed issue #551 and released it in v11.11.2.
- **Merged:** [CycloneDX JavaScript PR #1507](https://github.com/CycloneDX/cyclonedx-javascript-library/pull/1507)
  maps string-valued `package.json` engine constraints to the official npm
  CycloneDX taxonomy and ignores malformed non-string values. Maintainer
  `jkowalleck` requested that the engine handling move inside `ComponentBuilder`
  and that malformed `engines` values be covered for the array, `null` and
  string cases. I implemented both and reran 8 focused and 4,155 full tests,
  lint, eslint, knip, Node/web/declaration builds and a real installed-dist
  probe. The reviewer then dismissed the change request, approved twice and
  merged it as `2a816627`, releasing v10.2.0. This is a first contribution to
  CycloneDX JavaScript; it is not CycloneDX team membership, maintainership,
  assigned review duty or independent adoption.
- **Review:** [manual-approval PR #206 review #4943438856](https://github.com/trstringer/manual-approval/pull/206#pullrequestreview-4943438856)
  is a public `CHANGES_REQUESTED` review against exact third-party head
  `dbfab57bc8890bfe5e645adc12423271ce28e0ae`. At that head, I reproduced the
  same five compile blockers with `go test -mod=mod -count=1 ./...`, `go vet
  -mod=mod ./...`, `go build -mod=mod ./...` and `golangci-lint v2.11.4`; the
  corresponding base commands passed. Upstream CI run
  [28285105918](https://github.com/trstringer/manual-approval/actions/runs/28285105918)
  failed its Build job while Test/Lint were skipped. The PR remains open, so
  this is reproducible review evidence, not acceptance, delegated duty,
  maintainer authority or independent adoption.
- **Open, first contribution:** [GitUI PR #3016](https://github.com/gitui-org/gitui/pull/3016)
  addresses open/help-wanted Windows issue [#1936](https://github.com/gitui-org/gitui/issues/1936)
  at exact head `5d28b4488f014565756720819309bf501fde61e1`. With Windows
  `core.autocrlf=true`, the original `cargo fmt -- --check --config
  newline_style=Unix` produced exit 1 and 162 incorrect-newline findings; the
  one-line `rustfmt.toml` change to `Auto` made `cargo fmt -- --check` and
  `git diff --check` pass, and the workspace nextest run passed 313/313 with
  `--no-default-features`. Upstream [CI run 31876657508](https://github.com/gitui-org/gitui/actions/runs/31876657508)
  is `action_required` with zero jobs, not a pass or failure, and the PR has
  no review or comment. GitUI's [co-maintainer route in issue #2084](https://github.com/gitui-org/gitui/issues/2084)
  requires later contribution and review milestones; this open first
  contribution is not accepted code, reviewer status or co-maintainer status.
- **Review:** [GitUI PR #3015 review #4943518940](https://github.com/gitui-org/gitui/pull/3015#pullrequestreview-4943518940)
  is a public `COMMENTED` review against exact head
  `5c3d858a3525c52ef296a032b8a7e5e9eccb3863`. I reran `cargo fmt -- --check`
  and `git diff --check`, focused asyncgit stash nextest (14 passed, 159
  skipped), and the full asyncgit nextest suite (173 passed). A separate
  pygit2 reproduction showed the baseline stored subdirectory becomes
  unreopenable after libgit2 removes it while resolving to the worktree root
  keeps the stash reopenable. Upstream [CI run 31874657724](https://github.com/gitui-org/gitui/actions/runs/31874657724)
  is `action_required` with zero jobs; workspace clippy remains unverified
  because the environment lacked `perl` and baseline `filetreelist` lint
  denials remained. The PR's disclosed Log-tab/gix panic is recorded as a
  follow-up, so this is review evidence, not acceptance, assigned reviewer
  duty, maintainer authority, co-maintainer status or independent adoption.
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
- **Review:** [CycloneDX Python PR #980](https://github.com/CycloneDX/cyclonedx-python-lib/pull/980#pullrequestreview-4943269289)
  adds `Service.trustZone` for CycloneDX 1.5 and later while preserving the 1.4
  boundary. On exact head `25c9a4c4`, I ran 756 focused and 6,962 full tests,
  flake8, mypy, package builds and a clean-wheel probe, then verified strict
  JSON/XML validation and root/nested round trips for 1.5-1.7 plus omission and
  rejection in 1.4. I approved the head, but the PR remains open and retains a
  maintainer changes-request; this review does not override it or grant duty.
- **Review:** [CycloneDX Python PR #1007](https://github.com/CycloneDX/cyclonedx-python-lib/pull/1007#pullrequestreview-4934164425)
  removes quadratic dependency registration from `Bom.validate()`. I ran all
  6,961 tests, exercised the complexity guard across 20 hash seeds, compared
  base/candidate equality counts, and generated strict-valid 1.6 JSON at
  1,000, 2,000 and 4,000 components while preserving exact component and
  dependency reference sets. I approved exact head `caa74d7`; the PR remains
  open, and this is tested review evidence rather than assigned review duty,
  merge authority or maintainership.
- **Review:** [CycloneDX Python PR #940](https://github.com/CycloneDX/cyclonedx-python-lib/pull/940#pullrequestreview-4934245554)
  adds bounded, structured JSON/XML validation errors. On exact head
  `ac93dbca`, I ran 1,620 focused and 6,959 full tests and scanned all 359
  repository JSON fixtures. The scan reproduced a misleading nested-error
  selection in 10 of 21 contextual errors, including the repository's mixed
  declared/concluded-license fixture. I requested a tie-aware selection and a
  regression. The PR remains open and conflicting; this is tested review
  evidence, not accepted code, assigned duty, merge authority or maintainership.
- **Review:** [CycloneDX Python PR #935](https://github.com/CycloneDX/cyclonedx-python-lib/pull/935#pullrequestreview-4935189815)
  introduces a side-effect-free `ModelValidator`, but removed the existing
  public `Bom.validate()` call despite the linked maintainer direction to
  deprecate it. Against current `main`, the call returned `True`; exact head
  `00df85b` raised `AttributeError`. I ran 744 focused and all 6,965 tests,
  flake8, mypy, package builds and clean-wheel behavior probes, then requested
  a deprecated compatibility wrapper plus a legacy-caller regression. The PR
  remains open; this is tested review evidence, not acceptance, assigned duty,
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
- **Review:** [python-docx-template PR #650](https://github.com/elapouya/python-docx-template/pull/650#pullrequestreview-4943236325)
  adds hyperlink support across templated Word runs. On exact head `b98ff321`,
  I ran all 38 direct test scripts, flake8, package builds, clean-wheel tests,
  undeclared-variable and complex-URL cases, then verified both the visible
  rendered text and the serialized relationship target before approving it.
  The PR remains open, so this is review evidence rather than acceptance,
  delegated duty, maintainer authority or independent adoption.
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
- **Review:** [rclone PR #9768](https://github.com/rclone/rclone/pull/9768#pullrequestreview-4943139972)
  changes OneDrive upload-session handling after a 404. I traced the source
  history and current protocol guidance, reproduced one same-session PUT across
  ten retry-enabled runs, and ran the full `backend/onedrive` suite. I requested
  a permanent no-same-session-retry regression plus an explicit whole-operation
  retry decision on exact head `673f7daa`. The PR remains open; this is tested
  review evidence, not rclone authority or acceptance.
- **Review:** [CycloneDX JavaScript PR #1411](https://github.com/CycloneDX/cyclonedx-javascript-library/pull/1411#pullrequestreview-4943152500)
  removes an unmaintained email-format dependency. Its setup/build, 18 focused
  and 4,180 full tests, TypeScript, ESLint and Knip passed, but a real 1.7
  validator comparison showed that it rejects a quoted local-part address
  accepted by current `main` and by the replaced dependency. I requested a
  deliberate compatibility decision and regression on exact head `1fece39d`.
  The PR remains changes-requested and unaccepted.
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
- **Merged after maintainer approval:**
  [rclone PR #9766](https://github.com/rclone/rclone/pull/9766)
  implements pattern-based transfer ordering for help-wanted issue #3975.
  Maintainer `ncw` approved exact head `c0e4e905` and merged it as `bb7c081e`
  into default `master`, closing the issue. To be exact about the CI: the
  `windows` job was failing at the approved head and a post-merge `master` lint
  step also failed; the maintainer merged regardless, and I am not claiming
  either job as passing or as something I fixed. This is one accepted
  contribution, not rclone maintainership.
- **Closed as superseded:** [BuildKit PR #7038](https://github.com/moby/buildkit/pull/7038)
  made `history.maxEntries=0` explicitly disable build-history persistence. The
  focused integration test passed across nine worker variants and the approved
  fork workflow matrix was green. Maintainer `tonistiigi` then closed it in
  favour of his own PR #7040. It was not rejected on code grounds, but it was
  **not merged**, so I do not count it as an accepted contribution.
- **Open:** [Airflow PR #71535](https://github.com/apache/airflow/pull/71535)
  refreshes a stale local bare Git origin when a requested bundle tracking ref
  cannot be resolved. Focused, module, type, packaging and real promotion paths
  passed locally. The upstream matrix has now finished with no failing and no
  pending job, though ten jobs were cancelled upstream, so I describe it as
  "no failure" rather than fully green. It remains unaccepted.
- **Open:** [Astropy PR #20234](https://github.com/astropy/astropy/pull/20234)
  rejects FITS tables with more than 999 physical columns before writing a
  partial file and adds the 999/1000 boundary regression. Astropy member
  `pllim` requested a plain-text changelog entry; I pushed the tested one-line
  change and resolved the sole review thread. The previously gated fork
  workflows have now run: every required test, build and changelog check passes
  and both Codecov contexts are green. The one red context is an upstream job
  explicitly labelled an allowed failure, and its failures are SciPy
  development-version deprecation errors in unrelated modules, not in FITS. The
  review was not an approval, and the PR remains unaccepted.
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
PR #7267 and #7306, tox #4022, rclone #9766, Anchore Syft #5179, Plotly.js #7959,
CycloneDX JavaScript #1507 and TheELNFileFormat #157 are
one accepted contribution each in their respective projects; eLabFTW PR #7319
(merged by `NicolasCARPi` as `197e71d1`, closing issue #7302) joins #7267 and
#7306 there as the third accepted contribution in that project, for
eighteen accepted external contributions in total, before eLabFTW PR #7307
(approved by `NicolasCARPi` after an addressed changes-requested cycle and
merged as `8db29efc`, closing issue #6952) brought the total to **nineteen
accepted external contributions** and made eLabFTW a four-time accepted
project (#7267, #7306, #7319, #7307) — the deepest active repeat
relationship by recent engagement, with TheELNFileFormat (six accepted)
the longest-standing. BuildKit #7038 was closed as superseded and is not
counted. They do **not** make
me a module
owner or core
maintainer. CycloneDX Python #935/#940/#980/#1007/#1015/#1016, CycloneDX
JavaScript #1411 and specification #1019 are review contributions; rclone
#9768, python-docx-template #661, #642, #648 and #650, Argo CD #29175 and pandas
#66623 are independently tested reviews, while python-docx-template #662,
cibuildwheel #2966 and eLabFTW #7306/#7307 remain
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
