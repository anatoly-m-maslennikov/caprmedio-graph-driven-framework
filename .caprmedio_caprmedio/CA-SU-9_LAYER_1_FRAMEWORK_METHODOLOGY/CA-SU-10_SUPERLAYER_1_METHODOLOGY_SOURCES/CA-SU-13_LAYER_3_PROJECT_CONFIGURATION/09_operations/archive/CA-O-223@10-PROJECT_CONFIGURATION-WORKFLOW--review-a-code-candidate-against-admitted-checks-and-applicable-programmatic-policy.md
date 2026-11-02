---
atom_id: CA-O-223@10
content_role: Operations
type: Workflow
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
author: Anatoly Maslennikov
status: Archived
version: 10
updated_at: 2026-10-26 05:59:45 +0400
subjects:
  governs: 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Workflow'
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Requirement'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Method'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Evaluation'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Delivery'
  - Subject/Graph Node/Engineering/Implementation Evaluation
  - Subject/Graph Node/Engineering/Continuant/Carrier
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Step'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action'
  - Subject/Graph Node/Domain/Occurrent/Execution/Workflow Run
relations: {}
tier: 3
---
# Summary

Review a code candidate against admitted checks and applicable PROGRAMMATIC policy

## Operation

Entry is CA-O-226. Every Step-to-Step transition below is an explicit ON_RESULT edge in this Workflow; terminal results are not additional Steps. No other entry or successor selection is admitted.

Code Candidate Review Workflow means exactly four Steps: bind the candidate, run selected Evaluations, diagnose failed checks, and perform a read-only semantic review. It requires either an existing bounded Plan or an actually admitted in-session P/task containing its instruction, Definition of Done, and source context. It never creates a Plan Atom or fabricates an initiative identity. CA-O-020 and CA-O-089 retain their own selected P/Plan requirements.

| From Step | Result condition | Next Step or terminal result |
| --- | --- | --- |
| CA-O-226 | bound | CA-O-227 |
| CA-O-226 | blocked | unresolved |
| CA-O-227 | passed | CA-O-229 |
| CA-O-227 | failed | CA-O-228 |
| CA-O-227 | blocked | unresolved |
| CA-O-228 | expected_initial_failure | CA-O-229 |
| CA-O-228 | implementation_defect | CA-O-229 |
| CA-O-228 | test_implementation_defect | CA-O-229 |
| CA-O-228 | authority_change_required | CA-O-229 |
| CA-O-228 | environment_blocker | CA-O-229 |
| CA-O-228 | unresolved | CA-O-229 |
| CA-O-229 | passed | completed |
| CA-O-229 | findings | completed |
| CA-O-229 | partial | partial |
| CA-O-229 | unresolved | unresolved |

`completed` means all selected assessment work is complete: `passed` has no finding; `findings` has confirmed findings or an admitted expected-phase observation fully assessed and reported. `partial` means actual selected work remains unfinished. `unresolved` means a binding, evidence, authority, context, or permission is missing or blocked; completed findings and actual results remain retained. Unknown results and failed invocations are unresolved. No transition retries, replays, edits code, changes test expectations, or weakens an Evaluation.

CA-O-089's six labels map as follows: `implementation_defect` and `test_implementation_defect` become completed `findings` only after semantic assessment; `authority_change_required`, `environment_blocker`, and `unresolved` become `unresolved` with failed checks and completed findings retained; `expected_initial_failure` is an expected-phase observation, not a production defect, and can be completed only as an admitted expected-phase finding when its criteria genuinely hold. It never erases the failed check or permits an accepted-candidate claim without those criteria.

## Details

Bind candidate digest, owned paths, Plan-or-ephemeral-P/task context, direct full `requirements`, `methods`, `evaluations`, and `delivery` rows, Project Principles, permissions, allowed commands, source revisions/hashes, report location, and Run identity. CA-O-227 delegates unchanged to CA-O-020; CA-O-228 delegates unchanged to CA-O-089; CA-O-229 performs the separate semantic review and does not auto-fix. Binding/evaluation use Integrated context; diagnosis/semantic review use Isolated context only when admitted. Commands may write only explicitly admitted temporary fixtures with required permission. No Atom/source edit, replacement, promotion, release, MCP publication, or Journal-completeness gate is part of this Workflow.

Bind original full sources, revisions, paths, and digests **and** a complete explicit declared universe. An authorized/frozen request may explicitly select roots; expand declared governing parents per root, retain other explicitly selected applicable policy branches, and evaluate Scope/capability conditions. Parent relations alone do not define applicability, and physical directory ancestors or irrelevant siblings must not be inferred. `method_projection` is optional legacy derived convenience; direct rows remain required, while the projection's absence cannot block the review.

The executor owns actual Workflow, Step and Action lifecycle recording under applicable Run and Journal policy. These definitions do not invent a performed Run or business event. Recording failure remains distinct from actual review results and does not authorize automatic replay.
