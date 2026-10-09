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
version: 1
updated_at: "2026-10-09 15:41:25 +0400"
subjects:
  governs: "CAPRMEDIO Framework Instance"
  depends_on:
    - "Project"
    - "Plan"
    - "AI Agent"
    - "Operator"
    - "Framework Instance Settings"
    - "Methodology Source"
    - "Atom"
    - "Status"
    - "Content Role"
    - "Framework Package"
    - "Carrier"
    - "Projection"
relations:
  is_decomposition_of:
    - CA-P-1848
  blocks:
    - CA-P-1853
    - CA-P-1854
---
# Summary

Export **only** active Methodology

## Objective

the AI Agent implements deterministic delivery of the selected active Methodology sources into root `methodology/`.

## Details

- scope: the installation/release contribution of the CAPRMEDIO Framework Instance delivered by the caprmedio Project.
- input: the declared authoritative source Scope Units, installed-extension selection, Project configuration **and** current explicit Atom properties.
- output: **only** active source Atoms selected for Methodology delivery, **with** required non-Atom settings, defaults, schemas **and** support manifests admitted by the package contract. do **not** export inactive Atoms merely because a filename **or** folder looks current.
- replace the present full persisted-tree export contract. preserve source identity/provenance, deterministic inventories, counts/digests **and** all required source closure; keep authoritative archives/history at source, **not** as a second delivered authority.
- resolve dependencies on legacy Project Plan evidence **and** selected-route pins explicitly. supporting evidence is an identified immutable artifact, **not** fabricated history **or** an unrelated Project copied into the beta package.
- test active/inactive selection, configured extension revisions, non-Atom support, completeness, stale pins, unsafe paths, idempotent export **and** `.DS_Store` exclusion. real delivery is deferred to the gated local release.
- effort: own work for **=1** AI Agent **must** fit **<=15** minutes. **if** this Plan needs larger own work, decompose it **before** execution **and** preserve its Objective **and** acceptance.
- control: use applicable Operator input **and** inherited Framework Instance Settings for permission, confidence **and** retry gates. creation is planned work **only**, **not** permission to execute the local/public cycle immediately.

### Definition of Done

the Plan is **not** Done **if** inactive Atoms enter the export, required active/support inputs are omitted, source pins cannot be checked, output varies for identical inputs, **or** `.DS_Store` causes a failure.
