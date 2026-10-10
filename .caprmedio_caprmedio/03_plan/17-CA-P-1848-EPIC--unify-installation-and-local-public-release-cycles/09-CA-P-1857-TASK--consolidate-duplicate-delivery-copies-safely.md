---
atom_id: CA-P-1857
content_role: Plan
type: Plan
label: Task
work_sequence_number: 9
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
  depends_on: [Project, Plan, AI Agent, Operator, Framework Instance Settings, Framework Package, Methodology Source, Applicable Methodology, Atom, Carrier, Journal, Projection]
relations:
  is_decomposition_of: [CA-P-1848]
  blocks: [CA-P-1858]
---
# Summary

Consolidate duplicate delivery copies safely

## Objective

the AI Agent supplies a verified consolidation plan for redundant delivery/staging copies without losing source history **or** rollback evidence.

## Details

1. Treat root `101_FRAMEWORK_METHODOLOGY` as the current release product, not a duplicate candidate. The Project Methodology unit is source authority and `.caprmedio_caprmedio/000_CAPRMEDIO_framework` is installed current Methodology.
2. Examine only actual duplicate/staging candidates such as `.release-sources-*`, `_release_materialized`, package copies, nested control roots and empty legacy directories. Record path, role, identity, consumers and retention before any cleanup.
3. Preserve protected configuration/settings, authoring sources, selected/rollback evidence, current Run evidence and other Project resources. A Local release may only clear the product/installed contents explicitly owned by its ordered replacement stages.
4. Perform actual cleanup only after the Local command's complete suite and verification, with honest blocked/failure outcomes and no blanket prune.

### Definition of Done

the Plan is **not** Done **if** the product is misclassified as a duplicate, a candidate lacks consumer/identity/retention evidence, unique data or recovery evidence is lost, or cleanup affects unrelated Project resources.
