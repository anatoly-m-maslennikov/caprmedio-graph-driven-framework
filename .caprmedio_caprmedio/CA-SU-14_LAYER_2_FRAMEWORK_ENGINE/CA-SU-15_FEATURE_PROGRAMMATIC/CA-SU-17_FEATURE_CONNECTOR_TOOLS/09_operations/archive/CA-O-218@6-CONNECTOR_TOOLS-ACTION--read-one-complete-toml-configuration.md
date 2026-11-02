---
atom_id: CA-O-218@6
content_role: Operations
type: Action
current_scope_unit: CONNECTOR_TOOLS
claim_target_scope_unit: CONNECTOR_TOOLS
status: Archived
author: Anatoly Maslennikov
version: 6
updated_at: 2026-10-25 17:32:27 +0400
subjects:
  governs: Subject/Graph Node/Domain/Continuant/Governing Configuration
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Project
  - Subject/Graph Node/Engineering/Project Structure Declaration
  - Subject/Graph Node/Engineering/Project Settings Snapshot
relations:
  relates_to:
  - CA-R-1942
  - CA-M-382
  - CA-E-634
  - CA-D-631
  - CA-R-1936
  - CA-M-376
  - CA-D-625
  - CA-O-204
  - CA-M-375
  - CA-O-219
  - CA-O-220
tier: 3
---
# Summary

Read one complete TOML configuration

## Operation

Read One Complete TOML Configuration **means** the independent effect-free `read` Action of the same shared TOML connector whose `modify` Action is CA-O-204. CA-D-631 supplies its exact logical input/output refinement; CA-D-625 supplies the unchanged common envelope.

### Action

1. check the closed Read request, explicit Configuration identity, bound Project/source/schema authority **and** read permission. reject missing, ambiguous, unsupported **or** denied bindings **before** returning source content.
2. resolve **only** that logical target **to** its private authoritative TOML source. obtain complete exact source text, reject duplicate keys **and** verify the complete parsed document against the supplied applicable schema **and** declared-version constraints. do **not** choose a schema **or** fallback source.
3. verify a coherent observation of source text, parsed values **and** actual source-state evidence. enforce the supplied pin **or** historical view exactly; unpinned current Read returns actual evidence **without** requiring a pre-known token.
4. return CA-D-631's complete data/state, empty normal effects **and** precise errors. unavailable content is null; stale, invalid, denied **or** incomplete results never become success. preserve truthful unexpected effect evidence under CA-D-625.

## Details

CA-O-219 **and** CA-O-220 bind this Action for their respective configuration Workflows. it remains independently callable **without** a Workflow **or** earlier Query. Read does **not** grant permission for Modify **or** create any configuration/history/runtime effect. existing shared Run recording remains separate from configuration mutation.

this is a required source operation, **not** an executable binding **or** live admission. exact realization/definition/source pins, permission **and** applicable CA-R-1525/CA-R-1720 Run recording remain prerequisites for execution. retry, publication, Core adoption **and** migration remain outside this change.
