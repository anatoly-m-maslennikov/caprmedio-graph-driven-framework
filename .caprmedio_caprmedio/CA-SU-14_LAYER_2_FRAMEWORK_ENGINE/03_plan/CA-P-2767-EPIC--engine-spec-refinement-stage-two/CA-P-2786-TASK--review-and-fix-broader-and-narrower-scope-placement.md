---
identity:
  id: CA-P-2786
  ref_id: CA-P-2786
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
    name: CA-P-2786-TASK--review-and-fix-broader-and-narrower-scope-placement.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/CA-P-2767-EPIC--engine-spec-refinement-stage-two
author: Anatoly Maslennikov
relations:
  IS_BLOCKED_BY:
  - CA-P-2785
  - CA-P-2773
---

## Summary

Review and fix broader and narrower Scope placement

## Objective

Identify which selected Atoms should move to broader or narrower Scope Units and prepare justified corrections.

## Working procedure

Follow the parent Epic working procedure. Work in same-Scope batches of up to 15 minutes and keep a small Work Report.

## Subtasks

- [x] Pass one: test whether a locally owned contribution applies unchanged across a broader Scope Unit, or is specific enough to belong in a narrower receiver; distinguish reusable policy, shared solution and local decision. (ETA: up to 15 min per batch.)
- [x] Prepare supported promotion or demotion Drafts, removing redundant local copies only when coverage and references are preserved; check receiver permission and actual descendants rather than promoting by Tier or wording alone. (ETA: up to 15 min per batch.)
- [x] Pass two: recheck inherited applicability, sibling impact, Scope Contracts, relation endpoints and replacement consumers; retain unsupported moves as proposals or bounded Questions. (ETA: up to 15 min per batch.)

## Definition of Done

Every reviewed broader/narrower placement candidate has a reason and a disposition. In-scope moves are prepared for the adoption gate; out-of-scope moves have a handoff. No promotion broadens a claim merely to fit a parent Scope Unit.
