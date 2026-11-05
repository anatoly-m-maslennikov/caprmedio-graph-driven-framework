---
atom_id: CA-R-1695
ref_id: CA-R-1695
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Traceability
  dependencies:
  - CAPRMEDIO_MODEL <+ Journal
  - CAPRMEDIO_MODEL <+ Scope Unit
  - CAPRMEDIO_MODEL <+ Atom
  - CAPRMEDIO_MODEL <+ Projection
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Evaluation)
tier: 3
relations:
  child_of:
  - CA-R-1682
  - CA-R-1697
  - CA-R-1720
status: Active
version: 38
updated_at: 2026-11-02 18:35:20 +0400
carrier_destination:
  file:
    name: CA-R-1695-CORE_META_MODEL-RULE--preserve-implementation-traceability-in-the-shared-project-journal.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Preserve Implementation traceability in the shared Project Journal

## Claim

### Prose Claim


structural Scope Units that realize RMED Atoms.


**every** structural Scope Unit that realizes RMED Atoms **must** record its Implementation Bindings **in** the shared Project Work Journal. its admitted Records establish, replace, correct, **or** remove Implementation Bindings **and** bind exact Requirement, Method, Evaluation, **and** Delivery Atom Revisions **to** the native implementation targets that declare their realization.

the Journal is canonical for the declared implementation relationship. native source, configuration, executable evaluation mechanisms, packages, **and** delivery automation remain canonical for the operative realization itself. Operations evidence **and** Verification remain the authorities for what occurred **and** whether the realization is sufficiently assured. recording an implementation relationship never proves correctness **or** successful operation.

an Implementation Binding **must** survive transformations **or** migration of secondary storage history. the binding therefore identifies **every** source Atom by stable artifact identity plus revision digest **and** **every** native implementation target by a stable locator plus content digest. secondary storage records, review records, Authors, sessions, **and** signatures remain useful provenance but are **not** the sole semantic identity of the binding.

corrections, replacements, target removal, **and** changed implementation coverage append new records; accepted Journal records are never edited, reordered, **or** deleted. the effective implementation frontier is derived from the complete ordered record sequence.

Implementation-role Projections are regenerated from the Journal **and** its declared current source **and** target frontier. they **may** present implementation coverage, mappings, missing realization, **and** potentially stale bindings, but they remain rebuildable **and** non-authoritative over the Journal, normative Atoms, native implementation, **or** evaluation conclusions.

## Details

**every** implementing Scope Unit **must** preserve storage-independent traceability from exact normative Atom Revisions **to** native implementation targets **in** the shared Project Work Journal **and** derive Implementation Projections from that Journal.
