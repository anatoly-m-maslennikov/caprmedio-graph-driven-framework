---
cce_version: cce_1
cce_form: method
version: 13
updated_at: 2026-10-24 00:51:05 +0400
relations:
  child_of:
  - CA-M-261
  relates_to:
  - CA-M-262
  - CA-O-016
  - CA-R-1559
  - CA-O-024
subjects:
  governs: Project/Implementation/refactoring verification
  depends_on:
  - Spec
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Requirement'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Method'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Evaluation'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Delivery'
  - 'Atom/Content Role: Implementation'
  - Subject/Domain/Node/Continuant/Project
llm_session_ids:
- codex:01a02650-eff7-7453-8c37-0699b36773c6
atom_id: CA-M-270@13
status: Archived
content_role: Method
author: Anatoly Maslennikov
current_scope_unit: caprmedio
---
# Prepare verification before refactoring

**to** refactor existing Implementation, prepare the applicable verification **before** changing the target Implementation:

1. derive regression checks, end-to-end checks, acceptance gates, **and** canary criteria from the applicable Evaluations; select techniques by applicability rather than requiring **every** technique for **every** change. apply the governing Methods within Delivery boundaries while implementing these checks.
2. evaluate the existing Implementation using controlled complete inputs **and** record its outputs **and** existing failures as baseline evidence. expected correctness remains governed by RMED; an existing defect **must not** become a Requirement merely because it appears **in** the baseline.
3. evaluate the refactored candidate against current RMED **and** the recorded baseline under CA-M-262, using the implementation loop **and** retry policy. preserve the applicable checks across the comparison **unless** an authorized RMED change establishes a new baseline under CA-R-1559.
4. apply the required release gates **before** full rollout. **when** canary testing applies, prepare its criteria **before** refactoring **and** execute it on the candidate **after** that Implementation exists during the authorized controlled rollout.

this existing-Implementation baseline is comparison evidence, **not** missing specification recovered from old code, **and** is **not** a prerequisite for a fresh reconstruction with no existing Implementation.
