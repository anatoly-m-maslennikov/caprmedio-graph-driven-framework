---
subject_scopes:
  - feature-boundary
tier: core
version: 7
updated_at: 2026-08-21 06:34:42
relations:
  child_of:
    - CAPRMEDIO-FRAMEWORK-ENGINE-REQU-702--define-tools-feature-scope
---
# Define flat auto-commit Tool topology

`TOOLS` must own exactly four immediate peer `unordered_unit` Tool scopes for automatic commit after one governed project-path action. One action has exactly one file or folder subject and produces one Journal action and one Git commit:

| Scope | Full name and prefix | Tool kind | Structural address |
|---|---|---|---|
| `commit_trigger` | `COMMIT_TRIGGER` | Hook | `002_FRAMEWORK_ENGINE/TOOLS/COMMIT_TRIGGER` |
| `commit_context` | `COMMIT_CONTEXT` | Finder | `002_FRAMEWORK_ENGINE/TOOLS/COMMIT_CONTEXT` |
| `append_change_records` | `APPEND_CHANGE_RECORDS` | Doer | `002_FRAMEWORK_ENGINE/TOOLS/APPEND_CHANGE_RECORDS` |
| `commit_change_set` | `COMMIT_CHANGE_SET` | Doer and end-to-end flow orchestrator | `002_FRAMEWORK_ENGINE/TOOLS/COMMIT_CHANGE_SET` |

These Tools are peers at Structural level `3`; Hook, Finder, Doer, and orchestrator describe behavior rather than intermediate Structural groups. General authority shared by multiple Tools remains in `TOOLS`; authority specific to one Tool belongs to that Tool's scope. A host-level dispatcher or lifecycle callback is a replaceable adapter carrier of `COMMIT_TRIGGER`, not another Tool. No `OPS_TOOLS`, generic Journal Tool, dispatcher Tool, or other executable wrapper may be introduced into this flow.
