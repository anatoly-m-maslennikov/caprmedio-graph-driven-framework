---
cce_version: cce_1
cce_form: method
subjects:
  governs: Claim Value Set Consolidation Candidate Detection
  depends_on:
  - Subject/Graph Node/Engineering/Continuant/Tool//DETECT_CLAIM_VALUE_SET_CANDIDATES
  - Subject/Graph Node/Domain/Continuant/Atom.Local Scope Unit
  - Subject/Graph Node/Domain/Continuant/Atom.Subjects
  - Subject/Graph Node/Domain/Continuant/Atom.Content.Scope
  - Subject/Graph Node/Domain/Continuant/Term//Property
  - 'Subject/Graph Node/Domain/Continuant/Projection/Type: Entities Graph'
  - 'Subject/Graph Relation/Type: IS_ALLOWED_VALUE_OF'
version: 18
updated_at: 2026-10-25 17:32:27 +0400
relations:
  method_for:
  - CA-R-1358
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-M-238@18
status: Archived
content_role: Method
author: Anatoly Maslennikov
current_scope_unit: TOOLS
type: Eng Decision
tier: 1
---
# Detect Exact Claim Value-Set Consolidation Candidates

**to** detect Claim Value Set consolidation candidates, the `DETECT_CLAIM_VALUE_SET_CANDIDATES` Tool **must** inspect one Scope Unit's local active Atom frontier **without** its child Scope Unit frontiers, derive **every** Atom's Governed Subject Set from its GOVERNS Subjects, derive its Claim Scope from the Property **in** one exact `<Property>: <Value>[ **if** <Qualifier>].` Claim, accept a value **only** **if** one supplied Entity Graph Projection proves its IS_ALLOWED_VALUE_OF relation for that Property, group **only** identical Current Scope Owner, Governed Subject Set, Claim Scope, Property, **and** qualifier coordinates, report **every** contributing Atom ID **and** one proposed `Property: (A, B, C)` Claim, **and** report no candidate for unparseable, unproven, **or** semantically similar prose.
