---
atom_id: CA-R-1875@6
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: General
global_tier: 10
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: 'Entity/Node/Continuant/Atom/Content Role: Analysis.Status'
  depends_on:
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Analysis'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Analysis/Type'
  - Subject/Domain/Node/Continuant/Atom.Status
  - Extension
  - Project Configuration
version: 6
updated_at: 2026-10-23 03:06:32 +0400
relations:
  relates_to:
  - CA-R-1232
  - CA-R-1337
  - CA-R-1664
  - CA-R-1727
  - CA-R-1308
  - CA-R-1312
  - CA-R-1313
---
# Summary

Register Core Analysis Status Values

## Scope

the default Status value domain of Analysis Atoms with Type Analysis Report or Rationale.

## Claim

the Core Analysis Status model **must** inherit the allowed values of Atom.Status and add Done. That Content Role Status model applies to Analysis Atoms with Type Analysis Report or Rationale. An admitted Extension or Project Configuration **may** add values under the applicable complete Content Role and Type path; it **must not** remove inherited values.

## Details

this Status belongs to the Analysis Atom itself. It does **not** define a Status transition, carrier placement, setting, or a Workflow, Step, or Action Run outcome, receipt, retry state, result, or completion state. CA-R-1727 defines the meanings of Draft and Done for Analysis and the meaning of its archival.

