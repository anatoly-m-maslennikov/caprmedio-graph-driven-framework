---
atom_id: CA-E-326
ref_id: CA-E-326
container:
  scope_unit: CA-SU-16
role: Evaluation
form: Eval Case
topics:
  main_subject: "Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Storage"
tier: 2
relations:
  evaluation_for:
  - CA-M-208
status: Active
version: 20
updated_at: 2026-11-02 19:44:26 +0400
cce_version: cce_1
cce_form: evaluation
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: TOOLS
---
# Verify patch generic Artifact metadata

## Claim checked

CA-M-208 applies **only** schema-valid generic Artifact frontmatter patches while preserving body, identity, **and** atomicity.

## Applicable when

apply whenever generic frontmatter patch mechanics **or** schemas change.

## Test case

seal one Artifact with known body bytes. request one valid field change together with one unknown field; observe apply, **then** remove the unknown field **and** apply the sealed valid patch.

## Acceptance criteria

the invalid patch changes nothing; the valid patch changes **only** the declared frontmatter field, advances revision once, **and** preserves body bytes, path, filename, **and** identity.

## Failure disposition

reject the realization **and** preserve schema, patch operations, exact diff, revision, **and** body digest.
