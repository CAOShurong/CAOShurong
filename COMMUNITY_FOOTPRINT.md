# Community footprint

Public contributions made outside the owned repositories — upstream fixes,
reviews, triage and design comments in other projects' communities. This file
is updated every round by the identity agent (②) so the work is visible in one
place instead of being scattered across other people's repos.

## 2026-08-26
- [rclone/rclone#9823](https://github.com/rclone/rclone/pull/9823) — P1 修复 PR（fixes #9822，雷达新候选）：S3 multipart 上传中后端/代理返回无 ETag 的 200 响应时，WriteChunk 在 debug 日志里无条件解引用 `*uout.ETag` 导致整个传输 panic；修复为在 pacer 回调内返回可重试错误强制重传该分片（比仅加日志守卫更正确——nil ETag 否则会被记入 completedParts 直到 CompleteMultipartUpload 才被服务端 InvalidPart 拒绝）。go vet / s3 测试套件 / 全仓 build 全绿
- [jax-ml/jax#40014](https://github.com/jax-ml/jax/pull/40014) — verification review 5027204410 (RED confirmation, exact-head)
- [dask/dask#12570](https://github.com/dask/dask/pull/12570) — docs dead-link PR (889-URL sweep, first dask contribution)

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
- [zarr-developers/zarr-python#4289](https://github.com/zarr-developers/zarr-python/pull/4289) — P3 docs 修复 PR（fixes #3681）：文档示例里非持久化演示（~20 处数组）原本在构建时写盘到本地 `data/`，改为内存存储（`memory://`/`MemoryStore`/空 dict），持久化演示块改为各自清理自己的临时目录；`tests/test_docs.py` 61 passed/2 skipped 全绿（额外修掉一个 ZipStore 父目录未被创建的隐藏脆弱性）

## 2026-08-25

- [rclone/rclone#9817](https://github.com/rclone/rclone/pull/9817) — fix PR: dropbox ChangeNotify case-insensitive root trim (9 tests green)
- [pydantic/pydantic#13704](https://github.com/pydantic/pydantic/issues/13704) — triage: repro + root cause + fix-attempt
- [astral-sh/ruff#28051](https://github.com/astral-sh/ruff/pull/28051) — opened: exec-builtin non-call reference detection (preview)
- [jax-ml/jax#40151](https://github.com/jax-ml/jax/pull/40151) — exact-head verification review
- [restic/restic#22028](https://github.com/restic/restic/pull/22028) — docs dead-link fix
- [tqdm#1805](https://github.com/tqdm/tqdm/pull/1805) — fix PR (CI green)
- [eLabFTW](https://github.com/elabftw/elabftw) — multiple merged contributions (value-labels must-fix rescue)

## Totals (rolling)

Counts re-verified against the GitHub API on 2026-08-26 (evening; search:
`is:pr author:CAOShurong is:merged` / `is:open`, own org excluded from
merged; open items are all external). A PR counts here only once GitHub
shows it merged.

- External merged PRs: **22 / 100** across 12 upstream projects
  (latest merge: [argo-workflows#16818](https://github.com/argoproj/argo-workflows/pull/16818),
  merged 2026-08-26 — first argoproj contribution. Note: GitHub search
  under-counts by one — TheELNFileFormat #152 is MERGED per direct API but
  missing from the search index; totals here use direct-API verification)
- Open external PRs: **64** across **32** upstream organisations
- Communities active in: eLabFTW, TheELNFileFormat, SampleDB, Astropy, CycloneDX, Keycloak, Plotly.js, rclone, Syft, tox, regl-line2d, pydantic, ruff, jax, numpy, restic, tqdm, beets, sigstore, grype, and more.
