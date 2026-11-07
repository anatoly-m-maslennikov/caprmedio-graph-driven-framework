# Final Form proposal packet

## Form matrix

| Form | Admitted Roles |
| --- | --- |
| Requirement | Requirement only; existing CA-R-2999@1-draft |
| Solution | Requirement, Method, Evaluation, Delivery, Operations |
| Direct Policy | Requirement, Method, Evaluation, Delivery, Operations |
| Approach Policy | Requirement, Method, Evaluation, Delivery, Operations |
| Decision | Method, Evaluation, Delivery, Operations |

Concern, Analysis, Plan and Implementation are excluded from all five Form declarations.

Each common Form is one generic Requirement/Declaration Atom. Its active Subject is its Form-qualified Atom classifier. Its instance Role constraint is bound to that same classifier; there is no global `Atom.Header.Form` assertion and no per-Role admission boilerplate.

## Exact new bodies

The four exact proposal bodies are the `body` values in `drafts.json`. They use named instance bindings and resolved Role lists; there are no placeholders.

## Requirement/Requirement check

CA-R-2703@1 makes `Atom.Header.Form` one string and has no Form-not-equal-Role constraint. CA-R-2499@5 adds no Role/Form or placeholder restriction. No coordinated successor is needed. CA-R-2999@1-draft is already the sole Requirement Form proposal and is hash-pinned in `drafts.json`.

## Current authority dispositions

| Current source | Disposition | Successors |
| --- | --- | --- |
| CA-R-1767@35 — Distinguish Implementation Methods from Implementation Decisions | Retire; its materially changed Summary/Claim must not be mutated in place | Direct Policy, Approach Policy, Decision |
| CA-R-2123@9 — Limit PROGRAMMATIC Method and Delivery Types | Retire; remove the PROGRAMMATIC-specific legacy Type gate | Solution, Direct Policy, Approach Policy, Decision |

The listed generic Form declarations replace those Current governing sources directly. Individual legacy-instance classification is later work, not a prerequisite for the two source-authority retirements.

## Defaults and boundaries

Requirement and existing Declaration families are defaults. Rule is not a prospective default Form; legacy Rule Atoms map later. Scope Delegation is a common default, with exact declaration work owned by the scope lane.
