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
    - "Framework Package"
    - "Methodology Source"
    - "Applicable Methodology"
    - "Atom"
    - "Carrier"
    - "Journal"
    - "Projection"
relations:
  is_decomposition_of:
    - CA-P-1848
  blocks:
    - CA-P-1858
---
# Summary

Consolidate duplicate delivery copies safely

## Objective

the AI Agent supplies a verified consolidation plan for redundant delivery/staging copies without losing source history **or** rollback evidence.

## Details

- scope: the installation/release contribution of the CAPRMEDIO Framework Instance delivered by the caprmedio Project.
- input: root `101_LAYER_1_FRAMEWORK_METHODOLOGY`, `.release-sources-*` staging trees, `_release_materialized` snapshots, Tool/full-Engine package copies, nested repeated control roots **and** empty legacy root directories.
- separate byte-identical copies, differing/stale payloads, intentional immutable releases **and** referenced recovery evidence. record path, role, content identity, consumers **and** retention/disposition for each candidate.
- account for the accidental nested duplicate CA-D-388 carrier, stale runtime O128/O164/O169/O179/settings copies, missing CA-O-187 delivery, repeated materialized payload groups **and** tracked `.gitkeep`-only legacy roots.
- update consumers before retiring an old boundary. preserve non-identical valuable data, source archives, active/previous selected packages, current Run evidence, protected contents **and** another Project's resources.
- prepare/test bounded consolidation **and** rollback; perform actual removal **only** as the admitted cleanup after successful local cutover/verification. required retention choices are explicit, **not** a blanket prune.
- effort: own work for **=1** AI Agent **must** fit **<=15** minutes. **if** this Plan needs larger own work, decompose it **before** execution **and** preserve its Objective **and** acceptance.
- control: use applicable Operator input **and** inherited Framework Instance Settings for permission, confidence **and** retry gates. creation is planned work **only**, **not** permission to execute the local/public cycle immediately.

### Definition of Done

the Plan is **not** Done **if** a duplicate candidate lacks consumer/identity/retention evidence, unique data would be lost, a required recovery snapshot is removed, **or** cleanup changes unrelated Project resources.
