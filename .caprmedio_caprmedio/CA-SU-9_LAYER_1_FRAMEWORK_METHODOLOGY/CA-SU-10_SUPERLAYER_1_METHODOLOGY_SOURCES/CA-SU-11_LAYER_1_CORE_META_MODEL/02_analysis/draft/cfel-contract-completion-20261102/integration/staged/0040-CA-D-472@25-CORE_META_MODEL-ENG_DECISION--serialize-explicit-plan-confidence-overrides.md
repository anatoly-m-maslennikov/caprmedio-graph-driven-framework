---
subjects:
  active: 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan.Autonomous Confidence Threshold'
  passive:
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan/Type: Plan'
  - Entity/Aspect/Engineering/Execution Control/Decision Confidence
  - Carrier/File
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan.Content.Definition of Done'
version: 25
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-D-472@25
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
tier: 3
role: Delivery
form: Decision
---
## Summary

Serialize explicit Plan confidence overrides

## Claim scope

explicit Plan Autonomous Confidence Threshold overrides in Plan Atom Markdown File Carriers.

## Claim

an explicit Plan Autonomous Confidence Threshold override **must** use the top-level integer frontmatter field `autonomous_confidence_threshold` **in** that Plan Atom's own mandatory Markdown File Carrier.

- a Hub uses that same file, **not** a separately identified Objective **or** Epic settings file.
- omit an unselected override **without** copying its inherited value; the mandatory file requirement does **not** turn inheritance into a local selection.
- retain an explicit override even **when** it equals the inherited value.
- `epic_overrides` is **not** an alternative canonical encoding.
