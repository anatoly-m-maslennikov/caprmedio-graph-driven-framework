---
artifact_type: requirement
artifact_id: CARMADIO-REQUIREMENT-META-024
scope_path: layer:meta
subject_scopes:
  - topology
priority: high
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: relates_to
    targets:
      - CARMADIO-REQUIREMENT-META-023
---

# Requirement — Define layer handoffs

Each adjacent boundary owns a handoff:

| Boundary | Accepted input | Produced output |
|---|---|---|
| META → GOV | Semantic invariants and layer constitution | Governable carriers and policies |
| GOV → TOOL | Governed executable obligations | Callable enforcement and diagnostics |
| TOOL → SKILL | Stable capabilities and diagnostic contracts | Thin orchestration and entry gates |
| SKILL → IMPL | Accepted work context and satisfied workflow gates | Governed implementation work |
| IMPL → OPS | Verified and supportable implementation | Deliverable, releasable, and operable output |

Every handoff declares entry criteria, exit criteria, and blocker behavior.
Adjacent handoffs are preferred. A direct forward skip is allowed only when the
intermediate layers have no meaningful transformation or ownership to add.
CARMADIO must not create placeholder artifacts merely to simulate an unnecessary
handoff.

## Primary claim

Every adjacent CARMADIO layer boundary declares the accepted input, produced output, entry criteria, exit criteria, and failure behavior of its handoff.

## Rationale

Explicit handoffs prevent layers from sharing vague ownership or silently importing implementation details across boundaries.


## Historical frontmatter metadata

```yaml
promotion:
  affected_children:
    - "governance"
    - "tool"
    - "skill"
    - "implementation"
    - "operations"
  applies_unchanged: true
  local_context_required: false
```
