---
atom_id: CA-A-1267
content_role: Analysis & Advisory
type: Specification Proposal
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
status: Done
author: Anatoly Maslennikov
subjects:
  governs: Formal Model
version: 3
updated_at: 2026-11-02 15:49:28 +0400
relations: {}
tier: 3
---
# Summary

Allow Modules and Assets for runtime or tests

## Decision

Modules and Asset files can be for runtime or for tests. Runtime versus tests describes usage, not another primary kind: executable Module versus non-executable Asset remains the structural distinction. Both uses stay inside Package.

Examples: application code and test code are Modules; a configuration file consumed by the runtime and fixture data consumed by tests are Assets. Documentation remains descriptive/reference content, separate from the required runtime/test inputs and from executable Prompts.

This resolves the runtime-versus-tests question left in CA-A-1266. It does not add Test Module or Test Asset Types, a mandatory usage property, or a closed purpose enumeration. The remaining Resources member definitions can now be reviewed under this distinction; this record does not silently migrate or retire them.

## State

The affected Definition Drafts and proposal are refined. Current Atoms, implementation files and runtime remain unchanged.
