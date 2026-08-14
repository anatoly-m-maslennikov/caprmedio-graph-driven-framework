---
subject_scopes:
  - priority
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMADIO-REQUIREMENT-GOV-058-derive-effective-priority-during-comparison
    - CAPRMADIO-REQUIREMENT-GOV-059-configure-conflict-selection-mode
    - CAPRMADIO-REQUIREMENT-GOV-063-three-level-priority-vocabulary
---

# Effective priority conflict selection

Concern and Plan Atoms store exactly one `priority` value: `high`, `medium`, or
`low`. Every other Content role omits `priority`. `highest` is a virtual
comparison result and is never stored.

During direct comparison of two Concern or Plan Atoms:

1. start with each artifact's stored priority;
2. add one level when its scope is a strict ancestor of the competing scope;
3. add one level when its ordered layer precedes the competing layer; and
4. cap the result at virtual `highest`.

An unrelated or incomparable scope receives no scope increment.

`.caprmadio/caprmadio_settings.toml` exposes exactly two selection modes:

- `ask_always`, the default, explains the conflict and asks the operator; and
- `auto_by_effective_priority`, which may select only one uniquely eligible
  winner.

Ties, incomparable structure, uncertainty, or multiple winners always ask.
Mutually unsatisfiable external obligations stop for operator or external
resolution. RMAD tier precedence, deterministic replacement, explicit scoped
override, stale-view routing, and implementation drift follow their own
semantics rather than this selection mode.
