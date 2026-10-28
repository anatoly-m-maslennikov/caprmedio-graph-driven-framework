---
atom_id: CA-P-2682@1
content_role: Plan
type: Plan
label: Task
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Subject
version: 1
updated_at: 2026-10-27 18:34:34 +0400
relations:
  IS_CONTAINED_BY:
  - CA-P-2673
tier: 4
---
# Summary

Rebuild Candidate #10 Subject Graph

## Objective

Rebuild and check the Subject view from the adopted Current sources.

## Details

Start after P2681. Generate from real Current authoritative source Atoms; do not substitute Candidate text, Drafts, Archived sources, a mapping overlay or a packaged copy as the graph source.

Verify the main Subject structure and a defining Current R Atom for each displayed primary entity or topic. Keep namespaces, organizational headings and entity/topic kinds distinct; do not infer native relations merely from tree indentation. Present the agreed primary view without instances or property inventories. Existing qualified suffixes may be checked for preservation as source data; do not redesign them here.

Use the existing programmatic/local generation route where it can represent the adopted model faithfully. Keep projection identity for the same Type, selection and source of truth, and refresh its actual source-version provenance. A missing renderer capability is a separate concrete Tool issue, not permission to hide unsupported source Subjects or change the methodology to match code.

Compare the rebuilt source selection and its actual Subjects with the applied thin inventory. Report any unresolved old roots or missing defining R Atoms visibly. Keep full canonical paths in sources and concise indented labels in the readable tree. Do not claim global grammar, property or instance correctness from this bounded check.

## Definition of Done

The rebuilt primary Subject view reflects the adopted Current sources, with current defining R IDs and source provenance. No unsupported old roots are hidden; any remaining gap is explicit. Closure distinguishes prepared, reviewed, applied and rebuilt outcomes.


## References

- [A1218 — Candidate #10](../../../02_analysis/CA-A-1218-SPECIFICATION_PROPOSAL--subject-model-candidate-10.md).
- [A1219 — Mixed Subject targets](../../../02_analysis/CA-A-1219-SPECIFICATION_PROPOSAL--clarify-mixed-subject-targets.md).
- [A1220 — Project as a whole entity](../../../02_analysis/CA-A-1220-SPECIFICATION_PROPOSAL--define-project-as-a-whole-entity.md).
- [P2675 — Existing thin Draft/change inventory](../done/02-CA-P-2675-TASK--draft-main-subject-definitions.md).
