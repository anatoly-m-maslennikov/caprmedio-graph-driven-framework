---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-GOV-130
scope_path: layer:gov
subject_scopes:
  - carrier-format
priority: high
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: child_of
    targets:
      - CAPRMADIO-REQUIREMENT-META-079
  - type: relates_to
    targets:
      - CAPRMADIO-REQUIREMENT-GOV-102
      - CAPRMADIO-REQUIREMENT-GOV-116
      - CAPRMADIO-REQUIREMENT-GOV-119
      - CAPRMADIO-REQUIREMENT-GOV-126
---

# Requirement — Govern maintained Specification carriers

`specification` is the internal, maintained, Definition-role artifact Type for
thin semantic views enabled by META. Its four-character identity prefix is
`SPEC`.

A Specification uses Markdown with YAML frontmatter and lives directly in its
owning structural scope rather than in an Atomic Artifact Type folder. Its
canonical filename is:

```text
<PROJECT>-<SCOPE_PATH>-SPEC-<NNN>--<SUMMARY>.md
```

The stable Specification identity ends at `<NNN>`. Numbering follows the
Type-owned sequence. Supported direct subtypes are `domain_model`, `behavior`,
`architecture`, `design`, and `governance`; subtype remains frontmatter
classification and is omitted from the default filename.

Frontmatter contains only applicable non-derived properties:

```yaml
---
artifact_type: specification
artifact_subtype: domain_model
artifact_id: CAPRMADIO-META-SPEC-001
scope_path: layer:meta
priority: high
---
```

The body names Atomic Artifact IDs directly at every represented semantic
claim. Exact source revisions are carried by the governed Git transaction that
creates or updates the Specification; paths and links to other maintained
views are navigation only.

Creation and every update require a Git commit. The Specification ID is listed
as a new or updated child as applicable. Git history owns its revisions, so
`commit_on_create` and `commit_on_update` are invariants rather than
operator-selectable settings.

A Specification is current when its latest committed revision represents every
applicable source revision required by its scope. A changed source makes it
subject to lineage-impact review. `compatible` preserves the current
Specification revision; any affected disposition blocks a gate requiring that
Specification until an updated revision is committed. No frontmatter status
duplicates this derived condition.

## Primary claim

Specification is a maintained Markdown Type with stable `SPEC` identity,
scope-root placement, direct atomic provenance, and Git-governed revisions.

## Rationale

A concrete carrier contract makes the newly enabled semantic view usable
without treating it as an atom, hiding source revisions in frontmatter, or
creating a second currentness authority.
