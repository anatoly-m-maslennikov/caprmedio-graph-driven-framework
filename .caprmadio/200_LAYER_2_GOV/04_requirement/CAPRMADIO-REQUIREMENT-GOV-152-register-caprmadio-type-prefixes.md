---
subject_scopes:
  - artifact-catalog
version: 2
updated_at: 2026-08-17 20:02:25
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMADIO-REQUIREMENT-GOV-144-register-current-type-prefixes
  child_of:
    - CAPRMADIO-REQUIREMENT-GOV-181
---
# Register CAPRMADIO Type prefixes

Every registered artifact Type must have one globally unique four-character uppercase identity prefix from which the resolver derives the full Type without duplicated embedded Type metadata.

| Type | Prefix |
|---|---|
| `goal` | `GOAL` |
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
| `external_method` | `XMTH` |
| `method_binding` | `MBND` |
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

`change_plan` and `refactoring_plan` use their parent Plan Type's `PLAN` prefix and numbering sequence. `implementation_decision` uses its parent Method Type's `METH` prefix and numbering sequence. The retired internal Implementation Atom Type does not receive an active `IMPL` prefix; historical identities retain their recorded meaning until a separately governed identity migration rewrites them.

The canonical filename grammar remains:

```text
<PROJECT>-<SCOPE_PATH>-<TYPE_PREFIX>-<NNN>[-<SUBTYPE>]--<SUMMARY>.<ext>
```

Changing a registered prefix requires one governed lossless identity migration across active and archived carriers, relations, Projections, implementations, assurance records, and Git-bound provenance.
