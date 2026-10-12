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
status: Archived
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-10 18:08:27 +0400"
subjects:
  governs: "CAPRMEDIO Framework Instance"
  depends_on:
    - "Project"
    - "Plan"
    - "AI Agent"
    - "Operator"
    - "Framework Instance Settings"
    - "Methodology Source"
    - "Applicable Methodology"
    - "Scope Unit"
    - "Project Structure"
    - "Atom"
    - "Projection"
    - "Carrier"
relations:
  is_decomposition_of:
    - CA-P-1848
  blocks:
    - CA-P-1852
---
# Summary

Consolidate Methodology source **and** delivery paths

## Objective

the AI Agent establishes a source-preserving path migration that separates authoritative Methodology Atoms **from** delivered **and** installed Methodology.

## Details

- scope: the installation/release contribution of the CAPRMEDIO Framework Instance delivered by the caprmedio Project.
- input: authoritative sources currently under `.caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources`, Project Structure, root `101_LAYER_1_FRAMEWORK_METHODOLOGY` **and** its consumers.
- output: declare authoritative source Scope Unit paths **in** `project_structure.toml` **and** place authoring sources **in** their Project-owned Methodology Units, separate **from** the installed Framework Instance target. root `methodology/` becomes the derived delivery boundary.
- update compiler, retrieval, release, package, restore, discovery, tests **and** documentation references, including obsolete standalone `.caprmedio_framework` paths. retain original Atom identities **and** source traceability; path-only changes **must not** become new semantic revisions.
- prepare an inventoried, reversible migration **and** tests. actual source/path cutover occurs **after** the local release gate; the executing N Methodology remains usable while N+1 is prepared.
- root `101_LAYER_1_FRAMEWORK_METHODOLOGY` is an existing documented release copy, **not** another authoring authority. consolidate its delivery role into `methodology/` **after** consumers move; preserve its unique payload until compared **and** accounted for.
- effort: own work for **=1** AI Agent **must** fit **<=15** minutes. **if** this Plan needs larger own work, decompose it **before** execution **and** preserve its Objective **and** acceptance.
- control: use applicable Operator input **and** inherited Framework Instance Settings for permission, confidence **and** retry gates. creation is planned work **only**, **not** permission to execute the local/public cycle immediately.

### Definition of Done

the Plan is **not** Done **if** installed Methodology overwrites authoring authority, an Atom loses provenance, an old-path consumer remains unaccounted for, **or** the path cutover lacks recovery evidence.
