---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-META-172
scope_path: layer:meta
subject_scopes:
  - scope-topology
tier: core
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMADIO-REQUIREMENT-META-065-ordered-realization-topology
    - CAPRMADIO-REQUIREMENT-META-143-use-flat-layer-owned-feature-scopes
---

# Share canonical Features across SPEC and IMPLEMENTATION

SPEC and IMPLEMENTATION use the same ordered Feature set so that each normative scope has one corresponding realization scope:

1. METHODOLOGY — structured operational cases and playbooks used by Skills and Assurance.
2. TOOLS — deterministic operations, command-line behavior, migrations, and generated controls.
3. SKILLS — thin agent-facing wrappers and gated Skill chaining.
4. PROFILES — reusable implementation practices selected for a project or component.
5. ADAPTERS — provider, platform, host-runtime, and external-system integrations.
6. ASSURANCE — Test Cases, Evaluation Cases, checks, evaluators, and assurance execution.
7. DOCUMENTATION — README and framework documentation, navigation, examples, portability, and freshness.

Templates, schemas, shared libraries, Tests, Evaluations, installation logic, and generated dashboards belong to their owning Feature rather than forming additional canonical Features.
