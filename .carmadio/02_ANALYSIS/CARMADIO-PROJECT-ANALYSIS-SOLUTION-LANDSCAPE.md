# Solution landscape — Make DSET self-hosting and skills thin

## Capability gaps

| Capability | Requirement/test/eval IDs | Hard constraints |
|---|---|---|
| Repository rule authority | `CARMADIO-REQUIREMENT-GOV-014`, `CARMADIO-REQUIREMENT-GOV-017`; `CARMADIO-TEST-CASE-GOV-014`, `CARMADIO-TEST-CASE-GOV-017`; `CARMADIO-EVALUATION-CASE-GOV-007` | Local paths, one editable owner per rule ID, no remote live authority |
| Thin adaptive wrappers | `CARMADIO-REQUIREMENT-SKILL-002`, `CARMADIO-REQUIREMENT-SKILL-003`; `CARMADIO-TEST-CASE-SKILL-002`, `CARMADIO-TEST-CASE-SKILL-003`; `CARMADIO-EVALUATION-CASE-SKILL-002`, `CARMADIO-EVALUATION-CASE-GOV-009` | Same wrapper hash, no embedded normative fallback |
| Bounded self-hosting | `CARMADIO-REQUIREMENT-OPS-003`, `CARMADIO-REQUIREMENT-TOOL-004`; `CARMADIO-TEST-CASE-OPS-003`, `CARMADIO-TEST-CASE-TOOL-005` | Terminates, profile-aware, framework before external pilot |
| Honest failure/customization | `CARMADIO-REQUIREMENT-GOV-015..016`; `CARMADIO-TEST-CASE-GOV-015..016`; `CARMADIO-EVALUATION-CASE-GOV-008..009` | Stable diagnostics, justified non-applicability, explicit custom identity |
| Separate proof | `CARMADIO-REQUIREMENT-META-007`; `CARMADIO-TEST-CASE-META-007`; all evals | Tests and evals remain different artifacts and evidence streams |
| Discoverable skill surface | `CARMADIO-REQUIREMENT-SKILL-004`, `CARMADIO-REQUIREMENT-SKILL-005`; `CARMADIO-TEST-CASE-SKILL-004`, `CARMADIO-TEST-CASE-SKILL-005`; `CARMADIO-EVALUATION-CASE-SKILL-003` | One catch-all entrypoint, explicit lifecycle shortcuts, no duplicated substantive rules |
| Investigable next-step routing | `CARMADIO-REQUIREMENT-SKILL-006`; `CARMADIO-TEST-CASE-SKILL-006`; `CARMADIO-EVALUATION-CASE-SKILL-005` | Bounded local evidence, redaction, no competing authority |
| Predictable pre-1.0 releases | `CARMADIO-REQUIREMENT-OPS-004`, `CARMADIO-REQUIREMENT-OPS-007`; `CARMADIO-TEST-CASE-OPS-004`, `CARMADIO-TEST-CASE-OPS-007`; `CARMADIO-EVALUATION-CASE-OPS-002` | Integer version tuple, one bump per main PR, coordinated product/package identity |
| Guarded RC/final publication | `CARMADIO-REQUIREMENT-OPS-005..006`; `CARMADIO-TEST-CASE-OPS-005..006`; `CARMADIO-EVALUATION-CASE-OPS-003` | PR-only main updates, fully working RC, evidence-gated 1.0 |
| Proportional delegation budget | `CARMADIO-REQUIREMENT-SKILL-007..008`; `CARMADIO-TEST-CASE-SKILL-007..008`; `CARMADIO-EVALUATION-CASE-SKILL-005..006` | Main model/effort inheritance, useful medium fan-out, outcome cost rather than nominal price |
| Session continuity | `CARMADIO-REQUIREMENT-SKILL-009`; `CARMADIO-TEST-CASE-SKILL-009`; `CARMADIO-EVALUATION-CASE-SKILL-008` | One public entrypoint, linked internal runs, bounded checkpoint recovery after compaction, and authoritative-state refresh |
| Unambiguous semantic routing | `CARMADIO-REQUIREMENT-GOV-018..019`; `CARMADIO-DECISION-GOV-034`; `CARMADIO-TEST-CASE-GOV-018..019`; `CARMADIO-EVALUATION-CASE-GOV-010..011` | Exactly four Types; one direct subtype at most; User Story is a Decision subtype; tasks and Changes remain non-Type structures; current and historical identities use one canonical verbose vocabulary without aliases |

## Candidates

Comparison frame: each row names its comparator and criteria. Fixed constraints
are repository-local authority, fail-closed resolution, bounded recursion,
separate tests/evals, protected delivery, and no automatic 1.0 promotion.
Evidence is `sufficient` only for the cited claim and recorded revision;
otherwise it is `degraded` or `insufficient`.

| Candidate/version | Source/license | Compared with / criteria | Evidence address/currentness | Evidence eligibility | Comparison result | Costs and observed failures |
|---|---|---|---|---|---|---|
| Normative rules embedded in each skill/current pattern | Repository/project license | Registry-owned rules / ownership and maintenance | `wrapper-rule-inventory-2026-07-14.md`; current for recorded skill sources | sufficient | Unfavorable: duplicates authority and increases drift | Duplicate maintenance; observed wrapper/rule drift risk |
| Remote framework documents as live authority/current public repo | Public repository/project license | Repository-owned rules / offline and customized operation | `030_dset-gov-specification-architecture.md`; current for the authority Contract | sufficient | Unfavorable: fails local ownership and offline use | Network/runtime dependency; local customization cannot own truth |
| Generated local copies with silent framework fallback/custom | Project license | Explicit local registry / precedence and reproducibility | `090_dset-skill-procedure-lifecycle-orchestration.md`; current for fail-closed resolution | sufficient | Not eligible under the fixed no-hidden-fallback constraint | Hidden precedence and non-reproducible choices |
| Registry-resolved local governing documents plus thin wrappers/current implementation | Repository/project license | Embedded/remote/fallback models / authority, offline use, customization | `local-gate-2026-07-15.md`; current locally; hosted proof is stale | degraded | Favorable locally for §§0–§4; hosted comparison remains pending | Registry/materialization maintenance; distribution remains open |
| One public skill per lifecycle mode/current target | Repository/project license | Five-skill topology / direct discoverability and trigger overlap | `040_dset-skill-specification-methodology.md`; selected by `CARMADIO-DECISION-SKILL-002`; expanded runtime proof pending | degraded | Selected for implementation; host-native usability remains to be evaluated | Larger discovery surface; exact registry and generated checks constrain drift |
| One universal skill with embedded lifecycle rules/custom | Repository/project license | Thin orchestrator / single-owner authority | `030_dset-gov-specification-architecture.md`; current for rule ownership | sufficient | Not eligible under the fixed repository-owned-rule constraint | One oversized competing rule store |
| Primary orchestrator plus four specialists/absorbed target | Repository/project license | One-skill and per-mode alternatives / discovery, ownership, stop boundaries | `CARMADIO-DECISION-SKILL-001-select-the-dset-0-3-operating-shape.md`; five wrappers implemented at the recorded commit | sufficient for historical source claim | Replaced for the public-topology claim by `CARMADIO-DECISION-SKILL-002` | Smaller discovery surface but indirect access to most modes |
| Decimal version arithmetic (`+0.1`/`+0.01`) | Informal convention/no imported code | Integer SemVer tuple / transition correctness | `080_dset-ops-procedure-release.md`, section “Classification and transitions”; current for specified edges | sufficient | Unfavorable: arithmetic can claim 1.0 without readiness | Low implementation cost; invalid `0.9 + 0.1` promotion |
| SemVer-compatible tuple with DSET normal/small classes/SemVer 2.0.0 | [SemVer 2.0.0](https://semver.org/), CC BY 3.0 reference | Decimal arithmetic / ecosystem mapping and RC ordering | `080_dset-ops-procedure-release.md`, section “Classification and transitions”; transition engine tested; coordinated writes and publication pending | degraded | Favorable for deterministic transitions; end-to-end release proof pending | Transition and mirror-validation cost |
| Always lowest token-price model/generic heuristic | No governed source | Same-model inheritance / completed-task cost | `070_dset-skill-procedure-delegation-budget.md`, section “Model-selection evidence”; no task-relevant DSET comparator | insufficient | Evidence-needed; nominal price alone is not comparable completed-task cost | Retry/token expansion can cost more and fail more often |
| Same model/effort by default; vary useful fan-out and evidence/current policy | DSET policy; [DeepSWE v1.1](https://deepswe.datacurve.ai/), observed 2026-07-15 | Price-only downgrade / outcome quality and completed-task cost | `070_dset-skill-procedure-delegation-budget.md`, section “Model-selection evidence”; benchmark supports only the token-price limitation | degraded | Provisionally favorable; DSET fan-out comparison remains pending | Inheritance may use expensive models; avoids unsupported downgrade risk |

## Decision

The original operating shape is recorded in `CARMADIO-DECISION-SKILL-001`. Its
exact-five topology claim is partially replaced by `CARMADIO-DECISION-SKILL-002`;
its other
claims remain active. Candidate rows above contain comparison results only;
they do not authorize adoption, implementation, release, or rejection.
