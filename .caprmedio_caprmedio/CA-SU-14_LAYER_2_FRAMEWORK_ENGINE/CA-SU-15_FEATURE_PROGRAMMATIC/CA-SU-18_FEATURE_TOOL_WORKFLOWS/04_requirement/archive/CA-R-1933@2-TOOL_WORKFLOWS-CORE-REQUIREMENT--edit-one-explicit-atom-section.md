---
atom_id: CA-R-1933@2
content_role: Requirement
type: Requirement
current_scope_unit: TOOL_WORKFLOWS
claim_target_scope_unit: TOOL_WORKFLOWS
local_tier: Core
global_tier: 9
status: Archived
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-12 23:58:28 +0400"
subjects:
  governs: "Tool"
  depends_on: ["Atom", "Property", "Workflow"]
relations:
  relates_to: [CA-R-866, CA-M-373, CA-O-030]
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
