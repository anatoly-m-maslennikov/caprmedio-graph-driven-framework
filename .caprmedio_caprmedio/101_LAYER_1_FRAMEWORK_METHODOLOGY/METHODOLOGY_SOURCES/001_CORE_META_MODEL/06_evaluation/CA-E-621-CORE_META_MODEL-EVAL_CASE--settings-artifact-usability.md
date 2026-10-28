---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Framework Settings
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Settings
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Structure
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Framework Settings.Authority Modes
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
version: 32
updated_at: 2026-10-27 19:59:38 +0400
relations:
  evaluation_for:
  - CA-R-1052
  - CA-R-1402
  - CA-R-1750
  - CA-R-1430
atom_id: CA-E-621
content_role: Evaluation
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
type: Eval Case
tier: 3
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
