---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: Subject/Engineering/Operational Diagnostics
  depends_on:
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Requirement'
  - Subject/Engineering/Carrier
version: 12
updated_at: 2026-10-23 03:06:32 +0400
relations:
  evaluation_for:
  - CA-M-414
  derived_from:
  - CA-A-053
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-E-369@12
content_role: Evaluation
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
local_tier: Standard
global_tier: 8
status: Archived
author: Anatoly Maslennikov
---
# Reject unbounded production DEBUG logging

## Claim checked

production DEBUG logging is disabled by default **and** **may** be enabled **only** through
a bounded selector with automatic expiry **and** unchanged redaction.

## Test case

evaluate one production component configuration that enables DEBUG globally
**without** an expiry.

## Acceptance criteria

pass **only** **when** the configuration is rejected **before** deployment.

## Failure disposition

block production DEBUG **until** component, subject, run, entity, **or** equivalent
scope **and** automatic expiry are present.

## Sources

- [CA-M-414 — Emit structured operational diagnostics](../05_method/CA-M-414-PROGRAMMATIC-STANDARD-IMPLEMENTATION_METHOD--emit-structured-operational-diagnostics.md)
