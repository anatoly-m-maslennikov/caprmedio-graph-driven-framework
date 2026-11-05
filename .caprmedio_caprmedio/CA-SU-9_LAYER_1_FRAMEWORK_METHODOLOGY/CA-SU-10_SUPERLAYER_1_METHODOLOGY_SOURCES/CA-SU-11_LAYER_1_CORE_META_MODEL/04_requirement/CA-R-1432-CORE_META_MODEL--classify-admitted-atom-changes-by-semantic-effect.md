---
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom
  - CAPRMEDIO_MODEL <+ Atom.Content.Summary
  - CAPRMEDIO_MODEL <+ Carrier
  - CAPRMEDIO_MODEL <+ Atom.Header.Role
version: 30
updated_at: 2026-11-04 18:34:50 +0400
atom_id: CA-R-1432
ref_id: CA-R-1432
status: Active
tier: 2
role: Requirement
form: Rule
carrier_destination:
  file:
    name: CA-R-1432-RULE--classify-admitted-atom-changes-by-semantic-effect.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
container:
  scope_unit: CA-SU-11
---
## Summary

Classify admitted Atom changes by semantic effect

## Claim

### Prose Claim


the classification of admitted Atom changes by semantic effect.


**before** changing an admitted Atom, CAPRMEDIO **must** assign **`=1`** change class using these boundaries, identity results, **and** required reviews:

| Change class | Boundary | Identity result | Required review |
|---|---|---|---|
| `carrier_only` | Representation, the Atom's own filename **or** local placement, encoding, **or** lossless Entity-name/reference renaming **without** changing governed meaning **or** the Atom's Summary value **or** Content Role | Keep the Atom ID; assign a unique successor Version greater than the predecessor Version | Verify lossless recoding |
| `refinement` | Wording **or** criteria become clearer **or** stricter while content, applicability, **and** acceptance meaning remain equivalent **and** Summary **and** Content Role remain unchanged | Keep the Atom ID; assign a unique successor Version greater than the predecessor Version | Demonstrate equivalence |
| `semantic_revision` | Meaning **or** applicability changes while Summary **and** Content Role remain unchanged | Keep the Atom ID; assign a unique successor Version greater than the predecessor Version | Declare the delta **and** complete lineage-impact review |
| `replacement` | the Summary value changes under CA-R-1464 **or** Content Role changes | Create a new Atom ID; preserve the predecessor **and** successor identity binding under CA-R-807 | Review the replacement boundary **and** affected lineage |

For an existing Atom, only a Summary **or** Content Role change creates a new base Atom ID. Content Role changes always create a new Atom, even with unchanged Summary. Claim, other Content, Type, Status, applicability **or** other property changes alone retain the base ID when Summary **and** Content Role stay unchanged. Scope narrowing **or** expansion is a `semantic_revision`, **not** carrier-only. Adding a separately authored Atom gives that new Atom its own ID; it does not itself replace an existing Atom whose Summary **and** Content Role remain unchanged. Lossless serialization of the same Summary value is **not** a Summary change. the semantic change class is independent of storage transactions **or** version-control change sets; persistence preserves the admitted Atom, Carrier, **and** Journal authority.

Each distinct Atom revision **must** have a unique `(Atom ID, Version)` pair across all Atoms, including Drafts. **every** actual same-ID update **must** have a successor Version greater than the predecessor Version, regardless of change class, **and** refresh Updated At under CA-R-1788. an exact no-op **must** retain Version **and** Updated At. When a predecessor is archived, its Archive Carrier **must** carry `status: Archived`, identify that predecessor as `<canonical-ID>@<old-version>`, and preserve its numeric Version, prior Updated At, and unrelated content. The Current successor retains the canonical ID, carries a unique Version greater than the predecessor Version, and receives the actual Project-time edit instant. Git history preserves the exact pre-archive Carrier bytes; the archive conversion does not require an exact-byte copy.

this classification concerns changes **to** the Atom's own bytes, metadata, direct ownership **or** local placement. moving an ancestor **only** changes a descendant's repository locator **when** that descendant's own bytes, metadata, direct owner **and** placement relative **to** that owner remain unchanged; this is **not** an Atom update **and** **must** retain that descendant's Version **and** Updated At. this boundary applies **to** **all** Atoms, including Plans nested under a moved Plan **and** Atoms whose owning Scope Unit moves. an actual change **to** the Atom itself, including its Status, filename, direct owner **or** local placement, still follows the classification **and** revision rules above. Exact pre-change bytes remain available through Git history.

Tools **may** propose a class but **must** fail closed **when** the distinction between refinement, semantic revision, **and** replacement is uncertain.
