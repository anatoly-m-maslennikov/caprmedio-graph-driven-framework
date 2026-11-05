---
atom_id: CA-R-2469
ref_id: CA-R-2469
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
topics:
  main_subject: CAPRMEDIO_MODEL <+ (Node, Node.**)
version: 4
updated_at: 2026-11-02 08:06:47 +0400
tier: 3
role: Requirement
form: Rule
container:
  scope_unit: CA-SU-11
carrier_destination:
  file:
    name: CA-R-2469-CORE_META_MODEL-RULE--require-one-declaration-for-each-node.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---

## Summary

Require one Declaration for each Node

## Claim

### Formal Claim

```CFEL
# instances
Atom/(.Header.Role: Requirement)/(.Header.Form: Declaration)//$atom ((HAS_ACTIVE_SUBJECT)){::1} (Node, Node.**)
```

### Prose Claim


Evaluate ownership within the selected effective MODEL. Each member selected by (Node, Node.**), including the root and each Property, has exactly one effective Current authoritative Requirement/Form: Declaration addressing that Node.

Count inherited Current Declarations and explicit local replacements after MODEL override resolution. A replaced base Declaration remains available in its base MODEL and is not a second effective owner in the local MODEL. Drafts and archives are not Current owners. Other Atoms may address the same Node.


The count uses only the effective Current Declaration-to-Node links in that MODEL. HAS_ACTIVE_SUBJECT is the canonical Relation obtained from the dedicated active Subject field; obtaining its value from that field does not make it a derived view of another Relation.
