---
atom_id: CA-E-220
subject_scopes:
  - evaluation
version: 3
updated_at: 2026-08-21 04:24:00
relations:
  evaluation_for:
    - CA-R-856
    - CA-M-103
  check_of:
    - CA-D-011
---
# Install one self-contained release and all Hooks

## Claim checked

One apply installs a verified self-contained Tool release, stable launchers, the enabled Codex adapter, both Codex Hook phases, and all three Git Hook phases through `.caprmedio_install`.

## Test case

Install the complete canonical Tool source into a clean repository, inspect status, invoke the common machine interface of representative installed Tools, and load every installed executable entrypoint with the canonical source absent from its import path.

## Acceptance criteria

Status verifies every installed digest, current release, launcher, adapter, Codex Hook carrier, Git Hook, and `core.hooksPath`. The Codex Hook command addresses the stable `commit-trigger` launcher, status identifies host activation as requiring or depending on operator-controlled Codex review, representative Tool entrypoints return valid machine envelopes, every installed executable loads successfully, and `.caprmedio_install` contains no bytecode, cache, log, PID, or mutable runtime state.

## Failure disposition

Reject delivery if any Tool or dependency is missing, any Hook addresses another location, an installed Tool imports implementation outside its release, or mutable state enters the installation.
