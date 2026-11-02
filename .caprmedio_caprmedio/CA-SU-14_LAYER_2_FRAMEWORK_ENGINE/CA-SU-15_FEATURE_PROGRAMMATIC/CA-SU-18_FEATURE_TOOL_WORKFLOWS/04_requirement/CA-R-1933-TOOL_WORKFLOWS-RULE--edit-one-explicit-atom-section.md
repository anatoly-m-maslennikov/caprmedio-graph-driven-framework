---
atom_id: CA-R-1933
content_role: Requirement
type: Rule
current_scope_unit: TOOL_WORKFLOWS
claim_target_scope_unit: TOOL_WORKFLOWS
status: Active
author: Anatoly Maslennikov
version: 9
updated_at: 2026-10-27 20:00:05 +0400
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Workflow'
relations: {}
tier: 1
---
# Summary

Edit one explicit Atom section

## Scope

Logical edits of one explicitly selected section in one Atom.

## Claim

The section-edit family **must** support add, replace, remove, rename-title and reorder through **`=1`** explicit section operation per Atom Action. Bind the exact Atom identity, expected Version or source pin, section and requested change before preview. The storage connector resolves the section in the captured complete source; missing or ambiguous selection, stale source, invalid structure or missing permission **must** fail before the effect.

Preserve every unrelated Property and section. Replace changes the selected section value; rename-title changes only its title; reorder moves only that complete section to an explicit valid position, retaining its value and nested content. Add and remove **must** still produce a complete valid Atom under the applicable heading and Property rules. Any Summary or Type value change requires a new Atom ID and predecessor archival through the replacement Workflow; the section family **must not** perform it as a same-ID edit.

A verified unchanged requested state is a no-op with no edit, Version, timestamp or history effect. A failed or uncertain Action stops its several-Atom Workflow, retains earlier completed Actions and leaves the remainder untouched. Preserve each Action's source, permission, preview and storage-effect safeguards.

## Details

This Requirement defines required behavior. Saving it or citing historical fixtures does not prove implementation or current acceptance.
