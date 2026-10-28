---
subjects:
  governs: Subject/CAPRMEDIO/Carrier/File
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project
  - Subject/CAPRMEDIO/Carrier/Directory
version: 16
updated_at: 2026-10-27 19:59:25 +0400
relations: {}
atom_id: CA-D-452
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 3
type: Eng Decision
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
