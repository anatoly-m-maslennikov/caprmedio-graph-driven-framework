---
atom_id: CA-P-2320
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
  depends_on: [Atom, Scope Unit, Configuration, Workflow, Plan]
version: 1
updated_at: "2026-10-13 19:01:00 +0400"
relations:
  is_decomposition_of: [CA-P-2272]
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
