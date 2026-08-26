# Community footprint

Public contributions made outside the owned repositories — upstream fixes,
reviews, triage and design comments in other projects' communities. This file
is updated every round by the identity agent (②) so the work is visible in one
place instead of being scattered across other people's repos.

## 2026-08-26

- [astropy/astropy#19717](https://github.com/astropy/astropy/pull/19717) — exact-head 验证型审查（63b6b5f7）：确认修复有效（masked 全套件 1193 通过），但发现旧格式 pickle 向后兼容破坏（MaskedQuantity 旧 pickle 加载 TypeError，MRO 不对称机制已实证），并指出回归测试用 `MaskedNDArray([1,2,3])` 把数据误当 shape
- [astropy/astropy#20272](https://github.com/astropy/astropy/pull/20272) — 修复 PR：Masked 数组的 mask 若自身是 Masked/np.ma 数组会被嵌套存储导致静默丢值（fixes #20246，610+1288 测试全绿）
- [argoproj/argo-workflows#16818](https://github.com/argoproj/argo-workflows/pull/16818) — docs 死链修复 PR：security.md 中 RBAC manifest 目录改名后失效的 2 个链接（743 个 URL 全量核验）
- [rclone/rclone#9778](https://github.com/rclone/rclone/pull/9778) — exact-head 审查：补丁验证通过、stack overflow 可复现但 CLI 路径不可达（COMMENTED）
- [gitleaks/gitleaks#2239](https://github.com/gitleaks/gitleaks/issues/2239) — 分析评论：redact-half 在 filter→Finding.Redact 破坏性管线中不可行的代码走读
- [restic/restic#22029](https://github.com/restic/restic/pull/22029) — docs fix PR: resolve the design.rst contradiction on which files are encrypted (`data/` was wrongly listed as a plaintext exception; fixes #22013)
- [rclone/rclone#9798](https://github.com/rclone/rclone/issues/9798) — triage RCA comment: iclouddrive bundle-version static analysis root cause
- [jax-ml/jax#40150](https://github.com/jax-ml/jax/issues/40150) — XLA-CPU thunk regression design comment (repro + scale analysis)
- [sigstore/cosign#5072](https://github.com/sigstore/cosign/pull/5072) — docs dead-link fix PR (2 links)
- [numpy/numpy#32438](https://github.com/numpy/numpy/pull/32438) — P1 triage fix: MaskedArray.__array_wrap__ propagation
- [jax-ml/jax#40170](https://github.com/jax-ml/jax/pull/40170) — verification review (signed-zero fix, exact-head)
- [jax-ml/jax#40185](https://github.com/jax-ml/jax/issues/40185) — triage RCA (sigma^2 intermediate)
- [beetbox/beets#6950](https://github.com/beetbox/beets/pull/6950) — docs dead-link fix (first PR to repo)
- [anchore/grype#3630](https://github.com/anchore/grype/issues/3630) — discussion: direction-2 prototype

## 2026-08-25

- [rclone/rclone#9817](https://github.com/rclone/rclone/pull/9817) — fix PR: dropbox ChangeNotify case-insensitive root trim (9 tests green)
- [pydantic/pydantic#13704](https://github.com/pydantic/pydantic/issues/13704) — triage: repro + root cause + fix-attempt
- [astral-sh/ruff#28051](https://github.com/astral-sh/ruff/pull/28051) — opened: exec-builtin non-call reference detection (preview)
- [jax-ml/jax#40151](https://github.com/jax-ml/jax/pull/40151) — exact-head verification review
- [restic/restic#22028](https://github.com/restic/restic/pull/22028) — docs dead-link fix
- [tqdm#1805](https://github.com/tqdm/tqdm/pull/1805) — fix PR (CI green)
- [eLabFTW](https://github.com/elabftw/elabftw) — multiple merged contributions (value-labels must-fix rescue)

## Totals (rolling)

Counts re-verified against the GitHub API on 2026-08-26 (search:
`is:pr author:CAOShurong is:merged` / `is:open`, own org excluded from
merged; open items are all external). A PR counts here only once GitHub
shows it merged.

- External merged PRs: **21 / 100** across 12 upstream projects
- Open external PRs: **60** across **34** upstream organisations
- Communities active in: eLabFTW, TheELNFileFormat, SampleDB, Astropy, CycloneDX, Keycloak, Plotly.js, rclone, Syft, tox, regl-line2d, pydantic, ruff, jax, numpy, restic, tqdm, beets, sigstore, grype, and more.
