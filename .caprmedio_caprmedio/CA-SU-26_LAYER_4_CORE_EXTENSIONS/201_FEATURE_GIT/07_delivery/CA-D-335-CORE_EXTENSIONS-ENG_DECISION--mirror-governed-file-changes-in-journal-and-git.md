---
atom_id: CA-D-335
ref_id: CA-D-335
container:
  scope_unit: CA-SU-26
role: Delivery
form: Eng Decision
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Delivery/Git Commits
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal.Record
  - Subject/CAPRMEDIO/Carrier
tier: 1
status: Active
version: 20
updated_at: 2026-10-27 19:59:23 +0400
cce_version: cce_1
cce_form: atomicity
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
current_scope_unit: CORE_EXTENSIONS
author: Anatoly Maslennikov
---
# Mirror Governed File Changes in Journal and Git

**when** the Git Extension is selected, materialize **every** approved atomic change set as follows:

- create **`=1`** Git Commit containing **all** **and** **only** the approved changes; the change set **may** contain **`>=1`** File Carriers.
- retain **`=1`** canonical Journal file-change Event for **every** changed File Carrier, including **every** successor **and** predecessor Carrier changed by replacement.
- preserve the correspondence between the committed change set **and** its individual Journal Events; Git **must not** become another authoritative Journal.

successor **and** predecessor Carrier changes **may** share the approved atomic change set. their individual Journal Events **must not** require separate Git Commits.
