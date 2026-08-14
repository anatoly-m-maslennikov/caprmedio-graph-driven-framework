---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-GOV-132
scope_path: layer:gov
subject_scopes:
  - artifact-catalog
priority: high
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CAPRMADIO-REQUIREMENT-GOV-119
  - type: child_of
    targets:
      - CAPRMADIO-REQUIREMENT-GOV-131
      - CAPRMADIO-REQUIREMENT-GOV-133
  - type: relates_to
    targets:
      - CAPRMADIO-REQUIREMENT-GOV-102
      - CAPRMADIO-REQUIREMENT-GOV-113
      - CAPRMADIO-REQUIREMENT-GOV-114
---

# Requirement — Register Atom and Projection Type prefixes

Every registered artifact Type has exactly one globally unique, immutable, four-character uppercase identity prefix. The artifact catalog owns the mapping. Frontmatter keeps the full semantic `artifact_type`; the short prefix is an identity token and never replaces the Type name.

The canonical filename grammar is:

```text
<PROJECT>-<SCOPE_PATH>-<TYPE_PREFIX>-<NNN>[-<SUBTYPE>]--<SUMMARY>.<ext>
```

Project-prefix and scope-path segments follow the project’s governed identity settings. Omitted optional segments do not leave empty separators. The stable artifact ID ends at `<NNN>`. A subtype segment is semantic filename metadata but is not part of the stable ID. The `--` token separates identity metadata from the human-readable summary.

Numbering is one monotonically increasing sequence per registered Type across all of its subtypes.

## Canonical prefix registry

| Type | Prefix |
|---|---|
| `concern` | `CONC` |
| `external_problem` | `XPRB` |
| `conflict` | `CNFL` |
| `analysis` | `ANAL` |
| `external_analysis_report` | `XARP` |
| `conflict_analysis` | `CFAN` |
| `requirement` | `REQU` |
| `constraint` | `CNST` |
| `contract` | `CNTR` |
| `method` | `METH` |
| `implementation_methodology` | `IMET` |
| `integration_decision` | `IDEC` |
| `assurance` | `ASSU` |
| `assurance_standard` | `AUST` |
| `review_protocol` | `RVPR` |
| `implementation` | `IMPL` |
| `external_git_commit` | `XGCM` |
| `pull_request` | `PULL` |
| `observation` | `OBSV` |
| `external_evidence_record` | `XEVR` |
| `verification_record` | `VERC` |
| `catalog` | `CATL` |
| `map` | `MAPS` |
| `hub` | `HUBS` |

Examples:

```text
CAPRMADIO-GOV-REQU-001--artifact-form-is-explicit.md
CAPRMADIO-GOV-ASSU-002-QA-CASE--projection-interpretability.md
CAPRMADIO-OPS-ASSU-003-ASSURANCE-CONTROL--queue-stall-detection.md
CAPRMADIO-TOOL-IMPL-001--resolve-project-local-governance.md
CAPRMADIO-META-CATL-001--requirement-atom-catalog.md
```

Changing a registered prefix requires one governed, complete identity migration across active and archived carriers, relations, Projections, implementations, and assurance records. The newly admitted registry establishes the target vocabulary; it does not silently rename existing carriers.

## Primary claim

GOV assigns one unique four-character identity prefix to every registered Atom and Projection Type.

## Rationale

The predecessor’s prefix registry encoded superseded internal Types and the retired Specification Type. The successor aligns identities with role-equals-Type internal Atoms and the Catalog, Map, and Hub Projection vocabulary while preserving compact deterministic filenames.
