---
atom_id: CA-R-1781@7
content_role: Requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Subject/Graph Node/Engineering/Operational Diagnostics
  depends_on:
  - Subject/Graph Node/Engineering/Logging Policy
version: 7
updated_at: 2026-10-25 17:32:27 +0400
relations: {}
tier: 3
type: Rule
---
# Summary

Bound high-frequency INFO logging

## Scope

logging Implementation for high-frequency success, polling, **and** progress events under production Logging Policies.

## Claim

logging Implementation **must** bound high-frequency success, polling, **and** progress events through aggregation, sampling, **or** emission as `DEBUG` **where** appropriate rather than creating unbounded `INFO` noise.

## Details

the alternatives bound repeated normal-event volume; the severity taxonomy separately classifies material operational milestones.
