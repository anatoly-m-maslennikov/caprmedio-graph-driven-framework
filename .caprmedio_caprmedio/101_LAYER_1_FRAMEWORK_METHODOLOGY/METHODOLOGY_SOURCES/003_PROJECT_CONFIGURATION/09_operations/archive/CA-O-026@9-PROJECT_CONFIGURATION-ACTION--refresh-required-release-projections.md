---
subjects:
  governs: Subject/Domain/Node/Continuant/Scope Unit//PROJECT_CONFIGURATION
  depends_on:
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - Subject/Domain/Node/Continuant/Projection
  - Artifact/Revision
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
  - Subject/Domain/Node/Continuant/History/Journal.Record
  - 'Subject/Domain/Node/Continuant/Projection/Type: Reconciled Projection'
  - 'Subject/Domain/Node/Continuant/Projection/Type: Applicable Methodology'
  - Subject/Domain/Node/Continuant/Atom.Substance
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Delivery'
version: 9
updated_at: 2026-10-24 00:51:05 +0400
relations:
  relates_to:
  - CA-O-025
  - CA-O-010
  - CA-O-011
  - CA-R-1460
atom_id: CA-O-026@9
content_role: Operations
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Archived
author: Anatoly Maslennikov
type: Action
tier: 3
---
# Refresh required release Projections

Refresh Required Release Projections **means** the Action that makes the selected release candidate's required Projections current under their existing governing authority.

1. resolve the exact required Projection set **and** its source Revisions from the selected release gates.
2. retain an existing Projection **when** its governing currentness check passes for those sources; **otherwise** execute its registered derivation **and** Delivery procedure.
3. use the applicable reconciliation Workflow for a Reconciled Projection, including CA-O-011 for Applicable Methodology. do **not** change projected Claims **to** fix source conflicts.
4. check the resulting Projection against its own required Evaluations **and** current source binding.
5. return the exact checked results **or** the blocking failure; preserve actual execution evidence **in** the shared Journal.

an enabled Projection **not** required by the selected gate does **not** require refresh merely because an Atom changed. unresolved source conflicts, changed source bindings, failed publication, **or** missing required checks block success. this Action does **not** select a new Projection contract, authorize source corrections, **or** infer release readiness from successful refresh alone.
