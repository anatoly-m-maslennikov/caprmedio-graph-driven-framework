---
subjects:
  governs: Subject/Domain/Node/Continuant/Project.Framework Settings.Parameter Resolution Validation
  depends_on:
  - Subject/Domain/Node/Continuant/Project.Framework Settings
  - Default Settings
  - Subject/Domain/Node/Continuant/Project
  - Subject/Engineering/Carrier
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Evaluation'
version: 16
updated_at: 2026-10-24 02:14:24 +0400
relations:
  evaluation_for:
  - CA-D-407
  - CA-D-408
  - CA-M-279
  - CA-R-1441
atom_id: CA-E-450
content_role: Evaluation
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
type: Policy
tier: 5
---
# Summary
Validate framework parameter fallback

## Scope
Framework parameter resolution across explicit parameters, Framework Instance Settings, **and** Default Settings.

## Claim

the Evaluation **must** reject framework parameter resolution **if** **any** of the following falsifying conditions holds:

- a valid explicit parameter loses **to** a Default Settings value;
- a missing parameter fails **to** inherit its available valid default, including **when** another parameter **in** the same section is explicit;
- a valid explicit `false`, `0`, **or** empty value is mistaken for an absent parameter;
- an invalid explicit value is accepted **or** replaced by a fallback value;
- an invalid selected default is accepted, **or** a required parameter missing from Framework Instance Settings **and** Default Settings receives an invented value;
- an optional parameter absent from Framework Instance Settings **and** Default Settings is rejected solely for its absence;
- resolution reads another Project's instance selections **or** writes inherited values back as explicit selections;
- unchanged input values resolve differently on a repeated read;
- Default Settings uses an unregistered Carrier location **or** a parameter representation that differs from its registered Framework Instance Settings representation.

use the registered parameter constraints for the cases; **when** the current parameter catalog lacks a Boolean, zero-valued, **or** empty-valued example, use isolated test-fixture parameters **without** adding them **to** authoritative Settings.

## Details
