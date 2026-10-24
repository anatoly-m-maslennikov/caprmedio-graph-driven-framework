---
subjects:
  governs: 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Workflow'
  depends_on:
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Step'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - Subject/Domain/Node/Occurrent/Execution/Workflow Run
  - Subject/Domain/Node/Occurrent/Execution/Step Run
  - 'Subject/Graph/Relation/Type: On Result'
  - Subject/Domain/Node/Continuant/History/Journal.Record
version: 13
updated_at: 2026-10-24 01:50:12 +0400
relations:
  evaluation_for:
  - CA-R-1508
  - CA-R-1509
  - CA-R-1510
  - CA-R-1511
  - CA-R-1513
atom_id: CA-E-486
content_role: Evaluation
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
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

- define **`=2`** distinct Steps referencing the same Action with different input bindings; follow an admitted conditional transition between the Steps.
- revisit a Step under an accepted retry allowance within **`=1`** Workflow Run.
- introduce a Step with **`=0`** Action references, **`>1`** Action references, an unresolved Action, **or** an unresolved required input binding.
- introduce an untyped edge, an edge whose endpoint is an Action rather than a Step, **or** a next-Step reference missing from that Workflow.
- record a failed Step Run; separately reference a reusable Workflow definition **without** recording an execution.

### Acceptance

- the valid shared Action retains **`=1`** definition; Step bindings remain distinct.
- **every** actual revisit creates a distinct Step Run within the same Workflow Run **without** resetting its retry allowance.
- invalid Action cardinality, unresolved inputs, invalid endpoints, **and** untyped transitions fail the check.
- failed **or** absent execution evidence **must not** become successful completion, a new Workflow definition, **or** another historical source.

report the exact failing source, case, **and** condition; do **not** change source authority **to** make the check pass.
