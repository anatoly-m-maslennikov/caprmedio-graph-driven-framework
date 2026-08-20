---
subject_scopes:
  - feature-boundary
version: 6
updated_at: 2026-08-20 22:25:00
relations:
  child_of:
    - CA-R-802-REQUIREMENT-FR_ENGN_TOOLS--define-ops-tools-feature-group
---
# Emit only operational Hook triggers

`COMMIT_TRIGGER` must be one operational Hook unit owned immediately by `OPS_TOOLS`. A registered adapter establishes a logical repository file-change boundary from its substrate event and supplies a stable adapter identity, stable source-event identity, resolved repository identity, observation time, observed before-path and after-path candidates, and the structured LLM-session candidate resolved from explicit invocation context or the adapter's registered host interface. The candidate contains only canonical LLM application name and host session UUID; it does not concatenate or duplicate the event time. Repeated or noisy observations that carry the same adapter and source-event identities must produce the same single trigger identity rather than additional actions; an adapter that cannot establish that boundary or unambiguously resolve required LLM-session provenance must fail without emitting a trigger. The Hook emits only this minimal trigger and must not classify the change set, traverse the graph, gather Doer context, edit or stage files, create commits, write Journals, or perform any other mutation. Every pipeline-owned Work Journal or runtime-state write is correlated to its action and suppressed from emitting another `COMMIT_TRIGGER`, including when related records span multiple Journal carriers; suppression must not depend only on path spelling or timing. Adapter selection and enablement remain explicit and operator-controlled, and no one adapter's substrate event becomes canonical framework meaning.
