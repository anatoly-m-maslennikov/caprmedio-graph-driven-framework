---
cce_version: cce_1
cce_form: obligation
subjects:
  governs: Subject/Graph Node/Engineering/Aspect/Data Handling/Serialization
  depends_on:
  - Atom/Claim/Canonical Signature
  - Subject/Graph Node/Engineering/Continuant/Carrier
version: 16
updated_at: 2026-10-26 00:46:35 +0400
relations: {}
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-R-1450@16
status: Archived
content_role: Requirement
author: Anatoly Maslennikov
current_scope_unit: TOOLS
type: Rule
tier: 1
---
# Derive Restricted CCE Canonical Signatures

For one caller-selected active Atom Carrier frontier, the `DERIVE_CCE_CANONICAL_SIGNATURES` Tool **must** derive **only** the non-authoritative Canonical Signatures defined by `CA-R-1360` **and** **must not** change a Source Atom.
