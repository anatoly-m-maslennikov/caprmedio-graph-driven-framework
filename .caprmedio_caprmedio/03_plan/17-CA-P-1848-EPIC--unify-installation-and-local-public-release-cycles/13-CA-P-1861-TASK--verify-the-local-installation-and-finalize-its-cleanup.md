---
atom_id: CA-P-1861
content_role: Plan
type: Plan
label: Task
work_sequence_number: 13
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
status: Active
author: Anatoly Maslennikov
version: 4
updated_at: "2026-10-10 18:08:27 +0400"
subjects:
  governs: "CAPRMEDIO Framework Instance"
  depends_on: [Project, Plan, AI Agent, Operator, Framework Instance Settings, Framework Package, Applicable Methodology, Tool, Workflow, Action, Workflow Run, Journal, Carrier, Evaluation]
relations:
  is_decomposition_of: [CA-P-1848]
  blocks: [CA-P-1862]
---
# Summary

Verify the local installation **and** finalize its cleanup

## Objective

the AI Agent verifies Local release evidence and only its declared cleanup within the same programmatic command.

## Details

1. Verify the installed Project runs the selected reusable package, installed Methodology is the as-is product copy subject only to declared preserved settings, `ca` resolves from the installed runtime, and the selected image/restart returns the expected MCP endpoint.
2. Verify source/product/installed provenance, package/image/lock identity, preserved configuration/state and isolated Project resources.
3. Retain root `101_FRAMEWORK_METHODOLOGY` as the product boundary. Do not retire it as a legacy copy or delete authoring/recovery evidence. Cleanup remains limited to declared replaced installed/package content.
4. Record the honest terminal result without a separate handover or review command.

### Definition of Done

the Plan is **not** Done **if** installed execution/discovery fails, product and installed identities conflict outside an allowed exception, configuration or Project-owned evidence is absent, cleanup exceeds declared targets, or endpoint evidence is unverified.
