---
atom_id: CA-D-509@13
ref_id: CA-D-509@13
container:
  scope_unit: CA-SU-24
role: Delivery
form: Eng Decision
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Authoring/Prompt
    Authoring
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Operation/Storage/Directory Layout
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Action'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Step'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type:
    Workflow'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
tier: 3
status: Archived
version: 13
updated_at: 2026-11-02 19:30:12 +0400
carrier_destination:
  file:
    name: CA-D-509@13-PROMPTS-ENG_DECISION--store-the-rmed-review-prompt-package.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-22_FEATURE_AGENTIC/CA-SU-24_FEATURE_PROMPTS/07_delivery/archive
current_scope_unit: PROMPTS
claim_target_scope_unit: PROMPTS
author: Anatoly Maslennikov
---
# Summary

Store the RMED review prompt package

## Scope

the delivered prompt package for RMED Atoms Base Revise within the Implementation Folder of PROMPTS.

## Claim

the prompt package **must** occupy `ACTION_PROMPTS/RMED_ATOM_REVIEW/` relative **to** the PROMPTS Implementation Folder derived from the current Scope Unit Declarations, with these canonical Carriers.

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
