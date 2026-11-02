---
atom_id: CA-A-1287
content_role: Analysis & Advisory
type: Specification Proposal
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
status: Done
author: Anatoly Maslennikov
subjects:
  governs: Model::CAPRMEDIO::Graph Syntax::Format
version: 3
updated_at: 2026-11-02 15:49:28 +0400
relations: {}
tier: 3
---
# Summary

Use strings instead of ref Format

## Decision

Remove ref from the value Formats. Use string for the values identifying Actors, Scope Units, Subjects and other modeled targets. Definitions and applicable relations retain what each value identifies; the string Format does not itself prove existence, authority or target kind.

```text
Atom.Author[string]{1}
Atom.Local Scope Unit[string]{1}
```

Project Goal ownership still identifies an Operator and its target still identifies the Project. These meanings are preserved by their definitions, not by a ref or ref: Project datatype annotation. Existing-kind @ references and named-relation syntax are unchanged: removing a value Format does not remove reference relations or notation.

## State

The main Model proposal and Value Format Definition Draft use string in place of ref annotations. No stored value, YAML field, defining relation, Current source or runtime behavior is changed.
