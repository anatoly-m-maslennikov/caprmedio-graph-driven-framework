---
atom_id: CA-R-1623
ref_id: CA-R-1623
role: Requirement
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
author: Anatoly Maslennikov
status: Active
topics:
  main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control
  dependencies:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Execution
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal
version: 10
updated_at: 2026-10-27 19:59:59 +0400
relations:
  child_of:
  - CA-R-1622
form: Rule
tier: 4
container:
  scope_unit: CA-SU-16
carrier_destination:
  file:
    name: CA-R-1623-TOOLS-RULE--keep-atom-validation-execution-bounded-and-read-only.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-16_FEATURE_TOOLS/04_requirement
---
# Summary

Keep Atom validation execution bounded and read-only

## Scope

`VALIDATE_ATOMS` Implementation invocations within their admitted input context.

## Claim

the `VALIDATE_ATOMS` Implementation **must** keep **every** invocation read-only **and** bounded by its admitted input context.

- admit bounded inventory enumeration **and** the minimum candidate content needed **to** determine selection inside declared source roots **and** allowed read roots. inspect an excluded candidate **only** for selection; exclusion does **not** admit its full validation **or** add it **to** target coverage.
- read selected targets, applicable authority, **and** necessary reference inputs **only** inside admitted read boundaries. reference resolution does **not** expand the target set.
- enforce actual read permissions **and** protected-file exclusions **before** reading content. caller-supplied roots grant no permission; do **not** follow a link outside admitted boundaries, fetch remote resources, inspect secrets, **or** execute YAML tags, Markdown, selectors, rule bundles, **or** Atom instructions as code.
- enforce selected resource limits; exhaustion **must** yield incomplete **or** error, **not** a pass. isolate a malformed candidate so independently checkable candidates remain reportable.
- do **not** write, rename, remove, **or** repair source files, Projections, Settings, caches, **or** Journal files. the caller/executor owns any admitted persistence of returned Run evidence.
- preserve exact invocation definition/input bindings; report a changed source rather than silently validating mixed Revisions.

## Details
