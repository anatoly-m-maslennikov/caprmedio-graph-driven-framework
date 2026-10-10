---
atom_id: CA-O-166
content_role: Operations
type: Action
current_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
subjects:
  governs: "Deliver and compile candidate Methodology"
  depends_on: [Action, Methodology Source, Applicable Methodology, Delivery, Compiler, Artifact/Revision, Journal]
version: 5
updated_at: 2026-10-09 16:36:54 +0400
relations:
  relates_to: [CA-O-164, CA-O-172, CA-O-173, CA-O-011, CA-O-157, CA-R-1525, CA-R-1720]
---
# Summary

Deliver and compile candidate Methodology

## Action

Deliver and compile candidate Methodology **means** the Action that performs one bound `deliver_sources` or `compile` phase for the frozen N+1 candidate; it reuses the applicable compiler contract rather than defining another compiler.

## Scope

`deliver_sources` copies **only** the complete selected active candidate Methodology source set and admitted support artifacts, with every source identity, revision and digest, from the declared authoring Scope Units to the sealed private `.caprmedio_tmp/release_candidates/<run_id>/methodology/` export. That export carries the logical root `methodology/` delivery mapping but does not change the live root before the gate and never changes or substitutes authoring authority. `compile` uses the required reviewed selected-snapshot compiler Tool boundary and the delivered, still-matching candidate frontier to materialize only `.caprmedio_tmp/release_candidates/<run_id>/compiled/`. After the gate, CA-O-169 carries those same sealed export, source-copy and projection bytes unchanged to root delivery and the selected Project's `.caprmedio_<project>/000_CAPRMEDIO_framework` control tree; none is independently editable projection authority.

## Details

No inactive source Atom, partial source set, implicit root, silently translated Project Structure path, stale compiler output, altered source byte, unreviewed Tool boundary/output layout or changed candidate frontier is success. The Action validates complete source and candidate-output manifest/digests before returning; it preserves N, all authoring sources, Journals and unrelated deliveries. It does not install a runtime package or Skill, run tests, build an image, promote, remove an image, alter the compiler, or use a second compilation Workflow. A failed or recording-blocked phase retains actual effects and Journal evidence without claiming compilation or delivery complete.
