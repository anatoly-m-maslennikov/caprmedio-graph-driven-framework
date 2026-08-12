---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-GOV-152
scope_path: layer:gov
subject_scope: artifact-catalog
priority: high
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CAPRMADIO-REQUIREMENT-GOV-144
  - type: child_of
    targets:
      - CAPRMADIO-REQUIREMENT-GOV-149
      - CAPRMADIO-REQUIREMENT-GOV-150
      - CAPRMADIO-REQUIREMENT-GOV-151
  - type: relates_to
    targets:
      - CAPRMADIO-REQUIREMENT-GOV-133
      - CAPRMADIO-REQUIREMENT-GOV-142
---

# Requirement — Register CAPRMADIO Type prefixes

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
| `plan` | `PLAN` |
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
| `implementation_record` | `IREC` |

`change_plan` is a direct subtype and uses its parent Plan Type's `PLAN` prefix
and numbering sequence. The retired internal Implementation Atom Type does not
receive an active `IMPL` prefix; historical identities retain their recorded
meaning until the governed identity migration rewrites them.

The canonical filename grammar remains:

```text
<PROJECT>-<SCOPE_PATH>-<TYPE_PREFIX>-<NNN>[-<SUBTYPE>]--<SUMMARY>.<ext>
```

Changing a registered prefix requires one governed lossless identity migration
across active and archived carriers, relations, Projections, implementations,
assurance records, and Git-bound provenance.

## Primary claim

GOV assigns `PLAN` to the Plan Type, `IREC` to Implementation Record, and one
unique four-character prefix to every other active registered Type.

## Rationale

The registry must reflect the CAPRMADIO Type surface without granting a second
prefix to a direct subtype or retaining a live prefix for an unadmitted Atom
route.
