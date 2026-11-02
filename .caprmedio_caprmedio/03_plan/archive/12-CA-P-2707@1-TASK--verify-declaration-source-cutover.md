---
atom_id: CA-P-2707@1
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

Verify the Declaration source cutover

## Objective

Verify Current source readback, the absence of TOML readers/writers, and affected runtime/script tests. Run the complete suite with required integration tests before any release. No release, container restart, commit or push is implied.
