---
atom_id: CA-P-2358
content_role: Plan
type: Plan
label: Task
work_sequence_number: 2
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
status: Done
subjects:
  governs: Subject/Graph Node/Engineering/Continuant/Tool
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Atom
  - Subject/Graph Node/Domain/Continuant/Scope Unit
  - Subject/Graph Node/Engineering/Action
  - Subject/Graph Node/Engineering/Workflow
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Plan'
version: 9
updated_at: 2026-10-25 17:32:27 +0400
relations:
  is_decomposition_of:
  - CA-P-2301
tier: 3
---
# Summary

Verify private Atom Read and Query receivers

## Objective

Independently verify the actual private O047/O046 receivers against accepted RMEDO and final selected source/schema/permission bindings.

## Details

Own independent verification and targeted tests only, not the production receiver. Prepare isolated fixtures while P2357 runs; final acceptance consumes its stable implementation and exact reviewed source pins. Exercise actual receiver calls within genuine selected execution and recorded nonterminal Action Sessions. Independently establish full-ID Read, exact supplied Query frontier/criteria and completeness, empty/singular/multiple matches, correct observed identity/Version/state, and no hidden Query/Read progression. Cover missing, ambiguous, unreadable, malformed, denied, stale source/frontier, wrong Action/root/Session, unrecorded and terminal Action cases. Inspection-only unknown logical Revision/currentness must not be substituted for any verified evidence required by the receiving contract.

Estimated own work: up to 15 minutes. Split larger work before exceeding this bound. Root controls Plans and Git; implementation and independent verification own disjoint files. This child adds no public route, manifest, live Settings change, existing-caller migration, runtime activation or live Core migration.

### Definition of Done

Independent actual positive/refusal cases pass on exact final pins, including truthful incomplete-source diagnostics and no write effects. Compare affected source and Journal/Run state around the receiver itself: it creates no second Run or Journal event and does not change sources. Existing callers, Settings and runtime are not changed by this work; preserve unrelated pre-existing edits. Report exact results and limitations to Root. This child does not accept publication, registered routes or broader parent/runtime completion. Accepted source/history gates remain in force; no caller flag, guessed source mapping or inspection-only unknown evidence replaces them.

### Completion checkpoint

Independent actual receiver checks in committed `5d60b9053` cover full Read and exact empty/singular/multiple Query, malformed/incomplete/late-changed evidence, denied/stale admission, wrong/unstarted/terminal Sessions, retained sources/frontier and same-identity rehashed/resealed schema/Action substitution refusal. Source and Journal/Run snapshots around receiver calls prove empty effects, no source writes and no second Run/Journal event. Root's fresh final connector regression run passed 306 tests in 73.493 seconds; reopened accepted source/action digests remain current.

Final receiver SHA-256: `b111433608510a6021ca1f6e19e4b12e400bb14dc1989882fa23f5a62aff434d`; independent test SHA-256: `bcc54a355327689e31dd4cace3292550d5eb115aefa859a936fc3aed9100d201`. Independent coverage accepts only this private receiving boundary, not public routes, caller migration, live Settings/runtime or broader parent completion.
