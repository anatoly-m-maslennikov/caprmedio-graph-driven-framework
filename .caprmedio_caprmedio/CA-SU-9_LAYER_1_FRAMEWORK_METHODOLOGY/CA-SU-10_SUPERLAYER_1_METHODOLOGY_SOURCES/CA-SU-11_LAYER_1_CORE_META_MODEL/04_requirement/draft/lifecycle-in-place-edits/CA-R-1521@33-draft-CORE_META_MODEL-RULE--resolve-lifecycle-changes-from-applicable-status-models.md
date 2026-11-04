---
subjects:
  active: CAPRMEDIO_MODEL <+ Atom/(.Header.Role:=Operations)/Workflow
  passive:
  - CAPRMEDIO_MODEL <+ Entity
  - CAPRMEDIO_MODEL <+ Term//Artifact
  - CAPRMEDIO_MODEL <+ Atom
  - CAPRMEDIO_MODEL <+ Atom.Header.Role
  - CAPRMEDIO_MODEL <+ Scope Unit.order.ordered
  - CAPRMEDIO_MODEL <+ Atom.Header.Status
  - CAPRMEDIO_MODEL <+ Scope Unit
  - CAPRMEDIO_MODEL <+ Carrier
version: 33
updated_at: 2026-11-03 20:57:46 +0400
relations: {}
atom_id: CA-R-1521@33-draft
status: Draft
tier: 2
role: Requirement
form: Rule
---
## Summary

Resolve lifecycle changes from applicable Status models

## Claim

A Workflow that changes an Entity's Status **must** resolve the Entity's applicable status model and admit every requested Status allowed by that model **within** the selected operation's declared source/target Status group and boundary. It must not use a fixed universal list, required intermediate Status, or transition matrix. A model-allowed request outside that operation scope is refused or handed off to a separately admitted operation; it is not invoked implicitly. Atom creation and explicit Atom Status updates use the qualified Content Role/Type model, with no hardcoded exclusion inside the admitted group.

## Details

- Resolve the model from the actual Entity kind and, for an Atom, its qualified Content Role and Type. Apply the same rule to a Scope Unit or Atom Collection when its model defines Status values. Preserve authorization, expected-source/currentness, identity/collision, schema, Carrier, and other ordinary effect checks; a model-admitted Status does not authorize arbitrary values or unrelated effects. Non-Atom Entity models retain their own conditions.
- **Every** admitted Status change of a folder-backed Plan, Workflow, **or** Step parent requires the same requested Status for recursively contained latest Plan **or** Operations descendants, except that a containing Plan Atom whose requested Status is Done **or** Canceled preserves every recursively contained latest Plan already Done **or** Canceled and requests Canceled for every other recursively contained latest Plan. After the cascade, every selected latest Plan must be Done **or** Canceled; mixed terminal statuses are allowed, and no contained Plan is forced to match the parent's requested Status merely because the parent is Done **or** Canceled. For non-Plan parents, retain the existing Done exception: requesting Done for the parent leaves contained latest Plans already Done unchanged and requests Canceled for every other contained latest Plan. Requesting Archived selects **all** recursively contained latest Atoms, including Done descendants, for Archived under their own qualified models. There is no optional with/without-descendants mode. Containment selects the descendants; references **to** Atoms outside that Carrier tree do **not** select them.
- Compose separate independently admitted single-Atom Actions for the parent and each selected descendant. Each Action checks its own qualified Status model and ordinary effect preconditions; an unsupported value is refused for that Atom, not invented or applied by a multi-target Action. On any failure, stop and return completed outputs and errors; do not retry, replay, or roll back. This rule does not establish an atomic batch transaction.
- A cascade writes each affected Atom's own admitted Status. Separate versioned publication remains governed by CA-R-1432 and CA-R-1788.
- Select **only** the latest Version of each affected Atom. Retain exact prior Version bytes, including Version, Status, and Updated At, through Git; an older Archived Version is not a cascade target. A status-only in-place edit preserves Version and Updated At and creates no Archived predecessor or successor. Applicable placement keeps Current descendants inside the parent Carrier tree; Archived Plan Markdown follows CA-D-461's flat shared placement. Retained-history subtrees and non-Atom assets may accompany an authorized matching Directory Carrier move byte-for-byte unchanged and receive no invented Status update.
- A non-container-only Workflow selects no contained descendants. A container-aware Workflow applies the container and cascade behavior above; there is no optional with/without-descendants mode. Reading a containing folder or parent Status must not infer or override a descendant's carried Status. An ancestor-only move that leaves an Atom's own bytes, properties/metadata, direct owner, and placement relative to that owner unchanged changes only its repository locator; it preserves Version and Updated At and is not an edit to that Atom.
- Changing admitted values within the supported model must not require a separate Workflow for every value. Report unsupported model capabilities rather than silently approximating them. A missing status model must not be replaced with an invented universal Draft, Active, or Archived lifecycle for all Artifacts and Structural Entities.
