---
artifact_type: requirement
artifact_id: CARMADIO-REQUIREMENT-GOV-112
scope_path: layer:gov
subject_scopes:
  - lifecycle
priority: high
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CARMADIO-REQUIREMENT-GOV-039
  - type: relates_to
    targets:
      - CARMADIO-REQUIREMENT-GOV-098
      - CARMADIO-REQUIREMENT-GOV-102
---

# Requirement — Gate atomic admission and promotion

`.carmadio/dset_settings.toml` selects `medium` or `high` through
`artifacts.creation_strictness`; the default is `medium`.

At medium strictness, CARMADIO requires accepted authority, one primary claim, one
enabled artifact type, owning scope, creation provenance, material relations,
priority, and sufficient precision to establish a stable artifact identity and
initial committed revision. Optional non-authoritative context may remain
explicitly unknown.

At high strictness, CARMADIO stops before emission while any material authority,
meaning, boundary, classification, scope, lineage, conflict, or assurance
question remains ambiguous. It asks focused questions until the atom meets the
same one-primary-claim identity standard.

Both levels assess one-step promotion eligibility. Promotion is proposed only
when the claim applies unchanged at the broader enabled scope and always
requires explicit operator acceptance.

Admission does not prohibit later same-ID revisions. Every later change passes
the atomic change-class gate; changing the primary claim identity requires a
replacement.

## Primary claim

Atomic admission uses medium or high project-selected strictness and always
checks, but never automatically performs, one-step scope promotion.

## Rationale

The successor preserves admission rigor and promotion advice while removing
obsolete carrier and lifecycle-event language.
