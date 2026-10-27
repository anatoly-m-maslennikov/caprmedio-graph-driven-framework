---
atom_id: CA-P-2651@1
content_role: Plan
type: Plan
label: Task
work_sequence_number: 12
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
status: Archived
subjects:
  governs: Subject
version: 1
updated_at: 2026-10-26 05:17:30 +0400
relations:
  IS_CONTAINED_BY:
  - CA-P-2639
tier: 4
---
# Summary

Remove retired generic property Subjects

## Objective

Correct I05's false or retired Subject targets without deleting useful rules.

## Details

Estimated own work: up to 15 minutes. Follow P2642/P2643 for Claim meaning.

- Read Current D478/D480/D485, R1454 and O045's relevant header/content.
- Broad property-storage policies can govern Atom, with their precise boundary
  in Content Scope. Do not create an Atom.Property-valued field.
- Replace old generic Atom.Substance references with the actual governed thing,
  role-specific content/Claim or appropriate broader Subject, according to
  the source's meaning and the accepted representation choices.
- Correct accidental Atom.Atom/Tier paths to the existing canonical Atom.Tier
  path where the source clearly concerns numeric Tier.
- Do not blindly replace every occurrence with one field or revive Substance.
  Preserve actual obligations and distinguish source correction from Terms work.
- Preserve existing Drafts/Archives and unrelated sources; create normal
  predecessors for Current changes and record bounded readback.
- Split concrete uncertain mappings out for the Operator rather than guessing.

## Definition of Done

- The completed batch does not govern an invented Atom.Property field or
  revive generic Atom.Substance.
- Tier and Claim references match the intended current meanings.
- Useful storage and applicability obligations are preserved.
- No Terms Graph implementation, runtime change or unrelated content sweep
  was included.
