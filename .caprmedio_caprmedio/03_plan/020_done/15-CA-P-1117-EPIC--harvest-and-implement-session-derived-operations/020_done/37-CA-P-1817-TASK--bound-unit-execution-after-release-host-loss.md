---
atom_id: CA-P-1817
ref_id: CA-P-1817
container:
  atom: CA-P-1117
role: Plan
form: Plan
label: Task
topics:
  main_subject: Subject/Graph Node/Engineering/Release
  dependencies:
  - Subject/Graph Node/Engineering/Implementation
  - Subject/Graph Node/Engineering/Implementation Evaluation
  - Subject/Graph Node/Domain/Occurrent/Execution/Workflow Run
  - Subject/Graph Node/Domain/Continuant/History/Journal
tier: 3
relations:
  is_decomposition_of:
  - CA-P-1117
  relates_to:
  - CA-M-343
  - CA-E-586
  - CA-D-579
status: Done
version: 8
updated_at: 2026-10-25 17:32:27 +0400
carrier_destination:
  file:
    name: 37-CA-P-1817-TASK--bound-unit-execution-after-release-host-loss.md
    path: .caprmedio_caprmedio/03_plan/020_done/15-CA-P-1117-EPIC--harvest-and-implement-session-derived-operations/020_done
work_sequence_number: 37
current_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
---
# Summary

bound Unit execution after Release host loss

## Objective

implement the accepted host-independent Unit deadline and fixed temporary-mount contract, preserving sealed commands and non-passing timeout evidence.

## Details

source-first authority and independent review precede implementation. preserve the installed runtime, historical Release evidence and unrelated changes. root owns source publication and actual runtime dispatch.

## Definition of Done

the 18 bounded regression tests pass; independent code review accepts the guard; an installed-image diagnostic confirms daemon-owned timeout without a live host observer. full Release acceptance remains separately gated.

## Acceptance evidence

18 focused tests passed; independent review accepted the corrected command delimiter and timeout-latching behavior. the exact installed-N image ran a detached, isolated diagnostic with a two-second deadline and a child that exits zero on TERM. with no attached host observer during the deadline, the daemon reported exit 124. retained evidence: `.caprmedio_tmp/epic-resume-release/N15/deadline-tests/actual-docker.gTAxcn/terminal-inspect.json`. implementation commit: `8d1867c9e`. this is bounded guard acceptance, not a passing full Release gate.
