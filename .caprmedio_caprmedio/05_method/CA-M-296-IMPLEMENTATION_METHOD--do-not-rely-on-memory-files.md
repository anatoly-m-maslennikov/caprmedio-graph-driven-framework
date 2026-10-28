---
cce_version: cce_1
cce_form: method
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Project
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Term//Artifact
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Projection
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Projection/Type: Applicable Methodology'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
version: 15
updated_at: 2026-10-27 19:59:41 +0400
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  child_of:
  - CA-R-1490
atom_id: CA-M-296
status: Active
content_role: Method
author: Anatoly Maslennikov
current_scope_unit: caprmedio
type: Implementation Method
tier: 1
---
# Do not rely on memory files

**to** preserve valuable information while developing caprmedio, keep that information recoverable from its proper Project Artifacts **without** depending on Agent memory **or** session continuity.

- do **not** use `MEMORY.md`, similar memory files, conversation summaries, **or** handoff notes as governing authority **or** as the sole preserved copy of valuable information.
- preserve accepted decisions, findings, rationale, **and** necessary evidence **in** their appropriate Artifacts under Applicable Methodology. keep governing Atoms, analysis, **and** factual Journal records distinct; preserving a finding does **not** make it accepted authority.
- secondary summaries **may** help locate sources, but **must not** substitute for reading the relevant current sources **before** relying on their contents **or** claiming that work is complete.
- **before** reducing context **or** handing work over, ensure that valuable information remains recoverable from those Artifacts. a later session **must not** need an earlier Agent's private memory **to** recover it.
- missing, unavailable, **or** conflicting source information remains an explicit gap; do **not** fill it with remembered assertions. request Operator clarification **when** the unresolved gap prevents a sufficiently supported decision.
