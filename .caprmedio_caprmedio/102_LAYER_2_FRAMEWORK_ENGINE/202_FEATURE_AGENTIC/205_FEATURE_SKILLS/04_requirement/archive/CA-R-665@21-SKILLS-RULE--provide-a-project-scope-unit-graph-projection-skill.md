---
subject_scopes:
- skill-boundary
version: 21
updated_at: 2026-10-27 06:04:45 +0400
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  child_of:
  - CAPRMEDIO-REQU-702--define-framework-engine-layer-scope
author: Anatoly Maslennikov
content_role: Requirement
current_scope_unit: SKILLS
status: Archived
atom_id: CA-R-665@21
tier: 1
type: Rule
subjects:
  governs: Subject/Graph Node/Engineering/Authoring/Prompt Authoring
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Projection
  - Subject/Graph Node/Domain/Continuant/Scope Unit
  - Subject/Graph Node/Implementation/Code/Tool
---
# Provide a Project Scope Unit Graph Projection skill

the framework **must** provide `ca-project-settings` as the thin Operator-facing Skill that:

- checks **and** rebuilds the Project Scope Unit Graph **and** Sources Projections through their registered deterministic Tool under CA-R-1070;
- uses accepted Project Structure declarations as authority under CA-R-1483, rather than treating observed folders **or** Atoms as replacement declarations;
- routes proposed semantic changes **to** their owning authority, including Project Structure, Settings, **or** RMED Atoms as applicable;
- never edits either output Projection, authors effective values independently, **or** embeds executable Tool logic.
