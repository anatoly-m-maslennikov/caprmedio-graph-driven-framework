---
atom_id: CA-E-draft
content_role: Evaluation
type: QA Case
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
tier: 3
status: Draft
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-23 19:09:45 +0400"
subjects:
  governs: "Subject/Engineering/Source Unit Responsibility"
  depends_on:
    - "Subject/Engineering/Implementation Cohesion"
    - "Subject/Engineering/Outcome Evidence"
relations:
  relates_to:
    - CA-E-653
    - CA-R-2117
    - CA-M-431
    - CA-M-411
---
# Summary

Verify owner-only module citations and derived call-site traces

## Scope

New or materially changed admitted PROGRAMMATIC source and its directly owned
tests, including shared policy or decorator modules and their consumer modules.
Resolve the bound Method traceability policy first, then run this QA check. It
does not require a per-function, per-class, or per-method RMED block, and it
does not accept an `applies` annotation as evidence.

## Claim

The checker derives its required citation shape from the bound Method policy.
For each applicable owner module, it parses one current module-header
`# implementation of:` block, validates Atom IDs and role lines, verifies the
source and current carrier for each citation, selects the narrowest active
leaf for each applicable branch, and rejects an ancestor duplicated by that
leaf. A module header is the ownership unit; a per-unit block is neither
required nor used to establish completion.

A shared policy or decorator module cites the Method that it implements. A
consumer that only imports, calls, or decorates with that shared policy is not
the implementation owner of that Method and does not receive a duplicate
authored Method citation merely because a code reference exists. The checker
derives the provider/consumer code graph, verifies the actual decorator or
delegation mechanism rather than imports alone, and applies the Method's
owner-only and consumer-exception rules. A caller that owns independent claim
logic cites its own relevant roles; if it directly implements the policy
behavior elsewhere, the result is reviewed for duplicate ownership.

## Details

### Test case

Run an isolated fixture matrix containing:

1. a shared policy provider with a valid module-header Method citation;
2. a consumer that imports and calls the provider;
3. a consumer with an unused policy import;
4. a module missing the required decorator or delegation;
5. an unrelated consumer that references a different policy;
6. an independent policy owner with its own claim logic; and
7. a dynamic or unknown policy reference that cannot be resolved mechanically.

For every fixture, obtain the bound Method's role-ID parsing, source-validity,
provider/consumer graph, and test/evaluation-owner exception rules before
checking the result. The checker returns each measured citation, resolved
owner, applicable leaf, source evidence and test evidence; it reports an
unknown or unavailable Method rule as unresolved rather than substituting a
Requirement or an unrelated Evaluation.

The provider and consumers must be checked for actual decorator or delegation
behavior, not only imports or call-site syntax. A correctly cited module with
no per-function, per-class, or per-method block passes this owner-only case. A
new per-unit block in the obsolete or stale format is reported as a
traceability gap and must not crash runtime evaluation. Derive call-site
references mechanically for review; do not convert them into authored
ownership edges.

Reject malformed or incomplete cases containing an invalid or stale Atom ID,
version marker, path, filename title, wrong role citation, or archived Atom.
Calls are not proof that a policy was applied, comments are not proof of
conformance, and an unknown or dynamic reference is reported truthfully as
unresolved rather than treated as a complete call graph.

### Acceptance

Pass only when every assessed owner module has one valid current module-header
block, every citation resolves to the named current role, narrowest active
branches are selected without ancestor duplication, and the provider/consumer
matrix distinguishes implementation ownership from derived references. The
policy is accepted across all required modules only when the real decorator or
delegation mechanism is present; an import, call, comment, or relation alone
does not pass. Independent claim owners retain their own claim citations, and
many-to-many ownership is accepted when each localized module or package
relationship is substantive and unambiguous.

### Failure disposition

Report each missing, invalid, stale, overbroad, wrong-role, duplicate, or
unresolved citation and reject the affected traceability result. Preserve the
implementation and do not invent a call-graph edge, silently add an authored
citation, mass-edit source, or turn this Evaluation into a runtime failure.
Dynamic resolution remains unresolved until evidence identifies the owner and
the actual policy mechanism.

## Adoption notes

CA-E-653 and CA-R-2117 remain current context until a coordinated authority
revision is accepted; CA-R-2117 is informational here, not the rule source.
This Draft specifies a checker for the bound Method trace policy and does not
change those Atoms or claim current conformance. On promotion, the checker
must consume the promoted Method's own citation rules and retain unresolved
human-review results instead of treating a mechanically incomplete call graph
as complete.

Evaluated Method Draft: [module-start owner citations](../../05_method/draft/CA-M-draft-PROGRAMMATIC-STANDARD-ENG_DECISION--write-rmed-owner-citations-only-at-module-start.md).

Companion Method Draft: [localized ownership and shared policies](../../05_method/draft/CA-M-draft-PROGRAMMATIC-CORE-ENG_POLICY--localize-engineering-decisions-and-reuse-shared-policies.md).

These Draft references identify the candidate procedure for review, not an
active runtime policy. Operational evaluation requires the admitted Method;
historical CA-M-431 and CA-M-411 references are reconciliation context only.
