---
subjects:
  governs: Subject/Graph Node/Engineering/Aspect/Delivery
  depends_on:
  - Subject/Graph Node/Domain/Continuant/History/Journal.Record
  - Artifact/Revision
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
version: 20
updated_at: 2026-10-26 00:46:35 +0400
atom_id: CA-R-1147@20
status: Archived
content_role: Requirement
author: Anatoly Maslennikov
current_scope_unit: TOOLS
type: Rule
tier: 1
---
# Record a release outcome

the framework **must** provide one deterministic Tool that records a verified release success **or** a failed attempt as immutable Journal evidence, distinguishes a successful release from a failed non-release attempt, **and** binds either outcome **to** the attempted version, Revision, checks, **and** Work Journal event.
