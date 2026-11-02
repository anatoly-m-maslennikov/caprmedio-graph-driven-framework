---
atom_id: CA-O-212@7
content_role: Operations
type: Action
current_scope_unit: CONNECTOR_TOOLS
claim_target_scope_unit: CONNECTOR_TOOLS
status: Archived
author: Anatoly Maslennikov
version: 7
updated_at: 2026-10-24 10:48:25 +0400
subjects:
  governs: Subject/Domain/Node/Continuant/Scope Unit
  depends_on:
  - Subject/Domain/Node/Continuant/Project
  - Subject/Engineering/Project Structure Declaration
  - Subject/Engineering/Project Settings Snapshot
relations:
  relates_to:
  - CA-R-1938
  - CA-M-378
  - CA-E-630
  - CA-D-627
  - CA-R-1936
  - CA-M-376
  - CA-E-628
  - CA-D-625
  - CA-R-1484
  - CA-D-442
tier: 3
---
# Summary

Read one complete Scope Unit declaration

## Operation

Read one complete Scope Unit declaration **means** the reusable effect-free connector Action that reads one explicit canonical Scope Unit Name under CA-R-1938-CONNECTOR_TOOLS-REQUIREMENT--read-one-complete-scope-unit-declaration **and** CA-D-627-CONNECTOR_TOOLS-ENG_DECISION--deliver-complete-scope-unit-read-data, independently of Query, Find **or** Modify **and** **without** an enclosing Workflow requirement.

### Inputs **and** preconditions

require the common `read` request, exact logical identity, bound owning Project/source view, admitted declaration-schema evidence, read authorization **and** **any** supplied exact expected state. Project Settings owns root identity/state; Project Structure owns non-Project declarations. an unpinned current Read requires no pre-known revision **or** state token.

### Behavior **and** result

resolve exactly the explicit identity **and** selected source view, mechanically check supplied schema/authorization/preconditions, **and** return its complete applicable declaration with unchanged values **and** presence/absence plus actual source-state evidence under the common result roles. enforce a supplied pin **or** historical expectation exactly. do **not** invoke Query implicitly, guess latest state, infer facts from a folder **or** read unrelated configuration, descendants **or** Atoms. required effects are **none**.

### Stops

return the declared structured error for invalid input/schema, missing **or** ambiguous target/authority, stale expected state, denied read permission **or** backend/unavailable historical evidence. failure produces no successful empty full declaration, silent fallback, repair, new ID/Version, lifecycle transition **or** mutation authority.

## Details

CA-M-378-CONNECTOR_TOOLS-METHOD--construct-a-complete-scope-unit-read-adapter supplies the adapter convention; CA-E-630-CONNECTOR_TOOLS-QA_CASE--verify-complete-scope-unit-reads owns future checks. A real Run requires independently verified realization and applicable existing context/recording. This definition admits no new runnable route, wrapper Workflow, retry/resume or migration.
