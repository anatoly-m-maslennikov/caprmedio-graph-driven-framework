---
atom_id: CA-P-1824@5
content_role: Plan
type: Plan
label: Task
work_sequence_number: 5
current_scope_unit: caprmedio
author: Anatoly Maslennikov
assignee: AI Agent
autonomous_confidence_threshold: 90
status: Archived
version: 5
updated_at: 2026-10-24 08:22:45 +0400
subjects:
  governs: Implement the guarded image restoration coordinator
  depends_on:
  - Subject/Engineering/Action
  - Subject/Engineering/Tool
  - Framework Package
  - Docker Image
  - Subject/Domain/Node/Continuant/History/Journal
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
relations:
  is_decomposition_of:
  - CA-P-1820
  blocks:
  - CA-P-1826
tier: 3
---
# Summary

Implement the guarded image restoration coordinator

## Objective

Implement the accepted coordinator and bounded native invocation using the verified retained reader, direct Journal and shared publication lock. Publish only a genuinely changed image_digest after exact frozen-input revalidation.

## Details

The Operator explicitly approved rebuilding the missing selected image from verified retained N and registering its verified image digest. Preserve N's package, Version, public ca Skill, original proof and historical Journal. N21 remains unknown and is not replayed. No release gate is waived. Root owns Git, source admission and serialized runtime effects; independent workers own their assigned source scopes.

Work estimate: <=15 minutes; add a necessary remainder before expanding beyond this bound. Source RMED is reviewed before implementation. Test-first acceptance uses honest local doubles separately from actual Docker proof.

## Definition of Done

Coordinator success/refusal/partial/unknown/recording tests pass with accepted source and ABI. Package/Skill stay unchanged, same-ID results retain the selector/proof, and all actual effects are represented truthfully.

## Result

Independent review accepted code ea443b39a36c2504a12089d7a9778cd82e385a14c73a3a5d76007e19fffd7a0f after exact pending-event recovery was implemented. Thirteen coordinator tests pass, with the real executor type patched only at its command boundary; actual Docker execution remains CA-P-1826.
