---
atom_id: CA-P-2653
content_role: Plan
type: Plan
label: Task
work_sequence_number: 14
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
status: Done
subjects:
  governs: Subject
version: 2
updated_at: 2026-10-26 06:39:23 +0400
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

### Completion evidence

CA-PROJ-009 rebuilt from 2230 Current RMEDO sources. SHA-256 37696ac4d2ad2783d0ce99547747cd5462269ed9f1f28a86fa6b429a14b3df64; actual formal-rule Summaries restored; no YAML gaps.

Source verification: `.caprmedio_tmp/subject-fpf-refinement/verify.final.md`.
Final source/output pins: `.caprmedio_tmp/subject-fpf-refinement/graph-closure/graph.subject-views.manifest.json`.
Actual effect verified; no production tool/runtime implementation or release is claimed.

## Definition of Done

- The actual full Markdown projection is rebuilt from the corrected Current
  source frontier, with stable identity and verified provenance.
- The three-section form and accepted Subject meanings are preserved.
- No source correction is falsely inferred from rendering alone.
