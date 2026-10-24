---
atom_id: CA-D-618
content_role: Delivery
current_scope_unit: PROJECT_TOOLS
claim_target_scope_unit: PROJECT_TOOLS
author: Anatoly Maslennikov
status: Active
subjects:
  governs: Subject/Domain/Node/Continuant/History/Journal.Record
  depends_on:
  - Subject/Engineering/Carrier/Journal Serialization
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Step'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - Subject/Domain/Node/Occurrent/Execution
version: 6
updated_at: 2026-10-24 04:05:50 +0400
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
