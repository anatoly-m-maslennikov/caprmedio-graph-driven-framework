---
atom_id: CA-R-1891
ref_id: CA-R-1891
container:
  scope_unit: CA-SU-2
role: Requirement
form: Rule
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Communication
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control/Effect Authorization
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Component Structure
  - Subject/CAPRMEDIO/Carrier/Docker Image
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Runtime
tier: 3
status: Active
version: 18
updated_at: 2026-10-27 20:00:05 +0400
carrier_destination:
  file:
    name: CA-R-1891-WORKFLOW_ORCHESTRATOR-RULE--provide-isolated-host-execution-for-release-runs.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-2_APP_WORKFLOW_ORCHESTRATOR/04_requirement
current_scope_unit: WORKFLOW_ORCHESTRATOR
author: Anatoly Maslennikov
---
# Summary

provide isolated host execution for Release Runs

## Scope

the host execution capability for source-admitted Release Version Runs in WORKFLOW_ORCHESTRATOR.

## Claim

WORKFLOW_ORCHESTRATOR **must** provide a Release-only Host Executor that can run the admitted host-dependent gates while preserving the separate native **and** Docker execution boundaries.

## Details

- the capability uses the existing source-bound Release implementation, exact Operator authorization **and** canonical Journal recording.
- **only** a fresh admitted Release Run **or** an expressly authorized recovery of a Run already bound **to** this Host Executor can execute through it.
- worker startup remains explicit. startup creates no Run; it consumes no work from another executor's Queue.
- the ordinary Docker worker retains its existing isolation, with no host Docker socket added.
- an unavailable Host Executor blocks Release admission; another executor does **not** become an implicit fallback.
- this capability does **not** authorize promotion, image deletion **or** replay of an uncertain effect. those effects retain their existing gates.
