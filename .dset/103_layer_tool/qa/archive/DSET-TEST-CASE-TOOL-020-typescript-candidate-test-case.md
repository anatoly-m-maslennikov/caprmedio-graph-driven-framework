+++
artifact_id = "DSET-ATOMIC-RECORD-011"
semantic_id = "DSET-TEST-CASE-TOOL-020"
revision_mode = "atomic"
content_role = "method"
governance_origin = "internal"
relation_shape = "standalone"
scope_path = ["layer:tool"]
status = "accepted"
priority = "high"
llm_session_ids = ["codex:019f591f-04f6-70f2-8de7-828b7cccc69d"]

[[relations]]
type = "child_of"
target = "DSET-REQUIREMENT-TOOL-020"
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

This emitted Test definition is immutable. Runs and their evidence are
separate artifacts.
