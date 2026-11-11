---
identity:
  id: CA-P-2878
  ref_id: CA-P-2878
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
  updated_at: 2026-11-10 19:14:23 +0400
destination:
  file:
    name: CA-P-2878-TASK--review-and-fix-engine-numeric-tiers.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/020_done/CA-P-2767-EPIC--engine-spec-refinement-stage-two/020_done
relations:
  IS_BLOCKED_BY:
  - CA-P-2877
---

## Summary

Review and fix Engine numeric Tiers

## Objective

Review numeric Tiers and applicable graph-ordering rules after relation and Scope corrections. Recheck changed endpoints, ancestry and admitted exceptions. Preserve the distinction between a Tier number and its optional label.

## Subtasks

Each subtask is a batch of at most 15–20 minutes. Repeat per Scope Unit; give each subagent one Scope Unit.

- [x] Review pass one on a same-Scope batch.
- [x] Fix findings and prepare or refine the affected Drafts.
- [x] Run independent pass two on the corrected batch.
- [x] Fix pass-two findings and recheck affected earlier criteria.
- [x] Record a small Work Report and thin coverage entries.

## Definition of Done

Every changed governing relation passes the current Tier/Scope rules or has an explicit unresolved disposition; no named tier is substituted for numeric data. Tasks track work; specification changes belong in RMEDO. No runtime implementation is performed here.

## Final source checkpoint

Numeric ordering now passes for 364 selected candidate Atoms and 373 governing links. Every candidate has a declared owner and numeric Tier; all selected governing targets follow the same-Scope lower-Tier rule or permitted ancestor/explicit exception, with no cycle. Actual Header pins are recorded in candidate-ordering-validation.json. Recheck after any endpoint, owner, Tier or relation edit and again after adoption.
