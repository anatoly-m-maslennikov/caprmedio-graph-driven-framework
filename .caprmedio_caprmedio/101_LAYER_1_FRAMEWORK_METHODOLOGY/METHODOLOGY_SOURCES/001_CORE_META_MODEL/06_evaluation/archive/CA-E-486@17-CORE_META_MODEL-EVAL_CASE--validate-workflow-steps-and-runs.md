---
subjects:
  governs: 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Workflow'
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Step'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action'
  - Subject/Graph Node/Domain/Occurrent/Execution/Workflow Run
  - Subject/Graph Node/Domain/Occurrent/Execution/Step Run
  - Subject/Graph Node/Domain/Continuant/History/Journal.Record
version: 17
updated_at: 2026-10-26 22:47:49 +0400
relations:
  evaluation_for:
  - CA-R-1508
  - CA-R-1509
  - CA-R-1510
  - CA-R-1511
atom_id: CA-E-486@17
content_role: Evaluation
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
type: Eval Case
tier: 3
---
# Summary

Validate Workflow Steps and Runs

## Scope

Workflow Steps **and** Runs.

## Claim

the Evaluation **must** check Workflow Steps **and** Runs.

## Details

### Cases

- define **`=2`** distinct leaf Steps referencing the same Action with different input bindings; follow an admitted Conditional Step route whose result selects exactly one nested Step alternative.
- execute a containing Step and its nested substeps: record a distinct Step Run for the containing Step and for each executed nested Step; the containing Step Run launches no Action, while each executed leaf Step Run executes its **`=1`** referenced Action through its **`=1`** corresponding Action Run.
- revisit a Step under an accepted retry allowance within **`=1`** Workflow Run.
- introduce a leaf Step with **`=0`** Action references, **`>1`** Action references, an unresolved Action, **or** an unresolved required input binding; or give a containing Step an own Action launch.
- introduce an untyped edge, an edge whose endpoint is an Action rather than a Step, **or** a next-Step reference missing from that Workflow.
- record a failed Step Run; separately reference a reusable Workflow definition **without** recording an execution.

### Acceptance

- the valid shared Action retains **`=1`** definition; Step bindings remain distinct, and the containing Step does not duplicate Action behavior.
- every executed Step, including a containing Step, has its own distinct Step Run; the containing Step Run groups actual nested Step Runs and launches no Action, while each leaf Step Run executes its **`=1`** referenced Action through its **`=1`** corresponding Action Run.
- a Conditional Step selects exactly one declared nested Step alternative from its definition; no additional Branch, Fork, or Decision Atom is required.
- **every** actual revisit creates a distinct Step Run within the same Workflow Run **without** resetting its retry allowance.
- invalid Action cardinality, invalid containing-Step launch, unresolved inputs, invalid endpoints, **and** untyped transitions fail the check.
- failed **or** absent execution evidence **must not** become successful completion, a new Workflow definition, **or** another historical source.

report the exact failing source, case, **and** condition; do **not** change source authority **to** make the check pass.
