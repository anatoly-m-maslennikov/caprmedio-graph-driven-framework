---
atom_id: CA-D-670
ref_id: CA-D-670
role: Delivery
form: Eng Decision
topics:
  main_subject: CAPRMEDIO_MODEL <+ Scope Unit
  dependencies:
  - Entity/Object/Continuant/History
  - CAPRMEDIO_MODEL <+ Journal
  - CAPRMEDIO_MODEL <+ Carrier
tier: 3
status: Active
version: 1
updated_at: 2026-11-02 19:17:40 +0400
---
## Summary

Bind Scope Unit Declarations to source evidence

## Claim

A Scope Unit Declaration source binding identifies the exact current Declaration bytes by SHA-256 digest. Readers determine current structure from those bytes. Journal events record history and do not determine whether the current Declaration is readable.
