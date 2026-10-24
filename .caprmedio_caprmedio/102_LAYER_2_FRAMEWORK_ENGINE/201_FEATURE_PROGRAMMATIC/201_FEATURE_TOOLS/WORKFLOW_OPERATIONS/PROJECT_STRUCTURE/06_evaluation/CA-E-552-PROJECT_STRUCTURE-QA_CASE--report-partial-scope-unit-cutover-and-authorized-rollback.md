---
atom_id: CA-E-552
content_role: Evaluation
type: Eval Case
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
status: Active
author: Anatoly Maslennikov
version: 6
updated_at: 2026-10-24 00:51:05 +0400
subjects:
  governs: Subject/Domain/Node/Continuant/Scope Unit
  depends_on:
  - Subject/Engineering/Project Structure
  - Subject/Domain/Node/Continuant/Scope Unit
  - Subject/Domain/Node/Continuant/Project.Structure
  - Subject/Engineering/Carrier
  - Subject/Domain/Node/Continuant/History/Journal
relations:
  relates_to:
  - CA-R-1662
  - CA-R-1831
  - CA-R-1832
tier: 3
---
# Summary

Report partial Scope Unit cutover and authorized rollback

## Scope

An injected post-declaration failure inside one authorized recoverable cutover entered through CA-D-527's shared service interface.

## Claim

The Evaluation **must** prove partial effects and rollback are reported precisely, separately from service disposition/Run outcome, and no unapproved content is erased.

## Details

- Start the explicitly authorized D527 `execute`, then cause a reference-repair or explicitly included Carrier update to fail after a known declaration effect. Assert D527 carries the started service evidence while `structural_result.state = partial` lists applied/unapplied effects, preservation/breakage, and only the pre-authorized recovery boundary; assert no structural completion claim.
- Exercise the authorized rollback through the same shared contract and assert `structural_result.state = rolled_back` identifies restored and still-broken members. Retain required history/evidence, never reset or overwrite concurrent work, and do not treat a service terminal disposition as a structural success claim.
