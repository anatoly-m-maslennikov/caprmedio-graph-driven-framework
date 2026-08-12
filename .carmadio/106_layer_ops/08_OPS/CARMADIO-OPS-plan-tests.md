# Methodology OPS deterministic test case

This fragment owns exact deterministic proof for its listed IDs. Shared package behavior is connected by stable IDs, not duplicated plans.

| Test ID | Requirement or invariant | Assertion | Current automation |
|---|---|---|---|
| **CARMADIO-TEST-CASE-OPS-001** | CARMADIO-REQUIREMENT-OPS-001, CARMADIO-INVARIANT-OPS-001 | Validate representative supportability contracts for required evidence fields, correlation propagation, deploy/change identity, diagnostic permissions, redaction/access/retention/deletion behavior, volume/cardinality/sampling bounds, and resolvable runbook/incident links | Canonical validator pending; current scenario fixtures and review are manual |
| **CARMADIO-TEST-CASE-OPS-002** | CARMADIO-REQUIREMENT-OPS-002 | Parse the delivery workflow and runbook; prove stable policy/DSET check names and required authority/recovery fields | `python -m dset_toolchain check .` plus workflow assertions in CI |
| **CARMADIO-TEST-CASE-OPS-003** | CARMADIO-REQUIREMENT-OPS-003, CARMADIO-INVARIANT-OPS-002 | Require selected framework profiles to pass and materialize a complete temporary adopter before an external pilot | `python -m unittest tests.test_self_host tests.test_governance` |
| **CARMADIO-TEST-CASE-OPS-004** | CARMADIO-REQUIREMENT-OPS-004, CARMADIO-INVARIANT-OPS-003 | Exercise every allowed bootstrap/pre-1.0/RC/final/post-1.0 transition and reject ambiguous class, wrong arithmetic, invalid RC rollback, missing/multiple class, and automatic 1.0 promotion | Release-policy fixture matrix |
| **CARMADIO-TEST-CASE-OPS-005** | CARMADIO-REQUIREMENT-OPS-005, CARMADIO-INVARIANT-OPS-004 | Validate project delivery configuration and one release declaration; prove idempotent preparation, exact-merge publication, already-correct retry, partial recovery, collision stop, immutable tag, and no protected-branch content mutation | Release manifest/CI fixtures and hosted workflow assertion |
| **CARMADIO-TEST-CASE-OPS-006** | CARMADIO-REQUIREMENT-OPS-006, CARMADIO-INVARIANT-OPS-005 | Reject RC/final transitions whose exact-SHA readiness artifact has incomplete scope, failed/applicability proof, missing pilot/distribution evidence, blockers, or a substantive final-promotion diff | Release-readiness fixture matrix |
| **CARMADIO-TEST-CASE-OPS-007** | CARMADIO-REQUIREMENT-OPS-007, CARMADIO-INVARIANT-OPS-006 | Require canonical product identity and exact SemVer-to-PEP-440 RC equivalence while accepting independent schema/profile/template compatibility versions | Version-surface consistency fixtures |
| **Historical CARMADIO-TEST-CASE-OPS-016** | CARMADIO-DECISION-OPS-006 | Delivery-name release-role proof is superseded by cross-layer `CARMADIO-TEST-CASE-GOV-044` | Historical release-role fixtures |
| **CARMADIO-TEST-CASE-OPS-017** | CARMADIO-DECISION-OPS-008, CARMADIO-CONTRACT-TOOL-001 | Require representative source, governance, migration, and generated paths to resolve to the repository-owned LF worktree policy | `python -m unittest tests.test_cross_platform_contract` plus hosted platform matrix |
| **CARMADIO-TEST-CASE-OPS-018** | CARMADIO-DECISION-OPS-009, CARMADIO-CONTRACT-TOOL-001 | Require case-sensitive POSIX relative-path text to own project-health source traversal instead of host-native Path ordering | `python -m unittest tests.test_health` plus hosted platform matrix |
| **CARMADIO-TEST-CASE-OPS-019** | CARMADIO-DECISION-OPS-010, CARMADIO-CONTRACT-TOOL-001 | Require a Windows Python path with backslashes and spaces to remain one exact subprocess argument after verification-template expansion | `python -m unittest tests.test_verification` plus hosted platform matrix |
| **CARMADIO-TEST-CASE-OPS-020** | CARMADIO-DECISION-OPS-011, CARMADIO-CONTRACT-TOOL-001 | Require aliased repository paths to compare by resolved identity and Windows relative Path values to serialize as canonical POSIX repository text | Layout, archive, evidence, and hosted platform regressions |
| **CARMADIO-TEST-CASE-OPS-021** | CARMADIO-DECISION-OPS-012, CARMADIO-CONTRACT-TOOL-001 | Require temporary Git repositories and byte-sensitive fixtures to preserve exact worktree/blob identity independent of Windows newline defaults | Carrier-transition, semantic-atom, migration, bootstrap, artifact-type, and hosted platform regressions |

## Regression policy

Every accepted defect adds a deterministic regression test in its owning layer before the repair is archived.
