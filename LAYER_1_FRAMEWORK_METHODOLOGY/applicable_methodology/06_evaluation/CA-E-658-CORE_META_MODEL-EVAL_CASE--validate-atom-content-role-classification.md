---
subjects:
  active: CAPRMEDIO_MODEL <+ Atom.Header.Role
  passive:
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Selection
  - CAPRMEDIO_MODEL <+ Atom.Header.Role
  - CAPRMEDIO_MODEL <+ Atom.Content
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role:=Operations)/Action
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role:=Operations)/Workflow
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/(.Header.Form := Workflow) >{1+} Atom/(.Header.Role := Operations)/(.Header.Form := Step)'
  - CAPRMEDIO_MODEL <+ Carrier
version: 14
updated_at: 2026-11-02 17:54:42 +0400
relations:
  evaluation_for:
  - CA-R-1548
  - CA-R-1549@21
  - CA-R-1550
  - CA-R-2512
  - CA-R-2513
  - CA-R-2463
  - CA-R-2465
atom_id: CA-E-658
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Evaluation
form: Eval Case
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation/CA-E-658-CORE_META_MODEL-EVAL_CASE--validate-atom-content-role-classification.md
  source_atom_id: CA-E-658
  source_atom_revision: 14
  source_sha256: 0cfb3a020dfeaca04fab3a53847b2ae2f329b48fb2ebf745ecbed0a8ac047798
  original_relations_sha256: 3f77165aaf8f7e993bfc0f9ea81d811533335e6bf04708770913c7c330fa3ace
---
## Summary
Validate Atom Content Role classification

## Claim

### Prose Claim

classification of an Atom by its Content Role.

the classification Evaluation **must** fail **if** an Atom's Content Role does **not** match its actual contribution under the Specification **and** Change definitions.

- use the evaluated Atom's declared Content Role, complete Main Content, **and** applicable Specification **and** Change definitions as the input evidence.
- compare the declared Content Role with the contribution expressed **in** that Main Content, using the following classification table.
- report unresolved **when** required evidence is unavailable, unresolved, **or** contradictory; **otherwise**, report pass **if** the declared Content Role matches the observed contribution **and** fail **if** it does **not**.
- identify the evaluated Atom **and** report the declared Content Role, relevant content excerpt, applicable definition, **and** comparison result.

| Claim contribution | Expected classification |
|---|---|
| a model definition, required property, permission, **or** Actor participation/authorization policy governing a Concern, Analysis & Advisory, Task, Action, **or** Workflow | Requirement |
| a convention for authoring **or** constructing that content | Method |
| a falsifiable correctness check | Evaluation |
| a Carrier's fields, format, **or** placement | Delivery |
| a particular unresolved issue, analytical finding, **or** intended Task | the matching Concern, Analysis & Advisory, **or** Plan role |
| a particular reusable Action behavior, Workflow graph, **or** Step invocation binding | Operations |


reusing the specified content's role as the specification's role **must** fail this check. a long-lived Concern **or** reusable Workflow **must not** fail merely because its lifetime is long.
