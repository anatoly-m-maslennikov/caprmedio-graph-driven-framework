---
identity:
  id: CA-P-2775@1
  ref_id: CA-P-2775@1
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
    name: 08-CA-P-2775@1-TASK--review-and-fix-med-forms.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/archive
author: Anatoly Maslennikov
work_sequence_number: 8
relations:
  IS_BLOCKED_BY:
  - CA-P-2771
  - CA-P-2784
---

## Summary

Review and fix MED Forms

## Objective

Classify the refined MED using the active model rather than old names or product-name heuristics.

## Working procedure

Follow the parent Epic working procedure. Each item below is repeated in same-Scope batches of up to 15 minutes; decompose a larger batch before starting.

## Subtasks

- [ ] Pass one: inspect each Method, Evaluation and Delivery separately against Direct Policy, Approach Policy, Solution and Decision declarations. (ETA: up to 15 min per batch.)
- [ ] Fix Form and necessary claim boundaries in Drafts; preserve Role independence and do not force Declarations into these Forms. (ETA: up to 15 min per batch.)
- [ ] Pass two: review applicability, inheritance and specialization obligations for the corrected Forms and fix remaining errors. (ETA: up to 15 min per batch.)

## Definition of Done

Each selected MED has an evidence-backed Form consistent with the current model, including Approach Policy where appropriate. A local technology name alone does not decide the Form.
