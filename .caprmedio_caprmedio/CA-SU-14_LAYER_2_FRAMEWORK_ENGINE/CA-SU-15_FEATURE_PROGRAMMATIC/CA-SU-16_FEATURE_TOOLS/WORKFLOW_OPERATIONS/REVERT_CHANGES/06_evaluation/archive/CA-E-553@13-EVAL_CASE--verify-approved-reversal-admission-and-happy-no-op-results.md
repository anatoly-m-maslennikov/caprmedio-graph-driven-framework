---
atom_id: CA-E-553@13
content_role: Evaluation
type: Eval Case
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
status: Archived
author: Anatoly Maslennikov
version: 13
updated_at: 2026-10-27 06:04:45 +0400
subjects:
  governs: Subject/Graph Node/Engineering/Verification/Dynamic Testing
  depends_on:
  - Subject/Graph Node/Implementation/Code/Tool
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action'
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: Operator'
  - Subject/Graph Node/Domain/Continuant/Term//Artifact
  - Subject/Graph Node/Domain/Continuant/History/Journal
  - Subject/Graph Node/Domain/Occurrent/Execution/Workflow Run
  - Subject/Graph Node/Domain/Occurrent/Execution/Step Run
relations:
  evaluation_for:
  - CA-R-1833
  - CA-R-1834
tier: 4
---
# Summary

Verify approved reversal admission and happy/no-op results

## Scope

Functional mocked Project/MCP cases for REVERT_CHANGES manifest admission, exact happy reversal, no-op, pre-effect rejection, and cancellation admission.

## Claim

Every realization **must** prove that only the exact approved manifest can reach guarded execution, and that admitted/no-op/reverted results remain distinct from a mutation or Journal-completion claim.

## Details

Use a functional Project mock with governed effect adapters and real exposed MCP request/response validation. The happy case supplies one complete approval, current target/reference hashes, permissions, ordered effects, and preservation evidence; it expects `admitted`, then `reverted`, each approved effect once, retained prior history/reference evidence, and shared Run/Journal receipt references. It must assert no automatic inverse beyond the ordered manifest.

The already-satisfied case supplies the same complete approval and current evidence, expects `no_op`, zero applied effects, no fictitious mutation, and truthful shared Run evidence. Independently reject missing approval, altered effect ordering, missing before/after evidence, revoked permission, unsupported effect, or a stale target/reference/governing hash before any effect. Each returns `blocked`, names the precise binding, leaves targets/history/reference and effects unchanged, and creates no invented Action Run when dispatch never started.

For cancellation admission, use the real exposed MCP request/response surface to submit an Operator-admitted cancellation only after a confirmed safe boundary of the admitted manifest. Before the boundary, cancellation is refused without mutation and dispatch remains governed by the original admission. At the boundary, the MCP result is `canceled`, never `reverted` or `no_op`; it identifies the admitted manifest and safe boundary and preserves the exact effect account. The case supplies a Workflow-plus-Action execution path and verifies actual Workflow/Step/Action lineage rather than treating the MCP request as Run proof. It also verifies no automatic rollback, inverse, or replay is invoked by cancellation.

Acceptance compares full result, effect account, preserved evidence, mutation trace, and shared receipt references—not outcome text or count alone. This carrier records planned functional proof, not a runtime pass.

### Sources

- CA-R-1833; CA-R-1834; CA-O-130 v1; CA-O-131 v2; CA-O-132 v1; CA-P-1463 v1.
