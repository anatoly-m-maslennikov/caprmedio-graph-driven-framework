---
cce_version: cce_1
cce_form: definition
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Data Handling/Source Retrieval
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Term//Artifact
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Analysis'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Content
  - Subject/CAPRMEDIO/Carrier
version: 16
updated_at: 2026-10-27 19:59:44 +0400
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
atom_id: CA-O-035
status: Active
content_role: Operations
author: Anatoly Maslennikov
current_scope_unit: TOOLS
type: Action
tier: 1
---
# Ingest one external Analysis

Ingest External Analysis **means** the reusable Action that produces one attributable external-Analysis envelope **without** adopting its Claims as Project authority under CA-R-1145. its modeled boundary is the complete requested result; partial comparison, incomplete attribution, **or** an unreported unresolved input is **not** an independently successful outcome.

## Applicable when

use this Action **when** one external review **or** Analysis **must** be represented within a bounded project-analysis frontier **without** becoming accepted project authority.

## Action

1. resolve the external Analysis source identity, source digest, transformation session, **and** exact target frontier.
2. preserve the imported content **in** a provenance envelope that identifies its source, target frontier, **and** **all** declared transformations.
3. mark **every** imported claim as non-authoritative **and** require a separate governed adoption decision **before** **any** accepted project authority is created **or** revised.
4. return the envelope **and** explicit provenance links **without** editing source carriers **or** target authority.
5. reject a missing source identity, source digest, target frontier, **or** transformation provenance rather than filling it with inference.

## Outcome

one external Analysis is represented **in** an attributable bounded provenance envelope while its claims remain distinct from accepted project authority.

## Failure or stop

do **not** ingest an Analysis with incomplete provenance **and** do **not** create, revise, **or** imply adoption of **any** project authority.
