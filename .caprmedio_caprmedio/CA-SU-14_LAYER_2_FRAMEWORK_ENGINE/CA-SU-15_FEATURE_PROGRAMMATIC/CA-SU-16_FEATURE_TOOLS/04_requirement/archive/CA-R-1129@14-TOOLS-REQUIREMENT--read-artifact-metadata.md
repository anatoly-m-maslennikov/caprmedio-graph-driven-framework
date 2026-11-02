---
subjects:
  governs: Subject/Engineering/Artifact Query
  depends_on: []
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
version: 14
updated_at: 2026-10-24 00:51:05 +0400
atom_id: CA-R-1129@14
status: Archived
content_role: Requirement
author: Anatoly Maslennikov
current_scope_unit: TOOLS
---
# Read artifact metadata

the framework **must** provide one deterministic generic Artifact Tool that returns selected frontmatter fields **and** derived carrier identity for one artifact **without** loading its body, with explicit results for absent fields **and** parse errors.

this Tool owns form-agnostic metadata retrieval **only**. it does **not** define CAPRMEDIO Markdown Atom selector, lifecycle, identity, **or** output-view semantics; **when** used for an Atom, `ATOM_READ` owns the public Atom operation **and** **may** use this Tool **only** as a helper.
