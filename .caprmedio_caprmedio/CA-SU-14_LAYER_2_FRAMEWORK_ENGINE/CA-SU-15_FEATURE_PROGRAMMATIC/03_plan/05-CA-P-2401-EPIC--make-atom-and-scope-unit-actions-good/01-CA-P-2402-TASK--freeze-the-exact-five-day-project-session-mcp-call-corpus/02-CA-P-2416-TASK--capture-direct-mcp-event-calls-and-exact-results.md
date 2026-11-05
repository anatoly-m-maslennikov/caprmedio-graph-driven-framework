---
atom_id: CA-P-2416
ref_id: CA-P-2416
container:
  atom: CA-P-2402
role: Plan
form: Plan
label: Task
topics:
  main_subject: Subject/Graph Node/Engineering/MCP
  dependencies:
  - Subject/Graph Node/Domain/Continuant/Atom
  - Subject/Graph Node/Domain/Continuant/Scope Unit
  - Subject/Graph Node/Domain/Continuant/Term//Property
  - Subject/Graph Node/Engineering/Workflow
tier: 3
relations:
  is_decomposition_of:
  - CA-P-2402
status: Active
version: 7
updated_at: 2026-10-25 17:32:27 +0400
carrier_destination:
  file:
    name: 2-CA-P-2416-TASK--capture-direct-mcp-event-calls-and-exact-results.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/03_plan/5-CA-P-2401-EPIC--make-atom-and-scope-unit-actions-good/1-CA-P-2402-TASK--freeze-the-exact-five-day-project-session-mcp-call-corpus
work_sequence_number: 2
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
---
# Summary

Capture direct MCP event calls and exact results

## Objective

Complete one bounded evidence/safety prerequisite for the scoped five-day MCP audit without treating incomplete evidence as a completed operation.

## Details

Correct the known corpus omission by ingesting actual event_msg.payload.item.type=McpToolCall records and their exact status/result identifiers. Scan the frozen five-day project session frontier, retain real request/result pairs and event times, deduplicate repeated start/completion observations by native call identity, and keep embedded exec literals as candidates rather than canonical invocations. Own corpus-v2/** only; preserve release-v1 unchanged. Integrate the independent attribution/prefix review before declaring completeness. Freeze an append-safe immutable direct-event release and report unsupported event schemas or missing results explicitly.

Use a Luna worker and at most15minutes own work. Split any longer responsibility into a separately recorded bounded subtask before continuing. Historical analysis is MCP-call-only; this Task does not authorize implementation fixes, deployment or production tests. Manual permission covers planning records only, not Concern/source writes. All actual runtime reproductions require the verified disposable nonproduction harness.

### Definition of Done

The assigned evidence or fixture result has reproducible source references, exact observed outcomes and honest gaps; independent acceptance checks pass or blockers are recorded without effects being replayed. Production remains untouched. Planning checkpoint: A read-only release-v2 snapshot now contains 728 exact project-proven CAPRMEDIO native rows, including 384 lifecycle rows; bounded semantic review is independently accepted. Source timestamps use payload.started_at_ms. Complete immutable source provenance is NOT accepted: header-only 4 KiB pins do not cover distant calls and scanning was not bounded to initial fstat. Metadata basis/prefix claims have inconsistencies. This Task remains Active for that evidence-freeze limitation; semantic Tasks may use the accepted frozen row subset with explicit limits. Reports: .caprmedio_tmp/mcp-audit-20261020/corpus-v2/release-v2/.
