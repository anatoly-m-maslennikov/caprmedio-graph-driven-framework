---
atom_id: CA-R-1137
ref_id: CA-R-1137
container:
  scope_unit: CA-SU-16
role: Requirement
form: Rule
topics:
  main_subject: "Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Data Handling/Data Validation"
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Settings
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Framework Settings
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Projection
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
tier: 1
status: Active
version: 22
updated_at: 2026-10-27 19:59:51 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: TOOLS
---
# Validate project integrity

the framework **must** provide one deterministic read-only Tool that validates a selected Project scope as one integrated repository.

the Tool **must** apply Carrier validation **to** **every** selected Atom **and** check **all** of the following:

- unique identity resolution;
- registered structural **and** lifecycle topology;
- registered Relation **and** authority-graph rules applicable **to** RMEDO Atoms;
- authority modes **and** applicable Settings authority;
- Projection currentness;
- Journal replay integrity;
- Revision **and** proof provenance;
- generated-data stage direction;
- control-root/runtime hygiene.

the Tool **must** emit stable diagnostics **without** mutating Project files.
