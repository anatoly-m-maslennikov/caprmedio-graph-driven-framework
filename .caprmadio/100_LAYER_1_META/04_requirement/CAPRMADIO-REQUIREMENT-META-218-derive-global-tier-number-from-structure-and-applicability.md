---
subject_scopes:
  - requirement-topology
tier: core
version: 2
updated_at: 2026-08-17 22:39:00
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMADIO-REQUIREMENT-247-use-one-global-tier-number-for-rmad-authority
---
# Derive global tier number from structure and applicability

CAPRMADIO must derive an RMAD Atom's global tier number by adding its structural-level number to the configured position of its readable applicability-tier name. The Project Goal occupies tier `-1`; the current structure therefore resolves Project Principle, Core, and Standard to tiers `0`, `1`, and `2`, META Core and Standard to tiers `2` and `3`, GOV Core and Standard to tiers `3` and `4`, and SPEC Core and Standard to tiers `4` and `5`.
