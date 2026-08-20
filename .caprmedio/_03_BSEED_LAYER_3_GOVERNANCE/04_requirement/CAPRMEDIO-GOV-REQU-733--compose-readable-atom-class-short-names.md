---
subject_scopes:
  - carrier-format
version: 3
updated_at: 2026-08-20 18:36:57
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-REQU-036--expose-only-task-necessary-distinctions
    - CAPRMEDIO-GOV-REQU-345--represent-accepted-meaning-faithfully
---
# Compose readable Atom class short names

GOV derives each uppercase `SNAKE_CASE` typed-Atom class short name by splitting its canonical Type name into words, replacing every registered word with its canonical short form, preserving every unregistered word in full, and joining all resulting words with underscores.

| Canonical word | Short form |
|---|---|
| `external` | `EXT` |
| `implementation` | `IMPL` |
| `evaluation` | `EVAL` |
| `report` | `RPRT` |
| `control` | `CNTRL` |
| `record` | `REC` |

Every admitted typed-Atom class resolves to exactly one unique short name within its owning Content role; no fixed character width or unregistered ad hoc contraction is permitted. Canonical examples include `ANALYSIS_RPRT`, `EXT_ANALYSIS_RPRT`, `CONFLICT_ANALYSIS_RPRT`, `IMPL_DECISION`, `EVAL_CNTRL`, and `INCIDENT_REC`.
