---
subjects:
  governs: artifact-validation
  depends_on:
  - Subject/Domain/Node/Continuant/Atom/Content Role
  - Atom/Status
  - Subject/Graph/Relation
version: 14
updated_at: 2026-10-24 00:51:05 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  evaluation_for:
  - CAPRMEDIO-GOV-REQU-767
  - CAPRMEDIO-GOV-EVAL-005
  - CA-R-1137
atom_id: CA-E-106@14
status: Archived
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: TOOLS
---
# Reject inactive relation target

## Test case

**Fixture:** point a direct Relation authored by an Active RMED Atom at an Archived RMED Atom under CAPRMEDIO-GOV-REQU-767. also include an admitted Task dependency on a Done prerequisite Task as a control outside the RMED-to-RMED restriction.

**Expected result:** fail the Active RMED-to-Archived RMED fixture with the stable inactive-relation-target diagnostic **and** a non-zero exit. accept the admitted Done prerequisite with respect **to** this restriction; retain **all** other applicable Relation constraints under CAPRMEDIO-GOV-EVAL-005.
