---
atom_id: CA-R-1101
ref_id: CA-R-1101
container:
  scope_unit: CA-SU-20
role: Requirement
form: Definition
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
tier: 1
status: Active
version: 22
updated_at: 2026-11-02 19:44:26 +0400
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: APPS
---
# Define the AGENT_HOST_PLUGINS unit

`AGENT_HOST_PLUGINS` with prefix `AGENT_HOST_PLUGINS` **must** be one `unordered_unit` owned immediately by `APPS` at Structural level `4`, addressed by `002_FRAMEWORK_ENGINE/PROGRAMMATIC/APPS/AGENT_HOST_PLUGINS`, **and** realized under `002_FRAMEWORK_ENGINE/PROGRAMMATIC/APPS/AGENT_HOST_PLUGINS/`; it owns installable agent-host-specific plugin packages **and** their host wiring **without** duplicating provider-neutral CAPRMEDIO Skill, Tool, **or** Methodology behavior.
