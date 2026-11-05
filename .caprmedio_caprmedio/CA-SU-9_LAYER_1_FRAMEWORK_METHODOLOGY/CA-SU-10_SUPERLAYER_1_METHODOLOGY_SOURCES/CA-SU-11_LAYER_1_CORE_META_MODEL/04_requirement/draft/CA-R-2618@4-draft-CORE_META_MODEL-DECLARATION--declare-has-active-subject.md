---
atom_id: CA-R-2618
ref_id: CA-R-2618@4-draft
status: Draft
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation//HAS_ACTIVE_SUBJECT
version: 4
updated_at: 2026-11-05 14:25:52 +0400
tier: 3
role: Requirement
form: Declaration
carrier_destination:
  file:
    name: CA-R-2618@4-draft-DECLARATION--declare-has-active-subject.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/draft
container:
  scope_unit: CA-SU-11
---
## Summary

Declare HAS_ACTIVE_SUBJECT

## Claim

### Formal Claim

```CFEL
# model
Relation//HAS_ACTIVE_SUBJECT ((HAS_CLASSIFICATION)) Derivation == Direct;

# instances
Atom//$atom ((HAS_ACTIVE_SUBJECT)) $active_subject
```

### Prose Claim

HAS_ACTIVE_SUBJECT links an Atom to the declared model entity or instance named by its active Subject. This includes a Requirement/Form Declaration's target and is not restricted to the Node branch. Carrier entities, graph Relation types and their declared instances are admitted when selected by the active Subject. Literal values and CFEL syntax glyphs are not endpoints.

The Host is an Atom and the Target is the entity or instance resolved from its dedicated active Subject field. The field's source supplies the canonical HAS_ACTIVE_SUBJECT fact; obtaining that value from the field does not make this Relation a derived view of another Relation. An unresolved Subject remains a diagnostic, not an empty or automatically valid target population.

Forward `Host ((HAS_ACTIVE_SUBJECT)) Target` and reverse `Target <((HAS_ACTIVE_SUBJECT)) Host` are written views of the same fact. Ownership cardinalities are supplied by their applicable rules; this endpoint signature does not itself create an ownership count.
