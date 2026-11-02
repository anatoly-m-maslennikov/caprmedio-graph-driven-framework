---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: Subject/Engineering/Tool//DERIVE_CCE_CANONICAL_SIGNATURES.Canonical Signature Derivation Validation
  depends_on:
  - Subject/Engineering/Tool//DERIVE_CCE_CANONICAL_SIGNATURES
  - Atom/Claim/Canonical Signature
version: 9
updated_at: 2026-10-24 02:14:24 +0400
relations:
  evaluation_for:
  - CA-M-256
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-422@9
status: Archived
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: TOOLS
type: Policy
tier: 3
---
# Verify Restricted CCE Canonical Signature Derivation

the Evaluation **must** reject the Tool result **if** it violates CA-E-405 **or** changes one selected Source Atom.
