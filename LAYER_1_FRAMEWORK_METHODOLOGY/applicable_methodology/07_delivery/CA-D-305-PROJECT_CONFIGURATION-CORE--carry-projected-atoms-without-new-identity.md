---
subjects:
  governs: "Entity/Node/Continuant/Projection/Type: Applicable Methodology.Member"
  depends_on:
    ["Entity/Node/Continuant/Projection/Type: Applicable Methodology.Member", "Entity/Node/Continuant/Atom", "Entity/Carrier/File Carrier"]
version: 16
updated_at: "2026-10-19 15:56:19 +0400"
relations: {}
atom_id: "CA-D-305"
content_role: "Delivery"
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../sources/003_PROJECT_CONFIGURATION/07_delivery/CA-D-305-PROJECT_CONFIGURATION-CORE--carry-projected-atoms-without-new-identity.md
  source_atom_id: CA-D-305
  source_atom_revision: 16
  source_sha256: 7b1c4f96426e7907c90e5a949b037f26f39458fd769ed04e2b451a16376cdd39
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
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
