---
atom_id: CA-P-2308
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
  depends_on: [Configuration, Method, Evaluation, Delivery, Plan]
version: 2
updated_at: "2026-10-13 20:20:42 +0400"
relations:
  is_decomposition_of: [CA-P-2256]
---
# Summary

Preserve TOML text during pure edits

## Objective

After CA-P-2307 source acceptance and required affected FPF acceptance, implement the private pure TOML materializer with the approved dependency pin. Reuse existing semantic edit validation. Preserve unrelated bytes, types, comments and line endings; retain exact no-op bytes and refuse unsupported layout normalization. No file IO, new public representation or receiving authority.

## Details

Estimated own work: up to 15 minutes; split before exceeding that limit. Inherit CA-P-2256's accepted source and review gates. Root owns Plans and Git; workers own disjoint implementation and independent test files. No live configuration writes, installed activation, Core migration or Markdown/YAML dependency selection is authorized by this Task.

### Definition of Done

The bounded outcome has exact source/implementation pins, actual relevant checks and a different reviewer's acceptance. Preparation is not implementation; a Plan is not an executed FPF review. The parent and CA-P-2297 remain Active until their separate receiving/publication requirements pass.
