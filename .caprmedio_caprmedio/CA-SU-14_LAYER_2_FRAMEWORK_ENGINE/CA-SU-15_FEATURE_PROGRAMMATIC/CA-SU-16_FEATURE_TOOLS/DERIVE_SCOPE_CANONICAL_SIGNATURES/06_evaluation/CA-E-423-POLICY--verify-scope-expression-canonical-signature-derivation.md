---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Data Handling/Data Transformation
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Implementation/Code/Tool//DERIVE_SCOPE_CANONICAL_SIGNATURES
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Data Handling/Data Validation
version: 17
updated_at: 2026-10-27 19:59:34 +0400
relations:
  evaluation_for:
  - CA-M-257
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-423
status: Active
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: TOOLS
type: Policy
tier: 3
---
# Verify Scope Expression Canonical Signature Derivation

the Evaluation **must** reject the Tool result **if** it violates CA-E-407 **or** changes one selected Source Atom.
