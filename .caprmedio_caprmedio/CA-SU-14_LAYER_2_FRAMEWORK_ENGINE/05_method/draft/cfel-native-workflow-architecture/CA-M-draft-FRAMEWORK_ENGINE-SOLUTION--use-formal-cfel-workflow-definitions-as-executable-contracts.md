---
identity:
  atom_id: CA-M-draft
context:
  container:
    scope_unit: CA-SU-14
  role: Method
  form: Solution
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation
      <+ Execution Control
  tier: 0
state:
  status: Draft
  version: 1
  updated_at: 2026-11-11 04:14:10 +0400
destination:
  file:
    name: CA-M-draft-FRAMEWORK_ENGINE-SOLUTION--use-formal-cfel-workflow-definitions-as-executable-contracts.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/05_method/draft/cfel-native-workflow-architecture
author: Anatoly Maslennikov
---

## Summary

Use formal CFEL Workflow definitions as executable contracts

## Claim

### Prose Claim

Use the adopted executable CFEL profile as the Workflow execution contract. Compile the Workflow Formal Claim together with its referenced Step and Action contracts; derive the executable control/data-flow plan from those sources instead of maintaining a separate per-Workflow Python route, YAML program or independent graph definition. Prose and Mermaid explain the same definition and must agree; the engine executes the formal contract.

## Semantics

Resolve effective contracts through the declared ancestry and qualification chain at arbitrary depth, schematically `X//Y//Z/...`. Combine inherited properties and permitted refinements/overrides according to the model; This applies to all dependent entities and nested Properties and their constraints, not only primary kinds; preserve inherited nested structure instead of flattening it away. Node to Atom to Method is only an example, not a hardcoded entity or Role list. Do not assemble a contract only from its exact leaf declarations or silently narrow unresolved declaration semantics.

The executable profile binds Workflow inputs and outputs, typed fixed values, Step inputs, references to completed earlier outputs, nested Workflow calls, and explicit control flow. Preserve the distinction between an Action contract and its code or prompt implementation. Keep separately governed Workflow and Step carriers; a serialized block references those Steps rather than duplicating their Action contracts.

Parentheses delimit blocks and grouping; semicolons terminate statements. Multiline layout and indentation are optional readability aids with no execution meaning. Quoted strings, comments and nested parentheses must be tokenized correctly; semicolons inside a string are not statement boundaries.

A Decision Step evaluates a side-effect-free Boolean condition and selects exactly one declared branch. The proposed native Decision Step owns its condition; the enclosing Workflow Formal Claim owns its then/else branch bodies. IF identifies that Decision Step, so the engine can attribute the decision without duplicating its condition or destinations. Validate that the referenced Decision belongs to the enclosing Workflow; do not call an external Tool merely to choose a branch. Execution/Input Steps retain their declared Action or nested Workflow target. This requires an explicit Core amendment to the current leaf RUNS/cardinality rule; this Method Draft does not grant that amendment.

Conditions use typed Workflow inputs, constants or available earlier results, with comparisons and AND/OR/NOT. An absent value, type mismatch, unsupported construct, unresolved target or unavailable branch output is an explicit error, not a guessed Boolean. Both branch paths must satisfy the declared Workflow output contract; an output binding may consume only a value produced on its actual path.

## Details

The following are proposed executable-profile spellings, not valid Current CFEL or runnable Workflow Atoms. Every named Execution/Input Step needs its declared Action or Workflow target and input/output bindings. A native Decision Step instead owns its condition and is associated with the enclosing Workflow branches under the proposed Core exception. Core methodology must declare the grammar, name resolution and execution-context distinction before adoption.

One-Action body:

```text
RUN(Step//read);
RETURN(OUTPUT(Step//read, result));
```

The separate Decision Step carrier declares the condition, illustratively:

```text
Step//decide.Kind := "Decision";
Step//decide.Condition := (INPUT(approved) == true);
```

The Workflow body owns the branch map and references that Step:

```text
IF (Step//decide) THEN (
    RUN(Step//apply);
    RETURN(OUTPUT(Step//apply, outcome));
) ELSE (
    RUN(Step//decline);
    RETURN(OUTPUT(Step//decline, outcome));
);
```

Removing indentation or placing these statements on one line does not change their meaning. The explicit branch returns avoid reading an output of a Step that was not executed. These candidate RUN/RETURN/INPUT/OUTPUT constructs, Decision condition Property and IF-to-Step association need formal declarations; they are not inferred from their spelling.

The language-model owner remains Core methodology. FRAMEWORK_ENGINE consumes that model; it must not silently turn declarative CFEL constraints into effectful operations or evaluate arbitrary source as Python.
