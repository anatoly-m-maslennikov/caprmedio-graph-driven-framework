---
subjects:
  active: Atom/(.Role := Method)
version: 30
updated_at: 2026-11-02 19:44:26 +0400
relations: {}
atom_id: CA-R-1768
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Rule
---
## Summary

Absorb Implementation Decisions without semantic loss

## Claim scope

Eng Decisions.

## Claim

an Eng Decision **may** be archived as absorbed **only** **after** **`>=1`** active Eng Policies preserve **every** part of its still-necessary governed meaning for the affected realization scope.

## Details

Absorption does not create artificial children or override actual-child ownership. If a Scope Unit loses its last actual child, review, relocate or reclassify any locally owned Eng Policy under CA-R-2119@8; do not infer an automatic runtime conversion.
