---
subjects:
  active: CAPRMEDIO_MODEL <+ Atom.Header.Tier
  passive:
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Requirement)/(.Header.Form := Project Goal)'
  - CAPRMEDIO_MODEL <+ Project
  - CAPRMEDIO_MODEL <+ Atom.Header.Tier
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/Operator
version: 12
updated_at: 2026-11-02 00:18:22 +0400
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


Project Goal Atoms.


Every Requirement Atom of Type Project Goal **must** target the Project, be owned by its Operator Actor instead of a Local Scope Unit, and carry exactly one numeric Tier `-1`. Tier `-1` is explicit, is not omitted, and is outside the ordinary nonnegative Tier range. This Rule does not impose an arbitrary Type-to-Tier restriction beyond verified Project Goal identity and ownership.

## Details

The Project Goal retains its Operator Actor owner. CA-R-2149 uses its Target Project only as the derived ordering context; ordinary Goal ownership and Scope ordering are unchanged.
