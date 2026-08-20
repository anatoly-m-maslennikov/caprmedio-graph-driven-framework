---
subject_scopes:
  - provenance
tier: standard
version: 7
updated_at: 2026-08-20 22:58:24
relations:
  method_for:
    - CA-R-803-REQUIREMENT-FR_ENGN_TOOLS--emit-only-operational-hook-triggers
    - CA-R-804-REQUIREMENT-FR_ENGN_TOOLS--gather-complete-commit-action-context
    - CA-R-805-REQUIREMENT-FR_ENGN_TOOLS--commit-one-governed-file-action
    - CA-R-812-REQUIREMENT-FR_ENGN_TOOLS--append-governed-file-change-journal-records
---
# Process one file change

Use this flow for one governed repository file identity:

1. A registered adapter establishes one logical repository-file change from its substrate event. `COMMIT_TRIGGER` coalesces repeated observations with the same adapter and source-event identities into one stable trigger containing repository identity, observed before-path and after-path candidates, observation time, and the structured LLM-session candidate resolved from explicit invocation context or the adapter's host interface.
2. Run the shared `COMMIT_CONTEXT` gathering logic, either through its standalone Finder interface or internally through the orchestrated flow. Resolve one file identity. Treat creation as `ADD` and disappearance as `REMOVE`. Otherwise derive `moved` from a Structural-location change and `updated` from content, filename, or other governed carrier-state change. Map `moved=false, updated=true` to `UPDATE`, `moved=true, updated=false` to `MOVE`, and `moved=true, updated=true` to `MOVE+UPDATE`; reject `false, false` as no change.
3. Read upstream relations from the resulting staged graph for `ADD`, `UPDATE`, and `MOVE+UPDATE`, from the unchanged Artifact graph for `MOVE`, and from the last committed graph for `REMOVE`. Resolve authored directions and derived inverses only through the canonical relation-kind registry.
4. Resolve the explicit author or default it to the current operator's full GitHub username. Validate the LLM application name and host session UUID through the registered application adapter, with an explicit validated value taking precedence, and fail closed rather than guess. Resolve one `occurred_at` and calendar date in the configured Artifact timestamp timezone. Seal structured `llm_session`, `occurred_at`, and those other values with the adapter and source-event provenance, identity, change set, paths, versions, digests, Git base, ordered typed `sources`, singular resulting `result`, stable event and action identities, `previous_result_event` when one exists, and validation results as `COMMIT_CONTEXT`. If a non-`ADD` subject has no accepted prior result event, seal a `recovered` baseline candidate only from sufficient governed evidence.
5. Run the complete flow in dry-run mode to return the sealed context, complete predicted Journal sidecar record set and partitions, repository lease availability, and Git message projected from the structured change event without mutation. Show `<app>:<uuid>:<occurred_at>` only as a derived presentation; do not write session provenance into an Atom or Projection.
6. Doer 1, `APPEND_CHANGE_RECORDS`, acquires the repository-scoped apply lease, repeats every stale-context, frontier, identity, relation, version, recovery-evidence, index, and Git-base preflight, appends and fsyncs the complete ordered idempotent sidecar record set, and returns its ordered receipt set with the live lease token. Its internal Journal and runtime-state writes do not emit another Hook trigger.
7. Doer 2, `COMMIT_CHANGE_SET`, validates the complete receipt set and live lease, repeats the mutation-boundary checks, stages exactly the one governed subject change plus all and only its receipt-bound Journal lines, creates one commit from the deterministic message Projection, verifies the commit tree, every related record, message, and parent Git base, and then releases the lease.
8. Return the common Tool result envelope with the Journal receipt set, lease disposition, and commit identifier on apply or their predicted values on dry-run. After a partial append or post-append commit failure, retain one observable blocked action and reuse the same event identities, `llm_session`, `occurred_at`, and existing receipts on retry rather than duplicate or redefine a record. A different action waits until the blocked action succeeds or an operator explicitly resolves it.
