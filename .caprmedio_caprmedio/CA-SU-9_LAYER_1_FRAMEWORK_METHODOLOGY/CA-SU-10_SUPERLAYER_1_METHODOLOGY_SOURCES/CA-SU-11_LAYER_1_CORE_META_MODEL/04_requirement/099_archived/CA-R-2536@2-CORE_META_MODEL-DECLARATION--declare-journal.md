---
atom_id: CA-R-2536
ref_id: CA-R-2536@2
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Journal
tier: 3
status: archived
version: 2
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-R-2536@2-CORE_META_MODEL-DECLARATION--declare-journal.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/099_archived
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Declare Journal

## Claim

### Formal Claim

```CFEL
# model
Journal {::0}((IS_PROPERTY_OF));

Journal >| (Container == yes);

Journal ((NARROWER_THAN)) Continuant;

# instances
Journal//$journal{::1};

Journal//$journal_2 {::0+}((CONTAINS)) Event Record//$event_record;
```

## Semantics

A Journal preserves accepted event history.
