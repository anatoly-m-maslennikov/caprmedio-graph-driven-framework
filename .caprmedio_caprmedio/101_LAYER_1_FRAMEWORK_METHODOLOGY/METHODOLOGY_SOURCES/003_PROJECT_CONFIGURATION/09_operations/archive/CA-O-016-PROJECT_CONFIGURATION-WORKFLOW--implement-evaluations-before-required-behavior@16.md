---
atom_id: CA-O-016
content_role: Operations
type: Workflow
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Implementation Workflow"
  depends_on:
    ["Entity/Node/Continuant/Atom/Content Role: Operations/Type: Workflow", "Entity/Node/Continuant/Atom/Content Role: Operations/Type: Step", "Relation/Type: On Result", "Entity/Node/Occurrent/Execution/Workflow Run", "Entity/Node/Occurrent/Execution/Step Run", "Atom/Content Role: Plan/Type: Plan", "Implementation Retry Control"]
version: 16
updated_at: "2026-10-21T23:46:56+00:00"
relations:
  relates_to:
    - CA-R-1509
    - CA-R-1519
    - CA-R-1525
    - CA-R-1570
    - CA-O-091
    - CA-O-092
    - CA-O-093
    - CA-O-094
    - CA-O-095
    - CA-O-096
    - CA-O-099
    - CA-O-230
    - CA-O-098
global_tier: 11
---
# Summary

Implement Evaluations before required behavior

## Operation

Implementation Workflow **means** the test-first implementation graph below; its referenced Step Atoms own Action/input/context bindings, **and** its Action Atoms own operational behavior.

- entry: CA-O-091.
- nodes: CA-O-091, CA-O-092, CA-O-093, CA-O-094, CA-O-095, CA-O-096, CA-O-099, CA-O-230.
- transitions between Steps use Workflow-scoped `ON_RESULT`; `completed` **and** `blocked` are terminal results, **not** Steps.

| From Step | Result condition | Next Step **or** terminal result |
|---|---|---|
| CA-O-091 | evaluation_ready | CA-O-092 |
| CA-O-091 | requirement_ready | CA-O-093 |
| CA-O-091 | evaluation_runnable | CA-O-094 |
| CA-O-091 | review_ready | CA-O-230 |
| CA-O-091 | complete | completed |
| CA-O-091 | blocked | blocked |
| CA-O-092 | prepared | CA-O-091 |
| CA-O-092 | blocked | blocked |
| CA-O-093 | implemented | CA-O-091 |
| CA-O-093 | blocked | blocked |
| CA-O-094 | passed | CA-O-091 |
| CA-O-094 | failed | CA-O-095 |
| CA-O-094 | blocked | blocked |
| CA-O-095 | expected_initial_failure | CA-O-091 |
| CA-O-095 | implementation_defect | CA-O-096 |
| CA-O-095 | test_implementation_defect | CA-O-096 |
| CA-O-095 | authority_change_required | blocked |
| CA-O-095 | environment_blocker | blocked |
| CA-O-095 | unresolved | blocked |
| CA-O-096 | retry_permitted | CA-O-099 |
| CA-O-096 | retry_blocked | blocked |
| CA-O-099 | repaired | CA-O-091 |
| CA-O-099 | authority_change_required | blocked |
| CA-O-099 | blocked | blocked |
| CA-O-230 | preliminary_clear | CA-O-091 |
| CA-O-230 | passed | CA-O-091 |
| CA-O-230 | findings | CA-O-095 |
| CA-O-230 | partial | blocked |
| CA-O-230 | unresolved | blocked |

an unknown result, failed invocation, unresolved confidence/permission gate, **or** non-progressing revisit ends the Run as `blocked` with actual partial results. **every** repair path crosses CA-O-096; revisiting preparation **or** changing a failure **must not** reset that retry state. preparation revisits retain completed work **and** require a changed residual work/evidence/baseline state; otherwise they are blocked rather than looping.

a terminal blocker preserves completed effects **and** pending P work. resumption requires fresh admission under the definition-binding rules; it is **not** success **or** permission **to** silently replay completed work.

Method creation **and** acceptance are outside this Workflow. return retained issue, test, diagnosis, **and** fix evidence for a separately invoked Method-learning Run under CA-O-102; neither that Run nor creation of an M Atom is an implementation-completion prerequisite.

### Shared-context candidate closure

Every Agentic Step in this graph explicitly uses Integrated context. Shared context retains the current request, Plan, source-bound R/M/E/D, candidate, actual results, findings, and remaining budget; it never replaces complete Step inputs or permits a silent context fallback. Standalone review Workflow CA-O-223 and its Isolated CA-O-229 are unchanged.

Preparation selects tests before behavior, then preliminary code review before final checks, then final review against those actual checks. CA-O-230 invokes read-only CA-O-225 with an explicit preliminary or final phase. A preliminary_clear result is not acceptance. A repair changes the candidate and invalidates affected earlier checks and review; preparation selects their required reruns. Confirmed review findings use CA-O-095, CA-O-096, and CA-O-099 without bypassing diagnosis or resetting finite retry, confidence, permission, resource, or no-progress gates.

### Separate release continuation

After completed, return a release handoff only when release is in the admitted request: selected Project and release Workflow identity/revision or applicable selection rule, candidate and changed paths, Plan and R/M/E/D source bindings, current final review/check evidence, actual effects, required inputs, and unresolved limitations. Start release as a separately admitted Workflow Run under CA-R-1520 and CA-R-1525; do not use cross-Workflow ON_RESULT or treat this definition as release permission or execution. Resolve the actual release contract and current inputs at that admission.

## Details
