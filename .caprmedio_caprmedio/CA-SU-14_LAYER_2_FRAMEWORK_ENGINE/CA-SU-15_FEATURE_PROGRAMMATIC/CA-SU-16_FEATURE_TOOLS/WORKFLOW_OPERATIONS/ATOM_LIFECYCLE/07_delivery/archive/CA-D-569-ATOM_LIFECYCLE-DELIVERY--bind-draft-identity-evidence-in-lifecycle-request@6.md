---
atom_id: CA-D-569
content_role: Delivery
current_scope_unit: ATOM_LIFECYCLE
claim_target_scope_unit: ATOM_LIFECYCLE
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Workflow Operations/Atom Lifecycle/Request Parameters/Draft Identity Evidence"
  depends_on: ["Tool", "Workflow Operations/Atom Lifecycle/Dispatch Interface", "Atom/Revision/Status: Draft", "Atom/Revision/History"]
version: 6
updated_at: "2026-10-16 00:00:00 +0400"
relations:
  relates_to: [CA-D-531, CA-D-532, CA-D-568]
---
# Summary

Bind Draft Identity Evidence in Lifecycle Request

## Scope

the selected Atom Lifecycle dispatch request's ordinary target identity and Status boundary.

## Claim

CA-D-531's `request.parameters` **must not** carry `draft_identity_evidence` or any caller-selected Draft-history basis. The dispatcher binds the complete new or current target Carrier descriptor, exact current source/target identity and locator, expected Version/digest where a current target exists, requested result or Status, current qualified Role/Type Status model and revision, and sealed authorization.

Create and explicit Change Status admit any Status the resolved current Role/Type model admits. They require no retained Draft-history entry, Draft head, lineage link, consuming successor, predecessor selection, Journal existence, Journal completeness, baseline, receipt, or successful append. A manually created Draft without retained history is therefore eligible for an otherwise admitted explicit Status update. Ordinary schema, identity, collision, current-target/source, permission, and observed-effect safeguards remain; an unadmitted or stale target/model/permission stops unchanged.

Actual exact predecessor history is retained when the mutation produces it. Any Journal append records only observed facts after the independent mutation attempt; its absence or append failure is a diagnostic, does not invalidate an observed mutation, and never authorizes replay. Unknown effects remain unknown rather than being claimed successful.

## Details

This Delivery extends only the route-specific CA-D-531 lifecycle boundary; it does not alter CA-D-527's outer request, authorization, actual Run state, or Journal authority. CA-D-532 result carriers report actual observed facts and do not become an independent identity registry, Events writer, or Journal writer. This is a source contract, not an implemented request-field acceptance claim.
