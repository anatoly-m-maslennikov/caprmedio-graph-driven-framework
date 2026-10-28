---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: Subject/Graph Node/Engineering/Architecture/Component Structure
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Project.Settings
  - Subject/Graph Node/Carrier
version: 19
updated_at: 2026-10-27 06:04:45 +0400
relations:
  evaluation_for:
  - CA-M-417
  - CA-M-284
  derived_from:
  - CA-A-053
atom_id: CA-E-454@19
content_role: Evaluation
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
status: Archived
author: Anatoly Maslennikov
tier: 5
type: Eval Case
---
# Use one Settings Reader across Engine software

## Claim checked

representative Tool, App, **and** MCP consumers use one immutable, validated,
versioned settings snapshot.

## Test case

replace the shared Reader with a recording fake **and** execute one representative
consumer from **every** PROGRAMMATIC child feature.

## Acceptance criteria

pass **only** **when** the shared Reader validates the input at its boundary **and** **every** consumer receives the immutable snapshot explicitly, preserves the same Carrier **and** digest provenance, **and** performs no direct read, fallback, private default selection, **or** mutation. a consumer **may** reuse an already validated snapshot **without** calling the Reader; this Evaluation does **not** impose a per-consumer read count.

## Failure disposition

reject the bypassing consumer **until** it accepts the shared snapshot explicitly.

## Sources

- [Python documentation: `unittest.mock`](https://docs.python.org/3.14/library/unittest.mock.html)
- [CA-M-284 — Read Engine settings through one shared boundary](../05_method/CA-M-284-PROGRAMMATIC-ENG_POLICY--read-engine-settings-through-one-shared-boundary.md)
