---
atom_id: CA-P-096
ref_id: CA-P-096
container:
  scope_unit: CA-SU-00
role: Plan
form: Plan
label: Task
topics:
  main_subject: Subject/Graph Node/Engineering/Implementation Evaluation
  dependencies:
  - Subject/Graph Node/Engineering/Continuant/Carrier/Database Carrier
  - Subject/Graph Node/Engineering/Implementation
tier: 3
relations:
  derived_from:
  - CA-A-042
  - CA-A-062
status: Active
version: 9
updated_at: 2026-10-25 17:32:27 +0400
cce_version: cce_1
cce_form: obligation
autonomous_confidence_threshold: 98
author: Anatoly Maslennikov
current_scope_unit: caprmedio
---
# Select the derived Graph database through a parity spike

WHEN Graph App implementation needs a database commitment, THE Assignee MUST
execute the parity spike specified by `CA-A-042` and record one reversible
engine selection or an evidence-backed no-selection result.

## Scope

The rebuildable local database fed by authoritative Atoms and complete Work
Journals, its typed direct-relation representation, derived data stages, local
service boundary, and static-export boundary.

## Definition of Done

THE Task is NOT DONE IF (the same pinned source manifest, relation rules, and
acceptance scenarios are not run for the retained SQLite, LadybugDB,
SurrealDB, and TypeDB mechanisms OR complete Journal replay and source-frontier
rebuild are omitted OR the result uses one opaque weighted score OR the chosen
engine can establish authority independently of source files OR exact versions,
measures, accepted losses, fallback, and reopen conditions are absent OR a
database is selected from documentation alone).

## Details

Preserve SQLite plus LadybugDB as a conditional dual-engine option only if the
single-engine spike proves that one protected capability cannot otherwise be
met. Recheck current engine release and compatibility evidence when executing
the spike. Keep the database disposable: deletion followed by full rebuild must
restore the accepted query and publication results.
