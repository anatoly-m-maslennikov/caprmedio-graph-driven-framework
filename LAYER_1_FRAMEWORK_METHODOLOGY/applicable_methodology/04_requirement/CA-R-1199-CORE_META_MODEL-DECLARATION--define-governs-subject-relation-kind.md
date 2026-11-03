---
subjects:
  active: CAPRMEDIO <+ MODEL <+ CFEL <+ Relation//GOVERNS
  passive:
  - CAPRMEDIO <+ MODEL <+ CFEL > Relation
  - CAPRMEDIO <+ MODEL <+ Atom
  - CAPRMEDIO <+ MODEL <+ Entity
  - CAPRMEDIO <+ MODEL <+ Atom.Content
version: 36
updated_at: 2026-11-02 08:06:47 +0400
relations:
  depends_on:
  - CA-R-1275
atom_id: CA-R-1199
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 2
role: Requirement
form: Declaration
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1199-CORE_META_MODEL-DECLARATION--define-governs-subject-relation-kind.md
  source_atom_id: CA-R-1199
  source_atom_revision: 36
  source_sha256: 9e3d9efe97649c9df25e6544a20f95bf67df23773ae2e5ebc9bf08ebb1732604
  original_relations_sha256: 716ef4f4c69122347b79d3f5b5752b137772edf3b9edf48f251d5d752fc50a4d
---
## Summary

Define GOVERNS Subject Relation Kind

## Claim scope

the GOVERNS Subject Relation Kind.

## Claim

GOVERNS **means** the direct Subject Relation Kind from an Atom **to** the canonical Subject graph node about which the Atom governs through its applicable role-specific content.

```CFEL
((GOVERNS)) >| Derivation == Direct;

Atom// ((GOVERNS)) $governed_subject
```

## Semantics



The Target is the canonical Subject about which the Atom governs through its applicable content.
Forward `Host ((GOVERNS)) Target` and reverse `Target <((GOVERNS)) Host` are views of the same Relation fact.
GOVERNS relates Atom to canonical Subject graph node.

