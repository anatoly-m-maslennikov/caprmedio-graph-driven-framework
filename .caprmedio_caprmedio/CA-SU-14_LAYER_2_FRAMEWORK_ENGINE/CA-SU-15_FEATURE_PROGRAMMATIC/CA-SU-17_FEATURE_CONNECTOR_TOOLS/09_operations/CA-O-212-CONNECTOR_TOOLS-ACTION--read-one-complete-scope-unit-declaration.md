---
atom_id: CA-O-212
ref_id: CA-O-212
container:
  scope_unit: CA-SU-17
role: Operations
form: Action
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project
  - Scope Unit
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Settings
tier: 3
relations:
  depends_on:
  - CA-R-1938
  - CA-M-378
  - CA-E-630
  - CA-D-627
status: Active
version: 14
updated_at: 2026-11-02 19:44:26 +0400
carrier_destination:
  file:
    name: CA-O-212-CONNECTOR_TOOLS-ACTION--read-one-complete-scope-unit-declaration.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-17_FEATURE_CONNECTOR_TOOLS/09_operations
current_scope_unit: CONNECTOR_TOOLS
claim_target_scope_unit: CONNECTOR_TOOLS
author: Anatoly Maslennikov
---
# Summary

Read one complete Scope Unit declaration

## Operation

Read one complete Scope Unit declaration **means** the reusable effect-free connector Action that reads one explicit canonical Scope Unit Name under CA-R-1938-CONNECTOR_TOOLS-RULE--read-one-complete-scope-unit-declaration **and** CA-D-627-CONNECTOR_TOOLS-ENG_DECISION--deliver-complete-scope-unit-read-data, independently of Query, Find **or** Modify **and** **without** an enclosing Workflow requirement.

### Inputs **and** preconditions

require the common `read` request, exact logical identity, bound owning Project/source view, admitted declaration-schema evidence, read authorization **and** **any** supplied exact expected state. Project Settings owns root identity/state; Project Structure owns non-Project declarations. an unpinned current Read requires no pre-known revision **or** state token.

### Behavior **and** result

resolve exactly the explicit identity **and** selected source view, mechanically check supplied schema/authorization/preconditions, **and** return its complete applicable declaration with unchanged values **and** presence/absence plus actual source-state evidence under the common result roles. enforce a supplied pin **or** historical expectation exactly. do **not** invoke Query implicitly, guess latest state, infer facts from a folder **or** read unrelated configuration, descendants **or** Atoms. required effects are **none**.

### Stops

return the declared structured error for invalid input/schema, missing **or** ambiguous target/authority, stale expected state, denied read permission **or** backend/unavailable historical evidence. failure produces no successful empty full declaration, silent fallback, repair, new ID/Version, lifecycle transition **or** mutation authority.

## Details

CA-M-378-CONNECTOR_TOOLS-ENG_DECISION--construct-a-complete-scope-unit-read-adapter supplies the adapter convention; CA-E-630-CONNECTOR_TOOLS-EVAL_CASE--verify-complete-scope-unit-reads owns future checks. A real Run requires independently verified realization and applicable existing context/recording. This definition admits no new runnable route, wrapper Workflow, retry/resume or migration.
