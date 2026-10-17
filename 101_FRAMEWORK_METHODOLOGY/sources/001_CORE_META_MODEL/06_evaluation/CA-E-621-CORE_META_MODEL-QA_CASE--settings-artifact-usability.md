---
subjects:
  governs: "Entity/Continuant/Object/Project.Framework Settings"
  depends_on:
    ["Entity/Continuant/Object/Project.Settings", "Entity/Continuant/Object/Project.Structure", "Authority Mode", "Entity/Continuant/Actor/Type: Operator"]
version: 24
updated_at: "2026-10-15 18:50:35 +0000"
relations:
  evaluation_for:
    - CA-R-1052
    - CA-R-1402
    - CA-R-1750
    - CA-R-1430
atom_id: "CA-E-621"
content_role: "Evaluation"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "QA Case"
global_tier: 11
---
# Summary

Settings Artifact Usability

## Scope

the Operator has no undocumented Framework knowledge **and** **must not** edit the Framework Catalog.

## Claim

an Operator unfamiliar with the repository can configure framework-instance behavior, including default **and** Project Authority Modes, through Framework Instance Settings **and** Project initialization inputs through Project Settings using the owning Settings Artifacts **and** their in-file documentation, while recognizing authoritative Project Structure as the separate owner of Scope Unit declarations **and** explicit per-unit Authority Mode overrides. no structural Projection is required **to** make these choices.

## Details

### Acceptance criteria

**every** intended change is made through its owning Settings Artifact **or** Project Structure, **and** **`>=90`**% of classifications correctly distinguish project choices from methodology definitions.

### Failure disposition

record a Concern for **every** misleading **or** missing setting instruction **and** stop settings-usability readiness **until** it is corrected.
