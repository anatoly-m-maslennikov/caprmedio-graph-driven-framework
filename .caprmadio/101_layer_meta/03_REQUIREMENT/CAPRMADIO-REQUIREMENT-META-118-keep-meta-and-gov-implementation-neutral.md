---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-META-118
scope_path: layer:meta
subject_scope: principles
tier: core
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: relates_to
    targets:
      - CAPRMADIO-REQUIREMENT-META-030
      - CAPRMADIO-REQUIREMENT-META-057
      - CAPRMADIO-REQUIREMENT-META-095
      - CAPRMADIO-REQUIREMENT-META-112
---

# Requirement — Keep META and GOV implementation-neutral

CAPRMADIO META and GOV authority defines universal semantics, governance
invariants, and extension boundaries without depending on a programming
language, LLM provider or model, agent host, operating system, repository host,
package manager, database, deployment platform, or other replaceable
implementation mechanism.

Mechanism-specific obligations live in the earliest downstream scope that owns
the mechanism, such as a Method, Assurance, Delivery, implementation profile,
tool, skill, or repository configuration. A lower-level profile may specialize
META and GOV for its bounded use but cannot redefine their meaning or create a
backward dependency.

META or GOV may name a mechanism only when the mechanism itself is the explicit
Entity of Concern, such as a portability boundary or external constraint. The
reference must not make that mechanism a hidden prerequisite of the universal
kernel.

## Primary claim

CAPRMADIO META and GOV remain independent of replaceable implementation
mechanisms, which are governed only in their owning downstream scopes.

## Rationale

This adapts FPF's open kernel, layering, and notational-independence principles
to CAPRMADIO's provider-agnostic and cross-platform framework boundary.
