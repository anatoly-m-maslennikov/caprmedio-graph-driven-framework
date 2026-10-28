---
atom_id: CA-D-509
content_role: Delivery
current_scope_unit: PROMPTS
claim_target_scope_unit: PROMPTS
status: Active
author: Anatoly Maslennikov
version: 12
updated_at: 2026-10-27 19:59:26 +0400
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Authoring/Prompt Authoring
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Storage/Directory Layout
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Step'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Workflow'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
relations: {}
tier: 3
type: Eng Decision
---
# Summary

Store the RMED review prompt package

## Scope

the delivered prompt package for RMED Atoms Base Revise within the Implementation Folder of PROMPTS.

## Claim

the prompt package **must** occupy `ACTION_PROMPTS/RMED_ATOM_REVIEW/` relative **to** the PROMPTS Implementation Folder declared **in** `project_structure.toml`, with these canonical Carriers.

## Details

| Carrier | Contents |
|---|---|
| `CA-O-108.prompt.md` | gathering instructions bound **to** Step `CA-O-108` **and** Action `CA-O-105` |
| `CA-O-109.prompt.md` | checking instructions bound **to** Step `CA-O-109` **and** Action `CA-O-106` |
| `CA-O-110.prompt.md` | correction instructions bound **to** Step `CA-O-110` **and** Action `CA-O-111` |
| `README.md` | invocation guidance **and** the current three-Step implementation interface |
| `source_bindings.json` | referenced source Atom IDs, paths, Versions, **and** source digests |
| `workflow_progress.py` | report-based progress aggregation |
| `tests/` | implementation tests **and** their mock evidence |

the prompt file header carries its Step, Action, **and** execution-context binding. instruction text realizes those methodology definitions; it is **not** another source of operational authority. optional evaluator **and** legacy helper Carriers remain separate from the default three-Step interface.
