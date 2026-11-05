---
atom_id: CA-R-1942
ref_id: CA-R-1942
role: Requirement
form: Rule
current_scope_unit: CONNECTOR_TOOLS
claim_target_scope_unit: CONNECTOR_TOOLS
status: Active
author: Anatoly Maslennikov
version: 12
updated_at: 2026-11-02 19:44:26 +0400
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Project Model/Governing Configuration
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project
  - Scope Unit
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Settings
tier: 3
container:
  scope_unit: CA-SU-17
carrier_destination:
  file:
    name: CA-R-1942-CONNECTOR_TOOLS-RULE--read-one-complete-toml-configuration.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-17_FEATURE_CONNECTOR_TOOLS/04_requirement
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
