---
artifact_type: requirement
artifact_id: DSET-REQUIREMENT-META-071
scope_path: layer:meta
subject_scopes:
  - atomic-scope
priority: high
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: child_of
    targets:
      - DSET-REQUIREMENT-META-052
  - type: relates_to
    targets:
      - DSET-REQUIREMENT-META-038
---

# Requirement — Give every Atomic Artifact explicit scope

Every Atomic Artifact declares exactly one `scope_path` identifying its
project-relative structural owner.

An Atomic Artifact may also declare `subject_scopes` identifying the semantic
subjects needed to find, compare, and review related atoms within that
structural owner. Each subject scope is an unqualified layer-local token. Its
meaning and allowed vocabulary are selected by `scope_path`; a subject scope
never repeats the layer or other structural coordinates.

Scope narrows discovery but does not determine authority, obsolescence, or
relation closure. Those meanings remain governed by artifact type, lifecycle
placement, and explicit relations.

## Primary claim

Every Atomic Artifact has one structural owner and may carry governed
layer-local subject scopes without duplicating its structural path.

## Rationale

Structural ownership and semantic search answer different questions. Keeping
them separate makes obsolete-atom reviews narrow and efficient without
encoding structure twice or replacing explicit dependency relations.
