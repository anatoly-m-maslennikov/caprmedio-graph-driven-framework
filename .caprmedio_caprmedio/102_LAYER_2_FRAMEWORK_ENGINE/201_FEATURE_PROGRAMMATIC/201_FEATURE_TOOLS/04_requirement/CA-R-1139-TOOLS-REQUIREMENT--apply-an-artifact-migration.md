---
subjects:
  governs: artifact-migration
  depends_on: []
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
version: 15
updated_at: 2026-10-24 02:14:24 +0400
atom_id: CA-R-1139
status: Active
content_role: Requirement
author: Anatoly Maslennikov
current_scope_unit: TOOLS
type: Rule
tier: 1
---
# Apply an artifact migration

the framework **must** provide one deterministic generic Artifact Tool that applies one approved migration plan **only** **when** its recorded preconditions still match, commits **all** carrier **and** reference mutations as one rollbackable transaction, **and** appends the governed migration event through the Work Journal Tool.

this Tool owns generic migration-transaction mechanics **only**. `MIGRATE_ATOM_IDENTITY` **and** `REBIND_ATOM_RELATIONS` own their sealed CAPRMEDIO Markdown Atom migration **and** rebinding semantics, including their exact source, revision, relation, **and** MCP-gated effect boundaries; the generic Tool **must not** become a public alternative for those Atom changes.
