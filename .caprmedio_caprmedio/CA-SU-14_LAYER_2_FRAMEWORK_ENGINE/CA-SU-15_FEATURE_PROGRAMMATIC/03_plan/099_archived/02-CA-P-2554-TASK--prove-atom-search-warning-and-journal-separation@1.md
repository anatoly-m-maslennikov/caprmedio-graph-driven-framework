---
atom_id: CA-P-2554
content_role: Plan
type: Plan
label: Task
work_sequence_number: 2
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Backlog
subjects:
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  is_decomposition_of: [CA-P-2552]
  depends_on: [CA-P-2553]
version: 1
updated_at: "2026-10-21T16:54:03Z"
---
# Summary

Prove AtomSearch warning and Journal separation

## Objective

Run the bounded focused acceptance for the schema-invalid scan disposition after
CA-P-2553, with exact durable test evidence and no release or deployment claim.

## Details

At most 15 minutes own work. Use a fixture or observed source set containing valid
selected Atoms around one isolated `schema_invalid` Atom. Verify valid matches are
retained, the invalid Atom is skipped, the warning contains repository-relative
path and reason, the result is `complete: false`, and no source or Journal bytes
change. Verify fatal I/O, security, duplicate-identity, stale, ambiguous, and
incomplete-frontier cases still refuse rather than return partial complete data.
Record exact module/case names, Run ID or durable log, counts, skips/failures,
warning fields, and before/after Journal evidence. Preserve the complete-suite
and public-release distinction.

### Definition of Done

Focused proof is independently attributable and shows technical warnings remain
outside business Journal records. Until such evidence is observed, this Task stays
Backlog and CA-C-572 stays Active.
