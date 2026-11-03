---
atom_id: CA-R-2571
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Event Record
version: 2
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Requirement
form: Rule
---
## Summary

Capture Atom input and output metadata

## Claim

### Prose Claim


An Event Record for Atom creation or update has object_output. An update record also has object_input; creation input is optional.

For each present Atom input or output, the Event Record captures:

- Atom.Header.ID.
- Atom.Header.Version.
- Atom.Header.Updated At.

object_input contains the values before the change. object_output contains the values after it. Their IDs may differ. The captured values remain as recorded.
