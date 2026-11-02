---
atom_id: CA-R-draft
content_role: Requirement
type: Requirement
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
tier: 2
status: Draft
author: Anatoly Maslennikov
version: 2
updated_at: "2026-10-23 19:11:00 +0400"
subjects:
  governs: Subject/Engineering/Source Unit Responsibility
  depends_on:
    - Subject/Engineering/Implementation Cohesion
    - Subject/Engineering/Behavior Ownership
    - Subject/Engineering/Outcome Evidence
relations:
  relates_to:
    - CA-R-2117
    - CA-M-431
    - CA-E-653
    - CA-M-411
---
# Summary

Trace RMED claims to canonical module owners

## Scope

The admitted PROGRAMMATIC implementation boundary, including its descendant
Tools, Apps, MCP components, workflows and policy implementations. Generated
output, vendor code, frozen fixtures and legacy history remain outside this
Requirement unless separately admitted.

## Claim

Every applicable active RMED claim realized inside the admitted boundary must
be discoverably traceable to the actual canonical source module or package
that materially owns its implementation. The trace must distinguish a genuine
owner from a facade, caller, dependency or other consumer that merely reuses
the behavior. A claim may have several genuine owners and an owner may realize
several claims; many-to-many realization is valid when each relationship is
substantive.

Unknown, dynamic or ambiguous realization must be reported as unresolved;
known unimplemented claims must be reported as unimplemented. Neither may be
converted into an invented owner, relationship or compliance result.
Trace metadata is evidence of where to
inspect; it is not proof that the implementation conforms, is complete, or
has produced the required outcome.

## Details

1. Establish the current applicable RMED claims and the admitted
   implementation boundary before assessing traceability. Resolve each claim
   to the actual source owner when the owner is identifiable; preserve an
   explicit uncertainty when it is not.
2. Keep the owner/consumer distinction visible. A module that only imports,
   calls, decorates or wraps another implementation is not its owner solely
   for that reuse. A module that independently materializes applicable
   behavior is a genuine owner even when another module supplies a shared
   policy.
3. Preserve independent branches and many-to-many relationships without
   claiming that a projection, comment, relation, generated artifact or test
   invocation alone owns the implementation. A test may be an owner of an
   Evaluation claim when it materially implements that evaluation, but merely
   exercising another module does not transfer ownership.
4. Report missing, stale, ambiguous or out-of-boundary traceability as an
   unresolved gap for explicit disposition. Do not mass-edit sources or infer
   proof from a missing or malformed trace.

## Adoption notes

This Draft states the required traceability outcome: discoverable ownership of
implemented RMED claims, honest unresolved reporting and no false compliance
proof. The companion Method Draft defines how module-level owner metadata is
written and how owner/provider/consumer relationships are derived. The
companion Evaluation Draft checks whether that Method is applied correctly.
Current CA-R-2117, CA-M-431, CA-E-653 and CA-M-411 remain active authority
until a reviewed role correction or replacement is accepted and promoted.
This Draft does not silently supersede them and is not an implementation or
release gate.

Companion Method Draft: [write RMED owner citations only at module start](../../05_method/draft/CA-M-draft-PROGRAMMATIC-STANDARD-ENG_DECISION--write-rmed-owner-citations-only-at-module-start.md).

Companion Evaluation Draft: [verify owner-only module citations and derived call-site traces](../../06_evaluation/draft/CA-E-draft-PROGRAMMATIC-STANDARD-QA_CASE--verify-owner-only-module-citations-and-derived-call-site-traces.md).
