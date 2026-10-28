---
version: 20
updated_at: 2026-10-27 19:59:30 +0400
relations:
  child_of:
  - CA-M-263
  evaluation_for:
  - CA-M-263
subjects:
  governs: 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-209
status: Active
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: caprmedio
type: Policy
tier: 2
---
# Evaluate operator comprehension

## Claim checked

the intended Operator can identify the represented meaning, available controls, **and** material consequences.

## Applicable conditions

apply **when** governed meaning is exposed **to** a Project Operator.

## Acceptance

pass **only** **when** the intended Operator can identify the represented meaning, the controls available **to** them, **and** the material consequences of using those controls.

## Failure

treat the representation as failed for that Operator **and** report **every** unidentified meaning, control, **or** material consequence.
