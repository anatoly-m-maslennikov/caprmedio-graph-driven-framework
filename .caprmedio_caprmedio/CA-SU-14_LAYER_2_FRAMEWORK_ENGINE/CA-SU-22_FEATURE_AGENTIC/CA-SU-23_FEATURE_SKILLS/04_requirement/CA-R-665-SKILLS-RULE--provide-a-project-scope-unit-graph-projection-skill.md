---
atom_id: CA-R-665
ref_id: CA-R-665
container:
  scope_unit: CA-SU-23
role: Requirement
form: Rule
topics:
  main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ UX <+ Guidance
  dependencies:
  - MODEL//CAPRMEDIO <+ Projection
  - MODEL//CAPRMEDIO <+ Scope Unit
  - PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Architecture
    <+ Communication <+ Interface Contracts
tier: 1
status: Active
version: 23
updated_at: 2026-11-10 20:47:54 +0400
subject_scopes:
- skill-boundary
llm_session_ids:
- codex:019f591f-04f6-70f2-8de7-828b7cccc69d
- codex:01a02650-eff7-7453-8c37-0699b36773c6
author: Anatoly Maslennikov
current_scope_unit: SKILLS
destination:
  file:
    name: CA-R-665-SKILLS-RULE--provide-a-project-scope-unit-graph-projection-skill.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-22_FEATURE_AGENTIC/CA-SU-23_FEATURE_SKILLS/04_requirement
---
## Summary

Provide a Project Scope Unit Graph Projection skill

## Claim

### Prose Claim

the framework **must** provide `ca-project-settings` as the thin Operator-facing Skill that:

- checks **and** rebuilds the Project Scope Unit Graph **and** Sources Projections through their registered deterministic Tool;
- uses accepted Project Structure declarations as authority, rather than treating observed folders **or** Atoms as replacement declarations;
- routes proposed semantic changes **to** their owning authority, including Project Structure, Settings, **or** RMED Atoms as applicable;
- never edits either output Projection, authors effective values independently, **or** embeds executable Tool logic.
