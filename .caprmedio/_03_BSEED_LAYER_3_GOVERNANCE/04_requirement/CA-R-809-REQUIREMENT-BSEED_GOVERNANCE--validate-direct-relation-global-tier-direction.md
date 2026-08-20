---
subject_scopes:
  - relation-model
version: 1
updated_at: 2026-08-20 19:58:00
relations:
  child_of:
    - CA-R-808-REQUIREMENT-BSEED_GOVERNANCE--limit-active-direct-relations-to-upstream-or-same-tier
---
# Validate direct relation global-tier direction

GOV validators must derive the source and target global tiers for every direct relation authored by an active tier-classified Atom and reject the edge when `target_global_tier > source_global_tier`. Validation must fail closed when either required tier cannot be derived and must apply any stricter tier or endpoint boundary registered for the specific direct relation type.
