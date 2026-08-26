---
subject_scopes:
  - commit-automation
  - repository-reconciliation
version: 1
updated_at: 2026-08-22 02:30:28
relations: {}
---
# Reconcile one missed external project change

Given one Git-admitted project change made without any Codex Hook event, run the service's low-frequency reconciliation once. Verify it observes the current repository frontier, creates one governed action without invented Codex provenance, advances the normal commit pipeline once, and records that repository reconciliation—not Hook delivery—supplied the observation.

The case fails if the change remains invisible, is attributed to an unrelated session, bypasses the normal pipeline, or is processed again after the resulting frontier becomes current.

Candidate alignment: CA-E-001, CA-E-002, CA-M-002, CA-R-827, CA-R-861.

## Sources

- [Git documentation: git status porcelain format](https://git-scm.com/docs/git-status#_porcelain_format_version_2)
- [Codex hooks documentation](https://learn.chatgpt.com/docs/hooks)
