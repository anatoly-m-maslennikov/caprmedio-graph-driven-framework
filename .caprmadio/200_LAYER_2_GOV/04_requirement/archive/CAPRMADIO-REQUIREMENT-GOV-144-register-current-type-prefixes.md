---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-GOV-144
scope_path: layer:gov
subject_scopes:
  - artifact-catalog
priority: high
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CAPRMADIO-REQUIREMENT-GOV-132
  - type: child_of
    targets:
      - CAPRMADIO-REQUIREMENT-GOV-138
      - CAPRMADIO-REQUIREMENT-GOV-142
  - type: relates_to
    targets:
      - CAPRMADIO-REQUIREMENT-GOV-133
---

# Requirement — Register current Type prefixes

Every registered artifact Type has one globally unique four-character uppercase
identity prefix. Frontmatter retains the full semantic `artifact_type`; the
prefix is an identity token rather than another Type name.

| Type | Prefix |
|---|---|
| `concern` | `CONC` |
| `external_problem` | `XPRB` |
| `conflict` | `CNFL` |
| `analysis` | `ANRP` |
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
| `delivery` | `DELV` |
| `implementation` | `IMPL` |
| `external_git_commit` | `XGCM` |
| `pull_request` | `PULL` |
| `ops` | `OPER` |
| `external_evidence_record` | `XEVR` |
| `verification_record` | `VERC` |
| `catalog` | `CATL` |
| `map` | `MAPS` |
| `hub` | `HUBS` |
| `development_backlog` | `BKLG` |
| `implementation_journal` | `IJRN` |

The canonical filename grammar is:

```text
<PROJECT>-<SCOPE_PATH>-<TYPE_PREFIX>-<NNN>[-<SUBTYPE>]--<SUMMARY>.<ext>
```

The stable artifact ID ends at `<NNN>`. An optional direct subtype is readable
filename metadata and does not change the Type-level numbering sequence.
Project-prefix and Scope-path omission follow project settings and leave no
empty separators.

Changing a registered prefix requires one governed lossless identity migration
across active and archived carriers, relations, Projections, implementations,
assurance records, and Git-bound provenance. The current registry establishes
the target vocabulary but does not claim that the known legacy graph is already
migrated.

## Primary claim

GOV assigns one unique four-character prefix to every currently registered Atom
and Projection Type.

## Rationale

The predecessor omitted Delivery, Ops, and Development Backlog and retained the
rejected `ANAL` token. The current registry aligns compact identities with the
CAPRMADIO Type surface while keeping semantic Type names explicit in carriers.
