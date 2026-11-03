---
subjects:
  active: CAPRMEDIO_MODEL <+ Atom.Header.Subjects
  passive:
  - CAPRMEDIO_MODEL <+ CFEL > Relation//GOVERNS
  - CAPRMEDIO_MODEL <+ CFEL > Relation//DEPENDS_ON
  - CAPRMEDIO_MODEL <+ Atom.Header.Subjects
version: 30
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-R-1202
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Rule
---
## Summary

Resolve Every Direct Subject Target Once

## Claim

### Prose Claim


direct GOVERNS and DEPENDS_ON values in an Atom's Subjects Property.


**every** direct GOVERNS value **and** **every** direct DEPENDS_ON value **in** an Atom's Subjects Property **must** resolve **to** **`=1`** canonical Subject Target. resolution **must not** require an intermediate Subject/Entity **or** Subject/Reference Property **or** a repeated target-kind field.
