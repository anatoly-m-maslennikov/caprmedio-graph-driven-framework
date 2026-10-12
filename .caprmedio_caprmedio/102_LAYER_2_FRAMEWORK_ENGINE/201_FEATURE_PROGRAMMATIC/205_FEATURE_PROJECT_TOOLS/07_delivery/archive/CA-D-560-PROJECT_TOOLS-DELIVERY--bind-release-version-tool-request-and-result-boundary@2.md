---
atom_id: CA-D-560
content_role: Delivery
current_scope_unit: PROJECT_TOOLS
local_tier: Standard
global_tier: 11
status: Archived
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-11 16:46:21 +0000"
subjects:
  governs: "Tool/RELEASE_VERSION/Carrier"
  depends_on: [Tool, Workflow, Action, Manifest, Journal]
relations:
  delivery_for: [CA-R-1876, CA-R-1880, CA-M-331, CA-M-333]
---
# Summary

Bind the Release Version Tool request and result boundary

## Scope

The native Release Version Tool contract to be implemented after independent source review.

## Claim

The delivered `RELEASE_VERSION` Tool **must** expose exactly the request and result contract below through `PROJECT_TOOLS/RELEASE_VERSION/release_version.py`; it **must not** accept caller-authored Journal payloads or mutable path overrides.

## Details

```toml
schema = "caprmedio.release_version.v1"
entrypoint = "PROJECT_TOOLS/RELEASE_VERSION/release_version.py"
operations = ["prepare", "apply", "recover_recording"]

[request]
required = ["operation", "project_root"]
optional = ["candidate_version"]

[internal_request]
required = ["operation", "project_root", "candidateSnapshotManifest", "expected_executing_release", "expected_project_structure_digest", "expected_framework_settings_digest", "expected_source_frontier_digest", "run_receipt_refs"]
recover_recording_only = ["failed_recording_ref"]
forbidden = ["source_root", "output_path", "source_patch", "journal_payload", "run_event", "image_prune"]

[result]
required = ["operation", "outcome", "candidate_snapshot_manifest_sha256", "prior_release", "candidate_release", "runtime_selection", "skill_selection", "attempted_effects", "gate_evidence_refs", "image_refs", "rollback_state", "run_receipt_refs"]
```

The Operator-facing request identifies the bound Project and operation; optional `candidate_version` is a consistency expectation, not a caller-authored revision selection. Current registered Workflow/Step/Action and Action-to-Tool bindings, active-source snapshot, manifest and expected digests are derived internally at Run start and retained for the same Run. There is no manual revision-refresh prerequisite. `run_receipt_refs` may be empty before an actual Run exists; actual current Run/Action receipts are produced by shared recording and do not rewrite captured request bindings. `prepare` performs internal snapshot construction only, `apply` performs only effects admitted by the selected O graph, and `recover_recording` reconciles the same failed-recording identity without replaying an uncertain effect. This source contract is not an implementation, callable Tool, route, MCP schema registration, or release-readiness claim.
