---
atom_id: CA-E-513
ref_id: CA-E-513
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
topics:
  main_subject: CAPRMEDIO_MODEL <+ Carrier
  dependencies:
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/(.Header.Form := Workflow)'
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/(.Header.Form := Workflow) >{1+} Atom/(.Header.Role := Operations)/(.Header.Form := Step)'
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/(.Header.Form := Action)'
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Evaluation)
version: 23
updated_at: 2026-11-02 00:18:22 +0400
relations:
  evaluation_for:
  - CA-O-080
  - CA-O-087
  - CA-O-088
tier: 4
role: Evaluation
form: Eval Case
container:
  scope_unit: CA-SU-13
carrier_destination:
  file:
    name: CA-E-513-PROJECT_CONFIGURATION-EVAL_CASE--validate-the-atom-carrier-validation-workflow-definition.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/06_evaluation
---
## Summary

Validate the Atom Carrier Validation Workflow definition

## Claim

### Prose Claim


the Atom Carrier Validation Workflow definition.


the Atom Carrier Validation definition check **must** reject a graph **or** binding that cannot preserve its declared read-only assessment boundary.

- require **=1** entry **and** **=1** Step node, a resolvable Step reference, **=1** Action per Step, explicit compatible input bindings, **and** admitted Workflow-scoped transitions.
- require reachable terminal outcomes for incomplete, invalid, valid, **and** execution-error cases as defined by the referenced Action; **none** of the outcomes **may** be silently mapped **to** valid.
- verify that this graph is acyclic, contains no implicit retry **or** repair, **and** does **not** duplicate Action behavior inside its Step bindings **or** graph.
- verify that findings do **not** prevent assessment of independent targets, while missing authority **or** changed inputs cannot become proof of conformance.
- reference current self-sufficiency **and** source-binding Evaluations for the checked conditions; definition conformance **must not** be reported as a successful Tool execution.
