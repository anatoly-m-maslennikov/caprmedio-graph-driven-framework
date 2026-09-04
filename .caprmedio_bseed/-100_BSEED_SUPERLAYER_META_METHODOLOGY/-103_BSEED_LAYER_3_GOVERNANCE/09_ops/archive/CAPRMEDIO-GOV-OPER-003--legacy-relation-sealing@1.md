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
  - type: relates_to
    targets:
      - CAPRMEDIO-SPEC-TOOLS-CONC-056--legacy-relation-sealing
      - CAPRMEDIO-GOV-OPER-002--typed-artifact-relations
---

# Test result — Legacy relation sealing boundary

**LLM session IDs:**

- `codex:019f591f-04f6-70f2-8de7-828b7cccc69d`

## Subject and intended use

Corrective implementation commit
`23fe405a9c705b323ffcf2fb8d82d7151c27cfb5` for
`CAPRMEDIO-GOV-METH-023--typed-artifact-relations`, resolved Problem `CAPRMEDIO-SPEC-TOOLS-CONC-056--legacy-relation-sealing`, and
deterministic Test `CAPRMEDIO-GOV-EVAL-024--typed-artifact-relations-test-case`.

This record replaces the current deterministic conclusion drawn from Evidence
Record 023 without editing that historical observation. It does not satisfy
qualitative Evaluation `CAPRMEDIO-GOV-EVAL-012--typed-artifact-relations-evaluation-case`, hosted CI, release
readiness, or publication.

## Observed result

The sealing command rejects every newly authored atom that contains top-level
legacy `child_of` metadata and directs authors to canonical `relations`.
Repository validation still reads all already sealed legacy atoms as
compatibility `child_of` edges, so the admission restriction does not rewrite
or invalidate immutable history.

The first complete run after the corrective commit failed only because the new
commit-derived `implementation_of` edge made generated health and traceability
stale. Their explicit refresh restored the repository fixed point. The second
complete sequential run passed.

## Commands and results

```text
python -m unittest discover -s tests -q
  239 tests passed

ruff check .
  passed

mypy
  passed with strict configuration

python -m dset_toolchain check .
  DSET validation passed

git diff --check
  passed
```

Focused relation, atom, compilation, traceability, health, and bootstrap gates
also passed before the implementation commit. The complete suite and DSET
validation were run sequentially because self-host fixtures temporarily create
adopter repositories near the workspace.

## Reopen conditions

Reopen this evidence when relation vocabulary or meaning, legacy relation
compatibility, atom admission, projection ranges, commit provenance, relation
validation, generated traceability/health, or either cited implementation
commit changes.
