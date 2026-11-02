---
subjects:
  active: Carrier/File
  passive:
  - Entity/Aspect/Engineering/Data Handling/Serialization
  - Entity/Object/Continuant/History/Journal > Event Record
  - Project
  - Journal
  - Scope Unit
  - Entity/Object/Continuant/Governing Objects/Atom/Content Role
version: 27
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-D-339@27
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Archived
tier: 3
role: Delivery
form: Decision
---
## Summary

Serialize the shared Project Journal

## Claim scope

the shared Project-control Work Journal's serialization.

## Claim

the shared Project Work Journal **must** materialize its logical event table by serializing its ordered event Records as append-only NDJSON File Carrier segments **in** `.caprmedio_<project_name>/_journal/` **or** its registered subdirectories. these segments **must** remain Carriers of the same Journal, **not** separate Journals for Scope Units, Content Roles, workflows, **or** derived log views. describing the Journal as a table does **not** replace this registered serialization **or** require a database Carrier.

## Details

This serialization governs the Project-control Work Journal, not every runtime technical or business Journal. Runtime Journal Delivery may use configured local or remote databases and logging sinks.
