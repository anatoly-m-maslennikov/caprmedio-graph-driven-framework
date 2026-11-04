---
atom_id: CA-O-166
content_role: Operations
type: Action
current_scope_unit: PROJECT_CONFIGURATION
status: Active
author: Anatoly Maslennikov
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Delivery
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Action'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Projection/Type: Applicable Methodology'
  - Subject/CAPRMEDIO/Carrier
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Workflow'
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Traceability
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
version: 15
updated_at: 2026-11-02 19:46:47 +0400
relations: {}
tier: 3
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/09_operations/CA-O-166-PROJECT_CONFIGURATION-ACTION--deliver-and-compile-candidate-methodology.md
  source_atom_id: CA-O-166
  source_atom_revision: 15
  source_sha256: e837cbd3fb22fed742cb5eedf497aa65370a13af7a2119bbfd558cf9f3059fbb
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
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
