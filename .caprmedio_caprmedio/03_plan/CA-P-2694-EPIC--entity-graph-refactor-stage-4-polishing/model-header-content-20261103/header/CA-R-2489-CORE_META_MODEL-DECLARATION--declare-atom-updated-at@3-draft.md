---
atom_id: CA-R-2489@3-draft
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Draft
subjects:
  active: CAPRMEDIO_MODEL <+ Atom.Header.Updated At
version: 3
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
---
## Summary

Declare Atom.Header.Updated At

## Claim

### Formal Claim

```CFEL
Atom.Header.Updated At{:1}: [datetime]{:1};
Atom.Header.Updated At.*[]{:0};
Atom//$atom.Header.Updated At == MAX(Event Record//(.object_output{=1}, .object_output.version{=1}, .object_output.id = $atom.Header.ID, .object_output.version = $atom.Header.Version, (.action = create OR .action = update)).happened_at)
```
