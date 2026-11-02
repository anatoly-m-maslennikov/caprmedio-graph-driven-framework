---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Data Handling/Data Validation
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Term//Property
  - Subject/CAPRMEDIO/Carrier/File.YAML Frontmatter
version: 14
updated_at: 2026-10-27 19:59:36 +0400
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  evaluation_for:
  - CA-D-478
  - CA-D-485
  - CA-R-1136
atom_id: CA-E-509
status: Active
content_role: Evaluation
author: Anatoly Maslennikov
current_scope_unit: TOOLS
type: Eval Case
tier: 2
---
# Summary

Validate required defaults and optional overrides

## Claim

the Carrier validation Tool **must** preserve the distinction between a required defaulted Atom value **and** an optional inherited-setting override under CA-D-485.

- accept a required internally carried value equal **to** its registered default; reject its omission rather than rejecting its presence as redundant.
- accept an unselected absent override **and** a selected explicit override that currently equals the inherited value; change the upstream setting **and** verify that **only** the unselected override follows inheritance.
- reject the same Property maintained independently **in** frontmatter **and** body.
- a CLI failure identifies the Property **and** violated encoding rule with a non-zero exit **without** rewriting source values.
