---
subject_scopes:
  - principles
tier: core
version: 4
updated_at: 2026-08-20 20:03:45
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CA-M-001-PRINCIPLE-METHOD--mece_mutually-exclusive-collectively-exhaustive
    - CA-D-001-PRINCIPLE-DELIVERY--keep-implementations-replaceable-across-technologies
---
# Keep META and GOV implementation neutral

CAPRMEDIO META and GOV authority defines universal semantics, governance invariants, and extension boundaries without depending on a programming language, LLM provider or model, agent host, operating system, repository host, package manager, database, deployment platform, or other replaceable implementation mechanism.

Mechanism-specific obligations live in the earliest downstream scope that owns the mechanism, such as a Method, Evaluation, Delivery, Extension, Project Adaptation, tool, skill, or repository configuration. A downstream Extension or Project Adaptation may specialize META and GOV for its bounded use but cannot redefine their meaning or create a backward dependency.

META or GOV may name a mechanism only when the mechanism itself is the explicit Entity of Concern, such as a portability boundary or external constraint. The reference must not make that mechanism a hidden prerequisite of the universal kernel.
