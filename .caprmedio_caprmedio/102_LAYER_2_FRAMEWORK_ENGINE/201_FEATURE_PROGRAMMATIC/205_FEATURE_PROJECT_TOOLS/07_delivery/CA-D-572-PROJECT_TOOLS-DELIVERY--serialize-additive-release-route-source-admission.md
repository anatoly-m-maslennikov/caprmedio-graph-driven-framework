---
atom_id: CA-D-572
content_role: Delivery
current_scope_unit: PROJECT_TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 36
updated_at: "2026-10-10 19:05:35 +0400"
subjects:
  governs: "Project Tool/RELEASE_VERSION/Additive selected-route source admission"
  depends_on: [Tool, Workflow, Action, Manifest, Operator, Run, Journal]
relations:
  delivery_for: [CA-R-1876, CA-R-1877, CA-R-1878, CA-R-1879, CA-M-331, CA-M-332]
---
# Summary

Serialize additive Release route source admission

## Scope

The one Project-local Release Version source-admission record required before
the canonical selected-workflow manifest admits `release_version`.

## Claim

A successor of `.caprmedio_caprmedio/_projection/selected_workflow_bindings.json`
**must** admit `release_version` only through one closed
`release_source_admissions` record. At manifest build, that record derives its
current Workflow definition Pin from active Project-local CA-O-164 and derives
its ordered Step and Action definition Pins from CA-O-164's declared Steps
table. It derives each Pin's exact `atom_id`, positive integer `version`, safe
Project-relative `source_path`, and lowercase 64-hex `digest` from the unique
active registered Project authoring carrier. This Delivery declares neither
installed-copy paths nor copied digest constants.

## Details

`release_source_admissions` is an optional top-level array in the loaded
canonical `.caprmedio_caprmedio/_projection/selected_workflow_bindings.json`
manifest. It is never a member of D527's two-field `definition_manifest`. A
manifest containing `release_version` has exactly one record; one without that
route has none. No unknown member is accepted. Its record retains the existing
schema fields `route`, `acceptance_frontier`, `workflow`, `ordered_steps`,
`ordered_actions`, `rmed_frontier`, `mutation_capable`, and
`native_action_calls`; `route` is exactly `release_version`,
`mutation_capable` is exactly `true`, and `native_action_calls` is exactly
`[]`.

The resolver opens current Project-local CA-O-164, verifies it is the unique
active `Workflow` definition, and derives the entry Workflow Pin and ordered
Step/Action graph directly from its declared table. It refuses absent,
ambiguous, inactive, malformed, reordered, duplicate, unregistered, unsafe,
or unreadable definitions. It must not read an installed Methodology copy,
preserve an old definition digest, infer a graph, or select a checkout fallback.
`acceptance_frontier` remains the existing schema field for the one current
Operator command; it is not a Task status, review, separate approval, or
separate source-admission command.

The current RMED membership is definition-ID-only. At manifest build the same
resolver derives every member Pin from current registered authoring, preserving
the table's role and order. A missing or wrong-role member refuses the route;
this carrier neither supplies a version/path/digest constant nor pins itself.

| role | position | atom_id |
| --- | ---: | --- |
| requirements | 1 | CA-R-1876 |
| requirements | 2 | CA-R-1877 |
| requirements | 3 | CA-R-1878 |
| requirements | 4 | CA-R-1879 |
| requirements | 5 | CA-R-1880 |
| requirements | 6 | CA-R-1886 |
| requirements | 7 | CA-R-1887 |
| requirements | 8 | CA-R-1890 |
| methods | 1 | CA-M-331 |
| methods | 2 | CA-M-332 |
| methods | 3 | CA-M-333 |
| methods | 4 | CA-M-343 |
| methods | 5 | CA-M-344 |
| methods | 6 | CA-M-346 |
| evaluations | 1 | CA-E-571 |
| evaluations | 2 | CA-E-572 |
| evaluations | 3 | CA-E-573 |
| evaluations | 4 | CA-E-574 |
| evaluations | 5 | CA-E-586 |
| evaluations | 6 | CA-E-587 |
| evaluations | 7 | CA-E-589 |
| deliveries | 1 | CA-D-560 |
| deliveries | 2 | CA-D-561 |
| deliveries | 3 | CA-D-562 |
| deliveries | 4 | CA-D-563 |
| deliveries | 5 | CA-D-564 |
| deliveries | 6 | CA-D-566 |
| deliveries | 7 | CA-D-567 |
| deliveries | 8 | CA-D-571 |
| deliveries | 9 | CA-D-573 |
| deliveries | 10 | CA-D-574 |
| deliveries | 11 | CA-D-579 |
| deliveries | 12 | CA-D-580 |
| deliveries | 13 | CA-D-582 |

An admitted successor is refreshed only through the existing verified
Operator-commanded manifest process. Current definition Pins may change only
through current registered source derivation while the route identity,
definition-derived ordered graph, entry Step, result edges, and typed metadata
continue to match CA-O-164. Structural changes require their own authority and
cannot use a pin refresh. Existing preview, authorization, source-currentness,
write-readback, and Journal-recording checks remain required; refresh itself
does not execute the Release Workflow.

The record is source-admission serialization only. It does not create a second
Workflow graph, executor, permission grant, generic effect schema,
caller-supplied approval, Run, queue intent, Journal Event, compiler result,
package effect, or release completion. The existing unknown-effect resolver and
private implementation package inventory remain separately governed by their
own active sources; this Project Tool carrier does not restate their paths or
hashes. Executable code neither replaces nor derives definition revisions.
