---
subjects:
  governs: Subject/Graph Node/Engineering/Aspect/Architecture/Communication
  depends_on: []
version: 19
updated_at: 2026-10-26 00:46:35 +0400
llm_session_ids:
- codex:01a01cb6-4ee4-7553-b68d-0823dda35094
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-R-1111@19
status: Archived
content_role: Requirement
author: Anatoly Maslennikov
current_scope_unit: MCP
type: Rule
tier: 1
---
# Delegate MCP calls to canonical Tools

**every** MCP invocation **must** delegate **to** the selected canonical Tool executable **and** **must not** reimplement Tool decisions, project meaning, target resolution, validation, mutation, recovery behavior, **or** lifecycle semantics inside the MCP carrier. MCP owns **only** transport admission, canonical Tool selection, delegation, **and** result transport.

**every** Finder **and** **every** Doer dry run **must** remain independently executable **without** MCP. A direct executable invocation of a CAPRMEDIO Markdown Atom Doer with `--apply` **must** reject the request **unless** it carries the authorized project-local MCP delegation **and** its sealed Initiative action envelope. Introducing MCP **must not** create a Tool dependency on MCP **or** another APPS unit.
