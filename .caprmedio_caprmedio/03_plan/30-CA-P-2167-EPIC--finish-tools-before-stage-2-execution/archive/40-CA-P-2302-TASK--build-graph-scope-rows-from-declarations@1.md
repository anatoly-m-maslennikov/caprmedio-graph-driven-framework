---
atom_id: CA-P-2302
content_role: Plan
type: Plan
label: Task
work_sequence_number: 40
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: Tool
  depends_on: [Scope Unit, Projection, Plan, Project Structure]
version: 1
updated_at: "2026-10-13 04:51:49 +0400"
relations:
  is_decomposition_of: [CA-P-2167]
  blocks: [CA-P-2303]
---
# Summary

Build graph Scope rows from declarations

## Objective

Construct Scope Unit semantic rows from the complete validated Project Structure declarations, using declared parent, type, label, level, ordering/navigation and paths. Include declared untyped and absent authority folders; preserve established node IDs where their declarations match. Directory shape must not override declared topology. Reuse actual validation and preserve explicit Delivery binding. No source/Scope folder/Subject migration or graph output publication is included.

## Details

Estimated own work: 15 minutes. Split larger work before execution. Reopen R1070/M149/E295 and current Structure authority. Preserve the accepted Delivery-only implementation/receipt as a separate checkpoint. An author owns generator and focused tests; a different reviewer owns independent verification. Root owns Plans and Git.

CA-P-2303 may consume the stable first candidate within the same isolated implementation packet before final independent acceptance; no affected Tool use is admitted until CA-P-2304 accepts the complete resulting pins. Earlier source acceptance and tests are not current runtime readiness.

### Definition of Done

Not Done until the bounded outcome has exact code/source pins and actual focused checks; the combined repair requires independent CA-P-2304 acceptance. Invalid declarations must still refuse. No historical pin rebinding, live source effects, Subject changes or production graph output is authorized.
