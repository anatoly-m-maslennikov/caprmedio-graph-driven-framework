---
atom_id: CA-P-2706@1
role: Plan
form: Plan
label: Task
status: Archived
version: 1
updated_at: 2026-11-02 18:26:00 +0400
tier: 4
current_scope_unit: caprmedio
subjects:
  active: Scope Unit
relations:
  IS_CONTAINED_BY:
  - CA-P-2694
---
## Summary

Retire project_structure.toml entirely

## Objective

Retire obsolete governing Atoms and remove the live TOML file. Replace every production reader with Declaration-Atom sources; retire TOML row editors and file-only bindings. Update affected fixtures and documentation. Do not preserve a fallback or derived compatibility TOML.
