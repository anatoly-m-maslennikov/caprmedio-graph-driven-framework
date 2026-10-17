---
subjects:
  governs: "Entity/Continuant/Object/Atom/Content Role: Operations/Type: Workflow"
  depends_on:
    ["Entity", "Artifact", "Entity/Continuant/Object/Atom", "Atom/Content Role", "Type", "Status", "Structural Entity", "Entity/Continuant/Object/Scope Unit", "Container Atom", "Entity/Carrier"]
version: 8
updated_at: "2026-10-15 23:46:29 +0400"
relations: {"relates_to": ["CA-R-1519"]}
atom_id: "CA-R-1521"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1521-CORE_META_MODEL-GENERAL-REQUIREMENT--resolve-lifecycle-changes-from-applicable-status-models.md
  source_atom_id: CA-R-1521
  source_atom_revision: 8
  source_sha256: 8d16aee2c786b7e882eb422c731126cd464c573aceb9d4738dfc75f09d5e3418
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
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
- **every** admitted Status change of a folder-backed Plan, Workflow, **or** Step parent requires the same requested Status for **all** recursively contained Plan **or** Operations descendants, for **every** admitted target Status, **not** only Archived. containment selects the descendants; references **to** Atoms outside that Carrier tree do **not** select them.
- compose separate independently admitted single-Atom Actions for the parent **and** each selected descendant. each Action checks its own qualified Status model **and** ordinary effect preconditions; an unsupported value is a refusal for that Atom, **not** an invented Status **or** a multi-target Action. this rule does **not** establish an atomic batch **or** rollback transaction.
- select **only** the latest Revision of each affected Atom. retain exact prior Revision bytes, including Version, Status **and** Updated At; an older archived Revision is **not** a cascade target. applicable placement keeps descendants inside the parent Carrier tree, including **when** Archived.
- a cascade is an authoring operation that writes each affected Atom's own admitted Status **and** Revision metadata. reading a containing folder **or** parent Status **must not** infer **or** override a descendant's carried Status.
- changing the admitted values **within** the supported model **must not** require a separate Workflow for **every** value. unsupported model capabilities **must** be reported rather than silently approximated.
- a missing status model **must not** be replaced with an invented universal Draft, Active, **or** Archived lifecycle for **all** Artifacts **and** Structural Entities.
