---
atom_id: CA-E-draft
content_role: Evaluation
type: QA Case
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
tier: 3
status: Draft
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-23 18:58:14 +0400"
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
This Evaluation checks implementation ownership and mechanically derived
call-site traces. It does not require a per-function, per-class, or per-method
RMED block, and it does not accept an `applies` annotation as evidence.

## Claim

Each module that materially implements one or more applicable active RMED
obligations has one current module-header `# implementation of:` block. The
block uses Atom IDs only, uses the correct Requirement, Method, Evaluation, and
Delivery role lines, omits empty roles, cites the narrowest active leaf for
each applicable branch, and does not duplicate an ancestor already covered by
that leaf. A module header is the ownership unit; a per-unit block is neither
required nor used to establish completion.

A shared policy or decorator module cites the Method that it implements. A
consumer that only imports, calls, or decorates with that shared policy is not
the implementation owner of that Method and does not receive a duplicate
authored Method citation merely because a code reference exists. The policy
must still be checked across every module where it is required: verify the
actual decorator or delegation mechanism, not imports alone. A caller that
owns independent claim logic cites its own relevant Requirements, Methods,
Evaluations, and Deliveries; if it directly implements the policy behavior
elsewhere, it also cites that Method and the result is reviewed for duplicate
ownership.

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

CA-E-653, CA-R-2117, and CA-M-431 currently require per-unit ownership blocks
and remain active until a coordinated authority revision is accepted. This
Draft proposes the owner-only module-header rule as a replacement candidate;
it does not change those active Atoms or claim current conformance.

Companion Drafts: [ownership Requirement](../../04_requirement/draft/CA-R-draft-PROGRAMMATIC-GENERAL-REQUIREMENT--trace-rmed-claims-to-canonical-module-owners.md) and [citation format](../../05_method/draft/CA-M-draft-PROGRAMMATIC-STANDARD-ENG_DECISION--write-rmed-owner-citations-only-at-module-start.md).
