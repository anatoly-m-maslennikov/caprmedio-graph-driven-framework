---
atom_id: CA-P-2186
content_role: Plan
type: Plan
label: Task
work_sequence_number: 3
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: Tool
  depends_on: [Atom, Subject, Carrier, Projection, Plan, Operator]
version: 1
updated_at: "2026-10-12 05:40:17 +0400"
relations:
  is_decomposition_of: [CA-P-2183]
---
# Summary

Verify staged Subject candidates independently

## Objective

Independently accept the actual staged files and source-preservation boundary before read-only staged-candidate preparation.

## Details

Estimated own work: 15 minutes. Assignee: AI Agent independent of implementation. Required prerequisites: CA-P-2184 and CA-P-2185. Reopen actual contract/code/source/output pins and re-read staged candidates; producer success alone is insufficient.

Own dedicated independent fixtures under `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/ATOM_UPDATE/tests/test_subject_stage_preview.py` and one bounded verification receipt. Production code and other workers' tests are read-only. Author expected carrier/byte ledgers separately; corrupt staged bytes must fail.

Check fresh generated temporary paths, exact proposed carriers, preserved identity/Status/unrelated bytes, declared source context/provenance and actual validation. Reject stale/invalid inputs, unsafe destinations and staged files entering current-original selection. Compare original/history/Journal pins before/after and prove no publication or source effect-time receipt was created. Preserve default and live refusal behavior.

Deliver an independent staging receipt with actual hashes/checks and limitations. Together with CA-P-1963, it releases read-only current-source adaptation/re-pinning/mapping solely to create and review staged candidates; no original writes occur. Full source implementation, final shared graph/sealed live packet/approval, application and Step 2 retain their existing gates. Split a concrete overrun before execution.

### Definition of Done

The Plan is **not** Done if outputs are self-verified, expected ledgers or wrong-output controls are missing, pins/validation are stale, original/history/Journal/publication changes, staged candidates gain source authority, scratch consumption precedes this receipt, or own work exceeds 15 minutes without decomposition.
