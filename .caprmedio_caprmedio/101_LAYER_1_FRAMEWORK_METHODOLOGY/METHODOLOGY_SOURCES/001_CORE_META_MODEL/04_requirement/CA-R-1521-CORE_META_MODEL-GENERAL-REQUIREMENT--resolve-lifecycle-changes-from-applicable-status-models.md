---
subjects:
  governs: "Entity/Node/Continuant/Atom/Content Role: Operations/Type: Workflow"
  depends_on:
    ["Entity", "Artifact", "Entity/Node/Continuant/Atom", "Atom/Content Role", "Type", "Status", "Structural Entity", "Entity/Node/Continuant/Scope Unit", "Container Atom", "Entity/Carrier"]
version: 10
updated_at: "2026-10-20T20:50:42.243Z"
relations: {"relates_to": ["CA-R-1519"]}
atom_id: "CA-R-1521"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
---
# Summary

Resolve lifecycle changes from applicable Status models

## Scope

Workflows that change an Entity's Status.

## Claim

a Workflow for changing an Entity's Status **must** admit **any** requested Status allowed by that Entity's applicable status model, rather than a fixed list built into the Workflow. For Atom creation **and** explicit Atom Status updates, **any** value admitted by the qualified Content Role/Type model is selectable **without** a required intermediate Status **or** transition matrix.

## Details

- resolve the model using the actual Entity kind **and**, for an Atom, its qualified Content Role **and** Type.
- apply the same model-driven rule **to** a Scope Unit **or** Atom Collection **when** a status model is defined for it.
- preserve authorization, expected-source/currentness, identity/collision, schema **and** applicable Carrier rules; support for **any** admitted Atom Status does **not** authorize arbitrary values **or** unrelated effects. Non-Atom Entity models retain their own applicable transition conditions.
- **every** admitted Status change of a folder-backed Plan, Workflow, **or** Step parent requires the same requested Status for recursively contained latest Plan **or** Operations descendants, except that requesting Done for the parent leaves contained latest Plans already Done unchanged **and** requests Canceled for every other contained latest Plan. requesting Archived selects **all** recursively contained latest Atoms, including Done descendants, for Archived under their own qualified models. There is no optional with/without-descendants mode. containment selects the descendants; references **to** Atoms outside that Carrier tree do **not** select them.
- compose separate independently admitted single-Atom Actions for the parent **and** each selected descendant. each Action checks its own qualified Status model **and** ordinary effect preconditions; an unsupported value is a refusal for that Atom, **not** an invented Status **or** a multi-target Action. this rule does **not** establish an atomic batch **or** rollback transaction.
- select **only** the latest Revision of each affected Atom. retain exact prior Revision bytes, including Version, Status **and** Updated At; an older archived Revision is **not** a cascade target. applicable placement keeps Current descendants inside the parent Carrier tree; Archived Plan Markdown follows CA-D-461's flat shared placement. retained-history subtrees **and** non-Atom assets may accompany an authorized matching Directory Carrier move byte-for-byte unchanged; they receive no invented Status update.
- a cascade is an authoring operation that writes each affected Atom's own admitted Status **and** Revision metadata. reading a containing folder **or** parent Status **must not** infer **or** override a descendant's carried Status.
- changing the admitted values **within** the supported model **must not** require a separate Workflow for **every** value. unsupported model capabilities **must** be reported rather than silently approximated.
- a missing status model **must not** be replaced with an invented universal Draft, Active, **or** Archived lifecycle for **all** Artifacts **and** Structural Entities.
