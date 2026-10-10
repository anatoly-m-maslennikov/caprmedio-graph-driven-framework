---
atom_id: CA-O-166
content_role: Operations
type: Action
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
status: Active
author: Anatoly Maslennikov
subjects:
  governs: "Deliver and compile candidate Methodology"
  depends_on: [Action, Methodology Source, Applicable Methodology, Delivery, Compiler, Artifact/Revision, Journal]
version: 6
updated_at: "2026-10-10 19:05:19 +0400"
relations:
  relates_to: [CA-O-164, CA-O-172, CA-O-173, CA-O-011, CA-O-157, CA-R-1525, CA-R-1720]
---
# Summary

Deliver and compile candidate Methodology

## Action

Deliver and compile candidate Methodology **means** the Action that rebuilds the derived Framework Methodology product from the frozen active source boundary, then invokes the canonical applicable compiler.

## Scope

`deliver_sources` clears only replaceable product members under `101_FRAMEWORK_METHODOLOGY/`, preserves declared settings, and copies only active Core Meta-Model, installed extension, and Project Configuration source members from the Project-owned authority. `compile` applies CA-O-011 to that exact product and verifies that its bytes and source relations equal the private tested preparation. Neither phase writes the installed Framework.

## Details

Commit the successful product clear, active-source copy, and compilation separately, staging only each transition's owned changes. These checkpoints remain separate even when one Step invokes both clear and copy. A read-only or unchanged transition records its result without an empty commit; a failed transition or commit stops before the next transition.

No inactive source Atom, partial source set, implicit path, stale compiler output, altered source byte, or changed boundary is success. This Action does not run the full suite, install, publish, alter authoring, or create another compiler Workflow. A failed phase retains actual evidence without claiming delivery or compilation complete.
