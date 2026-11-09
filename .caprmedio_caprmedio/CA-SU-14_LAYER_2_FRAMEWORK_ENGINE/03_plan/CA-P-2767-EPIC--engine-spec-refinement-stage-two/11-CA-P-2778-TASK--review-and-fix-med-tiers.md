---
identity:
  id: CA-P-2778
  ref_id: CA-P-2778
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
  status: Done
  version: 2
  updated_at: 2026-11-09 07:59:08 +0400
destination:
  file:
    name: 11-CA-P-2778-TASK--review-and-fix-med-tiers.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/CA-P-2767-EPIC--engine-spec-refinement-stage-two
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

- [x] Pass one: check tiers, relation directions, scope ancestry and admitted cross-scope permissions against the active model and latest Operator decisions. (ETA: up to 15 min per batch.)
- [x] Fix supported tier assignments after claim, Form and relation corrections; preserve valid Tier-0 Scope Contracts and admitted exceptions. (ETA: up to 15 min per batch.)
- [x] Pass two: recheck the affected graph and fix remaining ordering conflicts without inventing policy meaning from a Tier label. (ETA: up to 15 min per batch.)

## Definition of Done

Every changed Tier has a model-backed reason. Numeric ordering, Scope Contract rules and admitted exceptions hold; Tier numbers do not decide Policy versus Decision.
