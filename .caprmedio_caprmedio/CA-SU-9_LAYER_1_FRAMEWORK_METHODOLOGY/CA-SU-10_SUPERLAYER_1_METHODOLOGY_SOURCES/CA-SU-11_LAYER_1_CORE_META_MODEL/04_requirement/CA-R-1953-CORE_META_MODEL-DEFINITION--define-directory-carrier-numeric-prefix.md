---
atom_id: CA-R-1953
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: Carrier/Directory.Numeric Prefix
relations:
  child_of:
  - CA-R-1174
version: 13
updated_at: 2026-11-02 00:18:22 +0400
tier: 3
role: Requirement
form: Entity Definition
---
## Summary

Define Directory Carrier.Numeric Prefix

## Claim scope

Directory Carrier names whose applicable naming convention uses a numeric prefix.

## Claim

A Directory Carrier's Numeric Prefix **means** the leading numeric part of its Name when the applicable naming convention uses one.

### Formal claim

```text
Directory.Numeric Prefix[int]{0..1}
```

## Details

CA-D-445 allows explicit native bindings. CA-D-651 governs any registered Atom numeric-Tier filename token grammar; this definition does not require a prefix for every directory or admit a Structural Level component.

Active CA-R-2515 currently assigns Carrier definitions and classification to Delivery. That conflict remains for the later content migration; this draft does not change or supersede active rules.
