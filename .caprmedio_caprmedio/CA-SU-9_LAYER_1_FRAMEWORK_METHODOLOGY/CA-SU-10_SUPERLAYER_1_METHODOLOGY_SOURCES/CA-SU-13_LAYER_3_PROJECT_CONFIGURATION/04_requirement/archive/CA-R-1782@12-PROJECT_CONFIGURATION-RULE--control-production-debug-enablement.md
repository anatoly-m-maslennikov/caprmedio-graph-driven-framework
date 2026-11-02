---
atom_id: CA-R-1782@12
content_role: Requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Entity/Aspect/Engineering/Observability/Logging
  depends_on:
  - Entity/Aspect/Engineering/Observability/Logging
version: 12
updated_at: 2026-10-29 07:45:30 +0400
relations: {}
tier: 3
type: Rule
---
## Summary

Control production DEBUG enablement

## Claim scope

logging Implementation for production DEBUG logging under Logging Policies.

## Claim

logging Implementation **must** keep production DEBUG logging disabled by default. temporary enablement **must** be scoped by component, subject, run, entity, **or** another bounded selector, have an automatic expiry, **and** preserve the same redaction rules as **every** other level.

## Details

the selector **and** expiry bound temporary production DEBUG use while preserving its required redaction treatment.
