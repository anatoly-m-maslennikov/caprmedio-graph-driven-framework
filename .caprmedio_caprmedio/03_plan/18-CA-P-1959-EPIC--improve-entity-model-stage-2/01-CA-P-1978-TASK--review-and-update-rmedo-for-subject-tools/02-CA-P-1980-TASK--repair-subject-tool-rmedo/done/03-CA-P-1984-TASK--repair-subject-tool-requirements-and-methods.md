---
atom_id: CA-P-1984
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
status: Done
subjects:
  governs: Tool
  depends_on: [Atom, Subject, Requirement, Method, Evaluation, Delivery, Operations, Plan, Operator]
version: 2
updated_at: "2026-10-10 23:57:34 +0400"
relations:
  is_decomposition_of: [CA-P-1980]
---
# Summary

Repair Subject Tool Requirements and Methods

## Objective

Define the minimum valid-file Subject lookup and patch-preview outcomes and implementation methods.

## Details

Estimated own work: 15 minutes. Assignee: AI Agent. Required prerequisites: CA-P-1982, CA-P-1983.

Exclusive files: CA-R-863 and CA-R-866; new CA-M-370 and CA-M-371 under the respective 05_method folders, owned by TOOLS. Reserve those new IDs and recheck uniqueness before authoring. Consume the repaired metadata and CA-P-1979 pins/ledger. Add structural field lookup with lexical exact/prefix matching, explicit valid-file filters, exact occurrence pins; add a separate Subject-only preview with explicit pinned replacements and complete-file validation. Preserve existing generic search/update and standalone apply guard. No automatic repair, ontology inference, grammar adoption, MCP adapter or migration framework. Existing revisions increment once; Summary stays fixed. Output: four coherent R/M Atoms and before/after pins.

Use the shared minimum contract in the CA-P-1979 review. A worker owns only the listed files; root owns integration, commits and Task completion. Recheck source pins after normalization. No unrelated changes, Core entity-model edits, source migration, runtime activation or release work. Ask for a concrete unresolved decision below 90% confidence. Decompose before exceeding 15 minutes.

### Local execution receipt

Revised CA-R-863 v13→14 and CA-R-866 v12→13; added CA-M-370 and CA-M-371 v1 under declared TOOLS ownership. The four source pins and identity/role/section checks are in `.caprmedio_caprmedio/_projection/core-entity-review/stage2/task-1984.receipt.json`. Root verified exact original Summaries and single-step Version increments, and preserved generic update and apply guards. The packet defines valid-file operations, not a migration framework or unsupported MCP delivery. Full independent cross-role acceptance remains CA-P-1981; no feature code or Core source changed.

### Definition of Done

The Plan is **not** Done if its stated output or exact before/after evidence is missing; a file outside its exclusive scope changes; preserved claims or identity are lost; the cross-role contract conflicts; checks fail; a prerequisite is incomplete; or own work exceeds 15 minutes without decomposition.
