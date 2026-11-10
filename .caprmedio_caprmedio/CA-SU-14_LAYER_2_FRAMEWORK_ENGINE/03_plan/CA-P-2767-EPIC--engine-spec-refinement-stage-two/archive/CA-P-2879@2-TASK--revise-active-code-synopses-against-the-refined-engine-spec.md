---
identity:
  id: CA-P-2879
  ref_id: CA-P-2879@2
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
  updated_at: 2026-11-10 06:12:11 +0400
destination:
  file:
    name: CA-P-2879@2-TASK--revise-active-code-synopses-against-the-refined-engine-spec.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/CA-P-2767-EPIC--engine-spec-refinement-stage-two/archive
relations:
  IS_BLOCKED_BY:
  - CA-P-2883
---

## Summary

Revise active Code Synopses against the refined Engine spec

## Objective

After accepted specification adoption and the passing main-subject graph gate, review active I/Code Synopsis Atoms and their real module evidence. Separate behavior that should be adopted into RMEDO from behavior that should change in code. Account for Atom-ID/version-to-module mapping and source/code mismatches. Record an empty active-I census if applicable and continue with the code/spec evidence and handoff; do not create an I Atom merely to fill the task. Create or revise a Synopsis only for an actual evidence-backed need under its current definition. Do not implement.

## Subtasks

Each subtask is a batch of at most 15–20 minutes. Repeat per Scope Unit; give each subagent one Scope Unit.

- [ ] Check the next same-Scope evidence batch and fix its inputs.
- [ ] Review pass one using actual sources and prepare the scoped dispositions.
- [ ] Fix pass-one findings.
- [ ] Run independent pass two on the corrected evidence and handoff.
- [ ] Fix pass-two findings and recheck affected earlier criteria.
- [ ] Record a small Work Report and the exact handoff.

## Definition of Done

Every reviewed active Synopsis has an evidence-backed disposition; accepted specification additions return through source review, and code corrections are prepared for a separate Epic. Tasks track work; specification changes belong in RMEDO. No runtime implementation is performed here.

## Carried Synopsis work

P2847 is superseded by this full-cycle review. Preserve Resolved I9 and the existing C714 issue; do not reopen an inactive Synopsis automatically or claim that cancellation repaired its code/evidence issue.

Any specification correction accepted during this task returns through the affected review/adoption checks and a fresh main-subject graph rebuild/recheck before handoff.
