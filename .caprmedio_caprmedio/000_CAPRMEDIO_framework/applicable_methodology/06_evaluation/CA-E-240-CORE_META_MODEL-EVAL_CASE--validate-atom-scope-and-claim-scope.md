---
atom_id: CA-E-240
ref_id: CA-E-240
container:
  scope_unit: CA-SU-11
role: Evaluation
form: Eval Case
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom.Header.Topics.Main Subject
  - CAPRMEDIO_MODEL <+ Atom.Header.Container
  - CAPRMEDIO_MODEL <+ Atom.Content.Claim.Prose Claim
  - CAPRMEDIO_MODEL <+ Scope Unit
tier: 7
relations:
  evaluation_for:
  - CA-R-2102
  - CA-D-495
  - CA-D-479
  - CA-R-2714
status: Active
version: 51
updated_at: 2026-11-05 22:47:24 +0400
carrier_destination:
  file:
    name: CA-E-240-CORE_META_MODEL-EVAL_CASE--validate-atom-scope-and-claim-scope.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation/CA-E-240-CORE_META_MODEL-EVAL_CASE--validate-atom-scope-and-claim-scope.md
  source_atom_id: CA-E-240
  source_atom_revision: 51
  source_sha256: e8e1047f20dfa9efcf14e5e1b78d25907c2ef3161ac7b91d000f9840b0766b3a
  original_relations_sha256: b448486d5687c8e6084f9eb8a06e38ac1eeb1387d6037d45636f2cf923a2da47
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
