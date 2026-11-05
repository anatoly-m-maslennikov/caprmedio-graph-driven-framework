---
atom_id: CA-R-1131
ref_id: CA-R-1131
container:
  scope_unit: CA-SU-16
role: Requirement
form: Rule
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Relation
tier: 1
status: Active
version: 23
updated_at: 2026-11-02 19:44:26 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: TOOLS
---
# Patch artifact relations

the framework **must** provide one deterministic generic Artifact Tool that adds, replaces, **or** removes explicitly selected typed relation targets **and** `relational_endpoints` descriptors by canonical project-graph node reference, including relative Scope Unit references that use exact full names **and** resolve from the source Artifact owner, while validating permitted relation kind, source **and** target classes, direction, lifecycle, cardinality, Content-role applicability, **and** endpoint identity **without** changing the Artifact body.

this Tool owns generic relation-patch mechanics **only**. it **must not** be exposed **or** applied as a substitute for a CAPRMEDIO Markdown Atom operation; `ATOM_UPDATE` owns declared Atom updates **and** `REBIND_ATOM_RELATIONS` owns its sealed Atom-rebinding case, including their target, revision, transaction, **and** MCP-gated effect semantics.
