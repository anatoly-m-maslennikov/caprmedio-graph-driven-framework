---
atom_id: CA-P-2689@1
content_role: Plan
type: Plan
label: Task
current_scope_unit: caprmedio
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Formal Model
version: 1
updated_at: 2026-10-28 20:00:14 +0400
relations:
  IS_CONTAINED_BY:
  - CA-P-2683
tier: 4
---
# Summary

Migrate governing paths and apply the new Relations

## Objective

Migrate governing paths and apply the new Relations.

## Details

After CA-P-2688.

Apply supported subjects.governs mappings first; then subjects.depends_on and source-pinned literal references in formal Claims. Use full canonical governing paths. Keep real named-instance/reference semantics, primary-kind uniqueness and no-alias decisions; never replace a procedure/module name with a new entity without evidence.

Apply the defined Relations to the in-scope model definitions and necessary typed source links. Keep schema/model edges distinct from actual Runtime/Run/Event instances. Preserve direct facts once and derive inverses. A partial scope cannot be presented as a fully migrated project graph.

Update the thin maps from actual readback. Record Unchanged, Drafted, Applied, Superseded or Unresolved honestly. Cross-scope consumers in Engine are dependencies of P2637, not permission to edit Engine here; if they prevent a safe change, expose the concrete dependency and ask the Operator.

## Definition of Done

Every selected governing/dependency target and necessary formal literal has a recorded applied, unchanged or explicitly unresolved disposition; newly declared relations use the correct meanings/directions and do not duplicate inverse facts.

## Progress

Not started. Prior analysis and Drafts are inputs, not completion evidence.
