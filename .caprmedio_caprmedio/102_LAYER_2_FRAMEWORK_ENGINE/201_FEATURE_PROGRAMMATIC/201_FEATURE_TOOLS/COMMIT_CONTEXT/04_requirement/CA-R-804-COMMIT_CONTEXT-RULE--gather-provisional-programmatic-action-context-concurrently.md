---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Data Handling/Source Retrieval
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal.Record
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - Subject/CAPRMEDIO/Carrier
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Projection/Type: Applicable Methodology'
cce_version: cce_1
cce_form: obligation
version: 34
updated_at: 2026-10-27 20:00:11 +0400
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
atom_id: CA-R-804
status: Active
content_role: Requirement
author: Anatoly Maslennikov
current_scope_unit: TOOLS
type: Rule
tier: 1
---
# Gather provisional programmatic action context concurrently

COMMIT_CONTEXT **must** be independently invocable **and** strictly read-only. from **`=1`** durable trigger, it **must** gather provisional action context containing the sealed Initiative **and** action identity, observed repository frontier, affected subject identity, expected **and** observed Revisions **or** digests, candidate change, Git state, Journal state, **and** available provenance bindings.

- multiple context gatherers **may** work concurrently because their output is provisional **and** mutation-free. identical input **and** an unchanged observed frontier **must** produce the same context identity.
- context capture **must not** require the observed Project state **to** conform **to** Applicable Methodology. retain observable Carrier identity **and** evidence **when** Atom classification, names, properties, **or** relations are unresolved **or** invalid; do **not** invent a conforming identity **or** successful classification.
- no gathered context grants authority **to** mutate.
- a consumer changing governed Project state **or** Git state **must** revalidate its mutation preconditions against the current repository frontier, expected subject Revision **or** digest, **and** durable action state immediately **before** that effect.
- Journal admission follows CA-R-1491 instead: preserve intact sealed observations about the recorded event. subsequent Project changes alone **must not** prevent historical recording; altered **or** incomplete event envelopes remain storage-integrity failures.
