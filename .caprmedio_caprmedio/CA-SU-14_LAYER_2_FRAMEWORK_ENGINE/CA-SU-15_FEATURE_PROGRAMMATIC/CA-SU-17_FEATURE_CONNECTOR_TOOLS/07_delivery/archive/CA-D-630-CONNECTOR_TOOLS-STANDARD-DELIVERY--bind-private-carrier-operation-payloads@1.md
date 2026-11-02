---
atom_id: CA-D-630
content_role: Delivery
type: Delivery
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
  delivery_for: [CA-R-1941]
  relates_to: [CA-D-625, CA-D-527, CA-M-381, CA-O-215, CA-O-216, CA-O-217]
---
# Summary

Bind private carrier operation payloads

## Scope

The private adapter binding and result carrier for O215 rename, O216 move and O217 removal, under CA-R-1941. This is an unimplemented contract, not an executable, public path API or new transport binding.

## Claim

The public logical request/result **must** retain CA-D-625's exact representations. Its supported common operation is `modify`; private `rename`, `move` and `remove` are declared storage variants behind that operation, not additions to the common operation enum.

## Details

The public request still contains exactly `operation,target,query,delta,expected_state,authorization,context`. Target is the admitted logical kind/identity, query is null, delta is the explicit already admitted logical change, and expected state and authorization/context bind the exact source and permission. Physical paths, basenames, filesystem roots and recursive selectors are not accepted as public logical target or delta selectors.

The connector's private bound plan identifies exactly:

- `variant`: rename, move or remove;
- `source_binding`: the uniquely resolved file/folder, approved root, parent and exact current-state evidence;
- `destination_binding`: the explicit resolved destination, approved root/parent and expected absence for an actual rename/move, or the verified unchanged destination binding for no-op; null for remove;
- `entry_inventory`: the complete finite approved inventory and expected states for a folder rename/move; empty-folder evidence for folder removal; null for a file;
- `admission_evidence`: the existing bound permission/schema/currentness evidence, positive non-Atom cleanup eligibility for remove, or required lifecycle/history admission for an internal Atom carrier move.

These are internal binding roles, not a second caller envelope or a permission token. Missing, ambiguous, stale or unsupported bindings are rejected under CA-R-1941; the connector cannot fabricate admission. Private relative locators must remain within the supplied roots with no symlink traversal or root/ancestor effect. Rename keeps the same parent; Move uses only the supplied destination; Remove has no destination and never expands descendants. Destination collisions, overwrite and merging are not represented as accepted effects.

Return exactly the common `data,current_state,effects,errors` roles. Data identifies the observed variant and its explicitly bound result; proposed maps are labelled as proposals. Current state records actual binding/type/presence and state evidence, not an invented Atom Version or lifecycle outcome. Mutation effects are known or unknown with actual evidence; a verified no-op has no mutation effect. Use the existing structured code/message/field errors: invalid bindings/forbidden frontiers, missing or ambiguous targets, stale state, denied permission, backend failure or uncertain effect map to CA-D-625's admitted codes. Every unknown effect includes `effect_uncertain`; errors never imply success, and empty errors require independently verified variant postconditions.

CA-D-527's existing selected service envelope remains unchanged where used. No public rename/move/remove route, API operation enum, CLI path option, Run/Event schema or implementation entrypoint is created. The FEATURE Delivery root remains future/unmaterialized; no existing code or installed carrier is moved. Required source review and functional proof remain separate.
