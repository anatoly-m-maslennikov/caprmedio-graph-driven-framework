---
atom_id: CA-R-1101
ref_id: CA-R-1101@22
container:
  scope_unit: CA-SU-20
role: Requirement
form: Definition
topics:
  main_subject: CAPRMEDIO_MODEL <+ Scope Unit
tier: 1
status: Archived
version: 22
updated_at: 2026-11-02 19:44:26 +0400
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: APPS
carrier_destination:
  file:
    name: CA-R-1101@22-APPS-DEFINITION--define-the-agent-host-plugins-unit.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/04_requirement/archive
---
## Summary

Define the AGENT_HOST_PLUGINS unit

## Claim

### Prose Claim

`AGENT_HOST_PLUGINS` with prefix `AGENT_HOST_PLUGINS` **must** be one `unordered_unit` owned immediately by `APPS` at Structural level `4`, addressed by `002_FRAMEWORK_ENGINE/PROGRAMMATIC/APPS/AGENT_HOST_PLUGINS`, **and** realized under `002_FRAMEWORK_ENGINE/PROGRAMMATIC/APPS/AGENT_HOST_PLUGINS/`; it owns installable agent-host-specific plugin packages **and** their host wiring **without** duplicating provider-neutral CAPRMEDIO Skill, Tool, **or** Methodology behavior.
