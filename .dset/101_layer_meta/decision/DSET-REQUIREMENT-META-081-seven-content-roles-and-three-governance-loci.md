---
artifact_type: requirement
artifact_id: DSET-REQUIREMENT-META-081
scope_path: layer:meta
subject_scopes:
  - artifact-model
priority: high
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - DSET-REQUIREMENT-META-069
  - type: relates_to
    targets:
      - DSET-REQUIREMENT-META-028
      - DSET-REQUIREMENT-META-048
      - DSET-REQUIREMENT-META-049
      - DSET-REQUIREMENT-META-051
      - DSET-REQUIREMENT-META-056
      - DSET-REQUIREMENT-META-080
---

# Requirement — Use seven Content roles and three Governance loci

DSET classifies the primary semantic contribution of every governed artifact through exactly seven `content_role` values:

1. `concern` identifies a matter requiring disposition, including a question, problem, risk, opportunity, or conflict.
2. `analysis` interprets concerns or observations and develops understanding without independently establishing the desired result.
3. `requirement` states what the governed subject must, may, or must not satisfy, including a desired result, obligation, boundary, invariant, or required state.
4. `method` selects or prescribes how accepted Requirements will be approached or realized.
5. `assurance` defines how a claim, realization, or real operating condition will be checked, including mechanism-neutral QA Cases and continuous production Assurance Controls.
6. `implementation` is a realized project change or executable/configured realization, including code, configuration, committed implementation state, and executable assurance machinery.
7. `observation` records what was observed, including evidence, measurements, test results, evaluation results, and verification outcomes.

Governance locus is an independent semantic axis with exactly three `governance_locus` values:

- `internal` for project-owned meaning;
- `external` for meaning imposed or owned outside the project; and
- `relation` for meaning that exists between explicit endpoints.

QA Cases and Assurance Controls have the Assurance role. Executable Test,
Evaluation, monitoring, alerting, and health-check mechanisms have the
Implementation role. Their results, production signals, and verification
records have the Observation role. Assurance may check authority but cannot
create, edit, or override it.

Artifact form is an independent structural axis. `scope_path` remains a structural ownership coordinate rather than a semantic role or locus.

## Primary claim

DSET uses Concern, Analysis, Requirement, Method, Assurance, Implementation, and Observation as its seven Content roles and internal, external, and relation as its three Governance loci.

## Rationale

Concern covers the full family of matters needing disposition, while
Requirement names the desired-result role directly instead of the overbroad
Definition label. Separating Assurance definitions, executable
Implementations, and resulting Observations preserves both bounded QA and
continuous production-assurance chains.
