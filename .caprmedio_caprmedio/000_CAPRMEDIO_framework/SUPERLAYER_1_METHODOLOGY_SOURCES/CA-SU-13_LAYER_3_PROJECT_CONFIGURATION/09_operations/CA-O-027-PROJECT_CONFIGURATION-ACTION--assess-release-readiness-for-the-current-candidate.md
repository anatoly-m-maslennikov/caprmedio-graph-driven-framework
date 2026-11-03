---
subjects:
  governs: Subject/caprmedio/Action//Assess Release Readiness
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - Subject/caprmedio/Workflow//Release Readiness
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Traceability
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Evaluation'
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Verification
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Projection
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal.Record
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Release.ID
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: AI Agent'
version: 16
updated_at: 2026-10-27 19:59:44 +0400
relations:
  depends_on:
  - CA-R-1646
atom_id: CA-O-027
content_role: Operations
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
author: Anatoly Maslennikov
type: Action
tier: 3
---
# Summary

Assess release readiness for the current candidate

## Operation

Assess Release Readiness **means** the Action that returns the readiness disposition for the exact selected release candidate.

1. compare the candidate's current authority, Implementation, configuration, required Projections, evaluators, environments, **and** material inputs with the evidence bindings required by CA-R-1646.
2. require complete passing results for **every** applicable release Evaluation, no unresolved required conflict check, **and** **all** selected approval gates satisfied.
3. **if** an affected input changed **or** a binding is unknown, return readiness blocked **until** the affected checks produce current evidence. preserve the earlier results as historical facts.
4. record the actual disposition **and** its candidate/evidence binding **in** the shared Journal.

a passed readiness disposition applies **only** **to** the checked candidate. it does **not** perform publication, create a release event, freeze a Version, change governing authority, **or** substitute AI Agent confidence for required Operator approval.

## Details
