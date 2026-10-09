# Core graph design checkpoint

The Epic now requires both derived RMED views:

- [R/M/E/D overview trees](rmed.roles.indented.txt).
- [Entity-centered tree with associated M/E/D](rmed.entities.indented.txt).

These are compact, literal Subject views. Associated M/E/D pointers are not yet proven applicability. Shared source references stay in [the exact view data](rmed.views.json). Empty M/E/D slots are omitted.

## Current review

All 294 old slash cases have a bounded current-content review: 247 are not asserted as native relations; 47 remain unresolved. Among them, 189 have evidenced display-only qualification candidates. No slash case was admitted as a native relation. See [the open questions](questions.md) before making semantic decisions.

The original baseline remains unchanged: 706 nodes, 4,534 Subject occurrences and 3,093 original relation segments. This checkpoint has not yet joined the full occurrence ledger or performed CA-P-1922 acceptance.

[The bounded structure design](structure.design.json) reviews 24 identities: 17 Continuant and three Occurrent display memberships, plus four non-temporal anchors. Six memberships follow the confirmed Operator display convention. It includes ten separately evidenced Term-taxonomy proposals and seven conditional common constraints. The remaining 682 nodes are explicitly unreviewed for whole-node disposition; CA-P-1907 owns that later work. No entity was deleted, generalized or adopted.

## Operator decisions and open distinction

The Operator confirmed Actor, Carrier and Scope Unit under Continuant as a display convention. Operator, File Carrier and Directory Carrier follow only their separately evidenced subtype links. This does not add native temporal taxonomy.

The Operator also named sessions and Workflow, Step and Action Runs as Occurrent examples. Actual activity, its reusable definition and its saved records are distinct. Session is outside the reviewed baseline and remains an unassessed example, not a new Core identity. Whether the Journal alone must store their representations, or preserves history alongside live/resumable state, is still a question. No ephemerality or Journal-only storage rule is adopted.

## Boundary

This is derived review evidence, not source authority, an accepted complete graph or an MCP Run. Core Atoms, Subjects, history and the Step 1 outputs are unchanged. Candidate acceptance and the separately authorized migration preview remain required.

[Checkpoint file pins](review.checkpoint.json) and [view explanation](rmed.views.md) preserve the exact inputs and evidence.
