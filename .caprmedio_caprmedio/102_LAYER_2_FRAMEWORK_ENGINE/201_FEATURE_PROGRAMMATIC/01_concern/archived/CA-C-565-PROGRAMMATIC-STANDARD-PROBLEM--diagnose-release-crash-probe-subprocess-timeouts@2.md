---
atom_id: CA-C-565
content_role: Concern
type: Problem
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Active
priority: high
subjects:
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  concern_about: [CA-P-2401, CA-P-2532, CA-O-164]
version: 2
updated_at: "2026-10-21T11:36:18Z"
---
# Summary

Diagnose release crash-probe subprocess timeouts

## Concern

The requested Local release cannot pass its full-suite gate: the history and current subcases of test_process_exit_after_history_or_current_retains_started_facts_without_replay in test_selected_subject_apply.py exceeded the existing30second child-process timeout instead of observing expected exit73. Cause is not yet established; do not label this a production lifecycle failure or assume a timing-budget change is the fix.

## Evidences

Run local-20261021-retention-110232, started from7c9540a94, reached tests only. Its selected-subject module ran25tests in968.378s with2timeout errors. Both tracebacks and exact child invocation are retained in .caprmedio_tmp/simple_local_release/local-20261021-retention-110232-tests-j9whr9y8.log. The owned release was interrupted after that confirmed failed gate; final report .caprmedio_runtime/simple_local_release/reports/local-20261021-retention-110232.md truthfully records failed/tests/KeyboardInterrupt. Distinguish the two preceding timeout errors from the subsequent intentional interruption; this was not a completed full suite.

No product copy, version bump, installed-runtime replacement or release-image retirement occurred; version remains0.4.4.9. Readback confirms original production container e81250f8ed4c39bf08007e05449c63b88d5c96b8f65f94f6fdec8622c6817d84 still healthy on08f26a9b8b14image. Four isolated containers left by interrupted tests were inspected against image sha256:e25bb127c4797dc915c43000a828bfb0fff02d51617792b11705c6efb772afe8, exact attempt355ebb599c3445daa2f128a250ec0b78 and Project-temp mounts, then stopped/removed non-force. The existing attempt-bound test-image owner removed that now-unused image; absence and sole running production container were read back. No volume/prune/foreign cleanup; host test log remains. Removed disposable container logs/writable state have no backup.

## Blast radius

P2532 owns isolated reproducibility and phase diagnosis on frozen disposable fixtures. Preserve actual authorization, source/currentness, schema, history, crash-boundary and no-replay checks. Do not bypass production safeguards, raise a deadline simply to pass, replay held Atom effects or use production MCP for tests. Repair only an evidenced root cause, split work before15minutes own work, and rerun required checks before any separately identified release attempt. Other Epic work may proceed only under its existing dependency gates.

### Bounded diagnosis checkpoint

The exact single test passes in isolation1/1 in60.255s, with history/current children reaching expected exit73 and all real history/no-replay assertions passing. Child authorization took about3.4s; dispatch-to-history-write about11.9/17.7s. The clean four-copy comparison retained unchanged30second child deadlines; all4instances reached the diagnostic90second parent limit with no write/exit73 events in their retained22-event traces. This is a bounded stress diagnostic, not4completed failing unittest results or an exact reproduction of the heterogeneous full suite. A first stress batch overlapped a root file-listing scan and is explicitly excluded from causal attribution. Final serial recovery passes1/1 in48.594s, both exit73, no diagnostic processes left. Traces are under .caprmedio_tmp/diagnose-crash-probe-20261021-JSqlaK/.

Evidence supports concurrent validation/filesystem timing sensitivity, not an unbounded lifecycle loop or a particular universal resource threshold. The suite runs2ordinary+2Docker modules, not5simultaneous modules inferred from interleaved log lines. P2533 will isolate the expensive selected-subject module once before those existing pools, preserving every test, source/currentness/authorization/crash/no-replay guard and the30/1800second deadlines. No production validation optimization, aggregate-evidence format, global lock or timeout increase is authorized. This Problem stays Active until repair and a fresh mandatory release gate pass.
