---
atom_id: CA-E-569
ref_id: CA-E-569
role: Evaluation
form: Eval Case
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
status: Active
author: Anatoly Maslennikov
version: 14
updated_at: 2026-11-02 19:46:47 +0400
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Project Model/Selection
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Term//Artifact
  - 'Subject/CAPRMEDIO/Carrier/File.Format: Markdown'
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Data Handling/Source Retrieval
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Evaluation'
relations:
  evaluation_for:
  - CA-R-1849
  - CA-R-1850
tier: 4
container:
  scope_unit: CA-SU-16
carrier_destination:
  file:
    name: CA-E-569-TOOLS-EVAL_CASE--verify-artifact-query-and-selected-fetch.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-16_FEATURE_TOOLS/06_evaluation
---
# Summary

Verify Artifact query and selected fetch

## Scope

Golden QA for
`LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_TOOLS/FIND_AND_FETCH_ARTIFACTS/tests/test_find_and_fetch_artifacts.py`.

## Claim

The golden test **must** prove that FIND_AND_FETCH_ARTIFACTS returns only the
correct default IDs or explicitly selected fetch values from one stable
read-only snapshot, and truthfully rejects every unsupported or incomplete
case.

## Details

Fixture distinct frontmatter and section namespaces, equal spelling across them,
explicit null and absent fields, boolean-versus-number values, date-like strings,
typed arrays/maps, every status, nested headings containing slash/tilde, Atom
and non-Atom identities, and several IDs. Assert RFC 8259 literals, RFC 6901
pointer/heading escaping, and CA-R-1850's precedence and parentheses
for `NOT`, `AND`, and `OR`; equality, inequality, and `IN`; no implicit Active narrowing;
selected-only fetch; bytewise identity ordering; bounded cursor continuation
validating exact retained members without second enumeration; and changed-snapshot
cursor rejection. Independently exercise invalid grammar/type/JSON literal or
selector, SQL/code-like input, missing/conflicting/duplicate identity, malformed
frontmatter, duplicate key/heading, incomplete read, inaccessible root,
filename-only identity, secret-shaped selection, attempted mutation, and every
resolved query budget. Assert no accepted partial result, mutation, secret value,
fabricated Run/Event, or snapshot enlargement; if execution is admitted, assert
use of the shared RUN_SUPPORT Journal contract.
