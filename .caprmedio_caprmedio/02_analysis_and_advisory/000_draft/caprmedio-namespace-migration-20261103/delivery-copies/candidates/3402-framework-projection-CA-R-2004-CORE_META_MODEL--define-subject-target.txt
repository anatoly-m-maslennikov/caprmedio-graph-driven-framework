---
subjects:
  active: CAPRMEDIO <+ MODEL <+ Atom.Subjects
  passive:
  - CAPRMEDIO <+ MODEL <+ Entity
atom_id: CA-R-2004
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
version: 14
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 1
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2004-CORE_META_MODEL--define-subject-target.md
  source_atom_id: CA-R-2004
  source_atom_revision: 14
  source_sha256: d70fe94e2a5c7a21405ac41290bda0355a4194a0eae735f4f74fce63af87bb12
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Define Subject Target

## Claim scope

a direct GOVERNS or DEPENDS_ON target in an Atom's Subjects.

## Claim


A direct GOVERNS or DEPENDS_ON target in Atom.Subjects must be the topic addressed by a canonical Entity-rooted Subject expression and may identify a kind, axis, property, allowed value, or named instance.

## Details

Subject says what an Atom concerns. Content Role says what its content does. They are independent by definition. An Atom of any RMED Role can govern a topic in any declared Subject branch. A topic about how work is performed does not require a separate Method root.

Entity is the canonical expression root. Its four sibling branches are Object, Aspect, Graph Syntax and Carrier under CA-R-2462. Object specializes into Continuant and Occurrent. A source path retains the declared operators and full qualification; a short display label is not another identity or alias.

The Subject does not repeat or assign the Atom's Local Scope Unit, folder or Carrier. Topic meanings come from source use and Semantics; the Terms Graph derives definitions from those cases rather than creating another authority layer.

Within the shared Atom branch, `Atom/Content Role` names the classification axis. `Atom/Content Role: Requirement` names a narrower Atom kind that inherits Atom properties. Naming the axis does not create a Content Role entity or assign a role value to an Atom instance.
