---
cce_version: cce_1
cce_form: obligation
subjects:
  governs: Applicable Methodology Retrieval Tool
  depends_on:
  - Applicable Methodology/Compilation Output
version: 12
updated_at: 2026-10-24 12:35:51 +0400
relations: {}
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-R-1241@12
status: Archived
content_role: Requirement
author: Anatoly Maslennikov
current_scope_unit: TOOLS
type: Rule
tier: 1
---
# Require Source-Backed Subject Retrieval

the Applicable Methodology Retrieval Tool **must** return **only** generated projected current RMEDO Atom Carriers that match the exact Subject **or** Process query through `subjects.governs` **or** enter its transitive prerequisite closure through `subjects.depends_on`, preserve compilation order, **and** resolve **every** returned Carrier **to** its exact authoritative Source Carrier.
