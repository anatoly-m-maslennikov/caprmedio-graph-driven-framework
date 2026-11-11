---
identity:
  id: CA-C-713
  ref_id: CA-C-713
context:
  container:
    scope_unit: CA-SU-14
  role: Concern
  form: Question
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom
  tier: 3
state:
  status: Resolved
  version: 2
  updated_at: 2026-11-09 21:15:45 +0400
destination:
  file:
    name: CA-C-713-QUESTION--may-connected-references-outside-this-epic-be-repaired.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/01_concern/021_resolved
author: Anatoly Maslennikov
relations:
  concern_about:
  - CA-R-1901
  - CA-R-2785
  - CA-D-366
  - CA-D-512
  - CA-E-525
---

## Summary

May connected references outside this Epic be repaired?

## Concern

Two reviewed Engine merges have three Current callers outside the migration scope. Core Delivery D366 cites D594 twice for the Project MCP port contract. Old DISCOVER_TOOLS Delivery D512 and Evaluation E525 each refer to D678 in their Header and content.

The proposed repair replaces those references with the surviving R1901 and R2785 contracts, preserving the callers' behavior, Summary, Form, Scope Unit, Tier and Status. The repeated R2785 citation in E525 becomes one citation. Normal Version updates and predecessor archives still apply. No other Core or old Tool migration, code change or runtime acceptance is included.

## Details

The Operator approved the reference-only repairs in D366, D512 and E525. D594 references are replaced by R1901; D678 references are replaced by R2785, with the repeated R2785 citation in E525 deduplicated. Their behavior, Summary, Form, Scope Unit, Tier and Status stay unchanged. Each repair receives its next Version and a predecessor archive.

This resolves the scope question only. It does not authorize any other Core or old Tool migration, code change, runtime acceptance or release. The repair preview and application receipts are in .caprmedio_tmp/engine-summary-merge-20261109.
