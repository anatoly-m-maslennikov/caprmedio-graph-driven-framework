---
subjects:
  governs: Subject/Engineering/Carrier
  depends_on: []
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
version: 19
status: Archived
updated_at: 2026-10-24 03:08:30 +0400
content_role: Requirement
current_scope_unit: TOOL_WORKFLOWS
claim_target_scope_unit: TOOL_WORKFLOWS
atom_id: CA-R-1133@19
tier: 3
type: Rule
author: Anatoly Maslennikov
---
# Summary

Rename an artifact carrier

## Scope

Generic Artifact rename orchestration and its boundary with logical Atom relocation.

## Claim

the framework **must** provide one deterministic generic Artifact Workflow that plans one artifact carrier rename under the active filename grammar, rejects collisions, plans governed canonical reference rewrites, records the identity mapping, **and** rolls back the complete rename **when** **any** required rewrite fails.

this Workflow owns generic naming and reference-rewrite policy and its admitted transaction safeguards, not connector mechanics. It supplies each exact storage target and delta, schema and authority bindings and expected state to the connector under CA-R-1936-CONNECTOR_TOOLS-CORE-REQUIREMENT--use-one-coherent-connector-interface; the connector does not select names, references or recovery. `ATOM_MOVE` owns CAPRMEDIO Atom relocation, identity preservation, destination validation, one-Atom storage-effect safeguards **and** MCP-gated effect semantics; the generic Workflow **must not** become a public alternative for moving such Atoms. This generic rename contract does not add automatic incoming-reference retargeting to Atom replacement.

## Details
