---
atom_id: CA-M-344
content_role: Method
current_scope_unit: PROJECT_TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 4
updated_at: "2026-10-11 16:51:04 +0000"
subjects:
  governs: "Tool/RELEASE_VERSION/Private suite reference-context construction"
  depends_on: [Tool, Release Version, Candidate Manifest, Test Suite, Project Structure, Operator, Workflow, Action, Source Carrier, Digest]
relations:
  method_for: [CA-R-1887]
---
# Summary

Construct and revalidate one private Release-suite reference context

## Scope

The deterministic Suite-owner procedure for the control-reference closure outside the candidate package rows.

## Claim

RELEASE_VERSION **must** derive the private context only from current trusted internal candidate, compilation, selected-N, image-context, and source-admission handoffs; it must not accept a caller-selected path, digest, reference row, or success assertion.

## Details

1. Start from the trusted candidate manifest SHA-256, compiled-candidate root, frozen selected-N identity, and selected-N image-context identity already admitted to the suite invocation.
2. Use the same release-only execution snapshot internally derived under current CA-D-572 at Run start. Generate its canonical bytes for `<control_relative>/_projection/release_execution_snapshot.json` only in the private reader/workspace; do not read or write the legacy multi-route manifest. Read and validate the regular, non-symlinked Operator registry, current Project settings carrier and declared Project Structure. Collect current CA-D-572 and the exact captured Workflow, Step, Action and RMED source pins from that release admission. Include the two Unit-deadline settings carriers declared by CA-D-580. Reject unknown, conflicting, missing, escaping, runtime, Journal, secret-shaped or non-regular filesystem inputs. Union identical shared pins once. Unrelated Prompt bindings and selected-source refresh authority pins are outside this local context.
3. Sort the resulting typed `reference_rows` by source path, use each captured filesystem byte string and the internally generated snapshot bytes, verify their SHA-256 and mode, and form `control_context_digest` from canonical JSON of the rows plus the trusted internal bindings. Copy only those verified bytes to their identical relative paths in the disposable workspace, then mount that closure read-only.
4. Issue the schema-2 private envelope and execute the already sealed suite command. The command receives no additional caller-controlled path or control input.
5. Before and after execution, reopen the same retained snapshot, captured definition rows and trusted internal bindings and require identical rows and `control_context_digest`, checking current protected settings and selected-N state; otherwise retain truthful non-passing evidence. Later authoring edits do not replace the captured release definitions or payload. The procedure never refreshes a changed input in place, replays a suite, or writes the canonical Project control carriers.

6. Before issuing the sealed Unit command, resolve the exact `[release_suite].unit_timeout_seconds` value from the captured bytes. An explicit Framework Instance value overrides the canonical default; an absent instance table/key falls back to the default. Accept only a finite numeric value that is not `bool`, is greater than zero, and is no greater than `7200` seconds. Write the derived private `unit-deadline.json` snapshot specified by CA-D-579 with the two source fingerprints, `control_context_digest`, configured seconds, and effective seconds; verify it against the captured context. A private fixture timeout may only shorten the configured value. This snapshot adds no public receipt or schema-2 field, and any source or context mismatch remains non-passing.
