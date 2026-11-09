---
atom_id: CA-R-665
ref_id: CA-R-665
container:
  scope_unit: CA-SU-23
role: Requirement
form: Rule
topics:
  {"main_subject": "Subject/CAPRMEDIO/Graph/Node/Aspect/UX/Guidance", "dependencies": ["CAPRMEDIO_MODEL <+ Projection", "CAPRMEDIO_MODEL <+ Scope Unit", "Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Architecture/Communication/Interface Contracts"]}
tier: 1
relations:
  child_of:
  - CAPRMEDIO-REQU-702--define-framework-engine-layer-scope
status: Active
version: 22
updated_at: 2026-10-27 20:00:10 +0400
subject_scopes:
- skill-boundary
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: SKILLS
---
## Summary

Provide a Project Scope Unit Graph Projection skill

## Claim

### Prose Claim

the framework **must** provide `ca-project-settings` as the thin Operator-facing Skill that:

- checks **and** rebuilds the Project Scope Unit Graph **and** Sources Projections through their registered deterministic Tool under CA-R-1070;
- uses accepted Project Structure declarations as authority under CA-R-1483, rather than treating observed folders **or** Atoms as replacement declarations;
- routes proposed semantic changes **to** their owning authority, including Project Structure, Settings, **or** RMED Atoms as applicable;
- never edits either output Projection, authors effective values independently, **or** embeds executable Tool logic.
