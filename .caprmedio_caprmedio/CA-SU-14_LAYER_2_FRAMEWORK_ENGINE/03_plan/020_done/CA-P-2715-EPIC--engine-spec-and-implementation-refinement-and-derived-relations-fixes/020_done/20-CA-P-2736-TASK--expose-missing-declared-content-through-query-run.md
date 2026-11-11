---
identity:
  id: CA-P-2736
  ref_id: CA-P-2736
context:
  container:
    atom: CA-P-2715
  role: Plan
  form: Plan
  label: Task
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom.Content
  tier: 4
relations:
  IS_BLOCKED_BY:
  - CA-P-2716
state:
  status: Done
  version: 3
  updated_at: 2026-11-09 01:40:38 +0400
destination:
  file:
    name: 20-CA-P-2736-TASK--expose-missing-declared-content-through-query-run.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/020_done/CA-P-2715-EPIC--engine-spec-and-implementation-refinement-and-derived-relations-fixes/020_done
author: Anatoly Maslennikov
---

## Summary

Expose missing declared Content through query_run

## Objective

Make the admitted Content needed for this migration queryable before creating source-copy Drafts. Fetch Atom data through query_run.

## Subtasks

- [x] Compare active Content declarations with the current SQL schema and compiler. (ETA: 15 min.)
- [ ] Prepare narrow missing Declaration Drafts from established role/content meanings; ask for any unsettled meaning. (ETA: 15–20 min per batch.)
- [ ] Review and improve the packet twice, then promote only accepted declarations. (ETA: 15–20 min per pass/batch.)
- [ ] Verify schema regeneration and real Atom Content through query_run; fix implementation only if a confirmed compiler defect remains. (ETA: 15–20 min per work unit.)

## Findings

The current literal schema matches its five declared value paths. Legacy Operation is not a formal path declaration. D479 retains legacy C/A/P/O readability, but this does not give the compiler an exact path. Claim Scope is currently prose in Claim.Prose Claim; do not invent a new path for it.

## Working procedure

Review and fix the next work unit first. Below 90% confidence, re-read Operator input, then ask if still uncertain. Keep one small P / Work Report. Main judgments use GPT-6.1 Sol High; no worker owns more than one Scope Unit.

## Acceptance

Accepted literal declarations produce the missing SQL columns and real source values through query_run. No raw-file SQL access, handwritten heading whitelist or raw-body public bucket is introduced. Unsettled property semantics remain explicit blockers.
