---
atom_id: CA-P-2560
content_role: Plan
type: Plan
label: Task
work_sequence_number: 3
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Done
version: 3
updated_at: "2026-10-21T19:05:01Z"
subjects:
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  is_decomposition_of: [CA-P-2557]
  depends_on: [CA-P-2558]
  relates_to: [CA-M-396, CA-M-397, CA-M-398, CA-M-399, CA-M-400]
---
# Summary

Preserve partial AtomSearch results with response errors

## Objective

Integrate the shared owner with AtomSearch: retain verified valid matches when a selected Atom is invalid, expose explicit response errors as well as incomplete status, and emit WARNING technical logs. Preserve safety/binding refusals and avoid duplicate diagnostic emission.

## Details

One Task per file. After completion, review and update dependant Tasks before their execution. Actual business Workflow lifecycle recording remains with its declared executor; this Task does not invent it in an error decorator.

### Definition of Done

Golden/disposable functional and MCP protocol checks verify partial data plus attributable errors, all-invalid input, unchanged source/Journal bytes, service survival, and unchanged unsafe-effect refusals. At most 15 minutes own work.

### Execution checkpoint

AtomSearch retains valid matches and per-carrier warnings, with complete:false and explicit schema_invalid response errors when invalid carriers are skipped. All-invalid scans remain attributable incomplete results. Unsafe source/identity/frontier failures still refuse the affected lookup rather than returning unsafe partial data. Other provider refusals emit WARNING, and logger absence is visible in the response without a guessed Project prefix. The Tools portfolio initially ran 64 cases in 21.657 seconds and found one stale errors=[] assertion; only that test expectation changed. Its related 10-case provider module then passed in 1.175 seconds, retaining the other passing cases. Final related 32-case rerun and independent review pass. No source/Journal mutation or deployment is claimed.
