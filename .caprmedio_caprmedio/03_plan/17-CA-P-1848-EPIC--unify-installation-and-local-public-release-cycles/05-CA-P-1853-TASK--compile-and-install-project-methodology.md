---
atom_id: CA-P-1853
content_role: Plan
type: Plan
label: Task
work_sequence_number: 5
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
  depends_on: [Project, Plan, AI Agent, Operator, Framework Instance Settings, Applicable Methodology, Methodology Source, Projection, Atom, Project Settings, Workflow, Evaluation]
relations:
  is_decomposition_of: [CA-P-1848]
  blocks: [CA-P-1855]
---
# Summary

Compile **and** install Project Methodology

## Objective

the AI Agent compiles the applicable product Methodology and installs it as the selected Project's current Methodology.

## Details

1. Prepare compilation inputs non-live and use the Local full preflight before the product wipe. After its pass, compile applicable Methodology in root `101_FRAMEWORK_METHODOLOGY` from its selected active-source product contents without repeating the suite solely for the deterministic copy.
2. After compilation, clear only replaceable installed Methodology contents and copy the product directory as-is to `.caprmedio_caprmedio/000_CAPRMEDIO_framework`.
3. Preserve `caprmedio_framework_settings.toml`, authoritative configuration, Project Structure, Operator registry and support settings; generated manifests and selectors refresh.
4. Verify source/product/installed identity and commit only the compilation-and-installed-copy step. Do not create a separate Operator command.

### Definition of Done

the Plan is **not** Done **if** compilation changes source authority, installed Methodology differs from the product copy without an allowed exception, protected settings are replaced, or identity/provenance is missing.
