---
artifact_type: requirement
artifact_id: CARMADIO-REQUIREMENT-META-030
scope_path: layer:meta
subject_scopes:
  - topology
priority: high
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: relates_to
    targets:
      - CARMADIO-REQUIREMENT-META-024
      - CARMADIO-REQUIREMENT-META-025
---

# Requirement — Govern layer extensions

A candidate layer must declare:

- one responsibility not already owned by another layer;
- its predecessor and successor;
- accepted inputs and produced outputs;
- entry, exit, and failure behavior;
- its dependency direction; and
- why a feature, profile, Work Area, or ordinary scope cannot own the concern.

The candidate is admissible only when the resulting graph remains acyclic and
existing responsibilities remain non-overlapping. Otherwise, model it using
the appropriate horizontal or scoped structure rather than adding a layer.

## Primary claim

A proposed CARMADIO layer is admitted only when it has one non-overlapping responsibility, explicit predecessor and successor handoffs, and preserves the acyclic layer graph.

## Rationale

An explicit admission test keeps the layer model extensible without allowing every profile, feature, or organizational preference to become a new layer.


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
