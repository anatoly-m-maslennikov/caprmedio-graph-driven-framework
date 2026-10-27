---
atom_id: CA-P-2642
content_role: Plan
type: Plan
label: Task
work_sequence_number: 3
current_scope_unit: caprmedio
claim_target_scope_unit: CORE_META_MODEL
author: Anatoly Maslennikov
status: Done
subjects:
  governs: Subject/Graph Node/Domain/Continuant/Atom
version: 2
updated_at: 2026-10-26 06:39:23 +0400
relations:
  IS_CONTAINED_BY:
  - CA-P-2639
tier: 4
---
# Summary

Define carrier-independent RMED Claims

## Objective

Define Claim as present on every RMED Atom without fixing its representation
to a Markdown content section. Apply decisions D03/D04 to the logical model.

## Details

Addresses I03's corrected premise. Estimated own work: up to 15 minutes.

- Read Current R1269, R1417 and R2001. Identify the exact clauses that make
  Claim Markdown-only or say a formal Graph Rule has no Claim.
- Preserve the distinction between a logical Claim and its representation.
  State that every RMED Atom has a Claim, without declaring one universal
  storage location or extending this requirement to C/A/P/O.
- A natural-language Claim uses atom.content.claim. A fully formal statement
  can use atom.claim.* or Governing Configuration; do not require all formal
  statements to change artifact form.
- Correct the no-Claim Graph Rule language. Do not introduce an inheritance
  exclusion merely because the Claim is structured YAML instead of prose.
- Preserve existing Drafts/Archives and unrelated meanings; create normal
  predecessors for changed Current definitions.
- Record the actual changed source IDs/versions and any concrete affected
  definition outside this bounded set. Split additional work instead of
  expanding this Task beyond its own-work estimate.

No code, renderer, configuration migration or Terms Graph work is included.

### Completion evidence

R1269@26, R1417@24 and R2001@10 define carrier-independent RMED Claims and the formal Graph Rule statement. V04 PASS.

Source verification: `.caprmedio_tmp/subject-fpf-refinement/verify.final.md`.
Final source/output pins: `.caprmedio_tmp/subject-fpf-refinement/graph-closure/graph.subject-views.manifest.json`.
Actual effect verified; no production tool/runtime implementation or release is claimed.

## Definition of Done

- The touched definitions require a logical Claim for RMED without one fixed
  representation.
- A formal Graph Rule is not described as Claim-less.
- The accepted natural-language and formal alternatives are stated consistently.
- No unnecessary duplicate Claim, new generic Substance field or inheritance
  exception was introduced.
- Actual source corrections and predecessor history are recorded separately
  from this Plan.
