---
subjects:
  governs: 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action//Assess Release Readiness'
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Workflow//Release Readiness'
  - Subject/Graph Node/Engineering/Traceability
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Evaluation'
  - Subject/Graph Node/Engineering/Verification
  - Subject/Graph Node/Domain/Continuant/Projection
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: Operator'
  - Subject/Graph Node/Domain/Continuant/History/Journal.Record
  - Subject/Graph Node/Domain/Continuant/History/Release.ID
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: AI Agent'
version: 15
updated_at: 2026-10-27 06:04:45 +0400
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
