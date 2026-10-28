---
atom_id: CA-R-1832
content_role: Requirement
type: Rule
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
status: Active
author: Anatoly Maslennikov
version: 8
updated_at: 2026-10-27 20:00:04 +0400
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Structure
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
relations: {}
tier: 3
---
# Summary

Report structural change result and breakage

## Scope

The result boundary after CA-O-143 cutover and CA-O-144 assessment.

## Claim

The Tool **must** return exact outcome, current declaration revision, actual effects, and complete preservation/breakage disposition without representing a source definition or preview as an executed change.

## Details

- Output includes operation, requested and resulting Scope Unit identity/parent/paths, pre/post TOML revisions, authorization revision, affected and repaired references, preserved Carriers, explicit breakages, validation evidence, recovery disposition, and available Workflow/Action Run and Journal references.
- `completed` is returned only after required assessment checks accept actual effects. `rolled_back` identifies the restored set and any remaining breakage. `partial` and all blocked outcomes remain terminally truthful and machine-readable.
- The result must distinguish absent evidence, failed evidence recording, and a failed structural operation; it must not manufacture a successful no-op, rollback, or journal receipt.
