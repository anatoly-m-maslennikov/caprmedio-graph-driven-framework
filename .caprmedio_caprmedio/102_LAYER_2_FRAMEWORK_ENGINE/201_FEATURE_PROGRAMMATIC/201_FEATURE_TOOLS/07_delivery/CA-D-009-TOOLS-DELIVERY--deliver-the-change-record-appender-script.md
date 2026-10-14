---
atom_id: CA-D-009
content_role: Delivery
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
cce_version: cce_1
cce_form: serialization
subjects:
  governs: "provenance"
  depends_on: [Journal, Journal/Record, Atom, Artifact/Carrier, Project, Applicable Methodology]
version: 19
updated_at: "2026-10-14 17:57:07 +0400"
relations:
  delivery_for: [CA-R-812, CA-R-1124, CA-R-1064]
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Summary

Deliver the change-record appender script

## Scope

The canonical APPEND_CHANGE_RECORDS executable Carrier, its CLI and Project-bound MCP transport, and shared Journal append serialization.

## Claim

APPEND_CHANGE_RECORDS **must** be delivered through the canonical source script `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/APPEND_CHANGE_RECORDS/append_change_records.py` **and** its content-identical Carrier **in** the selected `.caprmedio_runtime/tools` release.

- expose the common Doer CLI contract with dry-run **and** apply modes.
- use the release-local shared non-executable Journal append implementation for schema-version-3 `governed_project_change` file **or** folder events, including the recorded ordered folder entry set; retain read compatibility with accepted schema-version-2 file records.
- restrict admission checks **to** the event representation **and** storage-integrity boundary of CA-R-1491 **and** CA-D-340. the shared library **must not** apply Atom-ID grammar, filename conventions, lifecycle rules, folder-placement rules, **or** relation-validity checks as append gates.
- preserve recorded Project values **without** renaming **or** repairing them. accepted event storage does **not** certify the recorded Project state.
- keep mutable lease **and** append state under `.caprmedio_runtime`. the shared implementation remains a library, **not** an additional executable Tool.

## Details

### First recorded Atom change

the first recorded actual Atom `UPDATE`, `MOVE` **or** `MOVE+UPDATE` **may** be a schema-version-3 `completed` `governed_project_change` file event **without** `previous_result_event` **only** **when** no prior canonically confirmed result for that Atom identity exists. record **only** the actual change; do **not** automatically create a `recovered` baseline **or** invent an earlier event, Actor, time **or** outcome. this first record does **not** establish that the earlier state is replayable from the Journal.

**if** a prior canonically confirmed result exists, retain the required exact immediate `previous_result_event` link. known unmatched, unresolved **or** unconfirmed predecessor evidence is **not** a first recorded change **and** **must** refuse **until** the chain integrity is resolved; do **not** omit the link **or** substitute a fabricated baseline. `REMOVE` retains its existing predecessor requirement. preserve event/digest, stale-reference, replay, idempotency **and** append-only integrity checks **and** all accepted historical bytes **and** legacy read compatibility. this exception adds no field, schema version, writer **or** permission to perform the source change.

### Carrier-only recovered baseline

schema-version-3 `recovered` `governed_project_state` file records **may** encode observed present state through `recovery_evidence` with **=1** `carrier` object:

- `path`: the recorded result path;
- `sha256`: the recorded result digest;
- `observed_at`: the record's timezone-qualified Occurred At; **and**
- `observer_run_id`: the actual observing Run identifier.

this closed Carrier-only representation establishes present state **only**. the Author **and** Occurred At identify its recorder **and** observation, **not** an unobserved historical creator **or** creation time. historical Actor, time, intent, Scope, **and** outcome remain unproven unless separately evidenced.

retain accepted schema-version-3 `git` **and** `carrier` recovery evidence **and** schema-version-2 read compatibility. Git corroboration is optional for this Carrier-only representation. a recovered record carries **none** of `action_type`, `sources`, **or** `previous_result_event`; a subsequent non-ADD change links **to** the confirmed baseline through `previous_result_event`. admission verifies this representation **and** recording integrity, **not** current Project grammar.

### Project-bound MCP append transport

The same canonical script **must** expose `append_change_records` through the registered descriptor and CA-O-221. Its closed request contains only the complete existing sealed schema-3 `context` and strict boolean `apply`, default false. Dry run returns the validated original records and planned Journal receipts without writing. Apply uses the same shared append implementation and actual receipts, independently of a real-change commit, without acquiring a Git-effect lease, modifying the index, reconstructing observations from current files or creating a Commit. Existing sealed replacement references remain part of their original event digest and are preserved without a lifecycle-conformance judgment. Journal storage locks and integrity checks remain mandatory. Preserve actual append failure, partial effects and recording-pending evidence without replaying source changes or inventing completion. Public parameters and descriptor metadata confer no authorization; append requires the existing authorized Project-MCP caller boundary.

```toml
[tool_binding]
name = "APPEND_CHANGE_RECORDS"
mcp_name = "append_change_records"
entrypoint = "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/APPEND_CHANGE_RECORDS/append_change_records.py"
action_ids = ["CA-O-221"]
```
