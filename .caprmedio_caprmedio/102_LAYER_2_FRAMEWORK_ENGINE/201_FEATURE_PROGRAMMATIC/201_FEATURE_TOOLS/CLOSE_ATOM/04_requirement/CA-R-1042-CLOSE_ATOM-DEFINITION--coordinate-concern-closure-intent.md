---
subjects:
  governs: 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Concern'
  depends_on: []
version: 17
updated_at: 2026-10-25 17:32:27 +0400
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-R-1042
status: Active
content_role: Requirement
author: Anatoly Maslennikov
current_scope_unit: TOOLS
type: Definition
tier: 1
---
# Coordinate Concern closure intent

`CLOSE_ATOM` is the canonical CAPRMEDIO Markdown Atom Doer that coordinates one active Concern's transition **to** `solved`. It accepts one exact active Concern Atom ID, one explicit terminal disposition, optional explicit resolver **and** subject Atom-ID lists, **and** action context. It rejects missing, non-Concern, inactive, **or** unresolved referenced Atom IDs **and** returns one sealed closure action. Resolver **and** subject IDs describe supplied intent **only**; the Tool **must not** infer relation kinds, role meanings, **or** a participant that was **not** supplied.

the Tool **must** use the canonical Atom lifecycle operation for its effect rather than reimplement generic lifecycle semantics. It **must** default **to** a mutation-free dry run **and** accept `--apply` **only** through an authorized project-local MCP delegation with a sealed Initiative action envelope. A successful effect **must** receive durable `COMMIT_TRIGGER` intake acknowledgement **before** MCP reports success; `CLOSE_ATOM` itself does **not** append the Journal, stage files, **or** create a Git commit.
