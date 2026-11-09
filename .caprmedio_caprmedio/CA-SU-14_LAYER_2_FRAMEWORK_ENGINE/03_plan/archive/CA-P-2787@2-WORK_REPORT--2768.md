---
identity:
  id: CA-P-2787@2
  ref_id: CA-P-2787@2
context:
  container:
    atom: CA-P-2767
  role: Plan
  form: Work Report
  label: Work Report
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom
  tier: 4
state:
  status: Archived
  version: 2
  updated_at: 2026-11-09 05:53:06 +0400
destination:
  file:
    name: CA-P-2787@2-WORK_REPORT--2768.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/03_plan/archive
author: Anatoly Maslennikov
relations:
  IS_WORK_REPORT_FOR:
  - CA-P-2768
---

## Summary

Confirm the Engine refinement scope and inventory

## Details

Complete Current Engine query captured via query_run/query_page (1,959 rows). Selected 323 MED Atoms across ten nonempty eligible Scope Units: 213 readable,110 with no query-exposed Content. The older holds account for64 PROGRAMMATIC MED and11 APPS MED;35 additional MED holds are MCP30,WORKFLOW_ORCHESTRATOR4,PROMPTS1. Older78-RMEDO deferral is preserved; its R/O members are context, not counted as reviewed MED. The500 benchmark Atoms and their Scope Declaration remain excluded. Scanned excluded Tool-source query content for Workbench capabilities: only M259 mentions Workbench as supporting context for the old graph generator; it is not a Workbench query/View capability and stays excluded. No excluded Tool was silently included. Zero local MED are indexed in FRAMEWORK_ENGINE,AGENTIC orSKILLS; their eligible descendants are included. Current Scope declarations and owner IDs/names were resolved without moving scopes. Thin inventory is inventory.tsv; query evidence is in the execution cache. Existing protected sources are pinned by69,409 preimage hashes.
