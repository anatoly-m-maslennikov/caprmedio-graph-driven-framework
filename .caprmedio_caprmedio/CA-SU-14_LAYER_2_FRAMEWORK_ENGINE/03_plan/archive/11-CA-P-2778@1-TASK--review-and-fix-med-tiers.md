---
identity:
  id: CA-P-2778@1
  ref_id: CA-P-2778@1
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
  version: 1
  updated_at: 2026-11-09 05:38:07 +0400
destination:
  file:
    name: 11-CA-P-2778@1-TASK--review-and-fix-med-tiers.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/archive
author: Anatoly Maslennikov
work_sequence_number: 11
relations:
  IS_BLOCKED_BY:
  - CA-P-2776
---

## Summary

Review and fix MED tiers

## Objective

Make numeric Tiers consistent with the refined specification and its declared relations.

## Working procedure

Follow the parent Epic working procedure. Each item below is repeated in same-Scope batches of up to 15 minutes; decompose a larger batch before starting.

## Subtasks

- [ ] Pass one: check tiers, relation directions, scope ancestry and admitted cross-scope permissions against the active model and latest Operator decisions. (ETA: up to 15 min per batch.)
- [ ] Fix supported tier assignments after claim, Form and relation corrections; preserve valid Tier-0 Scope Contracts and admitted exceptions. (ETA: up to 15 min per batch.)
- [ ] Pass two: recheck the affected graph and fix remaining ordering conflicts without inventing policy meaning from a Tier label. (ETA: up to 15 min per batch.)

## Definition of Done

Every changed Tier has a model-backed reason. Numeric ordering, Scope Contract rules and admitted exceptions hold; Tier numbers do not decide Policy versus Decision.
