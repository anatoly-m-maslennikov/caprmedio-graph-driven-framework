---
subjects:
  active: Scope Unit
  passive:
  - Atom/(.Role := Requirement)/(.Form := Scope Unit Declaration)
  - Project
version: 1
updated_at: 2026-11-02 19:17:40 +0400
relations: {}
atom_id: CA-R-2688
status: Active
tier: 2
form: Rule
role: Requirement
---
## Summary

Require one Scope Unit Declaration

## Claim scope

Each Scope Unit, including Project.

## Claim

Every specific Scope Unit, including Project, has exactly one external Requirement Atom with Form `Scope Unit Declaration` and an active Subject naming that Scope Unit. The Declaration is the sole structural authority for its declared values.

The Declaration carries the Scope Unit Name, ordered state, optional Label, conditional order.number and direct containment. A non-root Scope Unit also has a stable ID. Project is unordered and has neither Scope Unit ID nor order.number. A non-root Scope Unit has one direct Parent; Project has none.

Authority and Delivery folder names are derived from the Declaration. `project_structure.toml` is not a governing source.

## Details

The Project Declaration is externally Operator-owned, like the Project Goal. The Operator is an Actor, not a Scope Unit.
