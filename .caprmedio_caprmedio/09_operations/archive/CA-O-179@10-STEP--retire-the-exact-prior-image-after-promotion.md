---
atom_id: CA-O-179@10
content_role: Operations
type: Step
current_scope_unit: caprmedio
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Step//Release Version/Step: retire exact prior image'
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Step'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action'
  - Subject/Graph Node/Engineering/Image
  - Subject/Graph Node/Engineering/Release Version/Runtime Package Carrier
  - Subject/Graph Node/Engineering/Permission
  - Subject/Graph Node/Domain/Continuant/History/Journal
version: 10
updated_at: 2026-10-25 17:32:27 +0400
relations:
  part_of:
  - CA-O-164
  invokes:
  - CA-O-169
tier: 3
---
# Summary

Retire the exact prior image after promotion

## Step

When explicitly selected, this Step invokes CA-O-169's existing safe retirement phase for inspected selected-Project noncandidate images after verified replacement installation and MCP smoke. Normal Local release performs this work inside CA-O-178; this carrier is not an additional occurrence in CA-O-164's complete registered graph.

## Details

Retain the exact admitted image of the current package Version. Another digest, including a same-fingerprint rebuild, is eligible only under complete matching inspected Project/root/control ownership, positive runtime classification and absence of every container reference. Preserve foreign, unowned, incomplete, in-use or unverified resources and report pending work. No sealed rollback-retention condition, canonical Journal receipt, force, global prune or uncertain retry is required or permitted as an added mechanism. Record actual removal/retention and logging failures independently; no release completion is inferred from this definition or from a Journal entry alone.
