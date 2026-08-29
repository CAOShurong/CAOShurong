# Contribution log — full detail

The README keeps the summary; this file keeps the receipts. Every entry here
is a public GitHub artifact (merged PR, open PR, review, or analysis thread).
Ordered roughly newest-first within each section.

## Merged (32 across 18 upstream repositories)

- **[restic #22029](https://github.com/restic/restic/pull/22029)** — removes the
  contradictory `data/` plaintext exception from the encryption documentation,
  matching the actual design and closing issue #22013. `MichaelEischer` merged
  exact head `4fee16ac` as `fb5e9df3` on 2026-08-29.
- **[restic #22028](https://github.com/restic/restic/pull/22028)** — repairs the
  broken PGP-key and MinIO documentation links, removing the obsolete MinIO
  Server section after its replacement redirected to a non-free product.
  `MichaelEischer` merged exact head `cf70c210` as `46ea3656` on 2026-08-29.

- **[asdf-vm/asdf #2317](https://github.com/asdf-vm/asdf/pull/2317)** — explains
  the dash-to-underscore mapping used by `ASDF_<TOOL>_VERSION` for dashed tool
  names such as `aws-sam-cli`. `Stratus3D` merged exact head `d1410b31` as
  `e4911f36` on 2026-08-28 after the documentation-site, shell, actions and
  semantic-pr checks passed.
- **[Apache Magpie #1118](https://github.com/apache/magpie/pull/1118)** — adds
  stable per-PR progress headers to the `pr-management-triage` interaction
  loop and four acceptance fixtures. Maintainer `potiuk` merged exact head
  `0949ce9a` as `e8c3a346` on 2026-08-27.
- **[Plotly.js #7981](https://github.com/plotly/plotly.js/pull/7981)** — corrects
  the `showspikes` documentation so it describes cursor-position behavior
  across all cartesian hovermodes. `emilykl` merged exact head `77fc5032` as
  `cc143a1c` on 2026-08-27.
- **[rclone #9818](https://github.com/rclone/rclone/pull/9818)** — repairs two
  dead backend-documentation links (Sia and Storj) after their sites moved.
  `albertony` merged exact head `31813d16` as `413138f5` on 2026-08-27.
- **[tox-dev/tox #4042](https://github.com/tox-dev/tox/pull/4042)** — updates
  the dead virtualenv discovery link and adds the required changelog fragment.
  `gaborbernat` merged exact head `4ef082c9` as `2a4a2157` on 2026-08-27.

- **[oss-review-toolkit/ort #12352](https://github.com/oss-review-toolkit/ort/pull/12352)** —
  repairs the user-facing license-handling guide after the declared-license
  mapping resource moved into the `spdx-expression` module. The one-line link
  fix passed DCO and was merged by `sschuberth` from exact head `7802e473` as
  `64a34a8a` on 2026-08-26.
- **[rclone #9823](https://github.com/rclone/rclone/pull/9823)** — treats a
  successful S3 `UploadPart` response without an ETag as a retryable error
  instead of dereferencing a nil pointer in a debug log and crashing the
  transfer. `ncw` merged exact head `3c0e7b28` as `660144d3` on 2026-08-26.

- **[argoproj/argo-workflows #16818](https://github.com/argoproj/argo-workflows/pull/16818)** —
  docs: fixes two dead RBAC manifest links in `docs/security.md`. The
  `workflow-controller-clusterrole.yaml` and `workflow-aggregate-roles.yaml#L4`
  links pointed at `manifests/cluster-install/workflow-controller-rbac/`, which
  was R100-renamed to `.../cluster-install-no-crds/workflow-controller-rbac/` in
  #14599 (2025-06-25); both 404'd since. First contribution to argoproj
  (CNCF graduated project). Merged 2026-08-26.
- **[regl-line2d #56](https://github.com/gl-vis/regl-line2d/pull/56)** — fixes
  the renderer half of [Plotly.js issue #7955](https://github.com/plotly/plotly.js/issues/7955):
  when callers supply a view `range`, line vertex positions are normalized by
  that range instead of static data bounds, so `scattergl` lines and markers no
  longer drift apart under deep zoom. Reviewer `dy` asked that my scratch
  verification script become a runnable test; I replaced it with a tape-based
  CPU-exact regression (`test/range-normalize.js`, 25 assertions including a
  discrimination subtest proving the old path drifts ~5 px at 1e-6 zoom), and
  he merged head `c2972eb` as `90d30fa1`.
- **[Astropy #20256](https://github.com/astropy/astropy/pull/20256)** — fixes
  the IERS DegradedAccuracy table handling so degraded-accuracy rows are
  merged instead of silently overwriting the predictive table (bug found while
  writing a regression test for issue #20242). `mhvk` reviewed, requested a
  changelog rename, approved after the fix, and merged it as `9f4de8d6`. He
  then opened follow-up #20262 for a forgotten test adjustment; I reproduced
  the failure locally on the merge commit and posted an exact-head
  verification of his PR.
- **[eLabFTW #7307](https://github.com/elabftw/elabftw/pull/7307)** — makes
  `prune:entries` remove orphaned `tags2entity` rows together with the
  soft-deleted entity rows in one transaction (issue #6952). `NicolasCARPi`
  requested changes (race condition, scalability, missing regression test), I
  addressed all three, and he approved and merged it as `8db29efc`.
- **[eLabFTW #7319](https://github.com/elabftw/elabftw/pull/7319)** — fixes
  the show-mode page-width regression from issue #7302: dashboard quick links
  carry `mode=show`, which re-applied the `max-width-70` cap for users
  preferring the tabular display. Traced to the `enableWide` condition
  (PR #7041 gated only the no-mode branch); one-line fix, merged as
  `197e71d1`.
- **[eLabFTW #7306](https://github.com/elabftw/elabftw/pull/7306)** — trims
  whitespace from CSV column names so headers like ` title ` match the
  expected column instead of failing with a misleading error (issue #7024).
- **[eLabFTW #7267](https://github.com/elabftw/elabftw/pull/7267)** — adds
  the licensed BenchLineage v0.3.5 demo as a cross-producer ELN import
  fixture after a maintainer welcomed the proposal in issue #7263. A real
  PHP/MySQL import selected an experiment and preserved all 20 linked
  uploads; merged at exact head `baeb6e37`.
- **[TheELNFileFormat #157](https://github.com/TheELNConsortium/TheELNFileFormat/pull/157)**
  — adds a web `.eln` checker reusing the test-suite checks. `SteffenBrinckmann`
  reviewed six requested changes; I implemented all of them (unified
  `runChecks` entry point, path/upload support, Streamlit alignment, ordered
  results, tests, consortium logo) and he merged it as `401e7aa5`.
- **[TheELNFileFormat #156](https://github.com/TheELNConsortium/TheELNFileFormat/pull/156)**
  — validates the single-root-folder archive requirement.
- **[TheELNFileFormat #155](https://github.com/TheELNConsortium/TheELNFileFormat/pull/155)**
  — clarifies how child `Dataset` relationships are represented (closes #116).
- **[TheELNFileFormat #154](https://github.com/TheELNConsortium/TheELNFileFormat/pull/154)**
  — makes parameter checks handle array-valued `Dataset` and `File` types,
  with regression cases for both invalid and valid nodes.
- **[TheELNFileFormat #153](https://github.com/TheELNConsortium/TheELNFileFormat/pull/153)**
  — clarifies `@type`, `additionalType` and `genre` in the specification
  (closes #105).
- **[TheELNFileFormat #152](https://github.com/TheELNConsortium/TheELNFileFormat/pull/152)**
  — adds a reproducible BenchLineage-generated `.eln` fixture and mapping.
- **[SampleDB #92](https://github.com/sciapp/sampledb/pull/92)** — preserves
  flexible ELN metadata named `parts` while assigning collision-free keys to
  generated nested-Dataset relationships.
- **[SampleDB #91](https://github.com/sciapp/sampledb/pull/91)** — fixes valid
  ELN imports that contain explicit ZIP directory entries while preserving
  rejection of genuine multi-root archives.
- **[Syft #5179](https://github.com/anchore/syft/pull/5179)** — adds detection
  for multi-arch ingress-nginx v1.9.6 binaries across amd64, arm64, arm/v7 and
  s390x, each producing exactly one 1.9.6 package in real CLI scans. `wagoodman`
  approved and merged it as `5c6cf08a`.
- **[Plotly.js #7959](https://github.com/plotly/plotly.js/pull/7959)** — fixes
  numeric `bundlecolors` sorting for parallel-categories paths (issue #7952).
  `camdecoster` requested NaN handling; I implemented it with the JSDoc and a
  Jasmine regression test, and he approved and merged it as `95bfea16`.
- **[CycloneDX JavaScript #1507](https://github.com/CycloneDX/cyclonedx-javascript-library/pull/1507)**
  — maps string-valued `package.json` engine constraints to the official npm
  CycloneDX taxonomy. `jkowalleck` asked for the handling to move inside
  `ComponentBuilder` with malformed-value coverage; after my rerun of 8
  focused and 4,155 full tests, lint, eslint, knip and builds he dismissed the
  request, approved twice, and merged it as `2a816627`, releasing v10.2.0.
- **[CycloneDX Python #1028](https://github.com/CycloneDX/cyclonedx-python-lib/pull/1028)**
  — encodes local XML-schema paths as file URIs and adds a regression test
  for package paths containing `#`. All 47 public checks passed; merged,
  closing issue #551, released in v11.11.2.
- **[Keycloak #51697](https://github.com/keycloak/keycloak/pull/51697)** —
  reports OID4VCI credential-request errors consistently and adds regression
  coverage for missing claims metadata and invalid proof timing. Fixed
  help-wanted issue #51692.
- **[tox #4022](https://github.com/tox-dev/tox/pull/4022)** — provisions the
  requested tox version before reading version-specific configuration. Added
  the exact `tox l` / `tox c` behavior coverage requested in review; `gaborbernat`
  approved and merged it as `c3f8d227` (closes #4021).
- **[rclone #9766](https://github.com/rclone/rclone/pull/9766)** — implements
  pattern-based transfer ordering for help-wanted issue #3975. `ncw` approved
  and merged it as `bb7c081e`. (For CI accuracy: the windows job was failing
  at the approved head and a post-merge lint step also failed; the maintainer
  merged regardless, and I do not claim either job as passing.)

## Open pull requests (proposals awaiting maintainer decision)

- **[tqdm/tqdm #1807](https://github.com/tqdm/tqdm/pull/1807)** — fixes a
  CI-safety/behavior bug (tqdm/tqdm#1501): `logging_redirect_tqdm` added a
  `_TqdmLoggingHandler` to any target logger even when it had **no** console
  handler, so a logger that previously produced no console output began
  emitting to the console. Root cause: the handler-replacement ran
  unconditionally; fix moves it under the `if orig_handler is not None:` guard.
  New regression test fails on pristine `master` and passes with the patch;
  full `tests/tests_contrib_logging.py` (20) + `tests/tests_contrib.py` pass;
  `git diff --check` clean. OPEN/MERGEABLE, review required. First PR to tqdm.
- **[pallets/click #3803](https://github.com/pallets/click/pull/3803)** — fixes a
  crash (pallets/click#3802): a second `KeyboardInterrupt` (Ctrl-C) arriving
  while click prints its "Aborted!" message during exception handling escaped
  `main()` and crashed the process. Root cause: `isatty()` only guarded
  `except Exception`, but `KeyboardInterrupt` is a `BaseException`, so the stream
  probe's `KeyboardInterrupt` escaped. Fix widens the guard to
  `(Exception, KeyboardInterrupt)` returning `False`. Two regression tests
  (`test_isatty_swallows_keyboard_interrupt`,
  `test_abort_echo_absorbs_keyboard_interrupt_in_isatty`) fail on pristine
  `main` and pass with the patch; full compat/termui/basic/options/arguments
  suites pass (1298 passed, 18 skipped). OPEN/MERGEABLE. First PR to click.
- **[fsnotify/fsnotify #773](https://github.com/fsnotify/fsnotify/pull/773)** —
  fixes the Windows deadlock between `Close()` and `Add()`/`Remove()` reported
  in #704: adds a `closeCh` channel closed by `Close()` under `mu`; `AddWith`
  and `Remove` `select` on it and return `ErrClosed` instead of blocking. New
  regression test `TestWindowsCloseAddRace` runs the race 200× and passes on
  Windows; `go build ./...` and `go vet ./...` clean. OPEN/MERGEABLE.
- **[libusb/libusb #1954](https://github.com/libusb/libusb/pull/1954)** —
  docs-only fix for #1938: corrects the `libusb_open()` event-source narrative
  after the events-lock removal. Exact head `24258d9c`; source cross-check and
  diff checks pass, while AppVeyor is pending. Open and awaiting review.
- **[ossf/scorecard #5202](https://github.com/ossf/scorecard/pull/5202)** —
  extends the Packaging detector to recognize `gh release create/upload/edit`
  and the official Nextcloud App Store release API, while keeping read-only
  `gh release view` as a non-match. Exact head `e7efdc2e`; focused file-parser,
  raw/evaluation tests, `go vet`, and diff checks pass locally, and PR Verifier,
  DCO and Kusari Inspector are green. The PR is OPEN/MERGEABLE and awaits
  maintainer review; its static fix does not claim a Packaging score without a
  successful workflow run.
- **[pypa/cibuildwheel #2977](https://github.com/pypa/cibuildwheel/pull/2977)** — docs-only refresh for three dead external links and one legacy redirect: CircleCI's moved open-source guide and canonical configuration reference, plus CPython's relocated Android and iOS testbed READMEs. Replacement URLs and destination headings were checked live; exact head `f8f58971`; the PR is OPEN/MERGEABLE with no reviewer requested, five successful contexts, one neutral check, and no pending or failing checks at the 2026-08-27 audit. Not accepted until merged.
- **[gitleaks/gitleaks #2252](https://github.com/gitleaks/gitleaks/pull/2252)** — fixes a CI-safety bug (gitleaks#1464): a failed git scan was silently reported as a clean pass. Root cause: the git-stderr error is routed through `DetectSource`'s per-fragment callback, which logged and returned `nil`, so the error never reached `findingSummaryAndExit` and the process exited `0` ("no leaks found") despite `0 commits scanned`. Fix: `DetectSource` propagates the error so the existing `os.Exit(1)` path fires; benign git warnings are not routed through this channel, so partial scans keep their behavior. Includes regression test `TestDetectGitFailedScanPropagatesError` (RED on pristine `master`, GREEN with the patch). First PR to gitleaks; MERGEABLE.
- **[mikefarah/yq #2840](https://github.com/mikefarah/yq/pull/2840)** — docs dead-link fix: README's strict-confinement note pointed at the dead `docs.snapcraft.io/snap-confinement/6233` URL (404 after the Snapcraft docs moved to `snapcraft.io/docs`); replaced with the live `snapcraft.io/docs/snap-confinement` page (HTTP 200 verified). First PR to mikefarah/yq; no CLA/DCO gate; MERGEABLE.
- **[xarray #11544](https://github.com/pydata/xarray/pull/11544)** — fixes
  GH#7527: `idxmax`/`idxmin` (DataArray and Dataset) silently promoted the
  integer coordinate label dtype to float64 on floating-point data even for
  fully-valid reduction slices. Root cause in `_calc_idxminmax`: `.where` ran
  unconditionally with the default float fill value. Fix gates the fill on
  `allna.any()` so valid slices keep their coordinate dtype. Carries a
  regression test and updated docstring examples. First PR to pydata/xarray.
- **[eLabFTW #7336](https://github.com/elabftw/elabftw/pull/7336)** — Ctrl+S
  save path for both TinyMCE and Markdown editors, following the fix direction
  `NicolasCARPi` gave on issue #7075. Reviewed once; two scoped fix commits
  (listener scope, no-shift modifier, eslint compliance) pushed in response.
- **[Plotly.js #7991](https://github.com/plotly/plotly.js/pull/7991)** —
  colorbar `dtick` log/date string forms documented as unsupported.
- **[Plotly.js #7986](https://github.com/plotly/plotly.js/pull/7986)** —
  Sankey `node.pad` clamp warning restore (fixes #7832).
- **[Plotly.js #7978](https://github.com/plotly/plotly.js/pull/7978)** —
  sankey nodes clipped at the plot edge laid out with corrected bounds
  (fixes #7946); CI green after a draft-log leak repair.
- **[Plotly.js #7977](https://github.com/plotly/plotly.js/pull/7977)** —
  `node.pad` warning no longer fires for geometry-derived effective padding
  (fixes #7832); full jasmine suite passes.
- **[Syft #5229](https://github.com/anchore/syft/pull/5229)** (draft) — PE
  VERSIONINFO parsing prefers the US-English StringTable over the last-parsed
  language block, so multi-language binaries report a matchable CPE (fixes
  #5177).
- **[Syft #5228](https://github.com/anchore/syft/pull/5228)** (draft) — yarn
  v1 dev-only classification uses the union of edges across same-name
  lockfile entries instead of last-entry-wins (fixes #5204).
- **[Syft #5227](https://github.com/anchore/syft/pull/5227)** (draft) —
  binary packages only excluded when owned by a same-named OS/Bitnami
  package, restoring ownership-overlap name matching (fixes #5214).
- **[Syft #5220](https://github.com/anchore/syft/pull/5220)** — requested-
  version metadata loss for packages whose version comes from a sibling
  same-name entry (fixes #5211); independent regression test included.
- **[Syft #5219](https://github.com/anchore/syft/pull/5219)** — uber-jar
  version read from the root `version.properties` instead of dropped
  (fixes #5163).
- **[Syft #5218](https://github.com/anchore/syft/pull/5218)** — Gradle
  `versions.lock` (consistent-versions plugin) lockfile parsing with an
  end-to-end verified fixture.
- **[Syft #5215](https://github.com/anchore/syft/pull/5215)** — reviewed and
  verified the community fix for #5214 with an independent test.
- **[setuptools #5312](https://github.com/pypa/setuptools/pull/5312)** —
  `dependency_links` deprecation documentation fix.
- **[setuptools #5310](https://github.com/pypa/setuptools/pull/5310)** — PEP
  639 UTF-8 license-file validation (RED/GREEN + e2e verified).
- **[setuptools #5309](https://github.com/pypa/setuptools/pull/5309)** —
  Windows false absent-package warning caused by a path separator mismatch in
  the analysis (fixes #5093).
- **[setuptools #5308](https://github.com/pypa/setuptools/pull/5308)** — bdist
  leftover cleanup (fixes #5134); red/green + e2e verified.
- **[setuptools #5307](https://github.com/pypa/setuptools/pull/5307)** —
  MSBuild property layout for VS2019+ Current (fixes #5275).
- **[rclone #9815](https://github.com/rclone/rclone/pull/9815)** — fixes
  #9634: `sync/move --delete-empty-src-dirs` was permanently disabled for any
  run sharing a stats `_group` with an earlier failed job. Regression test
  seeds an unrelated group error and asserts the subsequent clean move still
  removes emptied directories (fails on master); full `fs/sync` suite passes.
- **[GitUI #3016](https://github.com/gitui-org/gitui/pull/3016)** — Windows
  `core.autocrlf=true` fix for the help-wanted issue #1936: one-line
  `rustfmt.toml` change to `Auto`, workspace nextest 313/313.
- **[cibuildwheel #2966](https://github.com/pypa/cibuildwheel/pull/2966)** —
  removes an unconditional NuGet fallback source with regression coverage.
- **[Airflow #71535](https://github.com/apache/airflow/pull/71535)** —
  refreshes a stale local bare Git origin when a bundle tracking ref cannot be
  resolved. No failing jobs upstream (ten cancelled), so "no failure" rather
  than fully green.
- **[Astropy #20234](https://github.com/astropy/astropy/pull/20234)** —
  rejects FITS tables with more than 999 physical columns before writing a
  partial file; required tests, build, changelog and both Codecov contexts
  green (one red context is an upstream allowed-failure job in unrelated
  modules).
- **[Kustomize #6224](https://github.com/kubernetes-sigs/kustomize/pull/6224)**
  — legacy release-download support for pre-module tags; all 23 checks pass,
  blocked only on the official EasyCLA rerun authorization.
- **[python-docx-template #662](https://github.com/elapouya/python-docx-template/pull/662)**
  — fixes escaped Jinja delimiters split across Word runs (issue #548),
  following the project owner's public contribute-first maintainer path.

## Verified reviews of third-party changes

Each review ran the project's real test suite on the exact head under review.

- **CycloneDX Python** — #1016 (reproduced a lost strict-valid relationship,
  requested bounded coverage), #1015 (CycloneDX 1.7 algorithm identifiers; 344
  focused + 7,305 full tests), #980 (`Service.trustZone` across 1.4–1.7),
  #1007 (quadratic registration removal; complexity guard across 20 hash
  seeds), #940 (bounded validation errors; found misleading nested-error
  selection in 10 of 21 contextual errors), #935 (side-effect-free validator
  that dropped a public call; requested a compatibility wrapper).
- **python-docx-template** — #661 (sdist license/test contents), #642 (CLI
  validation that printed errors but returned exit 0 — requested changes),
  #648 (`Subdoc` imports), #650 (hyperlinks across templated runs).
- **GitUI** — #3015 (reran fmt/check + focused and full nextest; found a
  pygit2 stash-subdirectory reproduction).
- **manual-approval #206** — reproduced five compile blockers with go
  test/vet/build and golangci-lint on the exact head (`CHANGES_REQUESTED`).
- **Argo CD #29175** — reproduced three boolean-parsing boundary failures
  diverging from bundled Dex v2.45.1.
- **pandas #66623** — two exact MultiIndex memory tests failed and a doctest
  was stale (`CHANGES_REQUESTED`).
- **rclone #9768** — OneDrive upload-session handling after a 404; requested
  a no-same-session-retry regression.
- **CycloneDX JavaScript #1411** — found the replacement dependency rejects a
  quoted local-part address accepted by current `main`.
- **CycloneDX specification #1019** — implements the schema defect I reported
  in issue #1018; ran the Java, Node and Buf gates and closed my later
  duplicate to reduce maintainer work.
- **Syft** — #5225, #5216, #5198 (found a Windows CRLF edge case in the
  competing fix for my #5177 analysis), #5145 (real arm64 vmlinuz E2E probe).
- **Plotly.js #7967, HolmesGPT #2418** — exact-head verification reviews.
- **gitleaks #2249** — verification review (rev 204) of external author `vaibhav8a`'s fix for the file-read sibling of our #2252: an unreadable file made `Fragments` return `nil` and `findingSummaryAndExit` print `no leaks found` exit 0. Reviewed from exact head `509fce15` — `go build`/`go vet`/`go test ./sources/` clean; independently confirmed via grep that `s.Sema.Go`/`d.Sema.Go` errors are never read (no `.Wait()` is ever called), so the old `return nil` could never reach the caller; flagged the same defect class in the mid-read `return err` path as an out-of-scope sibling fix.

## Analysis threads (root-cause comments on upstream issues)

- **plotly.js #7979** — quiver `arrowref: 'paper'` automargin: `calc.js`
  expands ranges with a data-space reading of the arrow tip while `plot.js`
  renders paper arrows in pixels; off-square layouts are off by
  `sqrt(|ya._m|/|xa._m|)` (numerically verified: a ~1992 px tip in an 800 px
  plot).
- **plotly.js #7955** — scattergl line/marker zoom drift: shader-faithful
  float32 simulation plus a variant sweep; renderer-side fix merged in
  regl-line2d #56, analysis posted on the issue.
- **syft #5224** — CPE collisions from multiple packages sharing one CPE.
- **syft #5177** — PE `VERSIONINFO` language-block selection (led to PR
  #5229).
- **syft #5214** — exclude-binary-overlap-by-ownership suppressing vendored
  libraries owned by unrelated RPMs (led to PR #5227).
- **syft #5204** — yarn v1 cataloger dropping 627 of 745 packages silently
  (led to PR #5228); plus #5211 determinism and lossiness analysis.
- **syft #5173, #5129, #5163** — encoder asymmetry, Ansible inventory RFC
  feedback, glob-poisoning finding in the verification thread.
- **rclone #9810** — `ListR` disable timing; **#9807** — ModTime isolation
  without iCloud; **#9634** — empty-dir deletion gate (led to PR #9815).
- **HolmesGPT #2046** — design feedback at the author's invitation.
- **xarray #10267** — stale-triage: tried to reproduce the "repeated dimension
  name in DataTree" failure against current main and at the historical points
  where the asserting test was introduced and the night before #10623;
  `open_groups`/`open_dataset` were identical at every point with both engines,
  so the bug was fixed as a side effect of the DataTree/netCDF IO rework
  (most likely #10623). Recommended closing as already-fixed.
- **gitleaks #1464** — root-cause + design comment on a CI-safety bug: a failed
  git scan is reported as a clean pass. Reproduced on a `master` source build
  (`718896a`): an invalid `--log-opts` range makes git scan fail (`0 commits
  scanned`) yet the process exits `0` with "no leaks found". Root cause:
  `cmd/detect.go` logs and discards the `DetectSource` error instead of
  propagating it, so `findingSummaryAndExit` (`cmd/root.go:493`) never hits its
  `os.Exit(1)`; the earlier #1461 fix only covered the `DetectGit`/diff path.
  Advised against `logging.Fatal` (would drop collected findings, breaking
  partial scans) in favour of propagating the error; offered a minimal fix +
  regression test.

## Closed / superseded

- **[BuildKit #7038](https://github.com/moby/buildkit/pull/7038)** —
  `history.maxEntries=0` explicitly disabling build-history persistence.
  Integration test passed across nine worker variants; `tonistiigi` closed it
  in favour of his own PR #7040. Not merged, so not counted as accepted.
