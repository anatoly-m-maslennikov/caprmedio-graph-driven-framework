---
atom_id: CA-O-090
content_role: Operations
type: Action
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
author: Anatoly Maslennikov
status: Active
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control/Effect Authorization
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Method'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Evaluation'
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Verification/Dynamic Testing
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Summary
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Author
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Tier
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: AI Agent'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control/Decision Confidence
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Selection
version: 20
updated_at: 2026-10-27 19:59:45 +0400
relations:
  depends_on:
  - CA-R-1559
tier: 3
---
# Summary

Activate corrective Methods after verified fixes

## Operation

Corrective Method Acceptance **means** the Agentic Action that promotes a verified corrective Method Draft **only** after the repaired candidate **and** its regression evidence justify that Method.

- inputs: recorded corrective Method Drafts, diagnosis, actual fix, regression **and** current-candidate Evaluation results, source/definition bindings, current applicable Method authority, selected Plan, actual Author information, **and** confidence/permission gates.
- require that the regression detects the diagnosed defect, passes after the fix, **and** the required relevant checks pass against the current candidate. stale, absent, failed, **or** incomplete evidence keeps the Method Draft non-authoritative.
- check the proposed Method against Project Principles, higher-tier authority, existing Methods, its Claim/Subject boundary, **and** the actual fix. tests are necessary evidence, **not** proof that an overbroad policy is valid. do **not** generalize the Standard Method into Core, General, **or** a broader policy during this Workflow.
- reuse existing equivalent authority rather than activate a duplicate; retain the recorded Draft's disposition. any supersession **or** governing-authority edit follows its own permission **and** history rules.
- resolve the effective confidence threshold **and** permissions, including CA-R-1559 for governing-Atom changes. obtain required Operator approval; authorship **or** a passing test never grants permission. an unresolved gate returns `blocked` with the Draft unchanged.
- **only** after verification **and** admission, promote the new Method under the current Atom identity, Status, Carrier, **and** history rules, preserving its Summary. return `accepted` with actual activated identities/Revisions **and** the governing-baseline change; return `already_covered` for a nonduplicating disposition; return `blocked` for incomplete verification **or** admission.
- return the accepted Method identities **and** baseline change **to** the separate learning Run. refresh affected direct Method source bindings **and** require current-baseline review **before** later work relies on them; regenerate an optional derived projection only for a consumer that uses it. do **not** reopen a completed implementation Run merely **to** make learning part of its completion **or** claim its old evidence proves the changed authority.

## Details
