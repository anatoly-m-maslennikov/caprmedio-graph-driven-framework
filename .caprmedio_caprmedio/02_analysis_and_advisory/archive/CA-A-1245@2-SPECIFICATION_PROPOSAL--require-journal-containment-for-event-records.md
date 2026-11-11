---
atom_id: CA-A-1245@2
content_role: Analysis
type: Specification Proposal
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Formal Model
version: 2
updated_at: 2026-10-29 21:51:04 +0400
relations: {}
tier: 3
---
# Summary

Require Journal containment for Event Records

## Decision

The Operator specified History/Journal > Event Record and that Event Record exists only in Journal. Declare the Event Record kind there, not as a standalone Continuant child. Preserve its Continuant classification through /@(Event Record); that reference grants no independent existence. A Journal contains the record, not the actual Event or Run it describes.

The accepted declaration convention requires a permitted Journal container when no standalone option exists. This decision names the required container kind; it does not select an exact numerical upper bound on Journal parents or invent an Event Record identifier.

## Drafts

The new Event Record Definition Draft supplies the previously missing defining source. CA-A-1239 is the primary/property review view. No Current source or actual Journal is changed.
