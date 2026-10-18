---
subjects:
  governs: "Atom Change Classification"
  depends_on:
    ["Entity/Continuant/Object/Atom", "Entity/Continuant/Object/Atom.Substance", "Entity/Continuant/Object/Atom.Summary", "Entity/Continuant/History/Revision/Type: Atom", "Carrier-Only Recoding", "Lineage Impact Analysis", "Tool"]
version: 13
updated_at: "2026-10-15 18:42:57 +0000"
relations: {}
atom_id: "CA-R-1432"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1432-CORE_META_MODEL-GENERAL--classify-admitted-atom-changes-by-semantic-effect.md
  source_atom_id: CA-R-1432
  source_atom_revision: 13
  source_sha256: 38b23ac489e3e66b05a3b587f334c6581846cce7ee4037c512baab7ad59f14e7
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Classify admitted Atom changes by semantic effect

## Scope

the classification of admitted Atom changes by semantic effect.

## Claim

**before** changing an admitted Atom, CAPRMEDIO **must** assign **`=1`** change class using these boundaries, identity results, **and** required reviews:

| Change class | Boundary | Identity result | Required review |
|---|---|---|---|
| `carrier_only` | Representation, the Atom's own filename **or** local placement, encoding, **or** lossless Entity-name/reference renaming **without** changing governed meaning **or** the Atom's Summary value | Keep the Atom ID; increment Version by exactly **`1`** | Verify lossless recoding |
| `refinement` | Wording **or** criteria become clearer **or** stricter while primary Claim, applicability, **and** acceptance meaning remain equivalent **and** the Summary value remains unchanged | Keep the Atom ID; increment Version by exactly **`1`** | Demonstrate equivalence |
| `semantic_revision` | Meaning **or** applicability changes while the same primary Claim remains recognizable **and** the Summary value remains unchanged | Keep the Atom ID; increment Version by exactly **`1`** **and** create a new Revision | Declare the delta **and** complete lineage-impact review |
| `replacement` | the Summary value changes under CA-R-1464, the primary Claim changes identity, **or** an independently replaceable Claim is added **or** removed | Create a new Atom ID; preserve the predecessor **and** successor identity binding under CA-R-807 | Review the replacement boundary **and** affected lineage |

**if** Scope narrowing **or** expansion preserves the primary Claim identity **and** Summary value, **then** it is a `semantic_revision`, **not** a carrier-only change. splitting **or** combining independently replaceable Claims is a `replacement`. the Summary-change replacement rule takes precedence even **when** the Claim remains unchanged; lossless serialization of the same Summary value is **not** a Summary change. the semantic change class is independent of storage transactions **or** version-control change sets; persistence preserves the admitted Atom, Carrier, **and** Journal authority.

**every** actual same-ID update **must** increment Version by exactly **`1`**, regardless of change class, **and** refresh Updated At under CA-R-1788. an exact no-op **must** retain Version **and** Updated At. retaining the predecessor as history **must** preserve its exact prior bytes, including its prior Version, Status **and** Updated At; retaining history is **not** another edit to that predecessor.

this classification concerns changes **to** the Atom's own bytes, metadata, direct ownership **or** local placement. moving an ancestor **only** changes a descendant's repository locator **when** that descendant's own bytes, metadata, direct owner **and** placement relative **to** that owner remain unchanged; this is **not** an Atom update **and** **must** retain that descendant's Version **and** Updated At. this boundary applies **to** **all** Atoms, including Plans nested under a moved Plan **and** Atoms whose owning Scope Unit moves. an actual change **to** the Atom itself, including its Status, filename, direct owner **or** local placement, still follows the classification **and** revision rules above. exact older Revision bytes remain unchanged.

Tools **may** propose a class but **must** fail closed **when** the distinction between refinement, semantic revision, **and** replacement is uncertain.

## Details
