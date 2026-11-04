---
subjects:
  active: CAPRMEDIO_MODEL <+ Atom.Header.Tier
  passive:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Form := Goal)
  - CAPRMEDIO_MODEL <+ Atom.Header.Subjects.Active
  - CAPRMEDIO_MODEL <+ Project
  - CAPRMEDIO_MODEL <+ Atom.Header.Tier
version: 13
updated_at: 2026-11-04 09:19:08 +0400
relations: {}
atom_id: CA-R-2132
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
tier: 1
status: Active
role: Requirement
form: Rule
---
## Summary

Assign Project Goal Tier Minus One

## Claim

### Prose Claim


Atoms of Form Goal whose active Subject resolves to the Project Scope Unit root.


Every Atom of Form Goal whose active Subject resolves to the Project Scope Unit root **must** carry exactly one numeric Tier `-1`. Tier `-1` is explicit, is not omitted, and is outside the ordinary nonnegative Tier range. This Rule does not impose an additional Type-to-Tier restriction.

## Details

Under CA-R-2149, the Project resolved from the active Subject is the ordering context.
