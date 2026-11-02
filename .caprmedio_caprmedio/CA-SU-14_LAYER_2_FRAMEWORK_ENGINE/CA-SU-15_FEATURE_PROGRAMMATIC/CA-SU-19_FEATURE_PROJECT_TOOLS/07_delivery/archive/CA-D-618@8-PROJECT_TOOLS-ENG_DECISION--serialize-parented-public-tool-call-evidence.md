---
atom_id: CA-D-618@8
content_role: Delivery
current_scope_unit: PROJECT_TOOLS
claim_target_scope_unit: PROJECT_TOOLS
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Subject/Graph Node/Domain/Continuant/History/Journal.Record
  depends_on:
  - Subject/Graph Node/Engineering/Continuant/Carrier/Journal Serialization
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Step'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action'
  - Subject/Graph Node/Domain/Occurrent/Execution
version: 8
updated_at: 2026-10-25 17:32:27 +0400
relations:
  delivery_for:
  - CA-R-1928
type: Eng Decision
tier: 4
---
# Summary

Serialize parented public Tool-call evidence

## Scope

Tool-call evidence of one public-release Action.

## Claim

public-release Tool-call evidence **must** serialize input, result, effect, and report references under the actual parent Step and Action Run records of the existing schema-v5 Journal.

## Details

This Delivery adds neither a Tool Run kind nor a new Journal event schema. Started, terminal, and recording-pending states remain the shared schema meanings.
