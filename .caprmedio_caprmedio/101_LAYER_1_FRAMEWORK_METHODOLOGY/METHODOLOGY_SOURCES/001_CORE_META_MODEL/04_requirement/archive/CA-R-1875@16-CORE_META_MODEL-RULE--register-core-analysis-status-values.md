---
atom_id: CA-R-1875@16
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Analysis.Status'
  depends_on:
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Analysis'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Analysis/Type'
  - Entity/Object/Continuant/Governing Objects/Atom.Status
  - Entity/Object/Continuant/Selection//Extension Sources
  - Entity/Object/Continuant/Structural Unit/Scope Unit//PROJECT_CONFIGURATION
version: 16
updated_at: 2026-10-29 07:17:19 +0400
relations: {}
tier: 2
type: Rule
---
# Summary

Register Core Analysis Status Values

## Scope

the default Status value domain of Analysis Atoms with Type Analysis Report or Rationale.

## Claim

the Core Analysis Status model **must** inherit the allowed values of Atom.Status and add Done. That Content Role Status model applies to Analysis Atoms with Type Analysis Report or Rationale. An admitted Extension or Project Configuration **may** add values under the applicable complete Content Role and Type path; it **must not** remove inherited values.

## Details

this Status belongs to the Analysis Atom itself. It does **not** define a Status transition, carrier placement, setting, or a Workflow, Step, or Action Run outcome, receipt, retry state, result, or completion state. CA-R-1727 defines the meanings of Draft and Done for Analysis and the meaning of its archival.

