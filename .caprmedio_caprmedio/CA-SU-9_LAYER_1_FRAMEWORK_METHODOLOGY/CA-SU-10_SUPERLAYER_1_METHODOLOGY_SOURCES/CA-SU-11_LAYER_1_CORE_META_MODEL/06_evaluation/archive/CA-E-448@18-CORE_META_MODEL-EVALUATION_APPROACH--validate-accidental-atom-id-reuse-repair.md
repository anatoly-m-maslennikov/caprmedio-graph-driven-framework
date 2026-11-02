---
subjects:
  governs: Subject/Domain/Node/Continuant/Atom.ID
  depends_on:
  - Subject/Domain/Node/Continuant/Atom.ID
  - Subject/Domain/Node/Continuant/Atom/Content Role
  - Subject/Domain/Node/Continuant/Atom.Substance
  - Subject/Domain/Node/Continuant/Atom.Local Scope Unit
  - Subject/Domain/Node/Continuant/Atom
  - Subject/Domain/Node/Continuant/Atom.Version Number
  - Subject/Engineering/Carrier.Canonical Address
  - Subject/Domain/Node/Continuant/Project
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
  - Confidence Threshold
  - Subject/Domain/Node/Continuant/History/Journal
version: 18
updated_at: 2026-10-24 00:51:05 +0400
relations:
  evaluation_for:
  - CA-M-276
atom_id: CA-E-448@18
content_role: Evaluation
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
type: Policy
tier: 3
---
# Summary

Validate accidental Atom ID reuse repair

## Scope

Atom ID collision repairs.

## Claim

the Evaluation **must** reject completion of an Atom ID collision repair under CA-M-276-CORE_META_MODEL-METHOD--repair-accidental-atom-id-reuse **if** **any** of:

- the original owner was selected **without** sufficient recorded assignment evidence **or** the required Operator decision, **or** its valid Atom ID changed.
- a later accidental reuse retains the colliding ID, receives a previously used number, **or** receives an ID outside its Project prefix **and** Content Role sequence.
- an affected Claim, Content Role, Atom Scope, Claim Target Scope Unit, **or** textual Claim Scope changes beyond the approved identity-reference correction, a distinct Claim is lost **or** merged, **or** an unrelated identity changes.
- a prior Revision **or** historical Record is rewritten, history becomes unreachable, **or** the Work Journal lacks the exact mapping between the historical Carrier **and** its corrected identity.
- an affected current reference resolves ambiguously, remains unresolved, **or** resolves **to** a different intended Claim; an uncertain reference is rebound **without** the required Operator decision.
- legitimate same-Atom Revisions **or** derived copies are renumbered as accidental reuse, **or** lookup **or** compilation silently selects an identity winner.

the Evaluation **must** distinguish a paused collision awaiting an Operator decision from a completed repair. its checks **must** cover the verified-original-owner case, reversed Carrier discovery order, an unknown original owner, an ambiguous incoming reference, **and** legitimate same-Atom Revisions **or** derived copies.

## Details
