---
atom_id: CA-R-1133
ref_id: CA-R-1133
container:
  scope_unit: CA-SU-18
role: Requirement
form: Rule
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Storage
tier: 3
status: Active
version: 26
updated_at: 2026-11-02 19:44:26 +0400
carrier_destination:
  file:
    name: CA-R-1133-TOOL_WORKFLOWS-RULE--rename-an-artifact-carrier.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-18_FEATURE_TOOL_WORKFLOWS/04_requirement
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
current_scope_unit: TOOL_WORKFLOWS
claim_target_scope_unit: TOOL_WORKFLOWS
author: Anatoly Maslennikov
---
# Summary

Rename an artifact carrier

## Scope

Generic Artifact rename orchestration and its boundary with logical Atom relocation.

## Claim

the framework **must** provide one deterministic generic Artifact Workflow that plans one artifact carrier rename under the active filename grammar, rejects collisions, plans governed canonical reference rewrites, records the identity mapping, **and** rolls back the complete rename **when** **any** required rewrite fails.

this Workflow owns generic naming and reference-rewrite policy and its admitted transaction safeguards, not connector mechanics. It supplies each exact storage target and delta, schema and authority bindings and expected state to the connector under CA-R-1936-CONNECTOR_TOOLS-RULE--use-one-coherent-connector-interface; the connector does not select names, references or recovery. `ATOM_MOVE` owns CAPRMEDIO Atom relocation, identity preservation, destination validation, one-Atom storage-effect safeguards **and** MCP-gated effect semantics; the generic Workflow **must not** become a public alternative for moving such Atoms. This generic rename contract does not add automatic incoming-reference retargeting to Atom replacement.

## Details
