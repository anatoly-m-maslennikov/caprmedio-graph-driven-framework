---
subjects:
  governs: "Subject Projection Derivation"
  depends_on:
    ["Entity/Node/Continuant/Projection/Type: Atom Subjects Graph", "Entity/Node/Continuant/Atom.Subjects", "Subject Path", "Subject", "Subject Target", "Entity/Node/Continuant/Atom", "GOVERNS", "DEPENDS_ON"]
version: 16
updated_at: "2026-10-21 01:47:52 +0400"
relations: {}
atom_id: "CA-M-232"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/05_method/CA-M-232-CORE_META_MODEL-CORE--derive-atom-subjects-graph-from-current-atom-subjects.md
  source_atom_id: CA-M-232
  source_atom_revision: 16
  source_sha256: 9a3b1e59646b9e8835a17b51c91b79175ef2465404c6fb344e2c4b577694bdd1
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Derive Atom Subjects Graph from Current Atom Subjects

## Scope

Atom Subjects Graph derivation from current Atom Subjects.

## Claim

**to** derive an Atom Subjects Graph, the Generator **must** reproduce **every** selected Subject as a direct GOVERNS **or** DEPENDS_ON graph link from its source Atom **to** its target with its exact canonical Subject Target, Subject Path, **and** Relation Kind **without** adding authority, requiring a duplicate target-kind field **in** the Atom's Subjects, **or** creating a separately identified Subject object. a Projection **may** derive a target's kind from its canonical authority **when** the Projection's own Spec calls for that classification; it **must not** independently reauthor that kind **or** require it as duplicated source Subjects metadata. an Atom Subjects Graph may include Entity-root and Method-root Subject Targets. an Entities Graph view must include only Entity-root targets unless its own Spec explicitly admits a distinguishable external reference. an unmigrated temporal Carrier admitted temporarily by CA-D-269 retains its source classification as migration evidence **without** changing the direct reference **or** requiring that classification **in** the canonical flat representation.

## Details
