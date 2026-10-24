---
atom_id: CA-D-536@8
content_role: Delivery
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
status: Archived
author: Anatoly Maslennikov
version: 8
updated_at: 2026-10-24 00:38:25 +0400
subjects:
  governs: Subject/Engineering/Revert Changes/Request and Result Binding
  depends_on:
  - Subject/Engineering/Revert Changes
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
  - Artifact
  - Subject/Domain/Node/Continuant/History/Journal
relations:
  delivery_for:
  - CA-R-1833
  - CA-R-1834
type: Eng Decision
tier: 3
---
# Summary

Encode REVERT_CHANGES Tool binding

## Scope

The delivery Carrier and minimum MCP request/result contract for the REVERT_CHANGES Tool.

## Claim

The REVERT_CHANGES binding **must** expose strict request and result Carriers at one declared implementation location.

## Details

```toml
[tool_binding]
name = "REVERT_CHANGES"
entrypoint = "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/WORKFLOW_OPERATIONS/REVERT_CHANGES/revert_changes.py"
action_ids = ["CA-O-131"]
mcp_name = "revert_changes"
```

The strict request has `operation` (`admit` or `execute`), `reversal_request` for admission, and `approved_reversal_manifest` for execution. No Journal-only recovery operation or `pending_recording_event` field is exposed. Unknown fields, mixed modes, missing exact bindings, or a raw inverse instruction are explicit errors. The strict result has `outcome`, `manifest_id`, `effect_account`, `evidence_refs`, and `run_receipt_refs`; an admitted result additionally carries its manifest, while blocked/error results name the exact invalid binding. Existing `run_receipt_refs` retain actual shared Run observations and logging diagnostics, not canonical Journal receipts or a durability, permission or source-effect completion claim. Plain Journal append/read adds no logging retry or recovery, and logging failure does not change an independently observed reversal outcome or authorize effect replay. Actual Run-start failure still blocks before effects; actual Run-terminal failure preserves the effect account and reports `run_error`. The Tool exposes no generic delete/reset parameter and no auto-apply mode.

For admission, every frozen evidence reference uses one `evidence_pin`:
`{ evidence_ref, evidence_hash }`. `evidence_ref` is either an existing
canonical Journal Event reference `event:<event_id>` or a safe
Project-relative declared-carrier/member reference; it is not a URL, code,
resolver, symlink, traversal path, `.git`, or secret file. `evidence_hash` is
the SHA-256 of canonical Journal Event bytes for `event:<event_id>`, or of the
referenced member's raw bytes. The bounded reader resolves only configured
Project authority/evidence roots and rejects unsafe, missing, ambiguous,
oversized, changed, or unresolvable references; it creates no authority or
Journal and synthesizes no evidence.

`reversal_request` carries exact pins for `selected_change`, each retained
`history_record`, `before_record`, `after_record`, and each
`affected_reference`. `governing_definition` additionally carries
`{ atom_id, revision, evidence_ref, evidence_hash }`; `operator_decision` and
`executor_permission` carry `{ evidence_ref, evidence_hash }` with their
existing decision/capability fields. Operator-decision evidence records the
current Operator's exact ordered approved effects; executor-permission evidence
records the supported capability and current grant. Existing
`capability_permission` evidence remains separately required. Any changed,
revoked, missing, unsafe, unsupported, or hash-mismatched pin is a precise
pre-effect blocker; no ID, status, or hash-shaped value permits inference.
