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
