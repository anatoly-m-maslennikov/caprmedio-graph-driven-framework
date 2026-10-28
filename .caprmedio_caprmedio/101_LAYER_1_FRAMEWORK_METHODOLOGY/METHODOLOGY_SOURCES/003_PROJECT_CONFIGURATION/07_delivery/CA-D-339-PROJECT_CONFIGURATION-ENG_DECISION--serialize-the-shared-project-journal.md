---
subjects:
  governs: Subject/CAPRMEDIO/Carrier/File
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Data Handling/Serialization
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal.Record
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role
version: 24
updated_at: 2026-10-27 19:59:23 +0400
relations: {}
atom_id: CA-D-339
content_role: Delivery
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
author: Anatoly Maslennikov
tier: 3
type: Eng Decision
---
# Summary

Serialize the shared Project Journal

## Scope

the shared Project-control Work Journal's serialization.

## Claim

the shared Project Work Journal **must** materialize its logical event table by serializing its ordered event Records as append-only NDJSON File Carrier segments **in** `.caprmedio_<project_name>/_journal/` **or** its registered subdirectories. these segments **must** remain Carriers of the same Journal, **not** separate Journals for Scope Units, Content Roles, workflows, **or** derived log views. describing the Journal as a table does **not** replace this registered serialization **or** require a database Carrier.

## Details

This serialization governs the Project-control Work Journal, not every runtime technical or business Journal. Runtime Journal Delivery may use configured local or remote databases and logging sinks.
