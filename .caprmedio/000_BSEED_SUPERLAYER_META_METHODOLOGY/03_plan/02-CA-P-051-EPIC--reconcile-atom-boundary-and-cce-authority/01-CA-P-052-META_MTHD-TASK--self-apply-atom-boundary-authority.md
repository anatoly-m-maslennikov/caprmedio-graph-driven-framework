---
atom_id: CA-P-052
cce_version: cce_1
cce_form: obligation
subjects:
  - development-flow
  - atom-boundary
version: 1
updated_at: 2026-08-23 01:44:00
---
# Self-apply Atom-boundary authority

THE Operator MUST make every Atom in Task Scope comply with the active Atom-boundary authority.

## Scope

`(ALL Atoms WHERE (subjects IN (atom-boundary) AND Content Role != PLAN))`

## Definition of Done

THE Task is NOT DONE IF (ANY Atom in Task Scope violates active authority for one Atom, one Claim, one Claim Scope, Current-scope Atoms, or Relational Atoms OR ANY semantic resolution below 98 percent lacks an Operator disposition OR the Task Scope Resolution is not recorded).

## Details

Apply CA-M-119 to every changed Atom and preserve each accepted Claim while resolving conflicts among the Atom-boundary authorities.
