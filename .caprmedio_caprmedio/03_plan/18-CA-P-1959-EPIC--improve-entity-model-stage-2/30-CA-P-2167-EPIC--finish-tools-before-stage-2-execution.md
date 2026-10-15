---
atom_id: CA-P-2167
content_role: Plan
type: Plan
label: Epic
work_sequence_number: 30
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
status: Active
subjects:
  governs: Tool
  depends_on: [Atom, Subject, Projection, Plan, Journal, Operator]
version: 80
updated_at: "2026-10-15 12:26:16 +0000"
relations:
  is_decomposition_of: [CA-P-1959]
  blocks: [CA-P-1967, CA-P-1968, CA-P-1969, CA-P-1909, CA-P-1910, CA-P-1911, CA-P-1912]
---
# Summary

Finish Tools before Stage 2 execution

## Objective

The Tools required before affected Stage-2 execution have updated, independently verified connector/Workflow RMEDO with a coherent common logical connector interface, bounded implementation and fresh independent fixture proof.

## Details

### Actual Subjects-only migration and graph result — 2026-10-15

Local release `local-20261015-subject-batch-004` completed; its actual receipt is `.caprmedio_runtime/simple_local_release/reports/local-20261015-subject-batch-004.md`. The authorized sequence used pre-migration Git checkpoint `4fa3c461b` and committed all 611 edit drafts as `1d55642ea` before promotion.

One operation, `subjects-candidate4-20261015-001`, reached scheduler SUCCESS and a terminal completed batch: 611 completed, zero remaining, automatic retry false. Actual accepted/result evidence is `.caprmedio_install/workflow_orchestrator/runs/subjects-candidate4-20261015-001/accepted.json` and `subject_batch_progress.json` in that directory. No second confirmation, extra review/validation round, replay or batch rollback is claimed or required by this result checkpoint.

The actual migrated-source entity graph was rebuilt into `.caprmedio_caprmedio/_projection/core-subject-notation/after-current/`: `graph.json`, `indented.txt`, `provenance.json` and `manifest.json`. Its manifest records 906 owners, 4,491 occurrences, 782 nodes and 259 edges. Comparing its source hashes to `.caprmedio_tmp/stage2-migration-20261015/instructed-batch-source-refresh/source-pins.json` gives 611 changed and 295 unchanged owners (266 unchanged plus all 29 holds). The graph is the actual current mechanical Subjects projection, not full semantic/native graph admission. Ordinary content migration remains separate and unperformed.

Migration, required Journal effects and the actual graph output are committed as `6512a2e71`; these Plan result checkpoints are a separate change. This records successful authorized operation and actual graph output, not completion of unrelated deferred work. Keep this Plan Active while the Operator decides whether to move deferred branches to a Backlog Epic or retain them Active; no descendant is relocated or marked Done here, and no parent-status cascade is authorized.

### Operator-authorized minimum Subjects-only sequence — 2026-10-15

The Operator now authorizes this Candidate #4 Subjects-only sequence through the existing Workflows: commit current work → create the selected edit drafts → commit drafts → archive exact current predecessors and promote drafts → rebuild the entity graph from actual migrated sources. No additional confirmation, independent post-stage full preview, semantic review or extra review/validation round is required. This checkpoint supersedes conflicting earlier prerequisite, approval and Definition-of-Done clauses for this sequence; it does not remove normal operation checks or expand generic content-update authority.

Retain current target/draft checks and ordinary operation results, canonical ID and original Status restoration, Version +1, actual Project-time updated_at and byte-exact predecessor archives. Stop at the first failed or unknown result, preserve completed predecessors and the untouched remainder, and perform no automatic replay or batch rollback. Existing Git commits and predecessor archives remain recovery evidence, not permission for automatic reset. Preserve all 29 held owners unchanged and ordinary content migration separately under CA-P-1970. Record actual graph-rebuild output; candidate-only reproduction or a planned graph is not that output.

Local release `local-20261015-subject-batch-003` terminated with outcome `failed` at `tests`: the reported suite ran 3,391 tests with zero skips and one failed Docker module, `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/tests/test_first_cut_http_docker_e2e.py`. This is not release/runtime acceptance and no migration occurred. Evidence: `.caprmedio_tmp/verification/local-release-20261015-subject-batch-003.log` and `.caprmedio_runtime/simple_local_release/reports/local-20261015-subject-batch-003.md`.

Keep this Epic and unfinished descendants Active; completion and any status-cascade disposition remain unresolved. Preserve earlier receipts, failed/uncertain attempts and historical decisions without treating their superseded gates as current requirements. No FPF, new recovery machinery, content migration or unrelated rebuild is added.

### Selected Subjects-only batch Workflow — 2026-10-15

The Operator selected mass migration to the latest Candidate #4 through Workflows, using one reviewed exact Subject map/packet and one batch confirmation. For reusable Subjects-only batches, mandatory separate per-Atom semantic assessment reports and confirmations are removed; a batch does not depend on retaining the staging call's original MCP connection. Bind the persisted reviewed packet, exact targets/patches and current source evidence to that confirmation, with stale or mismatched evidence refusing before effects. This supersedes conflicting earlier per-target report/confirmation and same-connection requirements for Subjects-only batches; generic content updates remain unchanged.

This migration uses edit drafts: stage proposed next Atom revisions under `draft/` in bounded calls through the existing Tool. An edit draft carries a temporary `atom_id` such as `CA-R-123@draft` and Status `Draft`; the canonical current Atom remains unchanged. The temporary ID identifies a proposed edit, not a canonical original or a newly created Atom. New-Atom Drafts remain ID-free. After exact review and approval, archive the current revision byte-for-byte, restore the draft's canonical Atom ID and original Status, and publish Version N+1 with actual Project-time updated_at. Normalized promotion preserves the existing Subjects-only delta and all unrelated canonical bytes; temporary draft ID/Status do not become extra source changes. Reusable Subjects-only batches may still use a reviewed map without drafts; this migration selects the draft-backed path.

Retain independent per-Atom effects and truthful results within the ordered batch. Stop at the first failed or unknown result, keep completed predecessors, and leave the remainder untouched. No automatic replay or rollback of completed Atoms is admitted. Establish the exact pre-batch Git checkpoint and retain actual per-Atom before/after and failure evidence for explicit recovery; Git history is not a substitute for effect verification or permission for an automatic reset. Keep Version +1, actual Project-time updated_at and exact predecessor archives until the Operator explicitly changes those semantics. Previous-version archives and Git remain the existing recovery mechanisms; add no extra recovery machinery. Ordinary content, unrelated rebuilds and deferred content migration remain excluded.

Connected staging attempt 002 timed out and has no completion manifest. Its 611 candidate files reproduce the reviewed mechanical graph, but that candidate-only PASS is not successful staging, Tool completion or migration. Preserve that batch and the older uncertain batches; do not synthesize a receipt or replay them. Evidence: `.caprmedio_tmp/stage2-migration-20261015/connected-preview/stage611-current-rules-002.disposition.md` and `packet-stage-reproduction/candidate-only.md` under the same preparation root.

The Operator explicitly chose ordinary independent code review and tests without FPF for this change. Earlier FPF prerequisites do not apply to this fix. Execute these bounded responsibilities in order, reusing existing children and splitting any own-work leaf that exceeds 15 minutes before execution:

1. Align and independently check only the affected contracts for the selected batch review/confirmation, persisted packet, per-Atom effect and Git recovery boundaries.
2. Implement the batch through the existing Workflow and Atom-update machinery, including bounded existing-Tool edit-draft staging and normalized promotion, without another writer or general rebuild; retain current-rule self-update, target/intent validation and exact readback.
3. Run independent focused tests for rule self-update, stale packet/target refusal, draft tampering, draft/path collisions, normalized promotion restoring canonical ID/original Status, partial failure with completed predecessors preserved, reconnect/persisted confirmation, exact Version/time/history effects and no replay.
4. Verify the actual reviewed runtime and connected batch capability; local fixtures and saved candidate bytes do not establish it.
5. With the exact reviewed batch confirmation and required current evidence, execute the Subjects-only migration and independently reconcile all 906 owners, including 611 change owners, 266 unchanged owners and 29 holds, against the approved map/packet and reproduced graph.

These are pending ordered tasks, not completion receipts or a claim that current code already implements the decision. Keep this Epic Active. No source migration, completed stage, live approval receipt or new policy beyond the Operator's stated batch decision is inferred from this Plan update.

### Verified local release and current preparation evidence — 2026-10-15

Local release `local-20261015-current-rules-001` completed with terminal exit 0 after its mandatory full suite passed. It started from source HEAD `44b858ef9`; release checkpoints are `38039e0ff` (initial Journal checkpoint), `0280f77c4`, `eaa1b22b5` and `4a0aa8be2`. Exact suite module/test totals were not retained for this checkpoint and are not inferred. The actual local receipt is `.caprmedio_runtime/simple_local_release/reports/local-20261015-current-rules-001.md`.

The new Project MCP reports readiness on port 56317: container `6545b60287f9785d6c6c56467b18472f35d1def6d7f2bad5fb8c1e016cf31917`, image `sha256:92ec07477c7be9d3bfeed3acabbe0a80008bc7929805965d5f45b81bc9fdd7d6`, fingerprint `176ee3a888af7f7bdaac3aae70d68aa1e3029e9f5163b20f92df47989fc80d0f`. Its saved `ready.json` is under `.caprmedio_runtime/runtime/project_mcp/1c85ed12963e347a8b1698c22c50e1a1209fd9b20ec950631b61a9c12823bbee/`. The coordinator's actual connected `get_mcp_reload_status` succeeded at generation `cc69b313e2090ac70609c644509b45e5120e7e0fa5eb3e4a3e49d761c4dced76`; that response is conversation evidence, not an invented saved status receipt.

Independent review accepted the metadata-only `current-rules-refresh` successor and the mechanical forest's `mechanical-forest-current-rules` successor, preserving 906 source tuples, 611 change owners, 848 ordered patches, 266 unchanged owners and 29 held owners; Candidate #4 and the map remain unchanged. The preparation review is recorded in the reviewer's actual response, with no separate acceptance file claimed. The mechanical comparison is saved at `.caprmedio_tmp/stage2-migration-20261015/mechanical-forest-review/verification-current-rules.json`. These passes do not establish P1909 acceptance, native graph admission or a staged migration packet.

Fresh connected 611-owner preview and staging remain unverified. The first controlled-client attempt failed before any Tool call; `.caprmedio_tmp/stage2-migration-20261015/connected-preview/live611-current-rules-001.json` retains `calls: []` and matching before/after hashes and modes for all 906 sources. The coordinator identified a client SDK timeout-type mismatch and is correcting that client; no preview result or retry outcome is inferred. The Operator's question about one exact 611-owner batch confirmation plus the reviewed map instead of 611 forms/reports remains unanswered. Keep both Epics Active, preserve uncertain staging evidence and no replay, and retain the final graph/packet, exact publication approval and independent reproduction gates. Ordinary content migration remains deferred.

### Current-rule loading and unwanted-rollback regression — 2026-10-15

This supersedes the earlier open self-update/repinning decision. The Operator chose current rule reads without fixed rule-file Version/hash admission and removed redundant post-write checks against the intentionally replaced rule. Keep captured per-operation currentness, exact target pre-write checks, Operator confirmation, exact current/history readback and unrelated-authority checks. Historical Run observations use their saved bindings, not today's rule versions.

Committed `5344c513e` implements the Subject publication correction and current selected-definition/grammar/direct-provider reads. `396e33e46` covers finite validator readers; `e8784a9e5` covers Settings/Scope Query readers; `d7799050b` aligns six non-Core Tool contracts with exact predecessor archives. Independent bounded reviews passed; no live Subject/content migration or runtime replacement occurred.

The requested real functional test is `201_TOOLS/tests/test_subject_rule_self_update.py`: update a rule used by the updater, verify exact successor bytes and archived predecessor, then publish a second Atom in the same process using fresh rule Version/hash evidence. The old implementation reproduced the unwanted rollback; the corrected test passed in 24.096 seconds. All 25 existing publication tests passed in 244.161 seconds, including stale-target, unrelated-authority drift, write/readback failure, owned restoration and no-replay cases. Evidence: `.caprmedio_tmp/stage2-migration-20261015/postwrite-check-removal/`.

The preceding frozen suite at `70bbe1584` ran 370 modules and 3,324 tests with no skips and two failed modules in 1,125.127 seconds. It is not a green result. `c6ba7e406` fixes the release fixture's missing sibling modules and aligns query reconnect coverage with the existing representative policy; focused host tests passed. A new full suite on the current committed implementation remains required. Fresh connected preview/staging, final packet approval and independent migration reproduction remain pending. Keep both Epics Active. The separate per-Atom semantic-assessment decision is not waived by this checkpoint.


### Current implementation and native-preview checkpoint — 2026-10-15

Committed `926abb828` reuses invocation-local validation state without skipping complete validation, final status-frontier readback or finite authority-currentness checks. The producer passed 104 focused tests; a different reviewer passed 36 tests and checked the serialized 611-owner result, all 848 ordered patches and canonical carrier/intent seals. The saved full native preview completed in 155.309 seconds with all 906 pinned Core source digests and modes unchanged. See `.caprmedio_tmp/stage2-migration-20261015/optimized-preview/README.md` and `native611.json`. No full native staging or connected MCP acceptance is claimed.

Committed `d6386df38` delivers fresh-build exact Project ownership/name/full-HEAD image labels and the first safe Git checkpoint followed by clean-worktree verification, with existing environment-file exclusions retained. Cache reuse does not add an ownership claim, and HEAD provenance does not replace source-fingerprint/immutable-image identity. The older full suite at `2ddf5934d` passed 357 modules and 3,269 tests, zero skips and zero failed modules, in 860.112 seconds; log: `.caprmedio_tmp/verification/full-suite-20261015-host-blacklist.log`. It predates these changes. Focused results and this historical suite do not establish a full-suite pass for the current code, deployed activation or release completion.

Next, resolve large-response transport/limit handling and the final graph/candidate packet and approval gates. Native preview took longer than the earlier ninety-second gateway budget. Its preparation result is 3,903,714 bytes; independent review measured the actual SDK-serialized SSE envelope at 9,427,872 bytes because it represents the result twice. The Operator has approved preview/stage budgets of 300/600 seconds and a 16 MiB controlled-client response limit, leaving other limits unchanged. Implementation and tests are underway; deployed activation and connected acceptance remain unproven. The Operator must also decide how exact Subject self-updates of selected authority sources are admitted: 51 manifest-definition owners and two disjoint grammar pins are confirmed examples, not an exhaustive set, because additional validation-authority pins have been found. Current post-effect authority checks otherwise invalidate their own source pins and trigger restoration. Resolve that general policy without blindly refreshing pins or treating preparation as publication approval. Preserve uncertain staging evidence and no replay. P2167 and P1959 stay Active; live application, independent reproduction and the separate content migration remain outside this checkpoint's accepted result.

### Repository-host release and disabled MCP exposure — 2026-10-15

The Operator selected plain repository-host local/public release commands and then clarified that MCP release exposure must be disabled through a tool blacklist while preserving the adapters for later reuse. Use `PROJECT_TOOLS/release.py local|public` with optional `--project-root` (repository root by default), required `--run-id`, and optional public `--content-draft` UTF-8 JSON containing exactly `description` and `summary`; absent public content returns `input_required` without publication. `project_mcp.tool_blacklist` is the optional exact-name setting, with missing/empty meaning no blocked names. This Project blocks `release_version` and `public.release` in discovery and invocation. Preserve full-suite verification including required integrations, Draft public PRs, no merge, plain Journal observations and independent logging failures. Add no registry, Active Atom or prior-history gate.

Public Version `0.4.4` was released to `amm/dev` at `d83dc184d` with Draft PR [#30](https://github.com/anatoly-m-maslennikov/caprmedio-graph-driven-framework/pull/30) targeting `main`; it was not merged. The preceding frozen full suite passed 354 modules and 3,244 tests with zero skips. These observations do not establish acceptance of the subsequent host-entrypoint/blacklist change, which requires its own focused verification and fresh full release suite before another release.

Next, implement and verify this narrow host/blacklist alignment, then resume Subjects-only migration preparation with fresh connected preview, successful fresh staging/readback, current source/grammar pins, final graph/candidate packet checks and exact live publication approval. Preserve both uncertain staging batches; no replay or live Subject/content write is established. This Epic remains Active, and the separate content migration remains deferred. This checkpoint supersedes the earlier pending-public-release status and historical statements that release tools must be exposed through MCP.

The MCP host/gateway reads the blacklist at start or recreation; implementation-only reload does not refresh that Settings snapshot. This source alignment does not itself apply the blacklist to the running gateway or erase retained source contracts, implementations or read-only analysis.

### Green suite, connected refresh and next release gate — 2026-10-14 23:38:44 +0000

Run 11 passed at frozen source `401d19bdcb5fa287683f906662b39fadf68e6e05`: 354 modules, 3,244 tests, zero skips and zero failed modules; terminal exit 0, elapsed 1,012.440 seconds (about seventeen minutes). Log: `.caprmedio_tmp/verification/full-suite-20261015-run11-two-host.log`. The final real-launcher proof reports `completed` at `.caprmedio_tmp/tests/full-suite-integration/attempt-g5f9unsg/launcher-proof-l00yppf3/result.json`. This supersedes the earlier failed-suite checkpoints for current suite status; those records remain historical. The Operator accepted the speed and selected green suite → public release → Subject migration.

The separately approved MCP refresh completed: container `0c00e534a5cbf8a5699597547e367bdf048b1bbd2dbd5a757f618606f9c53bfd`, image `sha256:bc975a18f34e0ea8dbac05b2a9d267363b4d09a66f36ed3bf67a93e274752c2e`, fingerprint `7c8adfb0bcf10e3e69231bcbc821dc24472f6d338f78945941566153da2e3ea5`. `READY_STARTED` then `READY_REUSED` both reported readiness true on port 56317. An actual connected `get_mcp_reload_status` request succeeded at generation `b45c03fe3e644755d9fb05fef1a7aeea35bc77ec255852eec2aebde665975c9b` with zero in-flight requests. All four retained Settings hashes stayed unchanged; Git was clean before this checkpoint.

Next is the public release, pending Operator permission for the host command because the MCP container has no GitHub/Docker runtime. No public release, fresh staging, live Subject write or content migration is claimed. Keep this Epic Active: actual migration capability, fresh connected staging, final graph/candidate packet checks, exact live publication approval and independent reproduction remain open. A green suite and connected refresh do not complete those gates; full semantic W11/W12 completion remains deferred and partial/mechanical graph coverage remains required.

### Run 10 evidence and remaining diagnostics — 2026-10-14 23:05:10 +0000

Run 10 reported 354 modules, 3,241 tests, zero skips and one failed module: selected_workflows_docker_e2e. W02 failed at the inner twenty-second MCP child initialization boundary with timeout/connection closure. W04 enqueue reached the client's twenty-second timeout; its cause remains unknown and no effect is inferred from that timeout. The full suite did not pass, and the roughly ten-minute ETA was not met. Log: .caprmedio_tmp/verification/full-suite-20261015-run10-parallel.log.

The query Docker module's seven tests passed in 391.864 seconds; the HTTP first-cut module passed in 372.048 seconds. Both real launcher groups completed with retained state unchanged. These passes do not establish acceptance of the remaining thirteen Docker execution routes or the full suite.

Bounded fixes are committed as ebe37310e, b84f56f36 and a79dd1e19. A narrow fixture optimization and bounded diagnostic work remain underway, without an acceptance claim. Full semantic W11/W12 completion remains deferred; partial/mechanical coverage remains required. Keep this Epic Active: no live MCP replacement, Core Subject migration, fresh staging, live apply or publication approval follows from this checkpoint.

### Frozen-suite checkpoints and remaining runtime work — 2026-10-14 22:34:51 +0000

Run 8 reported 350 modules, 3,221 tests, zero skips and two failed entries: the selected-workflow Docker module and real launcher CLI. Run 9 reported 352 modules, 3,232 tests, zero skips and three failed entries: query Docker initialization, the supported-route Docker module and the real launcher CLI. Both HTTP first-cut modules passed. Logs: .caprmedio_tmp/verification/full-suite-20261015-run8-parallel.log and .caprmedio_tmp/verification/full-suite-20261015-run9-parallel.log. Neither run passed the full suite or demonstrated a ten-minute result.

Bounded test/fixture fixes are committed as 358574e29, ef3f091be, 81a882af4 and 360c16cfd. SDK startup/list-shape handling and the launcher's minimal capability probe remain in progress. The remaining thirteen Docker execution routes are not accepted until they pass; retain the partial/mechanical graph coverage. Full semantic W11/W12 completion is deferred by the Operator, not silently counted as complete.

Keep this Epic Active. The live MCP and Core Subjects remain untouched. No full-suite pass, runtime cutover, fresh connected staging, live apply or publication approval follows from these checkpoints; the existing Subjects-only/content-migration boundary and outstanding approval conditions remain.

### Current runtime verification and suite reduction — 2026-10-15

The reviewed query pagination fix is committed as afc33e7f1. It admits only the native Artifact pagination handle; other credential refusals and native snapshot checks remain. Earlier local fixes correct isolated Query fixtures, D514 discovery, stdio disconnection before HTTP startup, HTTP cleanup and test scheduling. Focused checks and independent reviews passed; they are not full-suite or installed-runtime acceptance.

Run 6 used frozen source afc33e7f1. It completed 345 test-bearing modules plus one zero-test fixture before being stopped after confirmed failures: the misnamed Git fixture; HTTP W03 test-container startup; one MCP child startup; and four query initialization timeouts. The selected-workflow Docker module and final real launcher did not complete. The log is .caprmedio_tmp/verification/full-suite-20261015-run6-parallel-authorized.log. The ten-minute ETA is not demonstrated. The Git fixture rename is fixed in f6884bbcc; its 23 tests and discovery check pass.

Next: retain bounded startup diagnostics without extending deadlines; move the exhaustive status matrix to real host execution while preserving every assertion and representative Docker coverage; independently review and test these changes before another full run. Do not infer the cause of lost startup diagnostics.

Reviewed scratch contract-currentness and prospective Subject-incidence preparation preserve the 906 owners, 611 change candidates, 848 patches and 29 holds. They are preparation, not the final accepted entity graph. The live MCP and Core Subjects remain unchanged. Both Epics stay Active; fresh connected staging, final graph/packet checks, exact publication approval and reproduction remain open.

### Remove the project-wide Engine write lock — 2026-10-14

The Operator explicitly removed the project-wide Engine write lock without a replacement. Remove its acquisition, hold, contention and lock-error requirements from the affected Tool contracts and implementation; do not introduce another lock or serialization mechanism. Distinct existing resource-specific locks remain unchanged. Preserve path/ownership safety, stale-source and authority rechecks, exact approval and confirmation, the affected-file exclusive window, independent readback, existing Action-local restoration, truthful errors/partial effects and no automatic replay. The model no longer excludes other Engine writers; final revalidation is not a concurrent-writer or crash-atomicity guarantee.

This decision supersedes only the shared Engine lock requirements and claims in earlier checkpoints and accepted-at-the-time receipts. Those historical records remain unchanged. Source alignment is not implementation, independent verification, runtime activation, fresh staging or live publication acceptance. Keep this Epic Active and the Subjects-only/content-migration boundary unchanged.

### Runtime-only tests and current migration preparation — 2026-10-14

The Operator requires the release suite to test executable Runtime and scripts, not the conformance of today's Atoms, generated Projections or Journal data. Remove pure live-content audits from mandatory tests; preserve parser, generator, append/read, protocol, authorization, currentness, failure and no-replay behavior with isolated fixtures. Detach fixtures that borrow changing authority files. Do not delete an entire mixed module or suppress a real runtime failure because it mentions an Atom or Journal. The Operator specifically dropped the unsupported W11/W12 semantic-publication positive test; `77644b081` removes it while retaining malformed/stale refusals. This does not complete the separate semantic graph feature or E555/E556.

Committed runtime progress: `b0f91cb98` removes the native-watch test race (18 tests and three slow-scan repetitions); `2f8951594` uses current query fixtures (five tests); `8147289f2` validates local-release inputs before tests/version/replacement (22 local and five consumer tests); `19df7cdca` aligns the direct-release refusal message (two tests); `7d34fb64b` separates actual effects from Journal logging failures (seven tests). `92d2fca4a` discovers and binds the selected public repository/PR before preparation, tests prepared materials before publication and refuses source drift during the suite (13 public, 11 route and five consumer tests). Its three production modules are 195/121/135 physical lines, with pinned formatting/lint and strict bounded typing checks passing. The graph Tool directory passed all 249 then-current tests without source changes. Independent reviews accepted these bounded behavioral changes, not a complete-suite or live-runtime result.

A new preparation-only request generation is at `.caprmedio_tmp/stage2-migration-20261014/journal-rule-refresh/`. Five meaningful plain-Journal rule updates require current Version/hash tuples: D340, O163, R1491, R1525 and R1720. Their Subjects and mapped meanings remain supported. The new generation preserves 906 owners, 611 change candidates, 848 ordered patches and 29 whole-owner exclusions. Public request SHA-256: `b6e259eb5c9e88d92d47321350a29e627e366cd3a619fb13f4dc883e67d8abd1`; manifest: `8c7f2d5a8a43a8defd02c2746b200f33a34a4e861a6f6757562725be547f7abe`. Earlier requests and staging batches remain unchanged. Author generation, DTO, preservation and failure-mode checks passed. Independent review verified the exact five-tuple delta, all current pins/old Subject values, ordered intents, grammar/DTO provenance and eleven unchanged historical artifacts. This is not preview, staging or application authority.

Bounded implementation-review exceptions retain existing test layout/style: native-watch test file 749 lines, query fixture 211 and Step-input fixture 206 versus the 200-line target; inherited formatting and native bootstrap E402 remain. Changed test units are at most 32 logical lines and preserve one coherent behavior; fixture C901 checks pass. Local-release preflight retains its existing ordered runner: file 703 lines, runner 245 logical lines and C901 58 versus 200/40/10 limits, without increased complexity; existing whole-file formatting/E731 and untouched helper complexity remain baseline. New preflight helpers meet their limits. These specific exceptions avoid unrelated reorganization during bounded fixes, not a general waiver. Reconsider fixture exceptions on the next fixture reorganization, and the runner exception before adding another release phase/branch or during planned decomposition.

The full frozen-source suite, installed runtime verification, successful connected fresh staging, accepted graph/candidate packet, exact live publication approval and independent reproduction remain outstanding. Keep both Epics Active. No public push, PR, live release, restart or Core Subject/content migration occurred.


### Retire the old release and installer path — 2026-10-14

The approved sealed-package release and separate installer source paths, obsolete callers and dedicated tests are retired. `01b82682c` commits the main code/test retirement; `a686fa779` removes orphaned host helpers and rejects the retired host namespace. Normal MCP startup, direct local/public release, ordinary Tool installation, shared current helpers and current integration tests remain. Removed code is recoverable through Git; installed runtime data and prior staging evidence were not removed.

`0ba4e520b` archives 65 obsolete contracts with exact predecessors; `8a8a711d0` and `90b56babe` preserve still-used obligations in mixed rules. `07bbaa9cd` removes the old test harness while retaining required integrations. Independently reviewed focused evidence includes 106 startup/discovery/registry/export/image checks, 51 ordinary installer/shared-helper checks and 17 host-namespace/graph-status checks. The derived ordinary registry validates 15 routes; effect-free source server creation lists 31 tools, including both direct Releases. These are source checks, not installed-runtime acceptance.

The first full-suite run was stopped after its source changed and remains diagnostic only. Current native graph semantic-publication coverage is still incomplete, and previously identified native-watch and fixture failures are not waived. Keep positive current tests; do not delete them merely to obtain a green suite. A fresh frozen-source full suite, including required current-code Docker integrations, must pass before release. Both Epics remain Active. No live Subject/content migration, runtime restart, release or push occurred.

### Verified implementation and diagnostic suite — 2026-10-14 20:37 +0400

This checkpoint supersedes earlier pending-implementation statements, not migration safeguards. The Journal batch limit is approximate under concurrent writes; no append lock is required.

Committed: `fc7378cf8` closes plain Journal callers and the direct release routes; `79d243b73` refreshes approved Subject preparation bindings; `e57745578` requires the full suite and disposable current-code Docker integrations. `5beb029ab` connects exact one-Atom staged Subject publication to the actual connected Codex confirmation form, preserving source checks, the exclusive window and no replay. Independent gateway tests passed, including both Operator-registry drift cases and the existing helper/forwarding paths. `2ca429dbd` aligns reversal rules with plain logging and preserves their exact predecessors.

The two authorized D562/D563 changes are recorded in `.caprmedio_caprmedio/_journal/Codex-2026-10-14-part-1.ndjson`, without baseline rows or an invented Workflow run. Earlier statements that these events were not recorded are historical.

The first full-suite run is diagnostic, not acceptance: it found stale Journal fixtures, old Core source paths, graph discovery/order defects, legacy sealed-release tests and hook-budget failures. `debbf866e` excludes archived predecessors from current graph sources; `d52b4137c` aligns producer/verifier carrier ordering. The actual current Core relation-registry tests passed independently without changing authority pins. `f420fa541` updates two reviewed Journal fixtures. Remaining fixture verification and the generated-bootstrap package-priority fix are in progress. Retirement of old release/installer APIs and dedicated tests awaits the Operator's answer; normal MCP startup must remain supported.

The diagnostic run began before subsequent fixes and newly added tests. A new frozen-source full-suite run, including required integrations, is mandatory before release acceptance. Focused passes do not waive existing Method-conformance gaps or establish installed/runtime acceptance. Keep both Epics Active. No live Subject migration, content migration, runtime activation/restart or push is established by these commits.

### Simplify release verification — 2026-10-14

The Operator chose simple local/public release commands verified by the full test suite, including required integration tests. Missing Docker or another required test environment, skipped required tests, failed tests or unknown completion stops release. Docker integration tests build a disposable image from current code; they do not use an old installed image or restart the running Project MCP. Add no whole-registry, dependency-admission or separate Active Atom metadata, placement or relation validation gate. Repair broken definitions and tests, not a closed seventeen-route successor solely for release. Normal input, permission, target and file/path safety remain. This supersedes earlier release-gate checkpoints; full-suite success is not yet established.

Remove proven-unused Journal validation/recovery helpers and obsolete sealed-release machinery, including their callers, exports and obsolete tests. Do not keep compatibility wrappers or new proof layers without a current caller or requirement. Ask the Operator before removal changes required behavior or risks existing data. Preserve actual source-effect safety, existing files, the uncertain staging batches and the Subjects-only/content-migration boundary.

Local implementation checkpoint: `ed9d4eaba` commits the plain Journal rules and exact predecessor histories; `4af84e77d` removes Journal proofs from installation-command rules. `caa4e05a0` implements plain append/read and Journal-independent Context/commit behavior (12 append/read, 23 Context, 23 disposable-Git, 15 native/adapter and 5 actual MCP protocol checks passed). `99a69741a` removes history prerequisites from graph generation and review recording (50 graph and 13 review checks passed). `9b1b11cc8` prepares the complete local-release payload and candidate image before replacing installed files; independent focused review passed, not full release acceptance. Caller closure, obsolete helper removal, full registry repair and installed acceptance remain open. No live Journal append, Subject publication, runtime restart or push occurred. Existing legacy formatting/size/complexity gaps remain explicit; the focused checks do not waive them.

### Shared Methods, registry repair and plain Journal — 2026-10-14

Use the [compiled PROGRAMMATIC implementation prompt](../../_projection/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/mrt_programmatic_methods_compact.projection.md) in every implementation-worker brief, together with the task's applicable RMEDO. It is a selected derived view, not new authority: small single-purpose modules/functions, pure decisions, objects only for owned state/resources/lifecycle, composition, typed boundaries, and conditional Methods. Recheck its sources when they change. Behavioral test passes do not establish formatting, complexity, size, typing, environment or full Method conformance. The inherited-Method audit found missing evidence and concrete construction/temp-placement gaps; repair and evaluate those without silently waiving the rules or widening untouched legacy scope.

Committed: `9cd9efff9` sets Journal segments to at most 1,000 rows (80 focused tests); `5aabd7a80` exposes the existing independent appender through MCP (17 new native/protocol tests); `aa0fa3e74` requires the complete registry before registration/freeze/new dispatch and removes direct/virtual Release bypasses (18 actual registry/query checks plus 12 isolated interpreter checks independently passed). The real complete fixture has fifteen routes, not seventeen. Known legacy full-suite failures and inherited-Method gaps remain explicit. No runtime activation is established by these commits.

The latest Operator decision supersedes the earlier first-change exception and Journal proof machinery: provide plain append and read only. Do not require previous records, baselines, chain validation, confirmed receipts, deduplication or Journal retry/recovery machinery. The Operator explicitly rejected retaining an extra corrupt-write or duplicate-retry validation layer. Append supplied records and read stored records; repeated appends are not silently deduplicated. Keep the 1,000-row batch limit as approximate under concurrent writes; no append lock is required. Preserve existing Journal files. Align the Journal rules, appender/readers and callers, and remove Journal-history prerequisites from unrelated operations. This does not remove source-change authorization, exact affected-target checks or source-effect no-replay state.

The Operator requires only local and public release. Keep D562's ID and Summary; revise it for installation within local release. Do not create D634 or a separate installer flow. D633 remains the proposed D563 replacement. Direct local recording is allowed for these two actual changes; record those changes without synthetic baseline rows. No D562/D563 publication or Journal append is established by this checkpoint.

Finish release discovery, local source admission and shared dispatch; derive and verify the full seventeen-route registry without restoring obsolete release phases. The approved connected-process exception applies only to confirmed Subject updates, using the actual Codex form and existing validation, locks, selected execution and Journal. Its source packet passed ordinary review; implementation and runtime acceptance remain open. Preserve both uncertain staging batches. Keep both Epics Active: no Core Subject publication, content migration, runtime restart, push or completed-Epic claim follows from this checkpoint.

### Full shared registry repair selected — 2026-10-14 15:42 +0400

The Operator chose to repair the complete shared registry, including release workflows. Do not replace whole-registry validation with per-workflow admission. This expands the prerequisite repair scope, not the Subjects-only migration's target set or the separate content Epic.

Reconcile current ordinary and release definitions before rebinding: distinguish exact relocations, changed contracts and retired steps; do not restore obsolete definitions to satisfy stale pins. Align the required source contracts and receiving implementations, then verify complete workflows and preserved refusal/history/recording behavior. Reuse the existing sealed registry producer/publication lifecycle with a narrowly specified complete successor; retain full-registry and accepted query-frontier validation. An updated hash alone is not compatibility evidence.

Current evidence is under `.caprmedio_tmp/stage2-migration-20261014/registry-repair/`: `current-source-inventory.json`, `ordinary-source-review.md`, `release-source-review.md` and `repair-proposal.md`. Reports/proposal may still be in preparation; they are not admission or acceptance receipts. Prepare the focused FPF design-challenge plan for the full repair and obtain approval before running that review. Actual registry publication, MCP activation, new scratch staging and live Atom migration remain separate approval gates. Existing uncertain staging batches and unrelated working-tree changes remain untouched.

### Accepted Codex confirmation trust model — 2026-10-14 15:28 +0400

The Operator accepted a form response from the connected Codex Session as sufficient confirmation, without separate identity proof, when the form shows the exact source-bound request, selected Session/Run, intended change and affected files and explicitly confirms review and the manual editing/maintenance-script/Git/sync pause. Tool arguments, client names and model assertions never count as that response. This supersedes earlier uncertainty about the confirmation trust choice only.

Build and independently verify the narrow connection to the existing private issuer and selected dispatch in the same process, with a nonserializable one-use confirmation and unchanged public API, route and request fields. Decline, cancel, malformed response, timeout, disconnect, mismatch or bound-evidence drift refuse before effects. Existing source/assessment/permission/Run checks, exclusive window, shared Engine lock and live-publication guard remain binding. This decision authorizes connection work only; it does not approve publication, further scratch staging, runtime activation or restart. Keep P2167 and P1959 Active.

### Fresh scratch-stage uncertainty and next local lanes — 2026-10-14 15:01 +0400

The Operator explicitly approved one new scratch-only CA-D-253 stage from the fresh preview, not a replay of the older uncertain attempt. Exactly one actual MCP request ran with preview seal ea23ecb10f6fbc1f791502b5b5ce7575e35c811febd157850dd5ea88ffcc71ae and its illustrative timestamp. It returned an uncertain error, not a successful staging receipt: Implementation call failed; no automatic replay. Independent readback passed for the exact persisted candidate, canonical manifest, seals and current source/grammar pins. Artifact fidelity is not Tool completion; neither manifest existence nor zero in-flight bookkeeping proves child termination.

Preserve both scratch batches unchanged: the fresh da3108347b2742a0bcdaee211cd184f3 and older e7e1dc30c56941b19c1e8ba0843daae4. All 906 current source pins remain unchanged. A separate read-only post-stage verification lane also confirmed all 12,203 Core Markdown paths/bytes unchanged and all 44 predecessor archives exact; its transcript evidence is identified in tools-first connected-preparation-activation.md, not represented as a filesystem receipt. Exact response, artifact and independent review hashes are recorded there. No automatic replay, cleanup, 611-owner connected acceptance, migration or publication is established.

The Operator requires actual human confirmation in the Codex UI and rejected the proposed terminal confirmation channel. This selects the required interface, not publication authorization. Next independent local lanes are a bounded stage-specific timeout correction with preserved uncertain/no-replay behavior; a no-effect Codex confirmation-form probe that cannot mint publication authority; and investigation of current selected-source readmission without silently refreshing changed meanings or weakening full-manifest validation. These lanes are pending work, not passed implementation, runtime activation or admitted publication.

CA-P-2382, P2167 and P1959 remain Active. Successful connected stage completion, any further scratch effect, runtime replacement and live publication remain separately gated; the new one-attempt approval does not authorize another request. The deferred content Epic remains separate. This checkpoint supersedes earlier unanswered fresh-stage and confirmation-channel statements only; keep their evidence as history.

### Current connected verification — 2026-10-14 14:35 +0400

The Operator approved activating only reviewed commit 920864025 and running a fresh read-only Subject preview. The clean committed image now serves this Project on the same port, 56317; unrelated dirty work was excluded. Actual MCP discovery/context, exact CA-D-253 lookup and its approved-profile preview succeeded. The new seal is ea23ecb10f6fbc1f791502b5b5ce7575e35c811febd157850dd5ea88ffcc71ae; staging is null and no source Atom changed. This is one representative preview, not a 611-owner MCP acceptance result.

CA-P-2384's 44 structural repairs and the fresh 611-owner/848-patch request are complete. Post-preview verification confirms all 906 source pins and the 12,203-file Core frontier still match the verified repair generation. Earlier statements about pending repair disposition and the old running image are superseded by this checkpoint. Exact activation, request/response and review evidence is in the tools-first connected-preparation-activation.md projection.

CA-P-2382 and both Epics remain Active. Preserve the earlier uncertain D253 batch unchanged; neither its replay nor a new stage nor live publication is authorized by the read-only approval. Fresh scratch staging requires separate approval and successful connected/readback proof. Live publication and the separate content Epic remain gated.

### Structural repair before migration — 2026-10-14

The Operator chose to fix all 44 structurally refused Atoms first, rather than exclude them, and explicitly approved direct repository authoring because the connected MCP only supports Subjects preparation. CA-P-2384 owns this bounded repair: headers, section containers and evidenced carrier placement, exact predecessor history, reviewed affected current references, and validation. Preserve Subjects, Summary wording and content meaning. This narrow authorization supersedes earlier staged-only restrictions for these structural repairs, not for Subject or content migration.

After repairs, prepare fresh pinned migration inputs; keep old requests, seals and the uncertain D253 staging evidence unchanged. Do not activate a runtime, replay staging, or publish Subjects under this authorization. Both parent Epics remain Active; broad content work stays in CA-P-1970.

### Connected staging timeout follow-up — 2026-10-14

CA-P-2382's one approved scratch-stage request returned uncertain after about 90 seconds, with matching artifacts written before and after that response. Preserve them; do not replay. Local real-gateway tests now cover successful fixture staging and late effects after an uncertain response (d2740da53; two tests independently passed). No Core source changed and connected success is still unproven.

[CA-P-2383 — Avoid repeated identity parsing in Subject preparation](30-CA-P-2167-EPIC--finish-tools-before-stage-2-execution/done/61-CA-P-2383-TASK--avoid-repeated-identity-parsing-in-subject-preparation.md) is Done locally in 63536837f: invocation-local exact-byte parse reuse retains fresh inventory/currentness and all validation. Fifty-five affected tests and independent code review passed. On identical frozen input, profiled host preview time fell from 77.301 to 51.661 seconds with the same seal and fresh-read counts. The fix is not activated; CA-P-2382 remains Active for connected verification. No timeout increase, live replay, broad tool rebuild or content migration. The 44-owner disposition and publication remain separately gated.

### Connected activation and request readiness — 2026-10-14

The Operator approved narrow MCP activation. Reviewed commit 15f9ce76e now runs in the Project MCP HTTP container on port 56317; unrelated dirty work and other services were excluded. Actual discovery and execution context report ATOM_SEARCH and ATOM_UPDATE as available through MCP with complete context. [Connected activation evidence](../../_projection/core-entity-review/stage2/tools-first/connected-preparation-activation.md) records exact image/container fingerprints and the distinction from installed-package release or operation execution. This supersedes the earlier unanswered activation question.

[CA-P-2381 — Prepare logical Subject preview request](30-CA-P-2167-EPIC--finish-tools-before-stage-2-execution/done/59-CA-P-2381-TASK--prepare-logical-subject-preview-request.md) is Done: all 611 owners and 848 ordered patches retained; four tests and independent exact conversion/source-pin review passed.

Current-carrier structural checks pass 567 targets and refuse 44 for pre-existing placement, property, section or Type issues. Keep the frozen mapping/request unchanged. The Operator has been asked whether to hold those 44 and stage only targets accepted by actual MCP preview; no answer or structural/content repair is inferred. Live publication remains separately gated, and both parent Epics remain Active.

### Direct preparation locally complete — 2026-10-14 11:12 +0400

CA-P-2379 and CA-P-2380 are Done for implementation and local protocol acceptance, committed as 15f9ce76e. Independent review passed after correcting exact no-op timestamp equality and hidden live/dangling role-directory links. Final checks: 48 native guards/staging/identity, seven provider, sixteen existing preview, eight protocol cases (seven real transport plus one CLI), and 43 publication compatibility methods. The compatibility increment 7d015c24e changes only four source-pin pairs and one expected Version literal. Root reran the provider and existing preview checks together: 23 passed.

[Direct preparation local completion](../../_projection/core-entity-review/stage2/tools-first/direct-preparation-local-completion.md) records the boundary and hashes. Connected MCP discovery sees D425 v16 but ATOM_UPDATE remains unresolved; the old running image has not loaded these providers. No Core staging, migration, source publication, Session, Journal or installed-package update occurred.

The existing narrow activation route builds an image from a clean reviewed commit, replaces only this Project's precisely attributed MCP HTTP container, then reconnects. The Operator has been asked to approve that interruption using commit 15f9ce76e, excluding unrelated dirty work and other services. No answer or activation is inferred. Selected-package acceptance, live publication and the wider Epic remain open. Keep CA-P-2167 and CA-P-1959 Active.

### Direct preparation rules accepted — 2026-10-14 10:56 +0400

CA-P-2378 is Done: six independently verified sources are committed as ef3bde3c6. The accepted contract exposes only preview_subjects and stage_subjects through the existing ATOM_UPDATE provider, not live update_atom. The native helper itself checks the reviewed preview seal before scratch creation. Existing publication and actual Step recording duties remain intact.

CA-P-2379 implementation and CA-P-2380 protocol verification now proceed in parallel with isolated fixture-pin compatibility. Prepared tests are not passing evidence. No installed runtime activation, live source migration or Core/content change is claimed. Both parent Epics remain Active.

### Discovery accepted; direct preparation next — 2026-10-14 10:38 +0400

CA-P-2373 is Done. Fixture-only commit `dea79c410` restores the current selected-route and retired-source checks without changing production behavior. All 68 affected checks pass; Root independently reviewed the diffs and reran 63 checks. The earlier baseline failures are superseded for those suites. Installed runtime activation is still unverified.

Direct preparation proceeds through these bounded leaves:

- [CA-P-2378 — Align direct Subject preparation rules](30-CA-P-2167-EPIC--finish-tools-before-stage-2-execution/done/56-CA-P-2378-TASK--align-direct-subject-preparation-rules.md).
- [CA-P-2379 — Expose direct Subject preparation](30-CA-P-2167-EPIC--finish-tools-before-stage-2-execution/done/57-CA-P-2379-TASK--expose-direct-subject-preparation.md).
- [CA-P-2380 — Verify direct preparation MCP](30-CA-P-2167-EPIC--finish-tools-before-stage-2-execution/done/58-CA-P-2380-TASK--verify-direct-preparation-mcp.md).

Production adapter edits wait for independent source acceptance; transport test preparation can proceed separately. Keep the source map and prepared request unchanged. This closes neither the wider Epic nor live publication and installed-readiness gates.

### Direct preparation route approved — 2026-10-14 10:34 +0400

The Operator answered Yes to separate direct MCP preview and staging calls. Reuse the existing Subjects-only preparation helpers: preview leaves source Atoms unchanged; staging writes reviewed candidates only under `.caprmedio_tmp`. This supersedes the unanswered route-choice checkpoint below. It does not approve live publication, waive current source checks, select a recording policy implicitly or authorize installed runtime replacement.

Next, define and independently review the narrow preparation request/result and source packet, then implement the existing-helper adapter and actual MCP transport tests. Keep scratch effects distinct from an Atom update or lifecycle event. Resolve only concrete remaining contract decisions; do not reopen the approved direct route. In parallel, repair evidenced outdated discovery fixtures without changing production release behavior or weakening negative checks. Ordinary content migration remains separate.

### Direct Subject lookup locally complete — 2026-10-14 10:24 +0400

CA-P-2369 and CA-P-2374–2377 are Done for their bounded proposal, rules, reader/provider and local MCP transport checks. The independently reviewed implementation is committed as `2a40cb4c8`; rules are `8186f93a4`, and Session receiver pin compatibility is `e75005fe0`. Final checks passed: 71 ATOM_SEARCH tests, 10 real MCP protocol tests and 55 affected Session tests. Two review findings were fixed: Project boundary/provenance revalidation and selected directory symlinks falsely appearing as empty results. Four adjacent unchanged O199 tests still fail before invocation on an absent legacy fixture; no full-suite success is claimed.

The local reader returned 127 active Core matches with full coverage and zero diagnostics; all 906 Core sources and Settings/Structure stayed unchanged. [Local completion receipt](../../_projection/core-entity-review/stage2/tools-first/direct-subject-lookup-local-completion.md). No Subjects, ordinary content, Journal or migration candidate was changed by this verification.

Installed readiness remains open: the connected Docker service has not been rebuilt or activated with this code. The Operator has been asked whether preview/staging should use separate direct MCP calls that preserve source Atoms and write candidates only to `.caprmedio_tmp`; that decision is unanswered. Lookup approval does not authorize it. Live publication still needs its real human-confirmation connection and applicable admission/manifest decisions. Keep this Epic and CA-P-1959 Active; content migration remains separate.

### Read-only lookup decision — 2026-10-14 09:50 +0400

The Operator answered Yes: Subject lookup may return matching Atoms and source hashes directly, without a Workflow Session or Journal records. CA-P-2369 resumes its bounded interface work, followed by independently checked rules, implementation and MCP verification. Reuse ATOM_SEARCH and the current reader/matcher; do not manufacture authorization/context records or waive root/source validation. Mutation safeguards, staging/publication decisions and the current manifest contract remain unchanged. The unanswered-lookup statements in earlier checkpoints are superseded; both parent Epics remain Active.

### Installed readiness checkpoint — 2026-10-14 06:26 +0400

Actual MCP discovery still returns zero Subject Tools; CA-O-030 context has no input/output schema or Tool description. A serving generation with zero in-flight calls was observed; no reload or execution was requested. A responding MCP is not usable Subject migration.

CA-P-2373 implements the independently reviewed native-Action discovery correction in commit `0a853fe5a`. The shared catalog associates source-admitted native_action_calls with the existing exposed route, without a standalone Action endpoint or weaker source checks. Four new regression tests pass. Nearby suites retain ten unrelated failures/errors reproduced with the pre-change method; P2373 remains Active rather than claiming its full existing-suite condition passed. No installed activation is claimed.

Three bounded read-only checks identified the remaining delivery decisions:

- The selected loader validates the whole 15/16/17-route portfolio before route selection. All six direct update_atom source paths are obsolete; five sources also changed, while O145 is an exact-byte relocation. Existing D588/D592 repair registrations do not authorize current reconciliation. Fixing only update_atom cannot satisfy the current full-portfolio contract. Do not refresh hashes blindly or silently broaden this Subject-only work to all routes.
- Existing update_atom enters completed O145/O067 assessment and lifecycle recording before its native update. Scratch staging cannot use that unchanged execution path or be hidden inside read-only preview. Direct preparation exposure needs explicit shared admission/recording policy; retaining the selected route needs a genuine preparation branch. No speculative contract or adapter was adopted.
- The private publication confirmation issuer has no production human-confirmation provider. The installed MCP SDK supports elicitation, but the current gateway does not forward it and an elicitation acceptance alone may be agent-generated. Do not manufacture consent from request JSON, test fixtures or a generic acceptance token.

The read-only lookup Session question remains first and unanswered. Resolve subsequent delivery choices one at a time. Evidence reports are temporary under `.caprmedio_tmp/stage2-migration-20261014/tool-readiness/` (manifest-reconciliation, preview-staging-exposure, host-confirmation-readiness and mcp-current-observation). These observations do not authorize publication, source migration or broad legacy repair. Parent Epics stay Active; the prepared Subject request and unchanged-owner exclusions remain intact.


### Current execution order — after Subject mapping

The Operator confirmed that the complete Subject map under CA-P-1959 comes first. This Epic's remaining MCP integration work follows mapping; it is not a prerequisite for preparing or resolving the map. This supersedes older tools-first sequencing for that read-only work. Completed local Tool Tasks remain Done; this Epic remains Active.

After the map has complete current source/occurrence coverage and no undisposed migration question, including explicitly approved whole-owner unchanged, deferred and retirement dispositions, perform only these migration-readiness tasks. Open meaning questions stay visible and their whole owners remain unchanged; they do not block supported owners:

- Repair the relevant MCP discovery/bindings and expose the existing field-aware `governs`/`depends_on` lookup. Verify that an actual MCP request returns the expected source-pinned matches.
- Expose the existing sealed Subjects-only preview and staging path. Verify staged output through MCP, with no authoritative source changes.
- Connect the existing publication authorization to real Operator confirmation for the exact reviewed change and exclusive window. Preserve stale-source checks and refusal without confirmation; request data must not manufacture permission.
- Support mapped `depends_on` values that converge on one target. Preserve one resulting dependency, unrelated bytes and source pins; propagate the exact effect through preview, staging and apply checks. Check and narrowly align affected RMEDO before implementation.
- Test the complete MCP path on isolated fixtures: lookup, preview, staging and approved apply, plus stale-source refusal, missing-confirmation refusal and converging dependencies. Verify Version/history/Journal effects and unchanged ordinary content.

Reuse existing implementation and existing child work where it fits; split remaining implementation into bounded leaves before execution. Do not reopen completed local Tasks merely because installed integration is missing. General connector rebuilding, configuration/type catalogs and content migration remain deferred. Completion is evaluated against this bounded migration-readiness scope; unrelated deferred children do not block this slice. Passing its checks does not authorize live Core migration or complete CA-P-1959's application/reproduction gates.

The current MCP assessment verified status/discovery responses, not usable end-to-end migration. Relevant binding evidence is invalid and the trusted-host publication provider is not configured. Explicit full-set dependency replacement is now locally verified; duplicate final values still correctly fail. The approximate 2–4 engineering-day estimate is provisional, not an execution deadline or acceptance criterion.

### Verified local Tool increment — 2026-10-14 06:09 +0400

P2367, P2368, P2370, P2371 and P2372 are Done with independent acceptance of their bounded outputs. D531 v5 now matches the accepted Subject patch shapes. Explicit depends_on complete-set replacement is implemented and sealed through the shared planner; same-membership requests preserve exact source bytes. Seven dedicated author tests, 49 prior local regressions, eight independent tests, 39 repaired selected apply/recovery tests and three actual isolated selected full-set publication tests passed. These prove Version/history/Journal effects and refusal for a changed intent or reviewed candidate, not installed MCP readiness.

The reviewed temporary request packet contains 611 Atoms and 848 patches (346 governs; 502 complete dependency sets). It preserves the 266 unchanged and 29 excluded owners; six builder tests plus independent coverage/source/stale-state checks passed. Request SHA-256: `a4f6b8b6083e8c054837dc7b03b3ae2f1500f9c429cfaa50917ae48cdac6fade`. All 906 original Core source hashes remain unchanged. Request preparation is not candidate staging, application or approval.

P2369 remains Active. Its narrow lookup-exposure proposal exists, but the Operator question is still open: direct read-only MCP lookup without Workflow Session/Journal records, or the current started-Session receiver requirement. Do not adopt either new policy silently. Other remaining installed gates are preview/staging exposure, truthful selected-manifest reconciliation, real host publication confirmation and an actual MCP round trip. Separately approved live Core migration and ordinary content work remain outside this increment. Keep both parent Epics Active.

### Current mapping and MCP checkpoint — 2026-10-14

The current map at `.caprmedio_tmp/stage2-migration-20261014/subject-map/subject-map.current.json`, SHA-256 `647f7a91ca166a9cfd08560f1303cfb2cc7d2724848dc50794cd1eee78e062f8`, covers all 906 current owners and 4,530 occurrences against Candidate #4 `a23019a1ee6cd3586640d6c3d9e211091f3683ac5f136058d745650570e78ca7`. Independent ledger verification passed: 611 change candidates, 266 unchanged, 17 deferred-model owners, 10 uncertain owners and 2 pending retirement. All 29 excluded owners stay wholly unchanged, including their otherwise supported changes. The 34 null mappings and 11 open meaning questions remain recorded; zero migration occurrences lack a disposition. This satisfies the mapping-disposition gate only. It neither resolves excluded meanings nor authorizes staging or live effects.

MCP discovery and context reads respond, but relevant execution bindings remain unavailable. The selected-route manifest references removed Core source paths; do not repair it by blindly substituting paths or accepting changed bytes. ATOM_SEARCH and ATOM_UPDATE preview/staging are currently local-only contracts, with no MCP binding. Existing code is reusable but not installed readiness.

Next, narrow the existing lookup and preview/staging contracts for the requested MCP exposure, then independently check the actual packet before implementation. Lookup must honor the selected PRMEDO frontier without requiring deferred C/A repair. Keep search and modification independent. Dependency convergence needs explicit narrow rules and tests because the current preview rejects duplicate results. Use bounded existing children or new leaves; keep live publication confirmation, source checks and the standalone apply guard unchanged. Do not use a local invocation as a substitute for the requested unavailable MCP operation.

For convergence, first reuse the explicit complete-set replacement already required by R1934/D623/D425: the reviewed packet names the exact current dependencies and the explicit duplicate-free proposed set. Prefer implementing this missing shape over adding implicit Tool-side merging. Verify the combined current contract and byte-preservation tests before implementation; generic duplicate-result refusal stays intact.

### Current continuation checkpoint — 2026-10-14 00:22:57 +0400

The Operator deferred Tools for Content Roles, Types and Labels, including a YAML source of truth for allowed Types, allowed and mandatory Properties, fractal nesting and Status models. No implementation, adoption or executed FPF review is claimed. The current work is only what is necessary for Subjects migration: current-source mapping, Subjects-only preview/staging, independent diff and graph verification, and separately approved exact application. Unrelated connector rebuilding, Draft lifecycle work and configuration/catalog changes are deferred; they must not be treated as migration prerequisites without a demonstrated dependency. Preserve the unfinished Draft repair without claiming acceptance. The broader Epic remains incomplete; its original DoD and prior checkpoints remain unchanged. Atom content migration remains separate.

### Current continuation checkpoint — 2026-10-14 00:05:19 +0400

Seven Carrier v4 relation-only source revisions are committed as `ed5de3af6`. E633 and O215–O217 passed admitted PRMEDO checks; R1941/M381/D630 remain blocked only by the known invalid Type fields awaiting the Operator's answer. This is source/rule work, not implementation, production pin adoption or live writes. Passing E633 acceptance still requires real receiver enforcement and verification; mock writer callbacks do not establish readiness.

Journal receipt-integrity correction `d7465c6b9` refuses canonical-digest tampering and orphan cache evidence. Independent code review passed; Root's fresh Journal 28, Appender 28 and Commit 25 checks all passed. The old 11-`operators_registry` fixture-error checkpoint is superseded by the final canonical lifecycle fixture committed as `b86b323ba`, SHA-256 `6c84bf55e63654d0365ee79374102dacde0bc290e4120bc8cbd3b9f7159b0c97`: author 34 checks, independent fixture review and fresh 34-check rerun (12.457 seconds) passed on unchanged pins. Historical notes remain unchanged; fixture repair grants no broader source/runtime acceptance.

Keep this Epic and all broad parents Active with the original DoD. P2294/P2253/P2301 retain unfinished descendants and are not closed or cascaded. R805 v25/D010 v24 require lease expiry/fencing, but the trusted deadline source remains a later one-question gate: R1385/O037 envelope end is only a reuse candidate, and `wait_seconds` is not a lifetime. The three Type-header question remains pending. Generic Property/Section receiving, raw renderer/literal publication and other wider gates remain open. No new Settings caller integration, live migration, Task or closure is inferred.

### Current continuation checkpoint — 2026-10-13 22:13:02 +0400

Ten bounded Tasks are now Done: P2270/P2302/P2303/P2304 after current 23-release/49-graph verification, and P2325–P2330 after independent exact cleanup/history reconciliation and current finite PRMEDO source admission. No source cleanup was repeated. See graph-and-direct-release-completion.md and bounded-cleanup-task-closure.md in the tools-first projection evidence.

The shared actual-Session admission helper and private O212/O218 read receivers are implemented and independently checked; all 264 connector tests passed. P2340/P2341/P2300 stay Active because the production complete Settings validator and remaining receiving branches are not complete. This packet registered no new route or runtime capability.

Latest Operator decision: build only the new no-legacy Settings reader. Do not migrate either Settings file, remove legacy fields or migrate existing callers now. The proposed preserve-unknown/legacy reader is not accepted. Define and independently review the narrow closed current Project schema, then implement and test the new reader; the existing legacy-rich carrier must receive truthful unsupported-field diagnostics rather than silent compatibility.

MCP initialization still fails and no server listens at the configured port. The two live Settings observations remain unregistered; direct writing is not authorized. Current lifecycle binding also needs real canonical-registry reconciliation (95 missing and 15 stale paths among 162 unique pins), not blind pin replacement or another unapproved historical-repair exception. Explicit Draft identity/source conflicts and actual cascade execution remain open. Keep this Epic Active.

### Current continuation checkpoint — 2026-10-13 21:40:47 +0400

P2336/P2337 single-Atom Status publication, P2344/P2345 nested Operations placement, P2342/P2343 typed Plan blocking admission, P2346/P2347 prerequisite closure and P2352/P2353 retained reference proof are Done after independent final-pin checks. All 433 validator tests and 33 independent publication/placement tests passed. Actual P2264 v6, P2256 v6 and P2272 v7 passed finite admission unchanged. Namespace and after-lookup mutation defects found during review are fixed, not waived.

P2348/P2349 Settings observation rules and P2350/P2351 graph receipt reading are Done; all 46 graph-generator tests passed. Both Settings files and the live Journal remain unchanged. Actual two-record registration still needs an available admitted route or the Operator's explicitly requested direct-writer choice. A successful reconnect is not yet verified: the observed endpoint still failed initialization.

Next Status work is current selected lifecycle binding review (P2338), explicit Draft identity (P2339), then actual independently executing cascade. Complete Settings/schema receiving admission, other Epic children, PROJECT_TOOLS relocation, runtime activation and live Subject migration are not closed by these checks. The Epic remains Active.

### Continued independent work — 2026-10-13

Keep the whole Epic open. CA-P-2315 repairs graph authority lookup; CA-P-2299 completes source-bound section preparation; CA-P-2316–2319 decompose contained Status work; CA-P-2320–2323 align the chosen Settings filename and shared Project boundary checks. Each slice has its own independent evidence; none substitutes for receiving, portfolio or runtime completion. Legacy source migration remains a separate Operator decision, not an automatic exclusion or normalization.

### Admitted lookup and contained Status changes — 2026-10-13

CA-P-2314 now follows the completed FPF design challenge `workflow-carrier-whitelist-d96b9733` and the Operator's follow-up decisions. Discover references through declared Scope Unit and selected Project roots, declared Content Role/Status placement, and authenticated same-stem Plan/Workflow/Step containers only. Unknown folders cannot supply targets or Plan parents. Legacy noncanonical `archive/` layouts stay excluded; their migration is separate later work.

Every parent Status change cascades to all contained latest P/O Atom versions, including nested Tasks/subtasks and Steps/substeps. Preserve nesting, older historical revisions and referenced Atoms outside the tree. Cascade means explicit independently admitted per-Atom changes through a Workflow, not inferred read-time Status or a new multi-target atomic connector. Current lookup work does not implement these mutations. CA-P-2264 owns the later lifecycle implementation and bounded tests, including single-target adapter compatibility, actual Version/history/Journal effects, and any unsupported child Status refusal. No new Status values, automatic retry or live migration are inferred.

Accept the narrow amended source packet independently before binding it in lookup. Then verify the helper, caller, exact sources and admitted-frontier currentness. Source acceptance, a completed review and focused tests do not close the whole Tools Epic or establish installed-runtime readiness.

### Local Subject application completed — 2026-10-13

CA-P-2179–2182 and their parent CA-P-2173 are Done after independent local acceptance. The remaining byte/effect ledger and actual recording-only recovery checks passed. Broader regression tests found and then verified the fix for a forbidden standalone update creating a lock file before refusal. Final evidence: 119 distinct Subject checks and 26 generic Atom Operations checks passed. [Completion receipt](../../_projection/core-entity-review/stage2/tools-first/subject-publication-local-completion.md).

This Epic and CA-P-2174 remain Active. The completed Tasks excluded installed runtime/image/manifest activation; provider absence is not unfinished work in those local Tasks. Installed readiness, other connector/Workflow work and separately approved Core migration remain open. Earlier local Active/deferral statements below are historical and are superseded by this checkpoint.

Own work: none. Complete this group through its bounded children. Historical Done Tool Tasks remain Done; this group covers only the remaining gaps.

Review and update three bounded contract packets first: patch-preview currentness, public graph notation/profile selection, and admitted Subjects-only application. Bind each packet to its actual declared Engine scope and current source pins. Preview and application share UPDATE contracts CA-R-866/CA-M-371/CA-E-304/CA-D-425/CA-O-030: one file owner serializes their source changes, then re-pins and independently re-verifies affected packets. CA-P-2171 independently verifies each actual updated packet before its affected implementation. CA-P-2174 independently checks the resulting implementation on isolated fixtures before this group unblocks full source implementation/use. Read-only staged preparation uses CA-P-2183's separate independent receipt; no branch may consume unfinished Tool capabilities.

Reusable Tools operate valid files only. Reuse the existing lookup, sealed preview, graph entry point and governed mutation boundary; do not create another Atom engine or general repair/migration framework. Preview selects eligible current NON-ARCHIVED originals, not literal `Active`, and preserves intended Status. The public graph entry point binds an explicit approved notation profile; legacy/default behavior stays separately checked. The admitted route must enforce exact sealed approval, current pins, Subjects-only effects, Version +1, actual Project-time metadata, prior history and required actual Journal records. Keep the existing standalone apply guard until an intentional contract-governed route is implemented; never bypass it or fabricate admission/receipts.

This group grants no live Core effects. CA-P-1909–1912 retain the sole final accepted graph, sealed preview, application and reproduction route. CA-P-1966's read-only current-source adaptation/re-pin for staged candidates requires CA-P-1963 and CA-P-2183's receipt, not the full publication gate. Live application needs CA-P-1910's separately Operator-approved exact packet; changed pins require a new preview. No ordinary Core content, carrier rename, native Relation admission, release or runtime activation is included.

The latest scope is Subject migration only. Terms compilation, identity/filename and Applicable Methodology adoption belong to the separate deferred CA-P-1970 Epic; they are not this group's work or completion gates. The staged branch changes only Subjects and required illustrative Version/time in candidate copies, never source content.

The Operator chose extending the existing admitted MCP update action with Subjects-only application. CA-P-2170 aligns the chosen route's current contracts, then independent packet acceptance gates bounded CA-P-2173 implementation. No local exception, completed capability or live packet approval follows from the choice. Final Tool readiness still requires actual application implementation and independent fixtures.

The later concurrency safety choice is deferred, not approved. Live changed-Subject writes remain blocked pending a later publication design and actual acceptance/verification under CA-P-2179. No exclusive-access requirement, quarantine policy or atomic exchange is inferred. Completed safe preview, pure materialization, no-op and isolated integration evidence do not complete successful publication, the application portfolio or this Tool gate; accepted RMEDO remains binding.

CA-P-2183 adds a bounded non-publishing staging path: opt-in local `ATOM_UPDATE run --stage-preview`, existing `proposed_carrier`, a fresh generated `.caprmedio_tmp/subject-preview/<id>/`, and re-read/validation. Its independent receipt plus CA-P-1963 release read-only current-source adaptation/re-pinning/mapping solely to create and review staged candidates; they do not require this group's publication receipt. Full source implementation still requires this group, and final accepted graph/sealed live packet, effect-time execution and separate content work retain their own gates. Tool RMEDO and Plans are updated normally; migration candidates stay staged. Actual implementation waits for independent verification of the updated, accepted governing RMEDO.

One integration owner controls shared state and Git. Parallel edit scopes must be disjoint; overlapping contract/source changes are serialized and re-pinned. Each own-work leaf fits 15 minutes; split a larger packet before execution. Preparation alone never completes an implementation group.

CA-P-2192 corrects only original-identity competitor classification: existing MethodologyLayout/ProjectStructure distinguish installed framework copies from authored originals. It adds no currentness exemption, installed-target admission or new policy. Actual contract adequacy, focused preservation/duplicate regressions and separate independent verification must pass before affected preview/staging use. No installed-source cleanup/mutation or live publication is included.

### Prospective logical connector and Workflow rebuild

The latest approved rebuild uses logical storage-neutral connectors. File/database representation and backend details are private; no database build, code implementation, runtime activation or live capability is authorized by these source edits. Author only the approved rebuilt RMEDO in the two newly approved FEATURE authority roots, not delivered/installed copies or unrelated legacy TOOLS. CA-P-2245–2247 own the serialized source packets; CA-P-2248 independently accepts their actual revised sources, exact predecessors and current pins before affected implementation. An author cannot accept their own packet.

The Operator now authorizes exactly two Unordered FEATURE siblings under PROGRAMMATIC: CONNECTOR_TOOLS and TOOL_WORKFLOWS, both Structural Level 3, with navigation numbers 5 and 6. Their authority roots are `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/305_FEATURE_CONNECTOR_TOOLS` and `.caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/306_FEATURE_TOOL_WORKFLOWS`. Their future, currently unmaterialized Implementation Folder bindings are `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/305_CONNECTOR_TOOLS` and `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/306_TOOL_WORKFLOWS`. Root alone owns the Project Structure additions. Existing TOOLS, its unrelated legacy authority/children and every existing delivery row/code path remain unchanged; this split covers only the rebuilt RMEDO packet, not a general legacy Tool rebuild.

Keep flat Content Role folders inside each new authority root: `04_requirement`, `05_method`, `06_evaluation`, `07_delivery` and `09_operations`. Shared general policies have Local Tier Core within their owning FEATURE; do not create extra CORE Scope Units or an additional grouping layer. Rebind only the approved rebuilt sources and their current owner/target/tier/filename/reference evidence under the assigned semantic mapping; historical receipts and archived sources remain unchanged. The latest authorization supersedes the earlier prospective "no new Scope Unit"/TOOLS-only restriction for these two declarations and this rebuilt packet only.

The coherent common interface is API in the broad logical sense, not a new transport or server. Connector Core CA-R-1936/CA-M-376/CA-E-628/CA-D-625 define common logical input, result, precondition, error and effect contracts for ALL connector Tools, with operation-specific refinements that do not contradict that shared contract. Workflow composition policies, including the affected CA-R-1093 contract, belong at Core within TOOL_WORKFLOWS. No transport, database, retry/resume or concurrent-publication design is selected; the retained independent Find/Read/Modify and per-Atom safety/stop behavior still apply.

Fresh source acceptance is not current code readiness. Later bounded implementation must address authority consumers with hardcoded source paths, release/admission bindings, selected-execution refresh and seals/pins, and the graph generator's incorrect delivery-path derivation rather than its explicit declared binding. Legacy Core change-class/archive alignment remains separate under the content Epic, and actual runtime/admission plus independent fixture acceptance must pass before affected use. Until those gates pass, the new delivery folders are unmaterialized, existing code stays at its old physical paths, historical accepted pins are not current acceptance, and no live capability or migration readiness is claimed.

The approved connector/Workflow behavior is:

- Find, Read and Modify are independent generally; createAtom and createSU are available as distinct actions. Reuse the existing read Action CA-O-047. findWorkflow and modifyWorkflow are independent, rather than a compulsory find/read/modify chain.
- No Atom deletion is provided: archive only. Any Summary change, including wording-only, requires a fresh Atom ID and archival of the predecessor; a property Tool must reject a same-ID Summary change. Replacement reports the requested target, created successor and archived predecessor IDs, for example target 100, created 200, archived 100. It does not automatically retarget references.
- Every actual changed same-ID Atom update, including a Status change, increments Version by exactly +1 and uses the actual Project-time Updated At. An exact no-op retains both Version and Updated At. Any Summary or Type change requires a fresh Atom ID and predecessor archival, not a same-ID update.
- A shared section-edit family adds, replaces, removes, renames a title and orders sections. Property-list edits select one item by VALUE, never by index, or replace the full set; add and remove are approved.
- A shared TOML connector serves distinct Project Structure and Project Settings Workflows, each with its corresponding schema checks; one config's Workflow does not substitute for the other.
- Subject search explicitly selects `governs`/`depends_on`, scope and exact/prefix/suffix/contains matching.
- Every Atom action is independent. Across multiple requested actions, stop at the first failure: successful earlier actions remain, and remaining targets are untouched. No cross-Atom all-or-nothing batch or rollback is admitted. One-Atom action safety, exact identity/currentness, authorization and truthful effects/recording remain binding. Resume/retry is explicitly DEFERRED, and no automatic continuation/replay is inferred.

These are retained Operator instructions for the prospective Engine contracts, not a claim that all existing Core contracts already agree. Core change-class/archive contracts may still differ and are not edited by this packet. Their later Core/content-Epic alignment and the separate executable admission gates remain required before affected use; source authoring grants no global conformance or live Tool capability.

The allocated new contract sources are CA-R-1933–1936 and CA-M-372–376, CA-E-625–628 and CA-D-622–625 plus the CA-D-425 revision, and CA-O-201–210. Operations scopes are CA-O-201 Find targets Workflow, CA-O-202 Modify explicitly selected targets Workflow, CA-O-203 Create Scope Unit Action, CA-O-204 TOML patch Action, CA-O-205 Project Structure Workflow and CA-O-206 Project Settings Workflow, with the required Steps CA-O-207–210. Reopen the actual resulting carriers and any affected existing contracts; these allocations are not accepted source pins or completed capability.

This section is the prospective execution input for this rebuild. It supersedes conflicting older executable assumptions in CA-P-2173/2174 and CA-P-2179–2182, including compulsory recovery/continuation work, scalar-indexed edits and cross-Atom all-or-nothing behavior. Existing receipt links, accepted-at-the-time source pins, Done statuses and historical results remain unchanged. Affected historical acceptance cannot be silently rebound to new bytes or used as new-design readiness.

The deferred concurrency/publication follow-up stays with CA-P-2179. No concurrent-write mechanism is chosen or enabled, and valid approval alone does not release the existing live changed-Subject gate. Deferred resume/retry is not an implicit additional implementation policy. Safe preview, no-op, pure materialization and non-publishing staged checks remain bounded evidence.

The Operator authorized completing CA-P-2249/2250 and their separate independent acceptance, then resuming CA-P-2251's retained approved read-only FPF review. Both authoring Tasks are now Done after actual different-reviewer PASS; CA-P-2251 is Active against 98 accepted current RMEDO sources (81 + 10 + 7), with current approved Plan/approval binding at continuation. This records review readiness, not an executed analytical result. This instruction authorizes no implementation, runtime capability, Core/configuration change, migration or live publication; CA-P-2252–2278 remain pending. CA-P-2249/2250 first author the missing Scope Unit Query/Read and private carrier operation contracts; each actual packet requires a different independent reviewer and accepted current/predecessor manifest. Packet readiness permits review while its author Task is Active, avoiding a circular Done-before-review prerequisite. Current acceptance of 81 sources under CA-P-2245–2248 is bounded evidence, not all future required RMEDO.

CA-P-2251 then performs the fresh FPF review only after ALL required rebuilt RMEDO has actual independent acceptance. Show the current review Plan and obtain explicit Operator approval first; bind the final Plan at execution. The intended single `$fpf design challenge` is read-only, without automatic fixes, adoption or report saving. Plan-validation PASS is not analytical execution. Findings require corrections/questions and renewed acceptance/re-review as needed. Split the actual review into <=15-minute executed portions before running if required.

Dependency order is contracts/independent acceptance (2248–2250), approved FPF review (2251), shared connector implementation (2252), logical connector adapters (2253–2258), receiving Workflows/lifecycle/configuration/recording (2259–2268), and actual placement/authority/admission/selected-seal/graph-binding compatibility (2269–2272). Explicit BLOCKS and required current accepted manifests govern start; Work Sequence and folders do not. Independent verification children 2273–2278 may prepare read-only fixtures early but accept actual stable implemented pins only. Every pending leaf below is linked, including the six children owned by existing CA-P-2174, with no duplicate verifier group.

Existing CA-P-2173 covers only its admitted Subject application outcome and reuses CA-P-2179–2182; it does not implement the whole rebuild. Subject rename is receiving use of explicit Property edits/CA-O-202, not a new Workflow family or native relation. Private file/folder mechanics cannot delete Atoms or expose physical backend targets. Scope Unit rename/move reuses CA-R-1829/CA-O-015 and adds no Scope Unit removal. Applicable conflicting Core policies require separate accepted alignment under CA-P-1970, not global content migration in this Epic. Preserve older admitted commit-domain recovery while batch retry/resume stays deferred.

Every own-work leaf remains <=15 minutes, with actual disjoint outputs and fresh independent positive/negative fixture proof before affected use. These pending Plans grant no implementation execution now, release/runtime activation, live Subject publication or migration approval. Existing shared final migration, content and live gates remain separate.

### Shared implementation modules — approved decisions

The Operator approved separate parsing, reading, writing and CLI responsibilities for every rebuilt connector. This is an internal implementation boundary: keep the same public logical connector API, supported operation subsets and outer execution bindings. Imported helpers are not separate Tools. One TOML connector may expose independent Read and Modify operations while using separate internal modules.

- Parsing accepts supplied content and returns structured data without filesystem access.
- Reading loads content through the connector's private backend binding and uses parsing helpers. It performs no writes.
- Writing persists only the explicitly prepared and admitted content or edits. It does not choose lifecycle or Workflow policy.
- CLI code accepts arguments and dispatches to the admitted operation; it owns no parsing or storage logic.
- Schema choice, identity allocation, Version/time, archiving, replacement and operation sequencing remain Workflow-owned. Mechanical checks of supplied schema, permission and currentness remain connector responsibilities.

Reuse existing modules where their responsibilities fit. Do not introduce an umbrella facade, one module per Atom, new helper Tools or a new Scope Unit. Migrate existing mixed modules only when the approved rebuild touches them; no repository-wide cleanup is included. TOOLS, CONNECTOR_TOOLS and TOOL_WORKFLOWS remain sibling Features; imports do not transfer authority or prove ancestry.

The completed read-only shared-module reviews recovered existing reuse and compared it with a conditional metadata-helper split. No runtime defect or extraction benefit was established. The Operator's later decisions above govern the rebuild; an exact metadata split remains to be checked when that module is touched.

Execute the following work through the existing bounded children, not as new own work in this Epic:

1. CA-P-2252 checks applicable RMEDO and its effective source bindings before implementing the common interface. Record any required contract clarification separately, with fresh independent acceptance and affected FPF review before dependent implementation. Do not treat these Plan instructions as already updated RMEDO.
2. CA-P-2269 inventories the exact helper dependencies, callers, exports and tests for each touched mixed module; resolve the canonical Tool binding of any CLI before moving executable ownership. Preserve public signatures, parsing behavior and existing error handling. Document unchanged modules rather than extracting speculative helpers.
3. CA-P-2252 and affected adapter children CA-P-2253–2258/2280 apply internal separation while preserving the common API. The implementation boundary does not authorize source migration, runtime admission or the deferred publication design.
4. CA-P-2273, with the affected fixture owners CA-P-2274/2275, independently verifies the separation and public API compatibility. Check parser purity, mutation-free reads, bounded writes and thin CLI dispatch, including invalid input, no-op and failure behavior.

The remaining review gaps are evidence tasks, not open design votes: effective legacy contract bindings (SG001), the metadata CLI's canonical Tool binding (SG002), and complete dependencies/callers plus a concrete need for any extraction (SG003). Resolve them only for the affected implementation; ask the Operator if a concrete conflict changes the agreed API, ownership or scope. Nothing in this section marks those checks, RMEDO updates or implementation Done.

### Current rebuilt-contract acceptance

CA-P-2245–2248 are Done for their actual independently accepted current authoring/check scope under the [sole combined acceptance receipt](../../_projection/core-entity-review/stage2/tools-first/logical-connector-contract-acceptance.md). This covers the delivered 81-source subset, approved declarations/exact history and expanded Plan packet, not all future operation-specific contracts or implementation. CA-P-2249/2250 are now Done after their actual independent source acceptance: [ten Scope Unit Query/Read sources](../../_projection/core-entity-review/stage2/tools-first/scope-unit-query-read-contract-acceptance.md) and [seven private-carrier v2 sources with final supplemental lexical acceptance](../../_projection/core-entity-review/stage2/tools-first/private-carrier-contract-acceptance-lexical-v2.md). The latter supersedes only the initial receipt's incomplete lexical coverage; prior receipts/pins remain unchanged historical evidence. The accepted current RMEDO input totals 98 sources (81 + 10 + 7). CA-P-2251 is Active to resume approved Plan `plan-3424292c-447b-4d4f-8ef6-3c586d5270c6`; CA-P-2252–2278 remain Backlog, and this Epic and the existing publication/verification groups remain Active. Source PASS and review activation are not FPF execution/PASS or runtime readiness. The complete-RMEDO and explicitly approved actual FPF review gates, independent fixtures and all deferred publication/live limits remain unchanged.

### Configuration Read correction

The original approved FPF review has now completed against the accepted 98-source packet. Its I002 finding identified the missing complete Configuration Read producer. The Operator selected F002: add that effect-free Read to the existing shared TOML connector. Earlier review-readiness statements above describe the prior checkpoint, not the current review state.

CA-P-2279 owns the source correction and different-reviewer acceptance. Read and Modify remain independent. Each configuration Workflow gets its own Read Step before its existing patch Step. CA-P-2280 records later bounded Read implementation; CA-P-2266/2267 consume it and CA-P-2275 verifies it. CA-P-2251 remains Active for the affected follow-up FPF review after fresh source acceptance; later implementation stays pending. No live, Core/content or migration gate changes.

### Current execution checkpoint

CA-P-2251 is now Done: the approved affected FPF alignment audit completed after Configuration Read acceptance, with I002/F002 verified and G003 closed. The prior pending-review statements above are historical checkpoints. All 36 accepted correction pins and the common interface sources were independently rechecked before continuation.

The Operator authorized continuing this Epic. CA-P-2252 is now Done for bounded pure shared contract support after independent structural acceptance; placement, adapters, independent portfolio fixtures and admission remain their own children. No existing MCP route, deferred publication mechanism or live migration is enabled. G004 remains unproven runtime work, not another unresolved source-design question.

### Shared contract implementation acceptance

CA-P-2252 completed the private pure `connector_contract.py` support and its focused test suite at the existing TOOLS boundary. [Independent structural acceptance](../../_projection/core-entity-review/stage2/tools-first/shared-connector-contract-acceptance.md) pins the code, tests and governing R1936/M376/E628/D625 sources: 15 focused tests and 140 independent assertions passed.

No public API, existing caller, executable binding or backend changed. This is the shared-support prerequisite only. The receiving adapters and their actual schema, permission, source-state and observed-effect checks remain pending; the independent portfolio and runtime/live gates remain open. The next implementation leaves are the existing adapter Tasks, with explicit dependencies and fresh checks retained. This Epic remains Active.

### Parallel adapter execution checkpoint

The Operator requested completion of the whole Epic with parallel implementation, continuing independent work when a blocker appears. This supersedes historical no-implementation-yet checkpoints, but does not approve deferred publication policy or live Core migration.

CA-P-2253–2258/2280 are Active. Their initial bounded private mechanics have focused author tests, not complete receiving/runtime acceptance. Remaining work is decomposed into CA-P-2294–2300 before continuation. Each child retains a 15-minute bound, disjoint edit ownership and independent verification. CA-P-2270/2272 have independent compatibility work; other receiving Workflows remain dependent on actual adapter readiness. Parsing, reading and writing stay separate; no speculative common facade or new public authority protocol is authorized.

The Operator reopened CA-P-2179 design and testing and then selected staged review plus an exclusive window; changed writes still require the remaining contract, implementation and independent acceptance gates. Applicable Core Version/history conflicts remain under CA-P-1970. Typed TOML result representation and exact runtime request/schema binding must be resolved against accepted source contracts before claiming complete adapters. Focused helpers and safe refusal cases do not close these gaps.

### Compatibility and narrow Core follow-up

The Operator separately authorized only the two Core Version/history rules and directly contradictory consumers to be aligned now; CA-P-1970 records that exception while broader content migration stays deferred. Independent source acceptance and affected analytical/consumer checks remain required before use.

CA-P-2270/2272 are Active with bounded independently reviewed implementation. A missing current CA-D-572 is a source-authority gap, not a digest refresh opportunity. The graph's legacy folder-derived Scope topology is a separate existing R1070/M149/E295 defect; CA-P-2302–2304 repair it in bounded portions without source/Subject migration or graph publication. Concrete Atom/Scope receiving mapping remains missing under CA-P-2301; generic callbacks and source-only descriptors do not complete it.

### Decomposing Plans

### Local implementation checkpoint — 2026-10-13

The approved Option 1 publication and private exact-change confirmation are implemented and independently reviewed. The public request is unchanged. Shared locking covers the selected Action and declared cooperating Engine writers. Final scoped verification passed 192 distinct checks, including real selected-route execution, caught restoration, interruption evidence, no replay, contention and truthful lock-error outcomes. [Exact evidence and limits](../../_projection/core-entity-review/stage2/tools-first/subject-publication-option-1-implementation-acceptance.md).

This is local implementation acceptance only. The installed trusted-host confirmation provider and runtime activation remain unconfigured; ordinary changed-Subject execution still refuses without actual confirmation. Six older composition tests remain blocked by pre-existing stale fixture pins. No live Core migration or full tools-Epic completion is claimed. This Plan remains Active for the remaining route/runtime gates. This checkpoint supersedes historical unconditional-prototype-deferral descriptions below, not their historical evidence.

### Approved failure handling and authorization binding

The Operator selected Option 1 after the bounded publication FPF review: caught errors attempt Action-local restoration, with observed failed/partial results; abrupt process interruption or crash is not crash-atomic and may leave partial state. Retain interruption evidence, inspect actual current/history/Run state before another change, and never automatically replay the Atom effect. This explicitly clarifies the earlier all-or-nothing wording; it does not permit false success, predecessor loss, or rollback of earlier independent actions.

The Operator authorized the narrow rule updates, shared-lock/exclusive-window implementation and full-path isolated tests. The existing authorization reference must bind explicit Operator confirmation for the exact reviewed change and affected current/history/authority files. Its purpose-specific internal trusted-host binding keeps public request fields unchanged; request data cannot manufacture confirmation. Missing, stale or mismatched confirmation refuses effects. No installed runtime provider or live Core migration is activated by this approval.

Implementation is divided into bounded responsibilities: source clarification and independent acceptance; internal authorization and Subject publication; shared locking of cooperating Engine writers; current selected-route fixtures; and independent contention/failure verification. Completed raw-helper checks alone cannot close publication acceptance. The existing publication Tasks and this Plan remain Active until their actual checks pass. This checkpoint supersedes conflicting historical deferral statements below without changing their past evidence.

### Current publication decision

CA-P-2179 records the Operator's selected staged-review plus exclusive-window model, with a shared lock for Engine writers and affected-file manual/Git/sync exclusion. This supersedes earlier statements in this Plan that the access/concurrency choice itself remains deferred. It does not waive source/FPF review, implementation, independent verification, actual route admission or separate live migration approval. The changed-Subject guard remains until those gates pass.

The narrow Version/history packet has [independent source acceptance](../../_projection/core-entity-review/stage2/tools-first/version-history-rule-alignment-acceptance.md); [actual runtime mismatches](../../_projection/core-entity-review/stage2/tools-first/version-history-runtime-gaps.md) remain, and affected FPF/use gates are not waived. The connector suite passed 135 tests, without whole-portfolio or admitted publication acceptance.

CA-P-2302–2304 now have [bounded graph implementation acceptance](../../_projection/core-entity-review/stage2/tools-first/declaration-graph-acceptance.md): 30 tests and a read-only current checkout probe (29 declared Scope Units). The legacy folder-topology refusal is fixed. Complete path-policy refusal remains unaccepted because the shared validator admits another Project control root; these Tasks and CA-P-2272 remain Active. Unresolved Settings revision receipts separately block full generation. No production graph or source/Subject migration was published.

CA-P-2279 is Done after [independent Configuration Read source acceptance](../../_projection/core-entity-review/stage2/tools-first/configuration-read-contract-acceptance.md). The original review input gains seven new current sources and nine accepted revisions; historical pins remain unchanged. The accepted correction subsequently passed the affected FPF follow-up; see the current execution checkpoint above.

- [CA-P-2279 — Define complete configuration Read](30-CA-P-2167-EPIC--finish-tools-before-stage-2-execution/done/38-CA-P-2279-TASK--define-complete-configuration-read.md)
- [CA-P-2280 — Implement complete configuration Read](30-CA-P-2167-EPIC--finish-tools-before-stage-2-execution/39-CA-P-2280-TASK--implement-complete-configuration-read.md)

- [CA-P-2249 — Align Scope Unit Query and Read contracts](30-CA-P-2167-EPIC--finish-tools-before-stage-2-execution/done/14-CA-P-2249-TASK--align-scope-unit-query-and-read-contracts.md)
- [CA-P-2250 — Align private carrier operation contracts](30-CA-P-2167-EPIC--finish-tools-before-stage-2-execution/done/15-CA-P-2250-TASK--align-private-carrier-operation-contracts.md)
- [CA-P-2251 — Review complete rebuilt RMEDO with FPF](30-CA-P-2167-EPIC--finish-tools-before-stage-2-execution/done/16-CA-P-2251-TASK--review-complete-rebuilt-rmedo-with-fpf.md)
- [CA-P-2252 — Implement the shared connector contract](30-CA-P-2167-EPIC--finish-tools-before-stage-2-execution/done/17-CA-P-2252-TASK--implement-the-shared-connector-contract.md)
- [CA-P-2253 — Adapt Atom Query and independent Read](30-CA-P-2167-EPIC--finish-tools-before-stage-2-execution/18-CA-P-2253-TASK--adapt-atom-query-and-independent-read.md)
- [CA-P-2254 — Implement Scope Unit Query and Read](30-CA-P-2167-EPIC--finish-tools-before-stage-2-execution/19-CA-P-2254-TASK--implement-scope-unit-query-and-read.md)
- [CA-P-2255 — Implement private carrier edits](30-CA-P-2167-EPIC--finish-tools-before-stage-2-execution/20-CA-P-2255-TASK--implement-private-carrier-edits.md)
- [CA-P-2256 — Implement TOML item and full-set edits](30-CA-P-2167-EPIC--finish-tools-before-stage-2-execution/21-CA-P-2256-TASK--implement-toml-item-and-full-set-edits.md)
- [CA-P-2257 — Implement scalar and value-based property edits](30-CA-P-2167-EPIC--finish-tools-before-stage-2-execution/22-CA-P-2257-TASK--implement-scalar-and-value-based-property-edits.md)
- [CA-P-2258 — Implement the shared section edit family](30-CA-P-2167-EPIC--finish-tools-before-stage-2-execution/23-CA-P-2258-TASK--implement-the-shared-section-edit-family.md)
- [CA-P-2259 — Bind independent Find and Modify Workflows](../001_backlog/24-CA-P-2259-TASK--bind-independent-find-and-modify-workflows.md)
- [CA-P-2260 — Bind Atom creation](../001_backlog/25-CA-P-2260-TASK--bind-atom-creation.md)
- [CA-P-2261 — Bind Scope Unit creation](../001_backlog/26-CA-P-2261-TASK--bind-scope-unit-creation.md)
- [CA-P-2262 — Bind Scope Unit rename and move](../001_backlog/27-CA-P-2262-TASK--bind-scope-unit-rename-and-move.md)
- [CA-P-2263 — Bind Subject rename to explicit property edits](../001_backlog/28-CA-P-2263-TASK--bind-subject-rename-to-explicit-property-edits.md)
- [CA-P-2264 — Bind Atom placement and Status changes](30-CA-P-2167-EPIC--finish-tools-before-stage-2-execution/29-CA-P-2264-TASK--bind-atom-placement-and-status-changes.md)
- [CA-P-2265 — Bind Summary and Type replacement](../001_backlog/30-CA-P-2265-TASK--bind-summary-and-type-replacement.md)
- [CA-P-2266 — Bind Project Structure updates](../001_backlog/31-CA-P-2266-TASK--bind-project-structure-updates.md)
- [CA-P-2267 — Bind Project Settings updates](../001_backlog/32-CA-P-2267-TASK--bind-project-settings-updates.md)
- [CA-P-2268 — Bind explicit change recording and commit](../001_backlog/33-CA-P-2268-TASK--bind-explicit-change-recording-and-commit.md)
- [CA-P-2269 — Place rebuilt code and update exports and callers](../001_backlog/34-CA-P-2269-TASK--place-rebuilt-code-and-update-exports-and-callers.md)
- [CA-P-2270 — Refresh authority consumers and release admission](30-CA-P-2167-EPIC--finish-tools-before-stage-2-execution/35-CA-P-2270-TASK--refresh-authority-consumers-and-release-admission.md)
- [CA-P-2271 — Refresh selected definition pins and seals](../001_backlog/36-CA-P-2271-TASK--refresh-selected-definition-pins-and-seals.md)
- [CA-P-2272 — Use explicit graph Delivery bindings](30-CA-P-2167-EPIC--finish-tools-before-stage-2-execution/37-CA-P-2272-TASK--use-explicit-graph-delivery-bindings.md)
- [CA-P-2302 — Build graph Scope rows from declarations](30-CA-P-2167-EPIC--finish-tools-before-stage-2-execution/40-CA-P-2302-TASK--build-graph-scope-rows-from-declarations.md)
- [CA-P-2303 — Separate graph observations and source attribution](30-CA-P-2167-EPIC--finish-tools-before-stage-2-execution/41-CA-P-2303-TASK--separate-graph-observations-and-source-attribution.md)
- [CA-P-2304 — Verify declaration driven graph discovery](30-CA-P-2167-EPIC--finish-tools-before-stage-2-execution/42-CA-P-2304-TASK--verify-declaration-driven-graph-discovery.md)
- [CA-P-2273 — Verify connector API and Query and Read fixtures](../001_backlog/01-CA-P-2273-TASK--verify-connector-api-and-query-and-read-fixtures.md)
- [CA-P-2274 — Verify carrier property and section fixtures](../001_backlog/02-CA-P-2274-TASK--verify-carrier-property-and-section-fixtures.md)
- [CA-P-2275 — Verify TOML and config Workflow fixtures](../001_backlog/03-CA-P-2275-TASK--verify-toml-and-config-workflow-fixtures.md)
- [CA-P-2276 — Verify Scope Unit and Atom lifecycle fixtures](../001_backlog/04-CA-P-2276-TASK--verify-scope-unit-and-atom-lifecycle-fixtures.md)
- [CA-P-2277 — Verify Subject stop-first-failure and recording fixtures](../001_backlog/05-CA-P-2277-TASK--verify-subject-stop-first-failure-and-recording-fixtures.md)
- [CA-P-2278 — Verify runtime and binding readiness](../001_backlog/06-CA-P-2278-TASK--verify-runtime-and-binding-readiness.md)
- [CA-P-2245 — Align logical connector Requirements and Methods](30-CA-P-2167-EPIC--finish-tools-before-stage-2-execution/done/10-CA-P-2245-TASK--align-logical-connector-requirements-and-methods.md)
- [CA-P-2246 — Align logical connector Evaluation and Delivery](30-CA-P-2167-EPIC--finish-tools-before-stage-2-execution/done/11-CA-P-2246-TASK--align-logical-connector-evaluation-and-delivery.md)
- [CA-P-2247 — Align logical connector Operations Workflows](30-CA-P-2167-EPIC--finish-tools-before-stage-2-execution/done/12-CA-P-2247-TASK--align-logical-connector-operations-workflows.md)
- [CA-P-2248 — Verify rebuilt Tool contracts independently](30-CA-P-2167-EPIC--finish-tools-before-stage-2-execution/done/13-CA-P-2248-TASK--verify-rebuilt-tool-contracts-independently.md)
- [CA-P-2192 — Exclude installed copies from Subject currentness](30-CA-P-2167-EPIC--finish-tools-before-stage-2-execution/done/09-CA-P-2192-TASK--exclude-installed-copies-from-subject-currentness.md)
- [CA-P-2183 — Stage and validate Subject preview candidates](30-CA-P-2167-EPIC--finish-tools-before-stage-2-execution/done/08-CA-P-2183-TASK--stage-and-validate-subject-preview-candidates.md)
- [CA-P-2168 — Align Subject preview currentness contracts](30-CA-P-2167-EPIC--finish-tools-before-stage-2-execution/done/01-CA-P-2168-TASK--align-subject-preview-currentness-contracts.md)
- [CA-P-2169 — Align public graph notation contracts](30-CA-P-2167-EPIC--finish-tools-before-stage-2-execution/done/02-CA-P-2169-TASK--align-public-graph-notation-contracts.md)
- [CA-P-2170 — Align admitted Subject application contracts](30-CA-P-2167-EPIC--finish-tools-before-stage-2-execution/done/03-CA-P-2170-TASK--align-admitted-subject-application-contracts.md)
- [CA-P-2171 — Verify updated Tool contracts independently](30-CA-P-2167-EPIC--finish-tools-before-stage-2-execution/done/04-CA-P-2171-TASK--verify-updated-tool-contracts-independently.md)
- [CA-P-2172 — Align Subject preview and public graph Tools](30-CA-P-2167-EPIC--finish-tools-before-stage-2-execution/done/05-CA-P-2172-TASK--align-subject-preview-and-public-graph-tools.md)
- [CA-P-2173 — Implement the admitted Subject application route](30-CA-P-2167-EPIC--finish-tools-before-stage-2-execution/done/06-CA-P-2173-TASK--implement-the-admitted-subject-application-route.md)
- [CA-P-2174 — Verify remaining Tools on isolated fixtures](30-CA-P-2167-EPIC--finish-tools-before-stage-2-execution/07-CA-P-2174-TASK--verify-remaining-tools-on-isolated-fixtures.md)

### Historical contract checkpoints

CA-P-2168/2169 are Done after actual source alignment and [independent contract acceptance](../../_projection/core-entity-review/stage2/tools-first/contract-acceptance.md). CA-P-2170/2171 are Done after [fresh seven-source MCP application acceptance](../../_projection/core-entity-review/stage2/tools-first/application-contract-acceptance.md) at commit `89da2e93d`; the overlapping UPDATE packet was independently re-accepted. All three contract packets now pass. CA-P-2178–2180 are released only as their concrete dependencies become ready. Later source changes require renewed acceptance. CA-P-2172/2175/2176 complete the bounded preview/graph snapshot in [independent implementation verification](../../_projection/core-entity-review/stage2/tools-first/preview-graph-verification.md). Application work, CA-P-2174 and this group's complete Tool-readiness gate remain pending; subsequent intent/materialization edits need their own verification.

CA-P-2178 is Done in [independent intent verification and deferred application status](../../_projection/core-entity-review/stage2/tools-first/intent-and-application-status.md). Final UPDATE 66 supersedes the earlier 59; SEARCH 49, dispatch five and selected golden-request five passed in their declared scopes. The native deferred-publication gate has independent static verification; those refusal/no-op/integration checks do not accept publication. Only pure intent/materialization is closed by that receipt. CA-P-2179/2180/2181/2182, CA-P-2173/2174 and this group remain Active where successful concurrent-safe publication is still unaccepted. Live changed-Subject writes are blocked, regardless of otherwise valid packet approval.

CA-P-2183–2186 are Done after [actual contract acceptance](../../_projection/core-entity-review/stage2/tools-first/staged-preview-contract-acceptance.md) at `15d2373db` and [independent staging verification](../../_projection/core-entity-review/stage2/tools-first/staged-preview-verification.md) at `ef39bf1fd`. The independently reviewed staging path and 14-case portfolio passed Root's final UPDATE 80, SEARCH 49, generic lifecycle 30 and selected-Subject eight checks. With CA-P-1963, this releases read-only current-source adaptation/re-pinning/mapping solely to create and review staged candidates. No Core migration or current re-pin is claimed; this group, its full publication gate, shared CA-P-1909–1912 and the separate content Epic remain pending.

CA-P-2192 is Done after [independent installed-copy identity acceptance](../../_projection/core-entity-review/stage2/tools-first/installed-copy-identity-acceptance.md) of correction `1fc85bf12`: 87 UPDATE tests, 13 independent cases and the real CA-R-728 approved no-op passed with sources unchanged. This is the bounded competitor-classification fix, not full publication readiness, ledger acceptance or migration export. The complete fresh ledger gate still precedes staging; this group remains Active.

### Definition of Done

The Plan is **not** Done if required work in “Current execution order — after Subject mapping” lacks updated independently verified governing RMEDO, bounded implementation, fresh independent positive/negative fixtures, affected current-source/binding compatibility or actual connected runtime evidence; the required current runtime suite is failed, skipped, stale or incomplete; preparation or a registry listing substitutes for actual capability; an existing safeguard is bypassed; or Tool readiness is treated as live migration approval. Preserve the accepted staged-review/exclusive-window model, exact confirmation, stale-source refusal, per-Atom failure handling and no automatic replay. General connector rebuilding, configuration/type catalogs, C/A work, deferred content work and unrelated unfinished children are not completion prerequisites for this Subjects-only slice. Existing historical receipts remain bounded to their inspected sources; no new FPF review or completion cascade is inferred.
