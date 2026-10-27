---
atom_id: CA-P-2320@5
content_role: Plan
type: Plan
label: Task
work_sequence_number: 1
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
status: Archived
subjects:
  governs: Tool
  depends_on:
  - Subject/Domain/Node/Continuant/Atom
  - Subject/Domain/Node/Continuant/Scope Unit
  - Configuration
  - Subject/Engineering/Workflow
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan'
version: 5
updated_at: 2026-10-24 08:22:45 +0400
relations:
  is_decomposition_of:
  - CA-P-2272
tier: 3
---
# Summary

Align canonical Settings filename

## Objective

The Settings carrier rules consistently name caprmedio_project_settings.toml.

## Details

Estimated own work: up to 15 minutes. Split further work before exceeding this bound. Inherit the parent's accepted source, independent review and execution gates. Root owns Plans and Git; assigned file ownership stays disjoint.

The Operator explicitly chose the existing caprmedio_project_settings.toml name. Align only D363/D364 conflicting filename clauses; preserve the selected owning Project control-root boundary, source identity and Summary. Exact predecessor archives and Version +1 are required. Independently verify unaffected dependent rules. No Settings file rename, fallback, projection rewrite or legacy Atom migration.

### Definition of Done

The Plan is **not** Done if its stated outcome lacks exact source/code/test evidence and independent verification; required checks fail; a deferred policy is inferred; existing safety checks are bypassed; or source-only/isolated evidence is represented as live runtime or migration acceptance.

### Accepted outcome

D363 v11 and D364 v10, with exact predecessor archives, passed independent source review. The affected FPF review completed under plan-c410a7a2-3cf9-4d12-9f25-24f0835e491b. The current receiving-rule-alignment-source-acceptance receipt records their exact hashes. No Settings carrier was renamed and no logical Settings revision evidence was fabricated. Boundary helper work can proceed independently of runtime admission.
