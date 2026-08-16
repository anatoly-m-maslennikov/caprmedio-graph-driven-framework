---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-META-029
scope_path: layer:meta
subject_scope: scope-topology
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMADIO-REQUIREMENT-META-066-meta-eligibility-rule
    - CAPRMADIO-REQUIREMENT-META-158-separate-authority-applicability-and-currentness
---

# Requirement — Bound profiles and applicability

A Profile is a reusable Method specialization for a declared scope. It may
select applicable tools, thresholds, durability behavior, language rules,
artifact governance, proof, or operational mechanisms. Once selected, its
applicable rules become part of the Method portion of the full current
Specification.

A profile must not:

- weaken or redefine a META invariant;
- change the meaning of a routing axis or layer;
- infer applicability from convenience alone; or
- require dummy artifacts for non-applicable concerns.

Non-applicability is explicit and reasoned. Project settings select allowed
profiles and routes but do not become a second source for their meanings.

## Primary claim

Profiles specialize Method and applicability without weakening META invariants,
redefining routing semantics, or requiring placeholder artifacts for
non-applicable concerns.
