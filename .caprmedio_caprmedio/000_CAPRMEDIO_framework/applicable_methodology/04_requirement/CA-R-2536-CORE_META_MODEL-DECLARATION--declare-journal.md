---
atom_id: CA-R-2536
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Journal
version: 2
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2536-CORE_META_MODEL-DECLARATION--declare-journal.md
  source_atom_id: CA-R-2536
  source_atom_revision: 2
  source_sha256: 20a5b68515df5b16e7b2a4facd9304f786d7fcbefb16097e8480d930ef93c991
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Declare Journal

## Claim

### Formal Claim

```CFEL
# model
Journal {:0}((IS_PROPERTY_OF));

Journal >| (Container == yes);

Journal ((NARROWER_THAN)) Continuant;

# instances
Journal//$journal{:1};

Journal//$journal_2 {:0+}((CONTAINS)) Event Record//$event_record;
```

## Semantics

A Journal preserves accepted event history.
