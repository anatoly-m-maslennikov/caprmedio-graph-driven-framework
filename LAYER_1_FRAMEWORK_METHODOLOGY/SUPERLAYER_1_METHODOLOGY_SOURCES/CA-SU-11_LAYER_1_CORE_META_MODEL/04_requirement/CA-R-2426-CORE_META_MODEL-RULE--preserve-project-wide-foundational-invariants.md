---
version: 3
updated_at: 2026-11-02 00:18:22 +0400
relations:
  child_of:
  - CA-M-447
subjects:
  active: CAPRMEDIO_MODEL <+ Project
  passive:
  - CAPRMEDIO_MODEL <+ Project
  - CAPRMEDIO_MODEL <+ Atom.Header.Tier
  - CAPRMEDIO_MODEL <+ Atom.Header.Role
atom_id: CA-R-2426
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Rule
---
## Summary

Preserve Project-wide foundational invariants

## Claim

### Prose Claim


Project-wide foundational invariants.


CAPRMEDIO must preserve all irreducible governed invariants that apply across the entire current Project independently of Scope Unit ancestry, scope label, Content Role, Artifact form, Extension, Project Configuration or substrate. Those Project-wide foundational invariants retain their applicability throughout the Project; Project-owned Tier `0` Atoms express their foundational authority. This does not make every local or Project-owned Tier `0` Atom Project-wide, add a conflict winner based on Tier, or impose a fixed Role checklist.
