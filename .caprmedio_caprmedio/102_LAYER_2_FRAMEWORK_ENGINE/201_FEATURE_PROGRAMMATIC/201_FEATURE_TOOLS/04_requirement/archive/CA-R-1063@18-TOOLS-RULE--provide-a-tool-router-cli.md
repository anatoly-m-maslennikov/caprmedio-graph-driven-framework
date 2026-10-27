---
subjects:
  governs: Subject/Engineering/Tool
  depends_on: []
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
version: 18
updated_at: 2026-10-24 23:19:22 +0400
atom_id: CA-R-1063@18
status: Archived
content_role: Requirement
author: Anatoly Maslennikov
current_scope_unit: TOOLS
type: Rule
tier: 1
---
# Provide a Tool router CLI

the framework **must** provide one deterministic CLI Tool router that accepts an LLM-selected intent, classifies it as a read-only `finder` intent **or** a mutating **or** materializing `doer` intent, resolves it through as many registered routing steps as required, returns **every** applicable Tool option **without** silently selecting **or** executing one, **and**, **after** the LLM selects an option, returns sufficient machine-readable how-to guidance **to** invoke that Tool correctly, including its command shape, required **and** optional inputs, admissible values, preconditions, effects, success checks, failure modes, **and** representative examples.
