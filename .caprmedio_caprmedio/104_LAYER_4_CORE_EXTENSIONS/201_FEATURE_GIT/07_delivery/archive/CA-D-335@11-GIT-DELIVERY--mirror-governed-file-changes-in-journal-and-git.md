---
cce_version: cce_1
cce_form: atomicity
subjects:
  governs: Governed File Change Materialization
  depends_on:
  - Journal/Record
  - Git Commit
  - Carrier
version: 11
updated_at: 2026-10-24 02:14:24 +0400
relations: {}
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
content_role: Delivery
current_scope_unit: CORE_EXTENSIONS
status: Archived
author: Anatoly Maslennikov
atom_id: CA-D-335@11
type: Eng Decision
tier: 1
---
# Mirror Governed File Changes in Journal and Git

**when** the Git Extension is selected, materialize **every** approved atomic change set as follows:

- create **`=1`** Git Commit containing **all** **and** **only** the approved changes; the change set **may** contain **`>=1`** File Carriers.
- retain **`=1`** canonical Journal file-change Event for **every** changed File Carrier, including **every** successor **and** predecessor Carrier changed by replacement.
- preserve the correspondence between the committed change set **and** its individual Journal Events; Git **must not** become another authoritative Journal.

successor **and** predecessor Carrier changes **may** share the approved atomic change set. their individual Journal Events **must not** require separate Git Commits.
