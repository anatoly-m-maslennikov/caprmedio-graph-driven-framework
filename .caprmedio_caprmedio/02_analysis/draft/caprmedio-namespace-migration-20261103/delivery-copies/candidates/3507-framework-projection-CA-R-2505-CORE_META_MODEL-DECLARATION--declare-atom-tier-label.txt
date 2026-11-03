---
atom_id: CA-R-2505
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO <+ MODEL <+ Atom.Tier.Label
version: 2
relations: {}
tier: 3
updated_at: 2026-11-02 00:18:22 +0400
role: Requirement
form: Declaration
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2505-CORE_META_MODEL-DECLARATION--declare-atom-tier-label.md
  source_atom_id: CA-R-2505
  source_atom_revision: 2
  source_sha256: 8d47c85725d9922b89f794a300a3cdca66afcd99424dff056399405f56b4796a
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Declare Atom.Tier.Label

## Claim

```CFEL
Atom.Tier.Label{:0..1}: [string]{:1};
Atom.Tier.Label.*[]{:0};
IF ((Atom.Tier.Label{=1}) AND (Atom.Tier = 0)) THEN (Atom.Tier.Label == Scope Contract);
IF ((Atom.Tier.Label{=1}) AND (Atom.Tier = 1)) THEN (Atom.Tier.Label == Core);
IF ((Atom.Tier.Label{=1}) AND (Atom.Tier = 2)) THEN (Atom.Tier.Label == General);
IF ((Atom.Tier.Label{=1}) AND (Atom.Tier = 3)) THEN (Atom.Tier.Label == Standard);
IF ((Atom.Tier.Label{=1}) AND (Atom.Tier = 4)) THEN (Atom.Tier.Label == Detail)
```
