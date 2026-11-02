---
cce_version: cce_1
cce_form: atomicity
subjects:
  governs: Subject/Graph Node/Engineering/Delivery/Git Commits
  depends_on:
  - Subject/Graph Node/Domain/Continuant/History/Journal.Record
  - Subject/Graph Node/Carrier
version: 19
updated_at: 2026-10-27 06:04:45 +0400
relations: {}
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
content_role: Delivery
current_scope_unit: CORE_EXTENSIONS
status: Archived
author: Anatoly Maslennikov
atom_id: CA-D-335@19
type: Eng Decision
tier: 1
---
# Mirror Governed File Changes in Journal and Git

**when** the Git Extension is selected, materialize **every** approved atomic change set as follows:

- create **`=1`** Git Commit containing **all** **and** **only** the approved changes; the change set **may** contain **`>=1`** File Carriers.
- retain **`=1`** canonical Journal file-change Event for **every** changed File Carrier, including **every** successor **and** predecessor Carrier changed by replacement.
- preserve the correspondence between the committed change set **and** its individual Journal Events; Git **must not** become another authoritative Journal.

successor **and** predecessor Carrier changes **may** share the approved atomic change set. their individual Journal Events **must not** require separate Git Commits.
