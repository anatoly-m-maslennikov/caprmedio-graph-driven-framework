---
atom_id: CA-P-1852
content_role: Plan
type: Plan
label: Task
work_sequence_number: 4
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
status: Active
author: Anatoly Maslennikov
version: 3
updated_at: "2026-10-10 18:08:27 +0400"
subjects:
  governs: "CAPRMEDIO Framework Instance"
  depends_on: [Project, Plan, AI Agent, Operator, Framework Instance Settings, Methodology Source, Atom, Status, Content Role, Framework Package, Carrier, Projection]
relations:
  is_decomposition_of: [CA-P-1848]
  blocks: [CA-P-1853, CA-P-1854]
---
# Summary

Export only active Methodology

## Objective

the AI Agent implements deterministic delivery of the selected active Methodology sources into root `101_FRAMEWORK_METHODOLOGY`.

## Details

1. Read only the Project Methodology unit after source migration; do not read the installed target as authority.
2. Select active Methodology-source atoms only: Core Meta-Model, selected extensions and Project Configuration. Exclude Project Engine, Plans and other atoms.
3. Replace product contents in root `101_FRAMEWORK_METHODOLOGY` from that exact selected source, retaining source identities. The product has no draft or archive role; protected support settings are preserved outside the source replacement.
4. Fail before effects for missing, stale, ambiguous or non-active selected sources. Supply only non-live preflight inputs until the Local full suite passes; then commit only the export step's owned changes.

### Definition of Done

the Plan is **not** Done **if** product content derives from an installed copy, inactive or non-Methodology atom, lacks source identity, or a malformed selection reaches the product path.
