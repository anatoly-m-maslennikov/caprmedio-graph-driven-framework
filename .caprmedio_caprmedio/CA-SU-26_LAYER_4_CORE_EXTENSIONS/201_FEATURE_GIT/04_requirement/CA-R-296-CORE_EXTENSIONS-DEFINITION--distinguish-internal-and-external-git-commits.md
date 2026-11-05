---
atom_id: CA-R-296
ref_id: CA-R-296
container:
  scope_unit: CA-SU-26
role: Requirement
form: Rule
topics:
  main_subject: Subject/CAPRMEDIO/Carrier/Git Commit
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
tier: 1
status: Active
version: 27
updated_at: 2026-10-27 20:00:09 +0400
cce_version: cce_1
cce_form: separation
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: CORE_EXTENSIONS
---
# Distinguish internal and external Git commits

an internal project commit uses Type Git Commit **and** derives the route `atomic / implementation / internal`.

an outside-owned commit governed as an external input uses Type External Git Commit **and** derives the route `atomic / implementation / external`.

the two Types use the repository-qualified native commit SHA as identity rather than a CAPRMEDIO artifact sequence. precise repository, author, signer, **and** source facts remain provenance. they do **not** replace the type-derived Governance locus.

## Rationale

distinct names preserve the one-type-to-one-route invariant while retaining the native identity **and** provenance required **to** trace internal **and** outside-owned implementation records.
