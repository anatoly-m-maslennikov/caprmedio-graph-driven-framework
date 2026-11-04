---
atom_id: CA-R-2559
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL
version: 2
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2559-CORE_META_MODEL-DECLARATION--declare-model.md
  source_atom_id: CA-R-2559
  source_atom_revision: 2
  source_sha256: 365bc7d8a6f0cf72740253ae73c83475a22d70fba83497ae9abed6c28b379263
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---

## Summary

Declare MODEL

## Claim

### Formal Claim

```CFEL
# model
MODEL {:0}((IS_PROPERTY_OF));

MODEL >| (Container == yes);

MODEL ((NARROWER_THAN)) Node
```

### Prose Claim



- A local MODEL inherits CAPRMEDIO's MODEL.
- MODEL inheritance is distinct from Node narrowing.
- Local overrides replace matching inherited rules in the local MODEL.
- Local overrides preserve the base MODEL's rules.
- Unmodified inherited Declarations are reused.

## Semantics

MODEL declares Node kinds, Relations, Properties, and rules.
