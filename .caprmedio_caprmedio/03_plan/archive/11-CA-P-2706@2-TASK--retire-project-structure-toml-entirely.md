---
atom_id: CA-P-2706@2
role: Plan
form: Plan
label: Task
status: Archived
version: 2
updated_at: 2026-11-02 19:06:45 +0400
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

Keep existing Scope Unit workflow definitions unchanged. Remove the four TOML-specific Create, Rename, Move and Remove implementations and executable bindings. Move existing Authority and Delivery folders to their derived paths in this Epic.
