---
atom_id: CA-M-381
content_role: Method
type: Method
current_scope_unit: CONNECTOR_TOOLS
claim_target_scope_unit: CONNECTOR_TOOLS
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Tool"
  depends_on: ["Artifact/Carrier","Action","Workflow","Atom","Operator"]
version: 1
updated_at: "2026-10-13 01:46:23 +0400"
relations:
  relates_to: [CA-R-1941, CA-R-1936, CA-M-376, CA-D-625, CA-D-630, CA-O-215, CA-O-216, CA-O-217]
---
# Summary

Bind private carrier storage changes

## Scope

Construction of the exact private adapter binding for CA-R-1941's one-carrier storage change, without exposing a physical path as the public logical target.

## Claim

**To** construct the binding, the adapter author **must** use the following convention:

1. Keep CA-D-625's logical target, explicit delta, required expected state and bound authorization/context unchanged. Select only the private variant that exactly realizes the already admitted delta. An unresolved or unsupported mapping is a blocker, not a choice of another target, lifecycle or semantic operation.
2. Resolve one source binding and, for rename/move, one destination binding under the supplied approved roots. Retain exact expected type, source identity/content/mode evidence, parent evidence and destination absence. Reject ambiguous resolution, root/ancestor selection, path escape and any symlink or substituted component; do not use string-prefix membership as proof.
3. For folder rename/move, bind the complete finite approved entry inventory and its expected states. Checking the actual folder against that inventory is verification only; newly discovered entries do not acquire permission. For removal, bind positive non-Atom cleanup eligibility and an exact file or empty-folder state.
4. Construct the mutation-free proposed location/absence map and explicit preservation frontier. Keep O215's same-parent rename, O216's explicit destination move and O217's non-Atom removal distinguishable. Do not add overwrite, merge, recursive cleanup or reference-rewrite fields.
5. Bind each Action's implementation to its required source/destination currentness rechecks and independently measurable postconditions. Use CA-D-630's private binding and common result roles; absent proof of a safe supported realization blocks execution. The Action, not this construction Method, owns its reusable behavior.
6. Keep observed results separate from proposals. Preserve actual known/unknown effects and errors; a true no-op needs verified unchanged requested state. Do not construct a completed lifecycle, history or reference-rewrite result from a private location change alone.

## Details

This convention implements only accepted CA-R-1941 authority. It creates no permission, transport, public path selector, retry or recovery policy. The Workflow retains semantic admission and sequencing. CA-O-040's broader generic rename is not the private variant. New source availability does not establish code, MCP or runtime admission; independent review and later functional proof remain required.
