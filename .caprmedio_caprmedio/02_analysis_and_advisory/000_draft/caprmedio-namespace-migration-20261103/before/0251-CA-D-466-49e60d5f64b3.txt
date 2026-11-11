---
subjects:
  active: Carrier
  passive:
  - Entity
  - Atom/(.Role := Delivery)
version: 22
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-D-466
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Delivery
form: Decision
---
## Summary

Place Carriers by Applicable Status Delivery

## Claim scope

Carrier placement where an applicable qualified Artifact Status model exists or does not exist.

## Claim

**when** an applicable qualified Artifact Status model exists **and** an Artifact has **`=1`** valid current Status, its Carrier placement **must** follow the most specific applicable Delivery rule for that Artifact Type; **only when** no more-specific mapping exists, Active uses the canonical current directory **and** another Status uses its lowercase Status subdirectory. **when** no applicable qualified Status model exists, Carrier placement **must not** derive a Status directory from absent Status.
