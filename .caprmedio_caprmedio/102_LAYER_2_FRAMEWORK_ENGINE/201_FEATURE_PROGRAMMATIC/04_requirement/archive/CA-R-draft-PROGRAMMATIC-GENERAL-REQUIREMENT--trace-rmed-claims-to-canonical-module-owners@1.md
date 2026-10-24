---
atom_id: CA-R-draft
content_role: Requirement
type: Requirement
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
tier: 2
status: Draft
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-23 19:01:35 +0400"
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

The assessed PROGRAMMATIC implementation boundary, including descendant
Tools, Apps, MCP components, workflows, and policy implementations. The
boundary covers source modules that materially realize active Requirement,
Method, Evaluation, or Delivery Atoms. Generated output, vendor code, frozen
fixtures, and legacy history remain excluded unless separately admitted.

## Claim

Each assessed source module that materially realizes one or more applicable
active RMED Atoms **must** carry one structured `# implementation of:` block
at the module beginning. The block **must** contain only canonical Atom IDs,
grouped by the optional `Requirement`, `Method`, `Evaluation`, and
`Delivery` role lines. Empty roles **must** be omitted. No
`implementation of:` block is required or permitted solely before a
function, class, method, or other implementation unit.

For every applicable graph branch, select the narrowest directly realized
leaf and do not repeat its ancestors. Independent branches remain separately
citable, and many-to-many realization is valid when each cited relationship
is substantive. The block uses no versions, paths, titles, draft markers, or
other non-canonical identity text.

A cross-cutting policy is cited at the module where that policy is actually
defined and implemented. A consumer that merely imports, calls, or decorates
that policy does not cite the policy Method solely for reuse. Consumers are
located mechanically from code references; a second manual `applies` graph
is not created. A module with other substantive RMED claims still cites its
own claims. Policy applicability is independent of citation: a missing
citation never waives enforcement, and an independent direct implementation
elsewhere is an owner that must cite the policy Method without duplicating
citations for mere reuse.

## Details

The owner-block shape below uses illustrative IDs, not asserted source links:

```text
# implementation of:
# Requirement: CA-R-123, CA-R-456
# Method: CA-M-789
# Evaluation: CA-E-012
# Delivery: CA-D-345
```

Only the role lines that have canonical IDs are present. A module is an
owner only when it materially realizes the cited claim; a facade, caller,
dependency, relation, or projection alone is not ownership. A test does not
own another module's behavior merely by exercising it; a test module that
materially implements an Evaluation Atom is an owner of that Evaluation and
cites its Atom ID. Comments
are trace metadata, not proof of conformance, completion, or outcome.
Resolve actual definitions and references before citing them. Preserve an
unknown or dynamic reference as an explicit uncertainty rather than
inventing a source, owner, parent, policy, or proof.

Keep Requirements as statements of what is required, while Methods state
how the implementation decision and its citation format are made.
Traceability remains many-to-many, but citations stay at the actual
canonical module owner and are not copied merely because behavior is reused.

## Adoption notes

This Draft proposes a coordinated future reconciliation of R2117, M431,
E653, and M411. Those current Atoms remain active authority until a reviewed
replacement is accepted and promoted. This Draft does not silently supersede
them and is not an implementation or release gate.

Companion Drafts: [citation format](../../05_method/draft/CA-M-draft-PROGRAMMATIC-STANDARD-ENG_DECISION--write-rmed-owner-citations-only-at-module-start.md) and [traceability Evaluation](../../06_evaluation/draft/CA-E-draft-PROGRAMMATIC-STANDARD-QA_CASE--verify-owner-only-module-citations-and-derived-call-site-traces.md).
