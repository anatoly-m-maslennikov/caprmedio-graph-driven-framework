---
atom_id: CA-P-1773
ref_id: CA-P-1773
container:
  atom: CA-P-1117
role: Plan
form: Plan
label: Task
topics:
  main_subject: Subject/Graph Node/Engineering/Release
  dependencies:
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Delivery'
  - Subject/Graph Node/Engineering/Evaluation
  - Subject/Graph Node/Engineering/Implementation
  - Subject/Graph Node/Engineering/Manifest
tier: 3
relations:
  is_decomposition_of:
  - CA-P-1117
  blocks:
  - CA-P-1757
  - CA-P-1717
  - CA-P-1721
status: Active
version: 9
updated_at: 2026-10-25 17:32:27 +0400
carrier_destination:
  file:
    name: 22-CA-P-1773-TASK--refresh-the-admitted-http-harness-source-pin.md
    path: .caprmedio_caprmedio/03_plan/020_done/15-CA-P-1117-EPIC--harvest-and-implement-session-derived-operations
work_sequence_number: 22
current_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
---
# Summary

Refresh the admitted HTTP Harness source pin

## Objective

Bind the new accepted HTTP case in the existing mandatory Docker Harness without weakening its exact source admission.

## Details

Root owns CA-D-572 private Harness metadata and the matching release_source_admission.py trust anchor. Only the existing test_docker_e2e.py byte pin and timestamp change; D572's Claim, closed schema, twelve occurrences, source frontier and Version 10 remain unchanged. This is carrier/source-pin recoding, not a new Workflow definition. Independent read-only review verifies that exact delta before a fresh release dispatch. Estimated slice <=15 minutes.

## Definition of Done

The private pins reopen successfully, the unchanged sixteen-route manifest remains valid, focused admission tests pass and independent review accepts. No stale-pin guard is bypassed and no historical Run is rebound.

## Pre-execution review

Root selects this necessary mechanical pin refresh under the accepted E584/E585 HTTP proof, DRY and current source authority. Actual Docker verification remains P1757.

## Approved first-cut disposition

Release-specific source-pin acceptance is deferred to a later milestone. This Plan remains Active, and its exact-pin, source-currentness and no-historical-Run-rebinding boundaries remain in force. Docker HTTP MCP transport is retained in the approved first cut and is not deferred; an existing dependency actually required to prove that retained HTTP transport may be reused without treating this deferred Release-specific acceptance as complete or dispatching a Release refresh.
