---
atom_id: "CA-O-020@draft"
content_role: Operations
type: Action
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
local_tier: Standard
author: Anatoly Maslennikov
status: "Draft"
subjects:
  governs: "Implementation Evaluation"
  depends_on:
    ["Entity/Node/Continuant/Atom/Content Role: Operations/Type: Action", "Atom/Content Role: Plan/Type: Plan", "Entity/Node/Continuant/Atom/Content Role: Evaluation", "Entity/Node/Continuant/Atom/Content Role: Method", "Implementation", "Artifact"]
version: 9
updated_at: "2026-10-19 11:49:15 +0000"
relations:
  relates_to:
    - CA-O-018
    - CA-O-089
    - CA-O-090
global_tier: 11
---
# Summary

Run implementation Evaluations

## Operation

Implementation Evaluation **means** the Agentic Action that executes the selected applicable checks against the current candidate **and** returns their actual results.

- inputs: the selected Plan, current candidate, admitted checks **and** commands, complete test inputs, current R/E/D **and** Method bindings, execution phase, **and** retained issue **and** regression evidence.
- run available checks, including baseline tests, regression tests, **and** required end-to-end tests. preserve failed, blocked, unevaluated, **and** stale outcomes; never replace execution with preparation **or** a remembered result.
- bind output **and** failure evidence **to** the actual candidate, commands, inputs, test definitions, **and** governing baseline. distinguish the initial pre-implementation run from a repair verification run.
- return `passed` **only** for complete current coverage with no failed **or** blocked checks; return `failed` with the available failure evidence; return `blocked` for missing execution prerequisites **or** untrustworthy/incomplete execution evidence. do **not** classify a failure as a code defect merely from the nonzero exit code.

## Details
