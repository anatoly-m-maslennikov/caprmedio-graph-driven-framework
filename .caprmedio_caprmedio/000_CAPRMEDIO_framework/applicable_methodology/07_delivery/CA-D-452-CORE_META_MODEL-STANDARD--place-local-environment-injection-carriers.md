---
subjects:
  governs: "Entity/Carrier/File Carrier"
  depends_on:
    ["Entity/Continuant/Object/Project", "Entity/Carrier/Directory Carrier"]
version: 6
updated_at: "2026-10-16 12:09:31 +0000"
relations: {}
atom_id: "CA-D-452"
content_role: "Delivery"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/07_delivery/CA-D-452-CORE_META_MODEL-STANDARD--place-local-environment-injection-carriers.md
  source_atom_id: CA-D-452
  source_atom_revision: 6
  source_sha256: 1e1979ce603da6c77a8e06224cdfc48a6ce690a5fcc38ad956c93fa1ffe1aa1b
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Place Local Environment Injection Carriers

## Scope

secret values and local environment injection Carriers.

## Claim

secret values **must** be stored **only** **in**:

- gitignored `.env` File Carriers; **or**
- a dedicated secret vault.

## Details

### File placement

- a repository-local `.env` File Carrier **must** remain outside **every** applicable Project authority Carrier root.
- **every** real `.env` variant **must** be gitignored, untracked, **and** excluded from durable **or** shared Git history **and** CAPRMEDIO discovery. a Git ignore rule does **not** remove a previously tracked secret from history.
- a tracked `.env.example` **may** contain variable names **and** unmistakable dummy placeholders **only**.

### Runtime injection

secret values **may** reach authorized runtime consumers through host injection from a permitted secret store; the injected value is **not** a separate persisted source.
