---
atom_id: CA-R-1782@4
content_role: Requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Subject/Engineering/Operational Diagnostics
  depends_on:
  - Logging Policy
version: 4
updated_at: 2026-10-24 01:37:42 +0400
relations: {}
tier: 3
type: Goal
---
# Summary

Control production DEBUG enablement

## Scope

logging Implementation for production DEBUG logging under Logging Policies.

## Claim

logging Implementation **must** keep production DEBUG logging disabled by default. temporary enablement **must** be scoped by component, subject, run, entity, **or** another bounded selector, have an automatic expiry, **and** preserve the same redaction rules as **every** other level.

## Details

the selector **and** expiry bound temporary production DEBUG use while preserving its required redaction treatment.
