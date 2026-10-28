---
subjects:
  governs: 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Plan.Autonomous Confidence Threshold'
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Plan/Type: Plan'
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control/Decision Confidence
  - Subject/CAPRMEDIO/Carrier/File
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Plan.Definition of Done'
version: 21
updated_at: 2026-10-27 19:59:25 +0400
relations: {}
atom_id: CA-D-472
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 3
type: Eng Decision
---
# Summary

Serialize explicit Plan confidence overrides

## Scope

explicit Plan Autonomous Confidence Threshold overrides in Plan Atom Markdown File Carriers.

## Claim

an explicit Plan Autonomous Confidence Threshold override **must** use the top-level integer frontmatter field `autonomous_confidence_threshold` **in** that Plan Atom's own mandatory Markdown File Carrier.

- a Hub uses that same file, **not** a separately identified Objective **or** Epic settings file.
- omit an unselected override **without** copying its inherited value; the mandatory file requirement does **not** turn inheritance into a local selection.
- retain an explicit override even **when** it equals the inherited value.
- `epic_overrides` is **not** an alternative canonical encoding.

## Details
