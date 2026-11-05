---
atom_id: CA-R-1135
ref_id: CA-R-1135
container:
  scope_unit: CA-SU-16
role: Requirement
form: Rule
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Data Handling/Source Selection
tier: 1
status: Active
version: 22
updated_at: 2026-11-02 19:44:26 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: TOOLS
---
# Query artifacts by filters

the framework **must** provide one deterministic generic Artifact Tool that returns stably ordered canonical artifact IDs **and** carrier paths matching composable filters for structural scope, layer, tier, Feature, Content role, subject scope, lifecycle state, **and** typed relations **without** loading artifact bodies.

this Tool owns generic artifact-query mechanics **only**. `ATOM_SEARCH` owns CAPRMEDIO Markdown Atom eligibility, selector, lifecycle, subtree, content-query, **and** output-view semantics; it **may** use this Tool as a helper but the generic Tool **must not** become the public Atom-search operation.
