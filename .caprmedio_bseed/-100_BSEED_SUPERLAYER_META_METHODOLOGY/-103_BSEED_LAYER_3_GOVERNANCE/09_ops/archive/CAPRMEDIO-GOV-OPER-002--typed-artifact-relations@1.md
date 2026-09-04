---
artifact_subtype: test_result
priority: high
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: evidence_for
    targets:
      - CAPRMEDIO-GOV-EVAL-024--typed-artifact-relations-test-case
---

# Test result — typed artifact relations

**LLM session IDs:**

- `codex:019f591f-04f6-70f2-8de7-828b7cccc69d`

## Subject and intended use

Implementation commit `cbddc0ab00606aa79b47dc7deced66dca73a1f56` for
`CAPRMEDIO-GOV-METH-023--typed-artifact-relations` and deterministic Test `CAPRMEDIO-GOV-EVAL-024--typed-artifact-relations-test-case`.
This evidence supports the local executable relation contract only. It does
not satisfy qualitative Evaluation `CAPRMEDIO-GOV-EVAL-012--typed-artifact-relations-evaluation-case`, hosted CI,
release readiness, or publication.

## Observed result

The implementation accepts the ten canonical forward relation types, converts
sealed legacy `child_of` metadata to typed compatibility edges, derives
`implementation_of` edges from Git trailers, and emits no inverse fields.
It validates range-based projection frontiers by semantic Type, optional direct
subtype, layer, exact structural scope, and globally ordered atom carrier.

The DSET repository self-applies three current GOV frontiers through
`CAPRMEDIO-GOV-CATL-003--methodology-projection-set`: Decision authority through atom carrier 035,
deterministic Tests through 036, and qualitative Evaluations through 037.
Generated traceability schema 1.3 and project health expose the same typed
relation inventory.

## Commands and results

```text
python -m unittest discover -s tests -v
  238 tests passed

ruff check .
  passed

mypy
  passed with strict configuration

python -m dset_toolchain check .
  DSET validation passed

git diff --check
  passed
```

The full test suite and repository validation were run sequentially because
self-host fixtures temporarily materialize adopter repositories near the
workspace. Parallel execution can expose those transient directories to a
concurrent repository scan and is not valid proof of a repository defect.

## Reopen conditions

Reopen this evidence when relation vocabulary or meaning, projection selector
shape, lifecycle compatibility, commit provenance, relation validation,
traceability schema, health rendering, or the cited implementation changes.
