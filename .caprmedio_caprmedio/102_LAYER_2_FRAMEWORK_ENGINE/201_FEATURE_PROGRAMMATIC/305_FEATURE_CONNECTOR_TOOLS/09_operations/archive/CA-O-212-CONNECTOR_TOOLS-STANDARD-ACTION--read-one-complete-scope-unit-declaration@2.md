---
atom_id: CA-O-212
content_role: Operations
type: Action
current_scope_unit: CONNECTOR_TOOLS
claim_target_scope_unit: CONNECTOR_TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-13 01:54:26 +0400"
subjects:
  governs: "Tool"
  depends_on: ["Scope Unit", "Project", "Project Structure", "Project Settings"]
relations:
  relates_to: [CA-R-1938, CA-M-378, CA-E-630, CA-D-627, CA-R-1936, CA-M-376, CA-E-628, CA-D-625, CA-R-1484, CA-D-442]
---
# Summary

Read one complete Scope Unit declaration

## Operation

Read one complete Scope Unit declaration **means** the reusable effect-free connector Action that reads one explicit canonical Scope Unit Name under CA-R-1938-CONNECTOR_TOOLS-STANDARD-REQUIREMENT--read-one-complete-scope-unit-declaration **and** CA-D-627-CONNECTOR_TOOLS-STANDARD-DELIVERY--deliver-complete-scope-unit-read-data, independently of Query, Find **or** Modify **and** **without** an enclosing Workflow requirement.

### Inputs **and** preconditions

Require the common `read` request, exact logical identity, bound owning Project/source view, admitted declaration-schema evidence, read authorization **and** **any** supplied exact expected state. Project Settings owns root identity/state; Project Structure owns non-Project declarations. An unpinned current Read requires no pre-known revision **or** state token.

### Behavior **and** result

Resolve exactly the explicit identity **and** selected source view, mechanically check supplied schema/authorization/preconditions, **and** return its complete applicable declaration with unchanged values **and** presence/absence plus actual source-state evidence under the common result roles. Enforce a supplied pin **or** historical expectation exactly. Do **not** invoke Query implicitly, guess latest state, infer facts from a folder **or** read unrelated configuration, descendants **or** Atoms. Required effects are **none**.

### Stops

Return the declared structured error for invalid input/schema, missing **or** ambiguous target/authority, stale expected state, denied read permission **or** backend/unavailable historical evidence. Failure produces no successful empty full declaration, silent fallback, repair, new ID/Version, lifecycle transition **or** mutation authority.

## Details

CA-M-378-CONNECTOR_TOOLS-STANDARD-METHOD--construct-a-complete-scope-unit-read-adapter supplies the adapter convention; CA-E-630-CONNECTOR_TOOLS-STANDARD-QA_CASE--verify-complete-scope-unit-reads owns future checks. A real Run requires independently verified realization and applicable existing context/recording. This definition admits no new runnable route, wrapper Workflow, retry/resume or migration.
