---
atom_id: CA-A-1246
content_role: Analysis
type: Specification Proposal
current_scope_unit: caprmedio
claim_target_scope_unit: caprmedio
status: Active
author: Anatoly Maslennikov
subjects:
  governs: Formal Model
version: 1
updated_at: 2026-10-28 20:15:34 +0400
relations: {}
tier: 3
---
# Summary

Require Implementation containment for Code

## Decision

The Operator states that Code does not exist outside Implementation. Code must be declared as a structural part under Implementation, not independently under Continuant. Its Continuant classification can remain a reference to that same declaration, without granting independent existence.

The proposed construction is Implementation > Code > Module, Unit, Asset. The Operator describes Asset as every non-executable file. The Asset population boundary is being clarified against logical Implementation content versus all files including Atom/configuration/Journal Carriers. Unit's exact meaning and the disposition of earlier Function/Class/Package/Tool kinds still need evidenced mapping. Do not invent those mappings or publish a complete Code definition from this partial proposal.

Independent Module existence outside Package remains distinct from the new requirement that Code belongs to Implementation. A parent-kind requirement is not waived by an independent option relative to some other container kind.

## State

Required Implementation ownership is decided. The Code-part refinement is being drafted, with unresolved meanings held explicitly. CA-A-1239 is the candidate view; no Current source, code file or runtime is moved.
