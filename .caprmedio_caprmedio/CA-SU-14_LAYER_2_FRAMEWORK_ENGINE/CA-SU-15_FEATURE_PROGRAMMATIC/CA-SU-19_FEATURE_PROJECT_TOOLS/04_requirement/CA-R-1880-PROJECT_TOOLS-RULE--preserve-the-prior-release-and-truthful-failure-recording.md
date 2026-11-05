---
atom_id: CA-R-1880
ref_id: CA-R-1880
container:
  scope_unit: CA-SU-19
role: Requirement
form: Rule
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Delivery
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control/Recovery
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Workflow Run
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution/Action Run
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Term//Artifact
  - Subject/CAPRMEDIO/Carrier/Docker Image
tier: 3
status: Active
version: 16
updated_at: 2026-10-27 20:00:05 +0400
carrier_destination:
  file:
    name: CA-R-1880-PROJECT_TOOLS-RULE--preserve-the-prior-release-and-truthful-failure-recording.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-19_FEATURE_PROJECT_TOOLS/04_requirement
current_scope_unit: PROJECT_TOOLS
author: Anatoly Maslennikov
---
# Summary

Preserve the prior release and truthful failure recording

## Scope

Local/public release failure, uncertain effects and current-Project image cleanup.

## Claim

Release Version **must** preserve the prior runtime until its prepared replacement is ready, report actual effects and failures truthfully, and never replay an uncertain effect automatically. After successful replacement and Project-MCP readiness, it **must** retire only verified superseded release-owned images for the current Project whose exact immutable identity and ownership are known and which have no retaining container or protected reference.

## Details

Preserve the current image and unrelated, other-Project or protected images. Establish current-Project ownership from actual build/launcher/start evidence containing immutable image identity and Project identity, checked against Docker inspection; a tag prefix alone is insufficient. Cleanup includes the exact prior image when eligible and reports removed, protected, in-use or unproven results. Do not force-remove containers or claim complete cleanup when ownership or use remains uncertain.

A failure after a real effect reports that partial state and the failed step for manual handling. It does not claim automatic rollback, restore a retired runtime selector or replay an unknown effect. A request, test result or prepared package is not release success. Preserve source data and unrelated configuration; no failure permits broad image pruning.

Journal records describe what happened. Earlier records, baseline rows, terminal-recording recovery and proof receipts are not prerequisites for a release or its first recorded change. A missing Journal record does not undo a real effect or turn it into a different outcome.
