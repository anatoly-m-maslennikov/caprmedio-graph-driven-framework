---
subjects:
  active: Carrier/File
  passive:
  - Aspects <+ Engineering <+ Data Handling <+ Serialization
  - Entity/Object/Continuant/History/Journal > Event Record
  - Project
  - Journal
  - Scope Unit
  - Entity/Object/Continuant/Governing Objects/Atom/Content Role
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
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/07_delivery/CA-D-339-PROJECT_CONFIGURATION-ENG_DECISION--serialize-the-shared-project-journal.md
  source_atom_id: CA-D-339
  source_atom_revision: 29
  source_sha256: 0de87e488104341e5bfb7420724d2b3f0eba1ee0c9af514e3b0c3c2483f76564
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Serialize the shared Project Journal

## Claim scope

the shared Project-control Work Journal's serialization.

## Claim

the shared Project Work Journal **must** materialize its logical event table by serializing its ordered event Records as append-only NDJSON File Carrier segments **in** `.caprmedio_<project_name>/_journal/` **or** its registered subdirectories. these segments **must** remain Carriers of the same Journal, **not** separate Journals for Scope Units, Content Roles, workflows, **or** derived log views. describing the Journal as a table does **not** replace this registered serialization **or** require a database Carrier.

## Details

This serialization governs the Project-control Work Journal, not every runtime technical or business Journal. Runtime Journal Delivery may use configured local or remote databases and logging sinks.
