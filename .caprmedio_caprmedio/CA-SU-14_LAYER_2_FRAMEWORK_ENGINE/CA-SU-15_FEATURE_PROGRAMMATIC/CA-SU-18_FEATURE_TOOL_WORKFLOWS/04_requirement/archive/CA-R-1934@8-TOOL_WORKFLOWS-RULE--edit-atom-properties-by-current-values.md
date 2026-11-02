---
atom_id: CA-R-1934@8
content_role: Requirement
type: Rule
current_scope_unit: TOOL_WORKFLOWS
claim_target_scope_unit: TOOL_WORKFLOWS
status: Archived
author: Anatoly Maslennikov
version: 8
updated_at: 2026-10-26 05:59:45 +0400
subjects:
  governs: Subject/Graph Node/Domain/Continuant/Atom
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Atom
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Workflow'
relations: {}
tier: 1
---
# Summary

Edit Atom Properties by current values

## Scope

Logical Property and list-entry edits of one explicitly selected Atom.

## Claim

Atom Modify **must** support explicit Property add, replace and remove, subject to the applicable complete-Atom schema and Property authority. Each edit binds its Atom identity and expected Version or source pin, explicit Property, operation and proposed value where required. Unknown or ambiguous Properties, stale sources, unapproved effects and invalid resulting values **must** fail closed.

For a list Property, support explicit entry add/remove, replacement of **`=1`** existing entry by its exact current value, or replacement of the complete set with an explicit proposed set. A current-value selector **must** identify exactly one existing entry; a missing or repeated selected value fails. Public entry replacement **must not** require or accept a caller-supplied index. Preserve unrelated entries and their order where that order is governed. Validate the resulting list against its Property's type, membership and uniqueness rules; a Subject dependency result **must not** contain duplicates.

A Summary or Type value change **must** use a new Atom ID and predecessor archival through the replacement Workflow, even when the Claim is unchanged. A verified unchanged requested state is a no-op with no edit, Version, timestamp or history effect. Preserve source, permission, preview and each one-Atom Action's storage-effect safeguards; a several-Atom Workflow retains completed Actions, stops at its first failed or uncertain Action and leaves the remainder untouched.

## Details

By-current-value editing is required new behavior. Earlier index-based fixtures do not establish its implementation or acceptance. Resume and retry policy for independent multi-Atom Actions is deferred.
