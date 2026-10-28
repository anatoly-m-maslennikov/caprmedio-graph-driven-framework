---
subjects:
  governs: 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type'
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Step'
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Authoring/Controlled English
version: 19
updated_at: 2026-10-27 19:59:42 +0400
relations:
  child_of:
  - CA-M-307
  depends_on:
  - CA-M-305
atom_id: CA-M-314
content_role: Method
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 6
type: Implementation Method
---
# Summary

Write Operations Claims with Type-specific CCE Profiles

## Scope

Operations Claims written with their admitted Operations Type-specific CCE Profiles.

## Claim

**to** write an Operations Claim, the Author **must** first resolve its admitted Operations Type **and** **then** apply **`=1`** primary Type profile:

1. for Action, use **means** to define the named reusable operational behavior. state its required inputs, preconditions, operational contribution, returned results, observable effects, **and** failure results. modality, condition, temporal, quantification, logical, restriction, predicate, **and** comparison Operators **may** constrain that behavior.
2. for Workflow, use **means** to define the reusable graph through Step references, entry, typed transitions, result conditions, **and** terminal outcomes. use condition, temporal, logical, restriction, predicate, **and** comparison Operators **only** with explicit transition scope under CA-M-305-CORE_META_MODEL-METHOD--write-workflow-schemes-using-step-references.
3. for Step, define the invocation binding of **`=1`** referenced Action with its parameters **and** inputs. do **not** copy the Action behavior **or** define another Workflow.

## Details

an Operations Claim **must not** combine more than one primary type profile. subordinate inputs, conditions, results, failures, transitions, **and** effects remain part of the selected type's single operational contribution.
