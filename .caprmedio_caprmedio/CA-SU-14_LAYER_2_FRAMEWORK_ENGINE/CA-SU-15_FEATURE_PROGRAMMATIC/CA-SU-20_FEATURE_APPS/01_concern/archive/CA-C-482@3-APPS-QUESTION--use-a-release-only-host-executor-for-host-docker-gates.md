---
atom_id: CA-C-482
ref_id: CA-C-482
container:
  scope_unit: CA-SU-20
role: Concern
form: Question
topics:
  main_subject: Release Version/Host Executor
  dependencies:
  - Release Version
  - Subject/Domain/Node/Occurrent/Execution/Workflow Run
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
  - Queue
  - DBOS
  - Docker Image
  - Implementation
relations:
  concern_about: [CA-R-1891, CA-M-347, CA-D-583, CA-E-590]
status: Archived
version: 3
updated_at: 2026-10-23 03:14:50 +0400
carrier_destination:
  file:
    name: CA-C-482@3-APPS-QUESTION--use-a-release-only-host-executor-for-host-docker-gates.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/01_concern/archive
current_scope_unit: APPS
local_tier: Standard
global_tier: 14
author: Anatoly Maslennikov
---
# Summary

use a Release-only Host Executor for host Docker gates

## Concern

the healthy isolated Docker worker cannot run the Release Workflow's host Docker gates: its image has no Docker client **or** socket, **and** its Project mount paths are container-local. the ordinary native scheduler also contains an older queued Base Revise Run outside the current Release scope.

## Evidences

- the runtime image was rebuilt from current code; worker **and** Agent are healthy on `sha256:65e889a15a6f6bd6fa7fd2f6c4b34a4acaf9bd37624424fe38b052f978e2d776`.
- the existing Docker Queue has no pending Runs. the native Queue retains `base-revise-replacements-20261004-0305`; it is **not** selected for this work.
- the real installed N image passes its retained-proof **and** immutable-image admission checks. actual N+1 Unit, image, end-to-end **and** promotion gates have **not** executed.
- the existing Release gate helpers are host-capable, but current MCP transport selection sends **all** queued work **to** the Docker worker.

## Blast radius

the fresh Release Run cannot reach its real host-dependent gates through the current public route. normal Docker Workflows remain usable.

## Disposition

under the Operator's direction **to** choose the best option **and** record uncertainty, select an explicitly started Release-only Host Executor with a separate scheduler namespace. preserve Docker isolation **and** both existing Queues. CA-R-1891, CA-M-347, CA-D-583 **and** CA-E-590 define the selected boundary before implementation. keep this Question active **until** the actual MCP-admitted Release execution establishes the boundary; no mock pass is promoted **to** real Release completion.
