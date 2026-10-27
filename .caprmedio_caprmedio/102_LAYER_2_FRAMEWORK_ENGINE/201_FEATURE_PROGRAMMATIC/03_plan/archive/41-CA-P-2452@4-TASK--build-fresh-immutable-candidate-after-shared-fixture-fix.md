---
atom_id: CA-P-2452@4
content_role: Plan
type: Plan
label: Task
work_sequence_number: 41
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Subject/Domain/Node/Continuant/Atom
  depends_on:
  - CA-P-2450
relations:
  is_decomposition_of:
  - CA-P-2401
version: 4
updated_at: 2026-10-24 08:06:50 +0400
tier: 3
---
# Summary

Build a fresh immutable candidate after the shared fixture fix

## Objective

Build one fresh immutable candidate from the current source after CA-P-2450's bounded shared-fixture repair, and record exact source and image provenance for the next isolated gate.

## Details

After CA-P-2450 is accepted, use the current checkout and its approved source/fixture inputs to produce a fresh candidate. Record the exact source fingerprint, image digest, build receipt, and preserved production/rollback identity. Do not reuse the superseded candidate, replay the interrupted batch, or change production. Preserve CA-P-2438 and CA-P-2439 as valid historical acceptance records; do not rewrite their claims.

At most15minutes ownwork, split before extending. Preserve concurrent edits and exact source/image provenance. No production replacement, public release, Git mutation, or historical replay is authorized by this preparation Task.

### Definition of Done

A fresh immutable candidate is built from the repaired current source with exact source/image provenance and a reproducible receipt, while protected production state is unchanged. This narrow Task does not claim isolated-case success, deployment acceptance, or release completion.

### Completion checkpoint

Admission receipt `.caprmedio_tmp/mcp-audit-20261020/isolation/execute/p2410-20261020T142943Z-563bd764/admission-receipt.json` records the fresh candidate image `febd5bcc189e3eda2b4926206beb23f26d26c7757092580b0ddf56705ac0aac9`, source fingerprint `b71c2770aef150235984df90e4e0984e17d2b7e8d7a8169ac8de15b3763a15b8`, and a passing production guard. This closes the bounded candidate-build task only; isolated public-case, deployment, and full-release acceptance remain separate gates.
