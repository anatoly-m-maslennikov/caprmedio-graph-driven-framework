---
atom_id: CA-P-1635
ref_id: CA-P-1635
container:
  atom: CA-P-1615
role: Plan
form: Plan
label: Task
topics:
  main_subject: Subject/Graph Node/Engineering/Evaluation Implementation
  dependencies:
  - Subject/Graph Node/Domain/Continuant/Atom
  - Subject/Graph Node/Domain/Continuant/Atom/Content Role
  - Subject/Graph Node/Domain/Continuant/Atom.Status
  - Subject/Graph Node/Engineering/Continuant/Carrier
  - Subject/Graph Node/Engineering/Continuant/Tool
  - Subject/Graph Node/Engineering/Evaluation Implementation
  - Subject/Graph Node/Domain/Continuant/History/Journal
tier: 3
relations:
  is_decomposition_of:
  - CA-P-1615
  blocks:
  - CA-P-1637
status: Done
version: 9
updated_at: 2026-10-25 17:32:27 +0400
carrier_destination:
  file:
    name: 2-CA-P-1635-TASK--build-status-model-golden-corpus.md
    path: .caprmedio_caprmedio/03_plan/done/15-CA-P-1117-EPIC--harvest-and-implement-session-derived-operations/done/9-CA-P-1612-TASK--complete-content-role-driven-atom-status-changes/done/3-CA-P-1615-TASK--resolve-and-implement-whitelisted-atom-status-changes/done
work_sequence_number: 2
current_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
---
# Summary

Build status model golden corpus

## Objective

Within <=15 minutes, build status model golden corpus.

## Details

New tests/test_authoritative_status_models.py and tests/fixtures/status_models/ only. Start with fixtures covering all declared roles, specialized Type precedence, fallback, exact casing, missing/ambiguous/stale/forged authority and caller whitelist rejection. Coordinate with P1634 API; preserve existing external tests.

Inputs: accepted CA-P-1633 source packet and current saved lifecycle inputs; current default role domains, R1825@3/E545@2 and D565@1. Host/image gates C449 and relocation gate C447 remain unchanged. The existing development worker can run focused development tests, not immutable-image proof.

## Definition of Done

Good fixtures pass and deliberate errors report correct refusal. Focused development-worker results are distinct from immutable-image proof.

## Result

The golden corpus first exposed specialized-model selection and configured-source defects; those were repaired in the separately owned helper. Final test SHA-256 68505e4ac15a0694eee069d39886571290d58f743ac69a685ea21fcc8f638407. Eleven focused tests passed in the existing development worker, covering all role domains, Type precedence/fallback, casing/pins/forgery, configured roots, duplicate YAML, positive integer versions, definition roles and duplicate body domains. Development-worker evidence only, not new image proof.
