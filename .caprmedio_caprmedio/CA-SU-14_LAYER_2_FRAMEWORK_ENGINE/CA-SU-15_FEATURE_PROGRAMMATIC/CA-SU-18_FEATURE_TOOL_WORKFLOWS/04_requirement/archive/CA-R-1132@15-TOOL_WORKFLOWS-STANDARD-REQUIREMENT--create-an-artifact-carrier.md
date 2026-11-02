---
subjects:
  governs: artifact-operations
  depends_on:
  - Artifact
  - Subject/Engineering/Carrier
  - Subject/Domain/Node/Continuant/Atom/Content Role
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
version: 15
status: Archived
updated_at: 2026-10-23 03:18:40 +0400
content_role: Requirement
current_scope_unit: TOOL_WORKFLOWS
claim_target_scope_unit: TOOL_WORKFLOWS
local_tier: Standard
global_tier: 11
atom_id: CA-R-1132@15
---
# Summary

Create an artifact carrier

## Scope

Generic Artifact construction orchestration and its boundary with logical CreateAtom.

## Claim

the framework **must** provide one deterministic generic Artifact Workflow that selects the canonical identity **and** filename required by the admitted Artifact Carrier schema **and** creates one Carrier from its structural owner **and** the inputs required by that schema, **without** silently overwriting an existing Carrier.

this Workflow owns generic construction, identity and naming decisions, not connector mechanics. Its connector receives the complete explicit target and content, supplied schema and authority bindings and expected absence under CA-R-1936-CONNECTOR_TOOLS-CORE-REQUIREMENT--use-one-coherent-connector-interface; it does not allocate identity or choose ownership. `ATOM_CREATE` owns CAPRMEDIO Atom admission, stable-identity, revision, per-Atom preflight **and** MCP-gated effect semantics; the generic Workflow **must not** become a public alternative for creating such Atoms.

## Details
