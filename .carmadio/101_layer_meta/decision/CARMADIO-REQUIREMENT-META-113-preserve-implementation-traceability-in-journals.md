---
artifact_type: requirement
artifact_id: CARMADIO-REQUIREMENT-META-113
scope_path: layer:meta
subject_scope: lifecycle-traceability
priority: high
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: child_of
    targets:
      - CARMADIO-REQUIREMENT-META-080
      - CARMADIO-REQUIREMENT-META-086
  - type: relates_to
    targets:
      - CARMADIO-REQUIREMENT-META-075
      - CARMADIO-REQUIREMENT-META-076
      - CARMADIO-REQUIREMENT-META-090
      - CARMADIO-REQUIREMENT-META-109
      - CARMADIO-REQUIREMENT-META-112
---

# Requirement — Preserve implementation traceability in Journals

Every structural scope that realizes normative Atoms maintains an append-only Implementation Journal. Its admitted records bind exact Requirement, Method, Assurance, and Delivery Atom revisions to the native implementation targets that declare their realization.

The Journal is canonical for the declared implementation relationship. Native source, configuration, executable assurance mechanisms, packages, and delivery automation remain canonical for the operative realization itself. Ops evidence and Verification remain the authorities for what occurred and whether the realization is sufficiently assured. Recording an implementation relationship never proves correctness or successful operation.

An implementation binding must survive ordinary Git history transformations such as squash merges, rebases, cherry-picks, and repository migration. The binding therefore identifies each source Atom by stable artifact identity plus revision digest and each native implementation target by a stable locator plus content digest. Git commits, pull requests, authors, sessions, and signatures remain useful provenance but are not the sole semantic identity of the binding.

Corrections, replacements, target removal, and changed implementation coverage append new records; accepted Journal records are never edited, reordered, or deleted. The effective implementation frontier is derived from the complete ordered record sequence.

Implementation-role Projections are regenerated from the Journal and its declared current source and target frontier. They may present implementation coverage, mappings, missing realization, and potentially stale bindings, but they remain rebuildable and non-authoritative over the Journal, normative Atoms, native implementation, or assurance conclusions.

## Primary claim

Each implementing scope preserves squash-resistant traceability from exact normative Atom revisions to native implementation targets in an append-only Implementation Journal and derives implementation Projections from that Journal.

## Rationale

Git remains mandatory repository provenance, but real delivery workflows may rewrite or consolidate its commit graph. A semantic implementation Journal preserves durable atom-to-code lineage across those transformations without duplicating the code or treating generated coverage views as authority.
