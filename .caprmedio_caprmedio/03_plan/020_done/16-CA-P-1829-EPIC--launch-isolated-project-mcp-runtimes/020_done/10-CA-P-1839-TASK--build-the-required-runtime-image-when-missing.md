---
atom_id: CA-P-1839
ref_id: CA-P-1839
container:
  atom: CA-P-1829
role: Plan
form: Plan
label: Task
topics:
  main_subject: Subject/Graph Node/Engineering/Image
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
  - CA-P-1840
status: Done
version: 8
updated_at: 2026-10-25 17:32:27 +0400
carrier_destination:
  file:
    name: 10-CA-P-1839-TASK--build-the-required-runtime-image-when-missing.md
    path: .caprmedio_caprmedio/03_plan/020_done/16-CA-P-1829-EPIC--launch-isolated-project-mcp-runtimes/020_done
work_sequence_number: 10
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
---
# Summary

Build the required runtime image **when** missing

## Objective

the AI Agent implements the build-if-missing branch for the admitted runtime image.

## Details

- input: the image resolver, accepted build contract, **and** image golden tests.
- output: a bounded build adapter that uses the intended distributive Framework source, resolves the built immutable image ID, **and** preserves an existing working runtime.
- verification: prove one build for an absent required image, no build for a compatible image, **and** truthful build-failure reporting. inspect the build context for excluded Project data, credentials, **and** generated state.
- effort: **`<=15`** minutes for **`=1`** AI Agent; the Epic's decomposition rule applies **before** execution **if** the estimate no longer holds.

### Definition of Done

- completion evidence: all 8 image golden tests passed. the build adapter assembles an exact private source closure, captures **and** re-inspects the immutable digest, checks input freshness **and** preserves existing runtimes. mock-only tests; real Docker build belongs **to** the proof Tasks.

the Plan is **not** Done **if** ((a compatible image is rebuilt unnecessarily) **or** (a failed build produces a ready image result) **or** (build input **or** existing-runtime preservation checks fail)).
