---
atom_id: CA-P-1983
content_role: Plan
type: Plan
label: Task
work_sequence_number: 2
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: Tool
  depends_on: [Atom, Subject, Requirement, Method, Evaluation, Delivery, Operations, Plan, Operator]
version: 1
updated_at: "2026-10-10 23:51:04 +0400"
relations:
  is_decomposition_of: [CA-P-1980]
  blocks: [CA-P-1984, CA-P-1985, CA-P-1986, CA-P-1987]
---
# Summary

Normalize legacy Subject Tool definitions

## Objective

Restore current carrier metadata and Summary form for the seven pinned legacy Tool definitions, without changing their existing substantive claims.

## Details

Estimated own work: 15 minutes. Assignee: AI Agent. Required prerequisites: CA-P-1982.

Exclusive files: Search CA-R-863, CA-E-301, CA-D-038, CA-D-424, CA-O-046; Update CA-D-041 and CA-D-425. Use one small ad-hoc script with exact before hashes from the CA-P-1979 report. Preserve IDs, filenames, titles as Summary, Subjects, relations and original body text. Set declared TOOLS ownership, current role, Active Status, standard tiers and author; increment each Version by one with actual Project-time updated_at. Do not infer separate Tool Scope Units. Default to preview; check every pin before an explicitly authorized authoring repair. Git retains prior contents. Output: corrected carrier metadata, script and before/after receipt. No generic reusable repair API.

Use the shared minimum contract in the CA-P-1979 review. A worker owns only the listed files; root owns integration, commits and Task completion. Recheck source pins after normalization. No unrelated changes, Core entity-model edits, source migration, runtime activation or release work. Ask for a concrete unresolved decision below 90% confidence. Decompose before exceeding 15 minutes.

### Definition of Done

The Plan is **not** Done if its stated output or exact before/after evidence is missing; a file outside its exclusive scope changes; preserved claims or identity are lost; the cross-role contract conflicts; checks fail; a prerequisite is incomplete; or own work exceeds 15 minutes without decomposition.
