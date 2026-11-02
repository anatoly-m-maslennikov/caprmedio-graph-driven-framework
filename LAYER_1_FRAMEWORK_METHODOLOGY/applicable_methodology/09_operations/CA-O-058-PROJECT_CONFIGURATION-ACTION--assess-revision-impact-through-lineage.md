---
subjects:
  governs: "Assess Lineage Impact"
  depends_on:
    ["Entity/Node/Continuant/Atom/Content Role: Operations/Type: Action", "Entity/Node/Continuant/Atom", "Entity/Node/Continuant/History/Revision/Type: Atom", "Entity/Relation", "Lineage Impact Analysis", "Entity/Node/Continuant/Actor/Type: Operator", "Entity/Node/Continuant/Actor/Type: AI Agent"]
version: 10
updated_at: "2026-10-19 15:56:46 +0400"
relations: {"child_of":["CA-E-002"]}
atom_id: "CA-O-058"
content_role: "Operations"
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "Action"
global_tier: 11
projection:
  source_carrier_path: ../../sources/003_PROJECT_CONFIGURATION/09_operations/CA-O-058-PROJECT_CONFIGURATION-ACTION--assess-revision-impact-through-lineage.md
  source_atom_id: CA-O-058
  source_atom_revision: 10
  source_sha256: d1f5357fc73156d93124ead0610cdbdbc8fad3eee189e55d9155a015d96c2c30
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Assess revision impact through lineage

## Operation

Assess Lineage Impact **means** the reusable Action that assesses **every** reachable descendant lineage branch of **`=1`** changed Atom **until** **every** branch has an explicit impact disposition.

apply this Action **when** the Atom:

- receives a new accepted Revision;
- is replaced by a successor; **or**
- moves **to** the archive.

an Operator **or** AI Agent performs this Action within its existing authority. the assessment follows the existing lineage recursively; it does **not** create another cross-Scope Unit dependency graph.

## Details
