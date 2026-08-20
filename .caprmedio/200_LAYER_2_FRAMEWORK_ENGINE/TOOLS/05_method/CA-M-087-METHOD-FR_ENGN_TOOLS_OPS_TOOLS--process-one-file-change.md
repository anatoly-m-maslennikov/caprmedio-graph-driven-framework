---
subject_scopes:
  - provenance
tier: standard
version: 1
updated_at: 2026-08-20 19:43:00
relations:
  method_for:
    - CA-R-803-REQUIREMENT-FR_ENGN_TOOLS_OPS_TOOLS--emit-only-operational-hook-triggers
    - CA-R-804-REQUIREMENT-FR_ENGN_TOOLS_OPS_TOOLS--gather-complete-commit-action-context
    - CA-R-805-REQUIREMENT-FR_ENGN_TOOLS_OPS_TOOLS--commit-one-governed-file-action
---
# Process one file change through Hook, Finder, and Doer

Use this flow for one governed repository file identity:

1. At a registered repository boundary, `COMMIT_TRIGGER` emits repository identity, event identity, and observed before-path and after-path candidates only.
2. Pass the trigger either to the optional `COMMIT_CONTEXT` Finder or directly to the `COMMIT_CHANGE_SET` Doer. Both paths invoke the same context-gathering implementation.
3. Resolve one file identity. Treat creation as `ADD` and disappearance as `REMOVE`. Otherwise derive `moved` from a Structural-location change and `updated` from content, filename, or other governed carrier-state change. Map `moved=false, updated=true` to `UPDATE`, `moved=true, updated=false` to `MOVE`, and `moved=true, updated=true` to `MOVE+UPDATE`; reject `false, false` as no change.
4. Read upstream relations from the resulting staged graph for `ADD`, `UPDATE`, and `MOVE+UPDATE`, from the unchanged Artifact graph for `MOVE`, and from the last committed graph for `REMOVE`. Resolve authored directions and derived inverses only through the canonical relation-kind registry.
5. Seal the resolved identity, change set, paths, versions, digests, Git base, relation frontier, canonical message, and validation results as `COMMIT_CONTEXT`. The standalone Finder returns this envelope without mutation.
6. Run the Doer in dry-run mode to return the sealed context and predicted result without changing Git. On explicit apply, reject stale or incomplete context and unrelated staged changes, stage only the resolved file change, create one canonical commit, and verify its tree, message, and parent Git base.
7. Return the common Tool result envelope with the commit identifier on apply or the predicted commit message on dry-run.
