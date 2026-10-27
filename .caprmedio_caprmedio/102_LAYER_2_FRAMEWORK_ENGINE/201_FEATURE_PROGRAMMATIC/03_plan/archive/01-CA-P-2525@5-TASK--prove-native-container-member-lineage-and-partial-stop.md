---
atom_id: CA-P-2525@5
content_role: Plan
type: Plan
label: Task
work_sequence_number: 1
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Subject/Domain/Node/Continuant/Atom
  depends_on: []
relations:
  is_decomposition_of:
  - CA-P-2506
version: 5
updated_at: 2026-10-24 08:06:50 +0400
tier: 3
---
# Summary

Prove native container member lineage and partial stop

## Objective

Prove native container member lineage and partial stop.

## Details

At most15minutes own work; split before extending. Own tests/test_container_lifecycle_functional.py only. Prepare independently of P2524 but final native execution waits for fixture readiness. Use existing checked-in frozen inputs and disposable Project; assert durable per-member one-target receipt/frontier/effects excludes container seal, actual Workflow/Step/Action identities and parent lineage with unchanged Initiative/action IDs; technical coordinator is not a fake Workflow Run. Add a native failure/mutation after first successful member to prove preserved exact history/effects, untouched remainder/parent, fresh rebind and no automatic replay. Retain all existing Archive/Done/auth/source-drift/duplicate checks. Do not alter source logic/guards or infer success from Journal alone; test controlled seam cannot replace native admission/effects. Missing other refusal/uncertainty cases remain explicit for P2495. Final native acceptance waits for P2524 and root review; no production MCP/Docker/release.

### Reviewed dependency and acceptance checkpoint

Dependency P2524 accepted: Project-temp fixture2checks and real nativeauth1check pass, independentAPPROVE; original5testhistorical50–55s, no hangingclaim/90secwhole-suitekill. Independent readiness review caught test-only failure-event mismatch before costlyrun: expectedterminaleventmustmatch realmemberoutcome (failed/partial→failed, completed/no_op→completed). Testowner corrects that and splits the newly expanded assertion helper for E539 cohesion; no productionlogic change. Then current native7testmodule executes with exacthash/observedevidence; remaining refusal/uncertaintymatrix explicitly notclosed.

### Current reviewed acceptance frontier

Final458-line test module SHA256634eed485a1cbeba0967d16cffea8372309e203e757666201c55f8eb0020dd27. Native7/7 passed67.783s; root independently reran final partial-failure case1/1 in10.710s (wall11.31). Root adjacent36/36 pass0.071s; AST/Ruff/diffchecks and final independent seam/assertion review APPROVE. Per-member durable one-target receipt/frontier/effects, actual Workflow→Step→Action lineage, unchanged Initiative/action IDs, technicalcoordinator exclusion, partial history, fresh-rebind refusal and no-replay are asserted. Two earlier native attempts each had1test-only failure: first expected one childcall but lifecyclefunction invokedpreview+execute; next raw providerfailedoutcome normalized tointerrupted_pending, notterminalfailed. Corrected to existing real SelectedExecution.handlersCA-O128 seam, delegating child to original handler and injecting parent terminalfailure in admittedhandler shape. These are retained test-fixture diagnosis, not production fixes or waived gates. The controlledhandler test proves orchestration/receipts/history, not the domainfunction's internal failure mechanism. E539boundedlegacycohesionexception: module458≤500lines for thisincrement, newassertionhelpers14–34single-purpose; reconsider split before crossing500oraddingunrelatedscenariofamilies. One generatedsourcepyc fromexplicitpy_compile was removed; finalsyntaxchecksASTwrite-free. Full P2495refusal/uncertaintymatrix remains open.
