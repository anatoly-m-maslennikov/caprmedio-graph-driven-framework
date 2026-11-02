---
atom_id: CA-R-1831@2
content_role: Requirement
type: Rule
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Archived
author: Anatoly Maslennikov
version: 2
updated_at: 2026-10-23 01:47:30 +0400
subjects:
  governs: Subject/Domain/Node/Continuant/Project.Structure
  depends_on:
  - Subject/Domain/Node/Continuant/Scope Unit
  - Subject/Engineering/Carrier
  - Subject/Domain/Node/Continuant/Atom
  - Subject/Domain/Node/Continuant/History/Journal
relations:
  relates_to:
  - CA-R-1829
  - CA-R-1830
  - CA-O-013
  - CA-O-014
  - CA-O-142
  - CA-O-143
---
# Summary

Apply authorized Scope Unit cutover losslessly

## Scope

The mutation boundary for an already assessed and exact-authorized structural proposal.

## Claim

The Tool **must** recheck currentness and apply only the authorized declaration, reference, and explicitly included Carrier changes through one recoverable cutover.

## Details

- Before mutation, the current TOML revision, selected references, authorization, and effective permission must still match the proposal. Any mismatch returns `stale`, `conflict`, or `permission_denied` before mutation.
- Rename and Move repair or explicitly report every affected reference and parent-owned Goal/Atom attachment; Remove never implies recursive Carrier/content deletion and must preserve or explicitly report every affected Atom, definition, and Carrier.
- A failed cutover returns `partial` with applied and unapplied sets plus the authorized recovery boundary. Only that boundary may roll back; the Tool must not overwrite concurrent edits, erase unapproved content, or claim completion.
- Journal evidence follows the existing shared Journal model. Recording failure is returned separately from the structural outcome and does not create a competing schema.
