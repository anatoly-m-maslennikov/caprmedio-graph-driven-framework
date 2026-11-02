---
atom_id: CA-C-626
current_scope_unit: caprmedio
status: Active
subjects:
  active: Project.Settings
version: 1
relations: {}
tier: 3
role: Concern
form: Question
updated_at: 2026-11-02 07:52:54 +0400
---

## Summary

Resolve the scope of framework root locator requirements

## Question

Should code-root and control-root locators be mandatory for every Project, or only where the applicable Framework Instance Settings require them?

## Details

Working choice: allow the two Properties to be absent in the generic MODEL. Preserve the caprmedio Project’s existing requirements in Project Configuration. CA-D-371 requires a code-root locator in Framework Instance Settings; CA-R-1980 defines the Project Configuration control-root locator. This does not remove either requirement from its established context.

The choice avoids broadening a Project Configuration condition to all Projects. Continue with this source-backed choice while the broader applicability is reviewed; this Question is not an approval gate.
