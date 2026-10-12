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
version: 2
updated_at: "2026-10-10 18:08:27 +0400"
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

the AI Agent establishes a source-preserving path migration that separates authoritative Methodology Atoms **from** the product and installed Methodology.

## Details

1. Verify the corrected registrations point authoring Methodology Sources to the Project Methodology unit and that `project_structure.toml` agrees before any installed-target wipe. The installed target remains read-only and is not source authority until Local release copies the product into it.
2. Limit the replacement source to active Methodology-source atoms: Core Meta-Model, selected extensions and Project Configuration. Exclude Project Engine, Plans and other Project atoms.
3. Make root `101_FRAMEWORK_METHODOLOGY` the product boundary, not a draft, archive or authoring authority. Prepare the selected active source as non-live test input and pass the Local full preflight before it is cleared and replaced, then compile applicable Methodology.
4. Treat `.caprmedio_caprmedio/000_CAPRMEDIO_framework` as the installed current Methodology. After product compilation, clear only replaceable installed contents and copy the product directory as-is while preserving `caprmedio_framework_settings.toml`, authoritative configuration, Project Structure, Operator registry and support settings.
5. Commit each source, product and installed step separately, staging only its owned changes. Do not perform this migration by authoring the Plan.

### Definition of Done

the Plan is **not** Done **if** a stale source registration remains, the active source set includes non-Methodology atoms, product or installed paths have an ambiguous role, protected settings are replaced, or a transition lacks its scoped commit boundary.
