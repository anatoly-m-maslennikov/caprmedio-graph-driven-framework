---
atom_id: CA-O-236@1
content_role: Operations
type: Action
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
author: Anatoly Maslennikov
status: Archived
version: 1
updated_at: 2026-10-29 23:57:07 +0400
subjects:
  governs: 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Requirement'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Method'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Evaluation'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Delivery'
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Verification/Static Analysis
  - Subject/CAPRMEDIO/Carrier
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
relations:
  depends_on:
  - CA-O-089
tier: 3
---
## Summary

Code Candidate Semantic Review checks bound evidence and policy without editing

## Operation

Code Candidate Semantic Review **means** the read-only Action that checks:

- the candidate;
- actual Evaluation **and** diagnosis evidence; **and**
- selected current R/M/E/D **and** Project-owned Tier 0 Atom bindings.

The Action assesses the complete bound applicable Method-policy set **and** reuses its meaning; it does **not** create **or** duplicate policy. For **every** applicable obligation, map it **to** its Evaluation predicate **and** current evidence, **or** retain an explicit gap. Record inapplicability with a reason rather than silently omitting an obligation. Missing required coverage remains unresolved; a selected subset of green linters is **not** complete review evidence.

The optional `review_phase` defaults to final for standalone review. In preliminary phase, assess the available candidate **and** complete bound code/policy assessment **without** pretending pending final checks have run. Return `preliminary_clear` **only when** that assessment has no confirmed findings; list **every** pending check **and** current source/candidate binding. Preliminary clearance is neither `passed` nor acceptance. Return `findings` for confirmed defects, `partial` for unfinished selected assessment, **and** `unresolved` for missing required authority, context, coverage, **or** permissions.

Final assessment requires actual complete current evidence bound **to** the same candidate, test definitions, applicable authority, portfolio, **and** inputs. Changed relevant bytes invalidate affected evidence.

Return:

- `passed` **only when** every selected assessment is current **and** complete with no findings;
- `findings` **when** selected assessment is complete **and** confirms implementation defects, test issues, **or** an admitted expected-phase observation;
- `partial` **when** actual selected assessment work remains unfinished; **or**
- `unresolved` **only when** required evidence, authority, context, **or** permission is missing **or** blocked; retain completed findings **and** actual results.

For `CA-O-089-PROJECT_CONFIGURATION-ACTION--diagnose-implementation-test-failures` result labels, map implementation/test defect **to** `findings` **and** authority/environment/unresolved **to** `unresolved`. `expected_initial_failure` remains an expected-phase observation **and** cannot produce an accepted-candidate claim **unless** admitted expected-phase criteria genuinely hold.

## Details

The Action performs no automatic fix, source/Atom edit, expected-result edit, retry, promotion, release, **or** Journal-completeness gate. Read-only commands are allowed; temporary fixture writes require explicit permission. Distinguish test issue, implementation defect, authority/environment blocker, expected-phase observation, **and** non-proven concern.
