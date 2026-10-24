---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: Subject/Engineering/Tool//DERIVE_SCOPE_CANONICAL_SIGNATURES.Canonical Scope Signature Derivation Validation
  depends_on:
  - Subject/Engineering/Tool//DERIVE_SCOPE_CANONICAL_SIGNATURES
  - Scope Expression/Canonical Scope Signature
version: 8
updated_at: 2026-10-24 01:18:03 +0400
relations:
  evaluation_for:
  - CA-M-257
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-423@8
status: Archived
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: TOOLS
type: Policy
---
# Verify Scope Expression Canonical Signature Derivation

the Evaluation **must** reject the Tool result **if** it violates CA-E-407 **or** changes one selected Source Atom.
