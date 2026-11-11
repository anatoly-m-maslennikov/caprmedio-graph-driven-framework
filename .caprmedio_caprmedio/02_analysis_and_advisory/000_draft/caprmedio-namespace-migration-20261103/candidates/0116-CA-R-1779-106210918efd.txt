---
atom_id: CA-R-1779
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
subjects:
  active: CAPRMEDIO <+ STRUCTURE <+ Aspects <+ Engineering <+ Observability <+ Logging
  passive:
  - CAPRMEDIO <+ MODEL <+ Carrier
  - CAPRMEDIO <+ MODEL <+ Atom/(.Role := Evaluation)
  - 'CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Projection/Type: Catalog'
version: 17
updated_at: 2026-11-02 18:35:20 +0400
relations: {}
tier: 3
role: Requirement
form: Rule
---
## Summary

Require production Logging Policies

## Claim scope

production-relevant components **and** their Logging Policies.

## Claim

**every** production-relevant component **must** define a Logging Policy. that policy:

- governs required log coverage, structure, severity, safety, **and** retention **before** failures occur;
- supports its Evaluation Controls;
- is referenced by the Catalog Projection over its applicable Evaluation Control Atoms; **and**
- identifies the events **and** context required **to** understand normal operation, detect failure, correlate distributed work, **and** investigate real production issues.

## Details

the policy describes the evaluation boundary, while logger Implementation **and** emitted record Carriers realize it.
