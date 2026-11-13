---
identity:
  atom_id: CA-P-3005
  ref_id: CA-P-3005
context:
  container:
    atom: CA-P-2791
  role: plan
  form: plan
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom
  tier: 4
  label: Task
state:
  status: canceled
  version: 1
  updated_at: '2026-11-11T22:18:41.347311+04:00'
destination:
  file:
    name: CA-P-3005-TASK--release-the-final-engine-image-locally.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/020_done/CA-P-2791-EPIC--align-engine-implementation-with-the-refined-specification/040_canceled
relations:
  IS_BLOCKED_BY:
  - CA-P-3003
  - CA-P-3004
author: Anatoly Maslennikov
---

## Summary

Release the final Engine image locally

## Objective

Build the image with the Current Workflow references, run both Workbench guards, activate it, and verify live health, Workbench, MCP registration, and query_run.

## Details

Activated sha256:a83b739fa9640965d38da51b35b8e7b52a75b4dccc4052a20f667ca2509e8b32. The Workbench resource and performance guards passed. Live health, frontend assets, the HTTP Workbench query, six MCP tool registrations, and query_run passed.
