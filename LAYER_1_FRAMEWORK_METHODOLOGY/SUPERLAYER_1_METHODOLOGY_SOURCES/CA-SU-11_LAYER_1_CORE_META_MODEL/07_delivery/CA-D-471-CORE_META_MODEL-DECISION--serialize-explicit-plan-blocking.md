---
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL <+ Relation
  passive:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan)
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation
  - CAPRMEDIO_MODEL <+ Atom.Header.ID
  - CAPRMEDIO_MODEL <+ Atom.Header.Subjects
version: 26
updated_at: 2026-11-04 16:52:59 +0400
relations:
  delivery_for:
  - CA-R-2762
  - CA-R-1580
  IS_CONTAINED_BY:
    scope_unit: CA-SU-11
atom_id: CA-D-471
status: Active
tier: 3
role: Delivery
form: Decision
carrier_destination:
  file:
    name: CA-D-471-CORE_META_MODEL-DECISION--serialize-explicit-plan-blocking.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery
---
## Summary

Serialize explicit Plan blocking

## Claim

### Prose Claim

For each direct `B IS_BLOCKED_BY A` fact, encode the prerequisite Plan `A` once as a canonical Atom ID in the dependent Plan `B` under `relations.IS_BLOCKED_BY`. Use a YAML sequence of unique Plan Atom IDs; an omitted list encodes no outgoing blocking Relations. Resolve each referenced ID to its intended Plan under applicable authority.

Do not store the derived `A BLOCKS B` view as a second fact. Do not encode Plan scheduling with `relations.depends_on` or `subjects.depends_on`. Store Plan containment separately under `IS_CONTAINED_BY`; do not derive blocking from containment or directory order.
