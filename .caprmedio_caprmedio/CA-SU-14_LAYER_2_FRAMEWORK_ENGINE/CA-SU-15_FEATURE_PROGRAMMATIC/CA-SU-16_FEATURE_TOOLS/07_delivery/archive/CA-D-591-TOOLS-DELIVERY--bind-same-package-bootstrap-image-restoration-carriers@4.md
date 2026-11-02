---
atom_id: CA-D-591
content_role: Delivery
current_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Archived
author: Anatoly Maslennikov
version: 4
updated_at: "2026-10-10 03:51:36 +0400"
subjects:
  governs: "Tool/FRAMEWORK_IMAGE_RESTORATION/Intent and proof carriers"
  depends_on: [Tool, Operator, Framework Package, Runtime, Skill, Manifest, Docker Image, Journal]
relations:
  delivery_for: [CA-R-1897, CA-M-353]
---
# Summary

Bind same-package bootstrap image restoration carriers

## Scope

The closed private intent, retained build proof, selector replacement and actual result of CA-O-187, outside the selected Release Version request and route.

## Claim

FRAMEWORK_IMAGE_RESTORATION **must** retain a frozen same-package intent, the applicable authentic canonical bootstrap proof and fresh attempt observations, and the actual image-binding restoration result while preserving existing package, selector, proof and canonical Journal schemas.

## Details

The admitted source API is restore_framework_image(project_root, *, journal, requested_run_id, expected_selector_sha256, image_executor, retry_of_terminal_event_id=None). Its only caller input seal is the exact selector SHA-256; it derives the retained package, original proof and context internally. The frozen intent contains exactly action_id = FRAMEWORK_IMAGE_RESTORATION, kind = retained_selected_framework_image_restoration, manifest_sha256, source_context_sha256, selected_selector_sha256, old_image_digest, retained_proof_receipt_sha256 and retained_context_sha256. Digest values are actual lowercase SHA-256 observations; old_image_digest is an immutable sha256 image ID. requested_run_id binds that closed intent and source authority through the existing direct Session, rather than adding an intent member. The registered Operator and authorization reference remain the direct Session's explicit authorization boundary. retry_of_terminal_event_id, when supplied, names one exact canonical partial terminal for a separately authorized fresh Run; it is not a member of the closed intent and grants no uncertain-effect replay. The replacement image digest is not prefilled in the started intent: it is an actual build result. No caller supplies a context path, proof path, Dockerfile, dependency, label, command, tag, network or replacement image override.

The intent digest is SHA-256 of canonical UTF-8 JSON excluding itself. Private restoration evidence occupies only the internally derived .caprmedio_runtime/framework_image_restoration/<intent_sha256>/ location and retains intent.json, the exact prior-selector.toml, the verified replacement-selector.toml when a different image digest is published, fresh actual build/inspect/canary attempt observations at derived private paths, and actual result.json. A fresh known-partial retry uses a distinct child attempts/<run_sha256>/ beneath that unchanged intent directory, where run_sha256 is SHA-256 of the exact requested_run_id UTF-8 bytes. It retains its own result.json and retry.json; the closed retry record contains schema = caprmedio.framework_image_restoration.retry.v1, intent_sha256, requested_run_id, retry_of_terminal_event_id, retry_of_terminal_event_digest and retry_of_result_ref. Its terminal reference and digest are actual canonical Journal observations. Repeating that Run inspects its own result without re-execution. The original intent-root result, prior-selector and historical terminal are never overwritten. The complete persistent package and public Skill inventories bind ordered paths, file digests and observed modes, including their directory structure, under the existing Release inventory exclusions and CA-R-1898's exact Finder metadata exclusion. These carriers support one Action's observation and recovery; they are not another Journal or authority registry.

The disposable build context and canonical image proof retain CA-D-575's existing bootstrap evidence shape and derived bootstrap_proof_key. Every actual build retains fresh immutable build/inspect/canary attempt records and outputs. For a different observed image digest, retain a new canonical proof containing those actual command records at the corresponding new key. For the original observed digest, reopen and preserve the existing canonical proof/key unchanged and retain the fresh attempt observations in restoration evidence instead of overwriting historical proof. The applicable canonical proof and fresh attempt bind the original package/source-context identity, authenticated persistent context digest and actual observed immutable image digest. The retained-package reader admits only the original legacy canary or the fixed metadata-aware complete-package canary under frozen program digests and exact command vectors. Historical context/probe bytes are not rewritten. The installed-N executor receives no bypass or additional selector field.

For a different observed image digest, the replacement selector has exactly CA-D-575's existing bootstrap fields and retains every frozen value except image_digest. For the original observed digest, all exact selector bytes remain unchanged. Both branches use one new fixed Project-wide selector lock shared with normal promotion plus an immediate exact frozen-input recheck; they do not reuse the distinct first-install lock as a substitute.

The actual result binds the frozen intent and Action Run, outcome and reason, observed image digest and applicable canonical proof key/receipt when available, fresh attempt references, prior and observed selector hashes, publication state, and retained effect references. Its closed outcomes are restored, no_op, blocked, partial, effect_uncertain, recording_pending and recovery_required. Both successful build branches are restored, including reproduction of the original image digest; no_op requires the exact image already available and freshly verified before building. An unavailable observation is absent or null, never an expected value presented as actual proof. The canonical Journal retains only its existing completed, no_op, failed, cancelled and partial outcomes: restored requires an observed canonical completed terminal, and no_op uses its existing no_op outcome when an Action was started. Uncertainty retains the started Run or original pending canonical recording without inventing a terminal outcome. The existing result/effect references record actual digests without new Journal fields. A terminal recording failure retains the actual selected or unselected state and any original pending event for exact recording recovery; no carrier authorizes replay or rewrites a historical receipt.

Effect references are safe Project-relative paths, unique in first-occurrence order. Different evidence origins may name the same physical proof path; they retain their distinct proof fields without duplicating the canonical Event's carrier reference. The recording-only API is recover_framework_image_terminal(project_root, *, journal, result_ref, image_executor), invoked explicitly with --execute --record-retained-result <owned result_ref>. It accepts only the internally owned immutable restored result whose original started Run, current selector, package/Skill and actual canonical image proof are independently verified. It appends only the original Run's terminal and returns that actual terminal with the original result_ref; it neither changes the raw result nor adds a Run, Event schema or effect. A retained pre-fix result with repeated identical proof-path references is read unchanged; only its canonical terminal reference list is normalized. Existing terminal or pending evidence, changed input, unavailable proof or uncertain effects refuse this recording-only path.

### Direct MCP binding

The Project MCP advertises `restore_framework_image` as the direct execution binding for CA-O-187, not a selected Release route. The server-bound Project root is never a caller argument. Its closed request has `operation` = `preview`, `execute` or `record_terminal`; execute requires `requested_run_id`, `expected_selector_sha256`, `operator` and `authorization_ref`, with optional `retry_of_terminal_event_id`. Recording requires the exact retained `result_ref`, `operator` and `authorization_ref`; preview carries no effect authorization.

The adapter derives the Journal Author from the exact registered Operator record and uses the existing direct Action Session and fixed Docker executor. The authorization reference is an actual retained Project-relative Operator command carrier, reopened before execution and bound to this request; it is not a permission Boolean or an inferred permission from discovery. Unknown request fields, stale source, missing command evidence or mismatched account refuse before effects. No caller supplies a Project root, build context, Docker input, replacement image, source pin or executor.

Preview uses the public read-only restoration-plan API to return the frozen intent and exact selector binding without a build, selector publication or Action start. Execute invokes the admitted source API once and returns its actual result. Recording invokes only the existing exact retained-result terminal recovery. Discovery advertises CA-O-187's binding and exact input schema; an unavailable binding remains unresolved rather than being treated as executable.

The Operator command carrier is canonical UTF-8 JSON (sorted keys, compact separators, no trailing newline and no self-digest) retained at a safe Project-relative path. Its exact keys are `schema_version = 1`, `operation`, `command_id`, `operator`, `journal_author`, `operators_registry_sha256`, `action_source` and `input`. `action_source` has exactly `atom_id = CA-O-187`, `version`, `path` and `sha256`, all reopened against the admitted direct Action source. For execute, `input` has exactly `requested_run_id`, `expected_selector_sha256` and optional `retry_of_terminal_event_id`; for recording, it has exactly `result_ref`. The Operation and input equal the actual MCP request, the Operator/account mapping equals the current exact registry, and the raw command bytes are hashed into retained invocation evidence. The carrier expresses the Operator's commanded input; it is neither a Full Gate receipt nor permission for a different Operation or retry. Refuse noncanonical, aliased, mismatched, unknown-field or unavailable carriers before a direct Action start.

```toml
[tool_binding]
name = "FRAMEWORK_IMAGE_RESTORATION"
entrypoint = "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/204_MCP/framework_image_restoration_mcp.py"
mcp_name = "restore_framework_image"
action_ids = ["CA-O-187"]
```
