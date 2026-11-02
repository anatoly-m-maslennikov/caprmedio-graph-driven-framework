---
subjects:
  governs: Subject/Graph Node/Domain/Continuant/History/Journal.Record
  depends_on:
  - Subject/Graph Node/Implementation/Code/Tool/Journal Append
  - Subject/Graph Node/Domain/Continuant/History/Journal.Record
  - Subject/Graph Node/Domain/Continuant/Atom
  - Subject/Graph Node/Carrier
  - Subject/Graph Node/Domain/Continuant/Project
  - 'Subject/Graph Node/Domain/Continuant/Projection/Type: Applicable Methodology'
cce_version: cce_1
cce_form: obligation
version: 30
updated_at: 2026-10-27 06:04:45 +0400
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
relations: {}
atom_id: CA-R-812@30
status: Archived
content_role: Requirement
author: Anatoly Maslennikov
current_scope_unit: TOOLS
type: Rule
tier: 1
---
# Append governed action records independently of real-change commits

APPEND_CHANGE_RECORDS **must** append supplied actual governed-action observations independently of that action's real-change Git commit.

## Append boundary

- append **may** occur **before** **or** **after** a real-change commit **and** **must not** be its admission gate.
- use plain Journal append/read under CA-R-1491, **without** prior-history, chain, validation, canonical-receipt, deduplication, retry **or** recovery prerequisites.
- preserve supplied observations **without** a Project-conformance judgment **or** fabricated baseline. a later Project change does **not** rebind an observation **to** later state.
- each requested append is an append, including repeated data. reading returns recorded entries **without** migrating, repairing **or** replaying them.

## Storage behavior

- reuse the shared Project Journal append/read implementation. do **not** introduce another writer, validator, reconciliation state **or** proof gate.
- leave existing entries unchanged; report actual I/O failure **and** any observed partial append truthfully, **without** automatic retry **or** source-effect replay.
- do **not** acquire a Git-effect lease, alter the index **or** create a Commit as part of append/read. a separately requested Journal-only Git commit remains governed by COMMIT_CHANGE_SET **and** its unchanged Git checks.
- Journal data records observations; it does **not** authorize **or** certify source changes, lifecycle outcomes, Run completion **or** Git effects.
