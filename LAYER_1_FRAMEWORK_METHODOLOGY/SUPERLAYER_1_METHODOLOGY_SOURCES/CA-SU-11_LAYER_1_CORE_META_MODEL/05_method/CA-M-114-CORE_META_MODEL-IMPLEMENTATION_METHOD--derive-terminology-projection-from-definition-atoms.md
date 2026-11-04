---
subjects:
  active: CAPRMEDIO_MODEL <+ Projection
  passive:
  - CAPRMEDIO_MODEL <+ Projection/(.Form:=Catalog)
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Method)/(.Header.Form := Term Definition)
  - CAPRMEDIO_MODEL <+ Term
  - CAPRMEDIO_MODEL <+ Project
  - CAPRMEDIO_MODEL <+ Atom.Content
  - CAPRMEDIO_MODEL <+ Entity
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role: Operations)/(.Header.Form: Action)'
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role: Operations)/(.Header.Form: Workflow)'
version: 44
updated_at: 2026-11-04 18:28:33 +0400
relations:
  IS_CONTAINED_BY:
    scope_unit: CA-SU-11
atom_id: CA-M-114
status: Active
tier: 3
role: Method
form: Implementation Method
carrier_destination:
  file:
    name: CA-M-114-CORE_META_MODEL-IMPLEMENTATION_METHOD--derive-terminology-projection-from-definition-atoms.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/05_method
---
## Summary

Derive Terminology Projection from Definition Atoms

## Claim

### Prose Claim


optional derivation of a terminology Projection from active Method Atoms of Type Term Definition.


**to** build a terminology list using the Catalog Type, the Generator **must** derive **every** Governed Term's name **and** Project-specific meaning from its active Method Atom of Type Term Definition. read the Term named by the defining Claim **and** verify that the Term Definition Atom's GOVERNS Subject Relation identifies its defined target under CA-R-1279-CORE_META_MODEL-RULE--govern-every-defined-term. inspect **every** named entity **and** named component of a Subject Path, **not** **only** its terminal component; extract **only** evidenced occurrences of reusable Project Terms. keep exact full entity names **and** source-admitted instance labels distinct from reusable Term occurrences; their spelling **or** position **in** a Subject Path alone does **not** classify them as Terms **or** require a Term Definition. obtain **every** evidenced reusable Term's meaning from that Term's own defining Claim, **not** by treating **all** path components as definitions supplied by the referencing Atom **or** inferring its meaning from Entity Definitions **or** their Semantics. include an entry **only** **when** its explicit Term Definition Claim establishes a Project-specific meaning; consistent use **or** capitalization alone does **not** supply defining authority. report uncertain Term classification **or** segmentation as unresolved; **do not** invent a definition, infer lexical authority from spelling, **or** silently resolve that uncertainty as ordinary vocabulary. exclude words **and** phrases used **only** with their ordinary English meanings. retain the source reference **without** classifying the direct Subject reference **or** a complete composite Subject Path as a Term **or** creating independent vocabulary authority.

## Details

This Method applies only when a terminology Projection is requested. It does not make a dictionary, lookup table, Terms Graph, or other Projection a prerequisite for direct source-based authoring or evaluation. Lexical meaning ownership remains with the exact active Term Definition Atom and revision; source selection and GOVERNS binding do not turn an Entity Definition or derived Projection into lexical defining authority.
