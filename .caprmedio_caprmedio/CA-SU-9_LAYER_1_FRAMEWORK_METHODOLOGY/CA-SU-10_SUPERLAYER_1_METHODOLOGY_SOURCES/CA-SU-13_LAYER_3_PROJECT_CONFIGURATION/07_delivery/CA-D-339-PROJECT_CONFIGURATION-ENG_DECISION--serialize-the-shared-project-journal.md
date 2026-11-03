---
subjects:
  active: CAPRMEDIO_MODEL <+ Carrier/File
  passive:
  - CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Data Handling <+ Serialization
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/History/Journal > Event Record
  - CAPRMEDIO_MODEL <+ Project
  - CAPRMEDIO_MODEL <+ Journal
  - CAPRMEDIO_MODEL <+ Scope Unit
  - CAPRMEDIO_MODEL <+ Atom.Header.Role
version: 29
updated_at: 2026-11-02 18:35:20 +0400
relations: {}
atom_id: CA-D-339
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
tier: 3
role: Delivery
form: Decision
---
## Summary

Serialize the shared Project Journal

## Claim

### Prose Claim


the shared Project-control Work Journal's serialization.


the shared Project Work Journal **must** materialize its logical event table by serializing its ordered event Records as append-only NDJSON File Carrier segments **in** `.caprmedio_<project_name>/_journal/` **or** its registered subdirectories. these segments **must** remain Carriers of the same Journal, **not** separate Journals for Scope Units, Content Roles, workflows, **or** derived log views. describing the Journal as a table does **not** replace this registered serialization **or** require a database Carrier.

## Details

This serialization governs the Project-control Work Journal, not every runtime technical or business Journal. Runtime Journal Delivery may use configured local or remote databases and logging sinks.
