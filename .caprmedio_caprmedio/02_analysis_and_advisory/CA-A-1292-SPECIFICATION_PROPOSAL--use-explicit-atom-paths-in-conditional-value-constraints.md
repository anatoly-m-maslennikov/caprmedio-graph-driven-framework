---
atom_id: CA-A-1292
ref_id: CA-A-1292
container:
  scope_unit: CA-SU-00
role: Analysis & Advisory
form: Specification Proposal
topics:
  main_subject: Model::CAPRMEDIO::Graph Syntax.Format Notation
tier: 3
status: Active
version: 2
updated_at: 2026-11-02 15:49:28 +0400
carrier_destination:
  file:
    name: CA-A-1292-CAPRMEDIO-SPECIFICATION_PROPOSAL--use-explicit-atom-paths-in-conditional-value-constraints.md
    path: .caprmedio_caprmedio/02_analysis_and_advisory
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
---
# Summary

Use explicit Atom paths in conditional value constraints

## Proposed syntax

Allow an if condition then constraint else constraint form inside the bracketed value context. Use the explicit atom-prefixed property path rather than an implicit owner reference:

```text
atom.tier[int, if atom.owning_scope_unit.name = 'project' then >=-1 else >=1]
```

The atom.owning_scope_unit.name path states whose owner name is evaluated. In this proposed condition, = compares values rather than assigning a value. The selected branch supplies the constraint on atom.tier. The bracketed value context follows A1291; this does not turn the same spelling outside that context into an instance assignment.

## Pending Tier-policy distinction

The Operator has refined the syntax example but has not yet answered whether it replaces the established Tier rules. Do not apply that policy change by inference. Existing Project Goals have Tier -1 and an Operator owner; ordinary Project-local Atoms have Tier >=0 and other ordinary Atoms have Tier >=1. The illustrated predicate would allow -1 for all Atoms matching the owner-name condition and does not by itself cover the Operator-owned Project Goal.

The literal project is preserved as supplied; it is not automatically reinterpreted as this project's actual name or the Project root kind. Binding the illustrative property path to a stored field or changing a Scope Unit name is outside this proposal.

## State

This is a separate conditional-syntax Specification Proposal. Conditional syntax admission and the Tier-policy example remain preparation work. No Core Definition, main Model constraint, Current Atom, governing configuration, tool or runtime is changed.
