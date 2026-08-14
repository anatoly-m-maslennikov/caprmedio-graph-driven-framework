---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-META-161
scope_path: layer:meta
subject_scopes:
  - artifact-model
tier: core
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMADIO-REQUIREMENT-META-142-give-every-atom-one-independently-replaceable-claim
  child_of:
    - CAPRMADIO-REQUIREMENT-META-114-apply-mece-to-canonical-decompositions
    - CAPRMADIO-REQUIREMENT-META-117-admit-only-materially-distinct-framework-constructs
    - CAPRMADIO-REQUIREMENT-META-131-nine-content-roles-with-plan
    - CAPRMADIO-REQUIREMENT-META-154-three-artifact-forms-with-generated-projections
---

# Role-specific Atom atomicity

An Atom is the smallest independently governed unit for its Content role. It
has one stable identity and one indivisible lifecycle, but its atomicity model
depends on the role:

| Content role | Atomicity model |
|---|---|
| Concern | One independently resolvable matter requiring disposition. |
| Analysis | One bounded inquiry or interpretation product with one analysis objective; it may contain multiple findings, alternatives, or conclusions. |
| Plan | One bounded execution package with one scope, owner, lifecycle, and terminal disposition; it may contain multiple action points. |
| Requirement | One independently replaceable required outcome, obligation, prohibition, or boundary. |
| Method | One independently replaceable realization or transformation rule. |
| Assurance | One independently replaceable assurance obligation or case with its acceptance and disposition boundary. |
| Delivery | One independently replaceable rule for making a realized deliverable available to users or target environments. |
| Implementation | Deferred. No Atom atomicity model is established; the internal Implementation remains the project outside `.caprmadio/`. |
| Ops | One bounded enacted occurrence or observation set with one source, context, and time boundary; it may contain multiple factual results. |

In this rule, a Claim is an independently governed proposition whose acceptance,
rejection, replacement, or disposition changes a Concern or the distributed
Specification. It does not mean every grammatical assertion.

Concern, Requirement, Method, Assurance, and Delivery are Claim-bearing roles.
Each of their Atoms owns exactly one independently replaceable Claim. Analysis
may state findings or conclusions and Ops may state facts, but those statements
remain within their bounded product or occurrence and do not become independent
Claims. Plan uses its bounded execution-package model, and Implementation Atom
atomicity remains deferred to CAPRMADIO-QUESTION-META-006.

A carrier must be split when part of its content requires an identity,
lifecycle, replacement, or terminal disposition independent of the applicable
role-specific unit. Definitions, boundaries, conditions, examples, findings,
action points, project elements, and factual results may remain together only
within that unit.

Every Atom is replaced or archived as a whole. Partial replacement, partial
absorption, and partially active Atom identities are forbidden.
