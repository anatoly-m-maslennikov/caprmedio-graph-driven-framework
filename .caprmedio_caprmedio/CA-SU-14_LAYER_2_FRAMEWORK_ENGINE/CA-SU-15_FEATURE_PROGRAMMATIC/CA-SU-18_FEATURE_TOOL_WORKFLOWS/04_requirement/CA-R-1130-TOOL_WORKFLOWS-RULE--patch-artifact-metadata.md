---
atom_id: CA-R-1130
ref_id: CA-R-1130
container:
  scope_unit: CA-SU-18
role: Requirement
form: Rule
topics:
  main_subject: "Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Storage"
tier: 3
status: Active
version: 27
updated_at: 2026-11-02 19:44:26 +0400
carrier_destination:
  file:
    name: CA-R-1130-TOOL_WORKFLOWS-RULE--patch-artifact-metadata.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-18_FEATURE_TOOL_WORKFLOWS/04_requirement
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
current_scope_unit: TOOL_WORKFLOWS
claim_target_scope_unit: TOOL_WORKFLOWS
author: Anatoly Maslennikov
---
# Summary

Patch artifact metadata

## Scope

Generic Artifact metadata-patch orchestration and its boundary with logical Atom Modify.

## Claim

the framework **must** provide one deterministic generic Artifact Workflow that derives a schema-validated field-level patch **to** one artifact's frontmatter, preserves its body bytes, decides governed revision metadata, **and** rejects unknown fields **or** failed preconditions before delegating the explicit storage delta.

this Workflow owns form-agnostic patch and revision policy, not connector mechanics. Its connector receives only explicit content or edits, supplied schema and authorization context and expected state under CA-R-1936-CONNECTOR_TOOLS-RULE--use-one-coherent-connector-interface; the connector makes no revision or lifecycle decision. The generic procedure **must not** be exposed **or** applied as a substitute for `ATOM_UPDATE` **to** a CAPRMEDIO Markdown Atom; the Atom Workflow owns that Atom's target resolution, authority validation, revision transition, one-Atom storage-effect safeguards **and** MCP-gated effect, **and** **may** use this procedure **only** as an internal helper.

## Details
