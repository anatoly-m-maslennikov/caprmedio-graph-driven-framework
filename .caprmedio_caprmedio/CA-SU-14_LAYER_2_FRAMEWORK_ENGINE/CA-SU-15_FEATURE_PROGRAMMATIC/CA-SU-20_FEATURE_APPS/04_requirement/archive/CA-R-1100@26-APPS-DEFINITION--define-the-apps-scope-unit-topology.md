---
atom_id: CA-R-1100
ref_id: CA-R-1100@26
container:
  scope_unit: CA-SU-20
role: Requirement
form: Definition
topics:
  main_subject: CAPRMEDIO_MODEL <+ Scope Unit
tier: 1
status: Archived
version: 26
updated_at: 2026-11-03 23:17:14 +0400
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: APPS
carrier_destination:
  file:
    name: CA-R-1100@26-APPS-DEFINITION--define-the-apps-scope-unit-topology.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/04_requirement/archive
---
## Summary

Define the APPS Scope Unit topology

## Claim

### Prose Claim

`APPS` **must** own the following immediate `unordered_unit` Scope Units: `WORKBENCH`, `GRAPH_UI`, **and** `AGENT_HOST_PLUGINS`.

- `WORKBENCH` owns the headless source indexer, rebuildable graph read model, **and** read-only query service derived from governed Atoms **and** Journals.
- `GRAPH_UI` owns the optional human interface over `WORKBENCH` **and** **must not** be required for headless Tool or MCP operation.
- `AGENT_HOST_PLUGINS` owns host-specific integration packages.

None of these applications, their databases, interfaces, or Projections becomes project authority.
