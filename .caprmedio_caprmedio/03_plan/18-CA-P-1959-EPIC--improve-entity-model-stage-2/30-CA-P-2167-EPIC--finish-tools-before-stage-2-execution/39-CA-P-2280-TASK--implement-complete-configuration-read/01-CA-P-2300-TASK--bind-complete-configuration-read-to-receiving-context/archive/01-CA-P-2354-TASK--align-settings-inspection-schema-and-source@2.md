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
  depends_on: [Atom, Configuration, Plan]
version: 2
updated_at: "2026-10-13 22:57:09 +0400"
relations:
  is_decomposition_of: [CA-P-2300]
---
# Summary

Align ordinary Settings reader schema and source

## Objective

Align only the complete Project Settings schema and narrow source description used by an ordinary standalone file reader that reads, parses and validates the supplied file.

## Details

Own only the necessary ordinary-reader schema/source alignment and pins. Inspect selected authority before amendments and preserve unrelated policy and existing schema constraints. The reader validates admitted fields and reports missing required fields, unknown fields and invalid supplied types accurately. It does not repair content or migrate existing Settings/callers. Remove the superseded inspection/history/currentness model from this reader's contract: no Journal scan, history/currentness output or gate. Coordinate the accepted schema with CA-P-2355.

Estimated own work: up to 15 minutes. Split before exceeding this bound. Root owns Plans and Git. Parallel workers own disjoint files; preserve unrelated changes. This Task does not authorize changes to existing Settings documents, existing callers, Journal or runtime. Keep Active until final integration.

### Definition of Done

Exact schema/source paths, Versions and digests plus focused valid/invalid schema cases establish this ordinary reader contract. Independent review confirms that no Journal lookup, history/currentness result or admission gate is required and existing schema constraints remain intact. This work does not change existing Settings/callers or Journal/runtime; preserve unrelated pre-existing edits. Broader receiving, parent-wide and runtime completion remain separate.
