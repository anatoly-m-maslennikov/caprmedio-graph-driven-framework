---
atom_id: CA-R-2618
ref_id: CA-R-2618
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation//HAS_ACTIVE_SUBJECT
tier: 3
status: Active
version: 3
updated_at: 2026-11-03 23:25:51 +0400
carrier_destination:
  file:
    name: CA-R-2618-CORE_META_MODEL-DECLARATION--declare-has-active-subject.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2618-CORE_META_MODEL-DECLARATION--declare-has-active-subject.md
  source_atom_id: CA-R-2618
  source_atom_revision: 3
  source_sha256: 875c1cbc4aa0656a57d574fa1849e73c9838e4ae303ea976c2a270036551a01d
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Declare HAS_ACTIVE_SUBJECT

## Claim

### Prose Claim

HAS_ACTIVE_SUBJECT links an Atom to the declared model entity or instance named by its active Subject. This includes a Requirement/Form Declaration's target and is not restricted to the Node branch. Carrier entities, CFEL operator descriptors, graph Relation types and their declared instances are admitted when selected by the active Subject. Literal values and operator glyphs are not endpoints.

The Host is an Atom and the Target is the entity or instance resolved from its dedicated active Subject field. The field's source supplies the canonical HAS_ACTIVE_SUBJECT fact; obtaining that value from the field does not make this Relation a derived view of another Relation. An unresolved Subject remains a diagnostic, not an empty or automatically valid target population.

Forward `Host ((HAS_ACTIVE_SUBJECT)) Target` and reverse `Target <((HAS_ACTIVE_SUBJECT)) Host` are written views of the same fact. Ownership cardinalities are supplied by their applicable rules; this endpoint signature does not itself create an ownership count.
### Formal Claim

```CFEL
# model
Relation//HAS_ACTIVE_SUBJECT ((HAS_CLASSIFICATION)) Derivation == Direct;

# instances
Atom//$atom ((HAS_ACTIVE_SUBJECT)) $active_subject
```

