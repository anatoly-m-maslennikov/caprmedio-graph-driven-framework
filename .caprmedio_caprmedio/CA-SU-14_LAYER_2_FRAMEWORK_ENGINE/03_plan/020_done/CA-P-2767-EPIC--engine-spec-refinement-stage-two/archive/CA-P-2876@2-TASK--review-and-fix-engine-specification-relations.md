---
identity:
  id: CA-P-2876
  ref_id: CA-P-2876@2
context:
  container:
    atom: CA-P-2767
  role: Plan
  form: Plan
  label: Task
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom
  tier: 4
state:
  status: Archived
  version: 2
  updated_at: 2026-11-10 11:49:56 +0400
destination:
  file:
    name: CA-P-2876@2-TASK--review-and-fix-engine-specification-relations.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/CA-P-2767-EPIC--engine-spec-refinement-stage-two/archive
relations:
  IS_BLOCKED_BY:
  - CA-P-2874
  - CA-P-2875
---

## Summary

Review and fix Engine specification relations

## Objective

Review relations between MED and their connected Requirements and Operations after Role/Form/Scope corrections. Check method_for, evaluation_for, delivery_for and replacement lineage against current relation Declarations, endpoint Roles, direction and cardinality. Account for incoming references before retirement.

## Subtasks

Each subtask is a batch of at most 15–20 minutes. Repeat per Scope Unit; give each subagent one Scope Unit.

- [ ] Review pass one on a same-Scope batch.
- [ ] Fix findings and prepare or refine the affected Drafts.
- [ ] Run independent pass two on the corrected batch.
- [ ] Fix pass-two findings and recheck affected earlier criteria.
- [ ] Record a small Work Report and thin coverage entries.

## Definition of Done

Changed and retained relations are reviewed against current definitions; no invalid retargeting or invented relation is used to complete a merge. Tasks track work; specification changes belong in RMEDO. No runtime implementation is performed here.

## Reviewed inputs

P2874 and P2875 are Done. Use the fresh effective candidates and exact Current relation declarations. Preserve case-distinct declared relations, and distinguish one Target per Relation fact from a limit on the Host's relation collection. Normalize only unambiguous declared names. Trace exact successor evidence before retargeting; do not use Summary similarity as identity proof. Record Scope/Tier ordering for its dedicated check. Prepare Draft repairs and run independent pass two before closing.
