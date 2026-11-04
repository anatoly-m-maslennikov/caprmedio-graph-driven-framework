---
atom_id: CA-M-450
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Term//ID
  passive:
  - CAPRMEDIO_MODEL <+ Term
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Method)/(.Header.Form := Term Definition)
version: 7
updated_at: 2026-11-04 18:28:33 +0400
relations:
  IS_CONTAINED_BY:
    scope_unit: CA-SU-11
tier: 1
role: Method
form: Term Definition
carrier_destination:
  file:
    name: CA-M-450-CORE_META_MODEL-TERM_DEFINITION--define-id.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/05_method
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/05_method/CA-M-450-CORE_META_MODEL-TERM_DEFINITION--define-id.md
  source_atom_id: CA-M-450
  source_atom_revision: 7
  source_sha256: e50baff8a701137943ffd82e5b262d1e910191b5f26045a68102f7a2ca60fcea
  original_relations_sha256: e367927d209b7bdecd9da53dd0dc693193d074370738c97b4bc15988d6240196
---
## Summary

Define ID

## Claim

### Prose Claim


The reusable lexical Term `ID` as used for identifiers of Continuant and Occurrent entity instances within a matching prefix namespace.


ID **means** a unique identifier used **to** find **`=1`** entity instance, whether Continuant **or** Occurrent, whose uniqueness is bounded **to** its matching prefix namespace. This Claim explicitly introduces the lexical Term instance named ID at `Term//ID`.

## Details

The Operator supplied this meaning and accepted `CA-P-123`, `CA-P-123@1-draft`, and `CA-P-123@3` as examples. The examples do not define lifecycle identity, version equivalence, Draft/Current/Archived transitions, or a rule for changing an existing identifier. Existing identifier and lifecycle authority retains those responsibilities. Matching local or numeric parts under different prefixes do not by themselves establish a collision; a collision within the matching prefix namespace does not satisfy the meaning.

`ID` retains its approved meaning across its uses. The contextual topic/code spellings `atom.id` and `projection.id` distinguish their respective ID Properties; they are not alternative complete canonical Subject names or case-folded aliases. Authored Subjects use their full admitted expressions. Their shared terminal label need not be globally unique. Dot remains qualification syntax rather than a Term. These literal spellings are not changed to `atom.atom_id` or similar invented spellings, and existing code identifiers are not renamed.

This Active Method Term Definition is the single authoritative meaning owner of the lexical Term ID under CA-R-1319. E evaluates well-formedness and conflicts. No dictionary Projection, extractor, or lookup service is required.

The initially flat target `Term//ID` is explicitly introduced by this defining Claim, not inferred from property-name letters. This definition introduces no property, domain instance, prefix namespace, Relation, or other entity merely by naming it. It does not implement the deferred Terms Graph or waive applicable defining-target binding rules; C605's separate Term-placement reconciliation remains applicable.
