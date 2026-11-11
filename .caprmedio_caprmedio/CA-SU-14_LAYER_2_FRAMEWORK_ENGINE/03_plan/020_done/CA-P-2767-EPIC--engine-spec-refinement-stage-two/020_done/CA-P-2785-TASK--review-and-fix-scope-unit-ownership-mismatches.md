---
identity:
  id: CA-P-2785
  ref_id: CA-P-2785
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
    name: CA-P-2785-TASK--review-and-fix-scope-unit-ownership-mismatches.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/020_done/CA-P-2767-EPIC--engine-spec-refinement-stage-two/020_done
author: Anatoly Maslennikov
relations:
  IS_BLOCKED_BY:
  - CA-P-2775
---

## Summary

Review and fix Scope Unit ownership mismatches

## Objective

Place each selected contribution in the Scope Unit whose responsibility it actually serves.

## Working procedure

Follow the parent Epic working procedure. Work in same-Scope batches of up to 15 minutes and keep a small Work Report.

## Subtasks

- [x] Pass one: compare the Claim with current Scope Delegations, Scope Contracts, permissions and the Methodology/Engine responsibility boundary; distinguish ownership from dependencies and Carrier paths. (ETA: up to 15 min per batch.)
- [x] Prepare supported ownership corrections in Drafts, including receiver permissions and affected consumers; identify Methodology-versus-Engine mismatches without rewriting excluded scopes. (ETA: up to 15 min per batch.)
- [x] Pass two: recheck actual applicability, direct and inherited constraints, containment and connected references; record out-of-scope moves as explicit handoffs and uncertain choices as C/Question. (ETA: up to 15 min per batch.)

## Definition of Done

Each selected MED has a justified owning Scope Unit or an explicit unresolved disposition. Wrong ownership is not hidden by a topical rename; no outside-scope source is silently moved or changed.
