# Ordered source migration preparation

`prepare_metadata_migration.py` and its current `planned-operations.json` are INVALID and MUST NOT be applied: the prior regex planner can truncate YAML list values. Replacement requires YAML-node-span key renames with full-content before/after operations.

Apply only after the root integration gate rechecks every source hash, writes required nonnative-analysis backups, and routes foreign Workbench/workflow ownership separately.
