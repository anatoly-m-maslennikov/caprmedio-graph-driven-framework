# Test plan — Add artifact governance profiles

Deterministic tests prove exact behavior. Probabilistic or qualitative proof belongs in [eval-plan.md](eval-plan.md).

| Test ID | Requirement | Deterministic proof |
|---|---|---|
| **CARMADIO-TEST-CASE-GOV-007** | CARMADIO-REQUIREMENT-GOV-004 | Project and schema accept separate implementation-language and artifact-profile fields; neither field substitutes for the other |
| **CARMADIO-TEST-CASE-TOOL-006** | `CARMADIO-REQUIREMENT-GOV-005`, `CARMADIO-REQUIREMENT-TOOL-005` | The artifact registry accepts unique valid areas with existing hubs and rejects missing hubs, duplicate roots, missing parents, and parent cycles with stable diagnostics |
| **CARMADIO-TEST-CASE-GOV-008** | `CARMADIO-REQUIREMENT-GOV-005`, `CARMADIO-REQUIREMENT-GOV-006` | Root README links every registered top-level area hub and each hub contains the required purpose, boundaries, and navigation sections |
| **CARMADIO-TEST-CASE-META-003** | `CARMADIO-REQUIREMENT-META-003`, `CARMADIO-REQUIREMENT-META-004` | The released documentation-v1 profile declares the artifact-type catalog and universal plus specification-specific authoring rules |
| **CARMADIO-TEST-CASE-TOOL-007** | CARMADIO-REQUIREMENT-TOOL-005 | JSON schemas parse; valid/invalid artifact-registry fixtures produce their expected results; `dset check` remains read-only |
| **CARMADIO-TEST-CASE-TOOL-008** | All | `dset verify`, Markdown link/portability validation, Ruff, strict mypy, unit tests, trace freshness, and `git diff --check` pass |

## Regression rule

Every validator defect adds a failing unit case or fixture before correction. Do not convert qualitative prose judgments into deterministic checks without a stable structural signal.
