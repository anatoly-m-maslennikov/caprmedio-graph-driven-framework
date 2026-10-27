---
atom_id: CA-P-2308
content_role: Plan
type: Plan
label: Task
work_sequence_number: 3
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
status: Done
subjects:
  governs: Subject/Graph Node/Engineering/Continuant/Tool
  depends_on:
  - Subject/Graph Node/Engineering/Configuration/Shared TOML Connector
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Method'
  - Subject/Graph Node/Engineering/Evaluation
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Delivery'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Plan'
version: 10
updated_at: 2026-10-25 17:32:27 +0400
relations:
  is_decomposition_of:
  - CA-P-2256
tier: 3
---
# Summary

Preserve TOML text during pure edits

## Objective

After CA-P-2307 source acceptance and required affected FPF acceptance, implement the private pure TOML materializer with the approved dependency pin. Reuse existing semantic edit validation. Preserve unrelated bytes, types, comments and line endings; retain exact no-op bytes and refuse unsupported layout normalization. No file IO, new public representation or receiving authority.

## Details

Estimated own work: up to 15 minutes; split before exceeding that limit. Inherit CA-P-2256's accepted source and review gates. Root owns Plans and Git; workers own disjoint implementation and independent test files. No live configuration writes, installed activation, Core migration or Markdown/YAML dependency selection is authorized by this Task.

### Definition of Done

The bounded outcome has exact source/implementation pins, actual relevant checks and a different reviewer's acceptance. Preparation is not implementation; a Plan is not an executed FPF review. The parent and CA-P-2297 remain Active until their separate receiving/publication requirements pass.

### Acceptance — 2026-10-13

The private pure materializer and independently authored literal-byte suite passed 20 tests (7 author, 13 independent) with Python 3.14.7 and TOMLKit 0.15.1. Independent review found and verified fixes for duplicate-path binding normalization and retained array whitespace loss. Exact final source/code/test/dependency pins and known refusal boundaries are recorded in `.caprmedio_caprmedio/_projection/core-entity-review/stage2/tools-first/toml-materializer-acceptance.md`. No receiver, publication, live configuration write or installed runtime acceptance is claimed; P2310 and P2297 remain separate.
