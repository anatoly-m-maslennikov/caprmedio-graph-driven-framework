---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-GOV-128
scope_path: layer:gov
subject_scopes:
  - lifecycle
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: child_of
    targets:
      - CAPRMADIO-REQUIREMENT-META-080
  - type: relates_to
    targets:
      - CAPRMADIO-REQUIREMENT-META-103
      - CAPRMADIO-REQUIREMENT-META-077
      - CAPRMADIO-REQUIREMENT-GOV-127
---

# Requirement — Classify every Atomic Artifact change

Before changing an admitted Atomic Artifact, CAPRMADIO assigns exactly one change
class:

| Change class | Boundary | Identity result | Required review |
|---|---|---|---|
| `carrier_only` | Representation, summary, filename, path, or encoding changes without changing governed meaning | Keep the artifact ID | Verify lossless recoding |
| `refinement` | Wording or criteria become clearer or stricter while primary claim, applicability, and acceptance meaning remain equivalent | Keep the artifact ID and commit a new revision | Demonstrate equivalence and assess lineage |
| `semantic_revision` | Meaning or applicability changes while the same primary claim remains recognizable | Keep the artifact ID and commit a new revision | Declare the delta and complete lineage-impact review |
| `replacement` | The primary claim changes identity, or an independently replaceable claim is added or removed | Create a new artifact ID and typed replacement relation | Review the replacement boundary and affected lineage |

Scope narrowing or expansion is a `semantic_revision`, not a carrier-only
change. Splitting or combining independently replaceable claims is a
`replacement`.

A same-ID revision names its previous committed revision as a parent and lists
the artifact ID as an updated child. A replacement names the applicable parent
revision, lists the successor as a new child, and archives the predecessor only
after the successor is committed.

Tools may propose a class but must fail closed when the distinction between
refinement, semantic revision, and replacement is uncertain.

## Primary claim

Every admitted Atomic Artifact change has one explicit class that determines
whether identity continues and which impact review applies.

## Rationale

The four classes preserve stable identities for genuine claim evolution while
preventing formatting changes, refinements, semantic changes, and replacements
from being treated as interchangeable.
