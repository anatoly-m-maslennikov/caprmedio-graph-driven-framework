---
atom_id: CA-R-1124
ref_id: CA-R-1124
container:
  scope_unit: CA-SU-16
role: Requirement
form: Rule
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Component
    Structure
tier: 1
status: Active
version: 25
updated_at: 2026-11-02 19:44:26 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: TOOLS
---
# Own deterministic scripts in Tools

**every** independently executable deterministic script **must** realize **=1** Tool, **and** **every** Tool **must** have **=1** canonical independently executable script, including a Tool invoked exclusively by a Skill. shared non-executable libraries **may** serve multiple Tools but do **not** constitute Tools themselves.
