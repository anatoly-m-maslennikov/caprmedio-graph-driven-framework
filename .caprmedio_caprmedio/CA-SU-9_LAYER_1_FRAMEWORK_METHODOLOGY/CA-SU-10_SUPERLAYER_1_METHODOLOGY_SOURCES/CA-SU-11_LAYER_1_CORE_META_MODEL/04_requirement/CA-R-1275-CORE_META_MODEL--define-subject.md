---
atom_id: CA-R-1275
ref_id: CA-R-1275
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom.Header.Context.Topics
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom
  - CAPRMEDIO_MODEL <+ Entity
  - CAPRMEDIO_MODEL <+ Term
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation
tier: 1
status: Active
version: 32
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-R-1275-CORE_META_MODEL-RULE--define-subject.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Define Subject

## Claim

### Prose Claim


Things or topics an Atom governs or depends on.



An Atom.Header.Subjects target must name the thing or topic the Atom governs or depends on; it is not a copied target, intermediate Subject object, or a requirement for a separate entity kind.

## Details

- GOVERNS and DEPENDS_ON are separate connected relations. Each relation connects an Atom to a target in the Subject graph.
- a Subject names the target; it is not the relation, an intermediate Subject object, or a copied target. A target may be a classification axis or another topic without being a separate entity kind.
- the set of Subjects forms a graph, and a full canonical Subject path names a target in that graph.
- Entity is the canonical expression root. Its direct branches follow the governing Entity Definition in CA-R-2462; this Rule does not enumerate a closed branch set. Object specializes into Continuant and Occurrent. A source path retains the declared operators and full qualification; a short display label is not another identity or alias.
- An Atom's Local Scope Unit does not determine its Subject. Name the governed thing or topic rather than copying that Scope Unit.
