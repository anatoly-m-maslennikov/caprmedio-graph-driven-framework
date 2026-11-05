---
atom_id: CA-A-1285
ref_id: CA-A-1285
container:
  scope_unit: CA-SU-00
role: Analysis & Advisory
form: Specification Proposal
topics:
  main_subject: Model::CAPRMEDIO::Continuant/Governing Objects/Atom.Subjects
tier: 3
status: Done
version: 3
updated_at: 2026-11-02 15:49:28 +0400
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
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
