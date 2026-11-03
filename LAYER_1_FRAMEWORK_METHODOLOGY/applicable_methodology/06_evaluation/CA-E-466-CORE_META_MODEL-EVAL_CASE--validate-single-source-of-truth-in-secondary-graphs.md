---
subjects:
  active: CAPRMEDIO <+ MODEL <+ Entity
  passive:
  - CAPRMEDIO <+ MODEL <+ Projection
  - CAPRMEDIO <+ MODEL <+ Atom
  - CAPRMEDIO <+ MODEL <+ Atom.Content
  - CAPRMEDIO <+ MODEL <+ Entity
  - CAPRMEDIO <+ MODEL <+ Journal
  - CAPRMEDIO <+ MODEL <+ CFEL > Relation
version: 28
updated_at: 2026-11-02 00:18:22 +0400
relations:
  evaluation_for:
  - CA-R-1437
  - CA-R-1470
  - CA-R-1471
  - CA-R-2535
atom_id: CA-E-466
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Evaluation
form: Eval Case
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation/CA-E-466-CORE_META_MODEL-EVAL_CASE--validate-single-source-of-truth-in-secondary-graphs.md
  source_atom_id: CA-E-466
  source_atom_revision: 28
  source_sha256: 9c85214ae66eacb3488df623db3d3cfd8759f1204cc73348aa2c05237a7051b7
  original_relations_sha256: 8db81e4f3cb2102db425222e58f0524bd60d360c9981ec917f8eb310b4cbb0d1
---
## Summary
Validate Single Source of Truth in secondary graphs

## Claim scope
source authority **in** secondary graph representations.

## Claim
the Evaluation **must** distinguish authoritative source facts from their secondary graph representations **and** reject a Projection that acquires independent authority for a represented fact.

### Test cases

| Case | Expected result |
|---|---|
| **`=1`** source Claim represented **in** multiple graphs | pass **if** **all** representations retain the same source identity **and** applicable Revision |
| two independently maintained authoritative declarations for the same fact **in** the same context, even **when** their values agree | fail |
| different Claims **or** different source facts used by a derived result | no Single Source of Truth failure merely because there are multiple source Atoms |
| a permitted derived Relation with identified derivation authority **and** source inputs, but no separately authored declaration for its computed result | pass this source-authority check |
| a derived edge with no admitted derivation authority **or** missing required source evidence | fail **or** report unresolved evidence; do **not** invent a source declaration |
| a source Atom reached through another Projection | pass **if** ultimate source traceability is retained |
| a Journal event **or** structural fact represented **in** a graph | pass **if** its existing source authority remains intact; do **not** fabricate an Atom Claim as historical **or** observed evidence |
| a projected fact corrected independently while its source **and** governing derivation remain unchanged | fail |

passing this source-authority Evaluation does **not** establish graph-specific Relation validity, completeness, **or** the truth of a recorded outcome; those remain subject **to** their applicable Evaluations.
