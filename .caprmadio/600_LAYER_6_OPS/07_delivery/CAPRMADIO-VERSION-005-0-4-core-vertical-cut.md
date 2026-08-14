+++
artifact_type = "version"
artifact_subtype = "roadmap"
artifact_id = "CAPRMADIO-VERSION-005"
version_scope_ref = "CAPRMADIO-VERSION-002"
published_baseline = "0.3.1"
status = "active"
llm_session_ids = ["codex:019f591f-04f6-70f2-8de7-828b7cccc69d"]
+++

# DSET 0.4 Roadmap — core vertical cut

## Route

Complete the semantic/governance runtime, then the views and review flow that
depend on it, then close distribution and hosted proof, and finally run fresh
release proof and archive reconciliation. The linked task owners remain
canonical; this Roadmap owns order and checkpoint conditions only.

## Milestones

| Milestone ID | Completion condition | Dependencies | Owner refs | Evidence when achieved | Status |
|---|---|---|---|---|---|
| M1-governed-model | Four semantic Types, artifact roles, immutable lifecycle, priority, and conflict routing execute consistently | Current registries and Decisions | `CAPRMADIO-TASK-GOV-049`, `CAPRMADIO-TASK-GOV-051`, `CAPRMADIO-TASK-GOV-045`, `CAPRMADIO-TASK-TOOL-046` | Schema, fixture, traceability, and recursive self-application proof | complete |
| M2-visible-health | Project health and external review import/reconciliation use the executable model | M1 | `CAPRMADIO-TASK-TOOL-043`, `CAPRMADIO-TASK-GOV-044` | Generated health fixture matrix and cross-agent audit reconciliation proof | active |
| M3-portable-distribution | Declared hosts, platforms, and dependencies pass or applicability is honestly narrowed | M1 | `CAPRMADIO-TASK-SKILL-020`, `CAPRMADIO-TASK-TOOL-036..037` | Host receipts, platform CI/WSL evidence, and dependency-policy proof | planned |
| M4-hosted-release | The actual candidate has current GitHub and publisher evidence | M2, M3 | `CAPRMADIO-TASK-OPS-025` | Exact-head checks, protected-target state, publication retry/collision proof | planned |
| M5-release-proof | All 0.4 gates run fresh and the Change reconciles and archives | M1..M4 | `CAPRMADIO-TASK-META-010`, `CAPRMADIO-TASK-TOOL-008..009` | Tests, independent Evaluations, Verification, Readiness Record, and archive proof | planned |

## Risks and replanning triggers

- Hosted authentication or runner gaps may require an explicit narrower
  applicability Decision; silence never counts as proof.
- A semantic migration that cannot preserve immutable legacy atoms reopens the
  governing lifecycle Decision before implementation continues.
- Any change to the `0.4` promise recompiles
  `CAPRMADIO-VERSION-002` first, then this Roadmap.
