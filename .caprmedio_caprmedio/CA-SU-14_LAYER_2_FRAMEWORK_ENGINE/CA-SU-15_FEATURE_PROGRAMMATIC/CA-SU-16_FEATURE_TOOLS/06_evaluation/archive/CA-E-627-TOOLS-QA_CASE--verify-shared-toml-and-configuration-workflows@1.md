---
atom_id: CA-E-627
content_role: Evaluation
type: QA Case
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Tool"
  depends_on: ["Tool","Workflow","Project Configuration","Scope Unit"]
version: 1
updated_at: "2026-10-12 23:13:13 +0400"
relations:
  evaluation_for: ["CA-R-1935"]
  relates_to: ["CA-M-375","CA-O-204","CA-O-205","CA-O-206"]
---
# Summary

Verify shared TOML and configuration workflows

## Scope

Required future checks for one shared TOML connector and configuration-specific Project Structure and Project Settings workflows.

## Claim

The shared connector supplies TOML storage mechanics; each configuration workflow owns its complete schema/domain validation before an authorized effect. Configuration kinds do not create separate connectors.

## Details

- Exercise Project Structure and Project Settings through their own workflows using the same TOML connector. Verify an accepted change and truthful no-op with exact expected/observed source-state evidence and no unrelated configuration effect.
- Independently validate complete proposed TOML and each configuration's admitted schema, including types, required fields, unknown keys and applicable structural/domain constraints. Valid TOML syntax alone cannot pass a configuration workflow.
- Reject edits to generated or protected fields and keep unrelated settings intact. Configuration-specific workflows use the admitted Project Structure and Project Settings source identities; a raw connector call cannot select an arbitrary configuration source.
- Reject malformed TOML, schema-invalid values, missing/ambiguous authority, stale source state and denied permission before the affected action writes. Recheck bound state at its effect boundary and preserve the prior admitted state on the action's claimed failure boundary.
- Verify Scope Unit Create through the Project Structure schema and workflow. A raw connector write cannot admit an undeclared Scope Unit or bypass structural validation.
- Return actual effects or explicit failure/uncertainty with the existing shared result/recording contract. No arbitrary configuration path, additional connector or hidden cross-configuration effect is inferred.
- Treat current file/TOML implementation behavior as the only backend behavior available for later proof. A replaceable backend contract is not a DB implementation or a concurrency/publication guarantee.

### Acceptance and failure disposition

Require independent before/proposed/after configuration ledgers and schema/currentness/permission evidence. Reject schema bypass, implicit connector multiplication, unproved restoration, false completion or lost accepted history. New workflow resume/retry and stronger concurrency/publication guarantees remain deferred. This source specifies required verification and records no actual test pass.
