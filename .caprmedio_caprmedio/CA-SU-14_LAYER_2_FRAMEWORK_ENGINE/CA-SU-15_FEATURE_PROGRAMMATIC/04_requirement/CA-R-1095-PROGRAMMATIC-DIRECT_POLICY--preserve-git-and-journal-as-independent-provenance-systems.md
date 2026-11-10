---
identity:
  atom_id: CA-R-1095
  ref_id: CA-R-1095
context:
  container:
    scope_unit: CA-SU-15
  role: Requirement
  form: Direct Policy
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Quality
      <+ Traceability
  tier: 3
state:
  status: Active
  version: 24
  updated_at: 2026-11-10 20:47:54 +0400
destination:
  file:
    name: CA-R-1095-PROGRAMMATIC-DIRECT_POLICY--preserve-git-and-journal-as-independent-provenance-systems.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/04_requirement
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
---
## Summary

Preserve Git and Journal as independent provenance systems

## Claim scope

PROGRAMMATIC behavior governing PROGRAMMATIC.

## Claim

### Prose Claim

PROGRAMMATIC **must** preserve Git **and** the Project Work Journal as two independent, intentionally redundant provenance **and** history systems. Git owns carrier bytes, tree state, commit identity, **and** ancestry. The Journal owns governed semantic action history, human-origin Initiative context, affected identities **and** revisions, **and** explicit cross-system bindings. **every** committed Journal carrier revision is independently recoverable through Git, but neither system substitutes for the other.

Technical warnings emitted while a bounded scan skips an isolated schema-invalid
Atom are not business Journal history. They must not fabricate a business action,
Run, or Journal record, or rewrite historical Journal carriers. The operation must
report `complete: false` when the scan is incomplete. The business Journal remains
business-only.

One sealed action **may** pass through `git_complete_journal_pending`, `journal_recorded_git_pending`, **and** `reconciled`. A real-change commit **may** complete **before** its canonical Journal record is appended; a Journal record **may** be prepared **before** that commit, but its canonical binding is complete **only** once the exact reachable real-change commit SHA is known. `reconciled` requires **=1** canonical action record, **=1** reachable real-change commit binding, **and** a later separate Git commit that versions the Journal carrier containing that record. The Journal record does **not** embed the SHA of the Git commit that **contains** that same record: reconciliation derives that Journal-to-Git binding from the exact carrier revision **and** reachable Git history, avoiding a self-referential digest cycle.

Journal incompleteness or unreconciled bindings **must not** gate Atom creation, update, Status change, promotion, ordinary later work, or release. Preserve observable pending states and detect missing events, unreachable commits, duplicates, digest mismatches and Journal commit lag; report or repair them without turning Journal completeness into effect-admission permission. Independent Git and other applicable release safeguards remain unchanged.

