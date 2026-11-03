---
atom_id: CA-R-1958
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Carrier
relations:
  child_of:
  - CA-R-1174
version: 15
updated_at: 2026-11-02 00:18:22 +0400
tier: 1
role: Requirement
form: Entity Definition
---
## Summary

Define Entity/Carrier

## Claim scope

Carrier representations of Continuants.

## Claim

A Carrier **means** a storage representation of a Continuant, distinct from what it represents. A Carrier can represent a record of an Occurrent, **not** the Occurrent itself.

### Formal claim

```text
Carrier.ID[string]{1}
Carrier.Canonical Address[string]{1}
Carrier.Format[string]{1}
```

For implementation_of, the direct owner is the governed Implementation Carrier and each tuple targets the specification Atom it implements. For evidence_for, the direct owner is the evidence Carrier and each tuple targets the Evaluation or Implementation Carrier it supports. These are endpoint permissions, not extra fields on reusable Relation Types or additional storage facts for their derived inverses.
