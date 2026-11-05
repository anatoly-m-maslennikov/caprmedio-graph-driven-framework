---
atom_id: CA-P-2047
ref_id: CA-P-2047
container:
  atom: CA-P-1966
role: Plan
form: Plan
label: Task
topics:
  main_subject: Subject
  dependencies:
  - Subject/Graph Node/Domain/Continuant/Atom
  - Subject
  - Subject/Graph Node/Domain/Continuant/Projection
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Plan'
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: Operator'
tier: 3
relations:
  is_decomposition_of:
  - CA-P-1966
status: Done
version: 6
updated_at: 2026-10-25 17:32:27 +0400
carrier_destination:
  file:
    name: 54-CA-P-2047-TASK--record-the-substance-field-decision.md
    path: .caprmedio_caprmedio/03_plan/done/18-CA-P-1959-EPIC--improve-entity-model-stage-2/done/8-CA-P-1966-EPIC--map-current-core-subject-origins/done
work_sequence_number: 54
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
---
# Summary

Record the Substance field decision

## Objective

Preserve the latest Operator decision as separate pinned evidence for later Subject mapping.

## Details

Estimated own work: 5 minutes. Record the actual answer: "we can keep atom.substance. claim/question/issue are just labels. we can rename them later". Atom.Substance is the shared dependent field. Claim, Question and Issue are role labels, not different dependent entities or allowed values of Substance. Preserve the owning Atom's Content Role. Record this clarification under stage2/operator.subject-decisions.2026-10-11.json without rewriting the frozen candidate or review reports. This decision can support a later candidate mapping for exact Atom/Claim; compound paths still require their own owner/domain evidence. Do not rename body headings or alter Summary, Substance, Scope, Details or source Subjects here. Grammar adoption and exact live mutation approval remain separate gates. Root owns this small authoring Task and Git.

Completion: the actual answer and its question/thread provenance are recorded in stage2/operator.subject-decisions.2026-10-11.json; SHA-256 743fd63f5c8c8ea19b0f1ffae1fa1d89d81504308c7f5345e2809fe7cef15ffc. The frozen candidate and original sources remain unchanged. Compound paths still need their own evidence, and body renaming stays Step 2. Receipt: stage2/task-2047.receipt.json.

### Definition of Done

Not Done if the actual answer or provenance is missing, the preserved inputs change, unsupported compound mappings are inferred, source content changes, or the recorded decision is presented as live migration approval.
