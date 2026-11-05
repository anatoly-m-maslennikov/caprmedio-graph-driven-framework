---
atom_id: CA-E-121
ref_id: CA-E-121
container:
  scope_unit: CA-SU-16
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Rule
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Type
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Framework Settings.Authority Modes
tier: 2
relations:
  evaluation_for:
  - CA-R-037
  - CA-R-1137
status: Active
version: 24
updated_at: 2026-10-27 19:59:29 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: TOOLS
---
# Reject strict orphan

## Test case

**Fixture:** leave an Active non-Goal tier-classified RMED Atom parentless **in** a strict scope, with its applicable Type **not** registered as orphan-permitted under CA-R-037. include a permitted orphan Type as a control.

**Expected result:** fail the non-exempt fixture with the stable strict-orphan diagnostic **and** a non-zero exit; do **not** reject the registered orphan-permitted control for parentlessness alone. this verdict diagnoses conformance **without** mutating the Atom, inventing a parent, **or** overriding the Operator's permission **to** retain a nonconforming Artifact.
