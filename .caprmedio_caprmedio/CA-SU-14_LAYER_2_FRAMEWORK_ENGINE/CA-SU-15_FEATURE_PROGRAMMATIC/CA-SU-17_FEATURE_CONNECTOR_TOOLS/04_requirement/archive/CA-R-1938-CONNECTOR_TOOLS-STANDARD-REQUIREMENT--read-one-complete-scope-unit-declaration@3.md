---
atom_id: CA-R-1938
content_role: Requirement
type: Requirement
current_scope_unit: CONNECTOR_TOOLS
claim_target_scope_unit: CONNECTOR_TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 3
updated_at: "2026-10-13 01:54:26 +0400"
subjects:
  governs: "Tool"
  depends_on: ["Scope Unit", "Project", "Project Structure", "Project Settings"]
relations:
  relates_to: [CA-M-378, CA-E-630, CA-D-627, CA-O-212, CA-R-1936, CA-M-376, CA-E-628, CA-D-625, CA-R-1484, CA-D-442]
---
# Summary

Read one complete Scope Unit declaration

## Scope

Effect-free full Read of one explicit Scope Unit in a bound Project and current or expressly pinned/historical source view.

## Claim

The Scope Unit Read result **must** contain the complete authoritative declaration state for exactly one explicit canonical Scope Unit Name **in** the bound Project, with actual source-view evidence **and** no mutation. Read is independently callable **without** Query, Find, Modify **or** an enclosing Workflow.

Identity **and** declaration authority **must** follow CA-R-1484-CORE_META_MODEL-GENERAL-REQUIREMENT--establish-scope-units-through-project-structure-declarations **and** CA-R-1483-CORE_META_MODEL-CORE--define-authoritative-project-structure. A non-Project unit is its complete admitted Project Structure declaration; the Project root is its complete governing Project Settings `project` table **and** has no duplicate child declaration. Return actual applicable carried properties, including declared binding values as data, **without** silently normalizing, repairing **or** inventing absent properties, IDs, Atom Versions **or** lifecycle. A full unit Read is **not** a recursive read of descendant units, owned Atoms, whole configuration **or** directory contents.

An unpinned explicit-name Read **must not** require a pre-known revision **or** state token. It returns actual exact source-state evidence. A supplied pin **or** requested historical view **must** be enforced exactly against available admitted authority; stale, missing, ambiguous **or** unsupported evidence **must not** be replaced by a guessed latest view, alias **or** successor.

Invalid request/schema, missing **or** ambiguous target **or** source authority, denied read permission, stale evidence **or** backend failure **must** produce the applicable structured error under CA-D-625-CONNECTOR_TOOLS-CORE-DELIVERY--deliver-coherent-connector-interface. **not** found is **not** a successful empty full Read; ambiguity is **not** a guessed first result. Required declaration, Carrier, history, Version, timestamp **and** lifecycle effects are **none**.

## Details

CA-D-627-CONNECTOR_TOOLS-STANDARD-DELIVERY--deliver-complete-scope-unit-read-data carries the concrete refinement; CA-M-378-CONNECTOR_TOOLS-STANDARD-METHOD--construct-a-complete-scope-unit-read-adapter, CA-O-212-CONNECTOR_TOOLS-STANDARD-ACTION--read-one-complete-scope-unit-declaration and CA-E-630-CONNECTOR_TOOLS-STANDARD-QA_CASE--verify-complete-scope-unit-reads own construction, operational behavior and future evaluation. These sources do not extend the Atom-only Read Action or establish an implemented Scope Unit route.
