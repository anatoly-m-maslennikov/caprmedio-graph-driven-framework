---
atom_id: CA-C-522@3
content_role: Concern
type: Question
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
local_tier: Standard
global_tier: 2
status: Archived
author: Anatoly Maslennikov
version: 3
updated_at: 2026-10-23 03:06:32 +0400
subjects:
  governs: Atom/Status
  depends_on:
  - Subject/Domain/Node/Continuant/Atom
  - Journal
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
relations:
  concern_about:
  - CA-P-2385
  - CA-P-2387
  - CA-D-446
  - CA-D-568
  - CA-D-570
---
# Summary

Which identity should a demoted Draft receive on promotion?

## Concern

For an identified Atom changed to ID-free Draft and later promoted, should an available genuine identified predecessor restore the old Atom ID as optional evidence, or should every promotion allocate a fresh ID? Manually authored Drafts without prior identity get a fresh unused ID either way.

## Evidences

The Operator explicitly removed mandatory Draft history/Journal gates. D568/D570 now prohibit retained-head/origin/lineage/consuming-successor admission. D446 preserves same-Atom demotion without carrying its assigned ID. Prior implementation restored a demoted ID only by mandatory trusted history. Restoring known same-Atom identity and not guessing from missing records must be reconciled explicitly. The Operator answered: "keep it simple, so #2. keep it simple everywhere. no special cases". Every ID-free Draft promotion allocates a fresh unused ID, including tool-demoted Drafts; no optional-history identity restoration remains. D446/D568/D570 and the native implementation are being aligned to this explicit decision.

## Blast radius

The identity choice is resolved; implementation and independent checks remain separate work. Manual Draft promotion, admitted Status support, independent Journal recording and ordinary safeguards proceed independently.
