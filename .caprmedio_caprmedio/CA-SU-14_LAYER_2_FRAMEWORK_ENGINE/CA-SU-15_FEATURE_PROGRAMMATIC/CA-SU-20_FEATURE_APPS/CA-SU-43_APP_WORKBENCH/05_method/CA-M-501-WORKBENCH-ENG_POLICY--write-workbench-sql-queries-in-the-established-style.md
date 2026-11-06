---
atom_id: CA-M-501
ref_id: CA-M-501
container:
  scope_unit: CA-SU-43
role: Method
form: Eng Policy
topics:
  main_subject: CAPRMEDIO_MODEL <+ Projection
tier: 4
status: Active
version: 2
updated_at: 2026-11-06 21:07:42 +0400
carrier_destination:
  file:
    name: CA-M-501-WORKBENCH-ENG_POLICY--write-workbench-sql-queries-in-the-established-style.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/05_method
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
author: Anatoly Maslennikov
---

## Summary

Write Workbench SQL queries in the established style

## Claim scope

SQL queries written for Workbench and its child Scope Units.

## Claim

### Prose Claim

Write Workbench SQL queries in this style:

```sql
SELECT
  "content.claim.prose_claim"
  ,"content.claim.formal_claim"
from atoms
where true
  and "header_status" = 'Active'
  and "content.claim.formal_claim" is not null
;
```

Use uppercase `SELECT` on its own line. Indent selected columns and conditions by two spaces; put each additional selected column on its own line with a leading comma. Use lowercase `from`, `where`, `and`, and other SQL keywords. Start a filtered `where` clause with `true`, then put one condition on each following line. Double-quote column names and single-quote string values. Put the final semicolon on its own line.

Use the actual complete flattened Header names and the declared Content names with dotted snake_case segments.

When formatting existing SQL, retain its expressions, identifiers, literal values and comments. Apply layout and keyword case without adding clauses, conditions or identifier quotes to reproduce an example.

