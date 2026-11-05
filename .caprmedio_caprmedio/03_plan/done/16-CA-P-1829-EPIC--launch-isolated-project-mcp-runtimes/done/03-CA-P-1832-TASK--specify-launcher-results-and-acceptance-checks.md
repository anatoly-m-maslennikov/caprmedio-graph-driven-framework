---
atom_id: CA-P-1832
ref_id: CA-P-1832
container:
  atom: CA-P-1829
role: Plan
form: Plan
label: Task
topics:
  main_subject: Subject/Graph Node/Engineering/MCP
  dependencies:
  - Subject/Graph Node/Domain/Continuant/Project
  - Subject/Graph Node/Domain/Continuant/Project.Settings
  - Subject/Graph Node/Domain/Continuant/Project.Structure
  - Subject/Graph Node/Domain/Continuant/Project.Framework Settings
  - Subject/Graph Node/Engineering/Continuant/Tool
  - Subject/Graph Node/Engineering/Action
  - Subject/Graph Node/Domain/Occurrent/Execution/Workflow Run
  - Subject/Graph Node/Engineering/Continuant/Carrier
  - Subject/Graph Node/Engineering/Evaluation
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: AI Agent'
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: Operator'
tier: 3
relations:
  is_decomposition_of:
  - CA-P-1829
  blocks:
  - CA-P-1833
  - CA-P-1834
status: Done
version: 8
updated_at: 2026-10-25 17:32:27 +0400
carrier_destination:
  file:
    name: 3-CA-P-1832-TASK--specify-launcher-results-and-acceptance-checks.md
    path: .caprmedio_caprmedio/03_plan/done/16-CA-P-1829-EPIC--launch-isolated-project-mcp-runtimes/done
work_sequence_number: 3
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
---
# Summary

Specify launcher results **and** acceptance checks

## Objective

the AI Agent specifies the observable success **and** failure contract for the Project MCP launcher.

## Details

- input: the reviewed selection **and** startup authority **and** existing HTTP authentication **and** Evaluation specifications.
- output: reviewed source E **and** D for authenticated host-side readiness, the MCP URL, safe structured metadata, bounded waiting, non-success outcomes, **and** the mock **and** real-Docker acceptance matrix. document endpoint readiness separately from Workflow-worker readiness.
- verification: bind each required result **to** an observable check; credentials remain separate from the URL **and** are absent from ordinary logs **and** results.
- effort: **`<=15`** minutes for **`=1`** AI Agent; the Epic's decomposition rule applies **before** execution **if** the estimate no longer holds.

### Definition of Done

- completion evidence: O188, E601 **and** D595; independent launcher_security review passed bounded host-authenticated MCP readiness, URL admission, safe structured failures **and** credential redaction.

the Plan is **not** Done **if** ((a success URL can be returned **before** authenticated readiness) **or** (a required startup outcome lacks an Evaluation) **or** (the output contract permits credential disclosure)).
