---
subjects:
  governs: provenance
  depends_on: []
version: 12
updated_at: '2026-10-21T17:26:17Z'
atom_id: CA-R-1095@12
content_role: Requirement
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
status: Archived
author: Anatoly Maslennikov
relations: {}
---
# Summary

Preserve Git and Journal as independent provenance systems

## Scope

PROGRAMMATIC behavior governing PROGRAMMATIC.

## Claim

PROGRAMMATIC **must** preserve Git **and** the Project Work Journal as two independent, intentionally redundant provenance **and** history systems. Git owns carrier bytes, tree state, commit identity, **and** ancestry. The Journal owns governed semantic action history, human-origin Initiative context, affected identities **and** revisions, **and** explicit cross-system bindings. **every** committed Journal carrier revision is independently recoverable through Git, but neither system substitutes for the other.

Technical warnings emitted while a bounded scan skips an isolated schema-invalid
Atom belong to the technical logging stream, not to the business Journal history.
For the selected Docker runtime, emit structured warnings to `stderr` with the
validated Project prefix from Project settings, repository-relative path, and
reason; Docker's local logging driver uses bounded rotation `max-size=10m` and
`max-file=3`, `mode=non-blocking`, and `max-buffer-size=1m`. When the buffer is
full, new technical messages may be dropped so the primary operation does not
stall; the logging failure remains observable. The Project prefix comes from the
existing bound Project selection and canonical prefix-field validation and must
never be guessed from a path, container, process, or caller. This uses the selected
immutable settings view, without an additional settings carrier or a claim of full
SettingsReader conformance. Docker logs are removed with the container. Warnings
must not fabricate a business action, Run, or Journal record, must not rewrite
historical Journal carriers, and must leave the operation `complete: false` when
the scan is incomplete. No separate local log directory is created; the business
Journal remains business-only.

One sealed action **may** pass through `git_complete_journal_pending`, `journal_recorded_git_pending`, **and** `reconciled`. A real-change commit **may** complete **before** its canonical Journal record is appended; a Journal record **may** be prepared **before** that commit, but its canonical binding is complete **only** once the exact reachable real-change commit SHA is known. `reconciled` requires **=1** canonical action record, **=1** reachable real-change commit binding, **and** a later separate Git commit that versions the Journal carrier containing that record. The Journal record does **not** embed the SHA of the Git commit that **contains** that same record: reconciliation derives that Journal-to-Git binding from the exact carrier revision **and** reachable Git history, avoiding a self-referential digest cycle.

Journal incompleteness or unreconciled bindings **must not** gate Atom creation, update, Status change, promotion, ordinary later work, or release. Preserve observable pending states and detect missing events, unreachable commits, duplicates, digest mismatches and Journal commit lag; report or repair them without turning Journal completeness into effect-admission permission. Independent Git and other applicable release safeguards remain unchanged.

## Details
