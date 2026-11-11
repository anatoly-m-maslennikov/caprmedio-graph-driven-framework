---
atom_id: CA-C-625
current_scope_unit: caprmedio
status: Active
subjects:
  active: Projection/(.Form := Applicable Methodology)
version: 1
relations: {}
tier: 3
role: Concern
form: Question
updated_at: 2026-11-02 08:06:47 +0400
---

## Summary

Identify Applicable Methodology members

## Question

How should Applicable Methodology identify its projected members without introducing an undeclared Member Property?

## Details

Working choice: preserve each projected member’s exact source Atom Version and the required direct source binding in the Projection’s applicable Rules and Delivery. Treat output members and selected input sources as distinct concepts; do not assume that Projection.Source.Atoms is the output-member collection.

Impact: member identity, source traceability and projected Carrier representation. Existing per-member requirements remain in force.

Continue with this working choice. This Question records uncertainty and is not an approval gate.
