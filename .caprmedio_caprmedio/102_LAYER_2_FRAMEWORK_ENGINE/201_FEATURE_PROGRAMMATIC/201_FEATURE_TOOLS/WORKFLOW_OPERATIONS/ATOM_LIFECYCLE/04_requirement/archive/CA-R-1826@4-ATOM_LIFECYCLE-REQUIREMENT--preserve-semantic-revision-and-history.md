---
atom_id: CA-R-1826@4
content_role: Requirement
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Workflow Operations/Atom Lifecycle/Revision and History
  depends_on:
  - Subject/Domain/Node/Continuant/Atom
  - Atom/Revision
  - Atom/Summary
  - Subject/Domain/Node/Continuant/History/Journal.Record
version: 4
updated_at: 2026-10-24 00:38:25 +0400
relations:
  relates_to:
  - CA-O-067
  - CA-O-051
  - CA-R-866
  - CA-R-1041
  - CA-R-1415
  - CA-R-1371
  - CA-R-1788
tier: 3
---
# Summary

Preserve semantic revision and history through lifecycle dispatch

## Scope

Result semantics at the dispatch boundary; native lifecycle Tools retain their own mutation mechanics.

## Claim

For every admitted result, the dispatcher **must** carry the native Tool's actual Version, Updated At, prior semantic Revision, replacement lineage, and effect evidence without fabricating a timestamp or history entry. A carrier-only/equivalent refinement uses the native Update rule; a semantic revision advances exactly once under its admitted class; Replace preserves predecessor/successor lineage; Change Status preserves prior state and records the actual current status model/revision used.

An actual no-op reports no accepted edit, timestamp refresh, Version advance, archive, or invented history. A rejected preflight reports no performed effect. A started operation with incomplete, failed, or partially verified effects reports each known effect and unknown remainder truthfully; it is not reported as a complete lifecycle success.

## Details

This contract does not define Journal storage or retry behavior; it provides the lifecycle result facts that the shared Run support records.
