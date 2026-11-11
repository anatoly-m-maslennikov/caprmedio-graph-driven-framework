---
atom_id: CA-P-1538
ref_id: CA-P-1538
container:
  atom: CA-P-1525
role: Plan
form: Plan
label: Task
topics:
  main_subject: Subject/Graph Node/Engineering/Query Filter Contract
  dependencies:
  - Subject/Graph Node/Engineering/Implementation
  - Subject/Graph Node/Engineering/Continuant/Tool
  - Subject/Graph Node/Engineering/Evaluation
tier: 3
relations:
  is_decomposition_of:
  - CA-P-1525
  blocks:
  - CA-P-1525
status: Active
version: 7
updated_at: 2026-10-25 17:32:27 +0400
carrier_destination:
  file:
    name: 2-CA-P-1538-TASK--complete-shared-filter-semantics-and-bounds.md
    path: .caprmedio_caprmedio/03_plan/020_done/15-CA-P-1117-EPIC--harvest-and-implement-session-derived-operations/08-CA-P-1520-TASK--deliver-read-only-artifact-and-journal-query-workflows/020_done/05-CA-P-1525-TASK--implement-artifact-query-tool
work_sequence_number: 2
current_scope_unit: caprmedio
claim_target_scope_unit: TOOLS
author: Anatoly Maslennikov
assignee: AI Agent
---
# Summary

Complete shared filter semantics and bounds

## Objective

Within <=15 minutes, test-first finish this bounded P1525 implementation remainder. The original source acceptance is still current; do not narrow its required behavior to existing passing tests.

## Details

Own only FIND_AND_FETCH_ARTIFACTS/query_filter.py and new tests/test_query_filter.py. Shared R1850@2 and P1532 accepted pins govern. Preserve exported parse_filter/evaluate_filter/typed_equal/QueryFilterError/MISSING API or coordinate an additive API early. Enforce recursion depth for NOT, parentheses and typed JSON literals, tokens including literals, bounded IN; validate bad JSON/duplicate object members/nonfinite numbers, malformed separators/operators and trailing syntax without eval. JSON number has one semantic type (integer/float compare numerically; booleans never numbers). Validate all selectors before short-circuit evaluation, via additive helper, so malformed unvisited branches cannot pass. Test missing/null, deep lists/maps, precedence, escaped quotes and all resource rejection cases with bounded diagnostics. No Artifact filesystem implementation, source/RMED/Plan, Journal/MCP or settings-file changes. Publish API to Artifact and Journal workers. Run focused golden test file; root persists result.

You are not alone; preserve concurrent edits and use apply_patch. Inherit 90% confidence and mechanical Git exception; root owns Plan writes/commits. No harvesting, FPF, external deployment, actual Project authority mutation or permission bypass. If unfinished, save the exact frontier instead of claiming Done.

### Definition of Done

Every owned requirement has passing golden evidence against current accepted source pins, exact commands/results and truthful integration/image remainder.
