---
atom_id: CA-O-draft
role: Operations
form: Workflow
status: Draft
version: 1
updated_at: '2026-11-03 18:54:48 +0400'
tier: 3
subjects:
  active: 'CAPRMEDIO_MODEL <+ Atom/(.Role := Operations)/Workflow'
  passive:
    - 'CAPRMEDIO_MODEL <+ Atom'
    - 'CAPRMEDIO_STRUCTURE <+ Scope Unit//PROJECT_CONFIGURATION'
relations: {}
---
## Summary

Update Atom via Draft

## Claim scope

This Workflow applies to one explicitly selected non-container Atom under the applicable CAPRMEDIO model in PROJECT_CONFIGURATION. It does not select descendants or perform a containment cascade.

## Claim

The Workflow accepts one exact Current predecessor and the caller's complete proposed content or changes, together with the applicable model and authority, source/currentness evidence, permission and effect admission, placement evidence, and any explicit target status. It does not invent missing changes or hide an edit operation. Its result carries the prepared Draft, the exact archived predecessor, the verified promoted result, any explicit old/new replacement mapping, and attributable diagnostics; a partial result retains the outputs already completed.

Resolve the promotion Status before any effect: use the caller's requested Current Status, or preserve the predecessor's Status when it remains admitted for the proposed Role/Form. If neither gives a valid Current Status, return diagnostics before creating a Draft or archiving anything. Bind the resolved Status as an enclosing Workflow input for the promotion Step.

Before creating a Draft, normalize the complete proposal against the exact Current predecessor. If it contains no actual requested Atom change, the Workflow returns a complete no-op terminal, preserves the Current Version and Updated At, and skips all three Steps; mechanical Draft metadata differences do not create an artificial N+1.

Its graph has exactly these three ordered Step nodes and no others:

1. [Create the proposed revision Draft](./CA-O-draft-PROJECT_CONFIGURATION-WORKFLOW--update-atom-via-draft/CA-O-draft-PROJECT_CONFIGURATION-STEP--create-the-proposed-revision-draft.md) is the entry Step. It must return a prepared and validated Draft before the next transition.
2. [Archive the exact revision predecessor](./CA-O-draft-PROJECT_CONFIGURATION-WORKFLOW--update-atom-via-draft/CA-O-draft-PROJECT_CONFIGURATION-STEP--archive-the-exact-revision-predecessor.md) runs only from that verified Draft result and must return the exact predecessor's verified archival result.
3. [Promote the prepared revision Draft](./CA-O-draft-PROJECT_CONFIGURATION-WORKFLOW--update-atom-via-draft/CA-O-draft-PROJECT_CONFIGURATION-STEP--promote-the-prepared-revision-draft.md) runs only from both verified prior results and is the terminal publication Step.

The child Step carriers own their individual RUNS bindings. This Workflow owns the entry, order, success transitions, input/output boundary, and terminal outcomes, but does not duplicate an Action algorithm or bind a Step to an implementation. A stale, invalid, ambiguous, unavailable, colliding, refused, failed, or uncertain result stops the graph at that point. Complete is reported only after verified promotion; otherwise the result truthfully reports blocked, failed, partial, or uncertain work and the actual completed outputs. There is no automatic retry or cross-step rollback, and Journal recording is an independent business-event record rather than a permission, completeness, or success gate.

## Details

For an unchanged Summary and Role, the prepared proposal uses the exact canonical identity with Version N+1 in its Draft marker (`canonical-ID@N+1-draft`). A Summary or Role replacement uses a role-only Draft marker and initial Version 1; promotion allocates a fresh never-reused canonical ID and returns an explicit old-to-new replacement mapping. An existing-Atom Draft carries its intended canonical identity and proposed Version rather than searching history.

The caller's target remains one non-container Atom: containers, semantic containment, descendants, and cascades are rejected. The first Step validates the exact source and complete proposal before the second Step can archive the Current predecessor. The second Step preserves the predecessor's Version N, Updated At, and content while materializing Archived, without creating N+1. The third Step requires that exact archival result, preserves the proposed content, Role, and meaning, admits only a model-qualified Current target status, and removes the Draft surface only after verified publication. No tier or scope upgrade is implicit.
