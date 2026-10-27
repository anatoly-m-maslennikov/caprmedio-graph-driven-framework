---
atom_id: CA-R-1942@9
content_role: Requirement
type: Rule
current_scope_unit: CONNECTOR_TOOLS
claim_target_scope_unit: CONNECTOR_TOOLS
status: Archived
author: Anatoly Maslennikov
version: 9
updated_at: 2026-10-26 05:59:45 +0400
subjects:
  governs: Subject/Graph Node/Domain/Continuant/Governing Configuration
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Project
  - Subject/Graph Node/Engineering/Project Structure Declaration
  - Subject/Graph Node/Engineering/Project Settings Snapshot
relations: {}
tier: 3
---
# Summary

Read one complete TOML configuration

## Scope

effect-free complete Read of one explicit Project Structure **or** Project Settings configuration through the shared TOML connector.

## Claim

the Configuration Read result **must** contain the complete authoritative TOML source **and** its complete parsed values for exactly one logical configuration **in** the bound Project, with exact observed source-state evidence **and** no mutation. Read is independently callable **without** Query, Modify **or** an enclosing Workflow.

an unpinned current Read **must not** require a pre-known source pin. a supplied pin **or** explicit historical view **must** match the exact available admitted source; missing history **or** stale evidence **must not** fall back **to** the latest source. the caller's context selects source authority **and** schema; the connector checks these bindings **without** choosing them. missing, ambiguous, denied, invalid **or** unreadable sources **must** return a structured failure, **not** a successful empty **or** partial document.

## Details

CA-D-631 fixes the representation **and** CA-O-218 binds Read on the same TOML connector as CA-O-204 Modify. no configuration, Carrier, history, Version, timestamp, lifecycle **or** runtime state is changed by Read. this contract does **not** admit a live route, a new backend **or** new history retention.
