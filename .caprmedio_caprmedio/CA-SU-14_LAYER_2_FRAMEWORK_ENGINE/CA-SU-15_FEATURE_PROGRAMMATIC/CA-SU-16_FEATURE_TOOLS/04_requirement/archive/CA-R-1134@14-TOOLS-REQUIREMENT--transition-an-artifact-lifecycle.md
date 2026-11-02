---
subjects:
  governs: Subject/Engineering/Carrier
  depends_on: []
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
version: 14
updated_at: 2026-10-24 01:28:26 +0400
atom_id: CA-R-1134@14
status: Archived
content_role: Requirement
author: Anatoly Maslennikov
current_scope_unit: TOOLS
type: Rule
---
# Transition an artifact lifecycle

the framework **must** provide one deterministic generic Artifact Tool that applies one registered artifact lifecycle transition, lazily creates its permitted destination directory, moves the carrier, updates required metadata **and** references, **and** fails closed on an undefined **or** ambiguous state model.

this Tool owns generic lifecycle-transition mechanics **only**. `ATOM_ARCHIVE`, `ATOM_PROMOTE`, `ATOM_UPGRADE`, **and** `CLOSE_ATOM` own their distinct CAPRMEDIO Markdown Atom transition meanings, validation, bulk rules **where** admitted, **and** MCP-gated effects; the generic Tool **must not** become a public alternative for those transitions.
