---
atom_id: CA-R-1780
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
subjects:
  active: CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Observability <+ Logging
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
  source_sha256: 49b28034d3e8e0df1f458bb8f6af6d65d27d62036336d5a22f08bae7d81ab30a
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Define production log severity meanings

## Claim

### Prose Claim


Logging Policies for production-relevant components.


a Logging Policy **must** use these four operational levels:

| Level | Required meaning |
|---|---|
| `ERROR` | an operation failed, correctness **or** availability **may** be affected, **or** explicit retry **or** intervention is required |
| `WARNING` | behavior was unexpected **or** degraded but recovered, fell back, **or** remains within an accepted tolerance |
| `INFO` | a material lifecycle, business, **or** operational milestone occurred, including start, stop, acceptance, state transition, completion, **or** summarized progress |
| `DEBUG` | sanitized internal state **or** decision detail is useful for bounded investigation but is unnecessary during normal production operation |

## Details

the four level meanings are one taxonomy **and** retain one lifecycle as a set.
