---
atom_id: CA-R-1781@12
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Archived
subjects:
  active: Entity/Aspect/Engineering/Observability/Logging
  passive:
  - Entity/Aspect/Engineering/Observability/Logging
version: 12
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Requirement
form: Rule
---
## Summary

Bound high-frequency INFO logging

## Claim scope

logging Implementation for high-frequency success, polling, **and** progress events under production Logging Policies.

## Claim

logging Implementation **must** bound high-frequency success, polling, **and** progress events through aggregation, sampling, **or** emission as `DEBUG` **where** appropriate rather than creating unbounded `INFO` noise.

## Details

the alternatives bound repeated normal-event volume; the severity taxonomy separately classifies material operational milestones.
