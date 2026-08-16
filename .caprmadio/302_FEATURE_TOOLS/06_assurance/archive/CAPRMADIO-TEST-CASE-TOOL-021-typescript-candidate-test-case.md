+++
artifact_id = "CAPRMADIO-ATOMIC-RECORD-014"
semantic_id = "CAPRMADIO-TEST-CASE-TOOL-021"
revision_mode = "atomic"
content_role = "method"
governance_origin = "internal"
relation_shape = "standalone"
scope_path = ["layer:tool"]
status = "accepted"
priority = "high"
llm_session_ids = ["codex:019f591f-04f6-70f2-8de7-828b7cccc69d"]

[[relations]]
type = "replacement_of"
target = "CAPRMADIO-TEST-CASE-TOOL-020"

[[relations]]
type = "child_of"
target = "CAPRMADIO-REQUIREMENT-TOOL-021"
+++

# Test Case — Validate the TypeScript candidate profile

Deterministic proof must validate the candidate profile's schema and identity,
the exact six gate mappings, pinned source evidence, safe relative paths,
canonical command sequence, warning-only ratchet, zero-error baseline,
candidate blocker semantics, and read-only target inspection.

Representative invalid fixtures must fail for a missing gate, unpinned source,
unsafe path, warning-count mismatch, non-zero error baseline, command absent
from the canonical sequence, active status with blockers, and target revision,
script, lockfile, or source/test-population drift.

This Test replaces `CAPRMADIO-TEST-CASE-TOOL-020` after its parent Requirement was
absorbed. This emitted Test definition is immutable. Runs and their evidence
are separate artifacts.
