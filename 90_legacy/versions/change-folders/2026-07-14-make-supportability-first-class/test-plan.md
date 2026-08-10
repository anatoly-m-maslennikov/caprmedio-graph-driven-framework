# Test plan — Supportability contract

> Archive candidate in [PR #3](https://github.com/anatoly-m-maslennikov/dset-specs-loops-framework/pull/3).

## Deterministic checks

| Test ID | Requirement | Proof |
|---|---|---|
| **CARMADIO-TEST-CASE-META-002** | CARMADIO-REQUIREMENT-META-002 | Assert exact active display name, subtitle, expansion, project ID, and repository slug; reject stale active identity outside archived history |
| **CARMADIO-TEST-CASE-OPS-002** | CARMADIO-REQUIREMENT-OPS-002 | Assert spec, implementation-plan, code-rule, and gate documents expose the required supportability-contract fields |
| **CARMADIO-TEST-CASE-OPS-003** | CARMADIO-REQUIREMENT-OPS-003 | Assert the documented incident chain reaches version, PR, DSET change, requirement, test/eval, and repair evidence |
| **CARMADIO-TEST-CASE-OPS-004** | CARMADIO-REQUIREMENT-OPS-004 | Assert secret/PII redaction, retention/access, cardinality/sampling, volume/cost, and authority boundaries are explicit |
| **CARMADIO-TEST-CASE-OPS-005** | CARMADIO-REQUIREMENT-OPS-005 | Assert local-tool, service, and distributed-workflow examples choose different applicable mechanisms without a vendor mandate |
| **CARMADIO-TEST-CASE-OPS-006** | CARMADIO-REQUIREMENT-OPS-006 | Assert deterministic support checks remain in test plans and operator-usability judgments remain in eval plans |
| **CARMADIO-TEST-CASE-GOV-005** | All | Resolve Markdown links, parse YAML, balance fences/details, reject unsupported Markdown, and run `git diff --check` |

## Regression rule

Every supportability defect that is mechanically detectable must add a failing deterministic check. Incident evidence must be redacted before it is committed under `proofs/`.
