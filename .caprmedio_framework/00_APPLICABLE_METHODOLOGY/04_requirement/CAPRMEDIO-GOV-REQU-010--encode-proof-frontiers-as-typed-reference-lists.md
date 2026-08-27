---
cce_version: cce_1
cce_form: obligation
subjects:
  declared:
    continuant:
      - provenance
tier: core
version: 3
updated_at: 2026-08-23 15:00:38
relations:
  child_of:
    - CAPRMEDIO-GOV-REQU-353--bind-proof-records-to-dependency-frontiers
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/04_requirement/CAPRMEDIO-GOV-REQU-010--encode-proof-frontiers-as-typed-reference-lists.md
---
# Encode proof frontiers as typed reference lists

CAPRMEDIO MUST encode a proof carrier's machine-readable dependency frontier as `proof_frontier_refs`, a YAML list whose entries use `atom:<atom-name>@<version>,<updated_at>` for exact Atom revisions or `<kind>:<repository-relative-locator>@sha256:<digest>` for `file`, `configuration`, `evaluator`, and `input` dependencies. An `environment` dependency uses `environment:<name>@sha256:<fingerprint>`. Prose `invalidation_conditions` make currentness `unknown` until a governed checker resolves them.
