---
identity:
  id: CA-P-2873
  ref_id: CA-P-2873@2
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
  updated_at: 2026-11-10 07:31:05 +0400
destination:
  file:
    name: CA-P-2873@2-TASK--review-and-fix-engine-duplication-with-dry.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/CA-P-2767-EPIC--engine-spec-refinement-stage-two/archive
relations:
  IS_BLOCKED_BY:
  - CA-P-2871
---

## Summary

Review and fix Engine duplication with DRY

## Objective

Apply current DRY policy and the accepted Summary-merge criterion to all eligible sources. Prefer existing survivors where they cover the claim. Preserve unique constraints and Evaluation coverage; check cross-Role duplicates without treating a different Role as proof of a distinct claim.

## Subtasks

Each subtask is a batch of at most 15–20 minutes. Repeat per Scope Unit; give each subagent one Scope Unit.

- [ ] Review pass one on a same-Scope batch.
- [ ] Fix findings and prepare or refine the affected Drafts.
- [ ] Run independent pass two on the corrected batch.
- [ ] Fix pass-two findings and recheck affected earlier criteria.
- [ ] Record a small Work Report and thin coverage entries.

## Definition of Done

Merge and retain decisions preserve meaning and coverage, identify the survivor and replacement lineage, and account for affected references. Tasks track work; specification changes belong in RMEDO. No runtime implementation is performed here.

## Reviewed inputs

P2871 is Done. Use the reviewed Role/Scope candidates and the effective candidate inventory. Do not count a Current predecessor and its prepared replacement as two retained claims. Keep idless sources reviewable by path/hash. Preserve explicit native-plugin, standalone-chat and old-Tool deferrals. Each same-Scope report records MECE, DRY and Form findings separately; shared source edits remain root-owned. Recheck affected claim and Role/Scope decisions after a correction.
