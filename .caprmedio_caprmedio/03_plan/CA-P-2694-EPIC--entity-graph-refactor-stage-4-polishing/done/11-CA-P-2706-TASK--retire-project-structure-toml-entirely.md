---
atom_id: CA-P-2706
ref_id: CA-P-2706
role: Plan
form: Plan
label: Task
status: Done
version: 3
updated_at: 2026-11-02 23:30:39 +0400
tier: 4
current_scope_unit: caprmedio
topics:
  main_subject: CAPRMEDIO_MODEL <+ Scope Unit
author: Anatoly Maslennikov
container:
  atom: CA-P-2694
---
## Summary

Retire project_structure.toml entirely

## Objective

Retire obsolete governing Atoms and remove the live TOML file. Replace every production reader with Declaration-Atom sources; retire TOML row editors and file-only bindings. Update affected fixtures and documentation. Do not preserve a fallback or derived compatibility TOML.

Keep existing Scope Unit workflow definitions unchanged. Remove the four TOML-specific Create, Rename, Move and Remove implementations and executable bindings. Move existing Authority and Delivery folders to their derived paths in this Epic.

## Result

The live TOML and its executable dependencies are removed. Current Declarations are the structural source. Authority and Delivery folders were migrated; the four TOML row-editing implementations and bindings were retired. Existing business Workflow definitions remain.

Source readback and runtime evidence are in [the adoption packet](../scope-unit-governance-20261031/README.md). Broader Engine verification remains in P2707.
