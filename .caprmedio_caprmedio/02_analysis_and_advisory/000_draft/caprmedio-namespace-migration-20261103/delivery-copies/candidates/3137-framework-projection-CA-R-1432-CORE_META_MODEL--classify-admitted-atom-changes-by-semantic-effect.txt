---
subjects:
  active: CAPRMEDIO <+ MODEL <+ Atom
  passive:
  - CAPRMEDIO <+ MODEL <+ Atom
  - CAPRMEDIO <+ MODEL <+ Atom.Content.Summary
  - CAPRMEDIO <+ MODEL <+ Carrier
  - CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Atom/Content Role
version: 27
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-R-1432
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 2
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1432-CORE_META_MODEL--classify-admitted-atom-changes-by-semantic-effect.md
  source_atom_id: CA-R-1432
  source_atom_revision: 27
  source_sha256: 48daca5dfaa73fe26f86c8c035ec1a46ee272a57c579e7c80f9e15ec92325a5e
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Classify admitted Atom changes by semantic effect

## Claim scope

the classification of admitted Atom changes by semantic effect.

## Claim

**before** changing an admitted Atom, CAPRMEDIO **must** assign **`=1`** change class using these boundaries, identity results, **and** required reviews:

| Change class | Boundary | Identity result | Required review |
|---|---|---|---|
| `carrier_only` | Representation, the Atom's own filename **or** local placement, encoding, **or** lossless Entity-name/reference renaming **without** changing governed meaning **or** the Atom's Summary value **or** Content Role | Keep the Atom ID; increment Version by exactly **`1`** | Verify lossless recoding |
| `refinement` | Wording **or** criteria become clearer **or** stricter while content, applicability, **and** acceptance meaning remain equivalent **and** Summary **and** Content Role remain unchanged | Keep the Atom ID; increment Version by exactly **`1`** | Demonstrate equivalence |
| `semantic_revision` | Meaning **or** applicability changes while Summary **and** Content Role remain unchanged | Keep the Atom ID; increment Version by exactly **`1`** | Declare the delta **and** complete lineage-impact review |
| `replacement` | the Summary value changes under CA-R-1464 **or** Content Role changes | Create a new Atom ID; preserve the predecessor **and** successor identity binding under CA-R-807 | Review the replacement boundary **and** affected lineage |

For an existing Atom, only a Summary **or** Content Role change creates a new base Atom ID. Content Role changes always create a new Atom, even with unchanged Summary. Claim, other Content, Type, Status, applicability **or** other property changes alone retain the base ID when Summary **and** Content Role stay unchanged. Scope narrowing **or** expansion is a `semantic_revision`, **not** carrier-only. Adding a separately authored Atom gives that new Atom its own ID; it does not itself replace an existing Atom whose Summary **and** Content Role remain unchanged. Lossless serialization of the same Summary value is **not** a Summary change. the semantic change class is independent of storage transactions **or** version-control change sets; persistence preserves the admitted Atom, Carrier, **and** Journal authority.

**every** actual same-ID update **must** increment Version by exactly **`1`**, regardless of change class, **and** refresh Updated At under CA-R-1788. an exact no-op **must** retain Version **and** Updated At. When a predecessor is archived, its Archive Carrier **must** carry `status: Archived`, identify that predecessor as `<canonical-ID>@<old-version>`, and preserve its numeric Version, prior Updated At, and unrelated content. The Current successor retains the canonical ID, advances Version by exactly **`1`**, and receives the actual Project-time edit instant. Git history preserves the exact pre-archive Carrier bytes; the archive conversion does not require an exact-byte copy.

this classification concerns changes **to** the Atom's own bytes, metadata, direct ownership **or** local placement. moving an ancestor **only** changes a descendant's repository locator **when** that descendant's own bytes, metadata, direct owner **and** placement relative **to** that owner remain unchanged; this is **not** an Atom update **and** **must** retain that descendant's Version **and** Updated At. this boundary applies **to** **all** Atoms, including Plans nested under a moved Plan **and** Atoms whose owning Scope Unit moves. an actual change **to** the Atom itself, including its Status, filename, direct owner **or** local placement, still follows the classification **and** revision rules above. Exact pre-change bytes remain available through Git history.

Tools **may** propose a class but **must** fail closed **when** the distinction between refinement, semantic revision, **and** replacement is uncertain.
