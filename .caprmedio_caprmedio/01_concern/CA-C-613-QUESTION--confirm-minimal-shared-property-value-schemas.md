---
atom_id: CA-C-613
ref_id: CA-C-613
container:
  scope_unit: CA-SU-00
role: Concern
form: Question
topics:
  main_subject: Entity
tier: 3
status: Active
version: 1
updated_at: 2026-10-29 09:39:47 +0400
carrier_destination:
  file:
    name: CA-C-613-CAPRMEDIO-QUESTION--confirm-minimal-shared-property-value-schemas.md
    path: .caprmedio_caprmedio/01_concern
current_scope_unit: caprmedio
author: Anatoly Maslennikov
---
## Summary

Confirm minimal shared Property value schemas

## Question

Should the chosen continuation below change when a concrete conflicting use is identified?

## Details

The implementation uses string for identifiers/names/locators, integers for counts, optional explicit Scope Unit Label, and one or more string values for an ordered Scope Unit Path. Settings/registry/configuration groups have zero direct scalar values; their children keep independent counts. Producer- or invocation-specific properties read within their defining Claim scope. These choices complete the existing model without new stored fields or advanced conditions; change them only if a concrete source requires a different shape.

Latest 48-hour input and Current source meanings support this minimal continuation but do not fix every representation detail. The Operator directed choosing the best option, tracking uncertainty and continuing.
