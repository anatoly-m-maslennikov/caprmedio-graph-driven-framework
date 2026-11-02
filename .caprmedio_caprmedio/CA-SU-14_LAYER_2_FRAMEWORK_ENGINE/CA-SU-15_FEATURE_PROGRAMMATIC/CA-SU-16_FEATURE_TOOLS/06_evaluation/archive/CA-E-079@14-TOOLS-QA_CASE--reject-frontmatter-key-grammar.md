---
subjects:
  governs: artifact-validation
  depends_on: []
version: 14
updated_at: 2026-10-24 01:18:03 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  evaluation_for:
  - CA-R-1136
atom_id: CA-E-079@14
status: Archived
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: TOOLS
type: Eval Case
---
# Reject frontmatter key grammar

## Test case

**Fixture:** change one registered frontmatter key from `snake_case` **to** another spelling.

**Expected result:** fail with the stable frontmatter-key-grammar diagnostic **and** a non-zero exit.
