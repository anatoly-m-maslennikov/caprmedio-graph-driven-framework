---
atom_id: CA-R-1134
ref_id: CA-R-1134
container:
  scope_unit: CA-SU-16
role: Requirement
form: Rule
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Storage
tier: 1
status: Active
version: 21
updated_at: 2026-11-02 19:44:26 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: TOOLS
---
# Transition an artifact lifecycle

the framework **must** provide one deterministic generic Artifact Tool that applies one registered artifact lifecycle transition, lazily creates its permitted destination directory, moves the carrier, updates required metadata **and** references, **and** fails closed on an undefined **or** ambiguous state model.

this Tool owns generic lifecycle-transition mechanics **only**. `ATOM_ARCHIVE`, `ATOM_PROMOTE`, `ATOM_UPGRADE`, **and** `CLOSE_ATOM` own their distinct CAPRMEDIO Markdown Atom transition meanings, validation, bulk rules **where** admitted, **and** MCP-gated effects; the generic Tool **must not** become a public alternative for those transitions.
