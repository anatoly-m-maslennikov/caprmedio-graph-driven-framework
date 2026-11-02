# Admitted-value formalization review — 2026-11-01

Status: candidate needs repair; no CFEL Rule or consumer change applied.

The Plan Work Sequence Number Declaration contains only formal constraints. Execution order belongs to the Workflow for Plan execution. No navigation Method or Term was created.

## Findings

1. Explicitly admitted literals alone do not establish “atomic unit” or prohibit an explicitly admitted placeholder. The intended Form restriction needs one clarification.
2. Short notations admitted for a Relation are not automatically the admitted values of a Relation Definition Property. Resolve the same Definition’s Relation explicitly before replacing the conditional-presence prose.
3. Effective MODEL resolution must use the selected model’s rules. Do not invent whole-set replacement or merge behavior. Unknown, incomplete, ambiguous or circular resolution cannot pass.
4. Extra context labels are unnecessary. Use the effective MODEL, the bearer’s Role or Relation, and complete declared admissions.

## Outcome

The two Declarations retain their constraints and prose. Node descendants and their Properties still have 19 prose Claims. The proposed language function remains a candidate, outside the Draft register. Parser and runtime behavior were not implemented or checked.

Evidence: [candidate](declaration-expansion/admitted-values-candidate-20261101.json), [independent review](declaration-expansion/admitted-values-review-20261101.json).

## Later Operator correction

A Form may share its Role’s name. The candidate’s anti-copy test is superseded. This correction removes only the same-name ban; it does not by itself settle the remaining atomic/admission wording or the Relation-to-notation admission mapping. See [decision](declaration-expansion/role-form-same-name-decision-20261101.json).
