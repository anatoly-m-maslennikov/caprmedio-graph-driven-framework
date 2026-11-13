---
atom_id: CA-R-1200
ref_id: CA-R-1200@41
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation//DEPENDS_ON
  dependencies:
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation
  - CAPRMEDIO_MODEL <+ Atom
  - CAPRMEDIO_MODEL <+ Entity
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Plan)/(.Header.Context.Form :=
    Plan)
  - CAPRMEDIO_MODEL <+ Atom.Content
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Operations)/(.Header.Context.Form
    := Workflow)
tier: 2
relations:
  depends_on:
  - CA-R-1275
status: archived
version: 41
updated_at: 2026-11-04 03:22:03 +0400
carrier_destination:
  file:
    name: CA-R-1200@41-CORE_META_MODEL-DECLARATION--define-depends-on-subject-relation-kind.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/099_archived
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Define DEPENDS_ON Subject Relation Kind

## Claim

### Prose Claim

#### Applicability
the DEPENDS_ON Subject Relation Kind of an Atom.

DEPENDS_ON **means** the direct Subject Relation Kind from an Atom **to** a canonical Subject entity or instance mentioned **in** its applicable role-specific content or other registered content, other than its GOVERNS target. this reference does **not** make the Atom's content—or every Governing Configuration fact—authoritative about that Subject entity or instance; formal authority depends on the applicable registered content form and role. a formal Claim may be carried in Markdown, structured YAML, or Governing Configuration, but Governing Configuration facts are not automatically Atom Claims.

The Target is a canonical Subject referenced by the Atom, other than its governing target.
Forward `Host ((DEPENDS_ON)) Target` and reverse `Target <((DEPENDS_ON)) Host` are views of the same Relation fact.
DEPENDS_ON relates Atom to referenced Subject entity or instance.

#### Details
mentions **in** Summary, Scope, Claim, Details, other registered body sections, tables, **and** examples count, whether the logical Claim is carried in Markdown, structured YAML, or Governing Configuration. this Relation does **not** establish Workflow control flow **or** execution order; Plan start prerequisites remain separately governed by `BLOCKS` under CA-R-1580-CORE_META_MODEL-DEFINITION--define-plan-blocking.
### Formal Claim

```CFEL
# model
Relation//DEPENDS_ON ((HAS_CLASSIFICATION)) Derivation == Direct;

# instances
Atom//$atom ((DEPENDS_ON)) $referenced_subject
```

