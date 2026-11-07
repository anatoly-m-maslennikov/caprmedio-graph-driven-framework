# Form proposal findings

## Smallest grounded declaration pattern

Use exactly one Requirement/Declaration Atom for each Form: Requirement, Solution, Direct Policy, Approach Policy and Decision. Its Main Subject is the generic classifier `Atom/(.Header.Form := <Form>)`, not a Role/Form pair.

Its Formal Claim admits the Form value and restricts instances to one approved Role whitelist:

```CFEL
Atom/(.Header.Form := <Form>)//$form;
$form.Header.Role:: [in (<approved roles>)]{::1};
```

This is grounded in the live generic Form selector, membership constraint and Form-value declaration patterns. It needs five Form declarations, not five semantic owners plus per-Role admission nodes. A Role-specific filter remains a selection/intersection of the generic classifier.

Requirement is a generic Form restricted to Role Requirement:

```CFEL
Atom/(.Header.Form := Requirement)//$requirement;
$requirement.Header.Role:: [in (Requirement)]{::1};
```

No live owner of that generic Form was found. Existing Requirement Declaration-family registrations remain distinct and unchanged.

## One human matrix choice

The exact same whitelist must govern all four Forms. The latest human direction is MEDO; the earlier contract/A1328 direction is RMEDO. Confirm one:

- MEDO: Method, Evaluation, Delivery, Operations.
- RMEDO: Requirement, Method, Evaluation, Delivery, Operations.

Both alternatives exclude Concern, Analysis, Plan and Implementation. Operations is not excluded merely because executable Workflow, Step and Action Forms remain distinct.

## Form semantics

- Requirement: a required outcome, behavior, property or constraint; admitted only to Requirement.
- Solution: how the current Scope Unit fulfills its responsibility, including descendants.
- Direct Policy: applies recursively to descendants without a local copy; SPECIALIZES can add detail without weakening parent constraints.
- Approach Policy: applies to a stated case and requires a local SPECIALIZES binding where that case applies.
- Decision: a particular local choice governed by applicable constraints.

None has a fixed or mandatory Tier.

Rule is dropped from the prospective default model. That does not rewrite or retire legacy Rule Atoms; their later classification is outside this lane.

## Exact Current dispositions

| Current source | Disposition | Form successors |
| --- | --- | --- |
| CA-R-1767@35 — Distinguish Implementation Methods from Implementation Decisions | Retire; do not mutate the materially changed Summary/Claim in place | Direct Policy, Approach Policy, Decision |
| CA-R-2123@9 — Limit PROGRAMMATIC Method and Delivery Types | Retire; remove the scope-specific legacy Type gate | Solution, Direct Policy, Approach Policy, Decision |

The generic Form declarations replace those two governing sources directly. Classifying individual legacy instances is later work; it is not a condition for retiring these source authorities.

Exact paths and SHA-256 pins are in `drafts.json`. Scope Delegation, Tier sources and other legacy-source preservation remain outside this lane.
