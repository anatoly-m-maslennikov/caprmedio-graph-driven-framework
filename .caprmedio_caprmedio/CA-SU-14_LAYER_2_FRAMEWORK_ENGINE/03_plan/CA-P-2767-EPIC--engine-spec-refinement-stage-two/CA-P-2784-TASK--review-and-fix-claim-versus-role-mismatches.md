---
identity:
  id: CA-P-2784
  ref_id: CA-P-2784
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
    name: CA-P-2784-TASK--review-and-fix-claim-versus-role-mismatches.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/CA-P-2767-EPIC--engine-spec-refinement-stage-two
author: Anatoly Maslennikov
relations:
  IS_BLOCKED_BY:
  - CA-P-2771
---

## Summary

Review and fix Claim versus Role mismatches

## Objective

Make each selected Atom’s Role match what its actual Claim contributes.

## Working procedure

Follow the parent Epic working procedure. Work in same-Scope batches of up to 15 minutes and keep a small Work Report.

## Subtasks

- [x] Pass one: read the full actual Claim and relevant Semantics and Details; compare the meaning with the current Role declarations, independently of topic, Form, filename and existing code. (ETA: up to 15 min per batch.)
- [x] Prepare corrections for supported R/M/E/D/O mismatches and mixed-Role claims. Apply the active identity and replacement rules for a Role change; do not silently relabel a Current Atom. (ETA: up to 15 min per batch.)
- [x] Pass two: review the corrected Drafts, including splits and affected relations; record uncertain bounded choices as C/Question and continue independent work. (ETA: up to 15 min per batch.)

## Definition of Done

Every selected MED source has a Claim-versus-Role disposition. Role mismatches with R or O are explicitly resolved or held; a broader inherited topic or architectural term alone does not determine Role.
