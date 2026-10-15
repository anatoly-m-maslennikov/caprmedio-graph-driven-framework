---
atom_id: CA-P-2381
content_role: Plan
type: Plan
label: Task
work_sequence_number: 59
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: Tool
  depends_on: [Atom, Subject, Projection, Plan]
version: 1
updated_at: "2026-10-14 11:17:35 +0400"
relations:
  is_decomposition_of: [CA-P-2167]
---
# Summary

Prepare logical Subject preview request

## Objective

Adapt CA-P-2372's exact accepted 611-owner request to the now-delivered direct MCP preview schema without invoking preparation or mutation.

## Details

Keep the original request and manifest unchanged. Verify their exact hashes and source pins; convert only the transport envelope to operation preview_subjects, explicit profile and logical Atom ID/Version/SHA-256 with the existing explicit patches. Preserve payload order, all 848 patches, exclusions and reviewed mappings. Physical selectors belong only in the provenance sidecar, never the public request. Validate the closed canonical input model without invoking its adapter. No preview seal, candidate Atom bytes, stage, approval or source effect is produced.

Own only derived scripts, tests and request/provenance files under .caprmedio_tmp/stage2-migration-20261014/public-request. Estimated work: up to 15 minutes. Root owns integration and Git; preserve unrelated work and all original sources.

### Definition of Done

Focused checks prove exact transport conversion, unchanged order/patches, preserved owner exclusions and stale-input/source refusal. An independent reviewer accepts the emitted request and its pins. Readiness states that connected MCP activation, actual preview and staging remain unperformed. This does not complete the parent Epic.
