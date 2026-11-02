---
atom_id: CA-A-1313@2
content_role: Analysis
type: Spec Proposal
current_scope_unit: caprmedio
status: Archived
author: Anatoly Maslennikov
tier: 3
version: 2
updated_at: 2026-10-29 21:18:38 +0400
subjects:
  governs: Entity/Object/Continuant/Structural Unit/Scope Unit
relations: {}
---
## Summary

Keep Goals outside and define Scope Contracts inside each Scope Unit

## Proposal

A Scope Unit is a unit of responsibility. Its external Goal states what its parent requires it to achieve; its internal Scope Contract states its foundational commitments. Ordinary Goals are owned by the parent Scope Unit and target the child. The Project retains its external Operator-owned Project Goal; the Operator is an Actor, not a Scope Unit.

Scope Contract is the optional readable Tier Label for numeric Tier 0, not an Atom Type or the separate Atom.Label property. Tier 1 is Core, Tier 2 General, Tier 3 Standard and Tier 4 Detail; numbers 5 and above remain valid without predefined names. Local foundational Atoms keep their own Content Roles and Types: an Operations Atom can remain a Workflow, Action or Step, a Method an Eng Policy or Eng Decision, and so on. Their combined contribution forms the unit's Scope Contract: required outcomes and boundaries (R), methods and policies (M), evaluation commitments (E), delivery commitments (D), and foundational operations (O). No unit is required to populate all five Roles.

Tier 1 and above specializes or realizes the contract. Project Principles become the Project's Scope Contract under the same general pattern; Principle is retired as a separate governing concept and Tier-0 label. This replaces the previous Project-only Tier-0 interpretation and the trial's R-only Scope Definition replacement for Goal. Goal remains; it is not globally retired.

Tier Labels do not grant additional conflict precedence or change applicable governing relation ordering. Review existing Principles, Goals and Core Atoms by complete meaning. Convert suitable existing local Goals and promote suitable Core commitments into Scope Contracts; retain genuinely external expectations as Goals. Do not blindly retype every Tier-0 or Tier-1 Atom, copy external Goals into an identical internal Claim, or promote technical details merely because they are reusable. Keep each contribution coherent enough for one concise Summary. Related statements may stay together. The 70/100-character trial has not adopted a new hard Summary limit.

## Adoption

Accepted direction from the Operator. P2701 prepares concrete Drafts and a thin source-to-Draft trace, resolves conflicts and coordinates retirement/replacement before publication. Existing Current sources remain authoritative until the reviewed successors are adopted. Unknown scopes/targets, conflicting authority and unresolved meaning stay explicit; no new Scope Units are invented. No code, runtime, release or Engine implementation change is included.

## Supersedes

The P2700 trial's R-only Scope Definition / Goal-retirement direction is superseded. Its 100-source review and unpromoted Drafts remain evidence, not an adoption batch. Reuse their useful content only after checking it against this decision. The earlier suggestion that the Scope Contract must be exactly one R is not retained. The brief proposal to introduce five RMEDO Scope Contract Types is superseded by the simpler Tier Label model; none of those Type definitions is to be adopted.
