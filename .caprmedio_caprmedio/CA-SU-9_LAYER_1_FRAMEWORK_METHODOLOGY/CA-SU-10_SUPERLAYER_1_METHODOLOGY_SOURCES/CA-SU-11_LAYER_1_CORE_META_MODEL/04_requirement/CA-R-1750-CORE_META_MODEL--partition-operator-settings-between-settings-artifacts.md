---
subjects:
  active: CAPRMEDIO_MODEL <+ Project.Settings
  passive:
  - Entity/Object/Continuant/Actor/Operator
  - CAPRMEDIO_MODEL <+ Project.Settings
  - Entity/Object/Continuant/Governing Objects/Governing Configuration
  - CAPRMEDIO_MODEL <+ Project.Settings.Name
  - CAPRMEDIO_MODEL <+ Project.Settings.Prefix
  - CAPRMEDIO_MODEL <+ Atom
version: 41
updated_at: 2026-11-02 20:07:03 +0400
relations: {}
atom_id: CA-R-1750
status: Active
tier: 1
role: Requirement
form: Rule
---
## Summary

Partition Operator Settings Between Settings Artifacts

## Claim

Each Operator-selected setting has one authoritative owner: Project Settings for Project initialization inputs, including Project Name and Prefix, or Framework Instance Settings for CAPRMEDIO behavior, configuration choices, and Authority Mode defaults. Atoms define permitted parameters, constraints, and applicability without fixing or duplicating selected values or defaults.
