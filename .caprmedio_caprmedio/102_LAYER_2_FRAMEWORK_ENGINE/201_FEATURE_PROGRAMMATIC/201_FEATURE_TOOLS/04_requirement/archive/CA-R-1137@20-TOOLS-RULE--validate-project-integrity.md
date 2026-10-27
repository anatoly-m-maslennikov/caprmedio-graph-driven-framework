---
subjects:
  governs: Subject/Graph Node/Engineering/Aspect/Data Handling/Data Validation
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Project.Settings
  - Subject/Graph Node/Domain/Continuant/Project.Framework Settings
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations'
  - Subject/Graph Node/Domain/Continuant/Projection
  - Subject/Graph Node/Domain/Continuant/History/Journal
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
version: 20
updated_at: 2026-10-26 00:46:35 +0400
atom_id: CA-R-1137@20
status: Archived
content_role: Requirement
author: Anatoly Maslennikov
current_scope_unit: TOOLS
type: Rule
tier: 1
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
