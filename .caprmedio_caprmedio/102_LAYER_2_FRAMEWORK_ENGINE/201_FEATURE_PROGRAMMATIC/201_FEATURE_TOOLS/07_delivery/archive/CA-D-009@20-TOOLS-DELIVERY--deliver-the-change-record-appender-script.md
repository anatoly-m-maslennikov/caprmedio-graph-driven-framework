---
atom_id: CA-D-009@20
content_role: Delivery
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Archived
author: Anatoly Maslennikov
cce_version: cce_1
cce_form: serialization
subjects:
  governs: "provenance"
  depends_on: [Journal, Journal/Record, Atom, Artifact/Carrier, Project, Applicable Methodology]
version: 20
updated_at: "2026-10-14 18:37:38 +0400"
relations:
  delivery_for: [CA-R-812, CA-R-1124, CA-R-1064]
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Summary

Deliver the change-record appender script

## Scope

The canonical APPEND_CHANGE_RECORDS executable Carrier, its CLI and Project-bound MCP transport, and shared Journal append/read serialization.

## Claim

APPEND_CHANGE_RECORDS **must** be delivered through the canonical source script `102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/APPEND_CHANGE_RECORDS/append_change_records.py` **and** its content-identical Carrier **in** the selected `.caprmedio_runtime/tools` release.

- expose the common Doer CLI contract with dry-run **and** apply modes.
- reuse the release-local shared Journal library for plain append **and** read. it remains a library, **not** another executable Tool **or** writer.
- append supplied actual event observations **without** prior-record lookup, predecessor-chain admission, schema/digest validation, canonical receipts, deduplication, automatic retry **or** recovery machinery. each explicit append is an append, including repeated supplied data.
- read existing records **without** migration, rewriting, repairing **or** excluding historical records because they do not meet current rules. existing Journal files remain unchanged except for explicitly requested appends.
- preserve supplied values **and** actual replacement references through serialization. do **not** invent a baseline, earlier event, Actor, session, time **or** outcome. a record is a log entry, **not** permission **or** proof of source-state, lifecycle, Git **or** Run correctness.

## Details

### Project-bound append/read transport

The same canonical script **must** expose the existing Project-bound `append_change_records` interface through its registered descriptor **and** CA-O-222, using the shared append/read library. The closed transport request remains `{context, apply}` with strict boolean `apply`, default false; `context` supplies the existing Journal location inputs and `predictions.journal_records`. This transport shape is not a Journal-row validation or sealed-context requirement. Dry run changes nothing. Apply appends the supplied observations independently of real-change commits. Read returns existing stored data as recorded; it does **not** replay source effects.

The appender **must not** acquire a Git-effect lease, alter the index, create a Commit, reconstruct observations from current files **or** perform the recorded source/lifecycle operation. Public parameters express data **and** requested operations, **not** authorization; retain the existing authorized Project-MCP boundary **and** ordinary filesystem access. Preserve truthful I/O failure **and** any actually observed partial append; do **not** claim an unobserved completion **or** automatically replay an effect. There is no Journal validation, idempotency, receipt, reconciliation **or** recovery prerequisite.

```toml
[tool_binding]
name = "APPEND_CHANGE_RECORDS"
mcp_name = "append_change_records"
entrypoint = "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/201_TOOLS/APPEND_CHANGE_RECORDS/append_change_records.py"
action_ids = ["CA-O-222"]
```
