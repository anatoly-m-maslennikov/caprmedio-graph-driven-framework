---
atom_id: CA-O-draft
role: Operations
form: Action
status: Draft
version: 1
updated_at: '2026-11-03 18:54:48 +0400'
tier: 3
subjects:
  active: 'CAPRMEDIO_MODEL <+ Atom/(.Role := Operations)/Action'
  passive:
    - 'CAPRMEDIO_MODEL <+ Atom'
    - 'CAPRMEDIO_STRUCTURE <+ Scope Unit//PROJECT_CONFIGURATION'
relations: {}
---
## Summary

Promote one Atom Draft

## Claim scope

This Action publishes one exact selected Draft for one non-container Atom under the applicable model. It rejects semantic containers, descendants, and cascades, and it never archives a Current as an implicit promotion precondition.

## Claim

Promote One Atom Draft **means** the reusable Action that validates and publishes one selected Draft into its canonical Current destination. It preserves the proposal's content, Role, and meaning, requires an explicit target Status admitted as Current by the applicable qualified model, and removes the Draft surface only after publication is verified.

## Details

1. Validate the exact selected Draft, complete proposed content/Role/meaning, destination placement, and explicit target Status. Reject missing, ambiguous, stale, invalid, or container targets with attributable diagnostics; do not select descendants.
2. Keep the identity chosen by the proposal. A new role-only marker receives a fresh, never-reused canonical ID. An existing-Atom Draft retains its exact target ID and proposed Version already selected before any archive step. An explicitly bound already-archived predecessor may validate the expected `N -> N+1` relationship; never restore an ID by searching history or inferring lineage.
3. Require the canonical Current destination to be empty before publication. An existing Current, destination collision, or conflicting placement returns a collision/handoff to the composed Update Workflow without invoking it and never overwrites another target.
4. Materialize the Current with the proposal's content, Role, meaning, exact identity, proposed Version, explicit model-admitted Current Status, and the actual Project-time publication instant as Updated At. Do not hardcode `Active`, upgrade tier or scope, or perform archival here; any predecessor archival is a separate selected Workflow whose verified result may be checked.
5. Verify the published Current and only then remove the selected Draft surface. If verification or cleanup is incomplete, retain the actual completed effects and report partial or unknown evidence; do not retry or roll back automatically.
6. A Journal or history record is not a permission, completeness, or success gate. Any Journal attempt records the actual business event only. Return the actual publication, collision/handoff, diagnostic, partial, or unknown result and preserve its evidence.

