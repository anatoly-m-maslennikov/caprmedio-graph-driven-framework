---
subjects:
  active: Atom/(.Role:=Operations)/Workflow
  passive:
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Workflow >{1+} Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Step'
  - Atom/(.Role:=Operations)/Action
  - Entity/Object/Occurrent/Execution/Workflow Run
  - Entity/Object/Occurrent/Execution/Step Run
  - Entity/Object/Continuant/History/Journal > Event Record
version: 23
updated_at: 2026-11-02 08:06:47 +0400
relations:
  evaluation_for:
  - CA-R-2464
  - CA-R-2465
  - CA-R-1510@18
  - CA-R-1511@22
atom_id: CA-E-486
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Evaluation
form: Eval Case
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation/CA-E-486-CORE_META_MODEL-EVAL_CASE--validate-workflow-steps-and-runs.md
  source_atom_id: CA-E-486
  source_atom_revision: 23
  source_sha256: 6eea192d37a315b282a508c00b9da3fb52a1258753f60d1aae071f824c7c897d
  original_relations_sha256: 35f4dc30c7d948fb1607a0437162ba4140b734d343edc1c138735e4c22a60db7
---
## Summary

Validate Workflow Steps and Runs

## Claim scope

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
