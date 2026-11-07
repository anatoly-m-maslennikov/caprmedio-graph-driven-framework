# Scope Delegation proposal findings

Analysis only. The complete source pins, draft bodies, formal whitelist candidates, retirement order and open issues are in `drafts.json`.

## Consolidated model

- Propose one generic Scope Delegation Form Declaration, one Project-only Scope Unit Declaration Form owner and one Requirement/Declaration that establishes Scope Unit cardinality; add no Rule Form to the new model. Every non-Project Scope Unit receives exactly one external RMEDO Scope Delegation; it combines the current external structural declaration and assigned contribution. Keep the receiving Scope Unit as Main Subject and the allocator outside it as Container.
- The Scope Delegation carries the existing Name, stable ID, ordered state, optional Label, conditional `order.number`, and direct structural Parent. These values reuse existing Scope Unit properties; the proposal creates no new per-unit fields.
- Scope Delegation is admitted by default in every containing Scope Unit, including Project, so Project can declare children. Only the receiving unit must be non-Project; Project itself has no incoming Scope Delegation and retains its separate root Declaration. A Requirement Scope Delegation permits local Requirement, Method, Evaluation, Delivery and Operations Roles; each Method, Evaluation, Delivery or Operations Scope Delegation permits its matching local Role. Inherited constraints still apply and no complete Role packet is required.
- Local R defaults are settled: Requirement for required outcomes/constraints and existing Declaration families for model definitions; no Rule Form in the new model, with legacy Rule mapping deferred. Include Eval Case and Operations Workflow/Step/Action; Decision is the concrete M/D choice. Solution and Direct/Approach Policy are not added to local Role/Form whitelists until their shared Role range is settled; the shared MEDO vs RMEDO Form range is still pending.
- Retain a separate Project-root Requirement/Scope Unit Declaration for current CA-R-2640; the Project has no Scope Delegation and retains its Project Goal/root Axioms. The Project-root Draft already proposes ID `CA-SU-00`.

## Current conflicts and exact actions

- CA-R-2684@1 is the current owner of the Requirement/Scope Unit Declaration Form. Replace it with two distinct Form owners before retirement: one generic Scope Delegation Form declaration with a bound-instance RMEDO Role whitelist, and one minimal Project-only Scope Unit Declaration Form declaration. This preserves the Project root Form without creating per-Role Scope Delegation declarations.
- CA-R-2688@2 requires one external Requirement Declaration for every Scope Unit, including Project. Propose a new-identity Requirement/Declaration separating the root declaration from one non-Project Scope Delegation. Supersede the conflicting CA-R-2688@3 Draft; it still encodes the former `world` exception and Requirement-only model.
- CA-R-926@39 requires one-or-more direct-parent Goals per non-Project unit. Replace with the single Scope Delegation obligation and retire R926 after adoption. The Scope Delegation Claim must state the actual contribution, not fabricate a Goal. The new model uses Requirement for required outcomes/constraints and existing Declaration families for model definitions; it adds no Rule Form. Legacy Rule instances are mapped in a later migration.
- CA-M-461@2 and its @3 Draft still instruct authors to create Declarations, Goals and Scope Contracts. Propose a new-ID authoring successor preserving useful structural checks and Tier-0 internal realization; retire both old identity and stale Draft. The successor is a general Method/Direct Policy authoring method; Method is included in both MEDO and RMEDO candidates, and it requires no local adoption Atom.
- CA-R-924@37 currently lists R/Goal, R/Demand and Plan/Plan. Propose the same-ID/Summary successor as Requirement/Declaration, adding the five RMEDO/Scope Delegation Role/Form pairs; preserve the Plan actual-Claim-target qualification.
- Keep CA-R-2523 Scope Unit kind, CA-R-2524 Project kind, Name/order authorities, role meanings and the Project-root CA-R-2640 identity. CA-R-2526@4 currently requires exactly one ID on non-Project Scope Units while allowing Project ID zero. Its same-ID/Summary successor requires one ID on every Scope Unit; CA-R-2524@3 must also remove its explicit Project ID-zero constraint. This is a model-authority change. CA-R-2640@2 supplies the approved root value `CA-SU-00`, but its instance adoption is separate. Tier-0 and Scope Contract label conflicts remain with the Tier lane; do not duplicate those amendments here.

## Project-root Form and ID ownership

- The new Scope Delegation Form Declaration is one generic Form classifier with a bound-instance Role whitelist `[in (Requirement, Method, Evaluation, Delivery, Operations)]`; it is not five Form declarations. The existing Forms lane pattern supplies the selector and whitelist structure.
- Retain the existing `Scope Unit Declaration` Form only for the Project root with a separate minimal Requirement/Declaration Form owner. Its bound instance must resolve through HAS_ACTIVE_SUBJECT to a `Scope Unit/Project` target. The cardinality Requirement remains responsible for exactly one root declaration.
- The CA-R-2526 successor makes the Scope Unit ID a model requirement for every Scope Unit. Because CA-R-2524@3 formally requires Project ID cardinality zero, a same-ID/Summary CA-R-2524 successor removes that prohibition and leaves cardinality to R2526. This removes the model conflict without adopting or changing the R2640/R2524 instance carriers.

## Material unresolved decisions

1. **Allocator reach:** may only a Scope Unit's direct structural Parent delegate, or can another authorized external Scope Unit allocate? This determines Container eligibility and how R926's direct-parent constraint is replaced. The draft deliberately keeps structural Parent distinct from allocator.
2. **Shared Solution/Policy Role range:** MEDO vs RMEDO admission is pending. This controls local Role/Form whitelist entries for shared Solution/Policy Forms; it does not block M461’s Method/Direct Policy successor. The Project root remains the existing root-only Scope Unit Declaration, CA-R-2640.

## Review boundary

Pins include the Current declaration/cardinality rules, existing conflicting R2688 and M461 Drafts, Project-root Current/Draft, Scope Unit identity/order authorities, current Role declarations and their reviewed successor Drafts, and the A1328 proposal. The proposal preserves Current files and does not allocate IDs, create native Drafts, migrate instances, change Tier rules, alter Workflow instances or authorize runtime behavior.


Each concrete Scope Delegation Claim can enumerate typed model-entity/instance targets for local Atoms’ HAS_ACTIVE_SUBJECT links, plus Role/Form pairs. The local Atom must also be contained by the receiving Scope Unit through Header.Container-derived IS_CONTAINED_BY. Current HAS_ACTIVE_SUBJECT is not limited to Node targets, Relation endpoints allow declared entities or instances, and existing typed selectors include (Node, Node.**). This constrains resolved targets without comparing scalar Main Subject strings by prefix or adding an operator/property. It remains a model constraint proposal, not evidence of runtime enforcement.
