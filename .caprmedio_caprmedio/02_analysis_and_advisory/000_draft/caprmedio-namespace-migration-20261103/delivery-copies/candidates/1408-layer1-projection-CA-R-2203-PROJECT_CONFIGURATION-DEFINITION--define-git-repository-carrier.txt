---
atom_id: CA-R-2203
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
subjects:
  active: CAPRMEDIO <+ MODEL <+ Carrier/Git Repository
version: 6
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 1
role: Requirement
form: Entity Definition
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/04_requirement/CA-R-2203-PROJECT_CONFIGURATION-DEFINITION--define-git-repository-carrier.md
  source_atom_id: CA-R-2203
  source_atom_revision: 6
  source_sha256: fbeed3993adce63288998a854c490bdf38466fe000f85e145aa4dc797b07b065
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Define Git Repository Carrier

## Claim

A Git Repository **means** a Carrier of versioned content and Git references.

### Formal claim

```text
Git Repository > @(Git Branch)
```

## Semantics

A remote repository or branch on GitHub is another Carrier. Git Repository > Git Branch denotes whole/part containment. Local connection names and URLs describe how the repository is selected.
