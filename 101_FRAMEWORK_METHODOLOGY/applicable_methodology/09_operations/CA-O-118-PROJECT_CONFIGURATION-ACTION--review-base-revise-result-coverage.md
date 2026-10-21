---
atom_id: CA-O-118
content_role: Operations
type: Action
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 6
updated_at: "2026-10-19 15:56:57 +0400"
subjects:
  governs: "RMED Atom Review Coverage Gate Action"
  depends_on: ["Entity/Node/Continuant/Atom/Content Role: Operations/Type: Workflow", "Entity/Node/Continuant/Atom/Content Role: Operations/Type: Step", "Entity/Node/Continuant/Atom/Content Role: Operations/Type: Action", "Entity/Node/Continuant/Atom", "Entity/Node/Continuant/Actor/Type: Operator", "Entity/Node/Continuant/History/Journal"]
relations:
  relates_to: [CA-O-104]
projection:
  source_carrier_path: ../../sources/003_PROJECT_CONFIGURATION/09_operations/CA-O-118-PROJECT_CONFIGURATION-ACTION--review-base-revise-result-coverage.md
  source_atom_id: CA-O-118
  source_atom_revision: 6
  source_sha256: c9e83186d4243a879d2ce8cbc7b15c64cf662817bf615e9fcc666eca64f1e390
  original_relations_sha256: 0e0a2445b2c035e0671f11f830da82891997aa34348962a7fd52c6d1de7ad708
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
