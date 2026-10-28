---
atom_id: CA-O-211@12
content_role: Operations
type: Action
current_scope_unit: CONNECTOR_TOOLS
claim_target_scope_unit: CONNECTOR_TOOLS
status: Archived
author: Anatoly Maslennikov
version: 12
updated_at: 2026-10-27 06:04:45 +0400
subjects:
  governs: Subject/Graph Node/Domain/Continuant/Scope Unit
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Project
  - Subject/Graph Node/Domain/Continuant/Project.Structure
  - Subject/Graph Node/Domain/Continuant/Project.Settings
relations: {}
tier: 3
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
