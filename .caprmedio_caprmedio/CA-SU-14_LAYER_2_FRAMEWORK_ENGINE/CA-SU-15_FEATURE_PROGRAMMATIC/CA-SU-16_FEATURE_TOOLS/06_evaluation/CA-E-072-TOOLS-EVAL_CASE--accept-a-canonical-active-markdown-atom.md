---
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Data Handling/Data Validation
version: 22
updated_at: 2026-11-02 19:44:26 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  evaluation_for:
  - CA-R-1136
atom_id: CA-E-072
ref_id: CA-E-072
status: Active
role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: TOOLS
form: Eval Case
tier: 2
container:
  scope_unit: CA-SU-16
---
# Accept a canonical active Markdown Atom

## Test case

**Fixture:** validate one canonical active Markdown Atom with a registered address, minimal frontmatter, one matching H1, **and** a non-empty claim body.

**Expected result:** pass with exit `0`, an empty diagnostic set, **and** unchanged bytes.
