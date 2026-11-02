---
atom_id: CA-A-1271@2
content_role: Analysis
type: Specification Proposal
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Model
version: 2
updated_at: 2026-10-29 21:51:04 +0400
relations: {}
tier: 3
---
# Summary

Keep Asset distinct from File Carrier

## Decision

Use Package > Asset, not Asset File. Asset is the logical, non-executable Implementation content needed by runtime or tests. Files are Carriers representing that content; being carried in a file does not make File part of the logical-kind name.

This overrides the Asset File naming decision in CA-A-1270. Keep the Runtime Package/Test Package specializations, common Module and Asset kinds, separate Documentation, and the Model root unchanged. It introduces no alias, new usage field, representation-count rule or runtime behavior.

## State

Restore the prepared Asset Definition as the promotion candidate. Keep the Asset File Draft only as explicitly superseded history. Current methodology and historical review reports remain unchanged.
