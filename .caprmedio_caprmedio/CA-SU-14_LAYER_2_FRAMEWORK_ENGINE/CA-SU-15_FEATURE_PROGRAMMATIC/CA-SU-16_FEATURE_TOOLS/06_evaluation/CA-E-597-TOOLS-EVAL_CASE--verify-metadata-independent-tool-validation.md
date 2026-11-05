---
atom_id: CA-E-597
ref_id: CA-E-597
container:
  scope_unit: CA-SU-16
role: Evaluation
form: Eval Case
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Data Handling/Data Validation
  dependencies:
  - Subject/CAPRMEDIO/Carrier
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Implementation
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Storage/Directory Layout
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Projection
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
tier: 4
relations:
  evaluation_for:
  - CA-R-1898
status: Active
version: 13
updated_at: 2026-10-27 19:59:38 +0400
carrier_destination:
  file:
    name: CA-E-597-TOOLS-EVAL_CASE--verify-metadata-independent-tool-validation.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-16_FEATURE_TOOLS/06_evaluation
current_scope_unit: TOOLS
author: Anatoly Maslennikov
---
# Summary

Verify metadata-independent Tool validation

## Scope

The persistent inventories and runtime message directories checked under CA-R-1898.

## Claim

The QA case **must** obtain the same validation result for otherwise identical fixtures with **and** without `.DS_Store`, while preserving failures for real invalid files.

## Details

1. Add Finder metadata at the root and nested paths of source, compiled output, retained package, public Skill, image context and runtime nonce-message fixtures. Compare selection, digests, currentness and validation results before and after.
2. Execute the fixed image canary's actual inventory checks against real fixture bytes. Metadata must not alter its result; a missing, changed, wrong-mode or other unexpected package file must still fail.
3. Preserve and reopen original legacy image proofs and the fixed metadata-aware proofs. Reject arbitrary canary code or changed isolation arguments.
4. Check that metadata bytes are not read, modified or deleted by validation. Distinct names such as `.ds_store` and `.DS_Store.bak` remain subject to ordinary admission.
5. Keep fixture results separate from actual Docker and Release acceptance. Historical failed attempts are not relabeled as successful.
