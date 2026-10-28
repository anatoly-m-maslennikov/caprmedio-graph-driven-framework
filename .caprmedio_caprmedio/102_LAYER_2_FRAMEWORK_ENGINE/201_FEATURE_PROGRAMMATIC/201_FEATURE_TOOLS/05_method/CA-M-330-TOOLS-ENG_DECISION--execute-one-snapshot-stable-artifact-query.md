---
atom_id: CA-M-330
content_role: Method
current_scope_unit: TOOLS
status: Active
author: Anatoly Maslennikov
version: 11
updated_at: 2026-10-27 19:59:42 +0400
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Selection
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Selection
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
relations: {}
type: Eng Decision
tier: 3
---
# Summary

Execute one snapshot-stable Artifact query

## Scope

The query evaluation method for FIND_AND_FETCH_ARTIFACTS, not a new parser,
Workflow, or Journal.

## Claim

FIND_AND_FETCH_ARTIFACTS **must** have CA-O-159 enumerate and retain one
allowlisted Markdown snapshot before parsing the closed filter grammar, then
evaluate and paginate only that retained snapshot in canonical identity order.

## Details

Reuse the existing safe Markdown/frontmatter parser. Validate the full snapshot
before accepting a result; preserve per-carrier diagnostics and reject ambiguity
or incomplete reads. Apply
CA-R-1850 without delegation to SQL, code, or eval; retain distinct
frontmatter/section namespaces and generic identity policy. Fetch bodies only
after matching identity and explicit selected request. Bind cursors to retained
digest and exact retained members; continuation cannot enumerate again. Enforce
resolved budgets and return measured coverage. No helper writes carriers,
Projections, Runs, or Journal Events on its own. An actual admitted selected
Action/Workflow uses CA-D-527 through CA-D-529 for shared Run and Journal
recording.
