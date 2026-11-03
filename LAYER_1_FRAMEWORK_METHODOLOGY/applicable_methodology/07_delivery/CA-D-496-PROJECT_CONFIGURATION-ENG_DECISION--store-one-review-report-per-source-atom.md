---
atom_id: CA-D-496
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
version: 24
updated_at: 2026-11-02 00:18:22 +0400
subjects:
  active: Entity/Object/Occurrent/Execution/Workflow Run
  passive:
  - Atom
  - Atom/(.Role := Evaluation)
  - Carrier/File
  - Projection
relations: {}
tier: 3
role: Delivery
form: Decision
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/07_delivery/CA-D-496-PROJECT_CONFIGURATION-ENG_DECISION--store-one-review-report-per-source-atom.md
  source_atom_id: CA-D-496
  source_atom_revision: 24
  source_sha256: c73c62d993818f3455d0a5ebe22f3c29b92c156841b8d54e52da034b78bc0382
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Store one review report per source Atom

## Claim scope

temporary evidence Carriers of a local RMED Atom review Run.

## Claim

the Run **must** store its temporary evidence under **`=1`** caller-admitted directory using this layout:

- `progress.json`: the original selection, per-Atom path **and** identity, current Step, state, report path, assigned worker, applicable context setting, **and** any blocked **or** unfinished work. a short handoff records the current Atom, completed edits, **and** next work **in** this file.
- `reports/<ordinal>.json`: **`=1`** report per selected Carrier, using its fixed four-digit ordinal. retain the check result **and** later applied corrections **in** this same file.

**every** report **must** contain the source path, carried Atom ID **and** Version, source observation, **all** **`=6`** local check outcomes, concise evidence, confirmed findings, unresolved coverage, applied corrections, **and** current state. a confirmed finding includes its location, source passage, applicable rule, **and** proposed fix. record the original checked source digest once so the fixer can notice concurrent changes.

## Details

shared checking rules **may** be stored once; reviewers receive their relevant actual contents. an existing mechanical report **may** be linked as supporting evidence. separate raw-part files, proposal reports, admission receipts, checkpoint files, **and** closure certificates are **not** required by this Workflow.

states are `pending`, `checked_clean`, `needs_fix`, `fixed_not_rechecked`, **or** `blocked`. `fixed_not_rechecked` records applied corrections **after** **all** initial checks conclude **and** findings are corrected **or** rejected with reasons, **without** claiming a post-fix pass. missing identity, unfinished checks, **or** unresolved findings retain `blocked`, including **when** safe partial corrections were applied.

progress records `reported_result`, `check_complete`, **and** `complete` separately from the derived current `state`. Run totals distinguish reports received, complete initial checks, **and** completed Atoms. preserve original reports **and** their gaps as evidence; reporting **or** editing an Atom does **not** complete unperformed checks. excluded checks are **not** marked as passed.

preserve earlier reports **and** completed work. a workflow-packaging **or** context-budget change alone does **not** invalidate a review of unchanged content under unchanged checking criteria. changed Atom content **or** a changed applicable criterion makes its earlier check historical; this Workflow does **not** automatically recheck it.
