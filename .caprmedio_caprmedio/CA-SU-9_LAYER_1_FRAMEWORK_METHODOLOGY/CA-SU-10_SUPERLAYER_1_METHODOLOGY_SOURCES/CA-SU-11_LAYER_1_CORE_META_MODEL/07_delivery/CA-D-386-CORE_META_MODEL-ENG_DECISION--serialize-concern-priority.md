---
subjects:
  active: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Concern).Header.Priority
  passive:
  - CAPRMEDIO_MODEL <+ Atom.Header.Role
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Concern).Header.Priority
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan)
version: 23
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-D-386
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Delivery
form: Decision
---
## Summary

Serialize Concern Priority

## Claim

### Prose Claim


Concern Atom Carriers and non-Concern Content Role Atom Carriers.


a Concern Atom Carrier **must** serialize **`=1`** selected Priority as `priority` with the lowercase value `high`, `medium`, **or** `low`. **every** non-Concern Content Role Atom Carrier **must** omit `priority`; virtual `highest` **must not** be stored.
