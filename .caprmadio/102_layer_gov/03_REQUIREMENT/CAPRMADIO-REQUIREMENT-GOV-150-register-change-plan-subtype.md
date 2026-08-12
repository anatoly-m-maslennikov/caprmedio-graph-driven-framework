---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-GOV-150
scope_path: layer:gov
subject_scope: artifact-catalog
priority: high
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CAPRMADIO-REQUIREMENT-GOV-148
  - type: child_of
    targets:
      - CAPRMADIO-REQUIREMENT-META-136
      - CAPRMADIO-REQUIREMENT-GOV-149
  - type: relates_to
    targets:
      - CAPRMADIO-REQUIREMENT-GOV-128
---

# Requirement — Register the Change Plan subtype

GOV registers `change_plan` as a direct subtype of the internal `plan` Atom
Type. Its canonical coordinate is:

```text
atom x plan x internal
```

The carrier declares `artifact_type: plan` and
`artifact_subtype: change_plan`. It identifies the governed artifacts and
native project targets to add, refine, replace, archive, or review; applicable
scope; ordering and dependencies; and explicit completion conditions.

A Change Plan lives in the applicable Plan role folder. Before admission it may
live under the role-local `drafts/` boundary and change freely. An admitted
revision is governed by normal Atom dependency, refinement, replacement, and
archive rules.

The optional-subtype setting may suppress the subtype token from filenames but
never from the carrier's registered semantic identity. The Type-level `PLAN`
prefix and Plan Type numbering sequence govern its identity.

## Primary claim

`change_plan` is the registered internal Plan Atom subtype for an accepted,
bounded, cross-artifact project change.

## Rationale

Direct subtype registration gives Change Plans a precise carrier contract while
preserving Plan as the single top-level internal Atom Type for the role.
