---
cce_version: cce_1
cce_form: separation
subjects:
  governs: 'Atom/Content Role: Implementation/Type'
  depends_on:
  - Atom/Identity
  - Governance Origin
  - Journal
version: 16
updated_at: 2026-10-24 02:04:43 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
author: Anatoly Maslennikov
content_role: Requirement
current_scope_unit: CORE_EXTENSIONS
status: Archived
atom_id: CA-R-296@16
type: Definition
---
# Distinguish internal and external Git commits

an internal project commit uses Type Git Commit **and** derives the route `atomic / implementation / internal`.

an outside-owned commit governed as an external input uses Type External Git Commit **and** derives the route `atomic / implementation / external`.

the two Types use the repository-qualified native commit SHA as identity rather than a CAPRMEDIO artifact sequence. precise repository, author, signer, **and** source facts remain provenance. they do **not** replace the type-derived Governance locus.

## Rationale

distinct names preserve the one-type-to-one-route invariant while retaining the native identity **and** provenance required **to** trace internal **and** outside-owned implementation records.
