---
atom_id: CA-P-1850
content_role: Plan
type: Plan
label: Task
work_sequence_number: 2
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
status: Active
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-10 18:08:27 +0400"
subjects:
  governs: "CAPRMEDIO Framework Instance"
  depends_on: [Project, Plan, AI Agent, Operator, Framework Instance Settings, Journal, Workflow Run, Action, Workflow, Framework Package, Carrier]
relations:
  is_decomposition_of: [CA-P-1848]
  blocks: [CA-P-1855]
---
# Summary

Protect existing state during installation migration

## Objective

the AI Agent supplies a verified migration that preserves existing operational state while `.caprmedio_install` becomes the beta package boundary.

## Details

1. Verify the corrected source registrations point authoring Methodology Sources to the Project Methodology unit before Local release changes product or installed Methodology. Treat `.caprmedio_caprmedio/000_CAPRMEDIO_framework` as read-only installed content until its ordered replacement step.
2. Repair `INSTALL_TOOLS/install_tools.py` whole-directory legacy deletion; explicit owned paths must never remove live state, historical evidence, credentials or unrelated contents.
3. Test quiescing, exact inventories, migration into selected-Project `.caprmedio_runtime`, selector updates, resumability and rollback with disposable fixtures. Preserve Journal records and honestly record interrupted Runs.
4. Actual Project state moves occur only inside Local release after its complete preflight suite passes before the first destructive product wipe. Preserve `caprmedio_framework_settings.toml`, authoritative configuration, Project Structure, Operator registry and support settings; generated manifests/selectors may refresh.
5. Require explicit retention/disposition for unmapped/protected content. Do not perform migration merely by authoring this Plan.

### Definition of Done

the Plan is **not** Done **if** stale source registration remains, legacy installation can delete operational state, an existing record is lost or reported as success, migration cannot resume/rollback, protected settings are replaced, or live cutover precedes the local gate.
