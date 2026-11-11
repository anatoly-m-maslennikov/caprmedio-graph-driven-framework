---
atom_id: CA-R-1782
ref_id: CA-R-1782
container:
  scope_unit: CA-SU-13
role: Requirement
form: Rule
topics:
  main_subject: "CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Operation <+ Observability <+ Logging"
  dependencies:
  - "CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Operation <+ Observability <+ Logging"
tier: 3
status: Active
version: 15
updated_at: 2026-11-02 18:35:20 +0400
carrier_destination:
  file:
    name: CA-R-1782-PROJECT_CONFIGURATION-RULE--control-production-debug-enablement.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/04_requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
---
## Summary

Control production DEBUG enablement

## Claim

### Prose Claim


logging Implementation for production DEBUG logging under Logging Policies.


logging Implementation **must** keep production DEBUG logging disabled by default. temporary enablement **must** be scoped by component, subject, run, entity, **or** another bounded selector, have an automatic expiry, **and** preserve the same redaction rules as **every** other level.

## Details

the selector **and** expiry bound temporary production DEBUG use while preserving its required redaction treatment.
