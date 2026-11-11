---
subjects:
  active: CAPRMEDIO <+ MODEL <+ Projection/(.Form := Applicable Methodology)
  passive:
  - CAPRMEDIO <+ MODEL <+ Atom
  - CAPRMEDIO <+ MODEL <+ Carrier/File
version: 32
updated_at: 2026-11-02 08:06:47 +0400
relations: {}
atom_id: CA-D-305
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
tier: 1
role: Delivery
form: Decision
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/07_delivery/CA-D-305-PROJECT_CONFIGURATION-DECISION--carry-projected-atoms-without-new-identity.md
  source_atom_id: CA-D-305
  source_atom_revision: 32
  source_sha256: 6cb5c5748a2a2b42cbddc32db2cc514ee26cbc096a84a97fd913eacb318d9ca2
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Carry Projected Atoms without New Identity

## Claim scope

The source binding and representation of each Atom Carrier projected as an Applicable Methodology member.

## Claim

Applicable Methodology **must** represent each projected Atom Carrier with a one-way source binding **to** its selected authoritative Atom Revision **without** creating another Atom identity:

- preserve the source Atom's authored Frontmatter **and** Main Content unchanged; the **only** compiler-added block is the source binding below.
- store **`=1`** `projection.source_carrier_path` value **in** the projected Carrier's Frontmatter. resolve it relative **to** the projected Markdown file's directory **to** the original Atom Carrier **in** the selected Methodology Sources.
- retain the source Atom ID **and** Version; together with the source binding, they identify the selected source Revision. verify source fidelity under CA-E-379 rather than assuming that an existing path proves currentness.
- treat this block as Projection metadata, **not** an authored Atom Property **or** a new Atom-to-Atom Relation. do **not** copy it upstream **or** add inverse links **to** source Atoms.

**after** removing **only** the generated source-binding block, the projected Carrier bytes **must** equal the selected source Carrier bytes. missing, ambiguous, wrong-source, **or** stale bindings **must not** be accepted as current Applicable Methodology.
