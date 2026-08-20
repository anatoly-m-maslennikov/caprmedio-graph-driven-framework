---
subject_scopes:
  - provenance
tier: standard
version: 3
updated_at: 2026-08-20 20:16:00
relations:
  method_for:
    - CA-R-803-REQUIREMENT-FR_ENGN_TOOLS_OPS_TOOLS--emit-only-operational-hook-triggers
    - CA-R-804-REQUIREMENT-FR_ENGN_TOOLS_OPS_TOOLS--gather-complete-commit-action-context
    - CA-R-805-REQUIREMENT-FR_ENGN_TOOLS_OPS_TOOLS--commit-one-governed-file-action
    - CA-R-812-REQUIREMENT-FR_ENGN_TOOLS_OPS_TOOLS--append-governed-file-change-event
---
# Process one file change

Use this flow for one governed repository file identity:

1. A real registered repository-file change occurs. `COMMIT_TRIGGER` catches that boundary and emits repository identity, stable event identity, and observed before-path and after-path candidates only.
2. Run the shared `COMMIT_CONTEXT` gathering logic, either through its standalone Finder interface or internally through the orchestrated flow. Resolve one file identity. Treat creation as `ADD` and disappearance as `REMOVE`. Otherwise derive `moved` from a Structural-location change and `updated` from content, filename, or other governed carrier-state change. Map `moved=false, updated=true` to `UPDATE`, `moved=true, updated=false` to `MOVE`, and `moved=true, updated=true` to `MOVE+UPDATE`; reject `false, false` as no change.
3. Read upstream relations from the resulting staged graph for `ADD`, `UPDATE`, and `MOVE+UPDATE`, from the unchanged Artifact graph for `MOVE`, and from the last committed graph for `REMOVE`. Resolve authored directions and derived inverses only through the canonical relation-kind registry.
4. Resolve the explicit author or default it to the current operator's full GitHub username. Resolve occurrence time and calendar date in the configured Artifact timestamp timezone. Seal those values with the identity, change set, paths, versions, digests, Git base, relation frontier, canonical `action_message`, predicted Journal partition, stable event identity, and validation results as `COMMIT_CONTEXT`.
5. Run the complete flow in dry-run mode to return the sealed context, predicted Journal event and partition, and predicted commit without mutation. Before apply, repeat every stale-context, frontier, identity, relation, version, and index preflight check.
6. Doer 1, `APPEND_CHANGE_EVENT`, appends and fsyncs exactly one idempotent Work Journal event in the selected author-date-count partition and returns a receipt. Its internal Journal write does not emit another Hook trigger.
7. Doer 2, `COMMIT_CHANGE_SET`, validates that receipt, stages exactly the governed subject change plus the receipt-bound Journal record, creates one commit whose message is byte-identical to the Journal `action_message`, and verifies the commit tree, message, and parent Git base.
8. Return the common Tool result envelope with the Journal receipt and commit identifier on apply or their predicted values on dry-run. After a post-append commit failure, reuse the same event and receipt on retry rather than append a duplicate.
