---
atom_id: CA-R-2469
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: (Node, Node/**, .**)
version: 4
updated_at: 2026-11-02 07:52:54 +0400
relations: {}
tier: 3
role: Requirement
form: Rule
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
