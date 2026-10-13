---
atom_id: CA-P-2354
content_role: Plan
type: Plan
label: Task
work_sequence_number: 1
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: Tool
  depends_on: [Atom, Configuration, Workflow, Journal, Plan]
version: 1
updated_at: "2026-10-13 22:24:17 +0400"
relations:
  is_decomposition_of: [CA-P-2300]
---
# Summary

Align Settings inspection schema and source

## Objective

Define the complete Project Settings schema and the narrow source bindings consumed by the new standalone inspection reader. Preserve the Operator-approved distinction between schema-valid Read with unknown history and admission for operations requiring verified history.

## Details

Own only the new inspection schema and its necessary source alignment/pins. Inspect the selected authority before amendments and keep unrelated policy unchanged. Accept the complete document according to the explicit admitted schema; reject missing, unknown or wrong-typed fields rather than repair, select defaults or trim the document. Do not migrate existing Settings, existing callers, Journal or runtime. Coordinate the accepted schema/source contract with CA-P-2355.

Estimated own work: up to 15 minutes. Split before exceeding this bound. Root owns Plans and Git. Parallel workers own disjoint files; preserve unrelated changes. This Task does not authorize changes to existing Settings documents, existing callers, Journal or runtime.

### Definition of Done

Exact schema/source paths, Versions and digests plus focused valid/invalid whole-document cases establish complete coverage. An unknown-history but schema-valid inspection document is admissible for Read; the result must not satisfy a verified-history operation gate. Scope and independent review must establish that this work does not change existing Settings/callers or Journal/runtime, preserving unrelated pre-existing edits. Parent-wide and runtime completion remain separate.
