---
atom_id: CA-O-166
ref_id: CA-O-166
container:
  scope_unit: CA-SU-13
role: Operations
form: Action
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Delivery
  dependencies:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Action'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Projection/Type: Applicable Methodology'
  - Subject/CAPRMEDIO/Carrier
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Workflow'
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Traceability
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
tier: 3
status: Active
version: 15
updated_at: 2026-11-02 19:46:47 +0400
carrier_destination:
  file:
    name: CA-O-166-PROJECT_CONFIGURATION-ACTION--deliver-and-compile-candidate-methodology.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/09_operations
current_scope_unit: PROJECT_CONFIGURATION
author: Anatoly Maslennikov
---
# Summary

Deliver and compile candidate Methodology

## Action

Deliver and compile candidate Methodology **means** the Action that rebuilds the derived Framework Methodology product from the frozen active source boundary, then invokes the canonical applicable compiler.

## Scope

`deliver_sources` clears only replaceable product members under `LAYER_1_FRAMEWORK_METHODOLOGY/`, preserves declared settings, and copies only active Core Meta-Model, installed extension, and Project Configuration source members from the Project-owned authority. `compile` applies CA-O-011 to that exact product and verifies that its bytes and source relations equal the private tested preparation. Neither phase writes the installed Framework.

## Details

Commit the successful product clear, active-source copy, and compilation separately, staging only each transition's owned changes. These checkpoints remain separate even when one Step invokes both clear and copy. A read-only or unchanged transition records its result without an empty commit; a failed transition or commit stops before the next transition.

No inactive source Atom, partial source set, implicit path, stale compiler output, altered source byte, or changed boundary is success. This Action does not run the full suite, install, publish, alter authoring, or create another compiler Workflow. A failed phase retains actual evidence without claiming delivery or compilation complete.
