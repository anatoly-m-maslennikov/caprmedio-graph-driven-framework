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
updated_at: "2026-11-06 23:03:24 +0400"
carrier_destination:
  file:
    name: CA-A-1328@1-draft-CORE_META_MODEL-SPECIFICATION_PROPOSAL--introduce-scope-delegation-and-policy-forms.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/02_analysis/draft
---

## Summary

Introduce Scope Delegation and policy Forms

## Proposal

Keep **Scope Unit** as the structural name. Introduce **Scope Delegation** as a shared Form under Requirement, Method, Evaluation, Delivery and Operations.

This proposal records the latest design decisions. It prepares a semantic change; adoption, companion Atom drafting, implementation and data migration remain separate work.

## Form system

| Form | Roles | Meaning |
| --- | --- | --- |
| Scope Delegation | R, M, E, D, O | Responsibility delegated to a target Scope Unit; the delegator retains overall Scope and accountability |
| Architectural Decision | R, M, E, D | A Tier-0 architectural commitment made in the containing Scope Unit and delegated to descendants |
| Direct Policy | R, M, E, D | A reusable policy that applies where its conditions match, without requiring a local copy |
| Approach Policy | R, M, E, D | A reusable conditional approach requiring a local case-binding specialization where its case occurs |
| Goal | R | The Project-level desired result |

Local Decision remains the proposed name for concrete local M/D choices. Existing E/Eval Case and appropriate local R Forms remain distinct. Their precise admission and legacy-name mapping require the follow-up declaration work.

Shared Form names have one shared meaning. The Role identifies the contribution. Each allowed Role/Form combination needs explicit admission; this table does not create every possible combination.

## RMEDO/Scope Delegation

A Scope Delegation defines responsibility delegated by a delegating Scope Unit to a target Scope Unit. Its Atom is authored outside the target unit. The delegator retains overall Scope and accountability; delegation does not transfer or relinquish either.

- Main Subject identifies the target Scope Unit itself.
- Container identifies the authorized external delegating context. Resolve the delegating Scope Unit through its Container chain when needed.
- Role identifies the contribution's nature.
- The Subject has no added Engineering, Method or other Role branch.
- The existing Main Subject supplies the target; no separate Target Scope Unit field is introduced.

| Classification | Delegated contribution |
| --- | --- |
| R/Scope Delegation | Required outcomes, capabilities and functional boundaries; examples: Create, Copy and Remove |
| M/Scope Delegation | Full engineering work, methods and architecture; examples: DB adapter and File adapter |
| E/Scope Delegation | A Scope Unit whose contribution exists purely for testing: mock adapters, fixtures or synthetic/obfuscated test data |
| D/Scope Delegation | Representation and delivery; example: packaging and publishing CI/CD artifacts |
| O/Scope Delegation | Operational duties; example: executing CI/CD pipelines |

The Claim determines the Role. CI/CD can have distinct D/Scope Delegation and O/Scope Delegation contributions. An adapter can have M/Scope Delegation without an artificial business R/Goal. Internal R constraints still apply. User-facing performance requirements are checked end to end; adapter measurements support technical budgets and diagnosis.

E/Scope Delegation is narrower than Evaluation generally. Production Tools can have E Policies and Eval Cases without an E/Scope Delegation. M Atoms can still describe the engineering realization of a testing component.

O/Scope Delegation delegates operational duty. Execution remains described by the admitted Workflow, Step and Action Forms; Role Operations alone supplies no executable binding.

Scope Delegation replaces the proposed Responsibility, Engineering Goal and Scope Form names. Structural R/Scope Unit Declaration continues to define identity and structure. Scope Delegation specifies the delegated contribution and boundaries. Structural identity remains with Scope Unit Declaration.

## Project root and external definition

The Project retains its R/Goal and root Axioms. Goal is not replicated under M, E, D or O, or mechanically assigned to every descendant Scope Unit.

Use the appropriate Scope Delegation when a contribution is delegated to another unit. A unit needs no artificial R contribution merely because its actual responsibility is engineering, testing, delivery or operations.

The structure is partially fractal: a unit receives its governing delegation from outside, then organizes realization and any further delegation inside. The Project's Goal and Axioms remain the root distinction.

## Architectural Decisions

An Architectural Decision is Tier 0 in the Scope Unit where the decision is made. Each Scope Unit can have zero or more Architectural Decisions independently for each RMED Role. No complete four-Role packet is required.

An Architectural Decision states a general architectural contribution for descendants. A Scope Delegation Atom states delegated responsibility. A local Decision states a concrete choice. These meanings remain distinct.

The resulting flow is:

```text
TOOLS: Tier-0 Architectural Decision
-> Scope Delegation Atoms for descendants, defined outside those descendants
-> Atoms that realize the delegated contributions
```

There is no mandatory intermediate descendant Goal or extra Scope Contract stage. Descendants can make further Architectural Decisions and repeat the delegation pattern.

## Direct and Approach Policies

Both kinds can be conditional. Their difference is the requirement for a local binding.

A Direct Policy applies when its condition matches. Coding style is an example. A descendant implements the applicable constraints without creating an Atom merely to copy them. A genuine optional specialization remains possible.

An Approach Policy names a case and prescribes what or how to handle it. The parent need not know which Tools will encounter the case. Each matching Scope Unit supplies a local Atom binding the Policy to its concrete cases through SPECIALIZES.

That local Claim states the concrete scope/case and its application of the prescribed contribution. Additional Tool-specific rules are optional. A reference alone is insufficient.

For async work:

- R/Approach Policy states when async is required and the synchronous blocking limits.
- M/Approach Policy states the prescribed queue, orchestration or other engineering approach.
- E/Approach Policy states checks and acceptance criteria.
- D/Approach Policy states the required representation of operation state and results.

A concrete choice can be a Local Decision or an Architectural Decision with further delegation, according to its contribution. Independent local Decisions remain valid and obey all applicable constraints.

SPECIALIZES preserves the parent's applicable constraints. It adds concrete scope, case binding or stricter detail. Specialization supplies no automatic permission to weaken a parent or discard it. Local governing links point upward where the declared Relation and authority rules permit; this proposal invents no stored downward governing edges.

## Mechanical gathering

Resolve each Tool from a selected authoritative source frontier, its declared Scope context and its case facts. Use Formal Claims and declared facts rather than Form names or directory names alone.

Keep applicability and completion separate:

| Condition result | Direct Policy | Approach Policy |
| --- | --- | --- |
| True | Applicable; no mandatory local copy | Applicable; require local specialization covering the case |
| False | Excluded with the reason | Excluded with the reason |
| Unknown | Unresolved | Unresolved |

A missing required specialization is a gap in an applicable Approach Policy. It does not make that Policy inapplicable or turn it into a Direct Policy. Conflicting bindings remain conflicts.

Gather applicable shared policies, local Scope Delegations and local specifications. Retain applicable parents alongside their specializers. Check required case coverage, identify independent local contributions and report gaps and conflicts. Inclusion does not prove implementation or a passed Evaluation.

Each result preserves source ID, Version, source hash, defining Scope, target context, condition result and relevant specialization links. Evaluation outcomes are resolver evidence, not a new stored three-valued Boolean Property.

The current Applicable Methodology compiler does not implement this Scope-and-case resolution. Its existing source selection, conflict handling and publication are separate from the proposed mechanism.

## Rationale

The design follows the user's examples: user-facing Create/Copy/Remove capabilities, internal DB/File adapters, dedicated testing assets and CI/CD delivery/operations.

Scope Delegation captures delegated contributions without forcing M -> R/Goal -> M conversions. Roles distinguish outcomes, engineering, evaluation, delivery and operations while the Subject remains the Scope Unit. Direct and Approach Policies expose the local-binding obligation needed for mechanical gathering. Architectural Decisions retain their coordination role.

## Source impact and transition

Review the Current authorities before adoption:

- R924 and R926: Goal classifications, external definition and non-Project Goals.
- R2424 and R2684: old Scope Contracts and structural Scope Unit Declarations.
- R2512-R2515 and the Operations definition: Role meaning and Scope Delegation Form admission.
- R1767 and R2123: existing Policy/Decision Forms, propagation and ownership rules.
- R1671: preserve independent local Decisions.
- R2766 and R2149: specialization, Tier and governing-Relation direction.

R926 still requires non-Project Goals until a coordinated successor is adopted. This proposal replaces that model with Scope Delegations. Decide replacement coverage and cardinality before adoption.

Classify legacy Atoms by contribution. Do not bulk-rename every Goal, Eng Policy, Eval Policy or Decision. Preserve distinct Claims and exact history. Apply the admitted identity rules when Role, Summary or contribution changes. Admit and review the new definitions before migration or runtime handoff.

## Companion Atom Drafts

None created by this request. Follow-up work covers Form admissions, Scope Delegation placement and targeting, Project Goal boundaries, required case binding, applicability resolution and the affected evaluations/delivery rules. Allocate IDs when those Drafts are created.

## Open decisions

- Scope Delegation Atom Tier and cardinality.
- Whether only the direct containing Scope Unit can delegate scope, or other authorized external Scope Units can also delegate it.
- Whether the Project also needs Scope Delegation Atoms alongside its Goal and Axioms.
- The exact count, placement and case coverage of required local bindings. A binding is already mandatory when an Approach Policy case matches.
- Exact legacy M/D Form renames and local Form admissions.
- Policy ownership at leaf Scope Units.
- Operations Forms beyond Scope Delegation.
- Consistent Tier and Relation rules for external delegation and internal realization.

These remain explicit adoption questions. This proposal assigns no defaults to them.
