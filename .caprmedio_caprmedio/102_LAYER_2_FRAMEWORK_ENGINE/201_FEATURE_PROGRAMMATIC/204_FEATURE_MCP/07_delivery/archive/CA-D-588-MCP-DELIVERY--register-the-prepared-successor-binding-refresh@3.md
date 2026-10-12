---
atom_id: CA-D-588
content_role: Delivery
current_scope_unit: MCP
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 3
updated_at: "2026-10-10 10:17:48 +0400"
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

The only current registration is the JSON object under `### Accepted source revision`. Its keys, replacement rows and nested pin shapes are exact; duplicate or unknown fields are invalid. Versions, occurrence counts and schema version are strict integers. Paths are safe regular Project-relative carriers with no symlink ancestry.

The exact input binding bytes, both prior Action archives and both current Active Action sources must match their registered identities, versions and raw-byte digests. Each replacement occurs at exactly the two named structural positions in its one named route. The four replacements repair only CA-O-134 and CA-O-137; no other non-Release pin or route field is replaced.

The same candidate includes the current `release_version` route and its sole source admission, freshly derived from current CA-D-572 authority and its actual declared source/private carriers. Missing or stale Release authority stops derivation. A non-Release-only intermediate is never published. After composition, recalculate both derived digests and validate all 16 routes and current source pins before any write.

The private reader is `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/selected_source_refresh.py`. It feeds the existing `release_manifest_publisher.py` refresh boundary, trusted Operator context, intent, atomic write, readback and Journal receipt. Historical schema-1 fixtures may reopen the archived authority; they do not admit the current Project's different input bytes.

## Private trusted-host refresh command

This Delivery realizes the existing CA-M-339 method for CA-R-1882 through one host-local `refresh-selected-release-binding` command lifecycle. It is a private Operator command, not a Project MCP Tool, selected-route binding, caller registry entry, generic Workflow invocation or raw Python-script substitute. It must not be registered in `implementation_server.py`, capability discovery, `selected_routes.py`, or any public transport.

The command accepts only an existing regular Project root and an explicit mode: `plan` is the default and `execute` requires a separate affirmative Operator command. It never runs during MCP startup, discovery, selected-route registration or plan generation. The host, not the command payload, supplies the actual authenticated session identity as the two non-empty `llm_session` fields (`app` and `uuid`), resolves the named Operator uniquely through `.caprmedio_caprmedio/operators_registry.toml`, and uses that Operator's registered Journal author. The fixed `authorization_ref` is read from this accepted D588 registration; neither it, a Plan, candidate bytes, context, Journal author, session identity nor a permission boolean is accepted from an untrusted caller.

In `plan` mode the host calls only `plan_release_manifest_refresh(project_root)` and returns its exact plan with no context, intent, Journal record, projection write, package replacement or automatic continuation. In explicit `execute` mode, in one trusted host process, it first derives that exact current plan, then calls `authorize_operator_refresh(project_root, plan, operator_name, journal_author, llm_session, authorization_ref)` and passes only the resulting opaque in-process context to `refresh_release_manifest(project_root, execute=True, authorization=context)`. It returns the existing publisher result unchanged: a plan is not a success receipt; publication is complete only after its atomic replacement, strict readback and Journal finalization. Stale input, changed source frontier, failed authorization, pending evidence or recording-required results remain truthful existing dispositions with no fallback write or package/runtime action.

No new Operation, Requirement, Method, Evaluation or Delivery identifier is claimed for this host adapter. Its governing references are the existing CA-R-1882, CA-M-339, CA-D-572 and this Delivery; a separately allocated Atom is required before any broader public or workflow-facing command is proposed.

### Accepted source revision

```json
{
  "schema_version": 2,
  "registration_id": "epic1848-graph-successors-release-frontier-20261010",
  "authorization_ref": ".caprmedio_caprmedio/03_plan/17-CA-P-1848-EPIC--unify-installation-and-local-public-release-cycles.md",
  "repair_task_id": "CA-P-1866",
  "input_manifest_ref": ".caprmedio_caprmedio/_projection/selected_workflow_bindings.json",
  "input_manifest_sha256": "dc75baa2d7748ced0683067e5de0047b09bc990b842355334cc877e7f6df4839",
  "input_canonical_manifest_sha256": "f944ead9f582956a1d74b6cbe07255d09586ddb13cb7ef01687992bc1a23a8f5",
  "pin_occurrences": 4,
  "replacements": [
    {
      "route": "build_entities_graph",
      "occurrences": [
        "ordered_steps[0].action",
        "ordered_actions[0]"
      ],
      "prior_pin": {
        "atom_id": "CA-O-134",
        "version": 2,
        "source_path": ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/CA-O-134-CORE_META_MODEL-ACTION--construct-entities-graph-projection.md",
        "digest": "b94eebdd85eab9f7080680e85999c68022e82cdfa7945bf0d840b429ebad037a"
      },
      "prior_archive_path": ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/archive/CA-O-134-CORE_META_MODEL-ACTION--construct-entities-graph-projection@2.md",
      "current_pin": {
        "atom_id": "CA-O-134",
        "version": 3,
        "source_path": ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/CA-O-134-CORE_META_MODEL-ACTION--construct-entities-graph-projection.md",
        "digest": "8a3dcb7cfdb3369ec268726cc54f3f0e0c1bfbc947841792deb87bb844245414"
      }
    },
    {
      "route": "build_terms_graph",
      "occurrences": [
        "ordered_steps[0].action",
        "ordered_actions[0]"
      ],
      "prior_pin": {
        "atom_id": "CA-O-137",
        "version": 2,
        "source_path": ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/CA-O-137-CORE_META_MODEL-ACTION--construct-terms-graph-projection.md",
        "digest": "6c154852b99df16961fe63c8fd869dbf86f8d75ecc950b25b189e41c3c1c5dad"
      },
      "prior_archive_path": ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/archive/CA-O-137-CORE_META_MODEL-ACTION--construct-terms-graph-projection@2.md",
      "current_pin": {
        "atom_id": "CA-O-137",
        "version": 3,
        "source_path": ".caprmedio_caprmedio/000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/09_operations/CA-O-137-CORE_META_MODEL-ACTION--construct-terms-graph-projection.md",
        "digest": "8ea08ef172a82515db7f145bf642a3943ecc41fc6decf4a86a69bea78ce494fd"
      }
    }
  ],
  "release_frontier": {
    "authority_atom_id": "CA-D-572",
    "route": "release_version",
    "admission_occurrences": 1
  }
}
```
