---
atom_id: CA-P-1971
content_role: Plan
type: Plan
label: Task
work_sequence_number: 13
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
author: Anatoly Maslennikov
assignee: AI Agent
status: Active
subjects:
  governs: Entity
  depends_on: [Atom, Subject, Term, Property, Carrier, Revision, Scope Unit, Projection, Plan, Tool, Journal, Operator]
version: 3
updated_at: "2026-10-10 23:34:31 +0400"
relations:
  is_decomposition_of: [CA-P-1959]
---
# Summary

Verify the Stage 2 entity model

## Objective

Verify the final RMEDO sources and their reproducible entity graph after both ordered steps.

## Details

Estimated own work: 15 minutes. Assignee: AI Agent. Required prerequisite: CA-P-1970.

Independently check final Subjects, Summary, Substance, Scope and Details against the accepted batch decisions and current governing RMED+O. Verify source identities, revisions, history, evidence coverage and affected validation/tests.

Check Summary replacements have new IDs and recorded lineage, not overwritten same-ID history. Use a separately authored expected ledger/oracle without calling the producer's graph builder, and prove altered outputs are rejected.

Rebuild the graph from authoritative Subjects with pinned implementation and compare the final relation semantics with the accepted model. Report unresolved, excluded and deferred matters explicitly. Terms remain a separate graph; same spelling does not authorize a Term edge.

Deliver one final receipt with exact source, implementation and output hashes, actual check results and remaining work. No automatic installed-copy refresh, runtime activation, release, push, PR or native MCP delivery follows from this pass. Split verification if it exceeds 15 minutes.

Inherit CA-P-1959's source boundary, confidence threshold and preservation rules. Creating this Plan records work; it does not start or complete it.

### Definition of Done

The Plan is **not** Done if a required check is failed, missing or stale, final graph reproduction diverges, an accepted decision is unaccounted for, source/body meaning is lost, or completion is overstated; any direct decomposing Plan is not Done; or own work exceeds 15 minutes without decomposition.
