---
subjects:
  governs: Subject/Graph Node/Engineering/Architecture/Communication
  depends_on: []
version: 20
updated_at: 2026-10-27 06:04:45 +0400
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-R-1104
status: Active
content_role: Requirement
author: Anatoly Maslennikov
current_scope_unit: APPS
type: Rule
tier: 1
---
# Route selected graph context into governed Codex work

`CODEX_PLUGIN` **must** let an operator transfer the canonical identities, paths, current digests, **and** declared selection boundary of GRAPH_UI nodes into a Codex conversation, ask questions about that bounded context, **and** request applicable CAPRMEDIO work through existing Skills **and** the provider-neutral MCP Tool interface. The plugin **must not** implement project mutation itself, widen the selected scope implicitly, bypass Tool validation **or** host permissions, expose secrets, **or** perform an irreversible action **without** the host's required operator confirmation; results **must** preserve Tool meaning, provenance, **and** explicit failure states.
