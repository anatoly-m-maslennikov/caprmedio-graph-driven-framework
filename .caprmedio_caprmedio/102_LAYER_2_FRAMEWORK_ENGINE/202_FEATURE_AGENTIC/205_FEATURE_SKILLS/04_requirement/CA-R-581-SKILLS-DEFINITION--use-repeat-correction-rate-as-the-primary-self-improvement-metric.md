---
subject_scopes:
- continuous-improvement
version: 19
updated_at: 2026-10-27 20:00:10 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  child_of:
  - CA-R-1423
  - CA-R-053
  - CAPRMEDIO-REQU-702--define-framework-engine-layer-scope
author: Anatoly Maslennikov
content_role: Requirement
current_scope_unit: SKILLS
status: Active
atom_id: CA-R-581
type: Definition
tier: 1
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Verification/Coverage
---
# Use repeat correction rate as the primary self-improvement metric

CAPRMEDIO **must** provide `repeat_correction_rate` as the primary self-improvement metric, calculated as repeated operator corrections for previously addressed failure classes divided by comparable opportunities for those failures.
