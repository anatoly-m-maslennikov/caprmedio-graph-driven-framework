---
atom_id: CA-D-532@12
content_role: Delivery
current_scope_unit: TOOL_WORKFLOWS
claim_target_scope_unit: TOOL_WORKFLOWS
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Subject/Graph Node/Engineering/Continuant/Carrier
  depends_on:
  - Subject/Graph Node/Engineering/Continuant/Carrier
  - Subject/Graph Node/Domain/Continuant/History/Journal.Record
version: 12
updated_at: 2026-10-25 17:32:27 +0400
relations:
  delivery_for:
  - CA-R-1826
  - CA-R-1828
type: Eng Decision
tier: 3
---
# Summary

Deliver lifecycle result carriers

## Scope

Workflow admission owns identity, Version/time, lifecycle and complete schema decisions. Connector calls use CA-D-625 only to verify the supplied request, source preconditions and permission and to perform the explicit mechanical operation. A connector does not choose those decisions.

The returned lifecycle dispatch record and its handoff to native Tools and shared Run support.

## Claim

The route-specific lifecycle payload in CA-D-527's one result preserves the typed request identity; complete sealed and observed target/predecessor Carrier sets and, for Replace, every successor Carrier set; expected and observed Version/digest; operation/model/currentness selection; authorization; diagnostics; exact native outcome; history/lineage; and known/unknown effects. It supplies those facts to the shared result without creating an outer result, a second Event schema, or an assertion of persistence that did not occur.

CA-D-527 alone carries the outer disposition, actual started Run IDs/definition bindings, actual terminal/partial outcome, and Journal append diagnostics when attempted. This payload marks an affected carrier/effect unknown or unverified only when its mutation state is not observed; a missing Journal record or append failure is an independent diagnostic, does not invalidate an observed mutation, and never authorizes replay. Unstarted preview, decline, and block results invent no Run/Event identity.

## Details

### Required logical workflow result

Each independent Atom action carries its logical target and observed result. A replacement result distinguishes `target`, `created` and `archived` identities with exact Versions and source-state evidence. For target 100, successful fresh-ID replacement reports created 200 and archived 100. A proposed or failed effect is not serialized as an observed created/archived Atom; known, unknown and unperformed states stay explicit. Every actual changed same-ID state, including archival Status, is N+1 with actual time; exact prior history stays at N. A no-op retains Version/time. Summary or Type changes require replacement.

An ordered workflow result lists completed actions, the first failure and unperformed remaining targets. Earlier successful actions remain; no cross-Atom all-or-nothing or automatic rollback is implied. Every Summary edit requires fresh-ID replacement and predecessor archival. Incoming references are unchanged unless a separate explicitly authorized Find/Modify workflow changes selected referrers. Resume/retry for this new workflow family and stronger concurrency/publication guarantees remain deferred. This is a required serialization contract, not implementation or admitted-route evidence.

Status-transition diagnostics distinguish observed broken references from an unperformed or failed transition. An authorized Archive that newly breaks Relations retains the actual transition, lists every newly broken Relation and active referrer, and identifies a separate repair handoff without automatic repair or retargeting.
