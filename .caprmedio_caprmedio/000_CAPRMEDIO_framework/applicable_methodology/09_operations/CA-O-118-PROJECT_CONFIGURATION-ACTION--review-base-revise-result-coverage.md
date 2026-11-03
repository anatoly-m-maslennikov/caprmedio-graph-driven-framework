---
atom_id: CA-O-118
content_role: Operations
type: Action
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
author: Anatoly Maslennikov
version: 13
updated_at: 2026-10-27 19:59:46 +0400
subjects:
  governs: Subject/caprmedio/Action//RMED Atom Review Coverage Gate Action
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Step'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
relations: {}
tier: 3
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/09_operations/CA-O-118-PROJECT_CONFIGURATION-ACTION--review-base-revise-result-coverage.md
  source_atom_id: CA-O-118
  source_atom_revision: 13
  source_sha256: d21eb00252353ba482fb741e69b0cf55429d63821f6819e15eec66392b35bb90
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Review Base Revise result coverage

## Operation

the Coverage Gate **must** compare saved main-Step results with their explicit expected work **and** return covered **only** at coverage **`=100`** percent.

## Details

- gather: compare the carried ordered selection **and** rule bindings with the frozen request; missing, duplicate, extra **or** unexplained work blocks coverage. an explicit empty selection has no omitted work.
- check: account for **all** selected Atoms **and** **all** **`=6`** required checks with evidence **and** concluded passed **or** failed results. blocked, pending **or** unknown results are missing coverage.
- fix: account for **all** selected Atoms **and** **all** initial findings with applied corrections **or** reasoned rejections. retain initial check evidence; blocked **or** unaccounted findings are missing coverage.
- report expected, covered, missing, coverage percent **and** evidence references. percentages do **not** round incomplete work to **`=100`**.
- incomplete **or** unknown coverage returns ask_operator with an explicit question; preserve completed effects **and** await an Operator decision.
- this Programmatic Action checks accounting, **not** whether an Atom **or** a repair is semantically correct.
