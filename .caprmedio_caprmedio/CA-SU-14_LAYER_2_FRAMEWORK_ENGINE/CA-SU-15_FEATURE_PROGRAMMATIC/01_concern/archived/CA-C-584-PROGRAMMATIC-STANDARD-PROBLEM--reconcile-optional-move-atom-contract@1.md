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
  concern_about: [CA-R-1847, CA-E-567, CA-O-016, CA-P-2613, CA-P-2619]
  relates_to: [CA-C-576]
version: 1
updated_at: "2026-10-23T00:44:56+0400"
---
# Summary

The exact 15-operation MCP contract and optional move_atom extension are not reconciled

## Concern

The current MCP route/admission inventory exposes an exact 15-operation
contract, while the current Project-side source package and the reviewed
R1847@16 contract include an optional move_atom operation as a possible
sixteenth capability. The difference is an explicit contract-boundary issue,
not evidence that the 15 admitted operations are invalid and not a reason to
silently add the optional operation to the live binding.

## Required disposition

Reconcile the current Project source, MCP admission definitions and E567@7
evaluation against the same source-bound contract. Decide whether move_atom is
an explicitly admitted extension or remains outside the current 15-operation
frontier. Preserve exact source pins, operation order and unsupported-operation
behavior; quarantine a mismatched optional extension until its candidate is
independently validated. Do not mutate the installed binding, emit a candidate
or claim runtime readiness from this review alone.

## Evidence boundary

CA-P-2619 completed the read-only current-source and both-query-admission
review. The source-review verifier revalidated 50 pins with no changes and
the Project/Engine/A1142/Core baselines remained unchanged. Historical raw
manifest drift and the optional move difference are kept distinct from the
current 15-operation observation.

## Next gate

Keep this Problem Active with CA-P-2613. A later bounded registry/source
requalification must resolve the contract boundary before any detached
candidate compilation or publication decision.
