# Community footprint

Public contributions made outside the owned repositories — upstream fixes,
reviews, triage and design comments in other projects' communities. This file
is updated every round by the identity agent (②) so the work is visible in one
place instead of being scattered across other people's repos.

## 2026-08-27
- [gitleaks/gitleaks#2249](https://github.com/gitleaks/gitleaks/pull/2249#pullrequestreview-5039796619) — P2 验证型审查（rev 204，对外部作者 `vaibhav8a` 的 exact head `509fce15`，closes #2232；review id `5039796619`，状态 COMMENTED，已披露 AI 辅助）：这是我们自己 #2252 的**文件读取孪生**——两者都修「静默判绿」类 CI 安全隐患（部分扫描被报成 `no leaks found` exit 0）。从 exact head 实测：`go build ./...` 干净、`go vet ./sources/... ./cmd/...` 干净、`go test ./sources/` 通过（4 个新测试里 2 个因权限位在 Windows runner 上按设计 self-skip，macOS/Linux CI 才跑到新的 `else` 分支）。**独立用 grep 确认了作者根因**：`s.Sema.Go(...)`/`d.Sema.Go(...)` 出现在 `sources/files.go`、`sources/git.go`、`detect/files.go`、`detect/git.go`，但**非测试代码里从来没有调用过 `.Sema.Wait()`（任何 Wait 都没有）**，于是 goroutine 内的错误被静默累积、永不被读取——原先 `return nil` 这个唯一回传通道因此永远到不了 `DetectSource`。修复（把读不到的文件错误收集进 mutex 保护的**本地** slice、join 进 `Fragments` 返回值）在不改变共享 semgroup 语义的前提下把错误送回调用方，并终于让 `cmd/root.go` 既有的 partial-scan 分支从文件打开路径可达。另指出一处作者正确地留在 scope 外的同源 defect：同一 goroutine 末尾的 `return err`（读取中途的 fragment-scan 错误）仍走 `s.Sema.Go`，因此被同一个「缺 Wait」的洞吞掉——建议用同样的本地错误收集模式补一个孪生修复。审查是诚实的 review 证据，不是接受/委派职责/合并权/维护权
- [gitleaks/gitleaks#2252](https://github.com/gitleaks/gitleaks/pull/2252) — P1 修复 PR（由 #1464 根因讨论升级而来，首次向该仓库做 PR 贡献）：CI 安全隐患——已失败的 git 扫描会被静默判绿。复现：在 `master`（`718896a`，即 #2252 的 base）源码构建后，非法 `--log-opts` 区间触发 git 扫描失败（`ERR [git] … stderr is not empty` + `0 commits scanned`），进程仍以 **0** 退出并打印 `no leaks found`。根因：`sources/git.go` 把 stderr 错误经 `yield(Fragment{}, err)` 传入 `DetectSource`，而 `DetectSource` 的片段回调仅 `logging.Error` 后 `return nil`，于是 `DetectSource` 返回 `nil`，`findingSummaryAndExit` 落到 `len(findings)==0 → 0`；#1461 只修了 diff/`DetectGit` 一侧，默认 `detect` 路径残留。修复：`DetectSource` 直接 `return err`（让 `cmd/root.go` 既有 `if err != nil { os.Exit(1) }` 生效），并移除 `cmd/detect.go`/`cmd/git.go`/`cmd/protect.go` 三处重写 `err` 的多余 swallow（benign 的「rename detection was skipped」类 warning 不进该 channel，partial-scan 行为不变、已采集 finding 仍先写出再非零退出）。回归测试 `TestDetectGitFailedScanPropagatesError` 自建临时仓库断言非法 `--log-opts` 返回非 nil 错误、合法扫描不报错；在 pristine `master` 上 RED、补丁后 GREEN；二进制实测非法扫描 exit 1、合法 scan exit 0。`go build/vet` + `go test ./detect/ ./sources/` 全绿，PR MERGEABLE，review required
- [mikefarah/yq#2840](https://github.com/mikefarah/yq/pull/2840) — docs 死链修复 PR（首次向该仓库贡献）：README 中 strict-confinement 说明指向的 `docs.snapcraft.io/snap-confinement/6233` 已 404（Snapcraft 文档迁移至 `snapcraft.io/docs`），改指现存活的 `snapcraft.io/docs/snap-confinement`（curl 跟随重定向 200 验证）；全仓外链清扫仅此一处真实失效（linux.die.net / StackOverflow 的 403 为反爬拦截，浏览器访问正常）。+1/-1，无 CLA/DCO 门槛，MERGEABLE

## 2026-08-26
- [dask/dask#12560](https://github.com/dask/dask/pull/12560#issuecomment-5425786759) — exact-head 验证型审查（base `ba5045e0` / head `fc78876c` 双 worktree 实测，py3.12 + pandas 3.0.5）：确认 `str.split(expand=True)` dtype 保持修复有效——base 上"pandas 结果 vs dask `_meta` vs dask 计算"三方矩阵在三种输入 dtype × 两种 convert-string 配置下错位（meta 报 `'str'`、实际产出 `'string'`），head 五探针全部自洽且 `string` dtype 与 pandas 精确一致；dask_expr 全套 **4329 passed** 零失败（`test_string_accessor.py` 53→54 恰为新增回归测试），两个 split 测试跨 `PYTHONHASHSEED` 0–15 全稳定。CI 归因：nightly 红全部是 scipy sparse 弃用连锁（`csr_matrix is being replaced by csr_array` 等）与无关事件循环错误，零字符串测试受累。附带发现（main 既有、非本 PR 引入，已附最小复现）：convert-off 下先构建 object 列 split 表达式再新建显式 `string` 列集合时，后者的输入元数据乃至计算输出可被翻转为 `'str'`（hash 种子依赖约 30% 概率，seed=7 确定性复现，pristine base 行为一致）
- [zarr-developers/zarr-python#4290](https://github.com/zarr-developers/zarr-python/pull/4290) — P1 修复 PR（fixes #4272，维护者在 issue 里明确背书方向 1）：嵌套序列 `chunks`（显式 rectilinear 请求）的边值恰好均匀+短尾（如 `[[10,10,4]]`）时，自 3.3.0 起被按"边值推断"静默折叠成 regular grid——两种 grid 创建时等价但 resize 行为分叉（regular 延伸均匀模式、rectilinear 追加边），追加式写入拿到与请求不同的（重写 chunk 的）布局。修复：`create_chunk_grid_metadata` 新增 keyword-only `requested_rectilinear`，两个 v3 创建调用点从原始用户输入推导（含 rectilinear shards 使外层 grid 变 rectilinear 的交互），flat/auto 规格保持按值推断，恢复 3.2.x 语义。回归测试 main 红/补丁绿；unified_chunk_grid+metadata+chunk_grids 612 passed、test_array.py 1307 passed 全绿（本地复现 issue 输出逐字节对齐）
- [oss-review-toolkit/ort#12352](https://github.com/oss-review-toolkit/ort/pull/12352) — docs 死链修复 PR（首次向该仓库贡献，6015 URL 全量外链清扫后定位）：license-handling 指南中内建 declared-license 映射表的链接仍指向 `utils/spdx/src/main/resources/`，该资源已在 db57349de 重构中移入新的 `spdx-expression` Gradle 模块，链接自那时起 404；修复为单行改指现路径。此链未被仓库自己的 linkspector 抓到的原因已查明：`.linkspector.yml` 以"Docusaurus 会自查"为由整体排除 `website/`，但 Docusaurus 只校验相对链接不校验绝对 GitHub blob URL。DCO SUCCESS
- [pydata/xarray#11543](https://github.com/pydata/xarray/pull/11543) — exact-head 验证型审查（base `551ced5e` / head `121c0595` 双 worktree 实测）：确认 netCDF4 引擎对非本机端序属性数组静默字节交换的修复有效——原始 base 复现 `>f8 [0,1]→[0,3.03865e-319]`、`>i4 [1,2]→[16777216,33554432]` 且无任何告警，head 全部用例（含 NETCDF3_CLASSIC 经 netcdf4 引擎写入、0-d 标量、只读数组属性）转绿；新回归测试 base 红 / head 绿；TestNetCDF4Data+TestScipy+TestGenericNetCDFData 共 431 passed 与 base 结果完全一致（零行为漂移）。附一条非阻塞事实更正：PR 描述中的 bears.nc 属性实为小端存储，并不触发此 bug
- [astropy/astropy#20265](https://github.com/astropy/astropy/pull/20265) — exact-head 验证型审查（base `3011554f` / head `c7af2c41` 双 worktree 实测）：确认修复有效——issue #20257 的报错实为"延迟爆炸"（`find` 本身不炸，陈旧的字符串 fill_value 留在 int64 结果上，直到 repr/filled 才 TypeError；astroquery 式 Table 过滤工作流在 base 复炸、head 通过）；无行为变化检查全过（比较 ufunc、非换 dtype ufunc 的自定义 fill 均原样保留）；table 套件 2425 passed + masked 套件 1192 passed 全绿。附两条非阻塞建议：`ma.core._check_fill_value` 是 numpy 私有 API 且为 astropy 首次使用（给出等价公开替代），回归测试建议补 masked 变体与合法自定义 fill 存活性断言
- [rs/zerolog#795](https://github.com/rs/zerolog/pull/795) — docs 死链修复 PR：README Benchmarks 段落的 `bench.zerolog.io` 已 NXDOMAIN（Cloudflare 与 Google 公共 DNS 双确认），logbench 基准套件改指其 GitHub 仓库本体；全仓 31 个 URL 扫描仅此一处失效
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

Counts were re-verified against the direct GitHub GraphQL/REST API on
2026-08-27. The merged set comes from the user's paginated `pullRequests`
connection, with TheELNFileFormat #152 directly rechecked because GitHub search
still omits it. Open items are external base repositories. A PR counts here
only once GitHub shows it merged.

- External merged PRs: **24 / 100** across **14** upstream repositories and
  **13** upstream owners. The latest merges are
  [rclone#9823](https://github.com/rclone/rclone/pull/9823) and
  [ORT#12352](https://github.com/oss-review-toolkit/ort/pull/12352), both merged
  2026-08-26 by upstream maintainers.
- Open external PRs: **66** across **37** repositories and **34** upstream
  owners (newest: [gitleaks#2252](https://github.com/gitleaks/gitleaks/pull/2252)).
- Communities active in: eLabFTW, TheELNFileFormat, SampleDB, Astropy, CycloneDX, Keycloak, Plotly.js, rclone, Syft, tox, regl-line2d, pydantic, ruff, jax, numpy, restic, tqdm, beets, sigstore, grype, and more.
