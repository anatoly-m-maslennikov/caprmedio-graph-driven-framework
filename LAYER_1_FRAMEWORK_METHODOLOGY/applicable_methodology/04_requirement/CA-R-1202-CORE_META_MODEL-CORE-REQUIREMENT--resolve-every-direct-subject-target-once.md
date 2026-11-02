---
subjects:
  governs: "Entity/Node/Continuant/Atom.Subjects"
  depends_on:
    - "GOVERNS"
    - "DEPENDS_ON"
    - "Subject Target"
version: 18
updated_at: "2026-10-21 01:47:52 +0400"
relations: {}
atom_id: "CA-R-1202"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1202-CORE_META_MODEL-CORE-REQUIREMENT--resolve-every-direct-subject-target-once.md
  source_atom_id: CA-R-1202
  source_atom_revision: 18
  source_sha256: bd72f7c1ceea726333dc58fa2d38bce5d73546498f200a77625700aaf1e2c09b
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Resolve Every Direct Subject Target Once

## Scope

direct GOVERNS and DEPENDS_ON values in an Atom's Subjects Property.

## Claim

**every** direct GOVERNS value **and** **every** direct DEPENDS_ON value **in** an Atom's Subjects Property **must** resolve **to** **`=1`** canonical Subject Target. resolution **must not** require an intermediate Subject/Entity **or** Subject/Reference Property **or** a repeated target-kind field.

## Details
