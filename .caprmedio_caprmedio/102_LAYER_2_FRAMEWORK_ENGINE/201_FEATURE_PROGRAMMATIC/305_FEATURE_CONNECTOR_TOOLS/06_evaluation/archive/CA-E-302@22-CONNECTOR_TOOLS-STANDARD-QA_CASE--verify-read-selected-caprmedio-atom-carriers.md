---
claim_target_scope_unit: CONNECTOR_TOOLS
current_scope_unit: CONNECTOR_TOOLS
content_role: Evaluation
atom_id: CA-E-302@22
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: Subject/Engineering/Tool//ATOM_READ
  depends_on:
  - Subject/Domain/Node/Continuant/Atom
  - Subject/Engineering/Carrier
  - Subject/Domain/Node/Continuant/Scope Unit
version: 22
status: Archived
updated_at: 2026-10-24 03:08:30 +0400
relations:
  evaluation_for:
  - CA-R-864
  - CA-O-047
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
tier: 4
type: Eval Case
author: Anatoly Maslennikov
---
# Verify read selected caprmedio atom carriers

## Claim checked

CA-O-047 reads one logical Atom by its explicit full ID in the source view fixed by the bound target/context and returns that complete state with its actual exact Version faithfully, without invoking Find or Modify or changing it.

## Applicable when

This primitive uses CA-D-625's coherent logical connector interface. The bound caller context supplies the requested scope, source view, permission and applicable validation authority; the connector checks them mechanically. It does not choose Atom identity, Version changes, lifecycle, defaults or a configuration schema.

Apply before relying on the logical Read connector. These are required future checks; this source records no observed implementation pass.

## Test case

Prepare two identified Atoms and an archived historical Version of one. Independently read each explicit full ID without a pre-known Version and verify the returned actual exact Version and source-state evidence. Also read exact ID/Version pairs when Version or expected state is supplied. Compare all returned Properties, sections and identity/lifecycle facts with independently authored expected complete states. A current-state request must not silently return a historical state, and a historical request must not silently substitute the current Version. The file adapter may use a physical locator internally; path, filename and filename stem are not substitutes for explicit logical identity. A requested historical or pinned Version must match exactly; omitted Version never triggers an implicit Find.

## Additional resolution cases

Request a missing ID, wrong supplied Version, ambiguous identity, unreadable state, unsupported output shape and denied read scope. Attribute each failure to the exact request; never guess or widen the selection. A list of reads is ordered independent requests: stop at the first failure, retain earlier returned states and leave later requests unperformed. Read performs no mutation. Find returns matches only, and no read result triggers Modify.

## Acceptance criteria

Each accepted result is the complete requested Atom state with its exact ID, actual Version and source-state evidence. Supplied Version/expected state is verified exactly; ambiguous source views fail. Properties and sections are faithful; physical storage details do not change logical identity. Invalid or unresolved targets produce explicit failures, and every source byte and existing history item remains unchanged.

## Failure disposition

Reject on wrong identity/Version, incomplete content, hidden ambiguity, implicit Find/Modify, widened access or any mutation. Retain requests, expected/actual complete states, source pins and independent before/after observations.
