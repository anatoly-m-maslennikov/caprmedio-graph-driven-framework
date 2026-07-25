---
artifact_type: requirement
artifact_id: DSET-REQUIREMENT-IMPL-010
scope_path: layer:implementation/scope:tools
subject_scopes:
  - migrations
priority: medium
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: child_of
    targets:
      - DSET-REQUIREMENT-IMPL-001
  - type: relates_to
    targets:
      - DSET-REQUIREMENT-IMPL-002
      - DSET-REQUIREMENT-IMPL-003
      - DSET-REQUIREMENT-IMPL-004
      - DSET-IMPL-GOV-001
---

# Requirement — Keep reusable migration tools

## Primary claim

Reusable migration executables belong to the IMPL `tools` scope under
`15_layer_implementation/tools/migrations`. The active toolkit contains only
portable, repeatable migrations and shared safety mechanisms; completed
schema-specific rewrites remain inert historical sources.

Every active migration:

- discovers or accepts its repository root instead of embedding a machine path;
- performs a mutation-free deterministic preview by default;
- requires explicit `--apply` before changing files;
- refuses unknown structures, path escape, symlink escape, collisions, and
  changed preimages;
- reports a stable plan digest that can bind preview to application;
- validates staged results before replacement and restores touched bytes after
  failure;
- verifies postconditions and produces no operations after successful
  reapplication; and
- uses portable Python filesystem and subprocess behavior across macOS,
  Windows, WSL, and Linux.

Executable entry points remain thin. Shared planning, digest, path-safety,
transaction, rollback, and verification behavior lives in reusable modules.
Migration-specific classification and rewriting remain bounded recipes.

Temporary transaction state belongs to `.dset_runtime`; optional redacted
append-only execution logs belong to `.dset_logs`. Neither location becomes
project authority.

## Rationale

One-off scripts are valuable during a cutover but unsafe as an implied public
toolkit. Extracting their proven safety mechanisms into a small migration
runtime preserves the useful work without promoting retired identities,
schemas, or repository layouts.
