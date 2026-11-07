## Summary

Introduce Scope Delegation and policy Forms

## Proposal

Keep Scope Unit as the structural name. Separate its external delegation from its internal definition. Each Atom has one Role and one Main Subject.

This proposal remains a Draft. The selected MODEL source packet was reviewed and promoted on 2026-11-07. Instance migration, implementation compatibility, installed outputs and projections remain separate Epic stages.

## Outside: Scope Delegation

Each non-Project Scope Unit within the Project has one external Scope Delegation Atom. It combines the proposed Scope Unit Declaration with the delegated responsibility. Its Role is one of RMEDO.

- Main Subject identifies the receiving Scope Unit.
- Container identifies the receiving unit’s direct containing Scope Unit. Only that Scope Unit owns the delegation.
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

Local R defaults are Requirement and existing Declaration families. M and D default to Decision; E includes Decision and Eval Case; O includes Decision, Workflow, Step and Action. Scope Delegation is admitted by default in every containing unit, including Project. Solution, Direct Policy and Approach Policy require explicit local admission. These three Forms allow RMEDO; Decision allows MEDO.

Role follows the contribution. Create, Copy and Remove can receive R contributions; internal DB/File adapters can receive M contributions. E delegation is for purely testing-support Scope Units, such as mock adapters or test-data providers. D covers delivery contributions. O covers operational duties.

The Project retains its R/Goal and root Axioms. The one-per-unit Scope Delegation rule excludes Project and the predefined external world. Project has one R/Scope Unit Declaration; its Declaration is contained by world. This Project uses CA-SU-00 for Project and CA-SU--1 for predefined world. It introduces no M/E/D/O Goal Forms or separate Target Scope Unit field.

## Inside: Tier and Forms

Tier 0 defines the Scope Unit internally. Form and Tier remain separate: Solution, Direct Policy, Approach Policy and Decision have no mandatory Tier. An Atom receives its Tier from its actual contribution under the admitted Tier rules.

A Solution specifies the contribution that realizes the current Scope Unit’s responsibility across the unit and its descendants. Its Role identifies the contribution. Its Main Subject is that Scope Unit. Its Container is inside that unit. Solutions are admitted under RMEDO; each Atom retains one Role.

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

A Solution can govern the Scope Unit as a whole. A Policy can govern an Aspect or a narrower topic. Policy Subjects follow their actual governed topic and the admitted scope whitelist.

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

## Project Package — separate change

The separate accepted rename is Implementation to Project Package. It is outside this model-adoption stage.

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

## Companion Atom Drafts and source adoption

The following Drafts were reviewed and consumed by manual source promotion. Current references use the unversioned ID; Version is listed separately.

- CA-R-2999@1-draft → CA-R-2999, Current Version 2.
- CA-R-3000@1-draft → CA-R-3000, Current Version 2.
- CA-R-3001@1-draft → CA-R-3001, Current Version 2.
- CA-R-2707@3-draft → CA-R-2707, Current Version 4.
- CA-E-661@6-draft → CA-E-661, Current Version 7.
- CA-R-2508@9-draft → CA-R-2508, Current Version 10.
- CA-R-2512@3-draft → CA-R-2512, Current Version 4.
- CA-R-2513@3-draft → CA-R-2513, Current Version 4.
- CA-R-2514@3-draft → CA-R-2514, Current Version 4.
- CA-R-2515@3-draft → CA-R-2515, Current Version 4.
- CA-R-2463@3-draft → CA-R-2463, Current Version 4.
- CA-R-3002@1-draft → CA-R-3002, Current Version 2.
- CA-R-3003@1-draft → CA-R-3003, Current Version 2.
- CA-R-3004@1-draft → CA-R-3004, Current Version 2.
- CA-R-3005@1-draft → CA-R-3005, Current Version 2.
- CA-R-1565@22-draft → CA-R-1565, Current Version 23.
- CA-M-314@25-draft → CA-M-314, Current Version 26.
- CA-D-457@27-draft → CA-D-457, Current Version 28.
- CA-R-3006@1-draft → CA-R-3006, Current Version 2.
- CA-R-3007@1-draft → CA-R-3007, Current Version 2.
- CA-R-3008@1-draft → CA-R-3008, Current Version 2.
- CA-R-924@38-draft → CA-R-924, Current Version 39.
- CA-M-507@1-draft → CA-M-507, Current Version 2.
- CA-R-2524@5-draft → CA-R-2524, Current Version 6.
- CA-R-2526@5-draft → CA-R-2526, Current Version 6.
- CA-R-1671@29-draft → CA-R-1671, Current Version 30.
- CA-R-1672@29-draft → CA-R-1672, Current Version 30.
- CA-R-1768@31-draft → CA-R-1768, Current Version 32.
- CA-E-445@29-draft → CA-E-445, Current Version 30.
- CA-D-404@29-draft → CA-D-404, Current Version 30.
- CA-R-1669@29-draft → CA-R-1669, Current Version 30.
- CA-R-947@42-draft → CA-R-947, Current Version 43.
- CA-D-402@28-draft → CA-D-402, Current Version 29.
- CA-D-442@28-draft → CA-D-442, Current Version 29.
- CA-R-2689@2-draft → CA-R-2689, Current Version 3.
- CA-R-2690@2-draft → CA-R-2690, Current Version 3.
- CA-E-670@3-draft → CA-E-670, Current Version 4.
- CA-D-669@3-draft → CA-D-669, Current Version 4.
- CA-E-006@41-draft → CA-E-006, Current Version 42.
- CA-E-621@38-draft → CA-E-621, Current Version 39.
- CA-E-672@2-draft → CA-E-672, Current Version 3.
- CA-D-670@2-draft → CA-D-670, Current Version 3.
- CA-D-666@2-draft → CA-D-666, Current Version 3.
- CA-D-667@3-draft → CA-D-667, Current Version 4.
- CA-D-671@2-draft → CA-D-671, Current Version 3.
- CA-E-671@2-draft → CA-E-671, Current Version 3.

## Remaining Epic work

Model choices for this packet are settled. The remaining work is instance mapping and migration, consumer compatibility and projection verification. Project Package naming and pre-existing Structural Level and legacy Settings reconciliation remain separate.
