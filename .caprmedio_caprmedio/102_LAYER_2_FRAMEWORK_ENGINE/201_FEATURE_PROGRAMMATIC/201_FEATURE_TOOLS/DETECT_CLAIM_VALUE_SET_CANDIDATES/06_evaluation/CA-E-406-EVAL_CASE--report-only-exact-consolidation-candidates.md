---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Verification/Dynamic Testing
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Implementation/Code/Tool//DETECT_CLAIM_VALUE_SET_CANDIDATES
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Content
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Local Scope Unit
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Subjects
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Content.Scope
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Term//Property
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Projection/Type: Entities Graph'
  - 'Subject/CAPRMEDIO/Graph/Relation/Type: IS_ALLOWED_VALUE_OF'
version: 24
updated_at: 2026-10-27 19:59:34 +0400
relations:
  evaluation_for:
  - CA-M-238
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-406
status: Active
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: TOOLS
type: Eval Case
tier: 2
---
# Report Only Exact Consolidation Candidates

## Test case

provide one active Source frontier containing: two mechanically parseable
single-value Claims with the same Current Scope Owner, Governed Subject Set,
Claim Scope, Property, **and** qualifiers but different unique values; one semantically similar prose Claim;
one Claim with a different qualifier; **and** one unparseable Claim.
place one Claim that differs from a qualifying Claim **only** by its location **in** one child Scope Unit frontier.

pass **only** **when** the Tool reports **`=1`** consolidation candidate containing
the two qualifying Atom IDs **and** one proposed `Property: (A, B)` Claim, reports no
candidate from the other Claims, **and** leaves **every** Source carrier unchanged.
the child Scope Unit Claim **must not** enter the candidate.
fail **when** candidate membership depends on semantic inference, **any** required
identity is missing, an ineligible Claim is included, an eligible Claim is
omitted, **or** **any** Source carrier is mutated.
