---
atom_id: CA-O-draft
role: Operations
form: Action
status: Draft
version: 1
updated_at: '2026-11-03 19:01:50 +0400'
tier: 3
subjects:
  active: 'CAPRMEDIO_MODEL <+ Atom/(.Role := Operations)/Action'
  passive:
    - 'CAPRMEDIO_MODEL <+ Atom'
    - 'CAPRMEDIO_STRUCTURE <+ Scope Unit//PROJECT_CONFIGURATION'
relations: {}
---
## Summary

Apply one Direct Atom Update

## Claim scope

One exactly selected non-container Atom and its requested changes.

## Claim

Resolve the selected Atom once, validate the requested change against its model, and apply the case determined by its Status:

| Source | Update |
| --- | --- |
| Draft | Edit the proposal in place, including semantic content. Leave Current untouched. An existing-Atom proposal with unchanged Summary and Role retains its intended canonical marker and proposed Version. A Summary or Role replacement becomes a role-only Draft marker at Version 1 without allocating a canonical ID. Keep the filename and placement consistent with the edited proposal. |
| Current | Admit only technical changes that preserve governed meaning, Summary and Role. Apply the normal same-ID update: archive predecessor N, then publish Current N+1 with the actual edit time under CA-R-1432 and CA-R-1788. No Draft staging is needed. |
| Archived | Apply the requested technical repair directly to the selected carrier. Metadata is editable under the normal applicable rules, and the result must agree with its filename and placement. Git retains the previous carrier revision; do not impose a separate requirement to freeze historical metadata. This repair does not implicitly publish Current or promote a Draft. |

Validate the result's fields, Markdown structure, identity, Status and carrier consistency, and do not overwrite another target. An unchanged result is a no-op. A valid semantic Current change returns a handoff to Update Atom via Draft without executing it; an Archived request outside the technical boundary returns diagnostics and may point to separate Create Atom Draft use.

Return actual completed changes and any diagnostics or partial outcome. Reject containers and descendant expansion. Do not automatically retry or roll back. Journal only actual business events, without requiring Journal history as permission or success proof.
