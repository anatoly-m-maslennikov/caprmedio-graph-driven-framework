---
atom_id: CA-R-1779@15
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Archived
subjects:
  active: Entity/Aspect/Engineering/Observability/Logging
  passive:
  - Carrier
  - Atom/(.Role := Evaluation)
  - 'Entity/Object/Continuant/Projection/Type: Catalog'
version: 15
updated_at: 2026-11-02 00:18:22 +0400
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
