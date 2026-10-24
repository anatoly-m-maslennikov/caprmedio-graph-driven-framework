---
atom_id: CA-P-2307
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
  depends_on: [Configuration, Method, Evaluation, Delivery, Plan]
version: 2
updated_at: "2026-10-13 16:35:00 +0400"
relations:
  is_decomposition_of: [CA-P-2256]
---
# Summary

Select TOMLKit for preserving configuration text

## Objective

Author and independently check the bounded selecting Method, Delivery and Evaluation for TOMLKit. Bind the Operator approval, exact package selection, capability, carrier/interface, boundary cost and evidence. Prepare any required affected FPF review Plan; do not infer its execution from dependency approval.

## Details

Estimated own work: up to 15 minutes; split before exceeding that limit. Inherit CA-P-2256's accepted source and review gates. Root owns Plans and Git; workers own disjoint implementation and independent test files. No live configuration writes, installed activation, Core migration or Markdown/YAML dependency selection is authorized by this Task.

### Review and bounded continuation

The approved affected FPF design challenge completed with independent validation under Plan `plan-48ac5070-505b-4d6f-8e2a-6f4e958084ba`. It found no new design correction in M383/D632/E635. Final result SHA-256: `4e6c0ab8c7aab1611ff2e5a598811309f99496fec5ecc76f5256d03efb16a9b3`. This records the completed conversational review, not a saved report or implementation acceptance. G002 (complete source admission) and G003 (implementation evidence) remain open.

The Operator approved fixing the two existing validator gaps first. Continue through:

- [CA-P-2311 — Filter proposed reference validation to selected identities](02-CA-P-2307-TASK--select-tomlkit-for-preserving-configuration-text/done/01-CA-P-2311-TASK--filter-proposed-reference-validation-to-selected-identities.md)
- [CA-P-2312 — Resolve implicit Project context in proposed carriers](02-CA-P-2307-TASK--select-tomlkit-for-preserving-configuration-text/done/02-CA-P-2312-TASK--resolve-implicit-project-context-in-proposed-carriers.md)
- [CA-P-2313 — Verify proposed carrier admission regressions](02-CA-P-2307-TASK--select-tomlkit-for-preserving-configuration-text/done/03-CA-P-2313-TASK--verify-proposed-carrier-admission-regressions.md)

Keep PyYAML with targeted Markdown/frontmatter text edits, as the Operator confirmed. No additional Markdown/YAML dependency or formatting-normalization policy is selected.

The three bounded validator Tasks are Done after independent review. Full admission remains blocked by a non-Atom evidence document in the Plan reference frontier; requested legacy-source metadata remains unresolved. See `.caprmedio_caprmedio/_projection/core-entity-review/stage2/tools-first/proposed-carrier-admission-review.md`. This parent stays Active; no TOMLKit implementation or live publication follows automatically.

### Definition of Done

The bounded outcome has exact source/implementation pins, actual relevant checks and a different reviewer's acceptance. Preparation is not implementation; a Plan is not an executed FPF review. The parent and CA-P-2297 remain Active until their separate receiving/publication requirements pass.
