---
atom_id: CA-D-531
content_role: Delivery
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Workflow Operations/Atom Lifecycle/Dispatch Interface"
  depends_on: ["Tool", "Authorization", "Atom"]
version: 5
updated_at: "2026-10-14 05:53:59 +0400"
relations:
  delivery_for: [CA-R-1825, CA-R-1827]
---
# Summary

Deliver sealed lifecycle dispatch interface

## Scope

The Project-local MCP entrypoint contract. This specification defines the interface, not an executable Carrier.

## Claim

The entrypoint is one selected route under CA-D-527 and accepts no independent outer request/result. Its CA-D-527 `request.parameters` carries the typed lifecycle boundary: requested operation/result; exactly one complete new target Carrier set for Create, or exactly one complete current target/predecessor Carrier set for Update, Replace, or Change Status; and, for Replace, the complete accepted set of one or more distinct successor Carrier sets. It also carries the exact target/predecessor identity and locator, expected current Version/digest, proposed result or status mapping, and current qualified status model and model revision. `mode` remains preview unless the CA-D-527 outer request explicitly executes with its sealed operator authorization; an adapter envelope does not add authority.

The entrypoint returns CA-R-1828 only as the route-specific payload of CA-D-527's result. CA-D-527 remains the sole owner of outer disposition, started Run identities/definition bindings, canonical receipts or recording blocker, and retry disposition. A Summary-changing Update returns a terminal non-effect `replace_handoff`; Replace is a separately admitted new outer request with fresh exact definitions, currentness, and permission, never inherited Update permission.

## Details

### Subject-only Update variant

The existing `update_atom` route's `request.parameters` additionally accepts exactly `{target, subject_patches, subject_intent_sha256, subject_profile?, semantic_assessment_report?}` for one Subject-only Update. `target` is exactly the existing complete descriptor with `atom_id`, `path`, `filename`, `version`, `digest`, `lifecycle`, `status`, `updated_at`, `content_role` and `type`, preserving actual absent-Type representation. It selects one complete eligible non-archived original, not a Draft, archive, delivered or projected copy; carried Status and placement remain exact preconditions. `subject_patches` is the closed ordered Subject-only list under CA-R-866, CA-D-425 and CA-D-623. Scalar `governs` replacement or replacement of one `depends_on` entry uses exactly `{field, old, new}`; the dependency's exact current `old` value must identify one existing entry. A `depends_on` entry addition or removal uses exactly `{field, operation: "add"|"remove", value}`; removal's exact current `value` must identify one existing entry. Complete `depends_on` set replacement uses exactly `{field, operation: "replace_set", old, new}`, with `old` equal to the exact current collection and `new` the complete explicit proposed collection. Unknown fields, caller-supplied indexes, missing or ambiguous current values, a wrong complete-set precondition and duplicate proposed dependencies fail; no implicit entry merge or duplicate acceptance is introduced. These are required input shapes, not an implementation or admission claim. Omission of `subject_profile` means `legacy`. `subject_intent_sha256` is CA-D-425's lowercase full intent hash.

This variant derives its complete intended proposal from the pinned source and explicit Subject spans; it accepts no complete `proposed` Carrier, `frontmatter`, `content`, caller class, successors, legacy identity proof/mapping, additional independent target, or other fields. `semantic_assessment_report` retains exactly CA-D-585's `{path, digest}`; it is required for a value-changing effect under CA-R-1892 and may be absent for pure preparation or truthful no-op. Report/assessment identifies the intended proposal before effect-time metadata materialization. A replacement-required or unresolved result remains a non-effect handoff/refusal.

CA-D-425 defines the sealed intent and the subordinate exact-byte `predecessorArchive` effect. For a value change, the outer `target_frontier` is exactly the ordered current path then predecessor-history path; `effects` is exactly the ordered objects `{type: "subjectUpdate", path, atom_id, before_version, version, subject_intent_sha256}` for the current Carrier and `{type: "predecessorArchive", atom_id, version, path, sha256, lifecycle}` matching the sealed history intent. For no-op, the frontier contains only the current path and effects is empty. These descriptors request only that one target's current/history transition; no unrelated effects are admitted. CA-O-067/CA-O-145 and CA-O-129 reuse their existing one-target assessment and lifecycle bindings. At application require the exact CA-D-527 execute envelope, current source/definition/permission evidence, actual selected session and canonically recorded CA-O-030 Action start, then repeat complete source/report/intent/destination validation. No caller Boolean or independent adapter envelope is an execution capability. Return actual materialization/current/history/effect facts inside CA-D-527's one result; shared recording and recording-only recovery remain unchanged. Generic parameters and local standalone apply rejection remain intact; this is not bulk execution, a new route or local transport permission.

For an authorized Archive, the model-admitted status transition proceeds even when it newly breaks Relations. Diagnostics enumerate every newly broken Relation and active referrer and expose only a separate repair handoff; the entrypoint never silently repairs, retargets, or suppresses the transition.

For an explicitly authorized Update of an already assigned legacy Atom whose frontmatter lacks Atom ID, the typed parameters may include `legacy_identity_proof = {atom_id, commit, path, digest}`. The complete target descriptor seals the actual prior bytes and values. The full committed carrier at that exact path in the current repository history must be byte-identical to the present carrier, carry the same assigned ID in its filename and Content Role location, and have no competing current owner. This is lossless identity serialization, not draft promotion, fresh assignment, collision-winner selection, or an automatic lookup fallback. The proposed carrier must retain that Atom ID, Content Role, and exact Summary value; a missing legacy Active field may only be serialized explicitly as Active. Preserve the entire original carrier as historical evidence, including when the semantic Version is retained, and retain its exact descriptor and proof in the shared Run records. Stale or forged proof, inactive or projected carriers, changed identity or Summary, and ambiguous ownership fail closed or use the separately authorized replacement handoff. Ordinary lookup and Update remain strict.
