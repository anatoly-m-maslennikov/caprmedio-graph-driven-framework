---
atom_id: CA-A-1285@1
content_role: Analysis
type: Specification Proposal
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
status: Archived
author: Anatoly Maslennikov
subjects:
  governs: Model::CAPRMEDIO::Continuant/Governing Objects/Atom.Subjects
version: 1
relations: {}
tier: 3
updated_at: 2026-10-29 02:33:15 +0400
---
# Summary

Use string format for Model Subject paths

## Decision

For simplicity, a Subject path is a string. Its format check verifies string-valued content and the admitted Model-tree notation. It does not prove or require that the named target existed before the defining Atom.

```text
subjects{0}
subjects.governs[string]{1}
subjects.depend_on[string]{0+}
```

A Definition can introduce its governed entity and path together. GOVERNS identifies what is defined or constrained; it does not itself assert prior existence. Writing a path alone is not defining authority or automatic instance creation. Explicit existing-kind references retain their separately declared meaning.

Do not infer target existence or reference authority from a special ref Format on Subjects. Model meaning and any separately governed semantic checks remain distinct from the basic string/syntax check. This decision does not settle Formats of unrelated properties.

## State

Subject examples, the Model proposal and related syntax R/M/E/D Drafts use string. Existing YAML subjects.depends_on spelling, Current source files and runtime remain unchanged.
