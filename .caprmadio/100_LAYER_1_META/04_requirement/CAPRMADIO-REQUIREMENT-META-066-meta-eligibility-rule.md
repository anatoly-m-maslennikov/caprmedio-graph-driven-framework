---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-META-066
scope_path: layer:meta
subject_scope: authority
tier: core
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMADIO-REQUIREMENT-META-022
  child_of:
    - CAPRMADIO-REQUIREMENT-META-117-admit-only-materially-distinct-framework-constructs
    - CAPRMADIO-REQUIREMENT-META-120-preserve-bounded-meaning-across-structural-scales
---

# Requirement — Apply the META eligibility rule

A rule belongs in META only when all three conditions hold:

1. it remains true when downstream languages, tools, hosts, providers, and
   repository layouts change;
2. it governs multiple layers or defines a boundary between layers; and
3. it can be stated without importing downstream implementation concepts.

If any condition fails, place the rule in the earliest downstream layer that
can own it completely. META owns the invariant; that layer owns the mechanism.

A concrete substrate is eligible for META only when the operator explicitly
makes it mandatory and non-substitutable for CAPRMADIO governance. Replacing
such a substrate is a constitutional amendment rather than a downstream
implementation choice.

For example, META may require durable changes to be traceable. GOV owns the
carrier and provenance policy, while IMPL owns applicable executable
enforcement. META must not absorb either mechanism merely because several
later layers use it.

## Primary claim

META owns only technology-independent cross-layer invariants and explicitly
operator-mandated, non-substitutable governance substrates whose replacement
would change the CAPRMADIO constitution.
