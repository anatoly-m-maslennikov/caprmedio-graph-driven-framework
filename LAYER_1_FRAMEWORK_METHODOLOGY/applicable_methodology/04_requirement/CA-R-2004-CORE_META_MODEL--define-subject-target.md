---
atom_id: CA-R-2004
ref_id: CA-R-2004
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom.Header.Topics
  dependencies:
  - CAPRMEDIO_MODEL <+ Entity
tier: 1
status: Active
version: 14
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-R-2004-CORE_META_MODEL-RULE--define-subject-target.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2004-CORE_META_MODEL--define-subject-target.md
  source_atom_id: CA-R-2004
  source_atom_revision: 14
  source_sha256: 99dfdbdffc267d46c15df7fe31989959d29a8eece51a055e069886f886b34381
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Define Subject Target

## Claim

### Prose Claim


a direct GOVERNS or DEPENDS_ON target in an Atom's Subjects.



A direct GOVERNS or DEPENDS_ON target in Atom.Header.Subjects must be the topic addressed by a canonical Entity-rooted Subject expression and may identify a kind, axis, property, allowed value, or named instance.

## Details

Subject says what an Atom concerns. Content Role says what its content does. They are independent by definition. An Atom of any RMED Role can govern a topic in any declared Subject branch. A topic about how work is performed does not require a separate Method root.

Entity is the canonical expression root. Its four sibling branches are Object, Aspect, Graph Syntax and Carrier under CA-R-2462. Object specializes into Continuant and Occurrent. A source path retains the declared operators and full qualification; a short display label is not another identity or alias.

The Subject does not repeat or assign the Atom's Local Scope Unit, folder or Carrier. Topic meanings come from source use and Semantics; the Terms Graph derives definitions from those cases rather than creating another authority layer.

Within the shared Atom branch, `Atom.Header.Role` names the classification axis. `Atom/(.Header.Role := Requirement)` names a narrower Atom kind that inherits Atom properties. Naming the axis does not create a Content Role entity or assign a role value to an Atom instance.
