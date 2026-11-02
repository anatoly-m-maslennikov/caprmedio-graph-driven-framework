---
atom_id: CA-R-1832@5
content_role: Requirement
type: Rule
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
status: Archived
author: Anatoly Maslennikov
version: 5
updated_at: 2026-10-24 13:39:34 +0400
subjects:
  governs: Subject/Domain/Node/Continuant/Project.Structure
  depends_on:
  - Subject/Domain/Node/Continuant/Scope Unit
  - Subject/Domain/Node/Occurrent/Execution
  - Subject/Domain/Node/Continuant/History/Journal
relations:
  relates_to:
  - CA-R-1829
  - CA-R-1831
  - CA-O-144
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
