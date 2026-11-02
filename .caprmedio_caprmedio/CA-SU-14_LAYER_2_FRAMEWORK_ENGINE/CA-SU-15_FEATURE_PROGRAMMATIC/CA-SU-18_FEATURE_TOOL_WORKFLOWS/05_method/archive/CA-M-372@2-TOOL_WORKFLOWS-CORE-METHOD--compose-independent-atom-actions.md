---
atom_id: CA-M-372@2
content_role: Method
type: Method
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
  depends_on: ["Atom", "Action", "Workflow"]
relations:
  relates_to: [CA-R-1093, CA-R-1067, CA-R-1105, CA-R-1155, CA-O-201, CA-O-202]
---
# Summary

Compose independent Atom Actions

## Scope

A Workflow composing explicit actions for several Atom targets.

## Claim

**To** compose Atom operations, the Workflow **must** retain Find, Read and Modify as independently invocable logical operations and execute **`=1`** explicit Atom target per Action:

1. Find, when requested, returns matches and matching facts. Read, when requested, returns the complete explicitly selected source with exact identity, Version and source pin. Neither step grants effect permission or silently selects Modify targets.
2. Bind the explicit target and delta for each requested Action. The storage connector maps logical Atom operations to their current storage; do not make a filename or folder an inferred logical identity.
3. Before each Action's effect, validate its own exact current source, applicable complete-source rules, admitted change class, preview and permission. Reject every same-ID Summary or Type value change and hand it to the replacement Workflow.
4. Execute the admitted Action and verify its actual outcome. Every actual changed same-ID Atom update advances Version by **`=1`** and uses actual Updated At, regardless of change class; preserve exact required before-Revision evidence. A validated no-op has no edit, Version, timestamp or history effect and permits progression to the next Action. Preserve any required actual Run recording.
5. On the first failed or uncertain Action, stop. Retain earlier completed Actions, apply the failed Action's own admitted storage-effect safeguards and leave all remaining targets untouched. Return the actual completed, no-op, failed, uncertain and untouched targets without converting partial work into whole-sequence success.

Do not promise a cross-Atom all-or-nothing effect, automatically retarget incoming references after replacement, or infer a resume or retry policy. Incoming references use independent Find and Modify Workflows. Resume and retry policy is deferred.

## Details

One-Atom source, permission, preview and storage-effect safeguards remain required. This Method does not enable deferred Subject publication or establish runtime acceptance.
