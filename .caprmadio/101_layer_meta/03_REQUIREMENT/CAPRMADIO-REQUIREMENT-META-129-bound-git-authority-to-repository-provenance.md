---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-META-129
scope_path: layer:meta
subject_scope: lifecycle-traceability
tier: core
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CAPRMADIO-REQUIREMENT-META-076
  - type: child_of
    targets:
      - CAPRMADIO-REQUIREMENT-META-128
  - type: relates_to
    targets:
      - CAPRMADIO-REQUIREMENT-META-097
      - CAPRMADIO-REQUIREMENT-META-113
      - CAPRMADIO-REQUIREMENT-META-121
      - CAPRMADIO-REQUIREMENT-META-123
---

# Requirement — Bound Git authority to repository provenance

Every CAPRMADIO-governed project uses Git as the required history and provenance
engine for persisted repository state. The accepted Git graph is canonical for
the repository snapshots, changes, integrations, authorship, and release
boundaries that it records.

Git provenance does not by itself own semantic authority, Assurance, Ops
Evidence, or graph-independent relationships between exact artifact revisions
and their realizations. Governed Journals preserve those relationships when a
normal delivery workflow squashes, rebases, cherry-picks, or migrates Git
history. A generated index remains derived and replaceable.

Rewriting a Git graph is permitted only when required governed relationships
and released-state identities remain replayable through stable artifact and
target revisions plus their Journals. A rewritten commit identifier cannot be
the sole identity of a semantic dependency.

Git is the explicit version-control dependency of the CAPRMADIO framework, not a
hidden implementation choice. GOV defines concrete commit, integration,
archive, and Journal-binding conventions.

## Primary claim

Git is mandatory and canonical for persisted repository provenance, while
graph-independent semantic lineage is preserved by governed Journals rather
than by permanent reachability of every intermediate commit.

## Rationale

This boundary keeps Git as the project history engine without losing semantic
traceability in ordinary squash, rebase, cherry-pick, and migration workflows.
