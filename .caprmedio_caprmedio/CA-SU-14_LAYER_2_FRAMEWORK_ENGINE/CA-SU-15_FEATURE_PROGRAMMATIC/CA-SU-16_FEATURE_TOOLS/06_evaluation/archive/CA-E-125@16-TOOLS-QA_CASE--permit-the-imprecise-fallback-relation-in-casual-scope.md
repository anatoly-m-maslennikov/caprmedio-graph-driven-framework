---
subjects:
  governs: 'Subject/Graph/Relation/Type: related_to'
  depends_on: []
version: 16
updated_at: 2026-10-24 08:53:16 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  evaluation_for:
  - CA-R-1137
atom_id: CA-E-125@16
status: Archived
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: TOOLS
type: Eval Case
tier: 2
---
# Permit the imprecise fallback relation in casual scope

## Test case

**Fixture:** add the registered imprecise fallback relation **in** a casual scope **where** no precise registered relation applies.

**Expected result:** pass the authority-mode relation check.
