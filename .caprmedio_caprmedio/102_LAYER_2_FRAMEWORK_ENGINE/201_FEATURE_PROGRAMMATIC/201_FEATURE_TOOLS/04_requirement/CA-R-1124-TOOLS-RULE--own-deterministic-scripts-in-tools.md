---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Component Structure
  depends_on: []
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
version: 24
updated_at: 2026-10-27 19:59:50 +0400
atom_id: CA-R-1124
status: Active
content_role: Requirement
author: Anatoly Maslennikov
current_scope_unit: TOOLS
type: Rule
tier: 1
---
# Own deterministic scripts in Tools

**every** independently executable deterministic script **must** realize **=1** Tool, **and** **every** Tool **must** have **=1** canonical independently executable script, including a Tool invoked exclusively by a Skill. shared non-executable libraries **may** serve multiple Tools but do **not** constitute Tools themselves.
