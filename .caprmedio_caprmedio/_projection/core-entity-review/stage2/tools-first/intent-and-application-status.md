# Subject intent verification and deferred application

2026-10-12. Non-authoritative implementation evidence for CA-P-2178 and the unfinished CA-P-2173 application group.

## Pure intent and materialization: verified

Independent reviewer `tools_first_verifier` (GPT-6.1 Sol, xhigh) accepted the pure intent/materialization implementation. Root reran the complete ATOM_UPDATE suite: **59 tests passed**, including the ten intent/materialization tests. Root also reran ATOM_SEARCH: **49 tests passed**. These are separate suites; the ten focused tests are already included in 59.

| Source | SHA-256 |
|---|---|
| `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/atom_subject_patch.py` | `0c2c7058470309820002ce9f97db8a2c30be17fe7726675658d4414c3633f218` |
| `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/ATOM_UPDATE/tests/test_subject_intent_materialization.py` | `66450ddca99d5e2b605d180dd9f4de93939ec2339ae0b75ea0082017439ec03b` |

The deterministic intent binds the current original, exact ordered patches, actual grammar-source evidence, intended Subject-only bytes with old execution metadata, the Version/time rule, and the exact predecessor destination. Materialization revalidates the live inputs and then computes the complete proposed revision without writing it. It preserves unrelated bytes and Status. A no-op preserves Version and time. Both profiles retain source-pin and no-follow checks. The tested preview still detects duplicate current originals outside the submitted target set.

## Admitted-route implementation: incomplete

The existing MCP update action has the closed Subject variant and passes its actual Session, Action Run and admitted lifecycle prior to the native implementation. Root reran its five dispatch tests successfully, plus all five selected golden-request tests in an isolated environment with the locked validation, MCP and workflow dependencies.

Native review found that a matching assessment hash alone did not prove that assessment completed in this Session. The implementation now reopens the canonical completed O067/O145 records and persisted result, with the same O127 lineage. This correction received independent source review; it does not by itself establish passing end-to-end application.

## Operator decision: defer concurrent publication

Independent review reproduced a concurrent edit being overwritten between the last fingerprint check and file replacement. History removal has the same ownership window. An earlier check does not close that window.

The Operator answered **“defer this”** to the proposed exclusive-access requirement. No lock requirement, quarantine design or atomic-exchange implementation was approved. The new native route now unconditionally refuses changed-Subject execution with `subject-publication-deferred` after admission and before effect-time materialization or any history/current write. Safe lookup, preview, pure materialization and exact no-op do not enable that publication path. The generic update route is unchanged.

Root also reran the four raw-helper tests, 30 existing selected-lifecycle tests and five Subject dispatch tests successfully. The raw-helper tests establish isolated mechanics only, not concurrency safety; the disabled publication/recovery prototype is not accepted for live use.

After the seven new native-preview/refusal tests were added, Root reran the full ATOM_UPDATE suite: **66 passed**. This supersedes, rather than adds to, the earlier 59-test count. The new cases use real carrier and Report authority for preview, closed parameters, source/intent pins, duplicate/history refusal, missing or stale Report, no-op and refusal of a caller Boolean without a Session.

| Deferred implementation source | SHA-256 |
|---|---|
| `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/atom_subject_apply.py` | `493898a6c984060495ca485aa32600dd68cfa4849425e5f96c9fae202fbbb403` |
| `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/atom_operations.py` | `0f39a181bb1ecfa226fd9e474ebd39c664a0ef03de1521874e8eb0b4a1ffbbc9` |

Independent reviewer `preview_currentness_tests` confirmed that the deferred diagnostic is unconditional after the actual admission check, before effect-time materialization and every current/history/rollback write. Preview and no-op return earlier; generic updates use a separate unchanged branch.

## Real selected-session refusal: verified

Root reran all **six selected Subject integration tests** successfully (12.299 seconds). The actual selected Session completes and reopens O067/O145 assessment records and their persisted result, admits the lifecycle prior and records the actual O030 start. Requested and actual child IDs differ in the positive fixture. The request reaches exactly `subject-publication-deferred`, not an unrelated earlier refusal. The writer is never called; current bytes, mode and archive remain unchanged. Missing completion, altered persisted assessment, forged start receipt, failed terminal recording, no replay and a real selected no-op are covered.

Independent reviewer `preview_currentness_tests` separately passed 19 checks: the same six selected cases, seven native cases and six generic composition cases. These overlapping runs are not additional distinct test counts. The seven native cases also pass with only Python 3.14, Pydantic and PyYAML; runtime-heavy checks use the locked validation/MCP/workflow groups in an isolated environment under `.caprmedio_tmp`.

| Acceptance fixture | SHA-256 |
|---|---|
| `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/ATOM_UPDATE/tests/test_subject_apply_portfolio.py` | `46a8eb177fe4992368eaa45ba5d00ab7a5931a042bff02114d53ae4e1e4a3f43` |
| `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/tests/test_selected_subject_apply.py` | `981619cd164b47b9b2973ebe6ba40e38aa838d9f1e39c1d0a8e9106eaeddeb4f` |

Commit `d6940f0e3` records the deferred gate, same-session evidence correction and these two fixture files. This is acceptance of the explicitly disabled live route, not acceptance of publication.

### Additional sealed-frontier checks

Commit `751fc9048` adds two selected-route test methods: 21 malformed frontier/effect variants and a deliberate in-memory mutant control. The independently authored portfolio passed eight selected tests and seven native tests in the locked isolated environment. Eighteen variants reach `subject-frontier-mismatch`; empty and duplicate frontiers fail earlier with exact shared `invalid-request` diagnostics. Removing the equality guard produces the wrong deferred diagnostic, which the control detects. All cases preserve source bytes, mode and history and confirm that the writer is not called.

The updated fixture hashes are `4b59a6d345893c582c6611d28713a68b0a707d63aed387581470284c044fe29d` for `test_subject_apply_portfolio.py` and `910b22d5833270cde87f1da2d2aec35b4d285594bb428773b45d90094daa72dd` for `test_selected_subject_apply.py`. These supersede the fixture snapshot above; the production gate is unchanged. CA-P-2181 remains partial. These results do not cover staging or successful publication.

Successful publication, rollback under concurrent edits, the full application portfolio and the final tools-first gate remain unaccepted. The accepted RMEDO describes the required behavior; this document records incomplete implementation, not a relaxation of that behavior. No original Core Subject was migrated or installed MCP runtime activated by this work. CA-P-1910 still requires its separate exact migration-packet approval.
