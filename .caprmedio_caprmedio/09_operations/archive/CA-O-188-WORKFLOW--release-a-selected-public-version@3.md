---
atom_id: "CA-O-188"
content_role: Operations
type: Workflow
current_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
status: "Active"
author: "Anatoly Maslennikov"
subjects:
  governs: "Release a selected public Version"
  depends_on: [Operator, Version, README, Pull Request, Version History, Full Gate, Journal, Tool]
version: 3
updated_at: "2026-10-10 19:05:19 +0400"
relations:
  relates_to: [CA-R-1920, CA-R-1924, CA-R-1925, CA-R-1926, CA-R-1927, CA-R-1928, CA-R-1929]
  invokes: [CA-O-189, CA-O-191, CA-O-193, CA-O-195, CA-O-197]
---
# Summary

Release a selected public Version

## Operation

Release a selected public Version **means** the **Operator**-invoked, non-recursive Workflow that prepares one selected Version for the personal remote from `amm/dev` to `main`, creates or updates its public Pull Request, and never merges it.

## Scope

One selected Version, one personal remote identity, `amm/dev`, `main`, the selected README, one full PR description, one concise Version History summary, a fresh full-suite result, and Journal Run lineage.

## Steps

| Step | Action | Result boundary |
| --- | --- | --- |
| CA-O-189 | CA-O-190 | discover at most one matching open PR |
| CA-O-191 | CA-O-192 | make the one content prompt for the PR body and concise Version History summary |
| CA-O-193 | CA-O-194 | run a fresh full suite before public release |
| CA-O-195 | CA-O-196 | mechanically apply documentation and history, commit/push, and create or update its `main` PR |
| CA-O-197 | CA-O-198 | when newly known, append the exact PR URL mechanically and refresh that same PR |

## Transitions

| Step result | Next result |
| --- | --- |
| a unique existing matching PR or no matching PR is evidenced | CA-O-191 |
| one content result is complete | CA-O-193 |
| fresh full suite passes for the public closure | CA-O-195 |
| immutable push proof and one actual open PR URL are evidenced | CA-O-197 |
| exact URL is already present, or mechanically appended and pushed to the same PR | complete |
| missing, stale, duplicate, unauthorized, unsafe, failed, partial, or uncertain result | stop with actual evidence; do not merge or replay remote effects |

## Details

This Workflow starts only on the Operator's command for the selected public-release Run. CA-O-192 is its sole content prompt; README, Version History, Git, and PR mechanics are programmatic. Its initial fresh full suite is its own public-release gate and cannot reuse Local Release evidence. A code, Methodology, or package change after that suite requires a fresh full suite before public release. Adding only the actual PR URL after the PR exists requires its mechanical follow-up commit and push, not a repeated suite. It never merges.

Every invoked Workflow, Step, and Action Run carries actual definition revisions, parent lineage, input/result/effect/report references, and truthful started or terminal Journal evidence under CA-R-1928. Tool calls are evidence attached to their parent Step and Action; they are not a fourth Tool Run kind. This Workflow invokes native bindings only after their registry admission. It grants no current GitHub write, merge, secret, credential, source-authority replacement, or implicit retry authority.
