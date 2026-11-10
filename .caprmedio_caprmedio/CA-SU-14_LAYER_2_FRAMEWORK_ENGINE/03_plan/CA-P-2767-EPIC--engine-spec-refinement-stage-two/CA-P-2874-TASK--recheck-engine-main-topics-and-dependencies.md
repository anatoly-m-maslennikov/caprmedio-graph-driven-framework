---
identity:
  id: CA-P-2874
  ref_id: CA-P-2874
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
  version: 3
  updated_at: 2026-11-10 11:49:56 +0400
destination:
  file:
    name: CA-P-2874-TASK--recheck-engine-main-topics-and-dependencies.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/CA-P-2767-EPIC--engine-spec-refinement-stage-two
relations:
  IS_BLOCKED_BY:
  - CA-P-2872
  - CA-P-2873
---

## Summary

Recheck Engine main topics and dependencies

## Objective

Recheck main subjects and dependencies after claim, Role, Scope and merge corrections. Verify canonical targets against current Declarations. Keep unresolved addresses explicit rather than applying a global separator replacement.

## Subtasks

Each subtask is a batch of at most 15–20 minutes. Repeat per Scope Unit; give each subagent one Scope Unit.

- [x] Review pass one on a same-Scope batch.
- [x] Fix findings and prepare or refine the affected Drafts.
- [x] Run independent pass two on the corrected batch.
- [x] Fix pass-two findings and recheck affected earlier criteria.
- [x] Record a small Work Report and thin coverage entries.

## Definition of Done

Every changed subject has authority evidence; both main subjects and dependencies are checked, with thin tracking and explicit unresolved cases. Tasks track work; specification changes belong in RMEDO. No runtime implementation is performed here.

## Reviewed inputs

The bounded corrective P2872 and P2873 rechecks are Done. Recheck the fresh effective candidate inventory, including newly identified sources, moved/retyped Drafts and survivor changes. Review both main subjects and dependencies against source Declarations and receiving permissions. Include the two Graph UI topic findings and R2430 duplicate dependency. C721 records the root/admission question; do not introduce a global alias or separator substitution. C723 prevents an unrelated Core Draft from shadowing the Workbench identity. No source promotion precedes the remaining full review cycle.

## Result

Checked main subjects and dependencies for 415 effective candidate carriers. Prepared 168 topic-only candidate edits, corrected sixteen further topic values across seven PROMPTS Drafts, and independently rechecked the fixes. Current defining sources attest the exact target paths; no global root or separator alias was introduced. C721 preserves the bounded unresolved bridge/admission cases for the policy/admission check. Retirements and trial withdrawals remain explicit adoption actions. All 360 Current input RMEDO files remain unchanged. See P2889, engine-topic-recheck-20261110.tsv and topic-review-validation.json.
