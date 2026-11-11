---
atom_id: CA-A-1297
ref_id: CA-A-1297
container:
  scope_unit: CA-SU-00
role: Analysis & Advisory
form: Specification Proposal
topics:
  main_subject: Model
tier: 3
status: Done
version: 3
updated_at: 2026-11-02 15:49:28 +0400
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
---
# Summary

Separate advanced expressions from the plain Model review

## Decision

Review the Model proposal and related prepared Drafts directly in subagents, without FPF. Cover primary kinds, relations and simple notation, containment and inheritance, Claim layout, direct-value cardinalities, basic Formats and agreement with the Operator's latest decisions.

Keep advanced formulas and conditions inside square brackets as separate proposals, outside this review. The core review uses [format], not [format, condition]. Numeric bounds and other substantive requirements stay in prose; excluding their formal annotation does not change those requirements.

## Excluded proposal material

A1282 holds general formula expressions. A1288–A1290 hold explicit Selection execution and Selection-result property projection. A1291 and its Value Constraint Annotation Definition Draft hold bracketed conditions and implicit materialization. A1292/A1293 hold conditional and reference-traversal experiments. Function-listing proposal A1237 also remains deferred. A1294's simple bound stays recorded, but its bracket condition spelling is excluded here; its Tier policy remains in prose. A1295's no-per-case-function rule remains applicable authoring guidance.

The advanced Definition Draft is retained, not deleted or promoted. Exclusion is a review/scope boundary, not retirement of the proposals. Do not report incompleteness of the excluded language as a defect in the plain packet.

## Review operation

Use four read-only review lanes: structure and relations; containment and inheritance; Claims/cardinalities/Formats/carriers; alignment with latest Operator decisions. The parent integrates findings and owns all edits. No FPF command, source promotion, Engine/code review or runtime change is included.

## State

The main proposal and shared syntax Drafts are separated from advanced conditions for review. Findings will be recorded after the parallel review; no review pass or closure is claimed by this scope record.
