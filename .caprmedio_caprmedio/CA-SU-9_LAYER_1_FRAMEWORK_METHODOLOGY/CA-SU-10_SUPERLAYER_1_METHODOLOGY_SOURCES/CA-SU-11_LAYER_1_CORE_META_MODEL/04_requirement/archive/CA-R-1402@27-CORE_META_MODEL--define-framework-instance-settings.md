---
subjects:
  governs: Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings
  depends_on:
  - Entity/Object/Continuant/Governing Objects/Governing Configuration
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project
  - Entity/Object/Continuant/Actor/Operator
version: 27
updated_at: 2026-10-29 10:13:48 +0400
relations: {}
atom_id: CA-R-1402@27
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
type: Entity Definition
---
## Summary

Define Framework Instance Settings

## Claim scope

Framework Instance Settings for a CAPRMEDIO Framework Instance serving a Project.

## Claim

Authority Modes groups the Project mode and default Scope Unit mode, whose admitted values are strict and casual under CA-R-1430; per-Scope overrides remain in Project Structure. Interaction.Reporting Mode selects silent or verbose under CA-R-1628. An optional explicit Implementation Retry Limit preserves default resolution when absent; the logical Property does not introduce another TOML section or duplicate CA-D-447's carrier key.

the Term Framework Instance Settings **means** the authoritative Artifact containing explicit Operator-selected behavior **and** configuration choices for **`=1`** CAPRMEDIO Framework Instance serving **`=1`** Project.

Framework Settings is a structured configuration group. This declares no direct scalar at the group; its declared children keep their field-specific requirements. It introduces no generic Configuration field.

### Formal claim

```text
Project.Framework Settings{0}
Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings.Authority Modes{0}
Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings.Authority Modes.Project Authority Mode[string]{1}
Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings.Authority Modes.Default Scope Unit Authority Mode[string]{1}
Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings.Interaction.Reporting Mode[string]{1}
Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings.Interaction.Reporting Mode: silent
Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings.Interaction.Reporting Mode: verbose
Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings.Implementation Retry Limit[int]{0..1}
```
