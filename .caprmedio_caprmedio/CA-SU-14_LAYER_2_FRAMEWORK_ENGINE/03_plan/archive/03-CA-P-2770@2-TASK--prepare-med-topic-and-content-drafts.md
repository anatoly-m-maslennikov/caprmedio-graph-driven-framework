---
identity:
  id: CA-P-2770@2
  ref_id: CA-P-2770@2
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
  updated_at: 2026-11-09 05:58:13 +0400
destination:
  file:
    name: 03-CA-P-2770@2-TASK--prepare-med-topic-and-content-drafts.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/archive
author: Anatoly Maslennikov
work_sequence_number: 3
relations:
  IS_BLOCKED_BY:
  - CA-P-2769
---

## Summary

Prepare MED topic and content Drafts

## Objective

Create source-bound Drafts for the selected MED refinements.

## Working procedure

Follow the parent Epic working procedure. Each item below is repeated in same-Scope batches of up to 15 minutes; decompose a larger batch before starting.

## Subtasks

- [ ] Prepare one next-version Draft per selected source and assign one Scope Unit per worker; create additional Drafts only for supported splits or missing specification. (ETA: up to 15 min per batch.)
- [ ] Assign main topics first, then review dependencies; preserve semantic distinctions between the two. (ETA: up to 15 min per batch.)
- [ ] Review and fix the Draft set and its thin tracking; retain existing unrelated Drafts and all Archived sources unchanged. (ETA: up to 15 min per batch.)

## Definition of Done

Each affected Current MED has an unambiguous Draft or explicit held reason. Tracking is thin: Atom ID | old topic | new topic | status. Drafts contain intended specification, not execution notes.
