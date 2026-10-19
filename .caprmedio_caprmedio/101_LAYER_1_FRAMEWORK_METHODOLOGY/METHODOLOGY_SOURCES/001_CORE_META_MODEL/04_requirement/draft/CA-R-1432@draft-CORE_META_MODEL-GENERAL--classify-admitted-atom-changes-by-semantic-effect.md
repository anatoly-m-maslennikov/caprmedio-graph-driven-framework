---
subjects:
  governs: "Atom Change Classification"
  depends_on:
    ["Entity/Node/Continuant/Atom", "Entity/Node/Continuant/Atom.Substance", "Entity/Node/Continuant/Atom.Summary", "Entity/Node/Continuant/History/Revision/Type: Atom", "Carrier-Only Recoding", "Lineage Impact Analysis", "Tool"]
version: 14
updated_at: "2026-10-19 11:39:54 +0000"
relations: {}
atom_id: "CA-R-1432@draft"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Draft"
author: "Anatoly Maslennikov"
global_tier: 10
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
