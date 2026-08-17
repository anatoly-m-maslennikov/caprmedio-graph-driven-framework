---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-GOV-109
scope_path: layer:gov
subject_scopes:
  - interaction
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMADIO-REQUIREMENT-GOV-066
  child_of:
    - CAPRMADIO-REQUIREMENT-META-093
    - CAPRMADIO-REQUIREMENT-META-107
---
# Separate development and release-readiness flows

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

`.caprmadio/caprmadio_settings.toml` records `development` as the default workflow mode
and `release_readiness` as the mandatory pre-release mode.

## Rationale

The successor removes retired compilation and Evergreen terminology while
preserving the different currentness needs of ordinary development and
release.
