---
cce_version: cce_1
cce_form: obligation
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Data Handling/Data Transformation
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Projection
  - Subject/CAPRMEDIO/Carrier
version: 20
updated_at: 2026-10-27 19:59:55 +0400
relations: {}
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-R-1451
status: Active
content_role: Requirement
author: Anatoly Maslennikov
current_scope_unit: TOOLS
type: Rule
tier: 1
---
# Derive Canonical Scope Signatures

for one caller-selected active Atom Carrier frontier, the `DERIVE_SCOPE_CANONICAL_SIGNATURES` Tool **must** derive **only** the non-authoritative Canonical Scope Signatures defined by `CA-R-1361` **and** **must not** change a Source Atom.
