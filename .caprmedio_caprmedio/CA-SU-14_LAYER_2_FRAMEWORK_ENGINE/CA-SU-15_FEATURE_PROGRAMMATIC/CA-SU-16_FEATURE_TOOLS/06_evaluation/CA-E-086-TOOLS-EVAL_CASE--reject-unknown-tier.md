---
atom_id: CA-E-086
ref_id: CA-E-086
container:
  scope_unit: CA-SU-16
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Tier
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Tier
  - Subject/CAPRMEDIO/Carrier
tier: 2
relations:
  evaluation_for:
  - CA-D-285
  - CA-R-1136
status: Active
version: 23
updated_at: 2026-10-27 19:59:28 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: TOOLS
---
# Reject unknown tier

## Test case

**Fixture:** give an ordinary RMED Atom an unregistered Local Tier token at the registered Local Tier position **in** its otherwise valid filename under CA-D-285; do **not** encode the tier **in** frontmatter.

**Expected result:** fail with the stable unknown-tier diagnostic **and** a non-zero exit.
