---
atom_id: CA-E-417
ref_id: CA-E-417
container:
  scope_unit: CA-SU-16
role: Evaluation
form: Eval Case
topics:
  main_subject: "Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Data Handling/Data Validation"
  dependencies:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Term//Artifact
  - Subject/CAPRMEDIO/Carrier
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal.Record
tier: 2
relations:
  evaluation_for:
  - CA-R-1146
  - CA-O-036
status: Active
version: 23
updated_at: 2026-10-27 19:59:34 +0400
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: TOOLS
---
# Verify reconcile declared provenance

## Claim checked

CA-O-036 read-only classifies declared provenance links as current, missing, conflicting, stale, **or** unverifiable **without** inferring repair **or** adoption.

## Applicable when

apply whenever declared-provenance comparison **or** finding classification changes.

## Test case

select Artifacts whose declared source, draft, session, revision, **and** digest links together contain one current, missing, conflicting, stale, **and** unverifiable case. reconcile them **and** compare **all** selected carriers **before** **and** **after**.

## Acceptance criteria

the result assigns **every** case exactly its corresponding classification with attributable source evidence. no selected Artifact changes, no link is repaired, **and** no adoption decision is created.

## Failure disposition

reject the realization **and** preserve selected carriers, declared links, observed targets, classifications, before-and-after digests, **and** no-mutation proof.
