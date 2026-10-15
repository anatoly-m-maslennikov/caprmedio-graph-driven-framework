# Local Subject publication completion

Derived verification receipt. Date: 2026-10-13. This is not installed-runtime or migration authority.

## Outcome

Independent review accepts local completion of CA-P-2179, CA-P-2180, CA-P-2181 and CA-P-2182; CA-P-2173 closes after those children. CA-P-2167 and CA-P-2174 remain Active.

This builds on [source acceptance](subject-publication-option-1-source-acceptance.md) and [bounded implementation evidence](subject-publication-option-1-implementation-acceptance.md). Their historical results are retained, not relabeled as new runs. The five governing source pins are unchanged.

## Gaps closed

- Independent literal full before/current/history byte and mode ledgers cover Active LF/CRLF and correctly placed Plan Done/Backlog originals. They preserve Status and unrelated content, independently control effect-time metadata, and compare the full native effect set and actual recorded references.
- Deliberately wrong current/history bytes, missing/extra/reordered/digest-tampered effects and extra recorded references fail the oracle. Expected bytes do not come from the production materializer.
- Actual post-publication recording failure is repaired through the existing Session/RunTracker/Journal path. The original canonical event is appended once to its original sealed partition; receipt and pending-file removal are verified. Current/history bytes, inode, mode and timestamps remain unchanged. No publisher, raw writer or executor is replayed.
- Full UPDATE regression discovery exposed a defect missed by the earlier scoped suite: forbidden standalone Subject apply created a persistent lock file before refusing. Request parsing and refusal now happen before lock acquisition; the generic update tail remains locked before authoritative target reads through effects and restoration. Input is read once. The original failing snapshot test was not weakened.

## Current verification

| Suite | Tests | Result |
| --- | ---: | --- |
| Full ATOM_UPDATE discovery | 87 | PASS, 75.110 seconds |
| Existing selected Subject application | 25 | PASS, 244.043 seconds |
| New independent byte/effect portfolio | 6 | PASS, author and independent reviewer |
| New actual recording-only recovery | 1 | PASS, author and independent reviewer |
| Existing generic Atom Operations | 26 | PASS |
| Distinct current scoped checks | 145 | PASS |

The initial ready-file discovery was 79 passes and one failure; the exact same refusal test now passes in the final 87. The final regression runner `epic_publication_blocker` verified 21 unchanged input pins before and after execution. Independent reviewer `connector_binding_review` ran the new six-case portfolio (56.053 seconds), actual recovery (12.801 seconds), and original refusal regression (1.184 seconds), then returned no remaining concrete local blocker and explicit closure eligibility. Repeated runs and the earlier 192 checks are not added to this table.

Execution used offline uv, Python 3.14.7, PyYAML 6.0.3 and pydantic 2.13.5. Full discovery used `python -m unittest discover` in `201_TOOLS/ATOM_UPDATE/tests`; selected/new suites used their exact test filenames under `203_APPS/WORKFLOW_ORCHESTRATOR/tests`. Scratch fixtures, cache and bytecode were kept under `.caprmedio_tmp`. Whitespace validation passed.

## Boundaries and remaining work

These Tasks explicitly exclude installed runtime/image/manifest activation. The absent installed confirmation provider is therefore not an unfinished local implementation requirement. Ordinary requests still cannot manufacture confirmation.

No Core Subject migration, content migration, installation, release or push occurred. Full tools-Epic/runtime acceptance remains open. The previously reported six old composition fixture failures from stale O128 pins were not repaired or silently rebound.

Recording-only recovery repairs the Journal receipt; it does not reconcile the enclosing service's cached pending result. Abrupt interruption may leave partial state requiring inspection. Cooperating-writer exclusion does not protect against outside writers ignoring the exclusive window, and does not provide crash atomicity.

## Current changed and related pins

Other production pins remain those in the preceding implementation receipt.

```text
9a3a860d2010e318f918f9246bd5955e77ef80d9d1ee3ef9d1b9cd2746ccf7b9  102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/atom_operations.py
255f525db2d831f4c49e8351c4262b781e8f179d5803eecacbfd40f400d04fae  102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/ATOM_UPDATE/tests/test_subject_apply_portfolio.py
4077459de7c1b7984615f31d627c180be5b18918673a5453ca888cfea36d3f96  102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/tests/test_selected_subject_apply_portfolio.py
6b0c7260f58a4506f0bff6be698f5be39d1b0e46d6bd0061211f5ee278f49a31  102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/tests/test_selected_subject_recording_recovery.py
3f006e5819879ef41d903503b7688f1ea5482fe927d86a8adb3e0af939b07e2f  102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/tests/test_selected_subject_apply.py
6c952c8d67cdb3ca79d71b1634ef6a5541cfa79603964f6680386da8bac60f08  102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/workflow_run_support.py
f2367f563ff9635dfbb8180b2e6164b53ae0359bb1686b8b098a05fbf5ae0c6f  102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/work_journal.py
```
