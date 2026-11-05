---
atom_id: CA-O-211
ref_id: CA-O-211
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
status: Active
version: 14
updated_at: 2026-11-02 19:44:26 +0400
carrier_destination:
  file:
    name: CA-O-211-CONNECTOR_TOOLS-ACTION--query-declared-scope-units.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-17_FEATURE_CONNECTOR_TOOLS/09_operations
current_scope_unit: CONNECTOR_TOOLS
claim_target_scope_unit: CONNECTOR_TOOLS
author: Anatoly Maslennikov
---
# Summary

Query declared Scope Units

## Operation

Query declared Scope Units **means** the reusable effect-free connector Action that executes one explicit Scope Unit Query under CA-R-1937-CONNECTOR_TOOLS-RULE--query-declared-scope-units **and** CA-D-626-CONNECTOR_TOOLS-ENG_DECISION--deliver-declared-scope-unit-query-data, independently of Read **or** Modify **and** **without** a mandatory enclosing Workflow.

### Inputs **and** preconditions

require the common `query` request, explicit canonical-name frontier **and** predicates, bound owning Project/source view, applicable declaration-schema evidence, read authorization **and** **any** supplied exact expected state. the source authority is Project Settings for the root **and** Project Structure for non-Project declarations. do **not** infer identity **or** authority from physical nesting **or** a Projection.

### Behavior **and** result

validate the admitted shape **and** bindings, resolve the explicit frontier uniquely, check the selected declaration graph **and** apply the supplied predicates **without** defaults. return the exact empty, singular **or** multiple matching identities **and** requested facts, deterministic ordering, observed source-state evidence **and** truthful coverage under the common result roles. Query does **not** return full declarations **or** call Read/Modify implicitly. required effects are **none**.

### Stops

return the declared structured errors for invalid input, unresolved **or** ambiguous frontier, invalid schema/graph, stale expected state, denied read permission **or** backend/incomplete evidence. no error becomes successful empty coverage, guessed historical state, a repaired declaration **or** effect authority.

## Details

CA-M-377-CONNECTOR_TOOLS-ENG_DECISION--construct-a-declared-scope-unit-query-adapter is the construction convention and CA-E-629-CONNECTOR_TOOLS-EVAL_CASE--verify-declared-scope-unit-queries owns future checks. A real Run still requires an independently verified realization and applicable existing context/recording. This Action definition introduces no runtime route, new Workflow wrapper, retry/resume or migration.
