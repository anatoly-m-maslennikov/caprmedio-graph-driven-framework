---
atom_id: CA-D-588
content_role: Delivery
current_scope_unit: MCP
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 4
updated_at: "2026-10-10 22:28:54 +0400"
subjects:
  governs: "MCP/selected source pin refresh"
  depends_on: [MCP, Projection, Workflow, Action, Operator, Journal, Atom, Source Carrier]
relations:
  delivery_for: [CA-R-1882, CA-M-339]
  relates_to: [CA-P-1866, CA-D-572]
---
# Summary

Register the prepared successor binding refresh

## Scope

the exact admitted selected-source revision refresh under the current Epic.

## Claim

the selected-source refresh registration **must** use the closed serialization below for this exact prepared-successor authority revision.

## Details

The only current registration is the JSON object under `### Accepted source revision`. Its keys and nested Pin shapes are exact; duplicate or unknown fields are invalid. Schema version and route counts are strict integers. Paths are safe regular Project-relative carriers with no symlink ancestry.

Schema 3 freezes the exact current 16-route input binding's raw-byte and canonical digests. Its first 15 route records and every source-registry freshness field remain byte-derived from that input; no non-Release route, query admission, registry reference, registry version, or registry digest is replaced. The sole replacement is `release_version` and its sole source admission, each freshly derived from the exact registered current CA-D-572 Pin.

Missing, stale, or changed CA-D-572 stops derivation. A stale twelve-Step retained Release route is replaced only by the current ten-Step source-derived route; structural, identity, order, typed-metadata, or non-Release drift is not a pin refresh. After composition, recalculate exactly the selected-binding and canonical-manifest digests and validate all 16 routes and current source Pins before any write.

The private reader is `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/selected_source_refresh.py`. It feeds the existing `release_manifest_publisher.py` refresh boundary, trusted Operator context, intent, atomic write, readback and Journal receipt. Historical schemas may reopen archived authority revisions; they do not admit the current Project's different input bytes.

## Private trusted-host refresh command

This Delivery realizes the existing CA-M-339 method for CA-R-1882 through one host-local `refresh-selected-release-binding` command lifecycle. It is a private Operator command, not a Project MCP Tool, selected-route binding, caller registry entry, generic Workflow invocation or raw Python-script substitute. It must not be registered in `implementation_server.py`, capability discovery, `selected_routes.py`, or any public transport.

The command accepts only an existing regular Project root and an explicit mode: `plan` is the default and `execute` requires a separate affirmative Operator command. It never runs during MCP startup, discovery, selected-route registration or plan generation. The host, not the command payload, supplies the actual authenticated session identity as the two non-empty `llm_session` fields (`app` and `uuid`), resolves the named Operator uniquely through `.caprmedio_caprmedio/operators_registry.toml`, and uses that Operator's registered Journal author. The fixed `authorization_ref` is read from this accepted D588 registration; neither it, a Plan, candidate bytes, context, Journal author, session identity nor a permission boolean is accepted from an untrusted caller.

In `plan` mode the host calls only `plan_release_manifest_refresh(project_root)` and returns its exact plan with no context, intent, Journal record, projection write, package replacement or automatic continuation. In explicit `execute` mode, in one trusted host process, it first derives that exact current plan, then calls `authorize_operator_refresh(project_root, plan, operator_name, journal_author, llm_session, authorization_ref)` and passes only the resulting opaque in-process context to `refresh_release_manifest(project_root, execute=True, authorization=context)`. It returns the existing publisher result unchanged: a plan is not a success receipt; publication is complete only after its atomic replacement, strict readback and Journal finalization. Stale input, changed source frontier, failed authorization, pending evidence or recording-required results remain truthful existing dispositions with no fallback write or package/runtime action.

No new Operation, Requirement, Method, Evaluation or Delivery identifier is claimed for this host adapter. Its governing references are the existing CA-R-1882, CA-M-339, CA-D-572 and this Delivery; a separately allocated Atom is required before any broader public or workflow-facing command is proposed.

### Accepted source revision

```json
{
  "schema_version": 3,
  "registration_id": "epic1848-current-local-release-frontier-20261010",
  "authorization_ref": ".caprmedio_caprmedio/03_plan/17-CA-P-1848-EPIC--unify-installation-and-local-public-release-cycles.md",
  "repair_task_id": "CA-P-1866",
  "input_manifest_ref": ".caprmedio_caprmedio/_projection/selected_workflow_bindings.json",
  "input_manifest_sha256": "3b8d7c34376b68b964d7713cace6a4aff90166b265ce053c9a699f36934560dc",
  "input_canonical_manifest_sha256": "0bf0c7000b83af54b25ac4d1729df9858276b8ce2012779dd154a04af80c330e",
  "input_route_count": 16,
  "preserved_route_count": 15,
  "release_frontier": {
    "authority_pin": {
      "atom_id": "CA-D-572",
      "version": 36,
      "source_path": ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/205_FEATURE_PROJECT_TOOLS/07_delivery/CA-D-572-PROJECT_TOOLS-DELIVERY--serialize-additive-release-route-source-admission.md",
      "digest": "f0f114ed0426b00951c5ea0bfa0d15f1fe08178e17023d97477205a82f729911"
    },
    "route": "release_version",
    "route_occurrences": 1,
    "admission_occurrences": 1
  }
}
```

