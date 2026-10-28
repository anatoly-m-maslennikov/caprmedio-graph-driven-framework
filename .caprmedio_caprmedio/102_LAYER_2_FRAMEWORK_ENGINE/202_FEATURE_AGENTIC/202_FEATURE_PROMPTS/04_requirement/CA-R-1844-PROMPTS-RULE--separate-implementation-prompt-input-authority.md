---
atom_id: CA-R-1844
content_role: Requirement
type: Rule
current_scope_unit: PROMPTS
claim_target_scope_unit: PROMPTS
status: Active
author: Anatoly Maslennikov
version: 11
updated_at: 2026-10-27 20:00:04 +0400
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Authoring/Prompt Authoring
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control/Effect Authorization
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Requirement'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Delivery'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Method'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Evaluation'
relations: {}
tier: 3
---
# Summary

Separate implementation prompt input authority

## Scope

the admitted input packet passed to one current Implementation Workflow prompt.

## Claim

the Implementation **must** carry selected active R/D targets as what to implement, one verified complete active-M projection as how to implement, and applicable E atoms as separate checks, each with identity, revision, path, digest, and full required content.

## Details

The M projection is a derived Run input, sorted repeatably and retained downstream; membership does not establish applicability. Missing, stale, conflicting, unauthorized, or incomplete inputs return the source Step's blocked result.
