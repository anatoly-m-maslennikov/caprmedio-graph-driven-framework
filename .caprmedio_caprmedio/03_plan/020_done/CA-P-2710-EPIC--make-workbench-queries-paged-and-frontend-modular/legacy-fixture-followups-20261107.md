# Legacy fixture follow-up — 7 November 2026

These groups remain outside the completed Workbench runtime objectives. No validation was weakened and no Workflow or Atom migration was repaired in this pass.

| Owning work | Recorded issue | Next action |
|---|---|---|
| Atom lifecycle/canonical writer | Subject-update setup rejects changed or missing preserved legacy root fields (`ProposedCarrierError`); direct-subject protocol cases reach `complete-carrier-invalid`. | Align the owning fixtures/authorized carrier migration with current contracts; preserve Current validation. |
| Atom lifecycle/status migration | Status-matrix and old Subject fixtures conflict with current carrier assumptions. | Review in the owning migration work, independently of Workbench indexing. |
| Journal append and observation | Selected creation/replacement/observation fixtures raise `PartialAppendError`. | Review append fixtures and their actual Journal contract in the Journal-owning scope. |

Evidence: `runtime-acceptance-20261107.md` in this folder and its referenced `.caprmedio_tmp/workbench/performance-gates-20261107/core-retirement-suite.log`. The older broad run also contained subsequently fixed transient fixture failures, so its total is not presented as a current unresolved count. Do not infer a green full suite from focused runtime acceptance.
