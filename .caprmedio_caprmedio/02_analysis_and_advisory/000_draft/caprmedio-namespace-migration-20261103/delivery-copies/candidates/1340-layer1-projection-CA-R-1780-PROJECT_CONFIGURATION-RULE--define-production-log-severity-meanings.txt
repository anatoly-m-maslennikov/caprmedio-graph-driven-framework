---
atom_id: CA-R-1780
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
subjects:
  active: CAPRMEDIO <+ STRUCTURE <+ Aspects <+ Engineering <+ Observability <+ Logging
version: 14
updated_at: 2026-11-02 19:44:26 +0400
relations: {}
tier: 3
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/04_requirement/CA-R-1780-PROJECT_CONFIGURATION-RULE--define-production-log-severity-meanings.md
  source_atom_id: CA-R-1780
  source_atom_revision: 14
  source_sha256: ed355f3ddd2a37cedc8a292ba7ede4a6908f05a4d9ce1ec7aa41946d6791a534
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Define production log severity meanings

## Claim scope

Logging Policies for production-relevant components.

## Claim

a Logging Policy **must** use these four operational levels:

| Level | Required meaning |
|---|---|
| `ERROR` | an operation failed, correctness **or** availability **may** be affected, **or** explicit retry **or** intervention is required |
| `WARNING` | behavior was unexpected **or** degraded but recovered, fell back, **or** remains within an accepted tolerance |
| `INFO` | a material lifecycle, business, **or** operational milestone occurred, including start, stop, acceptance, state transition, completion, **or** summarized progress |
| `DEBUG` | sanitized internal state **or** decision detail is useful for bounded investigation but is unnecessary during normal production operation |

## Details

the four level meanings are one taxonomy **and** retain one lifecycle as a set.
