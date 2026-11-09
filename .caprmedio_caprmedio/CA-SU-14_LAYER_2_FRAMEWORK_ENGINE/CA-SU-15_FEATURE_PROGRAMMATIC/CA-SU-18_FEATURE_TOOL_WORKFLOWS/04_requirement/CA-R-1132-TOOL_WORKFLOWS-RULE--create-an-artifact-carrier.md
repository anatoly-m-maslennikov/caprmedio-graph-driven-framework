---
atom_id: CA-R-1132
ref_id: CA-R-1132
container:
  scope_unit: CA-SU-18
role: Requirement
form: Rule
topics:
  main_subject: "Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Storage"
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Term//Artifact
  - Subject/CAPRMEDIO/Carrier
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role
tier: 3
status: Active
version: 28
updated_at: 2026-10-27 19:59:50 +0400
carrier_destination:
  file:
    name: CA-R-1132-TOOL_WORKFLOWS-RULE--create-an-artifact-carrier.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-18_FEATURE_TOOL_WORKFLOWS/04_requirement
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
current_scope_unit: TOOL_WORKFLOWS
claim_target_scope_unit: TOOL_WORKFLOWS
author: Anatoly Maslennikov
---
# Summary

Create an artifact carrier

## Scope

Generic Artifact construction orchestration and its boundary with logical CreateAtom.

## Claim

the framework **must** provide one deterministic generic Artifact Workflow that selects the canonical identity **and** filename required by the admitted Artifact Carrier schema **and** creates one Carrier from its structural owner **and** the inputs required by that schema, **without** silently overwriting an existing Carrier.

this Workflow owns generic construction, identity and naming decisions, not connector mechanics. Its connector receives the complete explicit target and content, supplied schema and authority bindings and expected absence under CA-R-1936-CONNECTOR_TOOLS-RULE--use-one-coherent-connector-interface; it does not allocate identity or choose ownership. `ATOM_CREATE` owns CAPRMEDIO Atom admission, stable-identity, revision, per-Atom preflight **and** MCP-gated effect semantics; the generic Workflow **must not** become a public alternative for creating such Atoms.

## Details
