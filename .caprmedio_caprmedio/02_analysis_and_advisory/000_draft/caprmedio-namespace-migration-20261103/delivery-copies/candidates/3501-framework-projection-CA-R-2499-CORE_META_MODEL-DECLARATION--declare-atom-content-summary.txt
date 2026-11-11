---
atom_id: CA-R-2499
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO <+ MODEL <+ Atom.Content.Summary
version: 2
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2499-CORE_META_MODEL-DECLARATION--declare-atom-content-summary.md
  source_atom_id: CA-R-2499
  source_atom_revision: 2
  source_sha256: f9e29fdc811390613cb190594cff6410895872a86a158ef91a771db087192041
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Declare Atom.Content.Summary

## Claim

```CFEL
Atom.Content.Summary{:1}: [markdown]{:1};
Atom.Content.Summary.*[]{:0};
DETERMINES(
  Atom//,
  (.ID),
  (.Content.Summary),
  (Atom.Status >| Status Group = Current) OR (Atom.Status >| Status Group = Archived)
)
```
