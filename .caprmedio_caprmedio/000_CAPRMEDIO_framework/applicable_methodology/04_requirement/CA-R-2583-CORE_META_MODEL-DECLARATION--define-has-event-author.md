---
atom_id: CA-R-2583
ref_id: CA-R-2583
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation//HAS_EVENT_AUTHOR
tier: 3
status: Active
version: 5
updated_at: 2026-11-03 20:00:05 +0400
carrier_destination:
  file:
    name: CA-R-2583-CORE_META_MODEL-DECLARATION--define-has-event-author.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2583-CORE_META_MODEL-DECLARATION--define-has-event-author.md
  source_atom_id: CA-R-2583
  source_atom_revision: 5
  source_sha256: 1b997967f0873dfc220cf5e18e5b4b10cdd8b2e5c214e48f450a80f61944e075
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Define HAS_EVENT_AUTHOR

## Claim

### Prose Claim

HAS_EVENT_AUTHOR identifies the Actor who performed the recorded event.

Forward `Host ((HAS_EVENT_AUTHOR)) Target` and reverse `Target <((HAS_EVENT_AUTHOR)) Host` are views of the same Relation fact.
HAS_EVENT_AUTHOR relates Event Record instance to Actor instance.
### Formal Claim

```CFEL
# model
Relation//HAS_EVENT_AUTHOR ((HAS_INVERSE)) Relation//IS_EVENT_AUTHOR_OF;

Relation//HAS_EVENT_AUTHOR ((HAS_CLASSIFICATION)) Derivation == Direct;

# instances
Event Record//$event_record ((HAS_EVENT_AUTHOR)) Actor//$actor;
```

