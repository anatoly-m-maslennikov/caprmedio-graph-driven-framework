---
atom_id: CA-P-2653@1
content_role: Plan
type: Plan
label: Task
work_sequence_number: 14
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Subject
version: 1
updated_at: 2026-10-26 05:25:18 +0400
relations:
  IS_CONTAINED_BY:
  - CA-P-2639
tier: 4
---
# Summary

Regenerate the full Subject Graph

## Objective

Regenerate the full Current RMEDO Subject Graph after the accepted source
corrections and partition-view verification.

## Details

- Follow P2652. Use actual Current authoritative source Atoms, excluding
  existing Drafts, Archives, delivery mirrors and derived copies.
- Use the existing local generator and supported project interpreter; no tool
  or renderer implementation changes are included.
- Preserve CA-PROJ-009 identity, selection and source-of-truth identity. Record
  the actual source IDs/Versions, time and reproducible provenance.
- Preserve the accepted three sections: primary Subjects without instances;
  per-primary properties with inherited-origin marks; instances including
  Relation Types and concrete Graph Rules.
- Verify partition union, source pins and the full result against the accepted
  corrections; do not reuse the old 2,238-source count as a target.

## Definition of Done

- The actual full Markdown projection is rebuilt from the corrected Current
  source frontier, with stable identity and verified provenance.
- The three-section form and accepted Subject meanings are preserved.
- No source correction is falsely inferred from rendering alone.
