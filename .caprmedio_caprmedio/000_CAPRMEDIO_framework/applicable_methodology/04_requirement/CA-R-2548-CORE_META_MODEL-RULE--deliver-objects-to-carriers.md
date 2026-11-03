---
atom_id: CA-R-2548
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO <+ MODEL <+ CFEL
version: 2
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2548-CORE_META_MODEL-RULE--deliver-objects-to-carriers.md
  source_atom_id: CA-R-2548
  source_atom_revision: 2
  source_sha256: b616f21c9395a82014634c502f7ac02748915e7aba4d18d1434652119d5d3ba9
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Deliver Objects to Carriers

## Claim

- `>>` delivers an Object to the referenced Carrier or Carrier part.
- A selection delivers its selected Objects.
- `@` refers to an already declared target.
- `!(selectors)` excludes those branches from a selection.
- Relative exclusions use the selection's base.
- `=` states an equality condition.
