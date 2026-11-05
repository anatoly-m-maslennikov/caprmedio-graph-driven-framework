---
atom_id: CA-D-269
ref_id: CA-D-269
container:
  scope_unit: CA-SU-11
role: Delivery
form: Policy
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom.Header.Topics
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom.Header.Topics
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation//GOVERNS
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation//DEPENDS_ON
  - CAPRMEDIO_MODEL <+ Entity
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation
tier: 3
status: Active
version: 28
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-D-269-CORE_META_MODEL-POLICY--serialize-atom-subjects-in-frontmatter.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-269-CORE_META_MODEL-ENG_DECISION--serialize-atom-subjects-in-frontmatter.md
  source_atom_id: CA-D-269
  source_atom_revision: 28
  source_sha256: 1e015cdfc9c0298838abca19238d57f424db0c92f81b99cc233e23f6df9024d4
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Serialize Atom Subjects in Frontmatter

## Claim

### Prose Claim


New or migrated Markdown Atom carriers.


For Markdown Atom carriers, encode `subjects` as a mapping with one scalar nonempty Entity path under `active` and zero or more unique nonempty Entity paths as a YAML sequence under `passive`. An omitted `passive` means zero. The grouping mapping has no direct value; its child values are counted separately. A Draft may be incomplete before promotion.

Preserve the decoded Entity paths exactly under the applicable notation and resolve targets under the applicable Subject rules. A defining Atom may introduce its target and path together. Do not add an intermediate reference object or a repeated target-type field. YAML quotes are not part of the decoded expression; preserve escapes and reference boundaries. Each YAML key occurs once within its own mapping. Preserve formal cardinality annotations and decoded Entity escapes exactly; do not serialize notation as extra YAML fields.

The canonical keys are `active` and `passive`. Existing `governs` and `depends_on` remain readable during carrier migration. Mixed old and new aliases with unequal values are invalid. Equal aliases can be read during transition, without asserting additional Subjects.

## Details

Reference migration preserves target identity and follows the governing Entity rules. Subject paths are distinct from formal Relation expressions in the body Claim.
