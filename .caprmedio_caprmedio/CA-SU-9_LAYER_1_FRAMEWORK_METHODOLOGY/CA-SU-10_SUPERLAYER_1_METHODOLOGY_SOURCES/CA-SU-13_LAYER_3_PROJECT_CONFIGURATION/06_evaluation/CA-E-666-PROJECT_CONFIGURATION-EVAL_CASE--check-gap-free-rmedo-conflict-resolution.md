---
subjects:
  active: 'CAPRMEDIO_STRUCTURE <+ Atom/(.Header.Role := Operations)/(.Header.Form := Workflow)//RMEDO Conflict Resolution'
  passive:
  - CAPRMEDIO_MODEL <+ Atom
  - CAPRMEDIO_MODEL <+ Atom.Content
  - CAPRMEDIO_MODEL <+ Atom.Header.Version
  - CAPRMEDIO_MODEL <+ Atom.Header.Tier
  - CAPRMEDIO_MODEL <+ Atom.Header.Updated At
  - 'CAPRMEDIO_MODEL <+ Atom.Header.Tier.Label: Scope Contract'
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/Operator
  - CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Execution Control <+ Decision Confidence
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/History/Journal <+ Event Record
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
---
## Summary

Check gap-free RMEDO conflict resolution

## Claim

### Prose Claim


RMEDO Conflict Resolution **and** its reused Actions.


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
