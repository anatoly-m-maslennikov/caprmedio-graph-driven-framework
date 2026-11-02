---
cce_version: cce_1
cce_form: separation
subjects:
  governs: Subject/CAPRMEDIO/Carrier/Git Commit
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
version: 27
updated_at: 2026-10-27 20:00:09 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
author: Anatoly Maslennikov
content_role: Requirement
current_scope_unit: CORE_EXTENSIONS
status: Active
atom_id: CA-R-296
type: Rule
tier: 1
---
# Distinguish internal and external Git commits

an internal project commit uses Type Git Commit **and** derives the route `atomic / implementation / internal`.

an outside-owned commit governed as an external input uses Type External Git Commit **and** derives the route `atomic / implementation / external`.

the two Types use the repository-qualified native commit SHA as identity rather than a CAPRMEDIO artifact sequence. precise repository, author, signer, **and** source facts remain provenance. they do **not** replace the type-derived Governance locus.

## Rationale

distinct names preserve the one-type-to-one-route invariant while retaining the native identity **and** provenance required **to** trace internal **and** outside-owned implementation records.
