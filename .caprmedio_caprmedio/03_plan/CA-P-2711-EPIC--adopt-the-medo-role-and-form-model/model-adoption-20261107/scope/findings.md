# Scope Delegation proposal findings

Analysis only. Source pins and rationale are in `drafts.json`; exact body-only candidates are in `ready-candidates.json`.

## Proposed model

- Define one generic `Scope Delegation` Form with a bound-instance Role whitelist for RMEDO: Requirement, Method, Evaluation, Delivery and Operations. Do not create a separate Form declaration for each Role. The Form is admitted in every containing Scope Unit, including Project, so Project can declare children. Only the receiving Scope Unit must be non-Project.
- Each non-Project Scope Unit has exactly one external Scope Delegation. Its Main Subject identifies the receiving Scope Unit. Its Container resolves to that Scope Unit’s one direct declared structural Parent; that direct containing Scope Unit is the allocator. Project has no incoming Scope Delegation and no structural Parent.
- The Scope Delegation carries existing Name, ID, ordered state, optional Label, conditional `order.number` and direct Parent values. It records the assigned contribution while the delegator retains its full scope and accountability. It creates no duplicate target field, Scope Contract, Goal, or stored whitelist Property.
- Each concrete Scope Delegation Claim lists permitted local `HAS_ACTIVE_SUBJECT` target selections and local Role/Form pairs. A local Atom must be contained by the receiving Scope Unit through its `Header.Container`-derived `IS_CONTAINED_BY` link, and its resolved subject target and Role/Form pair must be admitted. This uses existing entity/instance endpoint selectors rather than string-prefix matching.
- Local Requirement defaults are Requirement for outcomes and constraints and existing Declaration families for model definitions. No new Rule Form is introduced; legacy Rule instance mapping is separate. Solution, Direct Policy and Approach Policy permit RMEDO; Decision permits MEDO only. Eval Case, Workflow, Step and Action remain available under their established Roles. No mandatory Role packet is imposed.
- Keep a separate Project-only `Scope Unit Declaration` Form owner so retiring R2684 does not remove the Project root’s Form. Its bound instance is Requirement/Scope Unit Declaration and its `HAS_ACTIVE_SUBJECT` target is `Scope Unit/Project`. The cardinality Requirement, not this Form owner, requires exactly one root declaration.

## Source changes proposed

- Replace CA-R-2684@1’s generic Scope Unit Declaration Form ownership with two distinct Requirement/Declaration Form owners: generic Scope Delegation with one RMEDO whitelist, and Project-only Scope Unit Declaration. Retire R2684 only after both owners are admitted.
- Replace CA-R-2688@2 and CA-R-926@39 with a new Requirement/Requirement constraint requiring one Scope Delegation per non-Project Scope Unit, retaining the single Project-root Declaration and project-level Goal/Axioms. Scope Unit and Atom canonical owners remain R2523 and R2508.
- Reclassify CA-R-924 as Requirement/Requirement, preserving its ID and Summary, and add the five Role/Scope Delegation relational classifications. Preserve its Plan Claim-target qualification.
- Supersede CA-M-461 with general Method/Direct Policy authoring guidance. Method is permitted under both historical shared Role range candidates, so this source change does not depend on that choice and requires no local adoption Atom.
- CA-R-2526@4 permits Project ID zero. Its same-ID/Summary successor requires exactly one stable ID for every Scope Unit. CA-R-2524@3 also explicitly prohibits a Project ID; its same-ID/Summary successor removes only that prohibition and leaves cardinality to R2526. This is a model-authority change. The approved `CA-SU-00` value in R2640@2 and Project instance-carrier adoption remain separate.

## Settled decisions

- Only the receiving Scope Unit’s direct structural Parent may own its external Scope Delegation. Non-Project units have exactly one direct Parent; Project has none.
- Scope Delegation is admitted in every containing Scope Unit, including Project; the receiving unit must be non-Project.
- Shared Form Roles: Solution, Direct Policy and Approach Policy are RMEDO; Decision is MEDO only.
- Local Requirement Forms: Requirement for outcomes/constraints and existing Declaration families for model definitions; no new Rule default.

## Review boundary

The packet proposes source bodies and dispositions only. It does not edit Current/Draft carriers, allocate IDs, migrate instances, change Tier rules, alter Workflow instances, or claim runtime enforcement. All 37 pinned native carriers have verified hashes and actual Summary text; the two non-carrier analysis references are identified separately in `drafts.json`.
