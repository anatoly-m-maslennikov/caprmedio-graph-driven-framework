---
atom_id: CA-C-610
ref_id: CA-C-610
container:
  scope_unit: CA-SU-00
role: Concern
form: Question
topics:
  main_subject: 'Entity/Aspect/Product: CAPRMEDIO Framework'
tier: 3
status: Active
version: 1
updated_at: 2026-10-29 08:44:43 +0400
carrier_destination:
  file:
    name: CA-C-610-CAPRMEDIO-QUESTION--which-runtime-owns-automatic-context-initialization.md
    path: .caprmedio_caprmedio/01_concern
current_scope_unit: caprmedio
author: Anatoly Maslennikov
---
## Summary

Which Runtime owns automatic context initialization?

## Question

Should the chosen continuation below be changed after the remaining uncertainty is resolved?

## Details

Preserve legacy REQU-507's automatic session/context initialization commitment as a framework outcome, rather than dropping it for a malformed header. Use the existing Runtime/Session vocabulary and leave its concrete implementation owner to the later Engine Epic. This does not add a Session Engine entity or implement startup code.

The latest 48 hours and Current sources do not settle the remaining detail. The Operator authorized choosing the best-supported continuation, recording a Question, and continuing CA-P-2683. Tracked with the latest candidate in CA-A-1305.
