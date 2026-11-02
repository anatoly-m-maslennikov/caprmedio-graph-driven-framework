---
atom_id: CA-A-1268
content_role: Analysis
type: Specification Proposal
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
status: Active
author: Anatoly Maslennikov
subjects:
  governs: Model
version: 1
updated_at: 2026-10-29 00:04:17 +0400
relations: {}
tier: 3
---
# Summary

Name the root Model

## Decision

The root is Model, not Formal Model. Rename the root label and proposed canonical selectors from Formal Model::... to Model::..., preserving their structure and meaning. The storage fields subjects.governs and subjects.depends_on retain their names. The existing Subject definition is not silently turned into the new Model definition. Historical proposal records and the completed FPF report retain their recorded wording.

## State

Proposal and prepared Draft updates only. Current methodology, governing configuration, historical reports and implementation are unchanged.
