---
atom_id: CA-A-1274
content_role: Analysis
type: Specification Proposal
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
status: Done
author: Anatoly Maslennikov
subjects:
  governs: Model
version: 2
updated_at: 2026-10-29 21:51:04 +0400
relations: {}
tier: 3
---
# Summary

Use API as the interface umbrella

## Decision

API is enough as the umbrella for a Package invocation interface. API forms can include CLI, Web API/REST API, RPC and others. Do not treat API and CLI as two peer categories, or create separate primary branches for every example now. Some Packages expose a public API; API exposure is not mandatory for every Package. Public here concerns the exposed Package boundary, without implying Internet deployment.

## State

Model/Definition preparation only. Current methodology, Engine code and runtime are unchanged.
