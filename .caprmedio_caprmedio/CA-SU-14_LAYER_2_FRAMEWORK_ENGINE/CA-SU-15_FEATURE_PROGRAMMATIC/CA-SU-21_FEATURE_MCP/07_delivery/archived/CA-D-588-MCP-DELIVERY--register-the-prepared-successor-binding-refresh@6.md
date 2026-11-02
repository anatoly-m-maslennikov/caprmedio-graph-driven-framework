---
atom_id: CA-D-588
content_role: Delivery
current_scope_unit: MCP
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 6
updated_at: "2026-10-11 04:45:05 +0400"
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

the exact admitted single-Pin selected-source repair under the current Epic.

## Claim

the selected-source repair registration **must** use the closed serialization below for this exact single-Pin successor authority revision.

## Details

The only current registration is the JSON object under `### Accepted source revision`. Its keys and nested Pin shapes are exact; duplicate or unknown fields are invalid. Schema version and route counts are strict integers. Paths are safe regular Project-relative carriers with no symlink ancestry.

Schema 5 freezes the exact current seventeen-route input binding's raw-byte and canonical digests. It permits exactly one replacement: CA-O-030 v6 at `update_atom.native_action_calls[0]`, evidenced by its byte-identical archived v6 Carrier and active current v7 Pin. No other occurrence, route, admission, selected-source registry field, release frontier, or authority Pin is selected.

Missing, stale, changed, already-repaired, or non-byte-identical prior-archive evidence stops derivation. The existing prior-archive validator validates the registered prior digest, ID and Version; this historical archive is not required to carry an Archived status. After the one replacement, recalculate exactly the selected-binding, canonical-manifest, and deterministic serialized Manifest digests; all three must equal the registered values. Validate the complete seventeen-route candidate and the current source Pin before any write.

The private reader is `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/selected_source_refresh.py`. It feeds the existing `release_manifest_publisher.py` repair boundary, trusted Operator context, intent, atomic write, readback and Journal receipt. Frozen schemas 1 through 4 may reopen their archived authority revisions; they do not admit this current Project input, and this current registration admits only its new exact bytes rather than wider repair authority.

## Private trusted-host refresh command

This Delivery realizes the existing CA-M-339 method for CA-R-1882 through one host-local `refresh-selected-release-binding` command lifecycle. Its only host entrypoint is `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/selected_source_refresh_host.py:main(argv=None)`, invoked privately as that module path or as `-m selected_source_refresh_host` with the MCP directory on `PYTHONPATH`. It is a private Operator command, not a Project MCP Tool, selected-route binding, caller registry entry, generic Workflow invocation or raw Python-script substitute. It must not be registered in `implementation_server.py`, capability discovery, `selected_routes.py`, or any public transport.

The command accepts only an existing regular Project root and an explicit mode: `plan` is the default and `execute` requires a separate affirmative Operator command. It never runs during MCP startup, discovery, selected-route registration or plan generation. The host, not the command payload, supplies the actual authenticated Codex environment session identity as the two non-empty `llm_session` fields (`app` and `uuid`), resolves the named Operator uniquely through `.caprmedio_caprmedio/operators_registry.toml`, and uses that Operator's registered Journal author. The fixed `authorization_ref` is read from this accepted D588 registration; neither it, a Plan, candidate bytes, context, Journal author, session identity nor a permission boolean is accepted from an untrusted caller.

In `plan` mode the host calls only `plan_release_manifest_refresh(project_root)` and returns its exact plan with no context, intent, Journal record, projection write, package replacement or automatic continuation. In explicit `execute` mode, in one trusted host process, it first derives that exact current plan, then calls `authorize_operator_refresh(project_root, plan, operator_name, journal_author, llm_session, authorization_ref)` and passes only the resulting opaque in-process context to `refresh_release_manifest(project_root, execute=True, authorization=context)`. It returns the existing publisher result unchanged: a plan is not a success receipt; publication is complete only after its atomic replacement, strict readback and Journal finalization. Stale input, changed registered source Pin, failed authorization, pending evidence or recording-required results remain truthful existing dispositions with no fallback write or package/runtime action.

No new Operation, Requirement, Method, Evaluation or Delivery identifier is claimed for this host adapter. Its governing references are the existing CA-R-1882, CA-M-339 and this Delivery; a separately allocated Atom is required before any broader public or workflow-facing command is proposed.

### Accepted source revision

```json
{
  "schema_version": 5,
  "registration_id": "epic1848-exact-o030-v7-binding-repair-20261011",
  "authorization_ref": ".caprmedio_caprmedio/03_plan/17-CA-P-1848-EPIC--unify-installation-and-local-public-release-cycles.md",
  "repair_task_id": "CA-P-1866",
  "input_manifest_ref": ".caprmedio_caprmedio/_projection/selected_workflow_bindings.json",
  "input_manifest_sha256": "6d1e3aaacf33d4c3cb645f9ed46641dac38b6480773a080074bac51249c143f4",
  "input_canonical_manifest_sha256": "f903ad67c3b92d7edd2415107f467be42bce1c53d259f440ac1fdb513fa69d5f",
  "input_route_count": 17,
  "pin_occurrences": 1,
  "replacements": [
    {
      "target": "route",
      "route": "update_atom",
      "occurrences": ["native_action_calls[0]"],
      "prior_pin": {
        "atom_id": "CA-O-030",
        "version": 6,
        "source_path": ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/ATOM_UPDATE/09_operations/CA-O-030-TOOLS-ACTION--update-sealed-caprmedio-atom-carriers.md",
        "digest": "19097af83287005dae4d55e4b4da2234acce9e9f92b0f70671afb831bd8b256b"
      },
      "prior_archive_path": ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/ATOM_UPDATE/09_operations/archive/CA-O-030-TOOLS-ACTION--update-sealed-caprmedio-atom-carriers@6.md",
      "current_pin": {
        "atom_id": "CA-O-030",
        "version": 7,
        "source_path": ".caprmedio_caprmedio/102_LAYER_2_FRAMEWORK_ENGINE/201_FEATURE_PROGRAMMATIC/201_FEATURE_TOOLS/ATOM_UPDATE/09_operations/CA-O-030-TOOLS-ACTION--update-sealed-caprmedio-atom-carriers.md",
        "digest": "c2d70fa275a075d2fbc978cab246158cfd8413cec88716521336736d0bf060cc"
      }
    }
  ],
  "expected_manifest_sha256": "f898d30aeabe712ee8ae2545d732e6acde94efc8a5597db11229380937fbff52",
  "expected_selected_binding_digest": "cd05362d6f805902cf922151bc5135a91cb7ef267b0e85bfadf8e5d265a09284",
  "expected_canonical_manifest_sha256": "2c1bd6a93b1362fe1b2a457c2f5bf413a825748825027e607bb4d0f17ec55e25"
}
```
