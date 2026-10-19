---
subjects:
  governs: "Entity/Node/Continuant/Projection/Type: Applicable Methodology.Member"
  depends_on:
    ["Entity/Node/Continuant/Projection/Type: Applicable Methodology.Member", "Entity/Node/Continuant/Atom", "Entity/Carrier/File Carrier"]
version: 16
updated_at: "2026-10-19 11:48:30 +0000"
relations: {}
atom_id: "CA-D-305@draft"
content_role: "Delivery"
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
local_tier: "Core"
status: "Draft"
author: "Anatoly Maslennikov"
global_tier: 9
---
# Summary

Carry Projected Atoms without New Identity

## Scope

Applicable Methodology projected Atom Carriers.

## Claim

**every** Applicable Methodology projected Atom Carrier **must** retain a one-way source binding **to** the selected authoritative Atom Revision **without** creating another Atom identity:

- preserve the source Atom's authored Frontmatter **and** Main Content unchanged; the **only** compiler-added block is the source binding below.
- store **`=1`** `projection.source_carrier_path` value **in** the projected Carrier's Frontmatter. resolve it relative **to** the projected Markdown file's directory **to** the original Atom Carrier **in** the selected Methodology Sources.
- retain the source Atom ID **and** Version; together with the source binding, they identify the selected source Revision. verify source fidelity under CA-E-379 rather than assuming that an existing path proves currentness.
- treat this block as Projection metadata, **not** an authored Atom Property **or** a new Atom-to-Atom Relation. do **not** copy it upstream **or** add inverse links **to** source Atoms.

**after** removing **only** the generated source-binding block, the projected Carrier bytes **must** equal the selected source Carrier bytes. missing, ambiguous, wrong-source, **or** stale bindings **must not** be accepted as current Applicable Methodology.

## Details
