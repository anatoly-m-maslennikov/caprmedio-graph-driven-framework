---
atom_id: "CA-O-188"
content_role: Operations
type: Workflow
current_scope_unit: "PROJECT_CONFIGURATION"
claim_target_scope_unit: "PROJECT_CONFIGURATION"
local_tier: "Standard"
global_tier: 11
status: "Active"
author: "Anatoly Maslennikov"
subjects:
  governs: "Release a selected public Version"
  depends_on: [Operator, Version, README, Pull Request, Version History, Full Gate, Journal, Tool]
version: 2
updated_at: "2026-10-09 21:50:26 +0400"
relations:
  relates_to: [CA-R-1920, CA-R-1924, CA-R-1925, CA-R-1926, CA-R-1927, CA-R-1928, CA-R-1929]
  invokes: [CA-O-189, CA-O-191, CA-O-193, CA-O-195, CA-O-197]
---
# Summary

Release a selected public Version

## Operation

Release a selected public Version **means** the **Operator**-invoked, non-recursive Workflow that prepares one selected Version for the personal remote from `amm/dev` to `main`, creates or updates its public Pull Request, and never merges it.

## Scope

One selected Version, one personal remote identity, `amm/dev`, `main`, the selected README, full PR description, concise Version History entry, source proofs, typed current Full Gate evidence, and their Journal Run lineage.

## Steps

| Step | Action | Result boundary |
| --- | --- | --- |
| CA-O-189 | CA-O-190 | discover at most one matching open PR before freeze |
| CA-O-191 | CA-O-192 | prepare README and full PR material; include a Version History link only when its actual PR URL is already known |
| CA-O-193 | CA-O-194 | freeze the selected source closure and pass its typed current Full Gate |
| CA-O-195 | CA-O-196 | commit/push the gated closure and find, create, or update its `main` PR |
| CA-O-197 | CA-O-198 | finalize a newly known actual PR link, renew the gate, then follow up push and PR refresh when the snapshot changed |

## Transitions

| Step result | Next result |
| --- | --- |
| a unique existing matching PR or no matching PR is evidenced | CA-O-191 |
| material source proof is complete and any existing link is actual | CA-O-193 |
| full gate is typed, current, passed, and sealed for that source proof | CA-O-195 |
| immutable push proof and one actual open PR URL are evidenced | CA-O-197 |
| unchanged history closure, or a changed history closure with renewed gate, follow-up push, and refreshed same PR | complete |
| missing, stale, duplicate, unauthorized, unsafe, failed, partial, or uncertain result | stop with actual evidence; do not merge or replay remote effects |

## Details

This Workflow starts only on the Operator's command for the selected public-release Run. Source admission and local-release completion do not start it. One Operator command may explicitly select admission and release together; only those selected operations are authorized. Internal Steps follow the graph within the commanded Run, and the required gates still apply.

Every invoked Workflow, Step, and Action Run carries actual definition revisions, parent lineage, input/result/effect/report references, and truthful started or terminal Journal evidence under CA-R-1928. Tool calls are evidence attached to their parent Step and Action; they are not a fourth Tool Run kind. This Workflow invokes native bindings only after their registry admission. It grants no current GitHub write, merge, secret, credential, source-authority replacement, or implicit retry authority.
