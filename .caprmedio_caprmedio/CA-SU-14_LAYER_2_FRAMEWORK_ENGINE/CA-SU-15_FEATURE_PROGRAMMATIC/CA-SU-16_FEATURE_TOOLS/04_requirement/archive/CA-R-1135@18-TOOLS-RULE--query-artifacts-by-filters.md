---
subjects:
  governs: Subject/Graph Node/Engineering/Artifact Query
  depends_on: []
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
version: 18
updated_at: 2026-10-25 17:32:27 +0400
atom_id: CA-R-1135@18
status: Archived
content_role: Requirement
author: Anatoly Maslennikov
current_scope_unit: TOOLS
type: Rule
tier: 1
---
# Query artifacts by filters

the framework **must** provide one deterministic generic Artifact Tool that returns stably ordered canonical artifact IDs **and** carrier paths matching composable filters for structural scope, layer, tier, Feature, Content role, subject scope, lifecycle state, **and** typed relations **without** loading artifact bodies.

this Tool owns generic artifact-query mechanics **only**. `ATOM_SEARCH` owns CAPRMEDIO Markdown Atom eligibility, selector, lifecycle, subtree, content-query, **and** output-view semantics; it **may** use this Tool as a helper but the generic Tool **must not** become the public Atom-search operation.
