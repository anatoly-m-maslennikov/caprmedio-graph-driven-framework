---
subject_scopes:
  - requirement-topology
tier: core
version: 6
updated_at: 2026-08-20 02:38:43
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-REQU-031--model-project-structure-as-numbered-levels
    - CAPRMEDIO-REQU-049--use-one-global-tier-number-for-rmed-authority
---
# Derive global tier number from structure and applicability

CAPRMEDIO derives the root Goal as global tier `-1`; Project Principle, Core, and Standard as `0`, `1`, and `2`; each child Structural unit's Goal at its immediate parent's Standard global tier; and that child's Core and Standard at the next two global tiers, repeating the same handoff recursively while peer scopes at one Structural level share one mapping.
