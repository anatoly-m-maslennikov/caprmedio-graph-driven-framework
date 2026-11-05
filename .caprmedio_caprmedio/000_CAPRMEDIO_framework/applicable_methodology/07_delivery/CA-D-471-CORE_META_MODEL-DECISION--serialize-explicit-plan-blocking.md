---
atom_id: CA-D-471
ref_id: CA-D-471
container:
  scope_unit: CA-SU-11
role: Delivery
form: Decision
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan)
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation
  - CAPRMEDIO_MODEL <+ Atom.Header.ID
  - CAPRMEDIO_MODEL <+ Atom.Header.Topics
tier: 3
relations:
  delivery_for:
  - CA-R-2762
  - CA-R-1580
status: Active
version: 26
updated_at: 2026-11-04 16:52:59 +0400
carrier_destination:
  file:
    name: CA-D-471-DECISION--serialize-explicit-plan-blocking.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-471-CORE_META_MODEL-DECISION--serialize-explicit-plan-blocking.md
  source_atom_id: CA-D-471
  source_atom_revision: 26
  source_sha256: f52ca0e1d28edacc30d0d3da4e34e0bbf78a4589f0078a2b1e7097048b2959d4
  original_relations_sha256: 673cfbdec060744a589f1a458280405dd7fe1d1f030d8a94d3fedcf2988a439d
---
## Summary

Serialize explicit Plan blocking

## Claim

### Prose Claim

For each direct `B IS_BLOCKED_BY A` fact, encode the prerequisite Plan `A` once as a canonical Atom ID in the dependent Plan `B` under `relations.IS_BLOCKED_BY`. Use a YAML sequence of unique Plan Atom IDs; an omitted list encodes no outgoing blocking Relations. Resolve each referenced ID to its intended Plan under applicable authority.

Do not store the derived `A BLOCKS B` view as a second fact. Do not encode Plan scheduling with `relations.depends_on` or `subjects.depends_on`. Store Plan containment separately under `IS_CONTAINED_BY`; do not derive blocking from containment or directory order.
