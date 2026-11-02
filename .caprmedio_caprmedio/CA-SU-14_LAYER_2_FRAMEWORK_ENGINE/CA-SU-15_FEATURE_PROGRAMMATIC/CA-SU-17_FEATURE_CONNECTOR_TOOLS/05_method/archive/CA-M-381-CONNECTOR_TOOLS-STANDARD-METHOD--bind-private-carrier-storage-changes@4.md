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
version: 4
updated_at: "2026-10-13 23:51:12 +0400"
relations:
  method_for: [CA-R-1941]
  depends_on: [CA-D-625, CA-D-630]
---
# Summary

Bind private carrier storage changes

## Scope

Construction of the exact private adapter binding for CA-R-1941's one-carrier storage change, without exposing a physical path as the public logical target.

## Claim

**to** construct the binding, the adapter author **must** use the following convention:

1. keep CA-D-625's logical target, explicit delta, required expected state **and** bound authorization/context unchanged. select **only** the private variant that exactly realizes the already admitted delta. an unresolved **or** unsupported mapping is a blocker, **not** a choice of another target, lifecycle **or** semantic operation.
2. resolve one source binding **and**, for rename/move, one destination binding under the supplied approved roots. retain exact expected type, source identity/content/mode evidence, parent evidence **and** destination absence. reject ambiguous resolution, root/ancestor selection, path escape **and** **any** symlink **or** substituted component; do **not** use string-prefix membership as proof.
3. for folder rename/move, bind the complete finite approved entry inventory **and** its expected states. checking the actual folder against that inventory is verification **only**; newly discovered entries do **not** acquire permission. for removal, bind positive non-Atom cleanup eligibility **and** an exact file **or** empty-folder state.
4. construct the mutation-free proposed location/absence map **and** explicit preservation frontier. stage the exact source-bound change for Operator review **and** bind CA-R-1941's fresh trusted-host authorization record **and** recorded outside-edits-paused confirmation **to** the exact request, Action/variant, selected Session/Run **and** affected frontier. keep O215's same-parent rename, O216's explicit destination move **and** O217's non-Atom removal distinguishable. do **not** add overwrite, merge, recursive cleanup **or** reference-rewrite fields.
5. bind each Action's implementation **to** its required source/destination currentness rechecks **and** independently measurable postconditions. use CA-D-630's private binding **and** common result roles. require the confirmed exclusive window **and** existing shared Engine lock from final complete revalidation through effects **and** independent readback/verification; absent proof of a safe supported realization blocks execution. the Action, **not** this construction Method, owns its reusable behavior.
6. keep observed results separate from proposals. preserve actual known/unknown effects **and** errors; a true no-op needs verified unchanged requested state. do **not** construct a completed lifecycle, history **or** reference-rewrite result from a private location change alone.

## Details

This convention implements only accepted CA-R-1941 authority. It creates no permission, transport, public path selector, retry or recovery policy. The Workflow retains semantic admission and sequencing. CA-O-040's broader generic rename is not the private variant. New source availability does not establish code, MCP or runtime admission; independent review and later functional proof remain required.
