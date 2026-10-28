---
atom_id: CA-R-1875@14
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Analysis.Status'
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Analysis'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Analysis/Type'
  - Subject/Graph Node/Domain/Continuant/Atom.Status
  - Subject/Graph Node/Domain/Continuant/Selection//Extension Sources
  - Subject/Graph Node/Domain/Continuant/Scope Unit//PROJECT_CONFIGURATION
version: 14
updated_at: 2026-10-26 05:59:45 +0400
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

