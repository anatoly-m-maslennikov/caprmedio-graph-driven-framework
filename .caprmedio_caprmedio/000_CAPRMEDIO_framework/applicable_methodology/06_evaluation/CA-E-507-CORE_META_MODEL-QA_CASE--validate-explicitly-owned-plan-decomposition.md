---
subjects:
  governs: "Atom/Content Role: Plan/Type: Plan"
  depends_on:
    ["Atom/Content Role: Plan/Type: Plan", "Entity/Carrier/Directory Carrier", "Entity/Carrier/File Carrier", "Entity/Node/Continuant/Atom.ID", "Plan Graph"]
version: 7
updated_at: "2026-10-19 15:55:15 +0400"
relations: {"evaluation_for": ["CA-R-1579", "CA-R-1534", "CA-R-1536", "CA-R-1537", "CA-R-1538", "CA-D-481", "CA-D-460", "CA-D-461"]}
atom_id: "CA-E-507"
content_role: "Evaluation"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "QA Case"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/06_evaluation/CA-E-507-CORE_META_MODEL-QA_CASE--validate-explicitly-owned-plan-decomposition.md
  source_atom_id: CA-E-507
  source_atom_revision: 7
  source_sha256: 1bf6be28dc20a3fa85dbd510915d8b1470eb0e450e88bbcd58506e1b69689af5
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Validate explicitly owned Plan decomposition

## Scope

Plan decomposition declarations and their derived representations.

## Claim

the decomposition Evaluation **must** reproduce **only** the Plan Relations declared under CA-D-481-CORE_META_MODEL-DELIVERY--store-plan-decomposition-on-the-decomposing-plan.

- declare `B IS_DECOMPOSITION_OF A` on `B` **and** `C IS_DECOMPOSITION_OF B` on `C`; derive their exact `DECOMPOSES_INTO` inverses **and** derive `A` reaching `C` **only** **in** the recursive view.
- retain the same graph with **all** three Markdown files directly **in** `03_plan`, with matching optional Hub folders, **and** across valid Status placements. the declarations, **not** adjacency, determine the graph.
- count matching same-identity file **and** folder Carriers once, **without** a self-edge.
- change **only** Labels **or** navigation numbers: retain identities **and** Relation meanings.
- reject a cycle, self-edge, non-Plan **or** unresolved endpoint, **`>1`** immediate decomposition targets, authored inverse list, duplicate declaration, transitive edge invented by closure, **or** a missing mandatory Markdown file.
- reject nesting a Plan inside another Plan's directory **when** its carried decomposition target is absent **or** different; do **not** silently derive **or** repair the edge from that nesting.
- preserve every related Atom's independent Claim, Revision, Status, **and** owning Scope Unit.

## Details

report exact expected **and** observed endpoints **without** silently changing declarations **or** placement.
