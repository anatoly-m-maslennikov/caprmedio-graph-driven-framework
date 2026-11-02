---
subjects:
  governs: artifact-query
  depends_on: []
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
version: 12
updated_at: 2026-10-24 00:28:02 +0400
atom_id: CA-R-1135@12
status: Archived
---
# Query artifacts by filters

the framework **must** provide one deterministic generic Artifact Tool that returns stably ordered canonical artifact IDs **and** carrier paths matching composable filters for structural scope, layer, tier, Feature, Content role, subject scope, lifecycle state, **and** typed relations **without** loading artifact bodies.

this Tool owns generic artifact-query mechanics **only**. `ATOM_SEARCH` owns CAPRMEDIO Markdown Atom eligibility, selector, lifecycle, subtree, content-query, **and** output-view semantics; it **may** use this Tool as a helper but the generic Tool **must not** become the public Atom-search operation.
