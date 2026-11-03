---
atom_id: CA-R-1948
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Carrier.Canonical Address.Segment
relations:
  child_of:
  - CA-R-1174
version: 12
updated_at: 2026-11-02 00:18:22 +0400
tier: 3
role: Requirement
form: Entity Definition
---
## Summary

Define Carrier.Canonical Address.Segment

## Claim scope

Carriers whose canonical address format has component segments.

## Claim

A Canonical Address Segment **means** one component of a Carrier's Canonical Address under its applicable address format.

### Formal claim

```text
Carrier.Canonical Address.Segment[string]{1}
```

## Details

CA-D-301 governs project-owned address segments; CA-D-352 treats status subdirectories as placement components. Filesystem separators and portable-name restrictions are not imposed on every database address by this definition.

Active CA-R-2515 currently assigns Carrier definitions and classification to Delivery. That conflict remains for the later content migration; this draft does not change or supersede active rules.
