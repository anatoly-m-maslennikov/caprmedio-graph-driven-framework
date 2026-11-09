---
atom_id: CA-D-612@15
ref_id: CA-D-612@15
container:
  scope_unit: CA-SU-19
role: Delivery
form: Eng Decision
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Delivery
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Development/Architecture/Communication
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Implementation
tier: 3
status: Archived
version: 15
updated_at: 2026-11-02 19:46:47 +0400
carrier_destination:
  file:
    name: CA-D-612@15-PROJECT_TOOLS-ENG_DECISION--serialize-public-release-native-entrypoint-discovery.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-19_FEATURE_PROJECT_TOOLS/07_delivery/archive
current_scope_unit: PROJECT_TOOLS
claim_target_scope_unit: PROJECT_TOOLS
author: Anatoly Maslennikov
---
# Summary

Serialize public-release native entrypoint discovery

## Scope

The native description surface of the public-release Tool.

## Claim

The public-release source **must** expose its stable `PUBLIC_RELEASE` identity and `LAYER_2_FRAMEWORK_ENGINE/FEATURE_PROGRAMMATIC/FEATURE_PROJECT_TOOLS/PUBLIC_RELEASE/public_release.py` entrypoint. The direct `public.release` command uses this Project-bound implementation without a closed release-admission record or whole-registry validation gate.

## Details

Discovery describes the capability; it does not authorize Git or remote effects. Execute only on the Operator's public-release command for the selected Project and remote. Preserve the direct implementation's input, branch, URL and failure checks and its required full test suite, including integration tests.

This Delivery creates no alternate registry, caller-selected executor or standalone MCP adapter. The ordinary selected Workflows keep their own admission rules; removing obsolete release admission does not weaken them.
