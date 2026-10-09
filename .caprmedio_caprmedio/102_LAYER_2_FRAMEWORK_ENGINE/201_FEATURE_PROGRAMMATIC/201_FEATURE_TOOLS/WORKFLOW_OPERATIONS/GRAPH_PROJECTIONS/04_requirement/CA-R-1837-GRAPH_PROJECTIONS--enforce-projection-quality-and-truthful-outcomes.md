---
atom_id: CA-R-1837
content_role: Requirement
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-09 19:23:34 +0400"
subjects:
  governs: "Tool/WORKFLOW_OPERATIONS/GRAPH_PROJECTIONS/Quality disposition"
  depends_on: [Tool, Projection, Artifact, Journal, Workflow Run, Step Run]
relations:
  relates_to: [CA-R-1835, CA-R-1836, CA-O-134, CA-O-137, CA-R-1387, CA-E-432, CA-E-433]
---
# Summary

Enforce projection quality and truthful outcomes

## Scope

The common quality gate and result disposition of the two graph builders.

## Claim

`GENERATE_ENTITY_GRAPH` **must not** report final `built` or `no_op` completion when any required selection, source, fidelity, graph-validity, currentness, permission, persistence, or recording condition is unmet.

## Details

The result carries stable, sorted graph data plus a per-condition disposition: `pass`, `fail`, `unresolved`, or `not_applicable`, with source references and diagnostics. Complete requested coverage, exact source frontier/settings digest, graph-kind namespace, validation disposition, output identity/revision if persisted, and non-authoritative status are mandatory result fields. Any admitted derived fact context retains its binding to the exact source evidence under CA-D-539; its presence does not establish missing authority or currentness. Identical readable source bytes and settings produce byte-identical semantic output in stable canonical order. Actual Run identities and Journal receipt references remain execution evidence, not a reason to change otherwise identical semantic graph data.

Unknown/malformed/unreadable regions, stale inputs/prior projections, unresolved endpoints, conflicts, cycles, self-references, and cardinality defects are never silently omitted, repaired, converted to absence, or used to widen the selection. An explicitly evidenced empty selection is checked against the same quality conditions; it is not a substitute for absent or unreadable source evidence. `no_op` additionally proves that an existing output matches the exact current request and passed all required checks. A non-persisting description, capability or permission failure, ambiguous destination, unresolved Journal receipt, or stale output is not `no_op`.

Immediately before publication, the builder rechecks that every bound selected source identity, Revision, location, and digest is unchanged, including the settings and any admitted derived context's source bindings; a mismatch returns `stale` or `blocked` and never silently substitutes, repairs, or modifies source authority. The builder may publish only to an authorized explicit derived-output destination or one current, unambiguously registered destination for the requested graph. A configured projection root or a conventional filename does not register a destination. Without either admitted destination, permitted description/generation remains non-persisting; an Action requiring an unresolved target remains blocked. The builder rejects authority/Journal destinations, traversal, symlink escape, ambiguity, and authoritative-output requests.

Persistence effects reflect the observed destination and actual write: `created` and `replaced` are distinguished by the destination's prior state, not by whether optional prior-output evidence was supplied. A failure before replacement retains the prior output; a failure after an actual effect retains that effect's evidence. An uncertain effect is reported as uncertain rather than invented as success or absence. An accepted complete target is not replaced by an unapproved partial result.

A trusted confirmed Action-start context permits the admitted construction; it does not prove terminal recording. Successful construction evidence remains provisional until the shared recorder confirms the required terminal events. A terminal recording failure or pending receipt retains the real output identity/revision, effects and confirmed references while exposing the recording blocker or `recording_pending` state, with no final `built`/`no_op` completion or completed Action/Workflow claim. Recording-only recovery never replays the construction or fabricates a no-op Artifact change.

### Sources

- CA-O-134 and CA-O-137, result/effects clauses, at the exact revisions admitted for the work.
- CA-R-1387 v8, CA-M-259 v8, CA-E-432 v7, and CA-E-433 v8.
