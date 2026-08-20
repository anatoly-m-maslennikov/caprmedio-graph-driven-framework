---
subject_scopes:
  - feature-boundary
version: 9
updated_at: 2026-08-20 23:58:00
relations:
  child_of:
    - CA-R-802-REQUIREMENT-FR_ENGN_TOOLS--define-flat-auto-commit-tool-topology
---
# Emit only operational Hook triggers

`COMMIT_TRIGGER` must establish one logical repository file-change boundary from a registered adapter event and emit one minimal trigger to the `COMMIT_CHANGE_SET` end-to-end orchestration interface. The trigger contains a stable adapter identity, stable source-event identity, resolved repository identity, observation time, observed before-path and after-path candidates, and the structured LLM-session candidate resolved from explicit invocation context or the adapter's registered host interface. The candidate contains only canonical LLM application name and host session UUID; it does not concatenate or duplicate the event time.

Every logical change to an eligible governed repository file that an enabled adapter accepts must emit exactly one trigger. Repeated or noisy observations that carry the same adapter and source-event identities must produce the same single trigger identity rather than additional actions. An adapter that cannot establish the boundary or unambiguously resolve required LLM-session provenance must fail without emitting a trigger. The Hook must not classify the change set, traverse the graph, gather Doer context, edit or stage files, create commits, write Journals, or perform any other mutation. Every pipeline-owned Work Journal or runtime-state write is correlated to its action and suppressed from emitting another `COMMIT_TRIGGER`, including when related records span multiple Journal carriers; suppression must not depend only on path spelling or timing. Adapter selection and enablement remain explicit and operator-controlled, and no one adapter's substrate event becomes canonical framework meaning.
