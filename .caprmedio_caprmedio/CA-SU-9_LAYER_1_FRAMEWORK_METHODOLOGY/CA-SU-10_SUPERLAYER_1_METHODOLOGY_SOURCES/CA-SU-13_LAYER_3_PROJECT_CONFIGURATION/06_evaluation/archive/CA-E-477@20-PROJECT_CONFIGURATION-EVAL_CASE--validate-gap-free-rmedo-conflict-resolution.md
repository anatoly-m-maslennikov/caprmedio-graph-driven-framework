---
subjects:
  governs: 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Workflow//RMEDO Conflict Resolution'
  depends_on:
  - Subject/Domain/Node/Continuant/Atom
  - Subject/Domain/Node/Continuant/Atom.Content
  - Subject/Domain/Node/Continuant/Atom.Version Number
  - Entity/Node/Continuant/Atom.Global Tier
  - Subject/Domain/Node/Continuant/Atom.Updated At
  - 'Subject/Domain/Node/Continuant/Atom.Tier: Principle'
  - Subject/Graph/Relation
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
  - Subject/Engineering/Autonomous Confidence Threshold
  - Subject/Domain/Node/Continuant/History/Journal.Record
version: 20
updated_at: 2026-10-24 19:39:48 +0400
relations:
  evaluation_for:
  - CA-O-028
  - CA-O-005
  - CA-O-006
  - CA-O-008
atom_id: CA-E-477@20
content_role: Evaluation
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Archived
author: Anatoly Maslennikov
type: Eval Case
tier: 4
---
# Summary

Validate gap-free RMEDO conflict resolution

## Scope

RMEDO Conflict Resolution **and** its reused Actions.

## Claim

the Evaluation **must** check whether RMEDO Conflict Resolution follows CA-O-028 **and** its reused Actions **without** losing required authority.

## Details

| Case | Expected result |
|---|---|
| an older lower-tier Claim conflicts with higher-tier authority | preserve the higher-tier authority; propose a permitted correction **or** archival of the conflicting Claim |
| a newer lower-tier Claim conflicts with higher-tier authority | Updated At does **not** reverse Global Tier precedence |
| equally applicable same-tier Claims conflict; the newer accepted Claim aligns with Principles | prefer the newer Claim; evaluate the older Atom for correction **or** archival |
| timestamps, applicability, **or** precedence are unresolved | report uncertainty; do **not** invent a winner |
| removing an obsolete Atom improves Principle alignment; **all** coverage checks pass; valid delegation covers archival | archive **without** demanding another per-Atom approval; preserve exact history |
| an Atom has unique still-required content, an incoming reference needs repair, **or** a required Evaluation loses its target | block archival **until** the prerequisite coverage repair is active **and** checked |
| removal hides a conflict **or** leaves a missing required Claim, Relation, reference, **or** check | fail the completion claim |
| **all** Claims of an obsolete Atom are explicitly withdrawn by governing authority | preserve the archive **and** withdrawal evidence; do **not** invent a replacement Claim **or** successor |
| active Principles conflict, the effective confidence threshold is unmet, **or** mutation is outside delegation | ask the Operator; no autonomous resolution **or** mutation |
| a source changes **after** assessment, a correction is partial, **or** required rechecking is absent | no completion; report actual effects **and** reassess **only** within accepted retry bounds |

the check **must** use exact source Revisions **and** compare the affected authority **before** **and** **after** correction. an archival event alone is **not** evidence that coverage, alignment, authorization, **or** conflict resolution passed.
