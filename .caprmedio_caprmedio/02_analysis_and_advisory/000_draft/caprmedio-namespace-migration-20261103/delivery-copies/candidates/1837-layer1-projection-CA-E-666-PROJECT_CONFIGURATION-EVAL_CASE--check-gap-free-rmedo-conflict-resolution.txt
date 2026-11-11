---
subjects:
  active: 'CAPRMEDIO <+ STRUCTURE <+ Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Workflow//RMEDO Conflict Resolution'
  passive:
  - CAPRMEDIO <+ MODEL <+ Atom
  - CAPRMEDIO <+ MODEL <+ Atom.Content
  - CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Atom.Version Number
  - CAPRMEDIO <+ MODEL <+ Atom.Tier
  - CAPRMEDIO <+ MODEL <+ Atom.Updated At
  - 'CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Atom.Tier.Label: Scope Contract'
  - CAPRMEDIO <+ MODEL <+ CFEL > Relation
  - CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Actor/Operator
  - CAPRMEDIO <+ STRUCTURE <+ Aspects <+ Engineering <+ Execution Control <+ Decision Confidence
  - CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/History/Journal > Event Record
version: 4
updated_at: 2026-11-02 18:35:20 +0400
relations:
  evaluation_for:
  - CA-O-028
  - CA-O-005
  - CA-O-006
  - CA-O-008
atom_id: CA-E-666
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
tier: 4
role: Evaluation
form: Eval Case
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/06_evaluation/CA-E-666-PROJECT_CONFIGURATION-EVAL_CASE--check-gap-free-rmedo-conflict-resolution.md
  source_atom_id: CA-E-666
  source_atom_revision: 4
  source_sha256: d4859110a218ac9d8add3ca3c0b61ccff7d78bd55d93fe5b8b2115bb03b280c6
  original_relations_sha256: 0cecd19a21d5691fcd7dd41da7255a71b2ca140c377c5f048aacd3758388e8eb
---
## Summary

Check gap-free RMEDO conflict resolution

## Claim scope

RMEDO Conflict Resolution **and** its reused Actions.

## Claim

The Evaluation **must** check whether RMEDO Conflict Resolution follows CA-O-028-PROJECT_CONFIGURATION-WORKFLOW--resolve-rmedo-conflicts-without-leaving-gaps **and** its reused Actions **without** losing required authority.

## Details

| Case | Expected result |
|---|---|
| an older lower-tier Claim conflicts with higher-tier authority | preserve the higher-tier authority; propose a permitted correction **or** archival of the conflicting Claim |
| a newer lower-tier Claim conflicts with higher-tier authority | Updated At does **not** reverse Global Tier precedence |
| equally applicable same-tier Claims conflict; the newer accepted Claim aligns with the applicable Project-wide foundational commitments | prefer the newer Claim; evaluate the older Atom for correction **or** archival |
| timestamps, applicability, **or** precedence are unresolved | report uncertainty; do **not** invent a winner |
| removing an obsolete Atom improves applicable Project-wide foundational commitments alignment; **all** coverage checks pass; valid delegation covers archival | archive **without** demanding another per-Atom approval; preserve exact history |
| an Atom has unique still-required content, an incoming reference needs repair, **or** a required Evaluation loses its target | block archival **until** the prerequisite coverage repair is active **and** checked |
| removal hides a conflict **or** leaves a missing required Claim, Relation, reference, **or** check | fail the completion claim |
| **all** Claims of an obsolete Atom are explicitly withdrawn by governing authority | preserve the archive **and** withdrawal evidence; do **not** invent a replacement Claim **or** successor |
| active Atoms expressing applicable Project-wide foundational commitments conflict, the effective confidence threshold is unmet, **or** mutation is outside delegation | ask the Operator; no autonomous resolution **or** mutation |
| a source changes **after** assessment, a correction is partial, **or** required rechecking is absent | no completion; report actual effects **and** reassess **only** within accepted retry bounds |

The check **must**:

- Use exact source Revisions; **and**
- compare the affected authority **before** **and** **after** correction.

An archival event alone is **not** evidence that **any** of the following passed:

- coverage;
- alignment;
- authorization; **or**
- conflict resolution.
