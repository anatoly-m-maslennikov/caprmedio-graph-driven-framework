---
atom_id: CA-D-569
content_role: Delivery
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
author: Anatoly Maslennikov
status: Active
subjects:
  governs: Subject/Engineering/Atom Lifecycle/Dispatch Interface
  depends_on:
  - Subject/Engineering/Atom Lifecycle/Dispatch Carrier Topology
  - 'Subject/Domain/Node/Continuant/Atom.Status: Draft'
  - Subject/Engineering/Atom Lifecycle/Draft History
version: 12
updated_at: 2026-10-24 00:38:25 +0400
relations:
  relates_to:
  - CA-D-531
  - CA-D-532
  - CA-D-568
type: Eng Decision
tier: 3
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

For Draft markers, bind the exact Draft path/digest and filename marker to the request. `CA-R-draft`/ID-free sources require an explicitly admitted fresh target ID; `<canonical-ID>@<proposed-version>-draft` binds to the same canonical target and proposed Version, while legacy `<canonical-ID>@draft` requires that Version explicitly. Existing-marker promotion must also bind the exact current predecessor Version/digest and refuses stale or mismatched evidence before effects. No retained Draft history, lineage or Journal append is required.

### Existing-marker request bindings

For an existing-marker Draft through the lifecycle `change_status` route, `request.parameters` carries exactly `{target: <full Draft descriptor>, status: <requested qualified model-admitted non-Draft Status>, canonical_target: <full Current descriptor>, proposed_version: <positive integer>}`. Resolve that requested Status from the current qualified Role/Type model; do not hardcode Active or a Plan-specific exception. The unchanged source Draft Status uses ordinary no-op handling and does not admit canonical-target evidence or a publication. Native `ATOM_PROMOTE` remains the distinct Draft-to-Active capability under CA-R-869; this generic lifecycle binding does not broaden that shortcut. The full Draft descriptor includes the exact Draft path, filename marker, carried Version, digest, lifecycle and Status; the full Current descriptor includes the canonical ID, current path, filename, current Version, digest, lifecycle, current admitted Status, Content Role and Type. `canonical_target` is the current predecessor, not a second target or an instruction to allocate an ID.

For an existing-marker item through native `ATOM_PROMOTE`, the item carries exactly `{selector: <Draft path>, target: <full Draft descriptor>, atom_id: <canonical ID>, canonical_target: <full Current descriptor>, proposed_version: <positive integer>}`. The selector, Draft descriptor path, marker-derived canonical ID, explicit `atom_id`, canonical-target ID/path and all Version/digest/currentness pins must agree. A duplicate ID, path or Version representation that disagrees with another bound representation refuses before effects. `proposed_version` is a positive integer; Boolean values are invalid even where the host language treats them as integers. The carried marker, proposed Version, current predecessor digest and currentness checks are authoritative preconditions, not advisory hints.

Native new-marker packets support one Atom Action. Ordered bulk promotion remains the existing Workflow boundary: invoke one independently bound Action per item in declared order, without reordering and without cross-Atom rollback. Ordinary ID-free compatibility remains unchanged. A role-only new marker uses an explicitly admitted fresh canonical ID and exact Draft path/digest pins, and carries no `canonical_target` because it has no existing predecessor.

This Delivery extends only the route-specific CA-D-531 lifecycle boundary; it does not alter CA-D-527's outer request, authorization, actual Run state, or Journal authority. CA-D-532 result carriers report actual observed facts and do not become an independent identity registry, Events writer, or Journal writer. This is a source contract, not an implemented request-field acceptance claim.
