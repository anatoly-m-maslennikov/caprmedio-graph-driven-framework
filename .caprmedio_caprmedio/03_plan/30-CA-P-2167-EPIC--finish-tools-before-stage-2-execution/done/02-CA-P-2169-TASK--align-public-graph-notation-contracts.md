---
atom_id: CA-P-2169
content_role: Plan
type: Plan
label: Task
work_sequence_number: 2
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Done
subjects:
  governs: Tool
  depends_on: [Subject, Entity, Projection, Plan, Operator]
version: 3
updated_at: "2026-10-23 23:03:23 +0400"
relations:
  is_decomposition_of: [CA-P-2167]
  blocks: [CA-P-2171, CA-P-2176]
---
# Summary

Align public graph notation contracts

## Objective

The existing public graph entry point has explicit approved notation-profile selection and current pinned evidence.

## Details

Estimated own work: 15 minutes. Assignee: AI Agent. Review the public Entities Graph R/M/E/D/O in its declared Engine graph scope. Bind an exact carrier packet disjoint from the preview/application lanes before edits; the integration owner owns any shared carrier.

Review and update required same-Summary revisions for an explicit approved profile at the public entry point, reusing the internal reviewed parser. Preserve case-sensitive `Atom` versus `atom(...)`, `/`, `.` and `:` semantics, graph ownership, source pins and output provenance. `@` is filename punctuation only. An approved parsing profile does not admit new native Relations or unsupported candidate meanings. Preserve the legacy/default path and test rejection of absent/unsupported profile selection where explicit selection is required.

Deliver actual before/after contract pins, predecessor evidence and the profile/legacy/negative cases to CA-P-2171. Split a larger or identity-replacing packet before effect. No graph generation, implementation, Core content, native admission or source migration occurs here.

Inherit CA-P-1959/2167's preservation and shared-route boundaries.

### Completion receipt

The actual public graph profile packet passed [independent source verification](../../../_projection/core-entity-review/stage2/tools-first/contract-acceptance.md). It admits an explicit `approved` profile while retaining legacy/default semantics. Reviewed grammar pins/evidence participate in output and are checked before parsing, after construction and before publication/no-op. Current predecessor archives, Version increments, identities, Subjects and unrelated metadata were verified. Profile/case/stale-source checks do not grant native fact admission or selector resolution. This completes contract alignment and releases bounded CA-P-2176 implementation; no implementation or production graph completion is asserted.

### Definition of Done

The Plan is **not** Done if a required contract is missing, public profile selection is implicit, legacy/profile semantics or evidence drift is ignored, native admission is inferred from parsing, actual contract pins/cases are missing, or own work exceeds 15 minutes without decomposition.
