---
identity:
  id: CA-P-2780
  ref_id: CA-P-2780
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
    name: 13-CA-P-2780-TASK--promote-the-reviewed-med-specification.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/020_done/CA-P-2767-EPIC--engine-spec-refinement-stage-two/020_done
author: Anatoly Maslennikov
work_sequence_number: 13
relations:
  IS_BLOCKED_BY:
  - CA-P-2779
---

## Summary

Promote the reviewed MED specification

## Objective

Adopt only the reviewed specification changes and verify their real source state.

## Working procedure

Follow the parent Epic working procedure. Each item below is repeated in same-Scope batches of up to 15 minutes; decompose a larger batch before starting.

## Subtasks

- [x] Review the exact adoption batch, source versions, permissions and replacement bindings before promotion. (ETA: up to 15 min per batch.)
- [x] Promote or replace only accepted Drafts under the current lifecycle model, using the declared replacement relation; preserve existing Archived sources. (ETA: up to 15 min per batch.)
- [x] Query the actual Current sources, rebuild relevant topic/relation views through available supported paths, and fix adoption discrepancies. (ETA: up to 15 min per batch.)

## Definition of Done

Every admitted source is promoted, replaced, retained or explicitly held. Current source readback matches the reviewed result; Drafting, adoption and implementation are reported separately.
