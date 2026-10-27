---
cce_version: cce_1
cce_form: obligation
subjects:
  governs: Subject/Graph Node/Engineering/Data Handling/Serialization
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Projection
  - Subject/Graph Node/Carrier
version: 18
updated_at: 2026-10-27 06:04:45 +0400
relations: {}
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-R-1450
status: Active
content_role: Requirement
author: Anatoly Maslennikov
current_scope_unit: TOOLS
type: Rule
tier: 1
---
# Derive Restricted CCE Canonical Signatures

For one caller-selected active Atom Carrier frontier, the `DERIVE_CCE_CANONICAL_SIGNATURES` Tool **must** derive **only** the non-authoritative Canonical Signatures defined by `CA-R-1360` **and** **must not** change a Source Atom.
