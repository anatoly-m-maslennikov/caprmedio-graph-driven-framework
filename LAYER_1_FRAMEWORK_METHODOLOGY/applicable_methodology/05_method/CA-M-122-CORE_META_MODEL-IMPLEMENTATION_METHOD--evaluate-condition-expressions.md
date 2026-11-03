---
subjects:
  active: Aspects <+ Engineering <+ Authoring <+ Controlled English
  passive:
  - Aspects <+ Engineering <+ Authoring <+ Controlled English
  - Aspects <+ Engineering <+ Data Handling <+ Parsing
version: 30
updated_at: 2026-11-02 18:35:20 +0400
relations:
  child_of:
  - CA-M-113
atom_id: CA-M-122
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 5
role: Method
form: Implementation Method
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/05_method/CA-M-122-CORE_META_MODEL-IMPLEMENTATION_METHOD--evaluate-condition-expressions.md
  source_atom_id: CA-M-122
  source_atom_revision: 30
  source_sha256: 4512d0019a557bb46bffc6c7ed59a9e3173fb860334a792fa6db97e485e287d5
  original_relations_sha256: 5f066d0d540764c9ad10d23356476187cf16ff2f1371455cc960087fa7d5e467
---
## Summary

Evaluate Condition Expressions

## Claim scope

evaluation of CCE Condition Expressions.

## Claim

**to** evaluate one CCE condition expression, the Resolver **must** perform **all** of:

1. evaluate the innermost parenthesized function **before** its containing function.
2. evaluate **`=`** **and** **`!=`** as exact equality **and** inequality between one governed property **and** one canonical value.
3. evaluate **`<`**, **`<=`**, **`>`**, **and** **`>=`** **only** for properties with one governed comparison order.
4. evaluate **in** **and** **not in** as scalar membership **and** non-membership **in** one explicitly parenthesized value list, **or** according **to** CA-M-127-CORE_META_MODEL-IMPLEMENTATION_METHOD--evaluate-set-valued-property-membership **when** the governed property is set-valued.
5. evaluate **is empty** **and** **is not empty** as absence **and** presence of a governed property value.
6. evaluate **contains**, **starts with**, **and** **ends with** **only** for governed textual property values.
7. evaluate **and** as true **only** **when** **every** argument is true.
8. evaluate **or** as true **when** **`>=1`** argument is true.
9. evaluate **not** as the inverse truth value of its argument.
10. evaluate **if** ... **then** as false **only** **when** its antecedent is true **and** its consequent is false.
11. evaluate **every** as true **only** **when** its predicate is true for **every** member of its population.
12. evaluate **any** as true **when** its predicate is true for **`>=1`** member of its population.
13. evaluate **none** as true **only** **when** its predicate is false for **every** member of its population.
14. evaluate **where** as restriction of one population **to** members whose predicate is true.
15. use another logical function **only** **when** an active CCE Method gives that function **`=1`** logical meaning.
