---
atom_id: CA-R-2469
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: (Node, Node/**, .**)
version: 4
updated_at: 2026-11-02 08:06:47 +0400
relations: {}
tier: 3
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2469-CORE_META_MODEL-RULE--require-one-declaration-for-each-node.md
  source_atom_id: CA-R-2469
  source_atom_revision: 4
  source_sha256: 9069df73ee68904f926f545f9c999bd6d520a69e1b582c6a398fbe894a4eb290
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---

## Summary

Require one Declaration for each Node

## Claim

Evaluate ownership within the selected effective MODEL. Each member selected by (Node, Node/**, .**), including the root and each Property, has exactly one effective Current authoritative Requirement/Form: Declaration addressing that Node.

Count inherited Current Declarations and explicit local replacements after MODEL override resolution. A replaced base Declaration remains available in its base MODEL and is not a second effective owner in the local MODEL. Drafts and archives are not Current owners. Other Atoms may address the same Node.

```CFEL
Atom/(.Role: Requirement)/(.Form: Declaration)// ((HAS_ACTIVE_SUBJECT)){:1} (Node, Node/**, .**)
```

The count uses only the effective Current Declaration-to-Node links in that MODEL. HAS_ACTIVE_SUBJECT is the canonical Relation obtained from the dedicated active Subject field; obtaining its value from that field does not make it a derived view of another Relation.
