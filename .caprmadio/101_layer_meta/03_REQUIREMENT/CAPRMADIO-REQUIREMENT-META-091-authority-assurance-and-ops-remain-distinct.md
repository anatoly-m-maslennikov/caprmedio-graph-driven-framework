---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-META-091
scope_path: layer:meta
subject_scope: authority
priority: high
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CAPRMADIO-REQUIREMENT-META-028
  - type: child_of
    targets:
      - CAPRMADIO-REQUIREMENT-META-086
---

# Requirement — Keep authority, assurance, and Ops distinct

CAPRMADIO distinguishes:

- authoritative Requirements, Methods, Assurance criteria, and Delivery rules;
- concrete Implementations of those accepted claims;
- enacted execution, factual Ops records, and claim-bound evidence; and
- verification judgments about sufficiency and currentness.

Assurance material, evaluations, evidence, dashboards, and verification judgments may support, challenge, or invalidate reliance on a claim. They cannot establish, edit, replace, or override semantic authority. An assurance failure creates a Concern for the appropriate owner rather than silently changing the governing claim.

## Primary claim

CAPRMADIO keeps authoritative claims, assurance criteria, implementations, Ops facts, evidence, and verification judgments semantically distinct; assurance and Ops cannot establish or override authority.

## Rationale

Evidence can be canonical for a bounded Ops fact without becoming the authority for required behavior, implementation policy, delivery policy, or project scope.
