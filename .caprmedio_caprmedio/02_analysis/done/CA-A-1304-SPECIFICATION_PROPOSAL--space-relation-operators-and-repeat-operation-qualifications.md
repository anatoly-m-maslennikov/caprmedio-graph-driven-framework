---
atom_id: CA-A-1304
ref_id: CA-A-1304
role: Analysis & Advisory
form: Specification Proposal
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
status: Done
author: Anatoly Maslennikov
topics:
  main_subject: Entity
version: 3
updated_at: 2026-11-02 15:49:28 +0400
tier: 3
container:
  scope_unit: CA-SU-00
---
# Summary

Space relation operators and repeat Operation qualifications

## Decision

Place whitespace before and after the complete relation operator token. Its cardinality stays attached to the operator: Whole >{1+} Part, not Whole>{1+}Part or > {1+}. In a tree line, indentation supplies the left whitespace; an ordinary space separates the operator token from the following target.

Retain compact path separators /, // and . inside an operand. The rule does not add spaces inside property paths or change cardinality meaning. Keep the already spaced general named relation form Source ((RELATION_TYPE)) Target.

Repeat the Operations Content Role and Type qualification at each containment boundary. Each contained Type is declared only at its required structural position; no independent Step declaration followed by a reference is introduced.

```text
Atom/Content Role: Operations
	/Type: Workflow
		>{1+} Atom/Content Role: Operations/Type: Step
			>{0+} Atom/Content Role: Operations/Type: Sub-step
	/Type: Action
```

The latest example spells the Type Sub-step. The settled leaf-call and Workflow recursion rules are unchanged. Relative qualification navigation was discussed but its notation remains undecided; no parent-navigation operator is added.

## State

A1302 shows the explicit qualification and spaced relation tokens. Current source paths, historical inventories, code and runtime are not migrated by this presentation update.
