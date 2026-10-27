---
subjects:
  governs: Subject/Graph Node/Domain/Continuant/Atom.Tier
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Atom.Tier
  - Subject/Graph Node/Engineering/Continuant/Carrier
version: 21
updated_at: 2026-10-25 17:32:27 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  evaluation_for:
  - CA-D-285
  - CA-R-1136
atom_id: CA-E-086@21
status: Archived
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: TOOLS
type: Eval Case
tier: 2
---
# Reject unknown tier

## Test case

**Fixture:** give an ordinary RMED Atom an unregistered Local Tier token at the registered Local Tier position **in** its otherwise valid filename under CA-D-285; do **not** encode the tier **in** frontmatter.

**Expected result:** fail with the stable unknown-tier diagnostic **and** a non-zero exit.
