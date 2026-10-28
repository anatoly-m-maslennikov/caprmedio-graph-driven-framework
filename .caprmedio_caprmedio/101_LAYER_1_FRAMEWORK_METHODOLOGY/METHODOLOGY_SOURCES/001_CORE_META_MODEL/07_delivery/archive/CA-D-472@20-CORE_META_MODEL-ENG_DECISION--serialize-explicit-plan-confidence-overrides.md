---
subjects:
  governs: 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Plan.Autonomous Confidence Threshold'
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Plan/Type: Plan'
  - Subject/Graph Node/Engineering/Execution Control/Decision Confidence
  - Subject/Graph Node/Carrier/File
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Plan.Definition of Done'
version: 20
updated_at: 2026-10-27 06:04:45 +0400
relations: {}
atom_id: CA-D-472@20
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
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
