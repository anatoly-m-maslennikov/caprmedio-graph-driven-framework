---
atom_id: CA-P-2632
content_role: Plan
type: Plan
label: Task
work_sequence_number: 19
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Active
version: 1
updated_at: "2026-10-23T13:10:12+0400"
subjects:
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  is_decomposition_of: [CA-P-2631]
  depends_on: [CA-P-2629]
  relates_to: [CA-R-1840, CA-R-1841, CA-R-1842, CA-E-560, CA-E-561, CA-D-541, CA-D-542, CA-D-543, CA-C-583, CA-P-2630]
---
# Summary

Prepare identity-safe R1841 successor and Engine rebinding

## Objective

Prepare the identity-safe replacement of the misleading current R1841 carrier
and rebind its active Engine consumers without changing the historical
meaning or creating a second authority.

## Details

This is one bounded implementation-planning Task for the
compiler_rmed_reconciliation lane. The execution owner must archive the exact
current CA-R-1841 revision at its next qualified predecessor, create a fresh
canonical Requirement with the corrected Summary/body, and rebind active
consumers CA-R-1840, CA-R-1842, CA-E-560, CA-E-561, CA-D-541, CA-D-542 and
CA-D-543 with the required predecessor archives and version increments. Do not
create history relations merely to perform the rebind.

The previously reserved candidate ID CA-R-2118 is not currently free: a
current unrelated CA-R-2118 carrier exists in applicable methodology. Re-run
the full retained-carrier collision check immediately before writing; never
overwrite or merge that carrier. If the collision remains, allocate the next
fresh canonical ID and record the exact old-to-new mapping. Do not create a
CA-R-2118 Markdown or Journal carrier merely to preserve the stale
reservation.

Do not append the replacement mapping to the business Journal until the writer
returns the actual predecessor/successor paths, versions and hashes. No code,
runtime, binding, release or deployment change is part of this planning Task.

## Definition of Done

Return the exact identity-safe R1841 replacement and consumer-rebind mapping,
including every predecessor archive, successor version and SHA-256. Prove the
fresh ID is collision-free across current carriers and retained histories,
record the CA-R-2118 collision or its resolved allocation, and provide the
writer's bounded source evidence before any Journal mapping event is appended.
