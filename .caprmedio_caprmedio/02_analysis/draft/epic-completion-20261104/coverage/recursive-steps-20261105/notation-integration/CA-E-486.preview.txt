---
subjects:
  active: CAPRMEDIO_MODEL <+ Atom/(.Header.Role:=Operations)/Workflow
  passive:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/(.Header.Form := Workflow) >{1+} Atom/(.Header.Role := Operations)/(.Header.Form := Step)
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role:=Operations)/Action
  - CAPRMEDIO_MODEL <+ Entity/Object/Occurrent/Execution/Workflow Run
  - CAPRMEDIO_MODEL <+ Entity/Object/Occurrent/Execution/Step Run
  - CAPRMEDIO_MODEL <+ Event Record
version: 24
updated_at: 2026-11-05 02:06:39 +0400
relations:
  evaluation_for:
  - CA-R-2464
  - CA-R-2465
  - CA-R-1510@18
  - CA-R-1511@22
atom_id: CA-E-486
status: Draft
tier: 3
role: Evaluation
form: Eval Case
carrier_destination:
  file:
    name: CA-E-486@24-draft-CORE_META_MODEL-EVAL_CASE--validate-workflow-steps-and-runs.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation/draft
---
## Summary

Validate Workflow Steps and Runs

## Claim

### Prose Claim


Workflow Steps **and** Runs.


the Evaluation **must** check Workflow Steps **and** Runs.

## Details

### Cases

- define **`=2`** distinct leaf Steps referencing the same Action with different input bindings; follow an admitted Conditional Step route whose result selects exactly one nested Step alternative.
- execute a containing Step and its nested Steps: record a distinct Step Run for the containing Step and for each executed nested Step; the containing Step Run launches no Action or Workflow, while each executed leaf Step Run for an Action-running Step executes its **`=1`** referenced Action through its **`=1`** corresponding Action Run.
- execute a leaf Step with exactly one Workflow target.
- revisit a Step under an accepted retry allowance within **`=1`** Workflow Run.
- introduce a Step with neither one Action nor one Workflow nor one or more nested Steps, more than one RUNS target in total across Action and Workflow, an unresolved selected target, **or** an unresolved required input binding; or give a containing Step an own Action or Workflow launch.
- introduce an untyped edge, an edge whose endpoint is an Action rather than a Step, **or** a next-Step reference missing from that Workflow.
- record a failed Step Run; separately reference a reusable Workflow definition **without** recording an execution.

### Acceptance

- the valid shared Action retains **`=1`** definition; Step bindings remain distinct, and the containing Step does not duplicate Action behavior.
- every executed Step, including a containing Step, has its own distinct Step Run; the containing Step Run groups actual nested Step Runs and launches no Action or Workflow, while each leaf Step Run for an Action-running Step executes its **`=1`** referenced Action through its **`=1`** corresponding Action Run.
- a Conditional Step selects exactly one declared nested Step alternative from its definition; no additional Branch, Fork, or Decision Atom is required.
- **every** actual revisit creates a distinct Step Run within the same Workflow Run **without** resetting its retry allowance.
- invalid Step target cardinality, invalid containing-Step launch, unresolved inputs, invalid endpoints, **and** untyped transitions fail the check.
- failed **or** absent execution evidence **must not** become successful completion, a new Workflow definition, **or** another historical source.

report the exact failing source, case, **and** condition; do **not** change source authority **to** make the check pass.
