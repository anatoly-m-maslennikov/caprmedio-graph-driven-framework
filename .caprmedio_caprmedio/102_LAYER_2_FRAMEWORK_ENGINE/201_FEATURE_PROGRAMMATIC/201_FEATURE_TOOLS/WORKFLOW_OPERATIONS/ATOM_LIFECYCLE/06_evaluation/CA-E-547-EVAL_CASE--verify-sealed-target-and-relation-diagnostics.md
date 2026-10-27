---
atom_id: CA-E-547
content_role: Evaluation
type: Eval Case
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
author: Anatoly Maslennikov
status: Active
subjects:
  governs: Subject/Graph Node/Domain/Continuant/Atom
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Atom
  - Subject/Graph Relation
  - Subject/Graph Node/Engineering/Execution Control/Effect Authorization
version: 13
updated_at: 2026-10-27 06:04:45 +0400
relations:
  evaluation_for:
  - CA-R-1827
tier: 4
---
# Summary

Verify sealed target and Relation diagnostics

## Scope

One target/predecessor and active inbound/outgoing Relation handling.

## Claim

Exercise valid one-target preview, changed-after-seal rejection, absent MCP authorization rejection, and a model-admitted status-change/Archive result that breaks one active inbound and one active outgoing reference. Verify preview reports both references by identity, reason, and active-referrer status without mutation. Then apply the explicitly authorized sealed, current status request: verify the admitted status transition occurs, both broken references remain unretargeted, and the result directs their separate authorized repair. Also exercise an explicitly authorized sealed request whose structural/currentness checks pass.

## Details

### Acceptance criteria

Only an authorized, current request with valid structural/currentness controls may delegate mutation. Broken resulting active references are diagnostics and repair handoff for a model-admitted status transition, not a blanket veto; all rejected cases preserve the original frontier.
