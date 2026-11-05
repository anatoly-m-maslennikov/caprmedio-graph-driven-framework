---
atom_id: CA-A-1256
ref_id: CA-A-1256
role: Analysis & Advisory
form: Specification Proposal
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
status: Active
author: Anatoly Maslennikov
topics:
  main_subject: Formal Model
version: 2
updated_at: 2026-11-02 15:49:28 +0400
tier: 3
container:
  scope_unit: CA-SU-00
carrier_destination:
  file:
    name: CA-A-1256-CAPRMEDIO-SPECIFICATION_PROPOSAL--declare-contained-kinds-only-at-their-structural-location.md
    path: .caprmedio_caprmedio/02_analysis
---
# Summary

Declare contained kinds only at their structural location

## Decision

Remove the /@(Step) reference beneath Operations. Show Operations with Type Action and Type Workflow; Workflow >{1..} Step >{0..} Substep. A Step exists only inside a Workflow; Substep is distinct and exists inside a Step. The counts describe parts per whole: a Workflow has at least one Step; a Step may have zero or more Substeps. Each contained part still has exactly one immediate whole.

Remove duplicate Continuant classification references for Asset, Code Unit, Documentation, Event Record, Module, Package, Prompt, Resources, Step and Substep. Keep their structural declarations. This does not replace containment with specialization or infer inherited Atom properties for Step through its containing Workflow. Other explicit references, such as recursive Package and Scope Unit containment, remain.

## State

Update Draft model and affected Definition Drafts. No Current promotion, runtime change or new general inheritance rule is adopted by this cleanup.
