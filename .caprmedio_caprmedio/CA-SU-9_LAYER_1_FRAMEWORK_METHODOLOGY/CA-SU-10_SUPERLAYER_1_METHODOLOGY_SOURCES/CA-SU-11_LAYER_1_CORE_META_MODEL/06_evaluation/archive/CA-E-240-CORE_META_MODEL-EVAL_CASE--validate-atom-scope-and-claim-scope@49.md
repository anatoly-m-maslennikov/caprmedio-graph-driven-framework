---
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom.Header.Topics.Main Subject
  - CAPRMEDIO_MODEL <+ Atom.Header.Relations.IS_CONTAINED_BY
  - CAPRMEDIO_MODEL <+ Atom.Content.Claim.Prose Claim
  - CAPRMEDIO_MODEL <+ Scope Unit
version: 49
updated_at: 2026-11-03 20:00:05 +0400
relations:
  evaluation_for:
  - CA-R-2102
  - CA-D-495
  - CA-D-479
  - CA-R-2714
atom_id: CA-E-240
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 7
role: Evaluation
form: Eval Case
carrier_destination:
  file:
    name: CA-E-240-CORE_META_MODEL-EVAL_CASE--validate-atom-scope-and-claim-scope.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation
container:
  scope_unit: CA-SU-11
---
## Summary

Validate Atom Scope **and** Claim Scope

## Claim

### Prose Claim

Verify that each complete Atom has exactly one `Header.Subjects.Active` and resolves its target Scope Unit from that active Subject. Containment and the Atom's own Scope context are separate from target resolution. Preserve textual applicability in Claim.Prose Claim without letting it select a different target.

## Details

### Test case

Create valid local and cross-Scope Goal or Demand fixtures with resolvable active Subjects. Include separate containment and own Scope contexts, and narrower and composite textual applicability in Prose Claim. Repeat with a missing, ambiguous, or unresolved active Subject and with applicability that contradicts its resolved target.

### Acceptance criteria

Each valid fixture has exactly one active Subject, resolves its target from that Subject, preserves its applicability, and retains its distinct containment and own Scope context. Each invalid fixture fails and identifies the affected Subject or contradictory applicability. Do not infer another target from applicability or repair an unresolved Subject by guessing.
