---
atom_id: CA-A-1215
content_role: Analysis
type: Analysis Report
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
status: Done
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-16 00:44:07 +0400"
subjects:
  governs: Tool
  depends_on: [Atom, "Atom/Status", Journal, Workflow, Operator]
relations:
  relates_to: [CA-P-2385, CA-P-2386, CA-P-2387, CA-P-2388, CA-P-2389, CA-P-2390, CA-P-2400, CA-C-523]
---
# Summary

Review Atom Status history and Journal gate removal

## Question

What has been implemented and verified for CA-P-2385, and what are the limits of its bounded completion?

## Scope

The Operator's 2026-10-15 decisions for requested admitted Atom Status, ordinary fresh-ID Draft promotion, actual predecessor preservation and independent Journal recording. Inspect the current Project-local/methodology/Engine source packet, bounded source-impact reports, implementation observations and connected isolated checks. This is bounded implementation/test acceptance for the declared CA-P-2385 work, not a full-suite, installed-runtime or release receipt.

## Approach

Apply Project-local authority before methodology sources and Engine receiving contracts. Source changes and their exact actual history are distinct from implementation, test observations and connected runtime behavior. Root-directed source/Plan edits were direct-file operations; no MCP mutation or retrospective Journal admission is claimed for those edits.

Evidence comes from actual tool output observed in session codex:01a01cb4-e15e-78d1-9084-766bf6b0cd63 and the measured current carriers. The coordinating agent supplied execution results and source-audit results in this same session. No persisted external test-receipt file or retained MCP Run IDs were supplied; none are invented. Image digests identify the actual isolated test images, not the installed Project runtime. A Done Analysis records the completed bounded assessment. The related Plan Status changes are separate actual revisions; this report does not supply Status to a parent or descendant.

## Results

### Accepted source alignment

Commit dc6cfa1da contains 69 files: 23 revised authoritative source contracts, 23 exact predecessor archives and 23 bounded lineage-impact reports CA-A-1192–1214. The root source audit (execution outputs 17086 and 87157) checked 82 JSON source-pin objects and 56 examined child dispositions; all 23 source-before archives matched the actual predecessors. This count is a bounded source-integration result, not a full live dependency-graph or runtime-conformance proof.

- Project-local review found no conflicting local policy requiring a new edit.
- Methodology changes: CA-D-568/570/446/276/288, CA-O-127/128/129, CA-R-1521 and CA-E-490.
- Engine changes: CA-D-569, CA-R-1825, CA-D-531, CA-R-1828, CA-D-532, CA-E-545/548, CA-R-865, CA-O-032, CA-E-303, CA-R-1824 and CA-E-543/544.

The sources now distinguish schema-admitted Atom Status values from transition-matrix/intermediate-Status gates; non-Atom transition conditions remain. Ordinary ID-free Draft promotion always uses a fresh unused Atom ID, including tool-demoted Drafts. Actual prior identity/history remains evidence, not permission to restore a formerly held ID. Real predecessor history, source/currentness, collision, schema and permission safeguards remain. Journal existence/completeness/baseline/receipt and retained Draft-head/lineage checks do not gate mutation admission or success. Independent recording failure is diagnostic and never authorizes replay of actual effects.

### Observed connected checks before final native freeze

| Observed check | Isolated image SHA-256 | Result and elapsed time |
| --- | --- | --- |
| W01 creation directly Archived | 904c75f00b008adef9bfa724cb2810e63d90139d6c48b8d3cbf88f8ffeeb0e84 | Passed; 56.03 s |
| W04 manual Draft promotion, no-op and expected refusal | 904c75f00b008adef9bfa724cb2810e63d90139d6c48b8d3cbf88f8ffeeb0e84 | Passed; 68.204 s |
| Stale-source expected refusal | 904c75f00b008adef9bfa724cb2810e63d90139d6c48b8d3cbf88f8ffeeb0e84 | Passed; 21.07 s |
| W04 incomplete Journal | 06f569d811bbf1b26e06766897d2588cb8e5a613fe99f9fe8f79cb7e05a0c0fc | Passed; 45.346 s |
| Linux bounded 24-test bundle | 06f569d811bbf1b26e06766897d2588cb8e5a613fe99f9fe8f79cb7e05a0c0fc | 24 passed; test time 37.333 s, total execution 51.133 s |

Root execution 83759 returned exit zero for the latter observed checks. Changed non-native Python/test files separately passed the scoped Ruff F/E9 check. These observations establish their actual tested revisions only; they are not proof for later native concurrency changes, all Workflows, the whole suite, or installed MCP activation.

### Final implementation and independent acceptance

Implementation commit 3d658ee7a contains 49 accepted code/test/fixture-pin files. Source alignment remains separately committed as dc6cfa1da. The final native production files were independently confirmed at these exact SHA-256 values:

- 102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/atom_operations.py: 899dc4293c20156da0bafc88fbf30689888a19b5ff5f61602788cffdd2b77ac8.
- 102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/lifecycle_intents.py: c82eb7591684b06aa9598a0c2737e1f6fbb2fb72e51d96b9d70c26b02701984d.

The native two-thread duplicate-ID defect was repaired by one runtime-backed cross-process identity guard across fresh allocation and publication. Ordinary/direct/native and CLI fresh-ID writers use that guard; nested calls are reentrant. Independent review accepted exception release, parent/final-lock symlink refusals and the interrupted-acquisition descriptor cleanup, including a real blocked cross-process cancellation probe. No retained Draft-history/Journal gate, old-ID restoration exception, new retry or blind replay was introduced. CA-C-524@1 is Resolved after the actual repair and checks; its past state was not fabricated.

Final-code focused native golden checks passed 11/11; legacy CLI checks passed 26/26; scoped Ruff checks passed. Their host results do not substitute for the distinct Linux concurrency checks below. An older unrelated Replacement coordination gap is not claimed repaired or made a new completion dependency by this bounded change.

### Final image-specific functional and connected results

| Observed check | Isolated image SHA-256 | Result and elapsed time |
| --- | --- | --- |
| W01 creation directly Archived | 68c371acc0cc242ad107ca53804b16ddac1db7523e9531be627e7fd5fa663d5d | Passed; 36.524 s |
| W04 manual Draft promotion, no-op and expected refusal | 68c371acc0cc242ad107ca53804b16ddac1db7523e9531be627e7fd5fa663d5d | Passed; 47.331 s |
| Stale-source expected refusal | 68c371acc0cc242ad107ca53804b16ddac1db7523e9531be627e7fd5fa663d5d | Passed; 18.795 s |
| W04 incomplete Journal | 68c371acc0cc242ad107ca53804b16ddac1db7523e9531be627e7fd5fa663d5d | Passed; 34.625 s |
| Linux bounded 24-test bundle | 68c371acc0cc242ad107ca53804b16ddac1db7523e9531be627e7fd5fa663d5d | 24 passed; 14.537 s |
| W04 incomplete Journal after descriptor-cleanup correction | 0fac136ec9661a8884cbdcf53e0b7da34f5bc24506b71b6d452bc934c8df80a3 | Passed; 46.038 s |
| Linux native identity-lock/concurrency/interruption tests after descriptor-cleanup correction | 0fac136ec9661a8884cbdcf53e0b7da34f5bc24506b71b6d452bc934c8df80a3 | 4 passed; 4.268 s |
| Linux Subject-batch functional checks at the actual RunTracker._append_one boundary | b4b92f15f3172bf0a92d898e418dc6a11c32233033d700c863fa57e5066c9111 | 7 passed; 12.266 s |

Root execution 56813 returned exit zero for the four-journey/24-test image. That image precedes only the later BaseException descriptor-cleanup correction; it is not relabeled as a test of the exact post-cleanup bytes. Root execution 33291 returned exit zero for the post-cleanup incomplete-Journal journey and four Linux lock tests. Execution 35576 supplied the seven Subject-batch results. Independent review accepted the narrow cleanup correction and final source pins; these separate results compose the actual bounded acceptance, not a claim that all four journeys ran again on the final image.

The final four Linux guard tests check distinct Drafts receive distinct IDs; same-ID/different-path Create publishes once; a child process waits behind the Project lock; and interrupted lock acquisition closes its descriptor while preserving the original exception. The Subject-batch fixture was corrected to target the actual append boundary rather than weakening mutation/recording assertions. No missing Run IDs or persisted receipt files are invented.

### Independent host limitation

CA-C-523@3 remains an Active host Problem: fixture directory rename/removal produced Operation not permitted and raw host openat probes reproduced ENOENT despite a valid matching parent descriptor/path, with underlying OS/interposition cause unproven. Linux results do not make those failed host runs pass or prove that the host restriction is fixed. No forced deletion or weakened source/history behavior is authorized.

The same host restriction refused the attempted P2386 directory-carrier rename during Plan closure. Scoped per-file relocation preserved the actual files and historical bytes instead. Empty prior directory shells are not Plan identities and are not a claim of successful host directory cleanup.

### Bounded Plan completion

[CA-P-2385 — Remove history and Journal gates from Atom Status operations](../03_plan/18-CA-P-1959-EPIC--improve-entity-model-stage-2/30-CA-P-2167-EPIC--finish-tools-before-stage-2-execution/done/61-CA-P-2385-TASK--remove-history-and-journal-gates-from-atom-status-operations.md) and all contained current Plans CA-P-2386–2400 are Done for this bounded work. Each formerly Active remaining Plan was separately updated with N+1, its actual edit time, exact predecessor preservation and its own local done placement. Already Done descendants retained their bytes and own local placement while the ancestor bundle moved; no fictional descendant revisions were created. P2167 has no authored P2385 link to rewrite and remains byte-unchanged and Active. No unrelated referenced Plan was selected or closed.

The completed source/wrapper leaves retain their earlier bounded completion observations as historical checkpoints. The final native and functional results above close the later remaining work; older pending descriptions are not the final outcome. CA-C-524 is Resolved, while the independent host restriction CA-C-523 remains Active. This Plan completion is implementation/test acceptance, not release or live installed MCP activation.

## TLDR

The requested Atom Status, fresh-ID Draft promotion and independent Journal behavior are implemented and accepted for CA-P-2385. All contained tasks are Done with exact history and correct placement. Source and implementation commits, final hashes and image-specific test evidence are recorded separately. Host OS failures, whole-repository suite coverage and installed-runtime/release outcomes are not claimed resolved or passed.
