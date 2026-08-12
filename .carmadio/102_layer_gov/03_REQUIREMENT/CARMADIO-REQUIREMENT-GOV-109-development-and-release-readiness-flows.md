---
artifact_type: requirement
artifact_id: CARMADIO-REQUIREMENT-GOV-109
scope_path: layer:gov
subject_scopes:
  - interaction
priority: high
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CARMADIO-REQUIREMENT-GOV-066
  - type: child_of
    targets:
      - CARMADIO-REQUIREMENT-META-090
      - CARMADIO-REQUIREMENT-META-093
      - CARMADIO-REQUIREMENT-META-107
---

# Requirement — Separate development and release-readiness flows

Development is the default flow:

```text
active atomic authority
→ QA Cases
→ Implementation, including executable Tests and Evaluations
→ factual Ops records
→ development Verification
```

Development consumes active atomic authority plus any enabled current
Projections. It does not require every enabled Projection to refresh after
every new Atom unless that Projection's own gate requires currentness.

Release readiness is mandatory before a Version can be declared ready:

```text
all active atomic authority
→ optional atomic refactoring when overlap warrants it
→ refresh every required Projection
→ detect conflicts
→ resolve conflicts through new atomic authority
→ repeat to a fixed point
→ reconcile implementation and assurance
→ execute Tests and Evaluations at the exact candidate head
→ fresh Ops records and Verification
→ accepted readiness Verification Record
```

Conflict resolution never edits an accepted atom. Any applicable code,
configuration, Test, Evaluation, or Projection change after an assurance
run makes the affected release evidence stale.

`.carmadio/carmadio_settings.toml` records `development` as the default workflow mode
and `release_readiness` as the mandatory pre-release mode.

## Primary claim

Development may proceed atomic-first, while release readiness must reconcile
all active authority, required Projections, Implementation, and fresh
assurance to one exact-head fixed point.

## Rationale

The successor removes retired compilation and Evergreen terminology while
preserving the different currentness needs of ordinary development and
release.
