---
atom_id: CA-R-2003
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Entity/Property
  passive:
  - CAPRMEDIO_MODEL <+ Term//Property
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation//IS_PROPERTY_OF
  - CAPRMEDIO_STRUCTURE <+ Entity/Object/Continuant/Selection//Property Occurrences
relations: {}
version: 16
updated_at: 2026-11-02 19:46:47 +0400
tier: 1
role: Requirement
form: Rule
---
## Summary

Require exactly one immediate bearer for each dependent Entity occurrence

## Claim

### Prose Claim


Declared Property occurrences and their direct IS_PROPERTY_OF connections.


Every declared Property occurrence must have exactly one immediate bearer, identified by one outgoing direct IS_PROPERTY_OF connection to that bearer. A source establishes dependence independently of whether the edge is present, so a missing edge fails this requirement. The named Selection “Property Occurrences” selects those declared occurrences; it does not infer dependence from edges or create a bearer connection.

## Semantics

Property is the proposed kind `Entity/Property`, grounded in bearer dependence through IS_PROPERTY_OF. Its lexical Term is separately defined at `Term//Property`. Classifying an occurrence in that kind does not invent a bearer edge or treat a missing edge as proof of independence. The Property occurrence has identity qualified by its immediate bearer; the Property definition supplies its value Format and direct-value cardinality. The bearer-Relation count is distinct from the number of values a Property allows.

## Details

This is a Current-pinned N+1 successor of CA-R-2003@13 at `.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2003-CORE_META_MODEL--require-exactly-one-immediate-bearer-for-each-dependent-entity-occurrence.md`, SHA-256 `6a3eca859d913fb3800693219f3587bd35dc957f2509433e38606d2a1f8a730d`. It preserves the exactly-one immediate-bearer requirement and the existing declared-occurrence Selection criteria. The inherited Summary and source pin remain historical Current lineage; the proposed Selection-name mapping below is explicit and introduces no alias. The older @11 Draft is marked superseded preparation and is not overwritten or selected as the predecessor. No Current source is changed, no numeric identity is allocated, and no new Primary Entity branch is proposed.

This Draft records the governed Selection-name mapping from `Entity/Object/Continuant/Selection//Dependent Entity Occurrences` to `Entity/Object/Continuant/Selection//Property Occurrences`. The renamed Selection continues to select every source-declared Property occurrence independently of whether its IS_PROPERTY_OF connection exists. It includes missing-edge cases and neither infers dependence from edges nor creates a bearer connection. The old name remains only in this source-mapping evidence, not as an admitted alias. A named Selection names criteria under Current CA-R-1966@12; this mapping creates no new Object, independent member copies or identity rules. The immutable Atom Summary, filename and identity are unchanged. This is a proposed source mapping, not Current adoption.
