---
atom_id: CA-C-584
content_role: Concern
type: Problem
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
author: Anatoly Maslennikov
status: Active
priority: medium
subjects:
  governs: Entity/Node/Continuant/Implementation
  depends_on: []
relations:
  concern_about: [CA-R-1847, CA-E-567, CA-O-016, CA-O-127, CA-P-2613, CA-P-2614, CA-P-2619]
  relates_to: [CA-C-576]
version: 2
updated_at: "2026-10-23T00:51:57+0400"
---
# Summary

The exact 15-operation MCP contract and optional move_atom extension are not reconciled

## Concern

This is a concrete declaration mismatch. R1847@16 lines 37-42 defines the
exact 15-operation MCP route set and omits move_atom. E567@7 lines 25, 36 and
40 also expects the 15-operation contract. In contrast, the canonical Project
manifest contains 16 operations including move_atom, selected_route_spec.py
line 33 permits the optional selected-route name, and O127 supports the Move
operation. The public MCP declarations therefore differ from the canonical
Project manifest and the implementation's optional capability.

This finding is owned primarily by the lifecycle review CA-P-2614; the query
review CA-P-2619 also confirmed the current query/admission pins. It is not a
reason to relabel the 15-operation R1847 source as a 16-operation contract and
does not by itself establish a runtime failure.

## Required disposition

Reconcile the exact current Project manifest, public MCP declarations,
selected_route_spec.py optional-route handling, O127 and E567@7 against the
same source-bound contract. Preserve R1847@16's exact 15-operation meaning
until an authority-backed successor explicitly changes it. Do not invent a new
rule, silently add move_atom to the public frontier, rename the source
contract, mutate the installed binding or emit a candidate while this Problem
is open. Preserve operation order, source pins and unsupported-operation
behavior.

## Evidence boundary

The lifecycle lane CA-P-2614 and query/admission lane CA-P-2619 completed
read-only review. The exact evidence is R1847@16 lines 37-42, E567@7 lines 25,
36 and 40, selected_route_spec.py line 33 with
OPTIONAL_SELECTED_ROUTE_NAMES, the raw Project route count of 16 including
move_atom, and O127's Move support. The source-review verifier revalidated
50 pins with no changes; Project, Engine and A1142 baselines remained
unchanged.

## Next gate

Keep this Problem Active with CA-P-2613. Resolve the public-declaration versus
Project/code frontier before CA-P-2620 registry requalification or CA-P-2621
detached candidate compilation.
