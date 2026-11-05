---
atom_id: CA-R-1938
ref_id: CA-R-1938
container:
  scope_unit: CA-SU-17
role: Requirement
form: Rule
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project
  - Scope Unit
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Settings
tier: 3
relations:
  depends_on:
  - CA-D-625
status: Active
version: 15
updated_at: 2026-11-02 19:44:26 +0400
carrier_destination:
  file:
    name: CA-R-1938-CONNECTOR_TOOLS-RULE--read-one-complete-scope-unit-declaration.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-17_FEATURE_CONNECTOR_TOOLS/04_requirement
current_scope_unit: CONNECTOR_TOOLS
claim_target_scope_unit: CONNECTOR_TOOLS
author: Anatoly Maslennikov
---
# Summary

Read one complete Scope Unit declaration

## Scope

Effect-free full Read of one explicit Scope Unit in a bound Project and current or expressly pinned/historical source view.

## Claim

the Scope Unit Read result **must** contain the complete authoritative declaration state for exactly one explicit canonical Scope Unit Name **in** the bound Project, with actual source-view evidence **and** no mutation. Read is independently callable **without** Query, Find, Modify **or** an enclosing Workflow.

identity **and** declaration authority **must** follow CA-R-1484-CORE_META_MODEL-RULE--establish-scope-units-through-project-structure-declarations **and** CA-R-1483-CORE_META_MODEL--define-authoritative-project-structure. a non-Project unit is its complete admitted Project Structure declaration; the Project root is its complete governing Project Settings `project` table **and** has no duplicate child declaration. return actual applicable carried properties, including declared binding values as data, **without** silently normalizing, repairing **or** inventing absent properties, IDs, Atom Versions **or** lifecycle. a full unit Read is **not** a recursive read of descendant units, owned Atoms, whole configuration **or** directory contents.

an unpinned explicit-name Read **must not** require a pre-known revision **or** state token. it returns actual exact source-state evidence. a supplied pin **or** requested historical view **must** be enforced exactly against available admitted authority; stale, missing, ambiguous **or** unsupported evidence **must not** be replaced by a guessed latest view, alias **or** successor.

invalid request/schema, missing **or** ambiguous target **or** source authority, denied read permission, stale evidence **or** backend failure **must** produce the applicable structured error under CA-D-625-CONNECTOR_TOOLS-ENG_DECISION--deliver-coherent-connector-interface. **not** found is **not** a successful empty full Read; ambiguity is **not** a guessed first result. required declaration, Carrier, history, Version, timestamp **and** lifecycle effects are **none**.

## Details

CA-D-627-CONNECTOR_TOOLS-ENG_DECISION--deliver-complete-scope-unit-read-data carries the concrete refinement; CA-M-378-CONNECTOR_TOOLS-ENG_DECISION--construct-a-complete-scope-unit-read-adapter, CA-O-212-CONNECTOR_TOOLS-ACTION--read-one-complete-scope-unit-declaration and CA-E-630-CONNECTOR_TOOLS-EVAL_CASE--verify-complete-scope-unit-reads own construction, operational behavior and future evaluation. These sources do not extend the Atom-only Read Action or establish an implemented Scope Unit route.
