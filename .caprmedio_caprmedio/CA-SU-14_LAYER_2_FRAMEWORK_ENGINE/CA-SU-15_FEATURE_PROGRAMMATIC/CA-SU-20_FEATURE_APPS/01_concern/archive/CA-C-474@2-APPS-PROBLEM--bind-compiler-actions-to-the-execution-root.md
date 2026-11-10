---
atom_id: CA-C-474
ref_id: CA-C-474
container:
  scope_unit: CA-SU-20
role: Concern
form: Problem
topics:
  main_subject: Compiler Action execution-root binding
  dependencies:
  - Subject/Engineering/Runtime
  - Subject/Domain/Node/Occurrent/Execution/Workflow Run
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - Subject/Domain/Node/Continuant/Project
  - Journal
relations:
  concern_about: [CA-P-1714, CA-P-1624]
status: Archived
version: 2
updated_at: 2026-10-23 03:14:50 +0400
carrier_destination:
  file:
    name: CA-C-474@2-APPS-PROBLEM--bind-compiler-actions-to-the-execution-root.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/01_concern/archive
current_scope_unit: APPS
local_tier: Standard
global_tier: 14
author: Anatoly Maslennikov
---
# Summary

Bind compiler Actions to the execution root

## Concern

The selected compiler adapter passes the frozen host Project root unchanged into an Action running in Docker, instead of using its trusted execution-visible Project root.

## Evidences

Run release-methodology-reconcile-20261005-1805 has DBOS scheduler status SUCCESS but its governed Workflow, first Step and first Action ended interrupted_pending. CA-O-004 reported request-project-root-invalid for /Users/am/Documents/My_Repos/caprmedio-graph-driven-framework, while the Docker worker runs with Project root /project. The Action, Step and Workflow Journal records have empty effect references. No compiler publication receipt exists.

## Blast radius

Build Applicable Methodology through the selected Docker transport, and the fresh compiled-methodology prerequisite for first Framework N installation. This failure does not invalidate the already published sixteen-route manifest.

## Disposition

Repair the adapter by copying frozen parameters and replacing only project_root with the trusted executor context root. Preserve governed bindings and every other admitted parameter. Add host-versus-Docker regression tests before acceptance. Preserve the original interrupted Run; after the repaired runtime is loaded, submit a fresh normally admitted Run rather than replaying this one.
