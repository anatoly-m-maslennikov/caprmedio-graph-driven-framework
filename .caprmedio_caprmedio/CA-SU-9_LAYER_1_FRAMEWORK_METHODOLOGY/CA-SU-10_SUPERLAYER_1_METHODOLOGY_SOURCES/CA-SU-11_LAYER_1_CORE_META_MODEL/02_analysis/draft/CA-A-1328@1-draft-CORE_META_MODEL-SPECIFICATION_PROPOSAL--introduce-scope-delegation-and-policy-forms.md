---
atom_id: CA-A-1328
ref_id: CA-A-1328@1-draft
container:
  scope_unit: CA-SU-11
role: Analysis
form: Specification Proposal
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom
  dependencies:
  - CAPRMEDIO_MODEL <+ Scope Unit
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation//SPECIALIZES
tier: 3
status: Draft
version: 1
updated_at: "2026-11-07 01:16:12 +0400"
carrier_destination:
  file:
    name: CA-A-1328@1-draft-CORE_META_MODEL-SPECIFICATION_PROPOSAL--introduce-scope-delegation-and-policy-forms.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/02_analysis/draft
---

## Summary

Introduce Scope Delegation and policy Forms

## Proposal

Keep Scope Unit as the structural name. Separate its external delegation from its internal definition. Each Atom has one Role and one Main Subject.

This is a Draft proposal. Current Atoms, implementation and runtime remain unchanged until adoption.

## Outside: Scope Delegation

Each non-Project Scope Unit has one external Scope Delegation Atom. It combines the proposed Scope Unit Declaration with the delegated responsibility. Its Role is one of RMEDO.

- Main Subject identifies the receiving Scope Unit.
- Container identifies the external defining context.
- The delegating Scope Unit retains its overall scope and accountability.
- The receiving Scope Unit is responsible for its delegated contribution.

The Declaration carries:

- Name and ID.
- Ordered or unordered state.
- Order Number when ordered.
- Formal whitelists for Main Subject branches, Roles and Forms.

The Declaration's Role determines the permitted local RMEDO Roles:

| Declaration Role | Permitted local Roles |
| --- | --- |
| Requirement | Requirement, Method, Evaluation, Delivery, Operations |
| Method | Method |
| Evaluation | Evaluation |
| Delivery | Delivery |
| Operations | Operations |

These are permissions. They require no complete RMEDO packet. Applicable inherited constraints continue to govern the unit.

Default Forms are the Role's local Forms or analogs. Eval Case, Workflow, Step and Action are included. Rename Local Decision to Decision. Solution and Policies require explicit admission in the Scope Delegation.

The exact default R Form names and the default admission of child Scope Delegations remain open.

Role follows the contribution. Create, Copy and Remove can receive R contributions; internal DB/File adapters can receive M contributions. E delegation is for purely testing-support Scope Units, such as mock adapters or test-data providers. D covers delivery contributions. O covers operational duties.

The Project retains its R/Goal and root Axioms. The proposed one-per-unit Scope Delegation rule excludes Project. It introduces no M/E/D/O Goal Forms or separate Target Scope Unit field.

## Inside: Tier and Forms

Tier 0 defines the Scope Unit internally. Form and Tier remain separate: Solution, Direct Policy, Approach Policy and Decision have no mandatory Tier. An Atom receives its Tier from its actual contribution under the admitted Tier rules.

A Solution states how the current Scope Unit fulfills its responsibility, including its descendants. Its Main Subject is that Scope Unit. Its Container is inside that unit. Solutions are admitted under RMEDO; each Atom retains one Role.

| Form | Meaning |
| --- | --- |
| Solution | The solution for the current Scope Unit, including its descendants |
| Direct Policy | A rule applied directly to all descendants recursively |
| Approach Policy | An approach for particular cases, adopted through a local Atom where the case occurs |
| Decision | A particular choice within the Scope Unit |

Eval Case, Workflow, Step and Action retain their distinct meanings. Operations duty and executable Workflow/Action bindings remain separate.

Scope Contract is dropped from the proposed system. Architectural Decision, Architectural Solution, Primary Solution and General Solution are not separate Forms in this proposal.

A Scope Unit retains its own realization while delegating other contributions. Shared integration tests, CI/CD, composition and common code can belong to the containing unit. Having descendants does not impose a leaf-only realization rule.

## Policies and local adoption

A Direct Policy applies throughout the descendant subtree. It needs no local copy. Genuine SPECIALIZES Atoms can add applicable detail while preserving its constraints.

An Approach Policy states the case and prescribed approach. The containing unit need not enumerate which descendants will encounter that case. Each applicable descendant supplies a local Atom binding the approach to its actual case through SPECIALIZES. Additional Tool-specific rules are optional; a reference alone is insufficient.

For async work:

- R states when async is required and the blocking limits.
- M states the engineering approach.
- E states the checks and acceptance criteria.
- D states the representation and delivery requirements.

A Solution can govern the Scope Unit as a whole. A Policy can govern an Aspect or a narrower topic. Whether Policies must use Aspect Subjects remains open.

Independent Decisions remain valid. Applicable governing constraints continue to apply. SPECIALIZES adds scope, case binding or stricter detail; its links follow the admitted authority and Relation rules.

## Mechanical gathering

Start from an admitted source frontier, the receiving Scope Unit, its Scope Delegation and its case facts.

1. Select admitted local Atoms and applicable inherited constraints.
2. Include Direct Policies from the containing ancestry, recursively.
3. Evaluate each Approach Policy's case.
4. For a matching case, include the Policy and require its local specialization.
5. Retain applicable governing parents alongside their specializers.
6. Report missing bindings, conflicts and unresolved conditions.

A false case excludes the Approach Policy with a reason. An unknown case remains unresolved. A missing local binding is a gap in an applicable Policy; it does not remove that Policy.

Keep source ID, Version, hash, defining Scope, target context and relevant applicability/binding evidence. Gathering specifications does not establish implementation or a passed Evaluation. The proposed resolver is separate from the current compiler.

## Project, Product and Roles

Product sits under Project. A Project is itself a how toward a higher goal; here, toward the Product. Its local RMED meanings remain clear across Subject branches:

| Role | Project meaning |
| --- | --- |
| Requirement | Required behavior, properties, constraints and value across Aspects |
| Method | How we achieve it, including domain and engineering solutions |
| Evaluation | How we check it |
| Delivery | How we deliver it |

Role and Topic are independent. Engineering Requirements can constrain performance; Evaluation Requirements can constrain defect escapes or review rework; Delivery Requirements can constrain delivery failures, artifact correctness or delivery time. Required targets belong in R; observed measures are evidence. A how-fast question can specify a Requirement rather than a Method.

One Solution can supply constraints or inputs for another Solution. A domain Method can provide the how for a Product requirement and the what for an Engineering Method. That dependency changes neither Atom's Role. Role is interpreted within the Project; position in the realization chain alone determines neither Role nor Tier.

## Purpose traceability

Use CONTRIBUTES_TO as the shared Relation for a contribution toward another contribution. It applies across Roles and Forms.

Ideally, each RMEDO Solution, Policy or Decision links to an existing R that explains its purpose. This is optional authoring guidance. Missing links leave an Atom valid; create an R for its actual required contribution, rather than merely to fill a link.

CONTRIBUTES_TO expresses contribution. Evaluation and implementation evidence establish satisfaction of a Requirement. The preferred R target in this guidance does not restrict the general Relation to R targets.

## Project Package

Rename the structural root Package from Implementation to Project Package.

- Implementation remains the Role name.
- Project Package is the Project's root Package.
- Package, Module and Code Unit retain their structural meanings.

## Rationale

The model keeps one Role per Atom. External delegation states responsibility and boundaries. Internal Tier-0 Atoms define the unit. Forms describe contributions independently of Tier.

A unit keeps accountability for its full scope, including delegated parts. This supports both direct realization and descendant work. Direct and Approach Policies expose different adoption obligations for mechanical gathering.

## Source impact and transition

Review these Current authorities before adoption:

- R924 and R926: Project Goals and the replacement of non-Project Goals.
- R2424: replace the old Scope Contract system with Tier/Form separation.
- R2684 and R2688: consolidate external Scope Unit declaration and delegation, including identity and cardinality.
- R2512-R2515 and the Operations authorities: Role meanings and admitted Forms.
- R1767 and R2123: Policy/Decision names, propagation and Form admission.
- R1671: independent Decisions.
- R2766 and R2149: specialization, Tier and governing-Relation direction.
- R2553 and R2173: Project Package naming.

Current obligations remain Current until coordinated successors are adopted. Classify legacy Atoms by Claim. Preserve their identity and history under the admitted rules. Do not mechanically rename every existing Goal or Policy into a new Form.

## Companion Atom Drafts

Prepared Role Semantics updates:

- CA-R-2512@3-draft: Requirement Declaration.
- CA-R-2513@3-draft: Method Declaration.
- CA-R-2514@3-draft: Evaluation Declaration.
- CA-R-2515@3-draft: Delivery Declaration.
- CA-R-2463@3-draft: Operations Declaration.

Four successor Drafts were created; the existing Operations Draft was updated. Current Declarations remain unchanged.

Other follow-up Drafts must declare the Forms, external identity/whitelists, Tier rules, CONTRIBUTES_TO, adoption checks and delivery rules. Add their IDs when those Drafts exist.

## Open decisions

- Scope Delegation Tier and authorized external allocator reach.
- Exact default local R Forms and admission of child Scope Delegations.
- Counts of internal Atoms; no complete per-Role packet is required.
- Exact count, placement and case coverage of required Approach bindings.
- Policy Subject restrictions and remaining Role/Form admission details.
- Legacy identity, Tier and Relation migration details.
