---
identity:
  id: CA-P-2850
  ref_id: CA-P-2850
context:
  container:
    scope_unit: CA-SU-15
  role: Plan
  form: Plan
  label: Task
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Scope Unit
  tier: 4
state:
  status: Done
  version: 1
  updated_at: 2026-11-10 00:31:33 +0400
destination:
  file:
    name: CA-P-2850-TASK--archive-retired-tool-scope-units.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/03_plan
author: Anatoly Maslennikov
---

## Summary

Archive retired Tool Scope Units

## Objective

Archive the retired discovery/execution Tool and Workflow Orchestrator Atoms under their parent Scope Units, then remove the seven Scope Units and their Current declarations.

## Scope

CA-SU-2 through CA-SU-8. Preserve shared contracts required by Workbench, host releases and standalone Subject builders. Preserve all existing historical carriers and unrelated lifecycle Drafts. Rehome retained MCP Docker support before removing the old orchestrator delivery folder.

The shared MCP registration increment uses an editable provider inventory, a generated registry and an explicit global MCP blacklist. Blacklisted Tools must be absent from discovery and rejected on direct invocation; Project settings cannot re-enable them. Release packaging generates and validates the registry before image admission.

## Definition of Done

The seven governing Scope folders and Current declarations are absent; archived records reside under their parents, with identities, bodies, Versions and Updated At preserved. Shared live contracts and runtime support retain valid owners. The Current Scope graph and affected retained implementation checks pass. Deployment and unrelated retired Tool families remain outside this Task.
