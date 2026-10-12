---
atom_id: CA-P-1851
content_role: Plan
type: Plan
label: Task
work_sequence_number: 3
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
status: Active
author: Anatoly Maslennikov
version: 3
updated_at: "2026-10-11 23:48:54 +0000"
subjects:
  governs: "CAPRMEDIO Framework Instance"
  depends_on: [Project, Plan, AI Agent, Operator, Framework Instance Settings, Methodology Source, Applicable Methodology, Scope Unit, Project Structure, Atom, Projection, Carrier]
relations:
  is_decomposition_of: [CA-P-1848]
  blocks: [CA-P-1852]
---
# Summary

Consolidate Methodology source **and** delivery paths

## Objective

Use the declared source, product and installed Methodology folders without compatibility migration.

## Details

- Follow CA-P-1848's current direct happy path. Earlier snapshot, admission, selector, recovery and complete-corpus gate requirements are superseded.
- Commit everything before every release step and at the end, respecting Git ignore rules and secret exclusions.
- Stop and report a failed step for manual handling; no automatic rollback or retry.
- Preserve configuration, Project records and other Projects. Ignore .DS_Store.

## Definition of Done

The Objective is implemented and verified with actual evidence appropriate to this task. Record remaining manual issues. Mock tests do not prove live release, installation, MCP or PR completion.
