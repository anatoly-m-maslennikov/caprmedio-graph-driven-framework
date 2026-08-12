# Test plan — Add artifact governance profiles

Deterministic tests prove exact behavior. Probabilistic or qualitative proof belongs in [eval-plan.md](eval-plan.md).

| Test ID | Requirement | Deterministic proof |
|---|---|---|
| **CAPRMADIO-TEST-CASE-GOV-007** | CAPRMADIO-REQUIREMENT-GOV-004 | Project and schema accept separate implementation-language and artifact-profile fields; neither field substitutes for the other |
| **CAPRMADIO-TEST-CASE-TOOL-006** | `CAPRMADIO-REQUIREMENT-GOV-005`, `CAPRMADIO-REQUIREMENT-TOOL-005` | The artifact registry accepts unique valid areas with existing hubs and rejects missing hubs, duplicate roots, missing parents, and parent cycles with stable diagnostics |
| **CAPRMADIO-TEST-CASE-GOV-008** | `CAPRMADIO-REQUIREMENT-GOV-005`, `CAPRMADIO-REQUIREMENT-GOV-006` | Root README links every registered top-level area hub and each hub contains the required purpose, boundaries, and navigation sections |
| **CAPRMADIO-TEST-CASE-META-003** | `CAPRMADIO-REQUIREMENT-META-003`, `CAPRMADIO-REQUIREMENT-META-004` | The released documentation-v1 profile declares the artifact-type catalog and universal plus specification-specific authoring rules |
| **CAPRMADIO-TEST-CASE-TOOL-007** | CAPRMADIO-REQUIREMENT-TOOL-005 | JSON schemas parse; valid/invalid artifact-registry fixtures produce their expected results; `dset check` remains read-only |
| **CAPRMADIO-TEST-CASE-TOOL-008** | All | `dset verify`, Markdown link/portability validation, Ruff, strict mypy, unit tests, trace freshness, and `git diff --check` pass |

## Regression rule

Every validator defect adds a failing unit case or fixture before correction. Do not convert qualitative prose judgments into deterministic checks without a stable structural signal.
