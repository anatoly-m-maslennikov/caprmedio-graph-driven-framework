---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Data Handling/Data Transformation
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Content
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Summary
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Projection
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Authoring/Controlled English
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control/Decision Confidence
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: AI Agent'
version: 21
updated_at: 2026-10-29 23:58:03 +0400
relations:
  child_of:
  - CA-M-443
  - CA-R-380
atom_id: CA-O-053
content_role: Operations
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
author: Anatoly Maslennikov
type: Action
tier: 3
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/09_operations/CA-O-053-PROJECT_CONFIGURATION-ACTION--migrate-atoms-to-a-current-cce-version.md
  source_atom_id: CA-O-053
  source_atom_revision: 21
  source_sha256: 288cdff640b4ef6d048330b43eedccc79f9c124597cd1295c6c56b7bcf3cba61
  original_relations_sha256: e6f49019e8e73920ff560e36d53d124d605d60ba73f55c4bd9de725847b0b85b
---
# Summary

Migrate Atoms to a current CCE version

## Operation

Migrate Atom CCE Representation **means** the reusable Action that converts **`=1`** Atom's representation **to** the current CCE version while preserving its Claim, identity, **and** lifecycle. repeat this Action one Atom at a time for a selected set.

1. read the Atom's complete current Claim **and** applicable CCE authority.
2. convert its representation **without** changing the Claim **or** lifecycle. preserve its identity under CA-R-1432 **and** keep its Summary fixed under CA-R-1464; a required replacement is **not** an identity-preserving CCE migration.
3. validate its **`=1`** Claim **and** source-faithful derived Projections. checking the Summary does **not** authorize regenerating it for the same Atom identity.
4. resolve the effective Confidence Threshold for the migration according **to** CA-M-271. **if** semantic confidence is below that value, **then** request Operator disposition **before** continuing.

an Operator **or** AI Agent **may** perform this Action within its existing authority. the conversion **must not** silently split **or** merge Claims, replace an Atom's identity, **or** change its Summary; those effects require the separately governed replacement boundary under CA-R-1432. preserving identity does **not** prohibit a required Revision.

## Details
