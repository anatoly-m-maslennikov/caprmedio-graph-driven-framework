---
atom_id: CA-P-2609
ref_id: CA-P-2609
container:
  atom: CA-P-2581
role: Plan
form: Plan
label: Task
topics:
  main_subject: Subject/Graph Node/Engineering/MCP.selected Workflow capability routes
tier: 3
relations:
  is_decomposition_of:
  - CA-P-2581
  depends_on:
  - CA-P-2597
  - CA-P-2607
  relates_to:
  - CA-P-2601
  - CA-P-2602
  - CA-O-016
status: Done
version: 6
updated_at: 2026-10-25 17:32:27 +0400
carrier_destination:
  file:
    name: 11-CA-P-2609-TASK--verify-the-docker-free-isolated-mcp-harness.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/03_plan/5-CA-P-2401-EPIC--make-atom-and-scope-unit-actions-good/96-CA-P-2577-TASK--implement-the-shared-context-native-workflow/done/4-CA-P-2581-TASK--integrate-shared-workflow-continuation-and-retry-state/done
work_sequence_number: 11
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
---
# Summary

Verify the Docker-free isolated MCP harness

## Objective

Run the focused interactive-continuation checks in a naked isolated harness
without Docker or the production MCP port. Verify that current-session prompt
return, validated submission, pending/terminal transitions, explicit Project
binding and no-replay behavior remain attributable under the source-first O016
configuration.

## Details

Own work is bounded to 15 minutes. Use disposable frozen Project inputs, a
distinct nonproduction state/port if an HTTP boundary is required, locked uv,
and Project Temporary State. Do not start containers, touch production, replay
uncertain history, rebuild projections as authority, run the full suite, or
publish Git changes. Keep implementation, harness and real-Manifest journey
evidence separate; a Docker-free pass cannot claim runtime admission.

### Definition of Done

The focused naked-harness command passes or returns explicit bounded failures
for prompt/result and source-binding cases, with receipt paths, protected
production equality and the remaining complete real-Manifest gate recorded.

### Accepted completion evidence

The final Docker-free naked stdio smoke passed with 23 valid tools and an exact-path preview, using `.caprmedio_tmp/naked-mcp-final-20261022-1829`. It confirms the focused prompt/result and source-binding harness without Docker or the production port; it does not claim Docker runtime admission, current installed Project binding or deployment.

