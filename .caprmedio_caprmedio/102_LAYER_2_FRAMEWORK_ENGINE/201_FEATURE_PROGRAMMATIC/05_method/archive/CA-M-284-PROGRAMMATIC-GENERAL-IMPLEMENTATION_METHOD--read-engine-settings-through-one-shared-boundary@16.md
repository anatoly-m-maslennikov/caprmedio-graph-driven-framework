---
atom_id: "CA-M-284"
content_role: "Method"
type: "Implementation Method"
current_scope_unit: "PROGRAMMATIC"
claim_target_scope_unit: "PROGRAMMATIC"
local_tier: "General"
global_tier: 7
author: "Anatoly Maslennikov"
status: "Active"
subjects:
  governs: "engine-settings-reader"
  depends_on:
    - "Carrier"
    - "Projection"
    - "Artifact/Revision"
    - "Project Settings"
    - "programmatic software"
version: 16
updated_at: "2026-10-21T23:29:13+00:00"
relations:
  derived_from:
    - "CA-A-053"
  child_of:
    - "CA-M-415"
---
# Summary

Read Engine settings through one shared boundary

## Scope

apply **when** PROGRAMMATIC behavior depends on Project Settings.

## Claim

use one centralized Settings Reader for **every** applicable Tool, App, **and** MCP
component. the Reader reads the authoritative Project Settings Artifact,
validates the complete input, **and** returns an immutable typed snapshot with
the actual validated values, exact selected Project, physical source path,
raw SHA-256 Digest, **and** declared schema marker. the Reader **must not** query
the Work Journal **or** determine logical Revision **or** currentness. the snapshot
is derived; Project Settings is **not** a Projection.

## Details

### Procedure
1. read the authoritative Project Settings Carrier bound by CA-D-364 through
   the shared Reader; do **not** infer a replacement from a legacy filename.
2. validate the complete carrier at the boundary **and** return structured
   diagnostics for invalid input.
3. pass the immutable snapshot explicitly **to** the consuming deterministic core
   **or** application service.
4. do **not** add component-specific parsers, default chains, environment
   fallbacks, semantic overrides, **or** writes **to** the Reader.
5. make the control panel use the same Reader **and** request changes **to** the
   authoritative Project Settings Artifact through its dedicated Doer, **not**
   through the Reader, its immutable snapshot, **or** a Projection.

### Outcome

**every** component observes one validated settings snapshot **without** duplicating
parsing **or** inventing a second control panel.

### Failure or stop

stop **when** the authoritative Project Settings Carrier is missing **or** schema-invalid,
mandatory physical source path **or** Digest provenance is absent, **or** a consumer
would bypass **or** mutate the shared snapshot.

### Sources

- [Python documentation: `tomllib`](https://docs.python.org/3.14/library/tomllib.html)
- [Pydantic: strict mode](https://docs.pydantic.dev/latest/concepts/strict_mode/)
- [CA-A-053 — Reconcile shared PROGRAMMATIC policy decisions](../02_analysis/CA-A-053-PROGRAMMATIC-ANALYSIS_RPRT--reconcile-shared-programmatic-policy-decisions.md)
