---
subjects:
  active: CAPRMEDIO <+ MODEL <+ CFEL <+ Relation//DEPENDS_ON
  passive:
  - CAPRMEDIO <+ MODEL <+ CFEL > Relation
  - CAPRMEDIO <+ MODEL <+ Atom
  - CAPRMEDIO <+ MODEL <+ Entity
  - 'CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan/Type: Plan'
  - CAPRMEDIO <+ MODEL <+ Atom.Content
  - 'CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Workflow'
version: 39
updated_at: 2026-11-02 08:06:47 +0400
relations:
  depends_on:
  - CA-R-1275
atom_id: CA-R-1200
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 2
role: Requirement
form: Declaration
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1200-CORE_META_MODEL-DECLARATION--define-depends-on-subject-relation-kind.md
  source_atom_id: CA-R-1200
  source_atom_revision: 39
  source_sha256: 947df6df409e74eef63038de0d5d982f4c78a537795e876f24fc6563e66847b7
  original_relations_sha256: 716ef4f4c69122347b79d3f5b5752b137772edf3b9edf48f251d5d752fc50a4d
---
## Summary

Define DEPENDS_ON Subject Relation Kind

## Claim scope

the DEPENDS_ON Subject Relation Kind of an Atom.

## Claim

DEPENDS_ON **means** the direct Subject Relation Kind from an Atom **to** a canonical Subject graph node mentioned **in** its applicable role-specific content or other registered content, other than its GOVERNS target. this reference does **not** make the Atom's content—or every Governing Configuration fact—authoritative about that Subject graph node; formal authority depends on the applicable registered content form and role. a formal Claim may be carried in Markdown, structured YAML, or Governing Configuration, but Governing Configuration facts are not automatically Atom Claims.

```CFEL
((DEPENDS_ON)) >| Derivation == Direct;

Atom// ((DEPENDS_ON)) $referenced_subject
```

## Semantics



The Target is a canonical Subject referenced by the Atom, other than its governing target.
Forward `Host ((DEPENDS_ON)) Target` and reverse `Target <((DEPENDS_ON)) Host` are views of the same Relation fact.
DEPENDS_ON relates Atom to referenced Subject graph node.

## Details

mentions **in** Summary, Scope, Claim, Details, other registered body sections, tables, **and** examples count, whether the logical Claim is carried in Markdown, structured YAML, or Governing Configuration. this Relation does **not** establish Workflow control flow **or** execution order; Plan start prerequisites remain separately governed by `BLOCKS` under CA-R-1580-CORE_META_MODEL-DEFINITION--define-plan-blocking.
