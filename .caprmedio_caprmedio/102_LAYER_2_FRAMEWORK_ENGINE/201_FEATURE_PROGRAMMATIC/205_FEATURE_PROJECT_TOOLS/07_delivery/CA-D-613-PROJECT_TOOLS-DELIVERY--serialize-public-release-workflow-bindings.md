---
atom_id: "CA-D-613"
content_role: "Delivery"
current_scope_unit: PROJECT_TOOLS
claim_target_scope_unit: PROJECT_TOOLS
local_tier: "Standard"
global_tier: 11
author: "Anatoly Maslennikov"
status: "Active"
subjects:
  governs: "Public release Workflow bindings"
  depends_on: [Workflow, Step, Action, Tool]
version: 8
updated_at: "2026-10-14 12:27:48 +0000"
relations: {}
---
# Summary

Serialize public-release Workflow bindings

## Scope

the definition identities of one public-release execution.

## Claim

the canonical selected-workflow manifest **must** admit `public.release` only through one closed `public_release_source_admissions` record. Its exact fields are `route`, `workflow`, `ordered_steps`, `ordered_actions`, `rmed_frontier`, `mutation_capable`, and `native_action_calls`; `route` is exactly `public.release`, `mutation_capable` is exactly `true`, and `native_action_calls` is exactly `[]`. The record binds CA-O-188 and exactly four ordered Step/Action pairs: CA-O-189/CA-O-190, CA-O-191/CA-O-192, CA-O-195/CA-O-196 and CA-O-197/CA-O-198 before native dispatch.

## Details

`public_release_source_admissions` is a JSON-compatible array of exactly one
closed object. Its fields are exactly the seven Claim fields, with no unknown
field. The tables below are ordered definition-ID membership, not serialized
Pins. At manifest build, the resolver must derive each member's exact
`atom_id`, positive integer `version`, safe Project-relative `source_path`, and
lowercase 64-hexadecimal `sha256` from the unique active Atom registered in the
current Project authoring source set. It must reject a missing, duplicate,
wrong-role, unregistered, reordered, or unreadable member before it emits the
record. The emitted `workflow`, paired `ordered_steps`/`ordered_actions`, and
`rmed_frontier` Pins retain exactly the membership and positions below; no
version, path, or digest is declared by this Delivery Atom.

`rmed_frontier` is a closed object whose keys are exactly `requirements`,
`methods`, `evaluations`, and `deliveries`, each an ordered array of its derived
Pins. No Task, Task Done status, separate acceptance, or worker-review condition is an execution prerequisite. Current RMED and Operation Pins are source evidence, not execution success or authorization. One exact Operator command covers the Workflow and Actions. Before its first public effect, the native Tool completes and retains the fresh complete public suite required by CA-M-365/CA-M-366 against its current selected source and prepared material bindings. Actual-URL/history-only finalization verifies unchanged non-metadata inputs and reopens the same actual test/source/material evidence without another suite or writing prompt. This is internal native work, not a restored CA-O-193/CA-O-194 Step, a typed Public Full Gate, or a CA-D-566/local-promotion bridge.

#### `workflow`

| position | atom_id |
| ---: | --- |
| 1 | CA-O-188 |

#### `ordered_steps` and `ordered_actions`

The arrays have exactly the following paired positions.

| position | step_atom_id | action_atom_id |
| ---: | --- | --- |
| 1 | CA-O-189 | CA-O-190 |
| 2 | CA-O-191 | CA-O-192 |
| 3 | CA-O-195 | CA-O-196 |
| 4 | CA-O-197 | CA-O-198 |

#### `rmed_frontier`

| collection | position | atom_id |
| --- | ---: | --- |
| requirements | 1 | CA-R-1920 |
| requirements | 2 | CA-R-1921 |
| requirements | 3 | CA-R-1923 |
| requirements | 4 | CA-R-1925 |
| requirements | 5 | CA-R-1926 |
| requirements | 6 | CA-R-1927 |
| requirements | 7 | CA-R-1928 |
| methods | 1 | CA-M-365 |
| methods | 2 | CA-M-366 |
| methods | 3 | CA-M-368 |
| evaluations | 1 | CA-E-610 |
| evaluations | 2 | CA-E-611 |
| evaluations | 3 | CA-E-612 |
| evaluations | 4 | CA-E-613 |
| evaluations | 5 | CA-E-615 |
| evaluations | 6 | CA-E-616 |
| evaluations | 7 | CA-E-617 |
| evaluations | 8 | CA-E-618 |
| deliveries | 1 | CA-D-610 |
| deliveries | 2 | CA-D-611 |
| deliveries | 3 | CA-D-612 |
| deliveries | 4 | CA-D-616 |
| deliveries | 5 | CA-D-617 |
| deliveries | 6 | CA-D-618 |

CA-D-613 itself is deliberately absent from `rmed_frontier`: a record must not
pin its own carrier. The derived Operation and RMED Pins contain no canonical-
manifest digest, caller authorization, Run result, output digest, or cross-hash
cycle.

The record is the public Release admission in the complete common registry. It does not replace CA-D-547's current `release_source_admissions` record or the local `release_version` graph; the whole registry and both records pass one gate together. The selected request retains CA-D-527's existing
two-field `definition_manifest`; it never carries this admission record or a
second manifest binding. The sequence remains source-controlled Operations
authority; executable code neither replaces nor derives definition revisions.
