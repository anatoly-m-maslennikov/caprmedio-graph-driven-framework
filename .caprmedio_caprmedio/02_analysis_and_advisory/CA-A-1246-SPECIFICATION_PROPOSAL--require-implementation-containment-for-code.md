---
atom_id: CA-A-1246
ref_id: CA-A-1246
container:
  scope_unit: CA-SU-00
role: Analysis & Advisory
form: Specification Proposal
topics:
  main_subject: Formal Model
tier: 3
status: Active
version: 2
updated_at: 2026-11-02 15:49:28 +0400
carrier_destination:
  file:
    name: CA-A-1246-CAPRMEDIO-SPECIFICATION_PROPOSAL--require-implementation-containment-for-code.md
    path: .caprmedio_caprmedio/02_analysis_and_advisory
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
author: Anatoly Maslennikov
---
# Summary

Require Implementation containment for Code

## Decision

The Operator states that Code does not exist outside Implementation. Code must be declared as a structural part under Implementation, not independently under Continuant. Its Continuant classification can remain a reference to that same declaration, without granting independent existence.

The proposed construction is Implementation > Code > Module, Unit, Asset. The Operator describes Asset as every non-executable file. The Asset population boundary is being clarified against logical Implementation content versus all files including Atom/configuration/Journal Carriers. Unit's exact meaning and the disposition of earlier Function/Class/Package/Tool kinds still need evidenced mapping. Do not invent those mappings or publish a complete Code definition from this partial proposal.

Independent Module existence outside Package remains distinct from the new requirement that Code belongs to Implementation. A parent-kind requirement is not waived by an independent option relative to some other container kind.

## State

Required Implementation ownership is decided. The Code-part refinement is being drafted, with unresolved meanings held explicitly. CA-A-1239 is the candidate view; no Current source, code file or runtime is moved.
