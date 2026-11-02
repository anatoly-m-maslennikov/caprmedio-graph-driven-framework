---
atom_id: CA-O-016@22
content_role: Operations
type: Workflow
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Workflow//Implementation Workflow'
  depends_on:
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Step'
  - 'Subject/Graph/Relation/Type: On Result'
  - Subject/Domain/Node/Occurrent/Execution/Workflow Run
  - Subject/Domain/Node/Occurrent/Execution/Step Run
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan/Type: Plan'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action//Implementation Retry Control'
version: 22
updated_at: 2026-10-24 00:51:05 +0400
relations:
  relates_to:
  - CA-R-1509
  - CA-R-1519
  - CA-R-1525
  - CA-R-1570
  - CA-O-231
  - CA-O-232
  - CA-O-233
  - CA-O-094
  - CA-O-234
  - CA-O-096
  - CA-O-099
  - CA-O-230
  - CA-O-098
tier: 3
---
# Summary

Implement Evaluations before required behavior

## Operation

Implementation Workflow **means** the test-first implementation graph below; its referenced Step Atoms own Action/input/context bindings, **and** its Action Atoms own operational behavior.

Every implementation handoff carries direct full-source rows in `requirements`, `methods`, `evaluations`, **and** `delivery`; a `methods` row has the same shape as the other rows and retains full content, Atom ID, Version, source path, **and** digest. An authorized/frozen initial request may explicitly select source roots. The resolver verifies the original current sources/revisions/digests **and** complete explicit declared universe, expands declared governing parents per explicit root, retains other explicitly selected applicable policy branches, **and** evaluates Scope/capability conditions. Parent relations alone do not define applicability; never infer it from physical directory ancestors **or** siblings. R/D implementation targets remain separate from governing-parent authority. `method_projection`, when supplied, is an optional legacy derived convenience: it neither replaces direct rows **nor** blocks a Run when absent. Do **not** require compilation **or** a derived semantic paragraph.

An Agentic Step exposes its current prompt, inputs, **and** result contract while pending. The controlling session may execute **or** delegate that Step, then submits the actual result through the same invocation interface/continuation for executor next-Step selection. Every continuation requires fresh bound admission; it is one-use, an identical submission is idempotent, and a conflicting submission is refused. It never replays effects. This lifecycle neither hardcodes an MCP transport nor adds Workflow-wide Properties.

- entry: CA-O-231.
- nodes: CA-O-231, CA-O-232, CA-O-233, CA-O-094, CA-O-234, CA-O-096, CA-O-099, CA-O-230.
- transitions between Steps use Workflow-scoped `ON_RESULT`; `completed` **and** `blocked` are terminal results, **not** Steps.

| From Step | Result condition | Next Step **or** terminal result |
|---|---|---|
| CA-O-231 | evaluation_ready | CA-O-232 |
| CA-O-231 | requirement_ready | CA-O-233 |
| CA-O-231 | evaluation_runnable | CA-O-094 |
| CA-O-231 | review_ready | CA-O-230 |
| CA-O-231 | complete | completed |
| CA-O-231 | blocked | blocked |
| CA-O-232 | prepared | CA-O-231 |
| CA-O-232 | blocked | blocked |
| CA-O-233 | implemented | CA-O-231 |
| CA-O-233 | blocked | blocked |
| CA-O-094 | passed | CA-O-231 |
| CA-O-094 | failed | CA-O-234 |
| CA-O-094 | blocked | blocked |
| CA-O-234 | expected_initial_failure | CA-O-231 |
| CA-O-234 | implementation_defect | CA-O-096 |
| CA-O-234 | test_implementation_defect | CA-O-096 |
| CA-O-234 | authority_change_required | blocked |
| CA-O-234 | environment_blocker | blocked |
| CA-O-234 | unresolved | blocked |
| CA-O-096 | retry_permitted | CA-O-099 |
| CA-O-096 | retry_blocked | blocked |
| CA-O-099 | repaired | CA-O-231 |
| CA-O-099 | authority_change_required | blocked |
| CA-O-099 | blocked | blocked |
| CA-O-230 | preliminary_clear | CA-O-231 |
| CA-O-230 | passed | CA-O-231 |
| CA-O-230 | findings | CA-O-234 |
| CA-O-230 | partial | blocked |
| CA-O-230 | unresolved | blocked |

an unknown result, failed invocation, unresolved confidence/permission gate, **or** non-progressing revisit ends the Run as `blocked` with actual partial results. **every** repair path crosses CA-O-096; revisiting preparation **or** changing a failure **must not** reset that retry state. preparation revisits retain completed work **and** require a changed residual work/evidence/baseline state; otherwise they are blocked rather than looping.

a terminal blocker preserves completed effects **and** pending P work. resumption requires fresh admission under the definition-binding rules; it is **not** success **or** permission **to** silently replay completed work.

Method creation **and** acceptance are outside this Workflow. return retained issue, test, diagnosis, **and** fix evidence for a separately invoked Method-learning Run under CA-O-102; neither that Run nor creation of an M Atom is an implementation-completion prerequisite.

### Shared-context candidate closure

Every Agentic Step in this graph explicitly uses Integrated context. Shared context retains the current request, Plan, source-bound R/M/E/D, candidate, actual results, findings, and remaining budget; it never replaces complete Step inputs or permits a silent context fallback. Standalone review Workflow CA-O-223 and its Isolated CA-O-229 are unchanged.

Preparation selects tests before behavior, then preliminary code review before final checks, then final review against those actual checks. CA-O-230 invokes read-only CA-O-225 with an explicit preliminary or final phase. A preliminary_clear result is not acceptance. A repair changes the candidate and invalidates affected earlier checks and review; preparation selects their required reruns. Confirmed review findings use CA-O-234, CA-O-096, and CA-O-099 without bypassing diagnosis or resetting finite retry, confidence, permission, resource, or no-progress gates.

### Separate release continuation

After completed, return a release handoff only when release is in the admitted request: selected Project and release Workflow identity/revision or applicable selection rule, candidate and changed paths, Plan and R/M/E/D source bindings, current final review/check evidence, actual effects, required inputs, and unresolved limitations. Start release as a separately admitted Workflow Run under CA-R-1520 and CA-R-1525; do not use cross-Workflow ON_RESULT or treat this definition as release permission or execution. Resolve the actual release contract and current inputs at that admission.

## Details
