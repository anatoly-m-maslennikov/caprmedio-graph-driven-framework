---
atom_id: CA-C-528
content_role: Concern
type: Problem
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Active
priority: high
subjects:
  governs: Entity/Node/Continuant/Atom
  depends_on: []
relations:
  concern_about: [CA-P-2401]
version: 1
updated_at: "2026-10-20 15:30:14 +0400"
---
# Summary

Restore supported Concern status admission

## Concern

The unchanged complete-carrier preflight cannot admit a new Active Concern/Problem because its supported authority closure cannot establish the Concern status model. This is an observed current authoring blocker; it is not proof that the proposed carrier is a Draft or that every MCP route fails.

## Evidences

On 2026-10-20, ordinary MCP discover_tools(create_atom) and get_execution_context(create_atom) recovered and creation preview mcp-audit-c525-20261020-preview returned a proposal receipt. A read-only local prepare_create_atom_revision call for the proposed CA-C-525 Active Problem then refused before effects with ToolError complete-carrier-invalid, caused by ProposedCarrierError complete-carrier validation failed or is unresolved.

A read-only observer retained the unchanged validator result: findings=[], one AUTHORITY_UNSUPPORTED gap on atom_id, reason `Concern Draft classification requires its supported Status model.`, bound to CA-D-446 v14 / 4f075efddfa6ff3889d9d7f887010ced0bba2f5e85969e0a20ff06a8b8897b2a. The proposed metadata carries content_role Concern, type Problem and status Active. No effect, Run execution or source change was performed by either preflight; preview is not complete-carrier validation. This observation is after the historical five-day audit window and is separate from CA-C-525's graph-authority pin mismatch.

## Blast radius

Normal new-Concern authoring cannot claim complete native validation while this authority gap remains. The Operator explicitly authorized manual fallback when MCP cannot do the job; these manual records must not be presented as MCP-published effects or a native validation pass. Diagnose the applicable status-model authority/reader and verify a correction on isolated golden fixtures. Do not weaken schema/status checks or replay uncertain historical mutations to work around it.
