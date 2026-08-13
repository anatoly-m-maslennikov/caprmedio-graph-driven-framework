---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-META-127
scope_path: layer:meta
subject_scope: artifact-model
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CAPRMADIO-REQUIREMENT-META-125
  - type: child_of
    targets:
      - CAPRMADIO-REQUIREMENT-META-124
      - CAPRMADIO-REQUIREMENT-META-126
  - type: relates_to
    targets:
      - CAPRMADIO-REQUIREMENT-META-080
      - CAPRMADIO-REQUIREMENT-META-090
      - CAPRMADIO-REQUIREMENT-META-099
      - CAPRMADIO-REQUIREMENT-META-118
---

# Requirement — Provide the active META Atom Scope Catalog

CAPRMADIO provides one current, non-authoritative Catalog Projection that lists
every active META Atom exactly once under its canonical `subject_scope` and in
the Subject-scope order governed by META.

The Catalog is bound to an exact source frontier and distinguishes a current
result from a stale or incomplete result. Draft and archived Atoms are excluded
from the active view. A missing, multiple, unknown, or duplicate source
identity or Subject scope prevents the Catalog from claiming currentness.

The Catalog presents source Atom identities and human-readable labels without
paraphrasing their claims or establishing normative truth. Its carrier format,
serialization, source-digest algorithm, generation mechanism, storage path,
and replacement mechanics are governed downstream rather than by META.

## Primary claim

CAPRMADIO provides one source-bound, non-authoritative Catalog Projection that
groups every active META Atom exactly once by canonical Subject scope.

## Rationale

An implementation-neutral Catalog requirement preserves the helicopter view
while keeping source Atoms authoritative and leaving replaceable generation
mechanics outside META.
