---
identity:
  id: CA-P-2871
  ref_id: CA-P-2871@2
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
  updated_at: 2026-11-10 06:56:53 +0400
destination:
  file:
    name: CA-P-2871@2-TASK--review-and-fix-engine-roles-and-scope-placement.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/CA-P-2767-EPIC--engine-spec-refinement-stage-two/archive
relations:
  IS_BLOCKED_BY:
  - CA-P-2870
---

## Summary

Review and fix Engine Roles and Scope placement

## Objective

Check actual Claims against current Role definitions and the latest Operator corrections. Find internal technical material incorrectly classified as a Requirement; check outcome Requirements independently of their Subject branch. Review owning Scope Units, promotion/demotion and permissions. Prepare role changes with replacement lineage and connected-reference plans.

## Subtasks

Each subtask is a batch of at most 15–20 minutes. Repeat per Scope Unit; give each subagent one Scope Unit.

- [ ] Review pass one on a same-Scope batch.
- [ ] Fix findings and prepare or refine the affected Drafts.
- [ ] Run independent pass two on the corrected batch.
- [ ] Fix pass-two findings and recheck affected earlier criteria.
- [ ] Record a small Work Report and thin coverage entries.

## Definition of Done

Role and Scope decisions are evidenced, source permissions are checked, and any broader/narrower move or role replacement has a reviewed Draft and impact record. Tasks track work; specification changes belong in RMEDO. No runtime implementation is performed here.

## Reviewed inputs

P2870 is Done. Use the 494-source snapshot, corrected Claim Drafts, the latest Operator decisions and the independent review packets. Missing identity is not a semantic-review hold. Treat carrier-encoded lower_snake named values as valid under D657; do not title-case them merely to work around a reader bug. Keep native-plugin extraction D707 deferred.
