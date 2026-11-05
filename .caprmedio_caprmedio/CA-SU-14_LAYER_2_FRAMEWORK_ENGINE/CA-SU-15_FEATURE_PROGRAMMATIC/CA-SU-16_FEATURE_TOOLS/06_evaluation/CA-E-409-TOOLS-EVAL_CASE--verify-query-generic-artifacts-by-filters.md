---
atom_id: CA-E-409
ref_id: CA-E-409
container:
  scope_unit: CA-SU-16
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Project Model/Selection
  dependencies:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Term//Artifact
  - Subject/CAPRMEDIO/Carrier
  - Subject/CAPRMEDIO/Graph/Relation
tier: 2
relations:
  evaluation_for:
  - CA-R-1135
  - CA-O-038
status: Active
version: 21
updated_at: 2026-10-27 19:59:34 +0400
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: TOOLS
---
# Verify query generic Artifacts by filters

## Claim checked

CA-O-038 returns **every** **and** **only** generic Artifact IDs **and** paths selected by composable supported filters **in** stable order **without** loading bodies.

## Applicable when

apply whenever generic Artifact filters, canonical identity selection, **or** stable query ordering changes.

## Test case

construct a bounded Artifact frontier spanning structural scopes, layers, Tiers, Features, Content roles, subject scopes, lifecycle states, **and** typed relations, with body-only sentinels. apply one composable filter set with known membership, **then** add one unsupported filter.

## Acceptance criteria

the supported query returns **only** the expected canonical IDs **and** paths once **in** stable order, with no body sentinel accessed **or** returned. the unsupported-filter query returns an explicit diagnostic **and** no partial accepted result.

## Failure disposition

reject the realization **and** preserve the frontier, filters, expected membership **and** order, body-access evidence, **and** unsupported-filter diagnostic.
