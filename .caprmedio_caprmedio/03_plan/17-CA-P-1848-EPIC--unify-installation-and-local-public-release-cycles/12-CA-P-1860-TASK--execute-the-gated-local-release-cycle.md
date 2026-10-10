---
atom_id: CA-P-1860
content_role: Plan
type: Plan
label: Task
work_sequence_number: 12
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
status: Active
author: Anatoly Maslennikov
version: 5
updated_at: "2026-10-10 18:58:38 +0400"
subjects:
  governs: "CAPRMEDIO Framework Instance"
  depends_on: [Project, Plan, AI Agent, Operator, Framework Instance Settings, Framework Package, Methodology Source, Applicable Methodology, Version, Tool, Workflow, Action, Workflow Run, Journal, Projection]
relations:
  is_decomposition_of: [CA-P-1848]
  blocks: [CA-P-1861]
---
# Summary

Execute the gated local release cycle

## Objective

the AI Agent executes the one programmatic Local release command, whose internal complete preflight passes before its first destructive product wipe.

## Details

1. Verify the corrected registry maps Methodology Sources to the Project Methodology unit and that `project_structure.toml` agrees before any wipe. The installed target remains read-only and is not authoring authority before its later replacement step.
2. Prepare active Core Meta-Model, selected extensions, Project Configuration, Engine/package candidate, image and non-live test inputs without changing product or installed contents. Run the complete Local suite before the first destructive product wipe.
3. On the preflight pass, clear product contents in root `101_FRAMEWORK_METHODOLOGY`; replace them from the selected active source; compile applicable Methodology; clear replaceable installed contents; and copy the product directory as-is to `.caprmedio_caprmedio/000_CAPRMEDIO_framework`. Do not repeat the full suite solely for this deterministic generated copy.
4. Preserve `caprmedio_framework_settings.toml`, authoritative configuration, Project Structure, Operator registry and support settings, while refreshing generated manifests/selectors. Commit each completed source/product/installed step separately and stage only its owned changes.
5. Migrate state, replace only the selected installed package, install the same sealed package into the selected Project runtime, install `ca`, then start/reuse its selected image and smoke the returned MCP endpoint.
6. Execute Local release as the concrete Project Operation in `.caprmedio_caprmedio/09_operations` with helper tools from `PROJECT_TOOLS`; reusable compiler/installer, shared package/gate models/codecs, detached readers and generic O200 install/bootstrap/restore capability remain in `TOOLS`. Plan required code relocation/exclusion without performing it here.
7. Record exact Run/Step/Action/Tool evidence and failures. Do not rebuild after the gate, replay uncertain effects, or expose stale success; this command creates no extra Operator command.

### Definition of Done

the Plan is **not** Done **if** an authoring source is wiped, product/install ordering or protected-settings preservation fails, a step commits unrelated changes, Local release/helper delivery is not Project-owned, reusable generic capability leaves `TOOLS`, the promotion differs from gated bytes, or runtime/image/MCP evidence is incomplete.
