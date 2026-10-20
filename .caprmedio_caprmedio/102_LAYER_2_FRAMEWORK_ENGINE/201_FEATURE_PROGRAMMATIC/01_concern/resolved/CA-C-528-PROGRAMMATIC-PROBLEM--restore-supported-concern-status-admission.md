---
atom_id: CA-C-528
content_role: Concern
type: Problem
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Resolved
priority: high
subjects:
  governs: Entity/Node/Continuant/Atom
  depends_on: []
relations:
  concern_about: [CA-P-2401]
version: 4
updated_at: "2026-10-20T16:01:28.000Z"
---
# Summary

Restore supported Concern status admission

## Concern

The unchanged complete-carrier preflight cannot admit a new Active Concern/Problem because its supported authority closure cannot establish the Concern status model. This is an observed current authoring blocker; it is not proof that the proposed carrier is a Draft or that every MCP route fails.

## Evidences

On 2026-10-20, ordinary MCP discover_tools(create_atom) and get_execution_context(create_atom) recovered and creation preview mcp-audit-c525-20261020-preview returned a proposal receipt. A read-only local prepare_create_atom_revision call for the proposed CA-C-525 Active Problem then refused before effects with ToolError complete-carrier-invalid, caused by ProposedCarrierError complete-carrier validation failed or is unresolved.

A read-only observer retained the unchanged validator result: findings=[], one AUTHORITY_UNSUPPORTED gap on atom_id, reason `Concern Draft classification requires its supported Status model.`, bound to CA-D-446 v14 / 4f075efddfa6ff3889d9d7f887010ced0bba2f5e85969e0a20ff06a8b8897b2a. The proposed metadata carries content_role Concern, type Problem and status Active. No effect, Run execution or source change was performed by either preflight; preview is not complete-carrier validation. This observation is after the historical five-day audit window and is separate from CA-C-525's graph-authority pin mismatch.

Continuation checkpoint: CA-P-2420 removed the retired lowercase Concern-only identity branch. Current inherited R1608v8/R1947v3 status semantics now drive canonical Draft admission under D446v14 identity rules. Seventeen focused tests and516full validator tests passed; independent read-only review found no Concern semantic regression. This is source-level evidence only. The selected Docker golden corpus still had retired lowercase Concern statuses; CA-P-2427 updates it before CA-P-2425 isolated MCP acceptance. No installed/runtime repair or full-carrier graph-closure pass is claimed.

## Blast radius

Normal new-Concern authoring cannot claim complete native validation while this authority gap remains. The Operator explicitly authorized manual fallback when MCP cannot do the job; these manual records must not be presented as MCP-published effects or a native validation pass. Diagnose the applicable status-model authority/reader and verify a correction on isolated golden fixtures. Do not weaken schema/status checks or replay uncertain historical mutations to work around it.

### Resolution checkpoint

The approved release proof `.caprmedio_tmp/mcp-audit-20261020/continuation/local-release-verified-20261020.json` and canonical receipt `.caprmedio_runtime/simple_local_release/reports/local-20261020-current-target-parser-repair-1521.md` record the repaired status-admission path completing 410 modules and 3680 tests with zero skips/failures. The preceding isolated gate covered Current Concern Active/Done/Canceled cases with protected production equality, and the released candidate is image `a26b88751f9e8eb57132f648e114f0af4d0c25ff5acf66a6f891f7d05fb4fab3` with fingerprint `b95525f5be4b87c9b342f52199cd8f9260ff4206c2f130090cf63f4cc3e38f76`. This resolves the deployment-blocked status-admission repair only; no historical batch replay, unrestricted Concern capability or public release is claimed.
