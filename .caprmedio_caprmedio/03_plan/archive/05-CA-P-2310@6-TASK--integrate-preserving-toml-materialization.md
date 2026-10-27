---
atom_id: CA-P-2310@6
content_role: Plan
type: Plan
label: Task
work_sequence_number: 5
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
status: Archived
subjects:
  governs: Subject/Engineering/Tool
  depends_on:
  - Configuration
  - Method
  - Evaluation
  - Delivery
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan'
version: 6
updated_at: 2026-10-24 07:52:46 +0400
relations:
  is_decomposition_of:
  - CA-P-2256
tier: 3
---
# Summary

Integrate preserving TOML materialization

## Objective

After accepted sources and pure implementation, bind the materializer to the existing private writer and canonical scoped dependency group/lock. Keep current receiving validation, stale-source, permission and observed-effect checks. Run focused regressions and independent review; document only local capability, not admitted receiver/runtime readiness.

## Details

Estimated own work: up to 15 minutes; split before exceeding that limit. Inherit CA-P-2256's accepted source and review gates. Root owns Plans and Git; workers own disjoint implementation and independent test files. No live configuration writes, installed activation, Core migration or Markdown/YAML dependency selection is authorized by this Task.

### Definition of Done

The bounded outcome has exact source/implementation pins, actual relevant checks and a different reviewer's acceptance. Preparation is not implementation; a Plan is not an executed FPF review. The parent and CA-P-2297 remain Active until their separate receiving/publication requirements pass.

### Acceptance — 2026-10-13

The existing private connector writer now uses the accepted preserving materializer. Independent review passed at exact final pins; the full TOML suite passed 60 tests, including 11 independent integration tests and 6 author tests. Original schema, authority, stale-source, observed-effect and readback behavior remains intact. Literal-byte/no-op and failure-after-effect checks passed. See `.caprmedio_caprmedio/_projection/core-entity-review/stage2/tools-first/toml-writer-integration-acceptance.md`. This completes private integration only, not P2297 receiving schemas or public/runtime admission.
