---
subjects:
  active: CAPRMEDIO_MODEL <+ Atom.Header.Subjects
  passive:
  - CAPRMEDIO_MODEL <+ Atom.Header.Subjects
  - CAPRMEDIO_MODEL <+ CFEL > Relation//GOVERNS
  - CAPRMEDIO_MODEL <+ CFEL > Relation//DEPENDS_ON
  - CAPRMEDIO_MODEL <+ Entity
  - CAPRMEDIO_MODEL <+ CFEL > Relation
version: 28
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-D-269
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Delivery
form: Policy
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
