---
atom_id: CA-R-1819
ref_id: CA-R-1819
container:
  scope_unit: CA-SU-20
role: Requirement
form: Rule
topics:
  main_subject: "Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Execution Control"
  dependencies:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: AI Agent'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run
  - "Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Execution Control/Effect Authorization"
  - Subject/CAPRMEDIO/Carrier
tier: 3
status: Archived
version: 12
updated_at: 2026-10-27 20:00:03 +0400
carrier_destination:
  file:
    name: CA-R-1819@12-APPS-RULE--isolate-agent-proposals-from-project-writes.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/04_requirement/archive
current_scope_unit: APPS
author: Anatoly Maslennikov
---
# Summary

isolate Agent proposals from Project writes

## Scope

Agentic Action execution **in** the Docker runtime.

## Claim

an AI Agent **must** receive **only** its supplied execution context **and** required authentication, **without** access **to** writable Project Carriers, the host home directory **or** the Docker daemon.

## Details

- the AI Agent returns a structured proposal; the trusted worker alone admits **and** applies authorized changes.
- the execution context carries the selected Atom, checking rules, Action prompt **and** relevant saved phase report.
- container isolation replaces the inner CLI sandbox **only** **in** the dedicated Agent service, which has no Project mounts.
- credentials remain runtime data, excluded from the image, source control, public status **and** reports.
