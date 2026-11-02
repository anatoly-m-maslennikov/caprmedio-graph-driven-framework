---
atom_id: CA-M-330@7
content_role: Method
current_scope_unit: TOOLS
status: Archived
author: Anatoly Maslennikov
version: 7
updated_at: 2026-10-24 11:58:20 +0400
subjects:
  governs: Subject/Engineering/Artifact Query/Snapshot Evaluation
  depends_on:
  - Subject/Domain/Node/Continuant/History/Journal
  - Subject/Domain/Node/Continuant/Selection
  - Subject/Domain/Node/Continuant/Atom
relations:
  relates_to:
  - CA-R-1849
  - CA-R-1850
  - CA-O-159
  - CA-D-527
  - CA-D-528
  - CA-D-529
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
